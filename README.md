# RPI-Zero-MagicMirror for ~50€
A 40€ Magic mirror using a raspberry pi zero W.
Prices always fluctuate a little bit. Therefore when you are reading this it could be like 45-50€.
This guide will explain how to set up the MagicMirror2 OS on a raspberry pi zero.

## Hardware required for the Mirror (tools not included):

  * [Raspberry pi zero W](https://www.berrybase.de/raspberry-pi-zero-w) - ~11€
  * [Micro SD-card 16GB](https://www.ebay.de/i/273535152997?chn=ps&norover=1&mkevt=1&mkrid=707-134425-41852-0&mkcid=2&itemid=273535152997&targetid=888516359244&device=c&mktype=pla&googleloc=9068150&poi=&campaignid=1669295758&mkgroupid=90992276282&rlsatarget=pla-888516359244&abcId=1139676&merchantid=7364532&gclid=EAIaIQobChMIppr__Lfl6AIVRrDtCh1c8QtqEAQYAiABEgLwsPD_BwE) - 5€
  * [micro HDMI to HDMI adapter](https://www.aliexpress.com/item/33006250821.html?spm=a2g0s.9042311.0.0.27424c4dyB0J72) - ~1€
  * Dependent on your monitor inputs a matching cable [I used this](https://www.aliexpress.com/item/33014827860.html?spm=a2g0s.9042311.0.0.27424c4dyB0J72) - ~2€
  * [micro-USB male](https://www.aliexpress.com/item/32874847823.html?spm=a2g0s.9042311.0.0.27424c4dczswkm) - ~1€
  * [5v Relay](https://www.aliexpress.com/item/32969889587.html?spm=a2g0o.productlist.0.0.12d12f09ujISno&algo_pvid=617edfee-1041-4329-b242-70a5c9148285&algo_expid=617edfee-1041-4329-b242-70a5c9148285-1&btsid=0ab50f6215867803297066531e46cc&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_) - ~1€
  * [ikea Ribba frame at least 50x50cm](https://www.ikea.com/de/de/cat/ribba-serie-16456/) - ~10€
  * old monitor (or find one on ebay kleinanzeigen/craigslist/etc...) - ~0€-10€
  * [5v PSU](https://www.aliexpress.com/item/33008360777.html?spm=a2g0o.productlist.0.0.6aa67977TpXVsT&algo_pvid=e99d80ef-c883-439f-b3f7-81f06a91c2a6&algo_expid=e99d80ef-c883-439f-b3f7-81f06a91c2a6-0&btsid=0ab6f81615867816964263103e5a42&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_) - ~2€
  * if you do not have this lying around:
    * [some cables for soldering](https://www.aliexpress.com/item/4000197988123.html?spm=a2g0o.productlist.0.0.150f50f3s6cX67&algo_pvid=f45e848a-ba02-4de6-a01b-d48181557d3b&algo_expid=f45e848a-ba02-4de6-a01b-d48181557d3b-6&btsid=0ab6fb8315867817791791856e45de&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_) - ~5€
    * wood to cover the back of the frame (I used the 50x50cm RIBBA) - ~2€
    * maybe some wood to secure the display in place - (~2€)
  * [PIR motion sensor](https://www.aliexpress.com/item/1877185512.html?spm=a2g0s.9042311.0.0.27424c4dvxv2Pn)
  * mirror foil - ~10€
  

Total: 11€ + 5€ + 1€ + 2€ + 1€ + 1€ + 10€ + 0-10€ + 2€ + 5€ + 2€ + 2€ + 10€ = ~50-60€

To setup the hardware follow [this video](www.youtube.com).

RPi ZeroW Pinout:
![RPi Zero W Pinout image not found](https://github.com/CaptainDario/RPI-Zero-MagicMirror/blob/master/rpiZW_pins.png "Logo Title Text 1")
[source](https://raspberrypi.stackexchange.com/questions/83610/gpio-pinout-orientation-raspberypi-zero-w)

## Installing the OS on the RPI 0W

I used as a reference [this guide](http://emmanuelcontreras.com/how-to/how-to-create-a-magic-mirror-2-with-pi-zero-w/) however I need to make some changes. Also somethings were unclear to me. But he provides a ready made image that you can use to skip over all the steps described here (I did not test the image).

1. download [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/)
1. flash image to SD-card (I used [Balena Etcher](https://www.balena.io/etcher/))
2. copy "SSH" and "wpa_supplicant.conf" to the boot-partition of the SD-card (don not forget to change the placeholders in "wpa_supplicant.conf")
3. Install Node.js
  1. ``` sudo wget https://nodejs.org/dist/v10.16.0/node-v10.16.0-linux-armv6l.tar.xz ```
  2. ```tar xvf node-v10.16.0-linux-armv6l.tar.xz```
  3. ```cd node-v8.3.0-linux-armv6l```
  4. ```sudo cp -R * /usr/local/```
  5. ```sudo reboot```
4. ```sudo apt install npm```
5. ```sudo apt install git```
6. Install MagicMirror:
  1. ```git clone https://github.com/MichMich/MagicMirror```
  2. ```cd MagicMirror```
  3. ```npm install –arch=armv7l ```
7. ```sudo apt install chromium-browser```
8. ```sudo raspi-config```
  1. ```Boot Options```
  2. ```B1 Desktop/CLI```
  3. ```B2 Console Autologin```
9. ```sudo apt-get install xinit```
10. ```sudo apt install xorg```
11. ```sudo apt install matchbox```
12. ```sudo apt install unclutter```
13. copy "chromium_start.sh" and "mmstart.sh" to your homefolder
14. ```sudo chmod a+x ~/mmstart.sh```
15. ```sudo chmod a+x ~/chromium_start.sh```

17. To start the browser and show the mirror after boot up follow [this guide](https://github.com/MichMich/MagicMirror/wiki/Auto-Starting-MagicMirror)


## Installing Modules

### Turn on and off the mirror with the PIR-sensor:
 * [1st option](https://github.com/paviro/MMM-PIR-Sensor) (Did not get this working)
 * [2nd option](https://github.com/mboskamp/MMM-PIR) (setup as described in the link and used the 'toggle_relay.py' as callback script)
   * I had to follow [this suggestion](https://github.com/mboskamp/MMM-PIR/issues/10#issuecomment-519239401) to turn hdmi off/on:
     * in ~/MagicMirror/modules/MMM-PIR/callbackScripts/default/ the files "displayOff.sh" and "displayOn.sh" had to be slightly modified (look at the provided files)
   * To toggle the relay:
     * install pip:
       * sudo apt-get install python3-pip
     * install RPi.GPIO:
       * python3 -m pip install RPi
     * move the turnOn/OffRelay python scripts to the ~/MagicMirror folder
     
     
### Show guest wifi credentials and QR-code
  * [Shows a QR-code and wifi SSID and pwd](https://github.com/TeraTech/MMM-WiFiPassword)

### Other modules
* [complete official list](https://github.com/MichMich/MagicMirror/wiki/3rd-Party-Modules)



## Toggle relay via Home Assistant
