#!/bin/bash

# لقطة شاشة (تحاكي أمر #SCREEN#)
echo "Taking screenshot..."
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png .

# الحصول على معلومات الجهاز (تحاكي الحصول على الـ IMEI) 
echo "Device Info:"
adb shell ip addr show wlan0 | grep "inet "
