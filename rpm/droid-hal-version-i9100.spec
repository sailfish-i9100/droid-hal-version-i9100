# Feel free to cleanup this file by removing comments, once you have memorised them ;)

# rpm_device is the name of the ported device
%define rpm_device i9100
# rpm_vendor is used in the rpm space
%define rpm_vendor samsung

# Manufacturer and device name to be shown in UI
%define vendor_pretty Samsung
%define device_pretty Galaxy S2

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_native 1
%define have_led 1

%include droid-hal-version/droid-hal-version.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

