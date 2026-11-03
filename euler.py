"""Solución exacta y aproximación de y' = y, y(0) = 1, con Euler."""

from math import exp


def solucion_exacta(t: float) -> float:
    """La separación de variables da y(t) = e^t."""
    return exp(t)


def euler() -> list[tuple[float, float]]:
    """Realiza cinco pasos de h=0.2 en [0, 1], incluido el punto inicial."""
    h = 0.2
    y = 1.0
    puntos = [(0.0, y)]
    for n in range(1, 6):
        # Euler explícito: y_(n+1) = y_n + h*f(t_n, y_n); f(t,y)=y.
        y = y + h * y
        t = n * h  # Evita acumular el error de sumar repetidamente h.
        puntos.append((t, y))
    return puntos


def main() -> None:
    print("Ecuación: y' = y; condición inicial: y(0) = 1")
    print("Solución exacta: y(t) = exp(t)")
    print("Método de Euler: intervalo [0, 1], h = 0.2, cinco pasos\n")
    print(f"{'n':>2} {'t':>5} {'Euler':>12} {'Exacta':>12} {'Error absoluto':>16}")
    for n, (t, aproximacion) in enumerate(euler()):
        exacta = solucion_exacta(t)
        error = abs(exacta - aproximacion)
        print(f"{n:2d} {t:5.1f} {aproximacion:12.6f} {exacta:12.6f} {error:16.6f}")


if __name__ == "__main__":
    main()
