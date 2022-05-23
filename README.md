# KeyFobSecurity #
A project on the security in rolling code remote keyless entry systems, primarily used in vehicles. The project uses a laptop with a SDR hardware device, and microcontroller to simultaneously jam and record a key fobs signal, which can be later replayed to unlock the vehicle 
## Contents ##
- [KeyFobSecurity](#keyfobsecurity)
  * [Contents](#contents)
  * [What exactly is this method and how does it work?](#what-exactly-is-this-method-and-how-does-it-work)
      - [Rolling Codes](#rolling-codes)
  * [What vehicles / devices does this method work on](#what-vehicles--devices-does-this-method-work-on)
  * [Instructions](#instructions)
    + [Equipment List](#equipment-list)
    + [Method](#method)
      - [Installing Ubuntu and GNURadio](#installing-ubuntu-and-gnuradio)
      - [Installing Arduino IDE and programming the microcontroller](#installing-arduino-ide-and-programming-the-microcontroller)
      - [Wiring the microcontroller to the CC1101 Module](#wiring-the-microcontroller-to-the-cc1101-module)
  * [Legal](#legal)




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

So, what happens if you click the unlock button a load of times outside the vehicles range? That's why a long list is stored on both devices instead of just storing one code. The vehicle accepts any number of codes in front of the previously used code. After the image above the key fob is pressed twice out of range of the car, and then once within the cars range, as seen the car accepts the unlock code, and then discards all the codes previous to it.
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


## What vehicles / devices does this method work on? ##
Theoretically, any vehicle with using one-way communication and an RKEs (remote keyless entry system) can be used.
However, the method has only been tested on the following vehicles:
- Ford S-Max 2016
## Instructions ##
### Equipment List ###
1. CC1101 433MHz Wireless Transceiver (There are a few versions, I have the version with 8 pins)
2. USB Memory Stick (Min 8GB)
3. Wemos D1 Mini Microcontroller (Any ESP8266 microcontroller, or Arduino can be used)
4. Small Solderless Breadboard (SYB-170 is what I'm using)
5. Breadboard jumper wires (x8)
6. Portable Power Source (I'm using a portable power bank, batteries would work fine)
7. Hack RF One (Any GNURadio supported **transceiver** will work)
8. Laptop (The signal processing is quite demanding; a minimum quad core is likely required)

### Method ###
I will explain exactly how I have been operating the devices; however, alternatives can be made throughout as you wish.
Firstly, the intial steps taken such as installing ubnutu were completed from a windows operating system.
#### Installing Ubuntu and GNURadio ####
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
3. This may take quite a while, when finished you can then run the following to open GNURadio
```
pybombs run gnuradio-companion
```
4. The pybombs files can then be downloaded from this repository located in the pyBombs Folder
5. Connect the SDR device (HackRF One) to the laptop
6. You should be able to then open the downloaded GNURadio file and run the program
#### Installing Arduino IDE and programming the microcontroller ####
The next step is to program the microcontroller, and can be achieved from either Ubuntu or Windows
1. Download Arduino [Windows](https://www.arduino.cc/en/software)
or for Ubuntu, in terminal type:
```
sudo apt install arduino
```
2. Open the Arduino program, go to **File > Preferences**
3. Enter ```http://arduino.esp8266.com/stable/package_esp8266com_index.json``` in the **"Additional Boards Manager URLs"** and click **"OK"**
4. Go to **Tools > Board** (it may say ```Board:"Arduino Uno"``` as default) **> Boards Manager...**
5. Type in ```esp8266``` and click the **install** button
6. You should then be able to select ```LOLIN(WEMOS) D1 R2 & mini``` from the **Tools > Board > ESP8266** Boards menu
7. Next open the library manager by going to **Tools > Manage Libraries...** 
8. Type in **CC1101** and look for the option with the title ```SmartRC-CC1101-Driver-Lib``` and click **install**
9. You can then download the file located in folder ***'Arduino'*** in this repository
10. Connect the wemos D1 mini via USB, and select whatever port shows up in **Tools > Port > COMX** (X can be any number)
11. **Upload** the program using the upload button in the top left (the arrow pointing right), this may take a minute or two and the upload progress can be seen in the terminal at the bottom of the screen. *If you receive an error, you likely selected the wrong port.*
#### Wiring the microcontroller to the CC1101 module ####
1. The Arduino library installed in the previous step is located [here](https://github.com/LSatan/SmartRC-CC1101-Driver-Lib). If you are not using the Wemos D1 and instead using an Arduino or ESP8266 then you can follow the guide on their page on how to connect the CC1101 module
2. The CC1101 module can be wired to the wemos d1 mini using the following diagram:
<p align="center">
  <img width=50% src="https://user-images.githubusercontent.com/50533340/167989575-c3315ac0-7ed3-4d59-9d49-51c1b82eb3a3.png">
</p>


## Running the program ##
Now everything should be set up, open up the GNU Radio project it should look like this:
<p align="center">
  <img width=50% src="https://user-images.githubusercontent.com/50533340/169909438-f12813af-b2c5-404d-b134-0e1b6ed3f8ff.png">
</p>

If the custom python blocks **'Manage the peaking signal'** and **'Record Signal when Peak detected'** are showing up empty or giving errors, ensure the downloaded **epy_block_0.py** and **epy_block_3.py** are located in the same folder as the main GNU Radio project file.
Next, connect the signal jammer to a power source and place it next to the vehicle. You can confirm it's working by seeing if theres an open WiFi access point available named **ESPAP**.
The next step is to run the program! Click the execute button a the top of the window, with the play symbol.

## Legal ##
This project was completed for **educational purposes only** as part of a university project and should not be used on any vehicle or device you do not own. 
