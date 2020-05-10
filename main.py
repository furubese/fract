import matplotlib.pyplot as plt
import math

class Draw:
    def __init__(self, p):
        self.p = p
        self.sp = p
        self.rp = []

    def bunkatu(self, kakudo):
        p = []
        print("==self.p==")
        print(self.p)
        x, y = 0, 1
        sa = self.p[0][x]
        ln = (self.p[1][x] - self.p[0][x]) / 2
        N1 = ln / (1 + math.sin(kakudo / 2))
        N2 = ln * 2 - N1
        tate = math.cos(kakudo / 2) * N1
        print("yaaaaptate={}".format(tate))
        p.append([self.p[0][x], self.p[0][y]])
        p.append([N1 + sa, 0.0])
        p.append([ln + sa, tate])
        p.append([N2 + sa, 0.0])
        p.append([self.p[1][x], self.p[1][y]])
        self.rp = p
        print("==bunkatu==")
        print("rp = {}".format(self.rp))

    def cyck(self, kakudo, *plist):
        p = []
        x, y = 0, 1
        for i in range(len(*plist)):
            p.append([self.rp[i][x] * math.cos(kakudo) - self.rp[i][y] * math.sin(kakudo),
                      self.rp[i][x] * math.sin(kakudo) + self.rp[i][y] * math.cos(kakudo)])
        print("==cyck==")
        print(p)
        return p

    def de_cyck(self, kakudo, *plist):
        p = []
        x, y = 0, 1
        for i in range(len(*plist)):
            p.append([self.p[i][x] * math.cos(kakudo) + self.p[i][y] * math.sin(kakudo),
                      - self.p[i][x] * math.sin(kakudo) + self.p[i][y] * math.cos(kakudo)])
        print("==de_cyck==")
        print(p)
        return p

    def sai(self, kakudo):
        sp = []
        try:
            i = 0
            while i < len(self.rp):
                sp.append(self.rp[i])
                p = [self.rp[i], self.rp[i + 1]]
                rps = Draw(p)
                kaku = math.atan((self.rp[i + 1][1] - self.rp[i][1]) / (self.rp[i + 1][0] - self.rp[i][0]))
                rps.p = rps.de_cyck(kaku, rps.p[0])
                rps.bunkatu(kakudo)
                rps.rp = rps.cyck(kaku, rps.rp)
                sp.extend(rps.rp)
                sp.append(self.rp[i + 1])
                print("sp = {}".format(sp))
                i += 1
        except IndexError:
            pass
        print("==sp==")
        print(sp)
        self.rp = sp
        print("==sai==")
        print("rp = {}".format(self.rp))

    def draw(self):
        x = []
        y = []
        for i in self.rp:
            x.append(i[0])
            y.append(i[1])
        print("x = {}\ny = {}".format(x, y))
        plt.plot(x, y)
        plt.show()

if __name__ == "__main__":
    point = [0.0, 0.0], [1.0, 0.0]
    dl = Draw(point)
    dl.bunkatu(math.pi / 6)
    dl.sai(math.pi / 6)
    dl.draw()