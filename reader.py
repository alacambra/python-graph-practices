__author__ = 'alacambra'
import matplotlib.pyplot as plt
import numpy as np

data30 = np.loadtxt("data/channel-n50000-c400-items30", skiprows=1, delimiter="\t",  usecols=(4, 5))
data10 = np.loadtxt("data/channel-n50000-c400-items10", skiprows=1, delimiter="\t",  usecols=(4, 5))
data_t10 = np.loadtxt("data/channel-t60-c400-items10", skiprows=1, delimiter="\t",  usecols=(4, 5))

r = range(len(data_t10))
print len(r)
legend = ["ctime", "dtime", "ttime", "wait"]
i = 0

plt.title("total time")
# plt.plot(r, data30.T[0], label="30 channel items")
# plt.plot(r, data10.T[0], label="10 channel items")
plt.plot(r, data_t10.T[0], label="10 channel items")

# for c in data.T:
#     plt.plot(r, c, label=legend[i])
#     i += 1

plt.legend()
plt.show()