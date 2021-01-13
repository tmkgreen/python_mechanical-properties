#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:51:23 2020

@author: tmkgreen
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:06:30 2020

@author: tmkgreen
"""

import seaborn as sns
import matplotlib.lines as mlines
import matplotlib.patches as patches
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'
import matplotlib.pyplot as plt

# =============================================================================
# Heat 99/1 ASB
# =============================================================================
YS_RT_99_ASB = 129.297*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
UTS_RT_99_ASB = 195.589*6.89476
UE_RT_99_ASB = 5.9389
TE_RT_99_ASB = 17.2387

YS_330_99_ASB = 141.134*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
UTS_330_99_ASB = 176.77*6.89476
UE_330_99_ASB = 5.9121
TE_330_99_ASB = 15.313

YS_550_99_ASB = 125.89*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
UTS_550_99_ASB = 150.04*6.89476
UE_550_99_ASB = 4.05
TE_550_99_ASB = 16.04

# =============================================================================
# Heat 99/1 HT1045
# =============================================================================
YS_RT_99_1045_ave = 63.94*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_RT_99_1045_std = 18.342*6.89476
UTS_RT_99_1045_ave = 97.335*6.89476
UTS_RT_99_1045_std = 3.2456*6.89476
UE_RT_99_1045_ave = 8.3495
UE_RT_99_1045_std = 0.74034
TE_RT_99_1045_ave = 23.7967
TE_RT_99_1045_std = 1.02714

YS_330_99_1045_ave = 66.835*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_330_99_1045_std = 3.03348*6.89476
UTS_330_99_1045_ave = 77.935*6.89476
UTS_330_99_1045_std = 2.5668*6.89476
UE_330_99_1045_ave = 2.98465
UE_330_99_1045_std = 0.7575
TE_330_99_1045_ave = 15.4975
TE_330_99_1045_std = 2.830478

YS_550_99_1045_ave = 26.065*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_550_99_1045_std = 3.63840*6.89476
UTS_550_99_1045_ave = 60.194*6.89476
UTS_550_99_1045_std = 0.5572*6.89476
UE_550_99_1045_ave = 2.7525
UE_550_99_1045_std = 0.09828
TE_550_99_1045_ave = 29.3485
TE_550_99_1045_std = 1.15753

# =============================================================================
# Heat 99/1 HT1100
# =============================================================================
YS_RT_99_1100_ave = 77.96*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_RT_99_1100_std = 2.03647*6.89476
UTS_RT_99_1100_ave = 96.944*6.89476
UTS_RT_99_1100_std = 0.27436*6.89476
UE_RT_99_1100_ave = 7.50655
UE_RT_99_1100_std = 0.08266
TE_RT_99_1100_ave = 21.08
TE_RT_99_1100_std = 1.3025

YS_330_99_1100_ave = 38.275*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_330_99_1100_std = 2.72236*6.89476
UTS_330_99_1100_ave = 82.55*6.89476
UTS_330_99_1100_std = 2.0648*6.89476
UE_330_99_1100_ave = 4.57
UE_330_99_1100_std = 0.155563
TE_330_99_1100_ave = 16.275
TE_330_99_1100_std = 1.11016

YS_550_99_1100_ave = 54.8495*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_550_99_1100_std = 5.1767*6.89476
UTS_550_99_1100_ave = 63.08*6.89476
UTS_550_99_1100_std = 0.31113*6.89476
UE_550_99_1100_ave = 2.263
UE_550_99_1100_std = 0.4299
TE_550_99_1100_ave = 23.935
TE_550_99_1100_std = 4.08


# =============================================================================
# Heat 95/5 ASB
# =============================================================================
YS_RT_95_ASB = 144.66*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
UTS_RT_95_ASB = 183.76*6.89476
UE_RT_95_ASB = 4.1875
TE_RT_95_ASB = 16.1676

YS_330_95_ASB = 141.232*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
UTS_330_95_ASB = 184.068*6.89476
UE_330_95_ASB = 4.8175
TE_330_95_ASB = 13.8416

YS_550_95_ASB = 123.38*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
UTS_550_95_ASB = 145.68*6.89476
UE_550_95_ASB = 2.829
TE_550_95_ASB = 13.07

# =============================================================================
# Heat 95/5 HT1045
# =============================================================================
YS_RT_95_1045_ave = 52.62*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_RT_95_1045_std = 0.89095*6.89476
UTS_RT_95_1045_ave = 96.715*6.89476
UTS_RT_95_1045_std = 1.407*6.89476
UE_RT_95_1045_ave = 8.28365
UE_RT_95_1045_std = 0.620627
TE_RT_95_1045_ave = 22.87645
TE_RT_95_1045_std = 1.8408

YS_330_95_1045_ave = 81.405*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_330_95_1045_std = 16.99*6.89476
UTS_330_95_1045_ave = 79.698*6.89476
UTS_330_95_1045_std = 2.13829*6.89476
UE_330_95_1045_ave = 4.011
UE_330_95_1045_std = 0.43699
TE_330_95_1045_ave = 18.31
TE_330_95_1045_std = 1.1597

YS_550_95_1045_ave = 57.28*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_550_95_1045_std = 2.03647*6.89476
UTS_550_95_1045_ave = 62.29*6.89476
UTS_550_95_1045_std = 0.91924*6.89476
UE_550_95_1045_ave = 2.038
UE_550_95_1045_std = 0.22699
TE_550_95_1045_ave = 22.595
TE_550_95_1045_std = 2.3547

# =============================================================================
# Heat 95/5 HT1100
# =============================================================================
YS_RT_95_1100_ave = 75.9405*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_RT_95_1100_std = 21.587*6.89476
UTS_RT_95_1100_ave = 96.39765*6.89476
UTS_RT_95_1100_std = 3.78111*6.89476
UE_RT_95_1100_ave = 6.6218
UE_RT_95_1100_std = 0.96336
TE_RT_95_1100_ave = 20.253
TE_RT_95_1100_std = 0.627628

YS_330_95_1100_ave = 55.055*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_330_95_1100_std = 22.09709*6.89476
UTS_330_95_1100_ave = 82.44*6.89476
UTS_330_95_1100_std = 0.834386*6.89476
UE_330_95_1100_ave = 3.9695
UE_330_95_1100_std = 0.74458
TE_330_95_1100_ave = 17.085
TE_330_95_1100_std = 0.98288

YS_550_95_1100_ave = 39.295*6.89476 #mpa, Tensile stress at Yield (Offset 0.2 %)
YS_550_95_1100_std = 25.717*6.89476
UTS_550_95_1100_ave = 60.155*6.89476
UTS_550_95_1100_std = 0.77074*6.89476
UE_550_95_1100_ave = 2.6955
UE_550_95_1100_std = 1.4234
TE_550_95_1100_ave = 27.96
TE_550_95_1100_std = 4.9639

a4_dims = (6,6)
fig,[[ax0,ax1],[ax2,ax3]] =  plt.subplots(2,2,constrained_layout=True,figsize=a4_dims)

#first subplot
ax0.plot(1, YS_RT_99_ASB, color='c',marker='^',alpha=0.6)
ax0.plot(1, YS_RT_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax0.errorbar(2,YS_RT_99_1045_ave,YS_RT_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax0.errorbar(2,YS_RT_95_1045_ave,YS_RT_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax0.errorbar(3,YS_RT_99_1100_ave,YS_RT_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax0.errorbar(3,YS_RT_95_1100_ave,YS_RT_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax0.plot(5, YS_330_99_ASB, color='c',marker='^',alpha=0.6)
ax0.plot(5, YS_330_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax0.errorbar(6,YS_330_99_1045_ave,YS_330_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax0.errorbar(6,YS_330_95_1045_ave,YS_330_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax0.errorbar(7,YS_330_99_1100_ave,YS_330_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax0.errorbar(7,YS_330_95_1100_ave,YS_330_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax0.plot(9, YS_550_99_ASB, color='c',marker='^',alpha=0.6)
ax0.plot(9, YS_550_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax0.errorbar(10,YS_550_99_1045_ave,YS_550_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax0.errorbar(10,YS_550_95_1045_ave,YS_550_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax0.errorbar(11,YS_550_99_1100_ave,YS_550_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax0.errorbar(11,YS_550_95_1100_ave,YS_550_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax0.grid(color='gray',linestyle='--',which='major',axis='y',alpha=0.2)
ax0.axvline(x=4,color='k',lw=1)
ax0.axvline(x=8,color='k',lw=1)
ax0.set_xlim(0,12)
ax0.set_ylim(0,1400)

ax0.set_ylabel('Yield Strength (MPa)')
ax0.set_xlabel('Temperature (°C)')
ax0.set_xticks([2,6,10])
ax0.set_xticklabels(['RT','330°C','550°C'])
ax0.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=True) 

#second subplot
ax1.plot(1, UTS_RT_99_ASB, color='c',marker='^',alpha=0.6)
ax1.plot(1, UTS_RT_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax1.errorbar(2,UTS_RT_99_1045_ave,UTS_RT_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax1.errorbar(2,UTS_RT_95_1045_ave,UTS_RT_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax1.errorbar(3,UTS_RT_99_1100_ave,UTS_RT_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax1.errorbar(3,UTS_RT_95_1100_ave,UTS_RT_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax1.plot(5, UTS_330_99_ASB, color='c',marker='^',alpha=0.6)
ax1.plot(5, UTS_330_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax1.errorbar(6,UTS_330_99_1045_ave,UTS_330_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax1.errorbar(6,UTS_330_95_1045_ave,UTS_330_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax1.errorbar(7,UTS_330_99_1100_ave,UTS_330_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax1.errorbar(7,UTS_330_95_1100_ave,UTS_330_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax1.plot(9, UTS_550_99_ASB, color='c',marker='^',alpha=0.6)
ax1.plot(9, UTS_550_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax1.errorbar(10,UTS_550_99_1045_ave,UTS_550_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax1.errorbar(10,UTS_550_95_1045_ave,UTS_550_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax1.errorbar(11,UTS_550_99_1100_ave,UTS_550_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax1.errorbar(11,UTS_550_95_1100_ave,UTS_550_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax1.axvline(x=4,color='k',lw=1)
ax1.axvline(x=8,color='k',lw=1)
ax1.set_xlim(0,12)
ax1.set_ylim(0,1400)
ax1.grid(color='gray',linestyle='--',which='major',axis='y',alpha=0.2)

ax1.set_ylabel('UTS (MPa)')
ax1.set_xlabel('Temperature (°C)')
ax1.set_xticks([2,6,10])
ax1.set_xticklabels(['RT','330°C','550°C'])
ax1.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=True) 

#third subplot
ax2.plot(1, UE_RT_99_ASB, color='c',marker='^',alpha=0.6)
ax2.plot(1, UE_RT_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax2.errorbar(2,UE_RT_99_1045_ave,UE_RT_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax2.errorbar(2,UE_RT_95_1045_ave,UE_RT_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax2.errorbar(3,UE_RT_99_1100_ave,UE_RT_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax2.errorbar(3,UE_RT_95_1100_ave,UE_RT_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax2.plot(5, UE_330_99_ASB, color='c',marker='^',alpha=0.6)
ax2.plot(5, UE_330_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax2.errorbar(6,UE_330_99_1045_ave,UE_330_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax2.errorbar(6,UE_330_95_1045_ave,UE_330_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax2.errorbar(7,UE_330_99_1100_ave,UE_330_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax2.errorbar(7,UE_330_95_1100_ave,UE_330_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax2.plot(9, UE_550_99_ASB, color='c',marker='^',alpha=0.6)
ax2.plot(9, UE_550_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax2.errorbar(10,UE_550_99_1045_ave,UE_550_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax2.errorbar(10,UE_550_95_1045_ave,UE_550_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax2.errorbar(11,UE_550_99_1100_ave,UE_550_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax2.errorbar(11,UE_550_95_1100_ave,UE_550_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax2.axvline(x=4,color='k',lw=1)
ax2.axvline(x=8,color='k',lw=1)
ax2.set_xlim(0,12)
ax2.grid(color='gray',linestyle='--',which='major',axis='y',alpha=0.2)

ax2.set_ylabel('UE (%)')
ax2.set_xlabel('Temperature (°C)')
ax2.set_xticks([2,6,10])
ax2.set_xticklabels(['RT','330°C','550°C'])
ax2.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=True) 

#fourth subplot
ax3.plot(1, TE_RT_99_ASB, color='c',marker='^',alpha=0.6)
ax3.plot(1, TE_RT_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax3.errorbar(2,TE_RT_99_1045_ave,TE_RT_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax3.errorbar(2,TE_RT_95_1045_ave,TE_RT_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax3.errorbar(3,TE_RT_99_1100_ave,TE_RT_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax3.errorbar(3,TE_RT_95_1100_ave,TE_RT_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax3.plot(5, TE_330_99_ASB, color='c',marker='^',alpha=0.6)
ax3.plot(5, TE_330_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax3.errorbar(6,TE_330_99_1045_ave,TE_330_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax3.errorbar(6,TE_330_95_1045_ave,TE_330_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax3.errorbar(7,TE_330_99_1100_ave,TE_330_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax3.errorbar(7,TE_330_95_1100_ave,TE_330_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax3.plot(9, TE_550_99_ASB, color='c',marker='^',alpha=0.6)
ax3.plot(9, TE_550_95_ASB, color='darkorange',marker='^',alpha=0.6)
ax3.errorbar(10,TE_550_99_1045_ave,TE_550_99_1045_std, color='c',marker='o',alpha=0.6,capsize=3)
ax3.errorbar(10,TE_550_95_1045_ave,TE_550_95_1045_std, color='darkorange',marker='o',alpha=0.6,capsize=3)
ax3.errorbar(11,TE_550_99_1100_ave,TE_550_99_1100_std, color='c',marker='s',alpha=0.6,capsize=3)
ax3.errorbar(11,TE_550_95_1100_ave,TE_550_95_1100_std, color='darkorange',marker='s',alpha=0.6,capsize=3)

ax3.grid(color='gray',linestyle='--',which='major',axis='y',alpha=0.2)
ax3.axvline(x=4,color='k',lw=1)
ax3.axvline(x=8,color='k',lw=1)
ax3.set_xlim(0,12)

ax3.set_ylabel('TE (%)')
ax3.set_xlabel('Temperature (°C)')
ax3.set_xticks([2,6,10])
ax3.set_xticklabels(['RT','330°C','550°C'])
ax3.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=True) 

# =============================================================================
# Wrought Data, taken from NIMS database
# =============================================================================
ax0.errorbar(1,524,14, color='k',marker='D',alpha=0.6,capsize=3) #YS RT wrought
ax0.errorbar(5,455,22, color='k',marker='D',alpha=0.6,capsize=3) #YS 300 wrought
ax0.errorbar(9,346,14, color='k',marker='D',alpha=0.6,capsize=3) #YS 550 wrought
ax1.errorbar(1,685,10, color='k',marker='D',alpha=0.6,capsize=3) #UTS RT wrought
ax1.errorbar(5,561,21, color='k',marker='D',alpha=0.6,capsize=3) #UTS 300 wrought
ax1.errorbar(9,414,12, color='k',marker='D',alpha=0.6,capsize=3) #UTS 550 wrought
ax3.errorbar(1,24,1, color='k',marker='D',alpha=0.6,capsize=3) #TE RT wrought
ax3.errorbar(5,18,1, color='k',marker='D',alpha=0.6,capsize=3) #TE 300 wrought
ax3.errorbar(9,26,2, color='k',marker='D',alpha=0.6,capsize=3) #TE 550 wrought

# =============================================================================
# ODS Data, taken from Lucon, 'EU Batch' ODS-Eurofer97
# =============================================================================
ax0.errorbar(1,786,5,marker='D',color='b',alpha=0.6,capsize=3); #YS RT ODS Eurofer
ax0.errorbar(5,665,5,marker='D',color='b',alpha=0.6,capsize=3);#YS 330 ODS Eurofer
ax0.errorbar(9,469,116,marker='D',color='b',alpha=0.6,capsize=3);#YS 550 ODS Eurofer
ax1.errorbar(1,927,4,marker='D',color='b',alpha=0.6,capsize=3); #UTS RT ODS Eurofer
ax1.errorbar(5,781,1,marker='D',color='b',alpha=0.6,capsize=3); #UTS 330 ODS Eurofer
ax1.errorbar(9,518,139,marker='D',color='b',alpha=0.6,capsize=3); #UTS 550 ODS Eurofer
ax2.errorbar(1,8.4,0.1,marker='D',color='b',alpha=0.6,capsize=3); #UE RT ODSEurofer
ax2.errorbar(5,6.9,0.1,marker='D',color='b',alpha=0.6,capsize=3); #UE 330 ODS Eurofer
ax2.errorbar(9,6.0,1.3,marker='D',color='b',alpha=0.6,capsize=3); #UE 550 ODS Eurofer
ax3.errorbar(1,18.4,0.3,marker='D',color='b',alpha=0.6,capsize=3); #TE RT ODS Eurofer
ax3.errorbar(5,16.2,0.1,marker='D',color='b',alpha=0.6,capsize=3); #TE ODS 330 Eurofer
ax3.errorbar(9,24.8,5.7,marker='D',color='b',alpha=0.6,capsize=3); #TE 550 ODSEurofer

# =============================================================================
# WAAM G91 Data, taken from  Kun Li's paper in AM Journal
# =============================================================================
ax0.plot(1,985,marker='^',color='g',alpha=0.6); #YS RT WAAM ASB
ax1.plot(1,1242,marker='^',color='g',alpha=0.6); #UTS RT WAAM ASB
ax3.plot(1,10.9,marker='^',color='g',alpha=0.6); #TE RT WAAM ASB

ax0.plot(1,686,marker='s',color='g',alpha=0.6); #YS RT WAAM H2+A2
ax1.plot(1,774,marker='s',color='g',alpha=0.6); #UTS RT WAAM H2+A2
ax3.plot(1,19.4,marker='s',color='g',alpha=0.6); #TE RT WAAM H2+A2


# =============================================================================

# =============================================================================
# ## ASME 2007 BPV
# ax0.axhline(y=415,xmin=0,xmax=0.333,color='k',lw=1)
# ax0.axhline(y=372,xmin=0.333,xmax=.667,color='k',lw=1)
# ax0.axhline(y=277,xmin=0.667,xmax=1,color='k',lw=1)
# 
# ax1.axhline(y=585,xmin=0,xmax=0.333,color='k',lw=1)
# ax1.axhline(y=565,xmin=0.333,xmax=.667,color='k',lw=1)
# ax1.axhline(y=390,xmin=0.667,xmax=1,color='k',lw=1)
# 
# ax3.axhline(y=20,xmin=0.,xmax=0.333,color='k',lw=1)
# =============================================================================


## 6x6 figure
B99 = mlines.Line2D([], [], color='c', markerfacecolor='w',linestyle='None',
                          markersize=0, label='Build 99/1:')
ASB99 = mlines.Line2D([], [], color='c', marker='^',alpha=0.6, linestyle='None',
                          markersize=5, label='ASB')
HT104599 = mlines.Line2D([], [], color='c', marker='o',alpha=0.6,  linestyle='None',
                          markersize=5, label='HT1045')
HT110099 = mlines.Line2D([], [], color='c', marker='s', alpha=0.6,linestyle='None',
                          markersize=5, label='HT1100')
wrought = mlines.Line2D([], [], color='k', marker='D', linestyle='None',alpha=0.6,
                          markersize=5, label='Wrought Grade 91')
B95 = mlines.Line2D([], [], color='darkorange', markerfacecolor='w',linestyle='None',
                          markersize=0, label='Build 95/5:')
ASB95 = mlines.Line2D([], [], color='darkorange', marker='^',alpha=0.6, linestyle='None',
                          markersize=5, label='ASB')
HT104595 = mlines.Line2D([], [], color='darkorange', marker='o',alpha=0.6,  linestyle='None',
                          markersize=5, label='HT1045')
HT110095 = mlines.Line2D([], [], color='darkorange', marker='s', alpha=0.6, linestyle='None',
                          markersize=5, label='HT1100')
ODS = mlines.Line2D([], [], color='b', marker='D',  linestyle='None',alpha=0.6,
                          markersize=5, label='ODS Eurofer97')
WAAM = mlines.Line2D([], [], color='g', marker='^',  linestyle='None',alpha=0.6,
                          markersize=5, label='ASB WAAM G91')
WAAM_H2A2 = mlines.Line2D([], [], color='g', marker='s',  linestyle='None',alpha=0.6,
                          markersize=5, label='H2+A2 WAAM G91')
filler1= mlines.Line2D([], [], color='w',  linestyle='None',
                          markersize=0, label='')
filler2 = mlines.Line2D([], [], color='w',  linestyle='None',
                          markersize=0, label='')

lgd1 = fig.legend(handles=[B99,B95,ASB99,ASB95, HT104599, HT104595, HT110099, HT110095,wrought,ODS,WAAM,WAAM_H2A2,filler1,filler2],loc='upper center',bbox_to_anchor=(0.525,1.1),ncol=7,frameon=True,handletextpad=0,columnspacing=0.1)

for line, text in zip(lgd1.get_lines(), lgd1.get_texts()):
    text.set_color(line.get_color())

fig.text(0.01,0.978,'(a)')
fig.text(0.51,0.978,'(b)')
fig.text(0.01,0.48,'(c)')
fig.text(0.51,0.48,'(d)')

plt.savefig('Mech Prop Transparent no notation.png', bbox_extra_artists=(lgd1,), bbox_inches='tight', format='png', dpi=1200)
