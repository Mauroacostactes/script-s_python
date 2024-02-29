import requests

def obtener_ubicacion(numero_telefono):
    google_maps_api_key = 'tu_google_maps_api_key'

    url = f'https://www.googleapis.com/maps/api/geocode/json?address={numero_telefono}&key={google_maps_api_key}'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location
    else:
        return None

if __name__ == '__main__':
    numero_telefono_prueba = 'tu_numero_telefono'  # Reemplazr
    ubicacion = obtener_ubicacion(numero_telefono_prueba)
    print(ubicacion)
