# genesispicostudy
Project where I connect a Sega Genesis controller to a Pi Pico

# Motivation
I'm a programmer and game developer, with a few titles released on the market. Retro games are my main inspiration, and I'm passionate about gamepads, keeping a diverse collection.</br>

I also enjoy working on small electronics projects. Recently, I started a new project, finally putting my plans into practice.</br>

My website with the projects</br>
https://guimaraf.github.io/projects.html

# Description
I'm using an original Sega Genesis controller, connected to a DB9 female, which is connected to the Raspberry Pi Pico. With Python, I'm capturing the inputs from the gamepad.

# Connecting DB9 to the Pi Pico
Guide to connections on the board </br>
Separating the connections to make it easier to connect to the Pi Pico without a protoboard </br>

Pin 1 (Up) -> GPIO 2 </br>
Pin 2 (Down) -> GPIO 4 </br>
Pin 3 (Left) -> GPIO 6 </br>
Pin 4 (Right) -> GPIO 8 </br>
Pin 6 (Button B) -> GPIO 10 </br>
Pin 9 (Button A / Start) -> GPIO 12 </br>
Pins 7 and 8 (GND) -> GND of the Raspberry Pi Pico

# Libraries and tools used

# What is MicroPython?
MicroPython is a compact and efficient version of Python 3, which includes a subset of the standard library and is optimized to run on microcontrollers and environments with limited resources.”

https://micropython.org/ </br>

Download link for Pi Pico </br>
https://micropython.org/download/RPI_PICO/

# IDE Thonny
Thonny is a simple and user-friendly IDE, ideal for Python beginners. It facilitates learning with features such as step-by-step execution and error highlighting. In addition, Thonny allows you to program and test code in MicroPython directly on devices such as the Raspberry Pi Pico, making the process quick and accessible. </br>
https://thonny.org/

# Used libraries
machine
time

Both are native to MicroPython

![Alt text](/img/genesis6pad.png?raw=true "Sega Genesis 6 buttons")
</br>
