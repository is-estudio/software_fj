def registrar_error(mensaje):
    with open("logs.txt", "a") as f:
        f.write(mensaje + "\n")
