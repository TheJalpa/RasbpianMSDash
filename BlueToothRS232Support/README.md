##
## Introduction
##

In some cases people may find they do not want to use a usb or serial cable that has an extended length.
It may be more beneficial in these circumstances to use bluetooth.

I ended up using the diyautotune bluetooth adapter from their store
BTS4504C1H
https://www.efianalytics.com/products/class1Bluetooth.html

While I felt the price of it was a little steep, it has performed well so far.

This comes with a few caveats though.

- It is not simply plug and play in linux
- It must be configured to rfcomm in linux
- This will require modification of your tunerstudio startup script (or your own)

##
## Configuration
##

Currently this dash setup is utilizing raspbian buster 10.  The following steps must be taken to setup this adapter.

- After you have booted up your pi, look for available devices and connect and pair it
- Once you have done this, you will note if you attempt to "connect" to it, you will get "This device has no services that raspberry pi can use."
- Open up a terminal, and type in the following.  "sudo bluetoothctl" and hit enter.  You will now see a "#bluetooth" on your command line.
- type in "devices" and hit enter.  What you're looking for is the tunerstudio device you just paired, it will have a mac address, jot this down.
- type in "quit" and enter.  We're back to our shell.  Using an editor of your choice (I like vim) edit /etc/systemd/system/dbus-org.bluez.service
- find the line that says "ExecStart=/usr/lib/bluetooth/bluetoothd"
- change that to "ExecStart=/usr/lib/bluetooth/bluetoothd-C --noplugin=sap" and add "ExecStartPost=/usr/bin/sdptool add sp" below it
- write and quit/save your file
- open up /usr/local/bin/TunerStudio.sh in an editor
- above your tunerstudio variables add "bindport = 'sudo rfcomm bind 0 bmac'" with another line below it "$bindport" where bmac is the mac address of your bluetooth device
- write quit/save your file, restart your pi.  Once tunerstudio is open, go to communication and in the com dropdown, you should now see "/dev/rcomm0", select it, click accept.
- Save your tunerstudio project.  Restart your pi, when it comes up, you should be connected to your dash wirelessly ;)