# -*- coding: utf-8 -*-
"""
Algoritmo de Factorización por Ecuación Combinatoria (2*p1 - p2)
Busca factores primos de un número N encontrando un C tal que C^2 + 8*N sea un cuadrado perfecto.
"""
import math
import time

def es_primo(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def factorizar_por_ecuacion(N):
    if N % 2 == 0:
        return 2, N // 2
    
    start_time = time.time()
    
    # C = 2*p1 - p2
    # El rango de búsqueda para C_squared = C^2 es de 1 hasta 8*N.
    # Dado que C = 2*p1 - p2, para cualquier par de factores p1, p2,
    # C es siempre un número impar.
    # Probamos secuencialmente C = 1, 3, 5, 7...
    
    intentos = 0
    C = 1
    limite = int(math.sqrt(8 * N))
    
    while C <= limite:
        intentos += 1
        val = C**2 + 8 * N
        Y = math.isqrt(val)
        
        if Y * Y == val:
            # Encontramos un cuadrado perfecto. Calculamos los factores correspondientes
            # p1 = (Y + C) / 4 y p2 = (Y - C) / 2 (para C positivo)
            if (Y + C) % 4 == 0:
                p1 = (Y + C) // 4
                p2 = (Y - C) // 2
                if p1 * p2 == N and p1 > 1 and p2 > 1:
                    end_time = time.time()
                    return p1, p2, intentos, end_time - start_time
            
            # O la versión simétrica (para C negativo, es decir, p2 > 2*p1)
            if (Y - C) % 4 == 0:
                p1 = (Y - C) // 4
                p2 = (Y + C) // 2
                if p1 * p2 == N and p1 > 1 and p2 > 1:
                    end_time = time.time()
                    return p1, p2, intentos, end_time - start_time
                    
        C += 2 # C siempre es impar para factores primos impares
            
    return None

# Pruebas con compuestos reales (factores primos impares)
numeros_prueba = [
    143,        # 11 * 13
    2021027,    # 1009 * 2003
    1887839,    # 1009 * 1871 (ambos primos reales de tu lista)
    5148359     # ¿Es primo? Si no encuentra factores, es primo
]

print("--- SIMULACIÓN DE FACTORIZACIÓN POR ECUACIÓN COMBINATORIA ---")
for N in numeros_prueba:
    print(f"\nFactorizando N = {N}...")
    res = factorizar_por_ecuacion(N)
    if res:
        p1, p2, intentos, t = res
        print(f"¡Éxito! Factores encontrados: {p1} x {p2} = {N}")
        print(f"Comprobación: p1({p1}) es primo? {es_primo(p1)} | p2({p2}) es primo? {es_primo(p2)}")
        print(f"Ecuación del usuario: C = 2*p1 - p2 = 2*{p1} - {p2} = {2*p1 - p2}")
        print(f"Verificación de la ecuación: C^2 + 8*N = ({2*p1 - p2})^2 + 8*{N} = {abs(2*p1 - p2)**2 + 8*N} (Raíz: {math.isqrt(abs(2*p1 - p2)**2 + 8*N)})")
        print(f"Intentos (valores de C evaluados): {intentos}")
        print(f"Tiempo de ejecución: {t*1000:.3f} ms")
    else:
        print("No se encontraron factores. El número es primo.")
