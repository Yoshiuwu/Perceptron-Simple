import matplotlib.pyplot as plt
import numpy as np

#Definimos las variables para utilizar en el programa
Theta = 0
W = []
X = []
m = 0
b = 0

#Abrimos el archivo para obtener los valores de las entradas
with open('input.txt') as f:
    entrys = f.readlines()

#Separamos las entradas del documento en un vector
for entry in entrys:
    vector = entry.rstrip("\n").split(' ')
    vector[0] = int(vector[0])
    vector[1] = int(vector[1])
    X.append(vector)

#Imprimimos en consola para que el usuario ingrese los valores
w1 = float(input("W1: "))
w2 = float(input("W2: "))
theta = float(input("Theta: "))

#asignamos los valores ingresados por el usuario
Theta = theta
W = [w1, w2]
m = - W[0] / W[1]
b = Theta / W[1]

#Calculamos el producto punto con los valores
vF = np.dot(X ,W) - Theta >= 0

#Imprimimos el plano cartesiano para mostrar la gráfica
ejeX = np.arange(-2, 3, 1)
ejeY = np.arange(-2, 3, 1)
zeros = [0, 0, 0, 0, 0]
plt.plot(ejeX, zeros, 'k')
plt.plot(zeros, ejeY, 'k')

#Definimos los puntos por los que pasa la gráfica de acuerdo a las entradas del usuario
for i in range(len(X)):
    if vF[i]:
        plt.plot(X[i][0], X[i][1], 'og')
    else:
        plt.plot(X[i][0], X[i][1], 'or')

#Imprimimos el resultado de la salida
plt.axline((0, b), slope = m)

#mostramos la gráfica
plt.title('Perceptron')
plt.show()