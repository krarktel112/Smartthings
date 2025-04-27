import subprocess

try:
    result = subprocess.run(["powershell.exe", "-Command", "Get-Host"], capture_output=True, text=True, check=True)
    print("PowerShell command output:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error running PowerShell command: {e}")
except FileNotFoundError:
    print("PowerShell executable not found.")
