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
        sa = self.p[0][x], self.p[0][y]
        ln = (self.p[1][x] - self.p[0][x]) / 2
        N1 = ln / (1 + math.sin(kakudo / 2))
        N2 = ln * 2 - N1
        tate = math.cos(kakudo / 2) * N1 + sa[y]
        p.append([self.p[0][x], self.p[0][y]])
        p.append([N1 + sa[x], sa[y]])
        p.append([ln + sa[x], tate])
        p.append([N2 + sa[x], sa[y]])
        p.append([self.p[1][x], self.p[1][y]])
        self.rp = p
        print("==bunkatu==")
        print("rp = {}".format(self.rp))

    def cyck(self, kakudo, plist):
        p = []
        x, y = 0, 1
        for i in range(len(plist)):
            p.append([plist[i][x] * math.cos(kakudo) - plist[i][y] * math.sin(kakudo),
                      plist[i][x] * math.sin(kakudo) + plist[i][y] * math.cos(kakudo)])
        print("==cyck==")
        print(p)
        return p

    def de_cyck(self, kakudo, plist):
        p = []
        x, y = 0, 1
        for i in range(len(plist)):
            p.append([plist[i][x] * math.cos(kakudo) + plist[i][y] * math.sin(kakudo),
                      - plist[i][x] * math.sin(kakudo) + plist[i][y] * math.cos(kakudo)])
        print("==de_cyck==")
        print(p)
        return p

    def sai(self, kakudo):
        sp = []
        i = 0
        while i + 1 < len(self.rp):
            kaku = math.atan((self.rp[i + 1][1] - self.rp[i][1]) / (self.rp[i + 1][0] - self.rp[i][0]))
            print("kaku = {}".format(kaku))
            p = [self.rp[i], self.rp[i + 1]]
            rps = Draw(p)
            rps.p = rps.de_cyck(kaku, rps.p)
            rps.bunkatu(kakudo)
            rps.rp = rps.cyck(kaku, rps.rp)
            sp.extend(rps.rp[0:-1])
            print("sp = {}".format(sp))
            i += 1
        sp.append(self.rp[-1])
        self.rp = sp

    def draw(self):
        x = []
        y = []
        for i in self.rp:
            x.append(i[0])
            y.append(i[1])
        for i in range(len(x)):
            print("{:<20.9f}, {:<20.9f}".format(x[i], y[i]))
        print("x = {}\ny = {}".format(x, y))
        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    point = [0.0, 0.0], [1.0, 0.0]
    dl = Draw(point)
    dl.bunkatu(math.pi / 6)
    dl.sai(math.pi / 6)
    dl.draw()