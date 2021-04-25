import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([4.100000e+00,4.100000e+00,4.100000e+00,4.100000e+00,4.100000e+00,4.100000e+00,4.100000e+00,4.099999e+00,4.099999e+00,4.099999e+00,4.099998e+00,4.099997e+00,4.099995e+00,4.099992e+00,4.099988e+00,4.099980e+00,4.099969e+00,4.099952e+00,4.099925e+00,4.099882e+00,4.099815e+00,4.099711e+00,4.099547e+00,4.099290e+00,4.098888e+00,4.098258e+00,4.097271e+00,4.095726e+00,4.093308e+00,4.089525e+00,4.083612e+00,4.074382e+00,4.060005e+00,4.037684e+00,4.003205e+00,3.950358e+00,3.870323e+00,3.751279e+00,3.578884e+00,3.338653e+00,3.021246e+00,2.630121e+00,2.187550e+00,1.732588e+00,1.308769e+00,9.486891e-01,6.659335e-01,4.573207e-01,3.103850e-01,2.102400e-01,1.435064e-01,9.970240e-02,7.123317e-02,5.284947e-02,4.102786e-02,3.344639e-02,2.859258e-02,2.548851e-02,2.350482e-02,2.223770e-02,2.142852e-02,2.091189e-02,2.058207e-02,2.037153e-02,2.023715e-02,2.015136e-02,2.009661e-02,2.006166e-02,2.003936e-02,2.002512e-02,2.001603e-02,2.001023e-02,2.000653e-02,2.000417e-02,2.000266e-02,2.000170e-02,2.000108e-02,2.000069e-02,2.000044e-02,2.000028e-02,2.000018e-02,2.000011e-02,2.000007e-02,2.000005e-02,2.000003e-02,2.000002e-02,2.000001e-02,2.000001e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,2.000000e-02,])
c = "#f9a427"

hi_x = np.array([7.410686e-02,])
hi_y = np.array([3.690042e+00,])
lo_x = np.array([5.410811e+00,1.686552e+00,3.798366e+00,])
lo_y = np.array([2.000197e-02,2.018609e-02,2.000785e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$1 / P2_PhlF")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$1_P2_PhlF.png", bbox_inches='tight')
