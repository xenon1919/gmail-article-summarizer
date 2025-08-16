#!/usr/bin/env python3
"""
Setup script for automatic daily runs of Gmail Article Summarizer
Helps configure Windows Task Scheduler for continuous real-time updates
"""
import os
import subprocess
import sys
from datetime import datetime

def create_batch_file():
    """Create a batch file to run the script"""
    batch_content = f"""@echo off
cd /d "{os.getcwd()}"
python article_summarizer_gmail.py
pause
"""
    
    with open('run_summarizer.bat', 'w', encoding='utf-8') as f:
        f.write(batch_content)
    
    print("✅ Created 'run_summarizer.bat' file")
    return True

def create_powershell_script():
    """Create a PowerShell script for better automation"""
    ps_content = f"""# Gmail Article Summarizer Automation Script
# This script runs the article summarizer and logs the results

$scriptPath = "{os.getcwd()}"
$logFile = "$scriptPath\\summarizer_log.txt"

# Change to script directory
Set-Location $scriptPath

# Log start time
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
"[$timestamp] Starting Gmail Article Summarizer..." | Out-File -FilePath $logFile -Append

try {{
    # Run the Python script
    python article_summarizer_gmail.py 2>&1 | Out-File -FilePath $logFile -Append
    
    # Log completion
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$timestamp] Gmail Article Summarizer completed successfully" | Out-File -FilePath $logFile -Append
}}
catch {{
    # Log any errors
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$timestamp] Error running Gmail Article Summarizer: $_" | Out-File -FilePath $logFile -Append
}}
"""
    
    with open('run_summarizer.ps1', 'w', encoding='utf-8') as f:
        f.write(ps_content)
    
    print("✅ Created 'run_summarizer.ps1' PowerShell script")
    return True

def show_windows_task_scheduler_instructions():
    """Show instructions for Windows Task Scheduler"""
    print("\n📅 Windows Task Scheduler Setup:")
    print("=" * 50)
    print("1. Open 'Task Scheduler' (search in Start menu)")
    print("2. Click 'Create Basic Task' in the right panel")
    print("3. Name: 'Gmail Article Summarizer'")
    print("4. Description: 'Daily tech article summaries via email'")
    print("5. Trigger: Daily")
    print("6. Start time: 9:00 AM (or your preferred time)")
    print("7. Action: Start a program")
    print("8. Program/script: powershell.exe")
    print("9. Add arguments: -ExecutionPolicy Bypass -File")
    print(f"10. Add arguments: \"{os.path.join(os.getcwd(), 'run_summarizer.ps1')}\"")
    print("11. Start in: Leave blank")
    print("12. Finish and check 'Open properties dialog'")
    print("13. In Properties:")
    print("    - General tab: Check 'Run whether user is logged on or not'")
    print("    - Conditions tab: Uncheck 'Start the task only if computer is on AC power'")
    print("    - Settings tab: Check 'Allow task to be run on demand'")
    print("14. Click OK and enter your Windows password")

def show_advanced_scheduling_options():
    """Show advanced scheduling options"""
    print("\n⚙️ Advanced Scheduling Options:")
    print("=" * 40)
    print("📅 Multiple Times Per Day:")
    print("   - Create multiple tasks for different times")
    print("   - Example: 9 AM, 2 PM, 6 PM")
    print("   - Each task runs the same script")
    
    print("\n📅 Custom Schedules:")
    print("   - Weekdays only: Monday-Friday")
    print("   - Weekends only: Saturday-Sunday")
    print("   - Business hours: 9 AM - 5 PM")
    
    print("\n📅 Conditional Runs:")
    print("   - Only when computer is idle")
    print("   - Only when connected to internet")
    print("   - Only when on AC power")

def create_manual_run_script():
    """Create a script for manual runs"""
    manual_content = f"""#!/usr/bin/env python3
\"\"\"
Manual Run Script for Gmail Article Summarizer
\"\"\"
import subprocess
import sys
import os

def run_summarizer():
    print("🚀 Running Gmail Article Summarizer...")
    print("=" * 40)
    
    try:
        # Change to script directory
        os.chdir("{os.getcwd()}")
        
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
        print(f"❌ Error: {{str(e)}}")

if __name__ == "__main__":
    run_summarizer()
"""
    
    with open('manual_run.py', 'w', encoding='utf-8') as f:
        f.write(manual_content)
    
    print("✅ Created 'manual_run.py' for on-demand runs")

def show_test_instructions():
    """Show how to test the automation"""
    print("\n🧪 Testing Your Automation:")
    print("=" * 30)
    print("1. Test the batch file:")
    print("   Double-click 'run_summarizer.bat'")
    print("2. Test the PowerShell script:")
    print("   Right-click 'run_summarizer.ps1' → Run with PowerShell")
    print("3. Test manual run:")
    print("   python manual_run.py")
    print("4. Check logs:")
    print("   View 'summarizer_log.txt' for detailed logs")

def main():
    """Main setup function"""
    print("🚀 Setting up Automatic Daily Runs")
    print("=" * 40)
    print("📧 This will run your Gmail Article Summarizer automatically!")
    print("💰 Get real-time tech news summaries every day!")
    
    # Create automation files
    create_batch_file()
    create_powershell_script()
    create_manual_run_script()
    
    # Show setup instructions
    show_windows_task_scheduler_instructions()
    show_advanced_scheduling_options()
    show_test_instructions()
    
    print("\n🎯 Next Steps:")
    print("1. Set up Windows Task Scheduler (see instructions above)")
    print("2. Test the automation (see testing instructions)")
    print("3. Check your email daily for fresh article summaries!")
    
    print("\n💡 Pro Tips:")
    print("✅ Start with daily runs at 9 AM")
    print("✅ Monitor the log file for any issues")
    print("✅ Adjust timing based on your schedule")
    print("✅ You can always run manually: python manual_run.py")
    
    print("\n📊 What You'll Get:")
    print("📰 Daily email with latest tech articles")
    print("🤖 AI-powered summaries and insights")
    print("⚡ Real-time content from top tech sources")
    print("📧 Beautiful HTML emails in your inbox")

if __name__ == "__main__":
    main()
