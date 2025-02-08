import argparse
import json
import time


def main():
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("priceCatalogue")
    parser.add_argument("salesRecord")
    args = parser.parse_args()

    # Inicio variables por si hay error.
    catalogo = []
    ventas = []

    # Abrir y cargar los archivos
    try:
        with open(
            args.priceCatalogue,
            'r',
            encoding='utf-8'
        ) as archivo_catalogo:
            catalogo = json.load(archivo_catalogo)
    except Exception as e:
        print(f"Error al cargar el catálogo: {e}")

    try:
        with open(args.salesRecord, 'r', encoding='utf-8') as archivo_ventas:
            ventas = json.load(archivo_ventas)
    except Exception as e:
        print(f"Error al cargar el registro de ventas: {e}")

    # # Diccionario y calculo
    precios_catalogo = {}
    for item in catalogo:
        try:
            precios_catalogo[item["title"]] = item["price"]
        except Exception as e:
            print(f"Error procesando elemento del catálogo {item}: {e}")

    costo_total = 0
    for venta in ventas:
        try:
            producto = venta["Product"]
            cantidad = venta["Quantity"]
            precio = precios_catalogo[producto]
            costo_total += cantidad * precio
        except Exception as e:
            print(f"Error procesando venta {venta}: {e}")

    # Tiempo
    elapsed_time = time.time() - start_time

    # Escribir los resultados
    try:
        with open(
            "SalesResults.txt",
            'a',
            encoding='utf-8'
        ) as archivo_resultados:
            archivo_resultados.write("RESULTADOS DE LA EJECUCIÓN\n")
            archivo_resultados.write("===========================\n")
            archivo_resultados.write(
                f"Archivo de catálogo: {args.priceCatalogue}\n"
            )
            archivo_resultados.write(
                f"Archivo de ventas: {args.salesRecord}\n")
            archivo_resultados.write(f"Costo Total: {costo_total}\n")
            archivo_resultados.write(
                f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n")
    except Exception as e:
        print(f"Error al escribir el archivo de resultados: {e}")

    # Imprimir resultados
    print("RESULTADOS DE LA EJECUCIÓN")
    print("===========================")
    print(f"Archivo de catálogo: {args.priceCatalogue}")
    print(f"Archivo de ventas: {args.salesRecord}")
    print(f"Costo Total: {costo_total}")
    print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")


if __name__ == "__main__":
    main()
