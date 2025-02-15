import  matplotlib.pyplot as plt
import numpy as np
"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,"o--r")
plt.axis([0,6,0,20]) # x 6 ya y 20  ye kadar gider
plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
"""
"""
x = np.linspace(0,2,100)
plt.plot(x,x,label="linear",color="red")
plt.plot(x,x**2,label="quadratic",color="yellow")
plt.plot(x,x**3,label="cubic",color="green")

plt.xlabel("xLabel")
plt.ylabel("yLabel")
plt.legend() #label'lara verdiğimiz değerler görünsün
plt.title("Simple Plot")

plt.show()
"""
"""
axs[0].plot(x,x,color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="green")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="yellow")
axs[2].set_title("cubic")

plt.tight_layout() # yapmadığımız  taktirde yazılar üst üste biniyor
"""
"""
x = np.linspace(0,2,100)

fig,axs = plt.subplots(2,2) #2 tane axes alanı olusturduk. bir figür bir axes
fig.suptitle("grafik başlığı") # oluşturduğumuz figürün ana başlaığı
axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x**4,color="yellow")
plt.show()
"""
import pandas as pd


df = pd.read_csv('pandas_demo1.csv')
df['team_abbreviation'] = pd.to_numeric(df['team_abbreviation'],errors='coerce')
df = df.drop(["age"],axis=1).groupby("team_abbreviation").mean()
df.head(5).plot(subplots=True)
plt.legend()

plt.show()