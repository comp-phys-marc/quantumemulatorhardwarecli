Quantum Emulator Hardware Command Line Interface
================================================

CLI tool to provide a cross-platform interface for accessing GPIO, SPI, and I2C on the FT232H using the Python programming language.  
Using this tool you can control the GPIO pins and send or received SPI & I2C commands much like programming those interfaces on a Raspberry Pi or BeagleBone Black.  
This is built on [AdaFruit's Python GPIO library](https://github.com/adafruit/Adafruit_Python_GPIO) abnd the libFTDI library and supports Windows, Mac OSX, and Linux platforms.

- On a Debian-based Linux like Raspbian, Ubuntu, etc. in a terminal execute:
  
  ```
  sudo apt-get update
  sudo apt-get install build-essential python-pip python-dev python-smbus git
  git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
  cd Adafruit_Python_GPIO
  sudo python setup.py install
  ```

- On Mac OSX, first install PIP by [downloading the python script here](https://bootstrap.pypa.io/get-pip.py) and execute it with `python get-pip.py` in a terminal, then install the [git source control system](http://git-scm.com/downloads).  Then in a terminal execute:
  
  ```
  git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
  cd Adafruit_Python_GPIO
  sudo python setup.py install
  ```

- On Windows, first install the [latest Python 2.7 version](https://www.python.org/downloads/windows/), then install PIP by [downloading the python script here](https://bootstrap.pypa.io/get-pip.py) and execute it with `python get-pip.py` in a terminal, and finally install the [git source control system](http://git-scm.com/downloads).  Then in a git bash prompt execute:
  
  ```
  git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
  cd Adafruit_Python_GPIO
  python setup.py install
  ```