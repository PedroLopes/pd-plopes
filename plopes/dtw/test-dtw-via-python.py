import dtw_distance
from random import randint

dtw = dtw_distance.DtwDistance()

x = []
for i in range(0,1000):
    x.append(randint(0,9))

y = []
for i in range(0,1000):
    y.append(randint(0,9))

print("set_x: " + str(dtw.set_x(x)))
print("set_y: " + str(dtw.set_y(y)))
print("get_x: " + str(dtw.get_x()))
print("get_y: " + str(dtw.get_y()))
print("analyze: " + str(dtw.analyze()))
print("set_x: " + str(dtw.set_x(x)))
print("set_y: " + str(dtw.set_y(x)))
print("get_x: " + str(dtw.get_x()))
print("get_y: " + str(dtw.get_y()))
print("analyze: " + str(dtw.analyze()))
