# Ecuación diferencial separable y método de Euler en Python

Este proyecto resuelve analíticamente una ecuación diferencial separable y compara su solución exacta con la aproximación del método de Euler explícito en el intervalo **t ∈ [0, 1]**, con un paso de **h = 0.2**.

## 1. Planteamiento

Se selecciona el problema de valor inicial:

$$
\frac{dy}{dt}=y, \qquad y(0)=1.
$$

La ecuación describe un crecimiento cuya rapidez es proporcional al valor de la función, con constante de proporcionalidad igual a 1. La condición inicial permite determinar una solución particular única.

## 2. Solución analítica por separación de variables

Para las soluciones no nulas, se separan las variables:

$$
\frac{1}{y}\,dy=dt.
$$

Se integran ambos lados:

$$
\int\frac{1}{y}\,dy=\int dt \quad\Rightarrow\quad \ln|y|=t+C.
$$

Al aplicar la función exponencial y absorber el signo y la constante en A:

$$
y(t)=Ae^t.
$$

Se sustituye la condición inicial:

$$
y(0)=Ae^0=1 \quad\Rightarrow\quad A=1.
$$

Por lo tanto, la solución exacta del problema es:

$$
\boxed{y(t)=e^t}.
$$

Comprobación: su derivada es e^t = y(t), y en t=0 vale 1. Al dividir entre y se excluyó la solución de equilibrio y=0; esta también resuelve la ecuación diferencial, pero no cumple la condición inicial elegida.

## 3. Método de Euler

Para una ecuación de la forma y' = f(t,y), Euler explícito utiliza la pendiente al inicio de cada paso:

$$
t_{n+1}=t_n+h, \qquad y_{n+1}=y_n+h f(t_n,y_n).
$$

En este problema, f(t,y)=y y h=0.2, de modo que:

$$
y_{n+1}=y_n+0.2y_n=1.2y_n.
$$

El número de pasos es N=(1−0)/0.2=5. Se obtienen seis puntos al incluir el inicial. Por ejemplo, el primer paso es y₁=1+0.2(1)=1.2, y el segundo es y₂=1.2+0.2(1.2)=1.44.

## 4. Resultados

El error absoluto se calcula como |y(tₙ)−yₙ|. Los valores se muestran redondeados a seis decimales; el programa conserva la precisión de los números de punto flotante durante los cálculos.

| n | t | Euler | Solución exacta | Error absoluto |
|---:|---:|---:|---:|---:|
| 0 | 0.0 | 1.000000 | 1.000000 | 0.000000 |
| 1 | 0.2 | 1.200000 | 1.221403 | 0.021403 |
| 2 | 0.4 | 1.440000 | 1.491825 | 0.051825 |
| 3 | 0.6 | 1.728000 | 1.822119 | 0.094119 |
| 4 | 0.8 | 2.073600 | 2.225541 | 0.151941 |
| 5 | 1.0 | 2.488320 | 2.718282 | 0.229962 |

En t=1, Euler produce 2.488320 frente al valor exacto e≈2.718282, con un error absoluto de aproximadamente 0.229962. En este ejemplo subestima el crecimiento exponencial porque aproxima cada tramo mediante una recta con la pendiente al inicio del paso. Reducir h mejora la aproximación; Euler es un método de primer orden.

## 5. Ejecución

Se requiere **Python 3.9 o posterior**. Solo se utiliza `math`, incluida en la biblioteca estándar: no es necesario instalar paquetes adicionales.

Descarga el repositorio, abre una terminal en su carpeta y ejecuta:

```bash
python euler.py
```

En sistemas donde el intérprete se llama `python3`:

```bash
python3 euler.py
```

El programa imprime la ecuación, la solución exacta y la tabla comparativa.

## 6. Archivos

- `euler.py`: funciones de solución exacta, aproximación de Euler e impresión de resultados.
- `README.md`: planteamiento, desarrollo analítico, método numérico, resultados e instrucciones.
- `.gitignore`: excluye archivos temporales de Python y entornos virtuales.
