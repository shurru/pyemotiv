import numpy as np
import matplotlib.pyplot as plt

SIZE = 100
R1 = 0.5
R2 = 0.75

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
fig.canvas.set_window_title('broken spiral')
line1, = ax.plot([], [], '-k', label='black')
line2, = ax.plot([], [], '-r', label='red')
A= []
B=[]
ax.legend()

for i in range(0, SIZE):
    A.append(R1 * i * np.sin(i))
    B.append(R2 * i * np.cos(i))
    line1.set_ydata(A)
    line1.set_xdata(range(len(A)))
    line2.set_ydata(B)
    line2.set_xdata(range(len(B)))
    ax.relim()
    ax.autoscale_view()
    plt.draw()
