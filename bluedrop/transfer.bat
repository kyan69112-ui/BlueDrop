@echo off
REM Bluetooth File Transfer - Batch Script
REM Sends files to Bluetooth devices

setlocal enabledelayedexpansion

title Bluetooth AirDrop - File Transfer

:menu
cls
echo.
echo ========== Bluetooth AirDrop ==========
echo.
echo 1. Scan for Bluetooth devices
echo 2. Send file to device
echo 3. Exit
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" goto scan_devices
if "%choice%"=="2" goto send_file
if "%choice%"=="3" goto exit_app
echo Invalid choice. Please try again.
timeout /t 2 >nul
goto menu

:scan_devices
cls
echo.
python scan_bt.py
echo.
pause
goto menu

:send_file
cls
echo.
set /p file_path="Enter the full path to the file to send: "

if not exist "!file_path!" (
	echo Error: File not found at !file_path!
	timeout /t 2 >nul
	goto menu
)

set /p device_address="Enter the Bluetooth device address (format: XX:XX:XX:XX:XX:XX): "

echo.
echo Starting file transfer to device !device_address!...
echo.

REM Use Python to handle Bluetooth transfer
python -c "
import sys
import socket
from pathlib import Path

try:
	file_path = r'!file_path!'
	device_address = '!device_address!'
    
	sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
	sock.connect((device_address, 1))
    
	file_name = Path(file_path).name
	sock.send(f'FILE:{file_name}'.encode() + b'\n')
    
	with open(file_path, 'rb') as f:
		while True:
			chunk = f.read(4096)
			if not chunk:
				break
			sock.send(chunk)
    
	sock.send(b'END_OF_FILE')
	sock.close()
    
	print('File transferred successfully!')
except Exception as e:
	print(f'Error: {str(e)}')
"

echo.
pause
goto menu

:exit_app
echo.
echo Exiting Bluetooth AirDrop...
timeout /t 1 >nul
exit /b 0
