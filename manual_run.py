#!/usr/bin/env python3
"""
Manual Run Script for Gmail Article Summarizer
"""
import subprocess
import sys
import os

def run_summarizer():
    print("🚀 Running Gmail Article Summarizer...")
    print("=" * 40)
    
    try:
        # Change to script directory
        os.chdir(r"C:\Users\rishi\Downloads\Langflow Workflow")
        
        # Run the main script
        result = subprocess.run([sys.executable, "article_summarizer_gmail.py"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Article summarizer completed successfully!")
            print("📧 Check your email for the latest summaries!")
        else:
            print("❌ Error running article summarizer:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    run_summarizer()
