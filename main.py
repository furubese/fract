import matplotlib.pyplot as plt
import math


def kaku(x, y, waru, sita, k):
    a = []
    b = []
    wanlen = (x[1] - x[0]) / waru
    for i in range(waru + 1):
        b.append(y[0])
    for i in range(waru + 1):
        a.append(x[0] + wanlen * i)
    a.insert(2, kaku2(a[1:-1], b[1:-1]))
    b.insert(2, wanlen * math.sin(math.pi * k / 180))
    i = 0
    ra = []
    rb = []
    while i < len(a):
        ra.append(a[i] * math.cos(sita) - b[i] * math.sin(sita))
        rb.append(a[i] * math.sin(sita) + b[i] * math.cos(sita))
        i += 1
    print(a, b)
    print(math.cos(sita))
    return ra, rb


def kaku2(x, y):
    a = []
    for i in range(2 + 1):
        a.append((x[1] - x[0]) / 2 * i + x[0])
    return a[1]


def kaku3(x, y, waru, sita, k):
    """TODO 全部書き直し"""
    ra = []
    rb = []
    i = 0
    while i < len(x):
        tmp = kaku([x[i], x[i+1]],
                       [y[i], y[i+1]], waru, sita, k)
        ra.append(x[i])
        ra.extend(tmp[0])
        ra.append(x[i+1])
        rb.append(y[i])
        rb.extend(tmp[1])
        rb.append(y[i + 1])
        i += 2


if __name__ == "__main__":
    xz = [0.0, 1.0]
    yz = [0.0, 0.0]
    gx = 0
    gy = 0
    tmp_x = []
    tmp_y = []
    rx = []
    ry = []
    w = 3
    kakudo = 90
    kakudo2 = math.pi * 216 / 180
    for i in range(5):
        tmp_x = (kaku(xz, yz, w, kakudo2 * i, kakudo)[0])
        tmp_y = (kaku(xz, yz, w, kakudo2 * i, kakudo)[1])
        for g in range(len(tmp_x)):
            tmp_x[g] = tmp_x[g] + gx
            tmp_y[g] = tmp_y[g] + gy
        gx, gy = tmp_x[-1], tmp_y[-1]
        rx.extend(tmp_x)
        ry.extend(tmp_y)

    print(xz, yz)
    print("x = {}\ny = {}".format(rx, ry))
    plt.plot(rx, ry)
    plt.show()
