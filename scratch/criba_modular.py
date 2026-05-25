# -*- coding: utf-8 -*-
"""
Criba Modular de Residuos Cruzados
Evalúa la eficiencia de un filtro basado en congruencias para eliminar compuestos
generados por la ecuación C = 2*p1 - p2 sin usar pruebas de primalidad costosas.
"""
import math

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

# Generamos los primeros 200 primos
primos = []
n = 2
while len(primos) < 200:
    if es_primo(n):
        primos.append(n)
    n += 1

limite_superior = primos[-1]

# Primos de la criba modular
primos_criba = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

total_generados = 0
compuestos_totales = 0
primos_totales = 0

compuestos_filtrados = 0
compuestos_que_pasaron = 0

print("Analizando combinaciones para C = 2*p1 - p2...")

for i in range(len(primos)):
    p1 = primos[i]
    for j in range(len(primos)):
        p2 = primos[j]
        
        C = 2 * p1 - p2
        if C <= 1 or C > limite_superior:
            continue
            
        total_generados += 1
        es_C_primo = es_primo(C)
        
        if es_C_primo:
            primos_totales += 1
        else:
            compuestos_totales += 1
            
        # Aplicamos el filtro de Criba Modular de Residuos Cruzados
        # Si C es divisible por algún primo q de la criba (y C > q), entonces es compuesto.
        # Esto equivale a verificar si 2*p1 - p2 es divisible por q, es decir, 2*p1 = p2 mod q.
        filtrado = False
        for q in primos_criba:
            if C > q and (2 * p1) % q == p2 % q:
                filtrado = True
                break
                
        if not es_C_primo:
            if filtrado:
                compuestos_filtrados += 1
            else:
                compuestos_que_pasaron += 1

porcentaje_filtrado = (compuestos_filtrados / compuestos_totales) * 100 if compuestos_totales > 0 else 0
print("\n--- RESULTADOS DE LA CRIBA MODULAR ---")
print(f"Total candidatos válidos en rango: {total_generados}")
print(f"Primos reales generados:           {primos_totales}")
print(f"Compuestos generados:              {compuestos_totales}")
print(f"Compuestos filtrados por residuos: {compuestos_filtrados}")
print(f"Compuestos que evadieron el filtro:{compuestos_que_pasaron}")
print(f"Porcentaje de compuestos filtrados: {porcentaje_filtrado:.2f}%")
