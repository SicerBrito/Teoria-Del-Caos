# Simulación de Péndulos Dobles Caóticos y Teoría del Caos

## Autor

Sicer Andres Brito Gutierrez

Discord: SicerBrito#1610

## Teoría del Caos

La Teoría del Caos es una rama de la matemática y la física que estudia sistemas dinámicos que son extremadamente sensibles a las condiciones iniciales. Esto se refiere a la idea de que pequeñas diferencias en el estado inicial de un sistema pueden llevar a resultados drásticamente diferentes, lo que comúnmente se conoce como el "efecto mariposa". 🌪️

La teoría del caos se aplica en muchos campos como la meteorología, la economía, la biología, y otros sistemas complejos donde las predicciones a largo plazo se vuelven prácticamente imposibles debido a la gran sensibilidad del sistema.

### Ejemplos de la Teoría del Caos

1. **El clima como sistema caótico** 🌦️
   
   Imagina que estás tratando de predecir el tiempo con una semana de antelación. Aunque los meteorólogos tienen modelos precisos y datos detallados, el clima es un sistema caótico. Una pequeña variación en los datos iniciales, como una leve diferencia en la temperatura o la velocidad del viento en un lugar específico, puede llevar a un pronóstico completamente diferente días después.
   
   Este concepto se ilustra en lo que se conoce como el "efecto mariposa" 🦋, que sugiere que el aleteo de una mariposa en Brasil podría, en teoría, desencadenar un tornado en Texas semanas después. Por supuesto, esto es una metáfora, pero muestra cómo pequeñas causas pueden tener grandes efectos impredecibles.

2. **Péndulos acoplados y sistemas de péndulo doble** 🎢
   
   Imagina dos péndulos idénticos colgando de una barra. Si los empujas al mismo tiempo y con la misma fuerza, podrías esperar que se muevan de manera idéntica. Sin embargo, debido a la naturaleza caótica de estos sistemas, incluso pequeñas diferencias en las condiciones iniciales (como una ligera diferencia en el ángulo o una variación mínima en la fricción) pueden causar que sus trayectorias diverjan rápidamente, resultando en movimientos completamente diferentes.
   
   En el caso de un péndulo doble (dos péndulos conectados uno al extremo del otro), el movimiento es aún más caótico. Este sistema puede parecer predecible al principio, pero pronto sus movimientos se vuelven erráticos y difíciles de predecir, ya que cualquier pequeña variación se amplifica con el tiempo.
   
   Este comportamiento caótico ocurre porque estos sistemas son muy sensibles a las condiciones iniciales, lo que es una característica clave en la Teoría del Caos. Esto significa que, aunque el sistema es determinista (las leyes físicas son claras), el comportamiento a largo plazo se vuelve impredecible.

## Implementación de la Simulación de Péndulos Dobles Caóticos

### Descripción General
Este script de Python simula el comportamiento de múltiples péndulos dobles caóticos. Utiliza técnicas de integración numérica para resolver las ecuaciones diferenciales que describen el movimiento de los péndulos y crea una animación visual de su comportamiento.

### Dependencias
El script requiere las siguientes bibliotecas de Python:
- numpy: para cálculos numéricos
- matplotlib: para visualización y animación
- scipy: para integración numérica de ecuaciones diferenciales

### Estructura del Código

#### 1. Importación de Bibliotecas
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation
```

#### 2. Definición de Parámetros
```python
g = 9.81  # aceleración debido a la gravedad
L1, L2 = 1.0, 1.0  # longitudes de las barras
m1, m2 = 1.0, 1.0  # masas de los péndulos
num_pendulos = 10  # número de péndulos a simular
```

#### 3. Función de Dinámica del Péndulo Doble
```python
def pendulo_doble(y, t, L1, L2, m1, m2, g):
    # ... (implementación de las ecuaciones diferenciales)
```
Esta función define las ecuaciones diferenciales que describen el movimiento del péndulo doble.

#### 4. Condiciones Iniciales
```python
y0 = np.array([[np.pi/2, 0, np.pi/2, 0] for _ in range(num_pendulos)])
y0 += np.random.randn(*y0.shape) * 1e-3
```
Se establecen las condiciones iniciales para cada péndulo con pequeñas perturbaciones aleatorias.

#### 5. Simulación
```python
t = np.linspace(0, 30, 1000)
soluciones = np.array([odeint(pendulo_doble, y0_i, t, args=(L1, L2, m1, m2, g)) for y0_i in y0])
```
Se resuelven las ecuaciones diferenciales para cada péndulo utilizando `odeint`.

#### 6. Configuración de la Animación
```python
fig, ax = plt.subplots(figsize=(10, 8))
# ... (configuración del área de ploteo)
lines = [ax.plot([], [], 'o-')[0] for _ in range(num_pendulos)]
traces = [ax.plot([], [], '-', lw=1, alpha=0.3)[0] for _ in range(num_pendulos)]
```

#### 7. Funciones de Animación
```python
def init():
    # ... (inicialización de la animación)

def animate(i):
    # ... (actualización de la posición de los péndulos en cada frame)
```

#### 8. Creación y Visualización de la Animación
```python
anim = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=20, blit=True)
plt.title('Simulación de péndulos dobles caóticos')
plt.show()
```

### Funcionamiento
1. El script comienza definiendo los parámetros físicos de los péndulos dobles.
2. Se establecen condiciones iniciales ligeramente diferentes para cada péndulo.
3. Las ecuaciones de movimiento se resuelven numéricamente para cada péndulo.
4. Se crea una animación que muestra el movimiento de todos los péndulos simultáneamente.
5. La animación visualiza cómo pequeñas diferencias en las condiciones iniciales llevan a comportamientos muy diferentes a lo largo del tiempo, ilustrando el concepto de caos.

### Notas Adicionales
- El número de péndulos y otros parámetros pueden ajustarse para explorar diferentes escenarios.
- La simulación demuestra visualmente conceptos de la teoría del caos, como la sensibilidad a las condiciones iniciales.
- El código puede ser extendido para incluir análisis adicionales o visualizaciones de las trayectorias de los péndulos.
