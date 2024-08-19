import numpy as np
import matplotlib.pyplot as plt

plt.style.use('My_Rectangular_Fig')

"Load data"
Data_Pairs = np.loadtxt("M_P_S32.txt")
Data_OT = np.loadtxt("M_OT_S32.txt")
Data_CT = np.loadtxt("M_CT_S32.txt")



Plot_Color =  '#000000'


ax = plt.subplot(111)

"Set axis label"
ax.set_xlabel(r'$h_{r}$ = $g\mu_{\mathrm{B}}H$/|2$J/k_{\mathrm{B}}$|')
ax.set_ylabel('$m = M/M_{0}$')

"Plotting data"
ax.plot(Data_Pairs[:,0],Data_Pairs[:,1], label='Pairs', color = Plot_Color,  linestyle = 'solid', linewidth = 2)
ax.plot(Data_OT[:,0],Data_OT[:,1], label='Open Triplets', color = Plot_Color, linestyle = 'dotted', linewidth = 2)
ax.plot(Data_CT[:,0],Data_CT[:,1], label='Closed Triplets', color = Plot_Color, linestyle = 'dashed',dashes=[5, 1], linewidth = 2)
ax.legend(loc='lower right')

"Set x and y limits"
ax.set_xlim(0,6)
ax.set_ylim(0,1.02)




"Add text"
ax.text(1, 0.85, 'Spin = 3/2', horizontalalignment='center')

ax.text(1, 0.75, '$k_{\mathrm{B}} T/|J|$ = 0.2', horizontalalignment='center')



"Save figure" 
plt.savefig('FigR.png', dpi=400)

plt.show()









