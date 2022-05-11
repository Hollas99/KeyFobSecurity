# KeyFobSecurity
A project on the security in rolling code remote keyless entry systems, primarily used in vehicles. The project uses a laptop with a SDR hardware device, and microcontroller to simultaneously jam and record a key fobs signal, which can be later replayed to unlock the vehicle 

# What exactly is this method and how does it work?
This method is almost like a more advanced replay attack, to understand the method, first an understanding of rolling codes (hopping codes) is needed.
The rolling code system was implemented to prevent replay attacks from occurring, which they successfully do. As shown below.
This first image represents the long list of codes that both the key fob and vehicle will have, the codes are generate using an algorithm so both key fob and vehicle will have th exact same list.
![Artboard 1](https://user-images.githubusercontent.com/50533340/167958300-8ecb3229-77cc-41b4-a3c5-73c02cd7a523.png)

When the unlock button is pressed on the key fob as seen a single-use code is sent to the car, both key-fob and car then remove that code from the list.
![Artboard 2](https://user-images.githubusercontent.com/50533340/167958796-3d6475d8-2a48-4145-aa83-1151105cbacf.png)

So what happens if you click the unlock button a load of time outside the vehicles range? That's why a long list is stored on both devices instead of just storing one code. The vehicle accepts any number of codes infront of the previously used code up to around  
# What vehicles / devices does this method work on?

# Intructions
