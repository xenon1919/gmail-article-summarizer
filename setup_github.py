#!/usr/bin/env python3
"""
GitHub Setup Script for Gmail Article Summarizer
Helps initialize the repository for GitHub
"""
import os
import subprocess
import sys

def check_git_installed():
    """Check if git is installed"""
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def initialize_git_repo():
    """Initialize git repository"""
    print("🔧 Initializing Git repository...")
    
    try:
        # Initialize git repository
        subprocess.run(['git', 'init'], check=True)
        print("✅ Git repository initialized")
        
        # Add all files
        subprocess.run(['git', 'add', '.'], check=True)
        print("✅ Files added to staging area")
        
        # Initial commit
        subprocess.run(['git', 'commit', '-m', 'feat: initial commit - Gmail Article Summarizer'], check=True)
        print("✅ Initial commit created")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error initializing git: {e}")
        return False

def show_github_instructions():
    """Show instructions for setting up GitHub"""
    print("\n🚀 GitHub Setup Instructions:")
    print("=" * 50)
    print("1. Go to GitHub.com and sign in")
    print("2. Click the '+' icon → 'New repository'")
    print("3. Repository name: 'gmail-article-summarizer'")
    print("4. Description: 'Free AI-powered article summarizer that sends daily tech news to Gmail'")
    print("5. Make it Public (recommended)")
    print("6. DO NOT initialize with README (we already have one)")
    print("7. Click 'Create repository'")
    print("8. Copy the repository URL")
    
    print("\n📋 After creating the repository, run these commands:")
    print("=" * 50)
    print("git remote add origin https://github.com/YOUR_USERNAME/gmail-article-summarizer.git")
    print("git branch -M main")
    print("git push -u origin main")
    
    print("\n🎯 Repository Features:")
    print("=" * 30)
    print("✅ README.md - Project documentation")
    print("✅ LICENSE - MIT License")
    print("✅ .gitignore - Excludes sensitive files")
    print("✅ CONTRIBUTING.md - Contribution guidelines")
    print("✅ env.example - Environment template")
    print("✅ setup_github.py - This setup script")

def show_repository_structure():
    """Show the repository structure"""
    print("\n📁 Repository Structure:")
    print("=" * 30)
    
    files = [
        ("📄 README.md", "Main project documentation"),
        ("📄 LICENSE", "MIT License"),
        ("📄 .gitignore", "Git ignore rules"),
        ("📄 CONTRIBUTING.md", "Contribution guidelines"),
        ("📄 env.example", "Environment variables template"),
        ("📄 article_summarizer_gmail.py", "Main script"),
        ("📄 setup_gmail.py", "Setup script"),
        ("📄 requirements_gmail.txt", "Python dependencies"),
        ("📄 README_GMAIL.md", "Detailed documentation"),
        ("📄 AUTOMATION_GUIDE.md", "Automation guide"),
        ("📄 manual_run.py", "Manual execution script"),
        ("📄 run_summarizer.bat", "Windows batch file"),
        ("📄 run_summarizer.ps1", "PowerShell script"),
        ("📄 setup_automation.py", "Automation setup"),
        ("📄 demo_gmail.py", "Demo script"),
        ("📄 test_gmail.py", "Configuration test"),
        ("📄 setup_github.py", "GitHub setup script")
    ]
    
    for file_name, description in files:
        print(f"{file_name:<25} {description}")

def show_next_steps():
    """Show next steps after GitHub setup"""
    print("\n🎯 Next Steps After GitHub Setup:")
    print("=" * 40)
    print("1. ✅ Push code to GitHub")
    print("2. 📝 Add repository description")
    print("3. 🏷️ Add topics: python, ai, gmail, rss, automation")
    print("4. 📋 Create issues for future features")
    print("5. 🌟 Star your own repository")
    print("6. 📢 Share with the community!")
    
    print("\n💡 Pro Tips:")
    print("=" * 20)
    print("🔗 Add a link to your repository in your portfolio")
    print("📊 Enable GitHub Insights to track repository stats")
    print("🤝 Encourage others to contribute")
    print("📝 Keep documentation updated")
    print("🔒 Never commit .env file (it's in .gitignore)")

def main():
    """Main setup function"""
    print("🚀 GitHub Repository Setup")
    print("=" * 40)
    print("📧 Setting up Gmail Article Summarizer for GitHub")
    
    # Check if git is installed
    if not check_git_installed():
        print("❌ Git is not installed!")
        print("Please install Git from: https://git-scm.com/")
        return
    
    # Show repository structure
    show_repository_structure()
    
    # Initialize git repository
    if initialize_git_repo():
        print("\n✅ Git repository ready!")
    else:
        print("\n❌ Failed to initialize git repository")
        return
    
    # Show GitHub instructions
    show_github_instructions()
    
    # Show next steps
    show_next_steps()
    
    print("\n🎉 Your project is ready for GitHub!")
    print("📧 Share your free article summarizer with the world!")

if __name__ == "__main__":
    main()
