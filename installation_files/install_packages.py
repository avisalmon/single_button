import platform
import sys
import subprocess

def check_if_we_are_on_64_windows_10():
    if platform.system() == "Windows":
        # Check if it's a 64-bit Windows
        if platform.architecture()[0] == "64bit":
            # Get the Windows version
            version_str = platform.release()
        
            # Parse the Windows version string to get the major version number
            windows_version = int(version_str.split('.')[0])
        
            # Check if the Windows version is 10 or above
            if windows_version >= 10:
                print("Running on 64-bit Windows version 10 or above.")
                return True
            else:
                print("Running on 64-bit Windows, but not version 10 or above.")
                return False
        else:
            print("Running on 32-bit Windows.")
            return False
    else:
        print("Not running on a Windows system.")
        return False

if check_if_we_are_on_64_windows_10():
    print('ready to go')
else:
    sys.exit(1)

packages = ["pywin32", "pyserial"]

# make sure all packages installed
for package in packages:

    try:
        __import__(package)
        print(f'{package} is there')
    except ImportError:
        print(f'{package} is not there')
        try:
            # Use subprocess to run the pip install command
            subprocess.check_call(["pip", "install", package])
            #print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to install {package}")
            print(e)

exit()