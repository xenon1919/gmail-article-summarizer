#!/usr/bin/env python3
"""
Setup script for Gmail Article Summarizer
Installs dependencies and helps configure the environment
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_gmail.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please install manually:")
        print("pip install -r requirements_gmail.txt")
        return False
    return True

def create_env_file():
    """Create .env file template"""
    env_content = """# Gmail Article Summarizer Configuration
# Add your Gmail credentials here

# Your Gmail address
GMAIL_USER=your_gmail_address@gmail.com

# Your Gmail App Password (NOT your regular password!)
# Get this from: https://myaccount.google.com/apppasswords
GMAIL_PASSWORD=your_gmail_app_password_here

# Email address to send summaries to
RECIPIENT_EMAIL=your_email@example.com

# Optional: Hugging Face Token for better AI summaries (free from https://huggingface.co/settings/tokens)
# HUGGINGFACE_TOKEN=your_huggingface_token_here
"""
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(env_content)
        print("📝 Created .env file template")
        print("⚠️  Please edit .env file with your actual Gmail credentials!")
    else:
        print("📝 .env file already exists")

def main():
    """Main setup function"""
    print("🚀 Setting up Gmail Article Summarizer...")
    print("📧 This version sends article summaries via Gmail!")
    print("💰 Works completely FREE without OpenAI!")
    
    if not install_requirements():
        return
    
    create_env_file()
    
    print("\n🎯 Setup complete! Next steps:")
    print("1. Edit .env file with your Gmail credentials")
    print("2. Set up Gmail App Password (see instructions below)")
    print("3. Run: python article_summarizer_gmail.py")
    
    print("\n📧 Gmail App Password Setup:")
    print("1. Go to https://myaccount.google.com/security")
    print("2. Enable 2-Factor Authentication if not already enabled")
    print("3. Go to 'App passwords' (under 2-Factor Authentication)")
    print("4. Generate a new app password for 'Mail'")
    print("5. Use that 16-character password in your .env file")
    print("   (NOT your regular Gmail password!)")
    
    print("\n💡 Optional: Get a free Hugging Face token for better AI summaries")
    print("   Visit: https://huggingface.co/settings/tokens")
    
    print("\n📚 For detailed setup instructions, see README_GMAIL.md")

if __name__ == "__main__":
    main()
