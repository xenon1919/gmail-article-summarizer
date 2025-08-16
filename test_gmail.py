#!/usr/bin/env python3
"""
Test script to demonstrate Gmail Article Summarizer functionality
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_configuration():
    """Test if Gmail configuration is set up"""
    print("🔍 Testing Gmail Article Summarizer Configuration...")
    
    # Check required environment variables
    gmail_user = os.getenv('GMAIL_USER')
    gmail_password = os.getenv('GMAIL_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')
    hf_token = os.getenv('HUGGINGFACE_TOKEN')
    
    print(f"📧 Gmail User: {'✅ Set' if gmail_user else '❌ Missing'}")
    print(f"🔑 Gmail Password: {'✅ Set' if gmail_password else '❌ Missing'}")
    print(f"📬 Recipient Email: {'✅ Set' if recipient_email else '❌ Missing'}")
    print(f"🤖 Hugging Face Token: {'✅ Set' if hf_token else '❌ Missing (optional)'}")
    
    if not all([gmail_user, gmail_password, recipient_email]):
        print("\n❌ Missing required Gmail configuration!")
        print("\n📝 Please add these to your .env file:")
        print("GMAIL_USER=your_gmail_address@gmail.com")
        print("GMAIL_PASSWORD=your_gmail_app_password_here")
        print("RECIPIENT_EMAIL=your_email@example.com")
        print("\n📧 Gmail App Password Setup:")
        print("1. Go to https://myaccount.google.com/security")
        print("2. Enable 2-Factor Authentication")
        print("3. Go to 'App passwords' (under 2-Factor Authentication)")
        print("4. Generate a new app password for 'Mail'")
        print("5. Use that 16-character password (NOT your regular password!)")
        return False
    
    print("\n✅ All required configuration is set!")
    print("🚀 Ready to run: python article_summarizer_gmail.py")
    return True

def show_email_preview():
    """Show what the email will look like"""
    print("\n📧 Email Preview:")
    print("=" * 50)
    print("Subject: 📰 Article Summaries - 2025-08-16")
    print("From: your_gmail_address@gmail.com")
    print("To: your_email@example.com")
    print("\n📧 Email Content:")
    print("- Beautiful HTML formatting")
    print("- Article titles with links")
    print("- AI-generated summaries")
    print("- Key insights and takeaways")
    print("- Relevance scores")
    print("- Author and date information")
    print("=" * 50)

if __name__ == "__main__":
    print("🚀 Gmail Article Summarizer Test")
    print("=" * 40)
    
    if test_configuration():
        show_email_preview()
        
        print("\n🎯 Next Steps:")
        print("1. Update your .env file with Gmail credentials")
        print("2. Run: python article_summarizer_gmail.py")
        print("3. Check your email for beautiful article summaries!")
        
        print("\n💡 Benefits of Gmail version:")
        print("✅ No Notion setup required")
        print("✅ Beautiful HTML emails")
        print("✅ Works with any email client")
        print("✅ Easy to share with others")
        print("✅ No database management")
        print("✅ Completely free!")
    else:
        print("\n❌ Please configure Gmail credentials first!")
