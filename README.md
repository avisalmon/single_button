# The single Button Game. 

To get it up and running you need to:
1. Have the Kit.
2. We support windows 10 and above.
2. clone this repository to a chosen directory in your PC
3. Connect the ESP32 to the USB port and check that the device manager identifies:
	Porst (COM & LPT)  Silicon Labs CP210X USB to UART Bridge (Com??)
4. If not, install the CP210X driver for windows from Si Labs web site: 
	https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads
	Install the CP210x Windows Drivers
	(There is also a copy here in the installation files)
5. Make sure that now the device manager identifies the ESP32 and note the COM number
6. Make sure you have Python 3 in your system. If you need to install it make sure the mark “Add to Path” in the installation process. 
7. Install Thonny
8. In Thonny: 
	- Tools > Mnage Plug-ins > make sure esptools is installed. 
	- Tools > Options > Interperter > choose MicroPython(ESP32)
	- > Choose the correct Port
	- > goto install or update MicroPython
	- > Choose the right Port
	- > Chose or find the .bin file FW to upload in this repository root. 
	- > install. Sometimes you will need to press the boot button on the ESP32 while installing. This is the button right to the USB connector
9. In Thonny open the cloned directory. See the examples.

# To load the Fluppy Collection version:
1. Run step 1 - 6 above. 
2. Run the script setup_install.bat in the repository that you downloaded. 
3. some windows will pop up until you get the option to load Fluppy. 
4. choose option 2 and enter
5. before you continue, press the boot button on the ESP32. Its the button on the right to the USB connector. 
	(when you hold the device and the connector is at the bottom.)
6. Keep on holdiong the button and press enter in the PC. When you see presentage that loads the device, you can get your fingure off the button. 

wait until done.

