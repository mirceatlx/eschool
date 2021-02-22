# eschool - the best online school management system (at least in theory :0)

This project revolutionizes the current outdated and crap school system.


# Prerequisites

You show have Python and Django installed on your machine.

--install Python - https://www.python.org/
--install Django using pip in your terminal : pip3 install django
--install Git https://git-scm.com/downloads


As the python server is ran locally, you need to get your ipv4 address :

Windows : ipconfig
Linux : ifconfig
MacOS : no one uses macos

# Install 
To get the project on your computer run : git clone https://github.com/mirceatlx/eschool.git

# How to use it

First, go to settings.py in your project folder and at ALLOWED_HOSTS, insert your ipv4.
Then in project folder, run :
    1. python3 manage.py makemigrations
    2. python3 manage.py migrate

To finally run your project : python3 manage.py runserver 'your_ip':port
You can then open your browser.

# IMPORTANT
Some entities such as Class, or Teacher can only  be inserted in the database by the admin user 
from the terminal. 

# Motivation
Learn Django.

# Contributions
Anyone who is eager to help is awesome!:) (just make a pull request)






