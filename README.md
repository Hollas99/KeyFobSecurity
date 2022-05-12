# KeyFobSecurity #
A project on the security in rolling code remote keyless entry systems, primarily used in vehicles. The project uses a laptop with a SDR hardware device, and microcontroller to simultaneously jam and record a key fobs signal, which can be later replayed to unlock the vehicle 
## Contents ##
- [KeyFobSecurity](#keyfobsecurity)
  * [Contents](#contents)
  * [What exactly is this method and how does it work](#what-exactly-is-this-method-and-how-does-it-work)
      - [Rolling Codes](#rolling-codes)
  * [What vehicles / devices does this method work on?](#what-vehicles--devices-does-this-method-work-on)
  * [Instructions](#instructions)
      - [Equipment List](#equipment-list)
      - [Method](#method)



## What exactly is this method and how does it work? ##
This method is almost like a more advanced replay attack, to understand the method, first an understanding of rolling codes (hopping codes) is needed.
#### Rolling Codes ####
The rolling code system was implemented to prevent replay attacks from occurring, which they successfully do. As shown below.
This first image represents the long list of codes that both the key fob and vehicle will have, the codes are generated using an algorithm so both key fob and vehicle will have the exact same list.
<p align="center">
  <img src="https://user-images.githubusercontent.com/50533340/167963074-9103f77b-889f-467e-9720-dc6ddb173447.png">
</p>
When the unlock button is pressed on the key fob, as seen, a single-use code is sent to the car. Both key fob and car then remove that code from the list.
<p align="center">
  <img src="https://user-images.githubusercontent.com/50533340/167963092-763461d1-ed39-4cf0-b2a4-920a23a18d69.png">
</p>

So what happens if you click the unlock button a load of times outside the vehicles range? That's why a long list is stored on both devices instead of just storing one code. The vehicle accepts any number of codes infront of the previously used code. After the image above the key fob is pressed twice out of range of the car, and then once within the cars range, as seen the car accepts the unlock code, and then discards all the codes previous to it.
<p align="center">
  <img src="https://user-images.githubusercontent.com/50533340/167963102-f9a35ee9-84a5-4868-b620-e9a7bb2577e8.png">
</p>

<h4> How it works </h4>

1. The user goes to unlock their car, clicking the unlock button on their key fob
2. The microcontroller with a 433MHz antenna jams the signal, the laptop simultaneously records the signal
3. The user naturally will click the unlock button again
4. Once again, the signal is jammed and recorded
<p align="center">
  <img src="https://user-images.githubusercontent.com/50533340/167969015-11ec0c6e-8059-4d5e-9d32-cc34366119bc.png">
</p>
5. The laptop sends a signal over wifi to the microcontroller to stop jamming <br>
6. The laptop replays the first signal recorded and unlocks the car <br>
7. A second signal has still been recorded, and can be later used to unlock the car
<p align="center">
  <img src="https://user-images.githubusercontent.com/50533340/167969034-684074e5-3bb6-4fb1-8977-93895d2d2fd6.png">
</p>


## What vehicles / devices does this method work on ##
Theoretically, any vehicle with using one-way communication and an RKEs (remote keyless entry system) can be used.
However, the method has only been tested on the following vehicles:
- Ford S-Max 2016
## Instructions ##
#### Equipment List ####
1. CC1101 433MHz Wireless Transciever
2. USB Memory Stick (Min 8GB)
3. Wemos D1 Mini Microcontroller (Any ESP8266 microcontroller)
4. Breadboard jumper wires (x8)
5. Portable Power Source (Im using a portable power bank)
6. Hack RF One (Any GNURadio supported transciever will work)
7. Laptop (The signal processing is quite demanding, a minimum quad core is likely required)

#### Method ####
I will explain exactly how I have been operating the devices, however alternatives can be made throughout as you wish.
Firstly, the intial steps taken such as installing ubnutu were completed from a windows operating system.
1. Install Ubuntu Operating System on the laptop, I'm running Ubunutu 20 as dual boot
this can be achieved by downloading the latest iso file [here](https://ubuntu.com/download/desktop) and then create a bootable USB stick. I used [Rufus](https://rufus.ie). Install Ubuntu as the main OS or you can install it as dual boot as I have. 
2. The next step is installing GNURadio, open a terminal as root as type the following, official steps can be viewed [here](https://github.com/gnuradio/pybombs)
```
sudo apt-get install python3-pip
sudo pip3 install pybombs
pybombs auto-config
pybombs recipes add-defaults
pybombs prefix init ~/prefix-3.10 -R gnuradio-default
source ~/prefix-3.10/setup_env.sh
```
You can then run the following to open GNURadio
```
gnuradio-companion
```
3. 
