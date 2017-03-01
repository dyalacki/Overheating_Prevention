f = open("/home/pi/Desktop/rando_numbers")
lines = f.read().split(',')
f.close()

vals = map(int,lines)
print lines
print vals
print cmp(vals[1],20)
