import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$1 / P3_PhlF")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [3.699484e-04,3.255546e-04,2.663628e-04,2.071711e-04,3.255546e-04,4.735339e-04,1.923731e-04,6.215132e-04,2.663628e-04,4.735339e-04,7.103008e-04,4.587360e-04,3.995442e-04,5.179277e-04,4.291401e-04,4.143422e-04,6.067153e-04,4.587360e-04,4.883318e-04,5.327256e-04,4.735339e-04,4.883318e-04,5.179277e-04,5.475236e-04,5.623215e-04,9.618657e-04,8.434822e-04,1.154239e-03,1.405804e-03,1.479793e-03,1.361410e-03,1.435400e-03,1.065451e-03,7.250988e-04,8.138864e-04,1.346612e-03,1.598177e-03,1.953327e-03,2.116105e-03,2.397265e-03,1.642571e-03,1.894136e-03,1.923731e-03,2.175296e-03,3.151960e-03,2.811607e-03,2.397265e-03,2.130903e-03,3.018779e-03,3.921453e-03,3.344333e-03,2.959587e-03,3.877059e-03,4.661349e-03,3.240748e-03,4.528168e-03,5.356852e-03,3.921453e-03,5.682407e-03,5.312458e-03,5.859982e-03,6.895837e-03,6.141143e-03,7.295382e-03,7.680128e-03,7.946491e-03,9.293103e-03,7.265786e-03,8.923154e-03,1.040295e-02,1.058052e-02,1.043254e-02,1.137961e-02,1.220830e-02,1.263744e-02,1.340693e-02,1.420602e-02,1.530106e-02,1.604096e-02,1.612975e-02,1.666247e-02,1.945928e-02,1.820146e-02,1.932610e-02,2.166418e-02,2.139781e-02,2.272963e-02,2.312917e-02,2.496412e-02,2.426861e-02,2.460896e-02,2.687305e-02,2.638472e-02,2.740577e-02,2.838244e-02,2.697663e-02,2.725779e-02,2.835284e-02,2.537846e-02,2.583719e-02,2.407624e-02,2.380988e-02,2.240407e-02,2.025837e-02,1.866020e-02,1.581899e-02,1.376208e-02,1.203072e-02,1.099487e-02,8.819569e-03,7.472957e-03,6.081951e-03,4.720541e-03,3.729079e-03,2.856001e-03,2.086509e-03,1.583379e-03,1.361410e-03,9.766637e-04,9.322699e-04,9.766637e-04,9.322699e-04,5.327256e-04,5.771194e-04,5.919174e-04,3.847463e-04,3.403525e-04,3.699484e-04,3.107566e-04,3.551504e-04,2.515649e-04,1.775752e-04,1.923731e-04,1.923731e-04,1.775752e-04,1.035855e-04,2.219690e-04,1.923731e-04,8.878761e-05,7.398967e-05,1.183835e-04,1.331814e-04,1.183835e-04,1.035855e-04,1.331814e-04,7.398967e-05,1.479793e-05,5.919174e-05,4.439380e-05,2.959587e-05,5.919174e-05,4.439380e-05,0.000000e+00,2.959587e-05,5.919174e-05,4.439380e-05,4.439380e-05,7.398967e-05,2.959587e-05,1.479793e-05,0.000000e+00,2.959587e-05,1.479793e-05,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,4.439380e-05,0.000000e+00,0.000000e+00,4.439380e-05,1.479793e-05,0.000000e+00,1.479793e-05,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.479793e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.350241e-06,0.000000e+00,0.000000e+00,0.000000e+00,2.350241e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,9.860166e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.350241e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,2.350241e-06,2.350241e-06,0.000000e+00,7.509925e-06,0.000000e+00,0.000000e+00,7.509925e-06,0.000000e+00,2.350241e-06,0.000000e+00,4.700482e-06,2.350241e-06,7.509925e-06,1.972033e-05,1.501985e-05,0.000000e+00,7.509925e-06,9.860166e-06,2.252977e-05,7.509925e-06,1.501985e-05,2.207057e-05,1.456065e-05,7.050724e-06,0.000000e+00,4.700482e-06,4.700482e-06,9.860166e-06,7.050724e-06,2.207057e-05,1.221041e-05,3.003970e-05,2.207057e-05,3.474018e-05,3.238994e-05,1.501985e-05,1.926113e-05,3.944066e-05,2.207057e-05,3.944066e-05,5.962020e-05,3.474018e-05,3.709042e-05,4.649139e-05,5.681075e-05,4.930083e-05,5.446051e-05,5.211027e-05,4.740979e-05,5.962020e-05,3.474018e-05,1.456065e-05,4.930083e-05,7.464004e-05,6.105203e-05,6.810276e-05,9.952006e-05,1.033021e-04,6.902116e-05,3.944066e-05,7.372164e-05,6.902116e-05,6.575252e-05,1.234817e-04,9.155093e-05,8.358181e-05,1.535214e-04,5.635155e-05,7.607188e-05,5.165107e-05,9.063253e-05,6.432068e-05,1.061116e-04,7.888133e-05,4.930083e-05,4.225011e-05,6.856196e-05,7.280324e-05,2.677106e-05,2.677106e-05,3.709042e-05,4.649139e-05,2.912130e-05,2.958050e-05,1.221041e-05,9.860166e-06,5.446051e-05,3.193074e-05,7.509925e-06,7.509925e-06,7.050724e-06,7.050724e-06,1.501985e-05,1.221041e-05,0.000000e+00,3.193074e-05,2.207057e-05,3.238994e-05,2.488001e-05,2.488001e-05,3.474018e-05,5.165107e-05,6.713012e-05,3.238994e-05,8.495941e-05,5.726995e-05,8.495941e-05,1.722691e-04,1.173494e-04,2.501778e-04,3.496978e-04,4.421671e-04,4.200966e-04,5.027057e-04,6.153546e-04,1.005871e-03,1.142940e-03,1.367779e-03,1.595886e-03,1.886936e-03,2.264837e-03,2.435674e-03,3.275462e-03,3.731272e-03,4.449010e-03,5.023196e-03,5.778997e-03,6.985448e-03,7.538023e-03,9.138125e-03,1.048824e-02,1.303437e-02,1.558383e-02,1.713922e-02,2.088074e-02,2.320787e-02,2.670682e-02,3.116842e-02,3.376205e-02,3.684350e-02,4.114604e-02,4.428490e-02,4.495291e-02,4.635638e-02,4.668323e-02,4.735421e-02,4.624858e-02,4.439966e-02,4.160673e-02,3.920771e-02,3.505926e-02,3.110893e-02,2.828376e-02,2.438400e-02,2.061474e-02,1.828525e-02,1.579595e-02,1.374873e-02,1.138399e-02,9.663487e-03,7.952193e-03,6.431699e-03,6.070167e-03,4.859771e-03,4.260731e-03,3.692406e-03,3.011650e-03,2.451591e-03,2.257819e-03,2.010071e-03,1.681471e-03,1.458766e-03,1.144618e-03,1.187787e-03,8.824722e-04,7.772790e-04,6.842962e-04,6.532297e-04,6.649809e-04,6.179760e-04,4.982764e-04,4.677233e-04,4.123444e-04,3.330039e-04,2.784891e-04,1.719183e-04,2.343480e-04,1.949073e-04,1.117847e-04,1.094345e-04,1.234817e-04,6.810276e-05,6.013363e-05,6.529332e-05,6.810276e-05,7.091220e-05,5.354211e-05,3.147154e-05,1.456065e-05,7.050724e-06,9.400965e-06,0.000000e+00,0.000000e+00,1.221041e-05,9.860166e-06,0.000000e+00,7.050724e-06,7.509925e-06,2.350241e-06,0.000000e+00,0.000000e+00,2.350241e-06,0.000000e+00,0.000000e+00,2.350241e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_P3_PhlF.png", bbox_inches='tight')
