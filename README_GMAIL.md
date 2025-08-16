# 📧 Gmail Article Summarizer & Email Integration

A completely **FREE** Python solution that automatically collects articles from the web, summarizes them using free AI alternatives, and sends beautiful email summaries to your inbox.


This version uses:
- **Rule-based NLP** (completely free)
- **Hugging Face Inference API** (free tier)
- **Ollama** (local AI models, free)
- **Gmail SMTP** (free with your Gmail account)

## ✨ **Features**

- 🔍 **Smart RSS Monitoring**: Monitors multiple tech RSS feeds
- 🤖 **Free AI Summarization**: Uses multiple free AI services
- 📧 **Beautiful Email Delivery**: Sends formatted HTML emails
- 🎯 **Content Filtering**: Only processes relevant articles
- 📊 **Relevance Scoring**: Ranks articles by importance
- 🔄 **Automatic Workflow**: Runs end-to-end without manual intervention
- 💡 **Key Insights Extraction**: Identifies important points
- 🎯 **Topic Analysis**: Extracts main themes
- 📝 **Actionable Takeaways**: Provides next steps

## 🚀 **Quick Start (5 minutes)**

### 1. **Install Dependencies**
```bash
python setup_gmail.py
```

### 2. **Configure Gmail**
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Factor Authentication**
3. Go to **App passwords** (under 2-Factor Authentication)
4. Generate a new app password for **Mail**
5. Copy the 16-character password

### 3. **Set Up Environment**
Edit the `.env` file with your credentials:
```env
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_16_char_app_password
RECIPIENT_EMAIL=where_to_send@example.com
```

### 4. **Run the Script**
```bash
python article_summarizer_gmail.py
```

## 📧 **Gmail Setup Guide**

