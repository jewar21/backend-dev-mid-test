"""
Punto 2: Escribe una función en lenguaje de su preferencia que tome 
una lista de enteros y un entero de destino, y devuelva los índices
de los dos números que sumados dan el resultado del entero destino.
"""


def find_two_sum(nums, target):
    index_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i
    return []


nums = [2, 7, 11, 15]

try:
    target = int(input(f"Recuerda que esta es la lista: {nums}\n¿Qué número estás buscando?\n"))
    result = find_two_sum(nums, target)

    if result:
        i1, i2 = result
        print("\nResultado encontrado:")
        print(f"Índices: {result}")
        print(f"Valores: {nums[i1]} + {nums[i2]} = {target}")
    else:
        print("\n No se encontraron dos números en la lista que sumen el valor solicitado")
        print(f"Lista evaluada: {nums}")
        
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero")
