from __future__ import print_function
import sys

from flask import Flask, request, render_template, redirect, url_for
from forms import SymbolSearch


app = Flask(__name__)
@app.route("/", methods=['GET'])
def main():
    return render_template('form_submit.html')

if sys.version_info < (3, 0):
    input = raw_input


class Setter(object):
    def __init__(self, name):
        self.name = name

    def set(self, times):
#        print("This is {0}.".format(self.name))
        self.setMins(times)
        self.setHours(times)
        self.setDay(times)
        print("Settings applied.")
        times.printTimes()
        times.setAlarm()
        print("Alarm set.")

    def setMins(self, times):
        print("Current settings:")
        times.printTimes()
        val = input("mins? ").strip()
        print(val)
        if val:
            times.setMinutes(val)

    def setHours(self, times):
        print("Current settings:")
        times.printTimes()
        val = input("hours? ").strip()
        if val:
            times.setHours(val)

    def setDay(self, times):
        print("Current settings:")
        times.printTimes()
        val = input("day? ").strip()
        if val:
            times.setDay(val)


@app.route('/results/', methods=['POST'])
    def setMinsFlask(self, times):
        print("Current settings:")
        times.printTimes()
#        val = input("mins? ").strip()
        val = request.form['minutes']
        print(val)
        if val:
            times.setMinutes(val)

    def setHoursFlask(self, times):
        print("Current settings:")
        times.printTimes()
        val = request.form['hours']
        if val:
            times.setHours(val)

    def setDayFlask(self, times):
        print("Current settings:")
        times.printTimes()
        val = request.form['day']
        if val:
            times.setDay(val)

