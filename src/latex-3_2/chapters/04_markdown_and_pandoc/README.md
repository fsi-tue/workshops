# Markdown & `pandoc`

## Dateien

| Datei                                            | Beschreibung                                                    |
|--------------------------------------------------|-----------------------------------------------------------------|
| [README.md](README.md)                           | Diese Datei hier                                                |
| [info.md](info.md)                               | Beispiel Datei aus der Präsentation                             |
| [shownotes.md](shownotes.md)                     | Der gesamte Inhalt des Workshops in mensch- UND maschinenlesbar |
| [slides.md](slides.md)                           | Präsentations optimierte `shownotes.md`                         |
| [Makefile](Makefile)                             | Sammlung an `pandoc`-Befehlen, die für die Markdown Dateien     |
| [shownotes_settings.tex](shownotes_settings.tex) | Befehle/Einstellungen zum Aufhübschen der Shownotes             |
| [slides_settings.tex](slides_settings.tex)       | Befehle/Einstellungen zum Aufhübschen der Slideshow             |
| [pictures/](pictures/)                           | Bilddateien für `shownotes.md` und `slides.md`                  |

Hiermit sei darauf aufgefordert die jeweiligen Dateien im Texteditor der Wahl zu öffnen
und zu experimentieren!

## Makefile

Aufruf der verschiedenen Macros:

```sh
make <Befehl>
```

| Befehl        | Beschreibung                                                 |
|---------------|--------------------------------------------------------------|
| `info`        | Konvertiert `info.md` zur `info.html` für den Webgebrauch    |
| `default`     | Die Shownotes als PDF                                        |
| `shownotes`   | Die Shownotes aufgehübscht als PDF                           |
| `html`        | Die Shownotes als "Webversion"`*`                            |
| `epub`        | Die Shownotes als Ebook                                      |
| `beamer`      | Eine [LaTeX Beamer PDF Präsentation][beamer] von `slides.md` |
| `fancybeamer` | Aufgehübschte Version von `beamer`                           |
| `slidy`       | Slideshow mittels [Slidy][slidy] für den Browser`*`          |
| `revealjs`    | Slideshow mittels [reveal.js][revealjs] für den Browser`*`   |
| `clean`       | Löscht alle Dateien, die durch obige Befehle erstellt wurden |

`*`Diese Befehle binden zusätzlich noch [MathJax][mathjax] ein, damit der Tex code passt.


## Resources

- [Pandoc][pandoc]
  - [Demos][demos]
- [Github Flavored Markdown Specification][GFMspec]
- [CommonMark][CommonMark]
- [LaTeX Beamer][beamer]
- [Slidy][slidy]
- [reveal.js][revealjs] 
- [MathJax][mathjax] verwandelt LaTeX Formeln (vornehmlich Mathematische) in
  die schön lesbaren, die man aus Tex kennt.



[pandoc]: https://pandoc.org
[demos]: https://pandoc.org/demos.html
[GFMspec]: https://github.github.com/gfm/
[CommonMark]: http://commonmark.org/
[beamer]: https://de.overleaf.com/learn/latex/Beamer
[slidy]: https://www.w3.org/Talks/Tools/Slidy2/Overview.html
[revealjs]: https://revealjs.com
[mathjax]: https://www.mathjax.org
