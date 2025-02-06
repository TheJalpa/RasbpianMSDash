# RasbpianMSDash
A dash project for tunerstudio based on RASPBIAN
This is /not/ individual software, but rather
A collection of configurations you can use for your
Raspberry pi that will allow you to make a custom dash
and load it onto a small LCD for purposes of making
your own custom gauges in pods.

![picture](https://i.imgur.com/ah9AKqg.jpg)

# 
# The Basics
# 
This is based on a TFT display which will require the following:

- 1 TFT LCD Display
- 1 HDMI Driver board (compatible for TFT displays)
- 1 HDMI cable
- Raspberry pi 3b
- Raspbian OS installed on your Raspberry pi

Sources for LCD hardware:
The specific LCD I used was the following, along with the hdmi board
Model # TM034XDZP02 LCD
The cost for each is around $30, which puts it at close to $60 for both items.
This is one such example, keep in mind alibaba changes this stuff all the time so the link may expire, search the model number.  You are looking for a round 3.4" LCD and an HDMI driver board to go with it.
[https://www.alibaba.com/product-detail/HDMI-driver-board-3-4-inch_62223501742.html?spm=a2756.order-detail-ta-bn-b.0.0.3aa32fc2jbibs2](https://www.alibaba.com/product-detail/Confu-HDMII-to-MIPI-DSI-Driver_62052729760.html?spm=a2700.galleryofferlist.normal_offer.d_title.640713a0e6ZGUN)

[https://www.google.com/search?q=TM034XDZP02](Search by Model Number)

# 
# Notes for LCDs and Driver Boards
# 
I could not find a specific model number on the board, since these are made in china, some mass produced
it seems some have numbers, some do not.  What mine does have is "HDMI to DSI Version 1.2"
and is a MIPI DSI output to HDMI input, with an FFC adapter.

It should be noted you can use whichever TFT and driver board you prefer, but due to the pin setup
of these LCDs, they use a 39 pin setup, and will generally require a driver board to use with
your Raspberry pi, so contact the manufacturer before you purchase it to make sure the hdmi driver board
matches the TFT display.

I have seen some hats for them which seem to claim to work with MIPI setups but for separate pin setups.
It may be possible to get around this, but for purposes of this project, the HDMI driver board is assumed.

# 
# Designing a dashboard
# 
The easiest way to design a dashboard before loading it to your pi is to do the following:
- Install tunerstudio on your desktop/laptop
- Plug your LCD and driver board into your desktop/laptop hdmi as a secondary display
- Fire up tunerstudio, go into your dashboard, go into designer mode and set it to fullscreen
for "display #" where # is your monitor that your LCD represents (likely 2, or 3 if you have 2 monitors already)

This I found easiest to do since it was easy to simply make changes on the desktop rapidly, full screen it, 
put it into "demo mode" to see how I liked it, and rinse and repeat.

Once you have a dashboard you like that fits your LCD, export that dashboard and save it as a .dash file.
Any custom images you have used for backgrounds and custom settings will be saved with it.

Remember where you saved it, as you will need a way to put it on your pi (i just emailed it to myself
and downloaded it on my pi)

# 
# Directions for installing Raspbian
# 
It is best to utilize the directions on the official site for raspbian which can
be found here: https://www.raspberrypi.org/documentation/installation/installing-images/

I used balenaEtcher and etched an image of rasbian with desktop
https://www.raspberrypi.org/downloads/raspbian/

I would personally go with Raspbian Buster with Desktop, and skip the "recommended software" version
as we are only going to load up tunerstudio on here, and the smaller our footprint, the faster our boot times.

Download your image, load up balena etcher, select your image, insert your micro sd card and then flash
your raspbian image onto your SD card.  Once this is done, hook your raspberry pi up to a monitor,
along with your peripherals, and configure your basics (keyboard, username, password, etc.)

# 
# Directions for installing TunerStudio and setting your dash
# 

Note, this tutorial assumes you are hooking your pi up to a regular HDMI monitor and not using
your LCD until it's time to configure and test that.  So for the following steps, until prompted,
this assumes you're on your regular monitor, not your LCD (setting this up would be a nightmare otherwise)

This tutorial assumes that you own a full copy of tunerstudio.  Only the full version will work
with a fullscreen dash project to utilize the feature of booting into your dashboard fullscreen mode.
No, I won't help you crack it, and no, I won't give you my key.  Buy it like the rest of us did.

You will need to do this on your raspberry pi:

The linux version of tunerstudio can be found here:
http://tunerstudio.com/index.php/downloads
Navigate to "For Linux" and download the "TunerStudio MS", this will be a tar.gz file

Once this is done, go to your downloads folder and extract it to your home directory.
Your home directory will be your username when you setup your pi.  Default is just 'pi"
Open up a terminal window and type "ls /home/yourdirectoryusername/TunerStudioMS"
If default then "ls /home/pi/TunerStudioMS"
and what you should see is a list of files if you extracted it correctly to your home directory.

Ensure that you see "TunerStudio.sh" as a listed file in here.  If not, double check your installation.

From the same terminal, we need to ensure we create a symbolic link to start up tunerstudio.

Type the following:
"ln -s /home/yourdirectoryusername/TunerStudioMS/TunerStudio.sh /usr/local/bin"
Once this is done, type:
"bash /usr/local/bin/TunerStudio.sh"

This should fire up tunerstudio.
You will then need to enter your registration information so you're then using the full version
as by default, it is the lite version of tunerstudio.

Once you have done this, use a method to import your tune and dash that you have created.
Load your tune into tunerstudio, and on the dash, right click and "load/save" and select dash
Select "other", click the "...", navigate to your .dash file, load it, click apply and ok.

Once this is set, in tunerstudio, click "Options", go to Preferences, and select "load last project on startup"
After that is set, you can go back to preferences and select "Make Dashboard Fullscreen"
Save your tune. exit tunerstudio.

# 
# Directions for setting up the LCD for HDMI
# 
# Notes
This is the tricky part.  These little LCDs tend to need /very/ specific settings in order to work.
I spent a few hours playing with settings trying to even get a picture on mine and wondered if my lcd
wasn't broken at first.  I then hooked the driver board up to my desktop, it worked fine, so I knew
that wasn't the case.

These LCDs generally use a square resolution which is a bit odd and unusual for most monitors
and by default, raspbian seems to want to default to a resolution it appears it can't stretch to,
so the hdmi driver board will act as if it's trying to "lock on" but not sync up fully.

Under "RasbianConfig" folder in this project, you will need to use the "config.txt" file as an outline
for your own LCD.

# Physical hookup
Your Display HDMI driver board should really only hook up one way.
Generally it should look like the following:
LCD display (39 pin out) > tft board (40 pin out) > HDMI board > HDMI to Pi

It is worth noting, the 39 pin ribbon is a bit odd if you aren't used to them as they install at a 
bit of an angle.  I found the easiest way to do this is to open the clip,
install the ribbon with the contacts facing the board contacts at a slight angle,
it should slide in, and a line on the ribbon should line up with the flat side of the insert.
Clamp the clip down, and it should hold it firmly in place.

The longer ribbon is generally much easier as it sits fairly flat and lines up pretty easily.

It should also be noted, the driver board requires a usb cable to power it.

# Directions
Let's start with finding your resolution for your LCD.  The easiest way to do this is to hook this up
to your desktop, be it on windows or on mac.  It should automatically get you a picture on your desktop.
Once you've done this, go into your display settings where you see your monitor resolution, and pick out
the smaller, new monitor, and find the resolution that is being dipslayed.

In my case, it was 800x800 @ 60hz.  This is important, remember this.

Now, let's go back to your raspberry pi, and we will need to edit your /boot/config.txt file using 
the file in the folder in this project

Once these configuration settings have been set, reboot your pi (they won't take effect till you have)


# 
# Directions for starting TunerStudio At Startup
# 
With tunerstudio installed, registration set, and your dash settings set, assuming you have tested
and made sure it starts up with your tune, dashboard goes full screen, and your LCD works we can now set it to start at startup.

You will need to edit /etc/xdg/lxsession/LXDE-pi/autostart

Using your editor of choice (I generally do a sudo apt install vim and then vim it)
edit the above file and on line 3, add your bash file we created a symbolic link for.
In this case, "bash /usr/local/bin/TunerStudio.sh"
At startup, your raspberry pi should load to desktop, start tuner studio, load your tune, your dashboard
and then go fullscreen.

# 
# Final notes
# 
Each installation may vary a little bit from person to person as if you have used a different LCD
then the resolution may vary, along with the refresh rate, hardware may vary.

But again, the outline of config.txt gives you at least an idea of where to start on a config,
and can be edited on your raspberry pi accordingly.

Once this is complete, you can hook your raspberry pi up to your usb to serial and ensure that it sees your
ECU and it should automatically load at startup.

How you want to power your raspberry pi is up to you, I recommend a 12v to 5v usb stepdown.  These are generally
a larger amp power supply than the standard power supply that your usb comes with, which will give the pi
a bit more amperage to work with and should actually power it better, and load faster.

The largest drawback of load times on these is lack of power since standard usb power is less than 1 amp.

This tutorial is for my own individual car so I do not have a 3d printed mount that will work for your car,
so how you wish to house this into your gauge set is up to you.  Your easiest bet is a 3d printed custom mount.
Or perhaps something you fabricate yourself.

It should also be noted that for purposes of fitment, you should have your LCD screen be slightly smaller than the inner
diameter of your gauge pod, otherwise you leave yourself not a lot of room to house it properly and mount it.

## 
## Future updates:
## 

Coming soon I would like to add more config files and tutorial information on here.
If anyone has information pertaining to:

- optimizing the installation of raspbian to run faster
- optimizing the OS for minimal as possible installation

I would much appreciate any of the info above so I can make it faster, and a bit more crisp, as well as
get rid of the unecessary load info as it isn't needed except for troubleshooting.
