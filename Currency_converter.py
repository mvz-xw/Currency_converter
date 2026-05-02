def convertir():
    tasas = {
        "USD": 1,
        "PEN": 3.75,
        "EUR": 0.92,
        "MXN": 17.5,
        "BRL": 5.0,
        "COP": 4000,
        "GBP": 0.79,
    }

    print("=== CONVERSOR DE MONEDAS ===")
    print("Monedas disponibles:", ", ".join(tasas.keys()))

    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Convertir moneda")
        print("2. Salir")

        opcion = input("\nElige una opción (1/2): ")

        if opcion == "2":
            print("¡Hasta luego! 👋")
            break
        elif opcion == "1":
            try:
                cantidad = float(input("¿Cuánto dinero? "))
                moneda_origen = input("¿De qué moneda? ").upper()
                moneda_destino = input("¿A qué moneda? ").upper()

                if moneda_origen not in tasas or moneda_destino not in tasas:
                    print("❌ Moneda no disponible")
                    continue

                en_dolares = cantidad / tasas[moneda_origen]
                resultado = en_dolares * tasas[moneda_destino]
                print(f"\n✅ {cantidad} {moneda_origen} = {resultado:.2f} {moneda_destino}")

            except ValueError:
                print("❌ Ingresa un número válido")
        else:
            print("❌ Opción no válida")

convertir()