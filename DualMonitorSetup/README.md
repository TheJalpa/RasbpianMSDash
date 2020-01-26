## 
## Information pertainint to dual Monitor Setups.

I was able to get this working with a raspberry pi 4b

Things you will need:

- Raspberry pi 4b
- 2x lcd (see main readme on where to obtain this)
- 2x driver board (see main readme)
- 2x hdmi MICRO cable, and usb cables necessary to connect to your driver board, as well as power the pi 3b
I used these:
https://www.amazon.com/gp/product/B06WWQ7KLV/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1

- 1 USB-C Cable (keep in mind, you'll likely be using a 12v to 5v stepdown power supply like most, and will likely
need a usb to usb-c that'll fit your cable for this.  in my case it was a micro to usb-c adapter)
I used these successfully
https://www.amazon.com/gp/product/B01I0ZAJXO/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1

KEEP IN MIND, if you underpower your 4b, it will likely either not boot into the OS, may not power all your screens
and may not work properly.  You /cannot/ (I cannot urge this enough) likely /just/ power this from a standard usb
to usb-c as a standard usb output only puts out a little under 1 amp.  So for those who are planning on using a usb
cable in your car, you are better off using a 12v to 5v stepdown as many of them on amazon put out 3+ amps.

Your pi will use as much of it as it can.

- 1 sd card that'll fit your pi3b (remember, faster is of course, better)
- rasbian OS (you can use the RasbianConfig folder in primary directory for this)
- A copy of tuner studio

## 
## Actually getting tuner studio to work with 2 monitors
## 

Firstly and foremost, a few takeaways from this I found were:

- The config I initially got working for my displays was perfectly fine and in fact, my pi booted up with both
using the config found under the RaspianConfig folder in the core directory.  If you set yours right, you hopefully
should not have to modify this.

- You will need to create a second dashboard in tunerstudio.  There is a little icon next to your dashboard name
in tunerstudio.  Make whatever dashboard you want on lcd #2.

- Once you have your dash for lcd #2 made and you're happy with it, right click for full screen and send it to monitor 2.
This may have an odd notation like ".2" or ".1" and ".0" in it.  At least mine did for my mini lcds.

- Once you have a dashboard assigned to monitor 1 and monitor 2, ensure your options are set for loading your project on tunerstudio
and then to go fullscreen (see main readme step "Directions for installing TunerStudio and setting your dash") in core directory.

- Reboot your pi, and it should immediately load into tunerstudio, load your project, and one by one, load your dash onto each display.