### **Step 1: Enable 2-Factor Authentication**
1. Visit [Google Account Security](https://myaccount.google.com/security)
2. Click **2-Step Verification**
3. Follow the setup process

### **Step 2: Generate App Password**
1. Go to **App passwords** (under 2-Step Verification)
2. Select **Mail** as the app
3. Click **Generate**
4. Copy the 16-character password

### **Step 3: Use App Password**
- **DO NOT** use your regular Gmail password
- **DO** use the 16-character app password
- This is more secure and required for SMTP access

## 🔧 **Configuration Options**

### **RSS Feeds**
Edit the `rss_feeds` list in the script:
```python
self.rss_feeds = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://feeds.arstechnica.com/arstechnica/index",
    "https://www.wired.com/feed/rss",
    "https://feeds.feedburner.com/TechCrunch/"
]
```

### **Keywords**
Customize the `keywords` list to filter relevant content:
```python
self.keywords = [
    "tech", "technology", "digital", "online", "web", "internet",
    "software", "app", "mobile", "computer", "data", "cloud",
    "startup", "business", "innovation", "future", "trends",
    "artificial intelligence", "machine learning", "data science"
]
```

### **Email Settings**
- **Subject**: Customizable email subject line
- **HTML Formatting**: Beautiful, responsive email design
- **Content Length**: Automatically truncated to fit email limits

## 🤖 **AI Summarization Options**

### **1. Hugging Face (Recommended)**
- **Free tier**: 30,000 requests/month
- **Model**: `facebook/bart-large-cnn`
- **Setup**: Get token from [Hugging Face](https://huggingface.co/settings/tokens)

### **2. Ollama (Local)**
- **Completely free**: Run locally
- **Models**: llama2, mistral, codellama
- **Setup**: Install [Ollama](https://ollama.ai/)

### **3. Rule-based (Fallback)**
- **Always works**: No API keys needed
- **Simple NLP**: Extractive summarization
- **Reliable**: Works offline

## 📊 **Email Output Format**

Each email contains:
- 📰 **Article Title** with link
- 👤 **Author** and **Date**
- 📝 **AI Summary** (2-3 sentences)
- 💡 **Key Insights** (important points)
- 🏷️ **Main Topics** (extracted themes)
- ✅ **Actionable Takeaways** (next steps)
- 📊 **Relevance Score** (1-10 rating)

## 🔄 **Automation Options**

### **Windows Task Scheduler**
1. Open **Task Scheduler**
2. Create **Basic Task**
3. Set trigger (daily, weekly, etc.)
4. Action: Start a program
5. Program: `python`
6. Arguments: `article_summarizer_gmail.py`

### **Linux/Mac Cron**
```bash
# Edit crontab
crontab -e

# Add daily run at 9 AM
0 9 * * * cd /path/to/script && python article_summarizer_gmail.py
```

### **GitHub Actions**
Create `.github/workflows/summarizer.yml`:
```yaml
name: Daily Article Summaries
on:
  schedule:
    - cron: '0 9 * * *'  # Daily at 9 AM
  workflow_dispatch:  # Manual trigger

jobs:
  summarize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements_gmail.txt
      - run: python article_summarizer_gmail.py
        env:
          GMAIL_USER: ${{ secrets.GMAIL_USER }}
          GMAIL_PASSWORD: ${{ secrets.GMAIL_PASSWORD }}
          RECIPIENT_EMAIL: ${{ secrets.RECIPIENT_EMAIL }}
```

## 🛠️ **Troubleshooting**

### **Gmail Authentication Issues**
- ✅ Use **App Password** (not regular password)
- ✅ Enable **2-Factor Authentication**
- ✅ Check **Less secure app access** is OFF
- ✅ Verify Gmail address is correct

### **No Articles Found**
- ✅ Check RSS feed URLs are accessible
- ✅ Adjust keywords to be less restrictive
- ✅ Verify internet connection
- ✅ Check if RSS feeds have recent content

### **Email Not Received**
- ✅ Check spam/junk folder
- ✅ Verify recipient email address
- ✅ Check Gmail app password is correct
- ✅ Look for error messages in logs

### **Content Extraction Issues**
- ✅ Some websites block scraping
- ✅ Try different RSS feeds
- ✅ Check if articles have substantial content
- ✅ Verify website structure hasn't changed

## 📈 **Performance Tips**

### **Optimize for Speed**
- Reduce `max_articles` for faster processing
- Use fewer RSS feeds
- Increase `time.sleep()` for rate limiting

### **Improve Quality**
- Add Hugging Face token for better summaries
- Install Ollama for local AI processing
- Fine-tune keywords for better filtering
- Adjust content length thresholds

### **Reduce Email Volume**
- Increase relevance score threshold
- Use more specific keywords
- Reduce number of RSS feeds
- Set higher content length minimum

## 🔒 **Security & Privacy**

### **Data Handling**
- ✅ No data stored permanently
- ✅ Articles processed in memory only
- ✅ No tracking or analytics
- ✅ Respects website robots.txt

### **Email Security**
- ✅ Uses Gmail's secure SMTP
- ✅ App passwords are more secure
- ✅ No sensitive data in emails
- ✅ Recipient list is configurable

### **API Usage**
- ✅ Free tier limits respected
- ✅ Rate limiting implemented
- ✅ Error handling for API failures
- ✅ Fallback to rule-based methods

## 📚 **Getting Help**

### **Common Issues**
1. **"Authentication failed"**: Use app password, not regular password
2. **"No articles found"**: Check RSS feeds and keywords
3. **"Email not sent"**: Verify Gmail credentials
4. **"Content too short"**: Adjust content length thresholds

### **Debug Mode**
Enable detailed logging:
```python
logging.basicConfig(level=logging.DEBUG)
```

### **Test Individual Components**
- Test Gmail connection separately
- Verify RSS feed accessibility
- Check content extraction manually
- Test summarization with sample text

## 🎯 **Customization Examples**

### **Add New RSS Feeds**
```python
self.rss_feeds.extend([
    "https://example.com/feed/",
    "https://blog.example.com/rss"
])
```

### **Custom Keywords**
```python
self.keywords = [
    "python", "javascript", "web development",
    "data science", "machine learning", "AI"
]
```

### **Modify Email Template**
Edit the `send_email()` method to customize:
- Email subject line
- HTML styling
- Content layout
- Information displayed

### **Adjust Processing**
```python
# Process more articles
summarizer.run_workflow(max_articles=10)

# Custom RSS feeds
summarizer.rss_feeds = ["https://custom-feed.com/rss"]

# Custom keywords
summarizer.keywords = ["your", "custom", "keywords"]
```

## 🚀 **Advanced Features**

### **Multiple Recipients**
Modify the email sending to support multiple recipients:
```python
recipients = ["user1@example.com", "user2@example.com"]
for recipient in recipients:
    # Send email to each recipient
```

### **Custom Email Templates**
Create different email templates for different content types:
```python
if "AI" in article_data['title']:
    template = "ai_template.html"
else:
    template = "general_template.html"
```

### **Database Integration**
Add database storage for tracking processed articles:
```python
# Store processed URLs to avoid duplicates
processed_urls = load_processed_urls()
if url not in processed_urls:
    # Process article
    save_processed_url(url)
```

---

## 🎉 **Success!**

You now have a fully automated, FREE article summarization system that:
- ✅ Monitors tech RSS feeds automatically
- ✅ Uses free AI for intelligent summarization
- ✅ Sends beautiful email summaries
- ✅ Works completely offline (with rule-based fallback)
- ✅ Requires no paid subscriptions
- ✅ Is easily customizable and extensible

**Happy summarizing! 📰✨**
