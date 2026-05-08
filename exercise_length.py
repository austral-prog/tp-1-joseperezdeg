def length():
    """
    Ejercicio 7 - Conversión de Unidades de Longitud

    Dada una distancia en metros, convertir e imprimir:
    1. Kilómetros (1 km = 1000 m)
    2. Millas (1 milla ≈ 1609.34 m)
    3. Pies (1 pie ≈ 0.3048 m)
    4. Pulgadas (1 pulgada ≈ 0.0254 m)
    """
    m = 1000
    km = m/1000
    milla = m/1609.34
    pie = m / 0.3048
    pulgadas = m / 0.0254
    print(km)
    print(milla)
    print(pie)
    print(pulgadas)
length()
