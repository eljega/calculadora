# Pedir al usuario que ingrese una expresion matemática
operator = input("Ingresa la expresión matemática: ")

# Validar que la expresion solo contiene caracteres validos
# (numeros y los operadores basicos: +, -, *, /)
if not all(i.isdigit() or i in ['+', '-', '*', '/'] for i in operator):
    print("Expresión inválida")
else:
    try:
        # Evaluar la expresion matematica ingresada por el usuario
        result = eval(operator)
        # Imprimir el resultado
        print("El resultado es:", result)
    except:
        # Si ocurre un error al evaluar la expresion, imprimir un mensaje de error
        print("Expresión inválida")
