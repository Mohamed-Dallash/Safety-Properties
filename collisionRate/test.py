import jpype
import jpype.imports

import time

jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=tpdejavu.jar:CollisionRate.jar")

monitor = jpype.JClass("collision_rate.TraceMonitor")

file = open("log.csv")
while True:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    monitor.eval(line)
