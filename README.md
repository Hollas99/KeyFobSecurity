# KeyFobSecurity
A project on the security in rolling code remote keyless entry systems, primarily used in vehicles. The project uses a laptop with a SDR hardware device, and microcontroller to simultaneously jam and record a key fobs signal, which can be later replayed to unlock the vehicle 

# What exactly is this method and how does it work?
This method is almost like a more advanced replay attack, to understand the method, first an understanding of rolling codes (hopping codes) is needed.
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


# What vehicles / devices does this method work on?

# Intructions
