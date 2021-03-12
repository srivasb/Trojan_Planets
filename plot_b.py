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

# columns=['x1','y1']
# df2=pd.read_table('b.dat',sep=r'\s+',names=columns,dtype='a',engine='python')
# for col in df2.columns[:]:
#     df2[col]=pd.to_numeric(df2[col],errors='coerce')
# #print(df.dtypes)

# bbox_args = dict(boxstyle="round", fc="0.8")

# plt.figure()
# #Mean Plot
# ax = plt.gca()
# plt.scatter(df2.x1,df2.y1,color='k',marker='.',s=20)
# ax.set_ylim(-0.2,0.2)
# ax.set_xlim(990,1045)
# plt.grid(color='r', linestyle='-', linewidth=0.1,alpha=0.2)
# plt.title(r'Coordinates $x^\prime$ and $y^\prime$ that move along with Jupyter Orbit')
# plt.xlabel(r'$x_{\mathtt{rot}}$ coordinates')
# plt.ylabel(r'$y_\mathtt{rot}$ coordinates')
# ax.annotate(r'x={:e} , y={:e}'.format(df2.x1[3],df2.y1[3]),xy=(992,0.17),bbox=bbox_args,)
# # OverLay plot
# ax2 = mpl_il.inset_axes(plt.gca(), width='50%', height='60%', loc=7)
# ax2.scatter(df2.x1,df2.y1,color='k',marker='.',s=0.5)
# ax2.grid(color='r', linestyle='-', linewidth=0.1,alpha=0.2)
# ax2.set_title(r'Closes Look')
# ax2.margins(x=0.5)
# # To Show
# #plt.tight_layout(0.2)
# # plt.show()

columns=['x1','y1','x0','y0']
df2=pd.read_table('b.dat',sep=r'\s+',names=columns,dtype='a',engine='python')
for col in df2.columns[:]:
    df2[col]=pd.to_numeric(df2[col],errors='coerce')

fig = plt.figure()
ax = plt.gca()
plt.scatter(df2.x1,df2.y1,color='k',marker='.',s=40,label='Jupyter')
plt.scatter(df2.x0,df2.y0,c='r',marker='.',s=40,label='Sun')
ax.set_ylim(-0.5,0.5)
plt.grid(color='r', linestyle='-', linewidth=0.1,alpha=0.2)
plt.title(r'Coordinates $x^\prime$ and $y^\prime$ that move along with Jupyter Orbit')
plt.xlabel(r'$x_{\mathtt{rot}}$ coordinates')
plt.ylabel(r'$y_\mathtt{rot}$ coordinates')
plt.legend()
plt.tight_layout(0.5)
#plt.show()

plt.savefig("b0.pdf")
