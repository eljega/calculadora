import random
num = random.randint(0,101)

while True:
    select_num = input("Ingresa un numero del 0 al 100 (o 'q' para salir): ")
    if select_num == 'q':
        print("Juego terminado. El numero era: ", num)
        break
    select_num = int(select_num)
    if select_num < num:
        print("Tu numero: ", select_num, " es muy bajo")
    elif select_num > num:
        print("Tu numero: ", select_num, " es muy alto")
    else:
        print("¡Correcto! El numero era: ", num)
        break