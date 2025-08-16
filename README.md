# 📧 Gmail Article Summarizer

A **completely FREE** Python solution that automatically collects articles from the web, summarizes them using free AI alternatives, and sends beautiful email summaries to your inbox.

This project uses:
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
HUGGINGFACE_TOKEN=your_huggingface_token_here
```

### 4. **Run the Script**
```bash
python article_summarizer_gmail.py
```

## 📧 **Real-Time Article Sources**

The script monitors these live RSS feeds:
- **TechCrunch** - Latest tech news and startups
- **The Verge** - Technology, science, and culture
- **Ars Technica** - Tech analysis and reviews
- **Wired** - Technology and business news
- **TechCrunch Feedburner** - Additional tech content

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

## 🔄 **Automation Setup**

### **Windows Task Scheduler**
1. Open **Task Scheduler**
2. Create **Basic Task**
3. Set trigger (daily, weekly, etc.)
4. Action: Start a program
5. Program: `python`
6. Arguments: `article_summarizer_gmail.py`

### **Manual Runs**
```bash
# Run manually anytime
python manual_run.py

# Or use the batch file
run_summarizer.bat

# Or use PowerShell
.\run_summarizer.ps1
```

## 📁 **Project Structure**

```
📧 Gmail Article Summarizer/
├── 📄 article_summarizer_gmail.py    # Main script
├── 📄 setup_gmail.py                 # Setup script
├── 📄 requirements_gmail.txt         # Dependencies
├── 📄 README_GMAIL.md               # Detailed documentation
├── 📄 AUTOMATION_GUIDE.md           # Automation guide
├── 📄 manual_run.py                 # Manual execution script
├── 📄 run_summarizer.bat            # Windows batch file
├── 📄 run_summarizer.ps1            # PowerShell script
├── 📄 setup_automation.py           # Automation setup
├── 📄 demo_gmail.py                 # Demo script
├── 📄 demo_email.html               # Sample email
├── 📄 test_gmail.py                 # Configuration test
└── 📄 .env                          # Environment variables
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

## 💡 **Pro Tips**

### **Optimization:**
- Start with **daily runs at 9 AM**
- Monitor log files for any issues
- Adjust timing based on your schedule
- Use manual runs for immediate updates

### **Customization:**
- Modify RSS feeds in `article_summarizer_gmail.py`
- Adjust keywords for different topics
- Change email template styling
- Add more recipients

## 🎉 **Success!**

You now have a fully automated, FREE article summarization system that:
- ✅ Monitors tech RSS feeds automatically
- ✅ Uses free AI for intelligent summarization
- ✅ Sends beautiful email summaries
- ✅ Works completely offline (with rule-based fallback)
- ✅ Requires no paid subscriptions
- ✅ Is easily customizable and extensible

**Happy summarizing! 📰✨**
