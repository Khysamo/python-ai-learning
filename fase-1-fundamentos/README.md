# Fase 1 — Fundamentos de Python

## Proyecto: Consulta de Clima

Script que consulta el clima actual de cualquier ciudad del mundo usando la API gratuita de Open-Meteo y guarda el historial de consultas en un archivo CSV.

## ¿Qué hace?

- Recibe el nombre de una ciudad del usuario
- Convierte el nombre en coordenadas geográficas usando la API de Geocoding
- Consulta temperatura, humedad, viento y precipitación en tiempo real
- Guarda cada consulta en `clima_datos.csv` con títulos automáticos

## Cómo ejecutarlo

1. Activa el entorno virtual:
```bash
source venv/bin/activate