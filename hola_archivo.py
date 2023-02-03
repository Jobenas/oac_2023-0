def func(a: int, b: int) -> int:
    return a + b

print("Estoy por fuera del nombre main")

if __name__ == '__main__':
    print("Estoy en el parte que se ejecuta cuando se llama al archivo directamente")
    print(func(1, 2))