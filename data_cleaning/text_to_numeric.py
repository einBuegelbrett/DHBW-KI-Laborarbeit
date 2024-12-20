# Ja und Nein
def get_yes_no(value: str) -> int:
    """
    Wandelt 'ja' und 'nein' in numerische Werte um.

    :param value: Möglicher Wert des Attributs ('ja' oder 'nein')
    :return: 1 für 'ja', 0 für 'nein'
    :raises Exception: Wenn der Wert ungültig ist
    """
    if value == "ja":
        return 1
    elif value == "nein":
        return 0
    else:
        raise Exception(f"Ungültiger Wert: {value}. Erwartet 'ja' oder 'nein'.")


# Zimmer
def get_zimmer(zimmer: str) -> int:
    """
    Klassifiziert Zimmeranzahl in numerische Werte.

    :param zimmer: Textuelle Beschreibung der Zimmeranzahl
    :return: Numerischer Wert für Zimmeranzahl
    :raises Exception: Wenn der Wert ungültig ist
    """
    if zimmer in ['Ein Zimmer', '1 Zimmer']:
        return 0
    elif zimmer in ['Zwei Zimmer', 'Drei Zimmer', '2 Zimmer', '3 Zimmer', '1-2 Zimmer', '2-3 Zimmer', ]:
        return 1
    elif zimmer in ['Vier Zimmer', 'Fünf Zimmer', '3-4 Zimmer', '4-5 Zimmer', '4 Zimmer', '5 Zimmer']:
        return 2
    elif zimmer in ['Sechs Zimmer', '5-6 Zimmer', '6 Zimmer']:
        return 3
    else:
        raise Exception(f"Ungültiger Wert: {zimmer}. Erwartet eine gültige Zimmerbeschreibung.")


# Stockwerk
def get_stockwerk(range_str: str) -> int:
    """
    Wandelt Stockwerkbeschreibung in numerische Werte um.

    :param range_str: Textuelle Beschreibung des Stockwerks
    :return: Numerischer Wert für das Stockwerk
    :raises Exception: Wenn der Wert ungültig ist
    """
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
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet eine gültige Stockwerkbeschreibung.")


# Heizung
def get_heizung(range_str: str) -> int:
    """
    Wandelt Heizungsarten in numerische Werte um.

    :param range_str: Textuelle Beschreibung der Heizung
    :return: Numerischer Wert für die Heizung
    :raises Exception: Wenn der Wert ungültig ist
    """
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
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet eine gültige Heizungsbeschreibung.")


# Kindergarten
def get_kindergarten(range_str: str) -> int:
    """
    Wandelt die Nähe eines Kindergartens in numerische Werte um.

    :param range_str: Textuelle Beschreibung der Entfernung ('nah', 'erreichbar', 'fern')
    :return: 2 für 'nah', 1 für 'erreichbar', 0 für 'fern'
    :raises Exception: Wenn der Wert ungültig ist
    """
    if isinstance(range_str, str):
        if "nah" in range_str:
            return 2
        elif "erreichbar" in range_str:
            return 1
        elif "fern" in range_str:
            return 0
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet 'nah', 'erreichbar' oder 'fern'.")


# Schule
def get_schule(range_str: str) -> int:
    """
    Wandelt die Nähe einer Schule in numerische Werte um.

    :param range_str: Textuelle Beschreibung der Entfernung ('nah', 'erreichbar', 'fern')
    :return: 2 für 'nah', 1 für 'erreichbar', 0 für 'fern'
    :raises Exception: Wenn der Wert ungültig ist
    """
    if isinstance(range_str, str):
        if "nah" in range_str:
            return 2
        elif "erreichbar" in range_str:
            return 1
        elif "fern" in range_str:
            return 0
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet 'nah', 'erreichbar' oder 'fern'.")


# S-Bahn
def get_bahn(range_str: str) -> int:
    """
    Wandelt die Nähe zur S-Bahn in numerische Werte um.

    :param range_str: Textuelle Beschreibung der Erreichbarkeit ('nah', 'erreichbar', 'mit Bus', 'fern', 'nein')
    :return: 4 für 'nah', 3 für 'erreichbar', 2 für 'mit Bus', 1 für 'fern', 0 für 'nein'
    :raises Exception: Wenn der Wert ungültig ist
    """
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
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet 'nah', 'erreichbar', 'mit Bus', 'fern' oder 'nein'.")

