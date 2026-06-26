import csv
import requests
import os

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
CLIMA_URL = "https://api.open-meteo.com/v1/forecast"

def obtener_coordenadas(ciudad: str) -> tuple[float, float]:
    parametros = {
        "name": ciudad,
        "count": 1,
        "language": "es",
        "format": "json"
    }
    respuesta = requests.get(GEOCODING_URL, params=parametros)
    respuesta.raise_for_status()
    resultados = respuesta.json()["results"]
    return resultados[0]["latitude"], resultados[0]["longitude"]

def obtener_clima(latitud: float, longitud: float) -> dict:
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation",
        "timezone": "auto"
    }
    respuesta = requests.get(CLIMA_URL, params=parametros)
    respuesta.raise_for_status()
    return respuesta.json()["current"]

def guardar_en_csv(ciudad: str, datos: dict, nombre_archivo: str) -> None:
    archivo_existe = os.path.exists(nombre_archivo)
    with open(nombre_archivo, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        if not archivo_existe:
            escritor.writerow([
                "Ciudad",
                "Temperatura (°C)",
                "Humedad (%)",
                "Viento (km/h)",
                "Precipitación (mm)"
            ]) 
            escritor.writerow([
                ciudad,
                datos["temperature_2m"],
                datos["relative_humidity_2m"],
                datos["wind_speed_10m"],
                datos["precipitation"]
            ])
        else:
            escritor.writerow([
                ciudad,
                datos["temperature_2m"],
                datos["relative_humidity_2m"],
                datos["wind_speed_10m"],
                datos["precipitation"]
            ])
    


def main() -> None:
    ciudad = input("¿De que ciudad te gustaria saber el clima?")
    latitud, longitud = obtener_coordenadas(ciudad)
    datos = obtener_clima(latitud, longitud)
    guardar_en_csv(ciudad, datos, "clima_datos.csv")
    print(f"Ciudad: {ciudad}")
    print(f"Temperatura: {datos['temperature_2m']}°C")
    print(f"Humedad: {datos['relative_humidity_2m']}%")
    print(f"Viento: {datos['wind_speed_10m']} km/h")
    print(f"Precipitación: {datos['precipitation']}mm")


if __name__ == "__main__":
    main()

