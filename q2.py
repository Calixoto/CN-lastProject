import numpy as np
import matplotlib.pyplot as plt

# Valores dos parâmetros
a = 1
b = 0.25
c = 0.01
d = 0.02
e = 0.02
h = 0

# Funções das equações diferenciais


def prey_prey_eq(x, y):
    return x * (a - c * x - d * y)


def predator_prey_eq(x, y):
    return -y * (b - e * x) - h


# Pontos críticos
critical_points = [(12.5, 43.75)]

# Vetores para o gráfico
x = np.linspace(0, 150, 100)
y = np.linspace(0, 150, 100)

X, Y = np.meshgrid(x, y)
U = prey_prey_eq(X, Y)
V = predator_prey_eq(X, Y)

# Plot do campo vetorial
fig, ax = plt.subplots(figsize=(8, 6))
ax.quiver(X, Y, U, V, color='b', alpha=0.5)

# Plot dos pontos críticos
for point in critical_points:
    ax.plot(point[0], point[1], 'ro')

# Configurações do gráfico
ax.set_xlabel('Presa (x)')
ax.set_ylabel('Predador (y)')
ax.set_title('Modelo de Lotka-Volterra')
ax.grid(True)

# Mostrar gráfico
plt.show()
