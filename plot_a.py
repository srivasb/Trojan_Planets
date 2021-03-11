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

columns=['x0','y0','x1','y1']
df1=pd.read_table('a.dat',sep=r'\s+',names=columns,dtype='a',engine='python')
for col in df1.columns[:]:
    df1[col]=pd.to_numeric(df1[col],errors='coerce')


fig = plt.figure()
ax = plt.gca()
plt.plot(df1.x1,df1.y1,color='k',lw=0.2)
plt.scatter(df1.x0,df1.y0,c='r',s=200)
plt.grid(color='k', linestyle='-', linewidth=0.1,alpha=0.35)
plt.title(r'Jupyter Orbit around the sun')
plt.xlabel(r'$x$ coordinates')
plt.ylabel(r'$y$ coordinates')
ax.legend(['Jupyter Orbit',r'Sun'],loc=0)
plt.tight_layout(0.5)
#plt.show()
plt.savefig("a.pdf")