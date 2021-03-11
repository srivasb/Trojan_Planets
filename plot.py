# Latex .pgf Backend does have a maximun of point to plot
# If the data set exceeds 3000 point it wont work

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import mpl_toolkits.axes_grid1.inset_locator as mpl_il

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

columns=['x1','y1']
df=pd.read_table('b.dat',sep=r'\s+',names=columns,dtype='a',engine='python')
for col in df.columns[:]:
    df[col]=pd.to_numeric(df[col],errors='coerce')
#print(df.dtypes)

# fig = plt.figure()
# ax = plt.gca()
# plt.scatter(df.x1,df.y1,marker=',',s=0.1)
# ax.set_ylim(-0.5,0.5)
# #plt.scatter(df.x2,df.y2,c='r',s=0.1)
# plt.title(r'Coordinates $x^\prime$ and $y^\prime$ that move along with Jupyter Orbit')
# plt.xlabel(r'$x_{\mathtt{rot}}$ Coordinates')
# plt.ylabel(r'$y_\mathtt{rot}$ Coordinates')
# plt.tight_layout(0.5)
# #plt.show()

plt.figure()
#Mean Plot
ax = plt.gca()
plt.scatter(df.x1,df.y1,color='k',marker='.',s=10)
ax.set_ylim(-0.2,0.2)
ax.set_xlim(99,105)
plt.grid(color='r', linestyle='-', linewidth=0.1,alpha=0.2)
plt.title(r'Coordinates $x^\prime$ and $y^\prime$ that move along with Jupyter Orbit')
plt.xlabel(r'$x_{\mathtt{rot}}$ coordinates')
plt.ylabel(r'$y_\mathtt{rot}$ coordinates')
ax.legend([r'$x=99.9046\;\;y=1\exp(-10)$'],loc=2)
# OverLay plot
ax2 = mpl_il.inset_axes(plt.gca(), width='50%', height='60%', loc=7)
ax2.scatter(df.x1,df.y1,color='b',marker='.',s=1)
ax2.grid(color='k', linestyle='-', linewidth=0.1,alpha=0.2)
ax2.set_title(r'Closes Look')
ax2.margins(x=0.5)
# To Show
#plt.tight_layout(0.2)
# plt.show()

plt.savefig("b.pdf")
