cadena="Hola mundo"
cadena_2="tu puedes conquistarlo"
print(cadena,cadena_2)
print(len(cadena))
op="S"
while op.upper()!="N":
    cad = input("ingrese un nombre: ")
    if len(cad)>=8:
        print(cad)

    else:
        print("Ingresar una cadena mayor a 8 caracteres")

    op=input("Para terminar con la funcion primaria[N]: ")