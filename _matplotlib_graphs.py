import matplotlib.pyplot as plt
"""

#Stack Plot
yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]


plt.plot([],[],color = 'y',label='oyuncu1')
plt.plot([],[],color = 'r',label='oyuncu2')
plt.plot([],[],color = 'b',label='oyuncu3')

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=['y','r','b'])
plt.title("Yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("Gol sayısı")
plt.legend()
plt.show()

"""
"""
#Pie Grafiği

goalTypes = 'Penaltı','Kaleye Atılan Şut','Serbest Vuruş'

goals = [12,35,7]
colors = ['y','r','b']

plt.pie(goals,labels=goalTypes,colors=colors, shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%") #özelliklre kattık

plt.show()

""""""

#Bar Grafiği

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe(km)")
plt.title("Araç Bilgileri")

plt.show()

""""""
#Histogram Grafiği

yaslar = [1,2,3,2,3,12,2,2,1,21,2,11,4,43,5,46,5,6,678,89,87,65,4,97,54,3,32,1,2,86,23,34,45,56,67,78,89,90]
yasGruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yasGruplari,histtype="bar",rwidth=0.8)
plt.xlabel('Yaş Grupları')
plt.ylabel('Kişi Sayısı')
plt.title('Histogram')

plt.show()

"""