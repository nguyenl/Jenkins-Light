# Copyright (C) 2012 Lee Nguyen

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This python script is part of the Jenkins-Light project. It
# determines the colour of light to display on a traffic light
# controlled by arduino.
import serial
import time
import sys
from jenkinsapi import jenkins


# Configuration
JENKINS_URL = 'http://localhost:8080/'
DEVICE_PATH = '/dev/ttyUSB0'
BAUD_RATE = 9600

SUCCESS = 'g'
FAILURE = 'r'
BUILDING = 'y'
QUERY_FREQUENCY = 30 # Frequency to query jenkins, in seconds.

# Connect to the Arduino board.
ser = serial.Serial(DEVICE_PATH, BAUD_RATE)

# Sleep to allow Arduino board to configure serial communication.
time.sleep(2)

j = jenkins.Jenkins(JENKINS_URL)
current_state = ''


def change_light(state):
    global current_state
    if state != current_state:
        ser.write(state)
        current_state = state


def check_jenkins():
    try:
        jobs = j.get_jobs()
        for (name, job) in jobs:
            if not j[name]._data['lastBuild']:
                # If a job has never been built, skip it.
                continue
            last_build = j[name].get_last_build()
            if last_build and last_build.is_running():
                change_light(BUILDING)
                return
            elif not j[name].get_last_build().is_good():
                change_light(FAILURE)
                return
        change_light(SUCCESS)
    except:
        change_light(FAILURE)
        print "Unable to query jenkins:", sys.exc_info()[0]


if __name__ == "__main__":
    while(1):
        # Main application loop.
        check_jenkins()
        time.sleep(QUERY_FREQUENCY)
