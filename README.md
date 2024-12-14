# Image Processing Performance
Dieses Repository beinhaltet die praktische Arbeit zum Module Intelligente Robotik an der THI im Wintersemester 2024/25.\
Thema der Arbeit ist der Performance Vergleich von Bildverarbeitungsalgorithmen basierend auf verschiedenen Implementierungen, Architekturen und Bildsampeln.\
Hier befindet sich die Sammlung der Python basierten Implementierungen.\
Die folgenden Varianten wurden umgesetzt:
1. Intuitiver Ansatz mit Pydantic Objekten und ohne Optimierungen (`ipp_slow`)
2. Optimierter Ansatz mit schlankeren Datenstrukturen (`ipp_fast`)
3. Multithreading Implementierung mit Numpy (`ipp_numpy`)

## Installation
1. Klonen Sie das Repository.
2. Installieren Sie die Abhängigkeiten und die CLI.
```bash
pip install -e .
```

## Verwendung
Alle drei Varianten sind per CLI aufrufbar und dokumentiert.
### `ipp_slow`
```bash
ipp_slow --help
```

### `ipp_fast`
```bash
ipp_fast --help
```

### `ipp_numpy`
```bash
ipp_numpy --help
```

## Time Tracking
Um das Time Tracking zu realisieren, muss jeder Algorithmus seine erreichte Meilensteine mit Informationen und verstrichener Zeit auf der Konsole ausgeben.\
Geloggt werden Meilensteine direkt nachdem sie abgeschlossen wurden.\
Ein Konsolen Log sieht dabei wie folgt aus.
```
[timestamp] layer (module) message
```
Ein Besipiel mit echten Werten sieht so aus.
```
[0.107217425] 1 (open_project_image) finish open pil image
[0.169847847] 1 (open_project_image) finish convert pil image
[0.364496552] 1 (open_project_image) finish extract flat data
```
Dabei gibt der Layer an, in welcher Schicht das Event aufgetreten ist.\
Beispielsweise kann der übergeordnete Algorithmus eine utils Funktion aufrufen, welche dann auf der zweiten Ebene (Layer 1) loggt.\
Hier werden nur die Events auf Layer 0 dokumentiert, da diese zwischen den Algorithmen einheitlich sein müssen, um eine Vergleichbarkeit zu schaffen.

### Background Subtraction
Für die Background Subtraction fallen die folgenden Events an.\
Die Events auf Layer 1 kann je nach Implementierung variieren.
| Layer 0 | Event |
|---|---|
| 0 | finish preprocessing |
| 0 | finish background subtraction |
| 0 | finish postprocessing |

### Erode
Für die Erosion fallen die folgenden Events an.\
Die Events auf Layer 1 kann je nach Implementierung variieren.
| Layer 0 | Event |
|---|---|
| 0 | finish preprocessing |
| 0 | finish background subtraction |
| 0 | finish postprocessing |

### Dilate
Für die Dilation fallen die folgenden Events an.\
Die Events auf Layer 1 kann je nach Implementierung variieren.
| Layer 0 | Event |
|---|---|
| 0 | finish preprocessing |
| 0 | finish background subtraction |
| 0 | finish postprocessing |
