# Latex .pgf Backend does have a maximun of point to plot
# If the data set exceeds 3000 point it wont work

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

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

fig = plt.figure()
ax = plt.gca()
plt.scatter(df.x1,df.y1,marker=',',s=0.1)
ax.set_ylim(-0.5,0.5)
#plt.scatter(df.x2,df.y2,c='r',s=0.1)
plt.title(r'Coordinates $x^\prime$ and $y^\prime$ that move along with Jupyter Orbit')
plt.xlabel(r'$x_{\mathtt{rot}}$ Coordinates')
plt.ylabel(r'$y_\mathtt{rot}$ Coordinates')
plt.tight_layout(0.5)
#plt.show()

plt.savefig("b.pdf")
