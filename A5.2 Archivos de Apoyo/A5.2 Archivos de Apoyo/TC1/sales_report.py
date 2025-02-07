import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("catalogo")  
    parser.add_argument("ventas")   
    args = parser.parse_args()

    # Abrir y cargar los archivos
    with open(args.catalogo, 'r', encoding='utf-8') as archivo_catalogo:
        catalogo = json.load(archivo_catalogo)
    with open(args.ventas, 'r', encoding='utf-8') as archivo_ventas:
        ventas = json.load(archivo_ventas)

    # Diccionario y calculo
    precios_catalogo = {item["title"]: item["price"] for item in catalogo}
    costo_total = sum(venta["Quantity"] * precios_catalogo[venta["Product"]] for venta in ventas)

    # Escribir los resultados
    with open("resultados.txt", 'w', encoding='utf-8') as archivo_resultados:
        archivo_resultados.write(f"Archivo de catálogo: {args.catalogo}\n")
        archivo_resultados.write(f"Archivo de ventas: {args.ventas}\n")
        archivo_resultados.write(f"Costo Total: {costo_total}\n")

    print(f"Costo Total: {costo_total}")

if __name__ == "__main__":
    main()
