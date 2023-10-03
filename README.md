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
