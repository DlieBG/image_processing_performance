# Image Processing Performance
Dieses Repository beinhaltet die praktische Arbeit zum Module Intelligente Robotik an der THI im Wintersemester 2024/25.\
Thema der Arbeit ist der Performance Vergleich von Bildverarbeitungsalgorithmen basierend auf verschiedenen Implementierungen, Architekturen und Bildsampeln.

## Installation
1. Klonen Sie das Repository.
2. Navigieren Sie in den `python` Ordner.
```bash
cd python
```
3. Installieren Sie die Abhängigkeiten.
```bash
pip install -e .
```

## Verwendung
Führen Sie die `ipp_python` CLI Anwendung aus.
```bash
ipp_python --help
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
Beispielsweise kann der übergeordnete Algorithmus eine utils Funktion aufrufen, welche dann auf der zweiten Ebene (Layer 1) loggt.

### Background Subtraction
Für die Background Subtraction fallen die folgenden Events an.\
Die Events auf Layer 1 kann je nach Implementierung variieren.
| Layer 0 | Layer 1 | Event |
|---|---|---|
| | 1 | finish open pil image |
| | 1 | finish convert pil image |
| | 1 | finish extract flat data |
| | 1 | finish create flat pixels |
| | 1 | finish reshape pixels |
| 0 | | finish open reference image |
| | 1 | finish open pil image |
| | 1 | finish convert pil image |
| | 1 | finish extract flat data |
| | 1 | finish create flat pixels |
| | 1 | finish reshape pixels |
| 0 | | finish open image |
| 0 | | finish hsv conversion |
| 0 | | finish background subtraction |
| | 1 | finish reshape flat pixels |
| | 1 | finish create flat data |
| | 1 | finish put data to pil image |
| | 1 | finish save pil image |
| 0 | | finish save image |

### Erode
Für die Erosion fallen die folgenden Events an.\
Die Events auf Layer 1 kann je nach Implementierung variieren.
| Layer 0 | Layer 1 | Event |
|---|---|---|
| | 1 | finish open pil image |
| | 1 | finish convert pil image |
| | 1 | finish extract flat data |
| | 1 | finish create flat pixels |
| | 1 | finish reshape pixels |
| 0 | | finish open image |
| 0 | | finish create output image |
| 0 | | finish erode |
| | 1 | finish reshape flat pixels |
| | 1 | finish create flat data |
| | 1 | finish put data to pil image |
| | 1 | finish save pil image |
| 0 | | finish save image |

### Dilate
Für die Dilation fallen die folgenden Events an.\
Die Events auf Layer 1 kann je nach Implementierung variieren.
| Layer 0 | Layer 1 | Event |
|---|---|---|
| | 1 | finish open pil image |
| | 1 | finish convert pil image |
| | 1 | finish extract flat data |
| | 1 | finish create flat pixels |
| | 1 | finish reshape pixels |
| 0 | | finish open image |
| 0 | | finish create output image |
| 0 | | finish dilate |
| | 1 | finish reshape flat pixels |
| | 1 | finish create flat data |
| | 1 | finish put data to pil image |
| | 1 | finish save pil image |
| 0 | | finish save image |
