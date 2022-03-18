# Commands und Environments

| Startdatei | Enddatei       |
|------------|----------------|
| `main.tex` | `solution.tex` |


Die Startdatei ist die [typische Tübinger Informatik Vorlage][Vorlage].


## Resourcen

- [Mathematical Cheat Sheet][heinkenCheat]
- Overleaf Dokumnenationen: [Command][Command], [Environment][Environment]


# Aufgaben

## Aufgabe 1: Zahlenräume

Es gibt den Befehl `\mathbb{}` für den Mathe-Modus.
`\mathbb{R}` $\Rightarrow \mathbb{R}$

Schreibe
$$ \mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C} $$

mittels Custom Commands nach dem Muster
`\bbR` $\Rightarrow \mathbb{R}$ oder `\bb{R}` $\Rightarrow \mathbb{R}$


## Aufgabe 2: Aufgaben-Section mit Punkten

Ziemlich was der Titel sagt. Entwerfe einen Befehl `\aufgabe`, der zwei Argumenten
erwartet:

- Nummer der Aufgabe
- Punkte für die Aufgabe

Hilfreiche Befehle sind `\section*` und `\hfill`.
Optional sind `\small` und `\textcolor{color}{text}`.

![So solls aussehen](../../pictures/aufgabe_2.png)


## Aufgabe 3: Lösungs-Umgebung

Entwerfe eine Umgebung `löesung`, die den Text "**Lösung**:" als Präfix besitzt.
Der Präfix ist der einzige und optionale Parameter.

Hilfreiche Befehle:

- `\medskip` vertikale Lücke
- `\noindent` keine Einrückung
- `\textbf{}` Fett geschrieben





[Command]: https://www.overleaf.com/learn/latex/Commands
[Environment]: https://www.overleaf.com/learn/latex/Environments
[heinkenCheat]: https://www.caam.rice.edu/~heinken/latex/symbols.pdf
[Vorlage]: https://www.overleaf.com/latex/templates/template-for-theoretische-informatik-uni-tubingen/xwsycshfkjtf
