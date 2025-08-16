# Gmail Article Summarizer Automation Script
# This script runs the article summarizer and logs the results

$scriptPath = "C:\Users\rishi\Downloads\Langflow Workflow"
$logFile = "$scriptPath\summarizer_log.txt"

# Change to script directory
Set-Location $scriptPath

# Log start time
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
"[$timestamp] Starting Gmail Article Summarizer..." | Out-File -FilePath $logFile -Append

try {
    # Run the Python script
    python article_summarizer_gmail.py 2>&1 | Out-File -FilePath $logFile -Append
    
    # Log completion
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$timestamp] Gmail Article Summarizer completed successfully" | Out-File -FilePath $logFile -Append
}
catch {
    # Log any errors
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$timestamp] Error running Gmail Article Summarizer: $_" | Out-File -FilePath $logFile -Append
}
