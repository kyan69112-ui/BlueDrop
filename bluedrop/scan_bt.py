#!/usr/bin/env python
"""
Scan for nearby unpaired Bluetooth devices.
"""
import sys
import asyncio
import subprocess

print('Scanning for nearby UNPAIRED Bluetooth devices...')
print()

# Method 1: Try using bleak for BLE device discovery
try:
    from bleak import BleakScanner
    
    async def scan_ble():
        print('Discovering nearby BLE devices...')
        devices = await BleakScanner.discover(timeout=5)
        if devices:
            print(f'Found {len(devices)} device(s):')
            print()
            for device in devices:
                name = device.name if device.name else 'Unknown'
                address = device.address
                print(f'  Name: {name}')
                print(f'  Address: {address}')
                print()
        else:
            print('No BLE devices found.')
    
    asyncio.run(scan_ble())
    
except ImportError:
    print('Note: bleak library not installed. Using alternative method...')
    print()
    
    # Method 2: Use Windows Registry to find paired devices
    try:
        import winreg
        print('Scanning paired Bluetooth devices from registry...')
        print()
        
        reg_path = r"SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Devices"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
        
        device_count = winreg.QueryInfoKey(key)[0]
        
        if device_count > 0:
            print(f'Found {device_count} paired device(s):')
            print()
            for i in range(device_count):
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)
                try:
                    name, _ = winreg.QueryValueEx(subkey, "Name")
                    print(f'  Name: {name}')
                    print(f'  Address: {subkey_name}')
                    print()
                except:
                    print(f'  Address: {subkey_name}')
                    print()
                winreg.CloseKey(subkey)
        else:
            print('No paired devices found in registry.')
        
        winreg.CloseKey(key)
        
    except Exception as e:
        print(f'Registry scan failed: {e}')
        print()

print()
print('INSTRUCTIONS:')
print('1. Make sure your Bluetooth device is in DISCOVERABLE/PAIRING mode')
print('2. Make sure Bluetooth is enabled on your computer')
print()
print('If you don\'t see your device:')
print('  Settings > Devices > Bluetooth & other devices > Add device')
print('  Select "Bluetooth" and choose your device from the list')
print()
print('Use the device ADDRESS (format: XX:XX:XX:XX:XX:XX) with option 2')
