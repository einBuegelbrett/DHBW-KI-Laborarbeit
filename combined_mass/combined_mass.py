from pyds import MassFunction
from pandas import DataFrame

"""
Anmerkung: Basismasse wird eigentlich mit Eszet geschrieben, aber das ist kein ASCII-Zeichen. 
Um spätere Konvertierungsprobleme zu vermeiden, wird sie hier mit zwei 's' geschrieben.
"""

def calculate_basismasse(data: DataFrame, column_name: str, value: int, omega: list) -> MassFunction:
    """
    Berechnet die Basismasse für ein Attribut (z. B. 'Lage').

    :param data: DataFrame mit den Daten
    :param column_name: Name der Spalte (z. B. 'Lage')
    :param value: Möglicher Wert des Attributs (z. B. 0, 1, 2, 3 oder 4 für 'Lage')
    :param omega: Liste der Kategorien (Bewohnerkategorien)
    :return: Dictionary {Wert: MassFunction}
    """
    basismasse = {}
    total = len(data)

    # Überprüfe, ob Daten vorhanden sind
    if total == 0:
        raise ValueError("Der Datensatz ist leer. Keine Berechnung möglich.")

    for kategorie in omega:
        count_hypothesis = len(data[(data[column_name] == value) & (data['Bewohnerkategorie'] == kategorie)])
        basismasse[frozenset([kategorie])] = count_hypothesis / total

    # Unsicherheit hinzufügen
    basismasse[frozenset()] = 1 - sum(basismasse.values())

    # Validierung der Basismassen
    if any(mass < 0 for mass in basismasse.values()):
        raise ValueError(f"Negative Basismassen berechnet: {basismasse}")
    if sum(basismasse.values()) > 1.00001 or sum(basismasse.values()) < 0.99999:
        raise ValueError(f"Die Summe der Basismassen ist nicht gleich 1: {sum(basismasse.values())}")

    return MassFunction(basismasse)

def calculate_combined_mass(data: DataFrame, attributes_values: dict, omega: list) -> MassFunction:
    """
    Berechnet die kombinierte Evidenz für eine gegebene Kombination von Attributen indem die Basismasse Akkumuliert wird.

    :param data: DataFrame mit den Daten
    :param attributes_values: Dictionary {Attribut: Wert}, z. B. {'Garage': 1, 'Lage': 2}
    :param omega: Liste der Hypothesen (Bewohnerkategorien)
    :return: Kombinierte MassFunction
    """
    combined_mass = None  # Initialisiere die kombinierte Evidenz

    for attribute, value in attributes_values.items():
        # Berechne die Basismaße für das aktuelle Attribut und den aktuellen Wert
        basis_mass = calculate_basismasse(data, attribute, value, omega)
        print(f"Basismaße für {attribute}={value}: {basis_mass}")

        # Kombiniere die Evidenz mit der bisherigen kombinierten Evidenz
        if combined_mass is None:
            combined_mass = basis_mass  # Erste MassFunction
        else:
            try:
                # Kombiniere die Evidenzen
                combined_mass = combined_mass & basis_mass # Dempster-Shafer-Theorie
                print("Kombinierte Evidenz:", combined_mass)
            except ZeroDivisionError:
                # Konflikt erkannt: Setze die Masse auf Unsicherheit
                print("Konflikt erkannt: Keine gemeinsame Hypothese zwischen den Basismassen.")
                combined_mass = MassFunction({frozenset(): 1.0})

    return combined_mass
