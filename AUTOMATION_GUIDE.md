# 🚀 Gmail Article Summarizer - Automation Guide

## ✅ **What We've Set Up:**

### **📁 Automation Files Created:**
- `run_summarizer.bat` - Windows batch file for easy execution
- `run_summarizer.ps1` - PowerShell script with logging
- `manual_run.py` - Python script for on-demand runs
- `setup_automation.py` - Setup script for automation

### **📧 Real-Time Article Sources:**
- **TechCrunch** - Latest tech news and startups
- **The Verge** - Technology, science, and culture
- **Ars Technica** - Tech analysis and reviews
- **Wired** - Technology and business news
- **TechCrunch Feedburner** - Additional tech content

## 🎯 **How to Set Up Daily Automation:**

### **Option 1: Windows Task Scheduler (Recommended)**

1. **Open Task Scheduler**
   - Press `Win + R`, type `taskschd.msc`, press Enter
   - Or search "Task Scheduler" in Start menu

2. **Create Basic Task**
   - Click "Create Basic Task" in right panel
   - Name: `Gmail Article Summarizer`
   - Description: `Daily tech article summaries via email`

3. **Set Trigger**
   - Trigger: `Daily`
   - Start time: `9:00 AM` (or your preferred time)
   - Recur every: `1 days`

4. **Set Action**
   - Action: `Start a program`
   - Program/script: `powershell.exe`
   - Add arguments: `-ExecutionPolicy Bypass -File`
   - Add arguments: `"C:\Users\rishi\Downloads\Langflow Workflow\run_summarizer.ps1"`

5. **Configure Properties**
   - Check "Open properties dialog"
   - General tab: Check "Run whether user is logged on or not"
   - Conditions tab: Uncheck "Start only if computer is on AC power"
   - Settings tab: Check "Allow task to be run on demand"

### **Option 2: Manual Runs**

```bash
# Run manually anytime
python manual_run.py

# Or use the batch file
run_summarizer.bat

# Or use PowerShell
.\run_summarizer.ps1
```

## 📅 **Advanced Scheduling Options:**

### **Multiple Times Per Day:**
- **9 AM** - Morning tech news
- **2 PM** - Afternoon updates
- **6 PM** - Evening summaries

### **Custom Schedules:**
- **Weekdays only** - Monday to Friday
- **Weekends only** - Saturday and Sunday
- **Business hours** - 9 AM to 5 PM

### **Conditional Runs:**
- Only when computer is idle
- Only when connected to internet
- Only when on AC power

## 🧪 **Testing Your Setup:**

### **1. Test Manual Run:**
```bash
python manual_run.py
```

### **2. Test Batch File:**
- Double-click `run_summarizer.bat`

### **3. Test PowerShell Script:**
- Right-click `run_summarizer.ps1` → "Run with PowerShell"

### **4. Check Logs:**
- View `summarizer_log.txt` for detailed execution logs

## 📊 **What You'll Get Daily:**

### **📧 Email Content:**
- **Article titles** with direct links
- **AI-generated summaries** (2-3 sentences)
- **Key insights** and important points
- **Main topics** and themes
- **Actionable takeaways** and next steps
- **Relevance scores** (1-10 rating)
- **Author and date** information

### **🤖 AI Processing:**
- **Hugging Face** (free tier) - High-quality summaries
- **Rule-based NLP** - Reliable fallback
- **Ollama** (optional) - Local AI models

## 🔧 **Troubleshooting:**

### **Common Issues:**
1. **"Authentication failed"** - Check Gmail app password
2. **"No articles found"** - Check RSS feeds and keywords
3. **"Email not sent"** - Verify Gmail credentials
4. **"Task not running"** - Check Task Scheduler settings

### **Debug Steps:**
1. Check `summarizer_log.txt` for errors
2. Test manual run first
3. Verify `.env` file configuration
4. Check internet connection

## 💡 **Pro Tips:**

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

## 🎉 **Success Checklist:**

- ✅ Gmail credentials configured
- ✅ Hugging Face token set up
- ✅ Automation files created
- ✅ Manual run tested successfully
- ✅ Task Scheduler configured (optional)
- ✅ Daily email summaries working

## 📈 **Next Steps:**

1. **Set up Task Scheduler** for daily automation
2. **Test the automation** with manual runs
3. **Monitor your email** for daily summaries
4. **Customize settings** as needed
5. **Share with colleagues** if desired

---

**🎯 You now have a fully automated, real-time article summarization system that delivers fresh tech news to your inbox every day! 📰✨**
