import numpy as np
import matplotlib.pyplot as plt


def system_equations(t, y, m1, m2, k1, k2, b1, b2):
    x1, v1, x2, v2 = y

    x1_dot = v1
    v1_dot = (-k1 * x1 - b1 * v1 + k2 * (x2 - x1) + b2 * (v2 - v1)) / m1

    x2_dot = v2
    v2_dot = (-k2 * (x2 - x1) - b2 * (v2 - v1)) / m2

    return np.array([x1_dot, v1_dot, x2_dot, v2_dot])


def simulate_system(m1, m2, k1, k2, b1, b2):
    # Tempo de simulação de 0 a 10 segundos com passo de 0.01 segundos
    t = np.arange(0, 10, 0.01)
    num_steps = len(t)

    # Condições iniciais
    x1 = np.zeros(num_steps)
    v1 = np.zeros(num_steps)
    x2 = np.zeros(num_steps)
    v2 = np.zeros(num_steps)

    x1[0] = 0
    v1[0] = 0
    x2[0] = 1
    v2[0] = 0

    # Simulação do sistema usando o método de Euler
    for i in range(1, num_steps):
        dt = t[i] - t[i-1]

        x1_dot, v1_dot, x2_dot, v2_dot = system_equations(
            t[i-1], [x1[i-1], v1[i-1], x2[i-1], v2[i-1]], m1, m2, k1, k2, b1, b2)

        x1[i] = x1[i-1] + v1[i-1] * dt
        v1[i] = v1[i-1] + v1_dot * dt
        x2[i] = x2[i-1] + v2[i-1] * dt
        v2[i] = v2[i-1] + v2_dot * dt

    # Plotagem dos resultados
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1)
    plt.plot(t, x1)
    plt.xlabel('Tempo')
    plt.ylabel('Posição x1')

    plt.subplot(2, 2, 2)
    plt.plot(t, v1)
    plt.xlabel('Tempo')
    plt.ylabel('Velocidade v1')

    plt.subplot(2, 2, 3)
    plt.plot(t, x2)
    plt.xlabel('Tempo')
    plt.ylabel('Posição x2')

    plt.subplot(2, 2, 4)
    plt.plot(t, v2)
    plt.xlabel('Tempo')
    plt.ylabel('Velocidade v2')

    plt.tight_layout()
    plt.show()

    # Diagrama de fases
    plt.figure(figsize=(6, 6))
    plt.plot(x1, v1, label='Corpo 1')
    plt.plot(x2, v2, label='Corpo 2')
    plt.xlabel('Posição')
    plt.ylabel('Velocidade')
    plt.title('Diagrama de Fases')
    plt.legend()
    plt.grid()
    plt.show()


# Parâmetros do sistema
m1 = 10
m2 = 15
k1 = 800
k2 = 1500
b1 = 0.5
b2 = 3

# Simulação do sistema
simulate_system(m1, m2, k1, k2, b1, b2)
