import matplotlib.pyplot as plt

def isoterm(x, y):
    plt.plot(x, y)
    plt.show()

def W_m(x, y, c):
    w = []
    A = []
    B = []
    for i in range(len(x)):
        if(float(x[i]) > 0.3):
            break
        if(float(x[i]) > 0):
            c.append(1 / (y[i] * (x[i] - 1)))
            w.append(x[i])
    for i in range(int(len(w) / 2) + 1):
        A.append(c[i] - w[i] * (c[i + 2] - c[i]) / (w[i + 2] - w[i]))
        B.append((c[i + 2] - c[i]) / (w[i + 2] - w[i]))
    A_aver = 0
    B_aver = 0
    for i in range(len(A)):
        A_aver = sum(A) / len(A)
        B_aver = sum(B) / len(B)
    print("A =", A_aver)
    print("B =", B_aver)
    plt.plot(w, c)
    plt.show()
    return 1 / (A_aver + B_aver)


with open("data.txt", "r") as data:
    lines = data.readlines()
x = []
y = []
c = []
for line in lines:
    if float(line.split()[1]) < 0:
        continue
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))

isoterm(x, y)
Wm = W_m(x, y, c) * 0.1319 / (22.4 * 28)
print("Wm =", Wm)
Na = 6.002 * 10**23  # 1 / моль
Acs = 16.2 / 10**(20)  # м
M = 28  # г / моль
m = 0.1319 # г масса образца
Pa = 10 ** 5
V_ads = 244.6359 / 10 ** 6
V_m = 34.7# cm^3/mol
R = 8.31
T = 273
Ss = Wm * Na * Acs / M
S_por = Ss / m
V_por = Pa * V_ads * V_m / (R * T * m)
r_por = 2 * V_por * 10 ** (-6) / S_por
print("V_por =", V_por)
print("S_por =", S_por)
print("r_por =", r_por)
