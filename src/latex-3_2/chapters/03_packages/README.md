# Packages

## Dateien

| Datei                                | Beschreibung                                   |
|--------------------------------------|------------------------------------------------|
| [README.md](README.md)               | Diese Datei hier                               |
| [main.tex](main.tex)                 | **START** Mit dieser Datei beginnt das Kapitel |
| [main_input.tex](main_input.tex)     | Vorstufe zum Package mittels `settings.tex`    |
| [settings.tex](settings.tex)         | Auslagerungsdatei der Präambel                 |
| [main_package.tex](main_package.tex) | `main.tex` und ein Package                     |
| [uebungsblatt.sty](uebungsblatt.sty) | Das Package zu `main_package.tex`              |
| [main_class.tex](main_class.tex)     | `main.tex` und die Klasse `uebungsblatt`       |
| [uebungsblatt.cls](uebungsblatt.cls) | Verwendung mit `\documentclass{uebungsblatt}`  |

## Usage

Zum rendern der `.tex`-Dateien folgenden Befehl verwenden:

```
pdflatex --shell-escape -synctex=1 -interaction=nonstopmode "main".tex
```

## Resources

- Overleaf Dokumentation: [Package v Class][Package v Class], [Package][Package], [Class][Class]


# Aufgaben

## Aufgabe 6: Alle Befehle sind schon da 🎵

Sind sie das? Funktionieren alle Befehle und Umgebungen in `uebungsblatt.sty`
ohne Probleme in einer anderen Datei?

Kommentiere `\EXERCISES` in `main.tex` aus.

Sorge dafür, dass das keinen Fehler wirft. Selbiges für die anderen Übungsblatt
spezifischen Befehle.


## Zusatzaufgabe 7: `\documentclass{uebungsblatt}`

Neben Packages gibt es noch Klassen. Benutzt und benötigt in jedem Dokument:

```latex
\documentclass[a4paper]{scratcl}
```

Schreibe `uebungsblatt.sty` zu `uebungsblatt.cls` um. Richte dich nach der
[Overleaf Dokumentation][Class].
Der [Artikel zum Unterschied von Package und Class][Package v Class]
ist auch empfohlen.





[Package]: https://www.overleaf.com/learn/latex/Writing_your_own_package
[Class]: https://www.overleaf.com/learn/latex/Writing_your_own_class
[Package v Class]: https://www.overleaf.com/learn/latex/Understanding_packages_and_class_files


