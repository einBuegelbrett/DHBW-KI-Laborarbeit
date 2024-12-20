# Laborarbeit Künstliche Intelligenz

## Gruppe
- Aziz Carducci (1965015)
- Sven Sendke (8469950)

## Aufgabenstellung
Die Aufgabe besteht darin, ein Bayes'sches Netz und eine Evidenztheorie für die Bewertung von Wohnungen zu erstellen und diese dann zu vergleichen.
- Aufgabenstellung: **PE_2** (Bayes'sches Netze und Evidenztheorie)
- Datensätze: **PE_2_1** (Wohnungen_1.csv, Wohnungen_2.csv)

## Vorgehensweise
In den Jupyter Notebooks werden die Schritte und Ergebnisse dokumentiert. Die Notebooks sind unter den Ornern `notebook/wohnungen_1` und `notebook/wohnungen_2` zu finden. Diese sind folgendermaßen aufgeteilt:
- bayessches_netze_wohnungen_{1 oder 2}.ipynb: Stellt Aufgabenteil 1 dar, in dem ein KI Modell auf Basis eines Bayes-Netz erstellt wird.
- evidenztheorie_wohnungen_{1 oder 2}.ipynb: Stellt Aufgabenteil 2 dar, in dem ein KI Modell auf Basis der Evidenztheorie erstellt wird.
- vergleich_ki_wohnungen_{1 oder 2}.ipynb: Stellt Aufgabenteil 3 dar, in dem die beiden KI Modelle verglichen werden.

Zusätzlich wurde ein Python-Paket `data_cleaning` erstellt, das die Datenbereinigungsfunktionen enthält. Dieses wurde erstellt, da die Datenbereinigungsfunktionen in den verschiedenen Notebooks mehrfach verwendet werden. Die Funktionen befinden sich in der Datei `data_cleaning/text_to_numeric.py`.
Es wurde auch ein Python-Paket `combined_mass` erstellt, das die Funktionen für die kombinierte Grundmasse enthält. Die Funktionen sind in der Datei `combined_mass/combined_mass.py` zu finden.