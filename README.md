# Simulador de Cajero Automático

Este es un simulador de **Cajero Automático (ATM)** que permite realizar operaciones bancarias básicas como consultar saldo, retirar dinero y depositar dinero. El programa proporciona un menú interactivo para que el usuario pueda realizar estas operaciones de manera sencilla.

## Características

- **Consultar saldo**: Muestra el saldo actual de la cuenta.
- **Retirar dinero**: Permite retirar una cantidad específica, validando que el monto no sea negativo y que haya suficiente saldo disponible.
- **Depositar dinero**: Permite depositar una cantidad específica, asegurándose de que el monto sea positivo.
- **Salir**: Permite salir del programa de manera segura con un mensaje de despedida.

## Requisitos

- Python 3

## Instalación

1. Clona el repositorio o descarga el archivo `atm_simulador.py`:

   ```bash
   git clone https://github.com/rumindvisuals-dev/simulador-atm.git 
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd simulador-atm
   ```

3. Ejecuta el script en tu terminal o línea de comandos:

   ```bash
   python main.py
   ```

## Uso

Al ejecutar el programa, se te presentará un menú con las siguientes opciones:

1. **Consultar saldo**: Muestra el saldo actual disponible en la cuenta.
2. **Retirar dinero**: Te solicita ingresar el monto a retirar y verifica si es válido y si tienes suficiente saldo.
3. **Depositar dinero**: Permite ingresar el monto a depositar, validando que sea positivo.
4. **Salir**: Finaliza la sesión del cajero automático.

El programa repetirá el menú de opciones hasta que elijas salir.

# Contribuciones

Si deseas contribuir a este proyecto, no dudes en hacer un fork del repositorio y enviar tus pull requests. Asegúrate de seguir las buenas prácticas de codificación y agregar pruebas si es necesario.
