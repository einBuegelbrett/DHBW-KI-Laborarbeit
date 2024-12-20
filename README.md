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

Zusätlich wurde eine pyton package `data_cleaning` erstellt, die die Datenbereinigungsfunktionen enthält. Es wurde diese erstellt, denn die Datenbereinigungsfunktionen werden in den verschiedenen Notebooks mehrmals verwendet. Die Funktionen sind in der Datei `data_cleaning/data_cleaning.py` zu finden.