# miete
def get_miete(value: str) -> int:
    """
    Berechnet den Durchschnitt einer Miete basierend auf einem Wertebereich.

    :param value: Textuelle Beschreibung der Miete (z.B. '500-700')
    :return: Durchschnittswert als ganze Zahl
    :raises Exception: Wenn der Wert ungültig ist
    """
    if '-' in value:
        try:
            start, end = value.split('-')
            return int(round((int(start) + int(end)) / 2))
        except ValueError:
            raise Exception(f"Ungültiger Wertebereich: {value}. Erwartet z.B. '500-700'.")
    else:
        try:
            return int(value)
        except ValueError:
            raise Exception(f"Ungültiger Wert: {value}. Erwartet eine ganze Zahl oder einen Wertebereich wie '500-700'.")


# Funktion zum Berechnen des Durchschnitts aus einem Wertebereich
def get_nebenkosten(range_str: str) -> int:
    """
    Berechnet den Durchschnitt der Nebenkosten aus einem Wertebereich.

    :param range_str: Textuelle Beschreibung der Nebenkosten (z.B. '50-100')
    :return: Durchschnittswert als ganze Zahl
    :raises Exception: Wenn der Wert ungültig ist
    """
    if isinstance(range_str, str):
        if "ueber" in range_str:
            return 300
        elif "unter" in range_str:
            return 50
        else:
            try:
                start, end = map(int, range_str.split('-'))
                return int(round((start + end) / 2))
            except ValueError:
                raise Exception(f"Ungültiger Wertebereich: {range_str}. Erwartet z.B. '50-100' oder 'ueber 300'.")
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet eine gültige Beschreibung der Nebenkosten.")


# Alter
def get_alter(range_str: str) -> int:
    """
    Wandelt das Alter einer Immobilie in numerische Werte um.

    :param range_str: Textuelle Beschreibung des Alters ('ueber 100 Jahre', 'Neubau', '50-60 Jahre')
    :return: Durchschnittsalter als ganze Zahl
    :raises Exception: Wenn der Wert ungültig ist
    """
    if isinstance(range_str, str):
        if "ueber" in range_str:
            return 100
        elif "Neubau" in range_str:
            return 0
        else:
            try:
                numbers = range_str.split('-')
                start, end = map(int, [numbers[0].strip(), numbers[1].replace("Jahre", "").strip()])
                return int(round((start + end) / 2))
            except ValueError:
                raise Exception(f"Ungültiger Wertebereich: {range_str}. Erwartet z.B. '50-60 Jahre' oder 'ueber 100 Jahre'.")
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet eine gültige Altersbeschreibung.")


# Lage
def get_lage(range_str: str) -> int:
    """
    Wandelt die Lagebeschreibung in numerische Werte um.

    :param range_str: Textuelle Beschreibung der Lage ('Hauptstrasse', 'Spielstrasse', 'Wohngebiet', 'Nebenstrasse', 'Abgelegen')
    :return: 4 für 'Hauptstrasse', 3 für 'Spielstrasse', 2 für 'Wohngebiet', 1 für 'Nebenstrasse', 0 für 'Abgelegen'
    :raises Exception: Wenn der Wert ungültig ist
    """
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
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet 'Hauptstrasse', 'Spielstrasse', 'Wohngebiet', 'Nebenstrasse' oder 'Abgelegen'.")


# Stadtmitte
def get_stadtmitte(range_str: str) -> int:
    """
    Wandelt die Entfernung zur Stadtmitte in numerische Werte um.

    :param range_str: Textuelle Beschreibung der Entfernung ('Zentrum', '<5 km', '>30 km', '10-20 km')
    :return: 0 für 'Zentrum', numerischer Durchschnitt für einen Wertebereich
    :raises Exception: Wenn der Wert ungültig ist
    """
    if isinstance(range_str, str):
        if "Zentrum" in range_str:
            return 0
        if "<" in range_str:
            return 3
        elif ">" in range_str:
            return 30
        else:
            try:
                numbers = range_str.split('-')
                start, end = list(map(int, [numbers[0].strip(), numbers[1].replace(" km", "").strip()]))
                return int(round((start + end) / 2))
            except ValueError:
                raise Exception(f"Ungültiger Wertebereich: {range_str}. Erwartet z.B. '10-20 km'.")
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet eine gültige Entfernung zur Stadtmitte.")


