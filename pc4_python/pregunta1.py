import requests

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float'] 
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al consultar el precio de Bitcoin: {e}")
        return None

def calcular_valor_bitcoins(n, precio_usd):
    return n * precio_usd

def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
        precio_usd = obtener_precio_bitcoin()

        if precio_usd is not None:
            valor = calcular_valor_bitcoins(n, precio_usd)
            print(f"El costo actual de {n} Bitcoins en USD es: ${valor:,.4f}")
        else:
            print("No se pudo obtener el precio de Bitcoin.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()

