import platform
import psutil

from flask import Flask, escape, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    
    return "Test me!"

@app.route("/info")
def info():
    info = "="*40 + "System Information" + "="*40 + "<p>"
    uname = platform.uname()

    info += f"System: {uname.system}" + "<br>"
    info += f"Node Name: {uname.node}" + "<br>"
    info += f"Release: {uname.release}" + "<br>"
    info += f"Version: {uname.version}" + "<br>"
    info += f"Machine: {uname.machine}" + "<br>"
    info += f"Processor: {uname.processor}" + "<br>"

    # let's print CPU information
    info += "="*40 + "CPU Info" + "="*40 + "<p>"
    # number of cores
    info += "Physical cores:" + str(psutil.cpu_count(logical=False)) + "<br>"
    info += "Total cores:" + str(psutil.cpu_count(logical=True)) + "<br>"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    info += f"Max Frequency: {cpufreq.max:.2f}Mhz" + "<br>"
    info += f"Min Frequency: {cpufreq.min:.2f}Mhz" + "<br>"
    info += f"Current Frequency: {cpufreq.current:.2f}Mhz" + "<br>"
    # CPU usage
    info += "CPU Usage Per Core:" + "<br>"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        info += f"Core {i}: {percentage}%"  + "<br>"
    info += f"Total CPU Usage: {psutil.cpu_percent()}%" + "<br>"
    
    return info

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
