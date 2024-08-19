import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 22

"Load data"
Data_Pairs = np.loadtxt("M_P_S32.txt")
Data_OT = np.loadtxt("M_OT_S32.txt")
Data_CT = np.loadtxt("M_CT_S32.txt")





"Figure properites"
Fig_Width=22
Fig_Height = Fig_Width
Width = 16
Height = Width
Left = (Fig_Width-Width)/2
Bottom = (Fig_Height-Height)/2
Label_Size = 22
Legend_Size = 22
Tick_Size = 20
Linewidth_Axis = 1
Plot_Color =  '#000000'

fig = plt.figure(figsize=(Fig_Width/2.54,Fig_Height/2.54))


ax=plt.subplot(111) 

"Tickness of the axis"
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(Linewidth_Axis)
"Set size of the axis"
plt.subplots_adjust(left=Left/Fig_Width, right=Left/Fig_Width+Width/Fig_Width, top = Bottom/Fig_Height + Height/Fig_Height, bottom = Bottom/Fig_Height)


"Set axis ticks "
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.tick_params(direction='in', length=6, width=0.75)

"Set tickness of the axis ticks "
plt.xticks(fontsize = Tick_Size)
plt.yticks(fontsize = Tick_Size)

"Set axis label"
ax.set_xlabel('$h_{r}$ = $g\mu_{\mathrm{B}}H$/|2$J/k_{\mathrm{B}}$|', fontsize=Label_Size)
ax.set_ylabel('$m = M/M_{0}$', fontsize=Label_Size)

"Plotting data"
ax.plot(Data_Pairs[:,0],Data_Pairs[:,1], label='Pairs', color = Plot_Color,  linestyle = 'solid', linewidth = 2)
ax.plot(Data_OT[:,0],Data_OT[:,1], label='Open Triplets', color = Plot_Color, linestyle = 'dotted', linewidth = 2)
ax.plot(Data_CT[:,0],Data_CT[:,1], label='Closed Triplets', color = Plot_Color, linestyle = 'dashed',dashes=[5, 1], linewidth = 2)
ax.legend(loc='best', frameon=False, fontsize = Legend_Size)

"Set x and y limits"
ax.set_xlim(0,6)
ax.set_ylim(0,1.02)




"Add text"
ax.text(1, 0.95, 'Spin = 3/2', horizontalalignment='center')

ax.text(1, 0.85, '$k_{\mathrm{B}} T/|J|$ = 0.2', horizontalalignment='center')



"Save figure" 
plt.savefig('FigS.png', dpi=400)

plt.show()









