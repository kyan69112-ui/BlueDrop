# Bluetooth AirDrop

A simple Bluetooth file transfer application for sending files to other Bluetooth devices.

## Features

- **Device Discovery**: Scan for nearby Bluetooth devices
- **File Selection**: Browse and select files to send
- **File Transfer**: Send files via Bluetooth RFCOMM protocol
- **GUI Interface**: User-friendly Tkinter-based interface
- **Threading**: Non-blocking UI with background transfers

## Requirements

- Python 3.7+
- PyBluez library
- Tkinter (usually included with Python)
- Bluetooth adapter on your system

## Installation

1. Install Python 3.7 or higher
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

### Steps to Transfer a File

1. **Select a File**: Click "Browse File" and choose the file you want to send
2. **Scan for Devices**: Click "Scan for Devices" to discover nearby Bluetooth devices
3. **Choose Device**: Select a device from the list
4. **Send**: Click "Send File" to transfer the file

## How It Works

- The application uses PyBluez to interact with the Bluetooth stack
- Device discovery uses Bluetooth inquiry to find nearby devices
- Files are transferred using RFCOMM sockets (serial port profile)
- The receiver needs a compatible Bluetooth file transfer service running

## Limitations

- Requires compatible Bluetooth file transfer service on receiving device
- Windows users may need additional Bluetooth drivers
- Transfer speed depends on Bluetooth version and signal quality

## License

MIT License
