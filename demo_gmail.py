#!/usr/bin/env python3
"""
Demo script showing Gmail Article Summarizer functionality
"""
from datetime import datetime

def create_sample_summaries():
    """Create sample article summaries for demo"""
    return [
        {
            'article_data': {
                'title': 'SpaceX reveals why the last two Starships failed as another launch draws near',
                'author': 'Eric Berger',
                'date': 'August 15, 2025',
                'url': 'https://arstechnica.com/space/2025/08/spacex-reveals-why-the-last-two-starships-failed-as-another-launch-draws-near/'
            },
            'summary_data': {
                'summary': 'SpaceX has announced the launch is scheduled for no earlier than next Sunday, August 24. Engineers conducted extensive analysis of the previous failures and implemented key improvements to the rocket design.',
                'key_insights': '• SpaceX identified specific technical issues in previous launches\n• New safety measures have been implemented\n• Launch window opens August 24',
                'topics': 'Spacex, Starship, Launch, Rocket, Space',
                'takeaways': '• Monitor the upcoming launch for success indicators\n• Consider implications for space industry\n• Follow SpaceX\'s technical improvements',
                'relevance_score': 9
            }
        },
        {
            'article_data': {
                'title': 'Winklevoss twins\' crypto company Gemini files for IPO',
                'author': 'Kirsten Korosec',
                'date': 'August 15, 2025',
                'url': 'https://techcrunch.com/2025/08/15/winklevoss-twins-crypto-company-gemini-files-for-ipo/'
            },
            'summary_data': {
                'summary': 'Gemini Space Station Inc. plans to list on the Nasdaq Global Select Market under the symbol GEMI. The company aims to raise significant capital through this public offering.',
                'key_insights': '• Another crypto company heading to public markets\n• Gemini plans Nasdaq listing under GEMI symbol\n• Significant capital raise expected',
                'topics': 'Crypto, Gemini, IPO, Nasdaq, Finance',
                'takeaways': '• Watch for crypto market impact\n• Consider investment opportunities\n• Monitor regulatory developments',
                'relevance_score': 8
            }
        },
        {
            'article_data': {
                'title': 'Top 10 AI Tools That Will Transform Your Content Creation in 2025',
                'author': 'Adil Ahmad',
                'date': 'January 2, 2025',
                'url': 'https://techncruncher.blogspot.com/2025/01/top-10-ai-tools-that-will-transform.html'
            },
            'summary_data': {
                'summary': 'The digital landscape has evolved dramatically, and AI tools have become essential for creators. This comprehensive guide covers the most innovative AI solutions for content creation.',
                'key_insights': '• AI tools are revolutionizing content creation\n• 10 key tools identified for 2025\n• Significant productivity improvements possible',
                'topics': 'AI, Content, Creation, Tools, Technology',
                'takeaways': '• Evaluate AI tools for your workflow\n• Invest in productivity improvements\n• Stay updated on AI trends',
                'relevance_score': 10
            }
        }
    ]

def generate_email_html(summaries):
    """Generate HTML email content"""
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; }}
            .header {{ background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px; text-align: center; }}
            .article {{ border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin-bottom: 20px; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            .title {{ color: #2c3e50; font-size: 18px; font-weight: bold; margin-bottom: 10px; }}
            .meta {{ color: #7f8c8d; font-size: 14px; margin-bottom: 15px; }}
            .summary {{ background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 4px solid #3498db; }}
            .insights {{ margin-bottom: 15px; }}
            .topics {{ color: #3498db; font-weight: bold; }}
            .score {{ color: #e74c3c; font-weight: bold; }}
            .url {{ color: #3498db; text-decoration: none; }}
            .url:hover {{ text-decoration: underline; }}
            .footer {{ text-align: center; margin-top: 30px; color: #7f8c8d; font-size: 12px; }}
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
        <div class="footer">
            <p>🤖 Powered by FREE AI Summarization</p>
            <p>📧 Sent via Gmail Article Summarizer</p>
        </div>
    </body>
    </html>
    """
    
    return html_content

def save_demo_email():
    """Save demo email as HTML file"""
    summaries = create_sample_summaries()
    html_content = generate_email_html(summaries)
    
    with open('demo_email.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Demo email saved as 'demo_email.html'")
    print("📧 Open this file in your browser to see the email format!")

def main():
    """Main demo function"""
    print("🚀 Gmail Article Summarizer Demo")
    print("=" * 40)
    
    print("📧 Creating sample email with 3 article summaries...")
    save_demo_email()
    
    print("\n📊 Sample Articles:")
    summaries = create_sample_summaries()
    for i, summary in enumerate(summaries, 1):
        title = summary['article_data']['title']
        score = summary['summary_data']['relevance_score']
        print(f"{i}. {title[:60]}... (Score: {score}/10)")
    
    print("\n🎯 To use the real Gmail version:")
    print("1. Add to your .env file:")
    print("   GMAIL_USER=your_gmail_address@gmail.com")
    print("   GMAIL_PASSWORD=your_gmail_app_password_here")
    print("   RECIPIENT_EMAIL=your_email@example.com")
    print("2. Run: python article_summarizer_gmail.py")
    print("3. Check your email for real article summaries!")
    
    print("\n💡 Benefits:")
    print("✅ Beautiful HTML emails")
    print("✅ AI-powered summaries")
    print("✅ Key insights extraction")
    print("✅ Relevance scoring")
    print("✅ Completely free!")
    print("✅ No Notion setup required")

if __name__ == "__main__":
    main()
