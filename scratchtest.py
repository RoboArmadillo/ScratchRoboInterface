#scratch robot first test
#working with some caveats

import scratch, time, random, os, thread

def runscratch():
    os.system("scratch scratchrobot.sb")
thread.start_new_thread(runscratch,())

time.sleep(20)
print "Running scratch thing"
s = scratch.Scratch()
rightmotor = 0
leftmotor = 0
time.sleep(1)
s.broadcast('start')
msg=s.receive()
while msg[1] != 'ready':
    msg=s.receive()
    print msg

counter = 0
while counter < 10:
    msg = s.receive()
    print msg
    time.sleep(0.5)
    if msg[1] == 'look':
        s.sensorupdate({'markersseen' : 1})
        time.sleep(0.5)
        print s.receive()
        s.sensorupdate({'angle' : 2})
        time.sleep(0.5)
        print s.receive()
        s.sensorupdate({'distance' : random.randint(-30,30)})
        time.sleep(0.5)
        print s.receive()
        s.sensorupdate({'stop' : 1})
        time.sleep(0.5)
        print s.receive()
    elif msg[1] == 'search':
        rightmotor = s.receive()[1]
        time.sleep(0.5)
        leftmotor = s.receive()[1]
    elif msg[1] == 'turnleft':
        rightmotor = s.receive()[1]
        time.sleep(0.5)
        leftmotor = s.receive()[1]
    elif msg[1] == 'turnright':
        rightmotor = s.receive()[1]
        time.sleep(0.5)
        leftmotor = s.receive()[1]
    elif msg[1] == 'forward':
        rightmotor = s.receive()[1]
        time.sleep(0.5)
        leftmotor = s.receive()[1]
    print rightmotor
    print leftmotor
    counter +=1
s.broadcast("stop")
time.sleep(0.5)
s.receive()
        
