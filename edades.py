edades = []
i = 0
while i < 6:
	try:
		val = input(f"Ingrese la edad #{i+1}: ").strip()
		edad = int(val)
		if edad < 0:
			print("La edad no puede ser negativa. Intente de nuevo.")
			continue
		edades.append(edad)
		i += 1
	except ValueError:
		print("Entrada inválida. Ingrese un número entero.")

promedio = sum(edades) / len(edades)
print(f"\nEdades: {', '.join(map(str, edades))}")
print(f"Promedio de las 6 edades: {promedio:.2f}")

