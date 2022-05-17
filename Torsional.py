import math
class Points(object):
    def __init__(self, A, B, C):
        self.A=A
        self.B=B
        self.C=C

    def __sub__(self, no):
        return  Points((self.A-no.A),(self.B-no.B),(self.C-no.C))

    def dot(self, no):
        return (self.A*no.A)+(self.B*no.B)+(self.C*no.C)

    def cross(self, no):
        return Points((self.B*no.C-self.C*no.B),(self.C*no.A-self.A*no.C),(self.A*no.B-self.B*no.A))
        
    def absolute(self):
        return pow((self.A ** 2 + self.B ** 2 + self.C ** 2), 0.5)
if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
    
