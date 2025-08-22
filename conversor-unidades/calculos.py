def calcular_comprimento(valor, unidade_1, unidade_2):
    unidades_m = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1,
            'km': 1000,
            'inches': 0.0254,
            'ft': 0.3048,
            'yard': 0.9144,
            'miles': 1609.34
    }

    if unidade_1 not in unidades_m and unidade_2 not in unidades_m:
        return 'Unidade inválida'

    valor_m = valor * unidades_m[unidade_1]

    resultado = valor_m / unidades_m[unidade_2]

    return round(resultado, 4)

def calcular_peso(valor, peso_1, peso_2):
    unidades_kg = {
        'mg': 1000000,
        'g': 1000,
        'kg': 1,
        'ounce': 35.274,
        'pound': 2.20462
    }

    if peso_1 not in unidades_kg and peso_2 not in unidades_kg:
        return 'Unidade inválida'
    
    valor_kg = valor / unidades_kg[peso_1]
    
    resultado = valor_kg * unidades_kg[peso_2]

    return round(resultado, 4)

def calcular_temperatura(valor, temperatura_1, temperatura_2):
    
    if temperatura_1 == temperatura_2:
        return round(valor, 4)
    
    if temperatura_1 == 'Celsius' and temperatura_2 == 'Fahrenheit':
        resultado = (valor * 9/5) + 32
    elif temperatura_1 == 'Celsius' and temperatura_2 == 'Kelvin':
        resultado = valor + 273.15
    
    elif temperatura_1 == 'Fahrenheit' and temperatura_2 == 'Celsius':
        resultado = (valor - 32) * 5/9
    elif temperatura_1 == 'Fahrenheit' and temperatura_2 == 'Kelvin':
        resultado = (valor - 32) * 5/9 + 273.15

    elif temperatura_1 == 'Kelvin' and temperatura_2 == 'Celsius':
        resultado = valor - 273.15
    elif temperatura_1 == 'Kelvin' and temperatura_2 == 'Fahrenheit':
        resultado = (valor - 273.15) * 9/5 + 32

    return round(resultado, 4)

        