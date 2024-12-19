from pyds import MassFunction

def calculate_basismaße_multivalue(data, column_name, values, omega) -> dict:
    """
    Berechnet die Basismaße für ein mehrwertiges Attribut (z. B. 'Lage').

    :param data: DataFrame mit den Daten
    :param column_name: Name der Spalte (z. B. 'Lage')
    :param omega: Liste der Kategorien (Bewohnerkategorien)
    :param values: Liste der möglichen Werte des Attributs (z. B. [0, 1, 2, 3, 4] für 'Lage')
    :return: Dictionary {Wert: MassFunction}
    """
    mass_functions = {}

    for value in values:
        basismaße = {}
        for kategorie in omega:
            total = len(data)
            count_hypothesis = len(data[(data[column_name] == value) & (data['Bewohnerkategorie'] == kategorie)])
            basismaße[frozenset([kategorie])] = count_hypothesis / total

        # Unsicherheit hinzufügen
        basismaße[frozenset()] = 1 - sum(basismaße.values())

        # Erstelle die MassFunction für diesen Wert
        mass_functions[value] = MassFunction(basismaße)

    return mass_functions



def calculate_combined_mass(data, attributes_values, omega):
    """
    Berechnet die kombinierte Evidenz für eine gegebene Kombination von Attributen.

    :param data: DataFrame mit den Daten
    :param attributes_values: Dictionary {Attribut: Wert}, z. B. {'Garage': 1, 'Lage': 2}
    :param omega: Liste der Hypothesen (Bewohnerkategorien)
    :return: Kombinierte MassFunction
    """
    combined_mass = None  # Initialisiere die kombinierte Evidenz

    for attribute, value in attributes_values.items():
        # Berechne die Basismaße für das aktuelle Attribut und den aktuellen Wert
        basis_mass_dict = calculate_basismaße_multivalue(data, attribute, [value], omega)

        if value in basis_mass_dict:
            basis_mass = basis_mass_dict[value]
        else:
            continue

        print(f"Basismaße für {attribute}={value}:", basis_mass)

        # Kombiniere die Evidenz mit der bisherigen kombinierten Evidenz
        if combined_mass is None:
            combined_mass = basis_mass  # Erste MassFunction
        else:
            combined_mass = combined_mass & basis_mass  # Dempster's Regel

    return combined_mass
