Quantum Emulator Hardware Command Line Interface
================================================

CLI tool to provide a cross-platform interface for accessing Q.E.D. hardware through USB using the I2C on the FT232H in the Python programming language.
This is built on [AdaFruit's Python GPIO library](https://github.com/adafruit/Adafruit_Python_GPIO) and the libFTDI library. Supports Windows, Mac OSX, and Linux platforms.

Should be developed separately form Quantum Emulation Engine services, not using the smae python environment found in `distributedemulator/venv`.

## Setup the Adafruit library dependency

- On a Debian-based Linux like Raspbian, Ubuntu, etc. in a terminal execute:
  
  ```
  sudo apt-get update
  sudo apt-get install build-essential python-pip python-dev python-smbus git
  cd Adafruit_Python_GPIO
  sudo python setup.py install
  ```

- On Mac OSX, first install PIP by [downloading the python script here](https://bootstrap.pypa.io/get-pip.py) and execute it with `python get-pip.py` in a terminal, then install the [git source control system](http://git-scm.com/downloads).  Then in a terminal execute:
  
  ```
  cd Adafruit_Python_GPIO
  sudo python setup.py install
  ```

- On Windows, first install the [latest Python 2.7 version](https://www.python.org/downloads/windows/), then install PIP by [downloading the python script here](https://bootstrap.pypa.io/get-pip.py) and execute it with `python get-pip.py` in a terminal, and finally install the [git source control system](http://git-scm.com/downloads).  Then in a git bash prompt execute:
  
  ```
  cd Adafruit_Python_GPIO
  python setup.py install
  ```

## Multi-Protocol Synchronous Serial Engine Setup

- Linux

    ```
    sudo apt-get update
    sudo apt-get install build-essential libusb-1.0-0-dev swig cmake python-dev libconfuse-dev libboost-all-dev
    # wget http://www.intra2net.com/en/developer/libftdi/download/libftdi1-1.2.tar.bz2
    # tar xvf libftdi1-1.2.tar.bz2
    cd libftdi1-1.2
    # mkdir build
    cd build
    cmake -DCMAKE_INSTALL_PREFIX="/usr/" -DPYTHON_INCLUDE_DIR="/usr/include/python2.7" -DPYTHON_LIBRARIES="/usr/lib/python2.7/" ../
    make
    sudo make install
    ```

Make sure that the outputs of `sudo make install` are installed in `/usr/lib/python2.7`, not in another place. The tool is compatible only with python 2.7.

## Use

To run the tool:

```
sudo /usr/bin/python2.7 main.py <args>
```

## Notes

The hardware does not work over USB 3.0 ports at the moment.

## License

Copyright 2019 Marcus Edwards

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at:

```
http://www.apache.org/licenses/LICENSE-2.0
```

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.