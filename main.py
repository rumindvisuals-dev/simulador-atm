# Simulador ATM

# Saldo inicial del usuario
BALANCE = 9999  

# Opciones del menú principal
OPTIONS = {
    1: 'Consultar saldo',
    2: 'Retirar',
    3: 'Depositar',
    'q': 'Salir'
}

# Mensaje de bienvenida
welcome_message = '''
*** Cajero Automático de Ciudad Gótica ***
    --- Bienvenid@ ---'''

print(welcome_message)  # Muestra el mensaje de bienvenida al iniciar el programa

# Bucle principal del programa para mantener el cajero en ejecución
while True:
    # Mostrar las opciones disponibles al usuario
    print('\n*** Opciones ***\n')
    for number_option, option_message in OPTIONS.items():
        print(f"{number_option} - {option_message}")

    # Solicitar al usuario que ingrese una opción
    option = input('\nIngresa la opción deseada: ')

    # Si la entrada es un número, se procesa como una opción
    if option.isdigit():
        option = int(option)

        if option == 1:
            # Opción 1: Consultar saldo
            print('\nConsultando tu saldo...')
            print(f"Tu saldo actual es: ${BALANCE:.2f}")
        
        elif option == 2:
            # Opción 2: Retirar dinero
            print('\nRealizando retiro...')
            withdraw = input('Ingresa el monto a retirar: ')
            try:
                withdraw = float(withdraw)  # Convertir el monto ingresado a un número
                if withdraw <= 0:
                    print("No puedes retirar una cantidad negativa o igual a cero.")
                elif withdraw > BALANCE:
                    print("Saldo insuficiente.")  # Validar si el saldo es suficiente
                else:
                    # Actualizar el saldo después del retiro
                    print('Retirando cantidad...')
                    BALANCE -= withdraw
                    print(f"Has retirado ${withdraw:.2f}. Tu nuevo saldo es: ${BALANCE:.2f}")
            except ValueError:
                print("Ingresa un valor numérico válido.")  # Capturar errores de conversión
        
        elif option == 3:
            # Opción 3: Depositar dinero
            print('\nRealizando depósito...')
            deposit = input('Ingresa el monto a depositar: ')
            try:
                deposit = float(deposit)  # Convertir el monto ingresado a un número
                if deposit <= 0:
                    print("No puedes depositar una cantidad negativa o igual a cero.")
                else:
                    # Actualizar el saldo después del depósito
                    BALANCE += deposit
                    print(f"Has depositado ${deposit:.2f}. Tu nuevo saldo es: ${BALANCE:.2f}")
            except ValueError:
                print("Ingresa un valor numérico válido.")  # Capturar errores de conversión
        
        else:
            # Si la opción no es válida, se notifica al usuario
            print('Opción inválida. Selecciona otra opción.\n')

    elif option.lower() == 'q':
        # Opción 'q': Salir del programa
        print('Gracias por usar el Cajero Automático de Ciudad Gótica. ¡Adiós!')
        break  # Romper el bucle principal para salir del programa

    else:
        # Manejo de opciones no válidas (ni numéricas ni 'q')
        print('Opción inválida. Selecciona otra opción.\n')
        continue  # Continuar con la siguiente iteración del bucle principal

    # Solicitar al usuario si desea realizar otra operación
    while True:
        continue_option = input('\n¿Deseas realizar otra operación? (y|n): ').lower()
        if continue_option == 'y':
            # Si elige 'y', regresar al menú principal
            break
        elif continue_option == 'n':
            # Si elige 'n', salir del programa con un mensaje de despedida
            print('Gracias por usar el Cajero Automático de Ciudad Gótica. ¡Adiós!')
            exit()
        else:
            # Manejo de entradas no válidas en esta sección
            print("Opción inválida. Por favor ingresa 'y' para sí o 'n' para no.")
