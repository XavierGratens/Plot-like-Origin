import numpy as np
import matplotlib.pyplot as plt

plt.style.use('My_Rectangular_Fig')

"Load data"
"Load data"
MV11 = np.loadtxt("M_V11_S52.txt")
MV11 = np.vstack(([0,0], MV11))
MV12 = np.loadtxt("M_V12_S52.txt")
MV12 = np.vstack(([0,0], MV12))
MV13 = np.loadtxt("M_V13_S52.txt")
MV13 = np.vstack(([0,0], MV13))
MV14 = np.loadtxt("M_V14_S52.txt")
MV14 = np.vstack(([0,0], MV14))
MV15 = np.loadtxt("M_V15_S52.txt")
MV15 = np.vstack(([0,0], MV15))

MV16 = np.loadtxt("M_V16_S52.txt")
MV16 = np.vstack(([0,0], MV16))


MV17 = np.loadtxt("M_V17_S52.txt")
MV17 = np.vstack(([0,0], MV17))




#http://jfly.iam.u-tokyo.ac.jp/color/.

orange='#E69F00'
skyblue ='#56B4E9'
bluishgreen='#009E73'
yellow= '#F0E442'
blue = '#0072B2'
vermilion= '#D55E00'
reddishpurple='#CC79A7'
black= '#000000'




Plot_Color =  '#000000'
Plot_Color2 =  'r'
Cyan='#04FFFF'
vert='#00FF00'

ax = plt.subplot(111)

"Set axis label"
ax.set_xlabel(r'$g\mu_{\mathrm{B}}H$/|2$J/k_{\mathrm{B}}$|')
ax.set_ylabel('$m = M/M_{0}$')

z = MV11.shape[0]-5












"Plotting data"
ax.plot((MV11[:z,0]+MV13[:,0])/2,(MV11[:z,1]+MV13[:,1])/2, label='V. 11', color = Plot_Color, linestyle = 'solid', linewidth = 2)
ax.plot(MV12[:,0],MV12[:,1], label='V. 12', color = vermilion, linestyle = 'dotted', linewidth = 3)
ax.plot(MV14[:,0],MV14[:,1], label='V. 14', color = blue, linestyle = 'dashed', dashes=[5, 1], linewidth = 3)
ax.plot(MV15[:,0],MV15[:,1], label='V. 15', color =bluishgreen,  linestyle = 'dashdot', linewidth = 3)
#ax.plot(MV16[:,0],MV16[:,1], label='V. 16', color = Plot_Color2, linestyle = 'dashed',dashes=[5, 1], linewidth = 2)
#ax.plot(MV17[:,0],MV17[:,1], label='V. 17', color = Plot_Color, linestyle = 'dashed',dashes=[2, 1], linewidth = 2)
ax.legend(loc='lower right')

"Set x and y limits"
ax.set_xlim(0,14)
ax.set_ylim(0,1.02)
ax.text(2, 0.95, 'Spin = 5/2', horizontalalignment='center')

ax.text(2, 0.85, '$k_{\mathrm{B}} T/|J|$ = 0.1', horizontalalignment='center')




"Save figure" 
plt.savefig('Figure_3.png', dpi=400)

plt.show()









