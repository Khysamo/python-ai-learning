import os
import csv
import requests 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obtener_clima(ciudad: str) -> dict:
    parametros = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }
    respuesta = requests.get(BASE_URL, params=parametros)
    respuesta.raise_for_status()
    return respuesta.json()

def guardar_en_csv(datos: dict, nombre_archivo: str) -> None:
    with open(nombre_archivo, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([
            datos["name"],
            datos["main"]["temp"],
            datos["main"]["humidity"],
            datos["weather"][0]["description"]
        ])

def main() -> None:
    ciudad = input("¿De qué ciudad te gustaria saber el clima?")
    datos = obtener_clima(ciudad)
    guardar_en_csv(datos, "clima_datos.csv")
    print(f"Ciudad: {datos['name']}")
    print(f"Temperatura: {datos['main']['temp']}°C")
    print(f"Humedad: {datos['main']['humidity']}%")
    print(f"Condicion: {datos['weather'][0]['description']}")


if __name__ == "__main__":
    main()