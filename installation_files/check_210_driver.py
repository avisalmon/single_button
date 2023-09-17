import subprocess
import win32com.client
import platform
import sys
import serial.tools.list_ports
import re
import os

#check that you are on Windows 64 10 or above
if platform.system() == "Windows":
    # Check if it's a 64-bit Windows
    if platform.architecture()[0] == "64bit":
        # Get the Windows version
        version_str = platform.release()
        
        # Parse the Windows version string to get the major version number
        windows_version = int(version_str.split('.')[0])
        
        # Check if the Windows version is 10 or above
        if windows_version >= 10:
            #print("Running on 64-bit Windows version 10 or above.")
            pass
        else:
            print("Running on 64-bit Windows, but not version 10 or above.")
            input("press enter to abort...")
            exit(0)
    else:
        print("Running on 32-bit Windows.")
        input("press enter to abort...")
        exit(0)
else:
    print("Not running on a Windows system.")
    input("press enter to abort...")
    exit()


wmi = win32com.client.GetObject("winmgmts:")
drivers = wmi.InstancesOf("Win32_SystemDriver")

list_of_drivers = []

CP210 = False

for driver in drivers:
    list_of_drivers.append(driver.description)
    if "CP210" in driver.description:
        print("Driver CP210X installed. Great!")
        CP210 = True

if not CP210:
    driverexe = r'CP210xVCPInstaller_x64.exe'

    # Run the executable and wait until it's done
    subprocess.run(driverexe, shell=True, check=True)

#check if ESP32 is connected
com_number = 0
while com_number == 0:
    ports = serial.tools.list_ports.comports()
        
    pattern = r'COM(\d+)'

    if not ports:
        print("No COM ports found.")
    else:
        #print("Available COM ports:")
        for port in ports:
            #print(f"- {port.device}: {port.description}")
            if "CP210" in port.description:
                match = re.search(pattern, port.description)
                if match:
                    com_number = int(match.group(1))

    if com_number:
        print(f'your ESP32 is connected to COM{com_number}')
    else:
        input('\nPlease connect the ESP32 device, than press any key...')

os.chdir('esptool')
os.system('cls')
print(os.getcwd())

option = int(input('''

**************************
What would you like to do:

1. Run Thonny to work with MicroPython
2. upload the cute fluppy game
3. nothing. close the program
'''))

if option == 1:
    os.system('cls')
 
    # Run Thonny.
    try:
          os.system('start thonny')

    except subprocess.CalledProcessError:
        os.system('cls')
        print('''You dont have Thonny installed.
    Goto thonny.org, install and run Thonny. continue there.
    ''')
        input('press Enter to exit')
        

if option == 2:
    # cmd = 'cd esptool'
    # subprocess.run(cmd, shell=True)
    os.system('cls')
    os.system('cd esptool')
    cmd = f'python esptool.py --chip esp32 --port COM{com_number} write_flash -z --flash_mode dio --flash_freq 40m --flash_size detect 0x0 firmware_dump.bin'
    input('''***********************
* 
*
*
* hold the boot button on the ESP32 device, 
* right to the USB connector, 
* and press enter in parralel
*
****************************
    ''')
    subprocess.run(cmd, shell=True)
    os.system('cls')
    input('''Your Fluppy game should work now. 
If it does not, you might not pressed the boot button on the ESP32 while burning.
Run it all again 

Press enter to end the program...''')