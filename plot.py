import matplotlib.pyplot as plt
#  圧縮率
x = [4,9,16,25,36,64,100,144,225,400]
y = [188.3,186.2,171.1,160.2,150.7,132.4,126,120.1,111,102.3]

plt.title("comparision of 'rate' and 'size'")
plt.xlabel("compression rate(1/x)")
plt.ylabel("data size(KB)")
plt.plot(x,y)

plt.savefig("comparision of 'rate' and 'size'")