# Kaution
def get_kaution(range_str: str) -> int:
    """
    Berechnet die Kaution basierend auf einem Wertebereich.

    :param range_str: Textuelle Beschreibung der Kaution ('ueber 3000', 'keine', '1000-2000')
    :return: 3000 für 'ueber 3000', 0 für 'keine', Durchschnitt für einen Wertebereich
    :raises Exception: Wenn der Wert ungültig ist
    """
    if isinstance(range_str, str):
        if "ueber" in range_str:  # "ueber 100 Jahre"
            return 3000
        elif "keine" in range_str:  # Neubau als 0 interpretieren
            return 0
        else:
            try:
                start, end = map(int, range_str.split('-'))
                return int(round((start + end) / 2))
            except ValueError:
                raise Exception(f"Ungültiger Wertebereich: {range_str}. Erwartet z.B. '1000-2000'.")
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet eine gültige Kautionsbeschreibung.")


# Kueche
def get_kueche(range_str: str) -> int:
    """
    Wandelt die Küchenbeschreibung in numerische Werte um.

    :param range_str: Textuelle Beschreibung der Küche ('keine', 'Kueche (alt)', 'Kueche (neu)')
    :return: 0 für 'keine', 1 für 'Kueche (alt)', 2 für 'Kueche (neu)'
    :raises Exception: Wenn der Wert ungültig ist
    """
    if isinstance(range_str, str):
        if "keine" in range_str:
            return 0
        elif "Kueche (alt)" in range_str:
            return 1
        elif "Kueche (neu)" in range_str:
            return 2
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet 'keine', 'Kueche (alt)' oder 'Kueche (neu)'.")


# Bad
def get_bad(range_str: str) -> int:
    """
    Wandelt die Badbeschreibung in numerische Werte um.

    :param range_str: Textuelle Beschreibung des Bads ('Badewanne', 'Dusche', 'Dusche + Wanne', 'Dusche auf Flur', 'Waschbecken')
    :return: 0 für 'Badewanne', 1 für 'Dusche', 2 für 'Dusche + Wanne', 3 für 'Dusche auf Flur', 4 für 'Waschbecken'
    :raises Exception: Wenn der Wert ungültig ist
    """
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
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet 'Badewanne', 'Dusche', 'Dusche + Wanne', 'Dusche auf Flur' oder 'Waschbecken'.")


# mobliert
def get_mobliert(range_str: str) -> int:
    """
    Wandelt die Möblierungsbeschreibung in numerische Werte um.

    :param range_str: Textuelle Beschreibung der Möblierung ('ja', 'teilmoebliert', 'nein')
    :return: 2 für 'ja', 1 für 'teilmoebliert', 0 für 'nein'
    :raises Exception: Wenn der Wert ungültig ist
    """
    if isinstance(range_str, str):
        if "ja" in range_str:
            return 2
        elif "teilmoebliert" in range_str:
            return 1
        elif "nein" in range_str:
            return 0
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet 'ja', 'teilmoebliert' oder 'nein'.")


def get_quadratmeter(range_str: str) -> int:
    """
    Berechnet die Quadratmeter basierend auf einem Wertebereich.

    :param range_str: Textuelle Beschreibung der Fläche ('ueber 120', 'bis 20', '50-80')
    :return: 120 für 'ueber 120', 20 für 'bis 20', Durchschnitt für einen Wertebereich
    :raises Exception: Wenn der Wert ungültig ist
    """
    if isinstance(range_str, str):
        if "ueber" in range_str:
            return 120
        elif "bis" in range_str:
            return 20
        else:
            try:
                start, end = map(int, range_str.split('-'))
                return int(round((start + end) / 2))
            except ValueError:
                raise Exception(f"Ungültiger Wertebereich: {range_str}. Erwartet z.B. '50-80'.")
    raise Exception(f"Ungültiger Wert: {range_str}. Erwartet eine gültige Quadratmeterbeschreibung.")
