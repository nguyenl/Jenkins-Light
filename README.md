Jenkins-Light
=============
Jenkins-Light enables communication to a physical continuous-integration traffic light using an Arduino board to display the status of a Jenkins-CI server.

Included is the Arduino sketch and a Python script that queries Jenkins and sends a signal to the Arduino board to display status.


Arduino Setup
-------------
The Arduino sketch file can be found in the arduino/ directory.

The sketch is designed to blink a set of red, yellow, or green lights depending on the signal sent from the host PC through serial communication. A byte corresponding to the ASCII character 'r' turns on the red pattern, 'y' for yellow, and 'g' for the green pattern. The light LED should connect directly to the digital output pins on your arduino board.


Python Setup
-------------
The jenkins-light.py script creates a serial connection with the arduino board. It then queries the Jenkins-CI server for status and send the signal to the arduino board. 

The script must be configured to point to the Jenkins host address, and the Serial USB path must be configured as well. Both values are set at the top of the script.


PYTHON DEPENDENCIES
-------------
* Tested using Python 2.7
* [jenkinsapi](http://pypi.python.org/pypi/jenkinsapi)


LICENSE
-------------
Copyright (C) 2012 Lee Nguyen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.