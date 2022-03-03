import time
from datetime import timedelta

# Hora actual
myTime = time.localtime()
actualHour = myTime.tm_hour
actualMinute = myTime.tm_min
actualSecond = myTime.tm_sec

# Hora de salida
leaveHour = 19
leaveMinute = 0
leaveSecond = 0

# Resta de horas con datetime
restTime = timedelta(0,leaveSecond,0,0,leaveMinute - 5,leaveHour) \
           - timedelta(0,actualSecond,0,0,actualMinute,actualHour)

if restTime <= timedelta(0,0,0,0,0,0):
    print("Hora de ir a casa")
else:
    print("Todavía te quedan", restTime)