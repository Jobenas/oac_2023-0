


if __name__ == '__main__':
    with open("notas.csv", "r") as f:
        contenido = f.read()
    
    contenido = contenido.split("\n")
    print(contenido)
