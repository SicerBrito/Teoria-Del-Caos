# pip install numpy matplotlib scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Parámetros del péndulo doble
g = 9.81  # aceleración debido a la gravedad
L1, L2 = 1.0, 1.0  # longitudes de las barras
m1, m2 = 1.0, 1.0  # masas de los péndulos
num_pendulos = 10  # reducido para mejor visualización

# Función que describe la dinámica del péndulo doble
def pendulo_doble(y, t, L1, L2, m1, m2, g):
    theta1, z1, theta2, z2 = y
    c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)
    
    theta1_dot = z1
    z1_dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2) - 
              (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2)
    theta2_dot = z2
    z2_dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) + 
              m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)
    return [theta1_dot, z1_dot, theta2_dot, z2_dot]

# Condiciones iniciales con pequeñas perturbaciones
y0 = np.array([[np.pi/2, 0, np.pi/2, 0] for _ in range(num_pendulos)])
y0 += np.random.randn(*y0.shape) * 1e-3

# Tiempo de simulación
t = np.linspace(0, 30, 1000)

# Resolver las ecuaciones diferenciales para cada péndulo
soluciones = np.array([odeint(pendulo_doble, y0_i, t, args=(L1, L2, m1, m2, g)) for y0_i in y0])

# Configurar la animación
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-L1-L2-0.5, L1+L2+0.5)
ax.set_ylim(-L1-L2-0.5, L1+L2+0.5)
ax.set_aspect('equal')
ax.grid(True)

lines = [ax.plot([], [], 'o-')[0] for _ in range(num_pendulos)]
traces = [ax.plot([], [], '-', lw=1, alpha=0.3)[0] for _ in range(num_pendulos)]

def init():
    for line, trace in zip(lines, traces):
        line.set_data([], [])
        trace.set_data([], [])
    return lines + traces

def animate(i):
    for j, (line, trace) in enumerate(zip(lines, traces)):
        theta1, theta2 = soluciones[j, :i, 0], soluciones[j, :i, 2]
        x1, y1 = L1 * np.sin(theta1), -L1 * np.cos(theta1)
        x2, y2 = x1 + L2 * np.sin(theta2), y1 - L2 * np.cos(theta2)
        
        line.set_data([0, x1[-1], x2[-1]], [0, y1[-1], y2[-1]])
        trace.set_data(x2, y2)
    
    return lines + traces

anim = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=20, blit=True)

plt.title('Simulación de péndulos dobles caóticos')
plt.show()