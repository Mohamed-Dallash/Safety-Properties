import jpype
import jpype.imports

import time

jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=tpdejavu.jar:SafeDistance.jar")

monitor = jpype.JClass("safe_distance.TraceMonitor")

file = open("log.csv")
while True:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    monitor.eval(line)
