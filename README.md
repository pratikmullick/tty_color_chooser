#TTY Color Chooser
A menu-based TTY color terminal scheme for Linux BASH  TTY terminals.

##Installation
###Python3
The TTY color terminal is built using Python3 and uses inbuilt Python libraries.
Most distros come with Python3 within their default installation. Please
consult your distribution documentation for Python3 installation procedures.

###TTY Color Chooser
Simply run ``git clone <url>`` to download the script.

##Use
###Quick Setup
Run the script ``python3 color_chooser.py`` from a Terminal. On the first run,
it will ask to create a color configuration for you. Choose one of the color
schemes.

###Changing Color Schemes
If an existing color-scheme file is found, the program will ask you to create
a new one, delete the existing one, or install the existing one again. Choose
New, and select one of the color schemes.

##Troubleshooting
The installation of the chosen color-scheme might fail, due to permission issues
between Python3 and Bash. In such cases, please run
``$ ./tty_color.sh``
to install the color-scheme.

##Credits
MC PRTK <prtk.uncensored {at} gmail.com>
