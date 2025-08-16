import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import os
from typing import List, Dict, Optional
import logging
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GmailArticleSummarizer:
    def __init__(self, gmail_user: str, gmail_password: str, recipient_email: str):
        """
        Initialize the Gmail Article Summarizer
        
        Args:
            gmail_user: Your Gmail address
            gmail_password: Your Gmail app password (not regular password)
            recipient_email: Email address to send summaries to
        """
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password
        self.recipient_email = recipient_email
        
        # RSS feeds to monitor
        self.rss_feeds = [
            "https://techcrunch.com/feed/",
            "https://www.theverge.com/rss/index.xml",
            "https://feeds.arstechnica.com/arstechnica/index",
            "https://www.wired.com/feed/rss",
            "https://feeds.feedburner.com/TechCrunch/"
        ]
        
        # Keywords to filter content (broader for more articles)
        self.keywords = [
            "tech", "technology", "digital", "online", "web", "internet",
            "software", "app", "mobile", "computer", "data", "cloud",
            "startup", "business", "innovation", "future", "trends",
            "artificial intelligence", "machine learning", "data science",
            "technology trends", "digital transformation", "innovation",
            "fintech", "healthtech", "edtech"
        ]
        
        # User agent for web scraping
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_article(self, url: str) -> Optional[Dict]:
        """
        Scrape an article from a given URL
        
        Args:
            url: The URL of the article to scrape
            
        Returns:
            Dictionary containing article data or None if failed
        """
        try:
            logger.info(f"Scraping article: {url}")
            
            # Fetch the webpage
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract article content (common selectors)
            title = self._extract_title(soup)
            content = self._extract_content(soup)
            author = self._extract_author(soup)
            date = self._extract_date(soup)
            
            if not title or not content:
                logger.warning(f"Could not extract title or content from {url}")
                return None
            
            # Clean content
            content = self._clean_content(content)
            
            # Check content length
            if len(content.split()) < 100:
                logger.warning(f"Content too short for {url}")
                return None
            
            return {
                'url': url,
                'title': title,
                'content': content,
                'author': author,
                'date': date,
                'scraped_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            return None

    def _extract_title(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract article title"""
        selectors = ['h1', 'h2', '.title', '.post-title', '.entry-title', '.article-title']
        for selector in selectors:
            element = soup.select_one(selector)
            if element and element.get_text().strip():
                return element.get_text().strip()
        return None

    def _extract_content(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract main article content"""
        selectors = [
            '.entry-content',  # TechCrunch, WordPress sites
            'main',            # General main content
            'article',         # Standard article tag
            '.content',        # Generic content
            '.post-body',      # Blog posts
            '.article-body',   # Article content
            '.post-content',   # Post content
            '.story-body',     # Story content
            '.wp-block-post-content',  # WordPress blocks
            '.article-content' # Article content
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                # Remove unwanted elements
                for unwanted in element.select('script, style, nav, header, footer, .ads, .advertisement, .wp-block-buttons, .wp-block-columns'):
                    unwanted.decompose()
                
                text = element.get_text().strip()
                if len(text) > 100:  # Ensure we got substantial content
                    return text
        
        # Fallback: look for any div with substantial text
        divs = soup.find_all('div')
        for div in divs:
            text = div.get_text().strip()
            if len(text) > 1000:  # Look for substantial content
                # Remove unwanted elements
                for unwanted in div.select('script, style, nav, header, footer'):
                    unwanted.decompose()
                return div.get_text().strip()
        
        return None

    def _extract_author(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract article author"""
        selectors = ['.author', '.byline', '.post-author', '.entry-author', '.writer']
        for selector in selectors:
            element = soup.select_one(selector)
            if element and element.get_text().strip():
                return element.get_text().strip()
        return None

    def _extract_date(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract article date"""
        selectors = ['.date', '.published-date', '.post-date', '.entry-date', 'time']
        for selector in selectors:
            element = soup.select_one(selector)
            if element and element.get_text().strip():
                return element.get_text().strip()
        return None

    def _clean_content(self, content: str) -> str:
        """Clean and format content"""
        # Remove extra whitespace
        content = ' '.join(content.split())
        # Remove common unwanted text
        unwanted_phrases = [
            'advertisement', 'sponsored', 'subscribe', 'newsletter',
            'privacy policy', 'terms of service', 'cookie policy'
        ]
        for phrase in unwanted_phrases:
            content = content.replace(phrase, '')
        return content

    def summarize_article_free(self, article_data: Dict) -> Optional[Dict]:
        """
        Summarize article using free AI alternatives
        
        Args:
            article_data: Dictionary containing article information
            
        Returns:
            Dictionary containing summary and insights
        """
        try:
            logger.info(f"Summarizing article: {article_data['title']}")
            
            # Try different free AI services
            summary_data = None
            
            # Option 1: Try Hugging Face Inference API (free tier)
            summary_data = self._try_huggingface(article_data)
            if summary_data:
                return {
                    'article_data': article_data,
                    'summary_data': summary_data,
                    'summarized_at': datetime.now().isoformat()
                }
            
            # Option 2: Try Ollama (if installed locally)
            summary_data = self._try_ollama(article_data)
            if summary_data:
                return {
                    'article_data': article_data,
                    'summary_data': summary_data,
                    'summarized_at': datetime.now().isoformat()
                }
            
            # Option 3: Fallback to rule-based summarization
            summary_data = self._rule_based_summary(article_data)
            
            return {
                'article_data': article_data,
                'summary_data': summary_data,
                'summarized_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error summarizing article: {str(e)}")
            # Fallback to rule-based summary
            try:
                fallback_summary = self._rule_based_summary(article_data)
                return {
                    'article_data': article_data,
                    'summary_data': fallback_summary,
                    'summarized_at': datetime.now().isoformat()
                }
            except Exception as fallback_error:
                logger.error(f"Fallback summarization also failed: {str(fallback_error)}")
                return None

    def _try_huggingface(self, article_data: Dict) -> Optional[Dict]:
        """Try Hugging Face Inference API (free tier)"""
        try:
            # You can get a free API token from https://huggingface.co/settings/tokens
            hf_token = os.getenv('HUGGINGFACE_TOKEN')
            if not hf_token:
                logger.info("No Hugging Face token found, skipping...")
                return None
            
            # Use a free summarization model
            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
            headers = {"Authorization": f"Bearer {hf_token}"}
            
            # Prepare content for summarization
            content = article_data['content'][:1000]  # Limit content length
            
            response = requests.post(API_URL, headers=headers, json={"inputs": content})
            if response.status_code == 200:
                summary = response.json()[0]['summary_text']
                
                # Extract key insights using simple NLP
                insights = self._extract_key_insights(article_data['content'])
                
                return {
                    'summary': summary,
                    'key_insights': insights,
                    'topics': self._extract_topics(article_data['content']),
                    'takeaways': self._extract_takeaways(article_data['content']),
                    'relevance_score': self._calculate_relevance_score(article_data['content'])
                }
            
        except Exception as e:
            logger.warning(f"Hugging Face API failed: {str(e)}")
        
        return None

    def _try_ollama(self, article_data: Dict) -> Optional[Dict]:
        """Try Ollama (local AI models)"""
        try:
            # Check if Ollama is running locally
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            if response.status_code == 200:
                # Use Ollama for summarization
                content = article_data['content'][:2000]
                
                ollama_response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama2",  # or any model you have installed
                        "prompt": f"Summarize this article in 2-3 sentences:\n\n{content}",
                        "stream": False
                    },
                    timeout=30
                )
                
                if ollama_response.status_code == 200:
                    summary = ollama_response.json()['response']
                    
                    return {
                        'summary': summary,
                        'key_insights': self._extract_key_insights(article_data['content']),
                        'topics': self._extract_topics(article_data['content']),
                        'takeaways': self._extract_takeaways(article_data['content']),
                        'relevance_score': self._calculate_relevance_score(article_data['content'])
                    }
                    
        except Exception as e:
            logger.info("Ollama not available or failed")
        
        return None

    def _rule_based_summary(self, article_data: Dict) -> Dict:
        """
        Create a summary using rule-based NLP techniques
        This is completely free and doesn't require any API keys
        """
        content = article_data['content']
        words = content.split()
        
        # Simple extractive summarization
        sentences = content.split('. ')
        if len(sentences) > 3:
            # Take first, middle, and last sentences
            summary = '. '.join([sentences[0], sentences[len(sentences)//2], sentences[-1]])
        else:
            summary = content[:500] + "..." if len(content) > 500 else content
        
        return {
            'summary': summary,
            'key_insights': self._extract_key_insights(content),
            'topics': self._extract_topics(content),
            'takeaways': self._extract_takeaways(content),
            'relevance_score': self._calculate_relevance_score(content)
        }

    def _extract_key_insights(self, content: str) -> str:
        """Extract key insights using simple NLP"""
        # Look for sentences with key phrases
        sentences = content.split('. ')
        insights = []
        
        key_phrases = [
            'important', 'key', 'significant', 'major', 'breakthrough',
            'innovation', 'discovery', 'finding', 'result', 'conclusion'
        ]
        
        for sentence in sentences[:10]:  # Check first 10 sentences
            if any(phrase in sentence.lower() for phrase in key_phrases):
                insights.append(sentence.strip())
            if len(insights) >= 3:
                break
        
        if not insights:
            # Fallback: take first few sentences
            insights = sentences[:3]
        
        return '\n• '.join([''] + insights)

    def _extract_topics(self, content: str) -> str:
        """Extract main topics from content"""
        # Simple topic extraction based on frequency
        words = content.lower().split()
        word_freq = {}
        
        # Count word frequency (excluding common words)
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        
        for word in words:
            if len(word) > 3 and word not in common_words:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Get top 5 most frequent words
        topics = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        return ', '.join([topic[0].title() for topic in topics])

    def _extract_takeaways(self, content: str) -> str:
        """Extract actionable takeaways"""
        # Look for action-oriented sentences
        sentences = content.split('. ')
        takeaways = []
        
        action_words = ['should', 'must', 'need', 'will', 'can', 'could', 'would', 'recommend', 'suggest']
        
        for sentence in sentences:
            if any(word in sentence.lower() for word in action_words):
                takeaways.append(sentence.strip())
            if len(takeaways) >= 3:
                break
        
        if not takeaways:
            takeaways = ["Review the content for key insights", "Consider the implications for your field", "Share relevant findings with your team"]
        
        return '\n• '.join([''] + takeaways)

    def _calculate_relevance_score(self, content: str) -> int:
        """Calculate relevance score based on keyword density"""
        content_lower = content.lower()
        score = 5  # Base score
        
        # Check keyword density
        for keyword in self.keywords:
            if keyword in content_lower:
                score += 1
        
        # Check content length (longer articles get higher scores)
        if len(content.split()) > 1000:
            score += 1
        if len(content.split()) > 2000:
            score += 1
        
        return min(score, 10)  # Cap at 10

    def send_email(self, summaries: List[Dict]) -> bool:
        """
        Send article summaries via Gmail
        
        Args:
            summaries: List of summary dictionaries
            
        Returns:
            True if successful, False otherwise
        """
        try:
            logger.info(f"Sending email with {len(summaries)} article summaries")
            
            # Create email content
            subject = f"📰 Article Summaries - {datetime.now().strftime('%Y-%m-%d')}"
            
            # Build HTML email content
            html_content = f"""
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .header {{ background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
                    .article {{ border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin-bottom: 20px; background-color: #fff; }}
                    .title {{ color: #2c3e50; font-size: 18px; font-weight: bold; margin-bottom: 10px; }}
                    .meta {{ color: #7f8c8d; font-size: 14px; margin-bottom: 15px; }}
                    .summary {{ background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; }}
                    .insights {{ margin-bottom: 15px; }}
                    .topics {{ color: #3498db; font-weight: bold; }}
                    .score {{ color: #e74c3c; font-weight: bold; }}
                    .url {{ color: #3498db; text-decoration: none; }}
                    .url:hover {{ text-decoration: underline; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>📰 Daily Article Summaries</h1>
                    <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                    <p>Found {len(summaries)} relevant articles from tech RSS feeds</p>
                </div>
            """
            
            for i, summary in enumerate(summaries, 1):
                article_data = summary['article_data']
                summary_data = summary['summary_data']
                
                html_content += f"""
                <div class="article">
                    <div class="title">{i}. {article_data['title']}</div>
                    <div class="meta">
                        <strong>Author:</strong> {article_data.get('author', 'Unknown')} | 
                        <strong>Date:</strong> {article_data.get('date', 'Unknown')} | 
                        <strong>Relevance Score:</strong> <span class="score">{summary_data['relevance_score']}/10</span>
                    </div>
                    
                    <div class="summary">
                        <strong>Summary:</strong><br>
                        {summary_data['summary']}
                    </div>
                    
                    <div class="insights">
                        <strong>Key Insights:</strong><br>
                        {summary_data['key_insights']}
                    </div>
                    
                    <div class="insights">
                        <strong>Main Topics:</strong> <span class="topics">{summary_data['topics']}</span>
                    </div>
                    
                    <div class="insights">
                        <strong>Actionable Takeaways:</strong><br>
                        {summary_data['takeaways']}
                    </div>
                    
                    <div class="meta">
                        <a href="{article_data['url']}" class="url" target="_blank">📖 Read Full Article</a>
                    </div>
                </div>
                """
            
            html_content += """
            </body>
            </html>
            """
            
            # Create email message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.gmail_user
            msg['To'] = self.recipient_email
            
            # Attach HTML content
            html_part = MIMEText(html_content, 'html')
            msg.attach(html_part)
            
            # Send email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(self.gmail_user, self.gmail_password)
                server.send_message(msg)
            
            logger.info(f"Successfully sent email to {self.recipient_email}")
            return True
            
        except Exception as e:
            logger.error(f"Error sending email: {str(e)}")
            return False

    def get_articles_from_rss(self, rss_url: str, max_articles: int = 5) -> List[str]:
        """
        Get article URLs from RSS feed
        
        Args:
            rss_url: URL of the RSS feed
            max_articles: Maximum number of articles to return
            
        Returns:
            List of article URLs
        """
        try:
            logger.info(f"Fetching RSS feed: {rss_url}")
            
            response = requests.get(rss_url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'xml')
            
            # Find all item tags (articles)
            items = soup.find_all('item')[:max_articles]
            
            urls = []
            for item in items:
                link = item.find('link')
                if link and link.get_text():
                    url = link.get_text().strip()
                    # Check if URL contains any of our keywords
                    if any(keyword.lower() in url.lower() for keyword in self.keywords):
                        urls.append(url)
            
            logger.info(f"Found {len(urls)} relevant articles from RSS feed")
            return urls
            
        except Exception as e:
            logger.error(f"Error fetching RSS feed {rss_url}: {str(e)}")
            return []

    def run_workflow(self, max_articles: int = 10):
        """
        Run the complete workflow
        
        Args:
            max_articles: Maximum number of articles to process
        """
        logger.info("Starting Gmail Article Summarizer workflow")
        
        all_urls = []
        
        # Get URLs from RSS feeds
        for rss_feed in self.rss_feeds:
            urls = self.get_articles_from_rss(rss_feed, max_articles // len(self.rss_feeds))
            all_urls.extend(urls)
        
        # Remove duplicates
        all_urls = list(set(all_urls))
        logger.info(f"Total unique articles found: {len(all_urls)}")
        
        processed_count = 0
        success_count = 0
        summaries = []
        
        for url in all_urls[:max_articles]:
            try:
                # Scrape the article
                article_data = self.scrape_article(url)
                if not article_data:
                    continue
                
                # Summarize the article (using free methods)
                logger.info(f"Starting summarization for: {url}")
                summary_data = self.summarize_article_free(article_data)
                
                if not summary_data:
                    logger.warning(f"Failed to summarize article: {url}")
                    continue
                
                # Validate summary data structure
                if 'article_data' not in summary_data or 'summary_data' not in summary_data:
                    logger.error(f"Invalid summary data structure for: {url}")
                    continue
                
                # Add to summaries list
                summaries.append(summary_data)
                success_count += 1
                processed_count += 1
                
                # Rate limiting
                time.sleep(2)
                
            except Exception as e:
                logger.error(f"Error processing {url}: {str(e)}")
                continue
        
        # Send email with all summaries
        if summaries:
            if self.send_email(summaries):
                logger.info(f"Successfully sent {len(summaries)} summaries via email")
            else:
                logger.error("Failed to send email")
        else:
            logger.info("No summaries to send")
        
        logger.info(f"Workflow completed. Processed: {processed_count}, Success: {success_count}")

def main():
    """Main function to run the workflow"""
    
    # Load configuration from environment variables
    gmail_user = os.getenv('GMAIL_USER')
    gmail_password = os.getenv('GMAIL_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')
    
    if not all([gmail_user, gmail_password, recipient_email]):
        print("❌ Missing required environment variables!")
        print("Please set:")
        print("- GMAIL_USER (your Gmail address)")
        print("- GMAIL_PASSWORD (your Gmail app password)")
        print("- RECIPIENT_EMAIL (where to send summaries)")
        print("\nOptional (for better AI summaries):")
        print("- HUGGINGFACE_TOKEN (get free from https://huggingface.co/settings/tokens)")
        print("\nNote: This version works completely FREE without any AI API keys!")
        print("\n📧 Setup Gmail App Password:")
        print("1. Go to Google Account settings")
        print("2. Enable 2-factor authentication")
        print("3. Generate an App Password for this script")
        print("4. Use that password (not your regular Gmail password)")
        return
    
    # Create the summarizer
    summarizer = GmailArticleSummarizer(gmail_user, gmail_password, recipient_email)
    
    # Run the workflow
    summarizer.run_workflow(max_articles=5)

if __name__ == "__main__":
    main()
