import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# Check if file exists
if not os.path.exists(chrome_path):
    print(f"Error: Chrome not found at {chrome_path}")
    exit(1)

cmd_args = [
    chrome_path,
    "--remote-debugging-port=9222",
    r"--user-data-dir=C:\sel_chrome_profile"
]

print(f"Launching: {cmd_args}")
process = subprocess.Popen(
    cmd_args,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
)
print(f"Chrome launched with PID: {process.pid}")
