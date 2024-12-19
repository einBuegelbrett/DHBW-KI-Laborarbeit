# Zimmer
def get_zimmer(zimmer: str) -> int:
    if zimmer in ['Ein Zimmer', '1 Zimmer']:
        return 0
    elif zimmer in ['Zwei Zimmer', 'Drei Zimmer', '2 Zimmer', '3 Zimmer', '1-2 Zimmer', '2-3 Zimmer', ]:
        return 1
    elif zimmer in ['Vier Zimmer', 'Fünf Zimmer', '3-4 Zimmer', '4-5 Zimmer', '4 Zimmer', '5 Zimmer']:
        return 2
    elif zimmer in ['Sechs Zimmer', '5-6 Zimmer', '6 Zimmer']:
        return 3

# Stockwerk
def get_stockwerk(range_str: str) -> int:
    if isinstance(range_str, str):
        if "EG" in range_str:
            return 0
        elif "1.Stock" in range_str:
            return 1
        elif "2.Stock" in range_str:
            return 2
        elif "3.Stock" in range_str:
            return 3
        elif "4.Stock" in range_str:
            return 4
        elif "5.Stock" in range_str:
            return 5
        elif "6.Stock" in range_str:
            return 6
        elif "7.Stock" in range_str:
            return 7
        elif "8.Stock" in range_str:
            return 8
        elif "9.Stock" in range_str:
            return 9
    return -1

# Heizung
def get_heizung(range_str: str) -> int:
    if isinstance(range_str, str):
        if "Erdwaerme" in range_str:
            return 0
        elif "Gas-Etage" in range_str:
            return 1
        elif "Gas-Zentral" in range_str:
            return 2
        elif "Lüftungsheizung" in range_str:
            return 3
        elif "Oel" in range_str:
            return 4
        elif "Pellets" in range_str:
            return 5
    return -1

# Kindergarten
def get_kindergarten(range_str: str) -> int:
    if isinstance(range_str, str):
        if "nah" in range_str:
            return 2
        elif "erreichbar" in range_str:
            return 1
        elif "fern" in range_str:
            return 0
    return -1

# Schule
def get_schule(range_str: str) -> int:
    if isinstance(range_str, str):
        if "nah" in range_str:
            return 2
        elif "erreichbar" in range_str:
            return 1
        elif "fern" in range_str:
            return 0
    return -1

# S-Bahn
def get_bahn(range_str: str) -> int:
    if isinstance(range_str, str):
        if "nah" in range_str:
            return 4
        elif "erreichbar" in range_str:
            return 3
        elif "mit Bus" in range_str:
            return 2
        elif "fern" in range_str:
            return 1
        elif "nein" in range_str:
            return 0
    return -1

# miete
def get_miete(value: str) -> int:
    if '-' in value:
        start, end = value.split('-')
        return int(round((int(start) + int(end)) / 2))
    else:
        return int(value)

# Funktion zum Berechnen des Durchschnitts aus einem Wertebereich
def get_nebenkosten(range_str: str) -> int:
    if isinstance(range_str, str):
        if "ueber" in range_str:
            return 300
        elif "unter" in range_str:
            return 50
        else:
            # Teile den Wertebereich in zwei Zahlen auf
            start, end = map(int, range_str.split('-'))
            # Berechne den Durchschnitt
            return int(round((start + end) / 2))
    return -1

# Alter
def get_alter(range_str: str) -> int:
    if isinstance(range_str, str):
        if "ueber" in range_str:  # "ueber 100 Jahre"
            return 100
        elif "Neubau" in range_str:  # Neubau als 0 interpretieren
            return 0
        else:
            # Splitte den Wertebereich bei '-' und entferne "Jahre"
            numbers = range_str.split('-')
            start, end = list(map(int, [numbers[0].strip(), numbers[1].replace("Jahre", "").strip()]))
            return int(round((start + end) / 2))  # Durchschnitt berechnen
    return -1

# Lage
def get_lage(range_str: str) -> int:
    if isinstance(range_str, str):
        if "Hauptstrasse" in range_str:
            return 4
        elif "Spielstrasse" in range_str:
            return 3
        elif "Wohngebiet" in range_str:
            return 2
        elif "Nebenstrasse" in range_str:
            return 1
        if "Abgelegen" in range_str:
            return 0
    return -1

# Stadtmitte
def get_stadtmitte(range_str: str) -> int:
    if isinstance(range_str, str):
        if "Zentrum" in range_str:
            return 0
        if "<" in range_str:
            return 3
        elif ">" in range_str:
            return 30
        else:
            numbers = range_str.split('-')
            start, end = list(map(int, [numbers[0].strip(), numbers[1].replace(" km", "").strip()]))
            return int(round((start + end) / 2))
    return -1

# Kaution
def get_kaution(range_str: str) -> int:
    if isinstance(range_str, str):
        if "ueber" in range_str:  # "ueber 100 Jahre"
            return 3000
        elif "keine" in range_str:  # Neubau als 0 interpretieren
            return 0
        else:
            start, end = map(int, range_str.split('-'))
            return int(round((start + end) / 2))
    return -1

# Kueche
def get_kueche(range_str: str) -> int:
    if isinstance(range_str, str):
        if "keine" in range_str:
            return 0
        elif "Kueche (alt)" in range_str:
            return 1
        elif "Kueche (neu)" in range_str:
            return 2
    return -1

# Bad
def get_bad(range_str: str) -> int:
    if isinstance(range_str, str):
        if "Badewanne" in range_str:
            return 0
        elif "Dusche" in range_str:
            return 1
        elif "Dusche + Wanne" in range_str:
            return 2
        elif "Dusche auf Flur" in range_str:
            return 3
        elif "Waschbecken" in range_str:
            return 4
    return -1

# mobliert
def get_mobliert(range_str: str) -> int:
    if isinstance(range_str, str):
        if "ja" in range_str:
            return 2
        elif "teilmoebliert" in range_str:
            return 1
        elif "nein" in range_str:
            return 0
    return -1

def get_quadratmeter(range_str: str) -> int:
    if isinstance(range_str, str):
        if "ueber" in range_str:
            return 120
        elif "bis" in range_str:
            return 20
        else:
            start, end = map(int, range_str.split('-'))
            return int(round((start + end) / 2))
    return -1

