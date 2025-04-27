import subprocess

def open_powershell():
    try:
        subprocess.run(["powershell.exe"])
        print("PowerShell opened successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error opening PowerShell: {e}")
    except FileNotFoundError:
        print("PowerShell executable not found.")

if __name__ == "__main__":
    open_powershell()
