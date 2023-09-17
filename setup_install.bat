:: Check if Python 3 is installed
cd installation_files

@echo off

cls
echo ********************************
echo * We will start checks and installations.
echo * 
echo * please track the windows and follow instructions

python --version 2>NUL
:: Check the error code from the previous command
if %errorlevel% NEQ 0 (
    echo **************************************************************************
    echo Python 3 is not installed You must first install python from python.org  *
    echo Notice!                                                                  *
    echo ***!! please mark "ADD to path" when flagged in the installation !! ***  *
    echo *
    pause
    exit()
) else (
    ::echo Python 3 is installed. we are good to go.
    ::echo Ctrl+C to abort.
    ::pause
)

cls

echo ****************************************
echo Press Enter to install needed Python packages or Ctrl+C to abort
pause
start /wait cmd /c "python install_packages.py"
::echo .
::echo .
::echo We will now check that you have the driver for ESP32. 
::echo Connect the ESP32 to the USB cable.
::echo This window will be closed and a new window will be opened and we will continue there. 

start cmd /c "python check_210_driver.py"
exit()

