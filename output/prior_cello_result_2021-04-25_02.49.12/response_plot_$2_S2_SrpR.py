import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1.000000e-03, 1.000000e+02)
plt.ylim(1.000000e-03, 1.000000e+02)

x = np.array([1.000000e-03,1.122018e-03,1.258925e-03,1.412538e-03,1.584893e-03,1.778279e-03,1.995262e-03,2.238721e-03,2.511886e-03,2.818383e-03,3.162278e-03,3.548134e-03,3.981072e-03,4.466836e-03,5.011872e-03,5.623413e-03,6.309573e-03,7.079458e-03,7.943282e-03,8.912509e-03,1.000000e-02,1.122018e-02,1.258925e-02,1.412538e-02,1.584893e-02,1.778279e-02,1.995262e-02,2.238721e-02,2.511886e-02,2.818383e-02,3.162278e-02,3.548134e-02,3.981072e-02,4.466836e-02,5.011872e-02,5.623413e-02,6.309573e-02,7.079458e-02,7.943282e-02,8.912509e-02,1.000000e-01,1.122018e-01,1.258925e-01,1.412538e-01,1.584893e-01,1.778279e-01,1.995262e-01,2.238721e-01,2.511886e-01,2.818383e-01,3.162278e-01,3.548134e-01,3.981072e-01,4.466836e-01,5.011872e-01,5.623413e-01,6.309573e-01,7.079458e-01,7.943282e-01,8.912509e-01,1.000000e+00,1.122018e+00,1.258925e+00,1.412538e+00,1.584893e+00,1.778279e+00,1.995262e+00,2.238721e+00,2.511886e+00,2.818383e+00,3.162278e+00,3.548134e+00,3.981072e+00,4.466836e+00,5.011872e+00,5.623413e+00,6.309573e+00,7.079458e+00,7.943282e+00,8.912509e+00,1.000000e+01,1.122018e+01,1.258925e+01,1.412538e+01,1.584893e+01,1.778279e+01,1.995262e+01,2.238721e+01,2.511886e+01,2.818383e+01,3.162278e+01,3.548134e+01,3.981072e+01,4.466836e+01,5.011872e+01,5.623413e+01,6.309573e+01,7.079458e+01,7.943282e+01,8.912509e+01,1.000000e+02,])
y = np.array([2.099857e+00,2.099807e+00,2.099739e+00,2.099648e+00,2.099526e+00,2.099360e+00,2.099137e+00,2.098836e+00,2.098430e+00,2.097883e+00,2.097145e+00,2.096150e+00,2.094810e+00,2.093005e+00,2.090575e+00,2.087306e+00,2.082912e+00,2.077014e+00,2.069111e+00,2.058546e+00,2.044463e+00,2.025768e+00,2.001086e+00,1.968729e+00,1.926706e+00,1.872786e+00,1.804663e+00,1.720264e+00,1.618197e+00,1.498308e+00,1.362212e+00,1.213582e+00,1.057965e+00,9.020628e-01,7.526254e-01,6.153304e-01,4.940173e-01,3.904661e-01,3.046511e-01,2.352599e-01,1.802554e-01,1.373388e-01,1.042649e-01,7.901833e-02,5.988664e-02,4.546868e-02,3.464827e-02,2.655314e-02,2.051107e-02,1.600924e-02,1.265938e-02,1.016914e-02,8.319262e-03,6.945813e-03,5.926496e-03,5.170225e-03,4.609241e-03,4.193183e-03,3.884649e-03,3.655871e-03,3.486243e-03,3.360479e-03,3.267239e-03,3.198113e-03,3.146867e-03,3.108876e-03,3.080712e-03,3.059833e-03,3.044355e-03,3.032881e-03,3.024375e-03,3.018070e-03,3.013395e-03,3.009930e-03,3.007361e-03,3.005457e-03,3.004045e-03,3.002999e-03,3.002223e-03,3.001648e-03,3.001222e-03,3.000906e-03,3.000671e-03,3.000498e-03,3.000369e-03,3.000273e-03,3.000203e-03,3.000150e-03,3.000111e-03,3.000083e-03,3.000061e-03,3.000045e-03,3.000034e-03,3.000025e-03,3.000018e-03,3.000014e-03,3.000010e-03,3.000008e-03,3.000006e-03,3.000004e-03,3.000003e-03,])
c = "#006838"

hi_x = np.array([2.500000e-02,2.500000e-02,])
hi_y = np.array([1.622758e+00,1.622758e+00,])
lo_x = np.array([3.520956e-01,3.520956e-01,])
lo_y = np.array([1.031341e-02,1.031341e-02,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$2 / S2_SrpR")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("/root/output/response_plot_$2_S2_SrpR.png", bbox_inches='tight')
