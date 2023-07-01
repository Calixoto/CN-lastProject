import math
import matplotlib.pyplot as plt

# Constantes
L = 2
L0 = 1
k = 40
m = 1
g = 9.81
theta = 3 * math.pi / 4

# Funções das EDOs


def dx1_dt(x1, x2):
    return -1/2 * (g * math.sin(theta) + 2 * x1 * x2)


def dx2_dt(x1, x2):
    return 2 * (x1 ** 2) - k * (L - L0) + m * g * math.cos(theta)


# Simulação usando o método de Runge-Kutta de quarta ordem
t = 0
dt = 0.1  # Intervalo de tempo
t_total = 10

# Condições iniciais
x1 = 0
x2 = 0

# Listas para armazenar os valores de tempo e x1
time_values = []
x1_values = []

while t <= t_total:
    # Armazenar os valores atuais de tempo e x1
    time_values.append(t)
    x1_values.append(x1)

    # Calcular as taxas de variação
    k1_x1 = dx1_dt(x1, x2)
    k1_x2 = dx2_dt(x1, x2)

    k2_x1 = dx1_dt(x1 + k1_x1 * dt/2, x2 + k1_x2 * dt/2)
    k2_x2 = dx2_dt(x1 + k1_x1 * dt/2, x2 + k1_x2 * dt/2)

    k3_x1 = dx1_dt(x1 + k2_x1 * dt/2, x2 + k2_x2 * dt/2)
    k3_x2 = dx2_dt(x1 + k2_x1 * dt/2, x2 + k2_x2 * dt/2)

    k4_x1 = dx1_dt(x1 + k3_x1 * dt, x2 + k3_x2 * dt)
    k4_x2 = dx2_dt(x1 + k3_x1 * dt, x2 + k3_x2 * dt)

    # Atualizar os valores de x1 e x2 usando o método de Runge-Kutta
    x1 += (k1_x1 + 2*k2_x1 + 2*k3_x1 + k4_x1) * dt/6
    x2 += (k1_x2 + 2*k2_x2 + 2*k3_x2 + k4_x2) * dt/6

    # Atualizar o tempo
    t += dt

# Plotar o gráfico de x1 em função do tempo
plt.plot(time_values, x1_values)
plt.xlabel('Tempo')
plt.ylabel('x1')
plt.title('Pêndulo Amortecido: x1 vs. Tempo')
plt.grid(True)
plt.show()
