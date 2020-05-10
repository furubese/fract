import matplotlib.pyplot as plt
import math


def prinz(strings, debug):
    if debug:
        print(strings)
    else:
        pass


class Draw:
    def __init__(self, p, debug=False):
        self.p = p
        self.sp = p
        self.rp = []
        self.debug = debug

    def bunkatu(self, kakudo):
        p = []
        prinz("==self.p==", self.debug)
        prinz(self.p, self.debug)
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
        prinz("==bunkatu==", self.debug)
        prinz("rp = {}".format(self.rp), self.debug)

    def cyck(self, kakudo, plist):
        p = []
        x, y = 0, 1
        for i in range(len(plist)):
            p.append([plist[i][x] * math.cos(kakudo) - plist[i][y] * math.sin(kakudo),
                      plist[i][x] * math.sin(kakudo) + plist[i][y] * math.cos(kakudo)])
        prinz("==cyck==", self.debug)
        prinz(p, self.debug)
        return p

    def de_cyck(self, kakudo, plist):
        p = []
        x, y = 0, 1
        for i in range(len(plist)):
            p.append([plist[i][x] * math.cos(kakudo) + plist[i][y] * math.sin(kakudo),
                      - plist[i][x] * math.sin(kakudo) + plist[i][y] * math.cos(kakudo)])
        prinz("==de_cyck==", self.debug)
        prinz(p, self.debug)
        return p

    def sai(self, kakudo):
        sp = []
        i = 0
        while i + 1 < len(self.rp):
            kaku = math.atan((self.rp[i + 1][1] - self.rp[i][1]) / (self.rp[i + 1][0] - self.rp[i][0]))
            prinz("kaku = {}".format(kaku), self.debug)
            p = [self.rp[i], self.rp[i + 1]]
            rps = Draw(p)
            rps.p = rps.de_cyck(kaku, rps.p)
            rps.bunkatu(kakudo)
            rps.rp = rps.cyck(kaku, rps.rp)
            sp.extend(rps.rp[0:-1])
            prinz("sp = {}".format(sp), self.debug)
            i += 1
        prinz("self.rp = {}".format(self.rp), self.debug)
        sp.append(self.rp[-1])
        self.rp = sp

    def cop(self, kakudo, w):
        x, y = 0, 1
        p = []
        for i in range(len(self.rp)):
            p.append([self.rp[i][x], self.rp[i][y]])
        for g in range(w):
            cyd = Draw(0).cyck((math.pi / 1 * 3 + kakudo) * (g + 1), p)
            sp = []
            for i in range(len(cyd)):
                sp.append([cyd[i][x] + self.rp[-1][x], cyd[i][y] + self.rp[-1][y]])
            prinz("===cop===", self.debug)
            prinz(sp, self.debug)
            self.rp.extend(sp)

    def spril(self, kakudo, poi, k):
        p = [[0.0, 0.0], [poi[0], poi[1]]]
        for g in range(100):
            p = [[0.0, 0.0], [p[1][0] * 0.99, p[1][1]]]
            dle = Draw(p, False)
            dle.rp = p
            for i in range(k):
                dle.sai(kakudo)
                print("{}.".format(i))
            cyd = Draw(0).cyck((math.pi / 1 * 3 + kakudo) * (g + 1), dle.rp)
            sp = []
            for i in range(len(dle.rp)):
                sp.append([cyd[i][0] + self.rp[-1][0], cyd[i][1] + self.rp[-1][1]])
            prinz("===spril===", self.debug)
            prinz(sp, self.debug)
            self.rp.extend(sp)

    def draw(self):
        x = []
        y = []
        for i in self.rp:
            x.append(i[0])
            y.append(i[1])
        for i in range(len(x)):
            prinz("{:<20.9f}, {:<20.9f}".format(x[i], y[i]), self.debug)
        prinz("x = {}\ny = {}".format(x, y), self.debug)
        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    point = [0.0, 0.0], [1.0, 0.0]
    kei = 2
    kakus = math.pi * 1 / 180
    dl = Draw(point, False)
    dl.rp = point
    for i in range(kei):
        dl.sai(kakus * 60)
        print("{}.".format(i))
    dl.cop(kakus * 60, 2)
    dl.spril(kakus * 60, [point[1][0], point[1][1]], kei)
    dl.draw()