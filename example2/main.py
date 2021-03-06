class PrintableTransportation(object):
    def __str__(self):
        return "%s %s" % (getattr(self, strattr), self.typename)

class Bus(object):
    typename = 'bus'
    def __init__(self, name):
       self.name = name 

class Train(object):
    typename = 'train'
    def __init__(self, line):
       self.line = line 

class Plane(object):
    typename = 'flight'
    def __init__(self, callsign):
       self.callsign = callsign 

b1 = Bus("LAX Flyaway")
t1 = Train("Pacific Coastliner")
p1 = Plane("El Mariachi")

print("I took the {} to the {} and then hopped on the {}.".format(b1, t1, p1))
