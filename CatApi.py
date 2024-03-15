import requests
import os

def pobierz_zdjecie_kota(liczba_zdjec=1):
    # Tworzenie URL-a do zapytania do The Cat API z określonym limitem zdjęć
    url = f'https://api.thecatapi.com/v1/images/search?limit={liczba_zdjec}'

    try:
        # Wykonanie zapytania HTTP GET do API
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie, czy zapytanie zakończyło się sukcesem
        dane = response.json()  # Pobranie danych w formacie JSON

        # Pobranie tylko określonej liczby zdjęć, jeśli API zwróciło więcej niż oczekiwano
        for zdjecie in dane[:liczba_zdjec]:
            url_zdjecia = zdjecie['url']
            pobierz_obraz(url_zdjecia)

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas pobierania danych: {e}')

def pobierz_obraz(url):
    try:
        # Wykonanie zapytania HTTP GET, aby pobrać obraz
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie, czy zapytanie zakończyło się sukcesem

        # Pobranie samej nazwy pliku z URL
        nazwa_pliku = os.path.basename(url)

        # Zapisanie obrazu w bieżącym katalogu
        with open(nazwa_pliku, 'wb') as plik:
            plik.write(response.content)

        print(f'Zapisano obraz: {nazwa_pliku}')

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas pobierania obrazu: {e}')

if __name__ == '__main__':
    liczba_zdjec_do_pobrania = 1  # Określenie ilości zdjęć do pobrania
    pobierz_zdjecie_kota(liczba_zdjec_do_pobrania)