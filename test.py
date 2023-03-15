import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,100)

x_0 = 3
y_0 = 2
 
x_1 = 3
y_1 = 5

x_2 = 4
y_2 = 5

x_3 = 6
y_3 = 6

x = x_0*(1-t)**3 + 3*x_1*t*(1-t)**2 + 3*x_2*t**2*(1-t) + x_3*t**3
y = y_0*(1-t)**3 + 3*y_1*t*(1-t)**2 + 3*y_2*t**2*(1-t) + y_3*t**3


# Titulo de la gráfica y ejes


# Gráfica de los Puntos P0, P1, P2, P3  
#x_puntos = [x_0,x_1,x_2,x_3] 
#y_puntos = [y_0,y_1,y_2,y_3] 
#plt.plot(x_puntos, y_puntos, color='green', linestyle='dashed', linewidth = 3, 
        # marker='o', markerfacecolor='blue', markersize=12) 

# Curva de Bezier
#plt.xlim(0, 100)
#plt.ylim(0, 50);
#plt.plot(x,y,c=(1,0.5,0.5),lw=4)

f = plt.figure()
plt.title('Curva de Bezier') 
plt.xlabel('Eje x') 
plt.ylabel('Eje y') 
f.set_figwidth(20)
f.set_figheight(10)
plt.plot(x,y,c=(1,0.5,0.5),lw=4)
plt.show()
