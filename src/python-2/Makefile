lam:
	lookatme --live slides.md
.PHONY:lam

html:
	pandoc -f markdown -t slidy -i -s --self-contained -o slides.html slides.md
.PHONY:html

pdf:
	pandoc -f markdown -t beamer --pdf-engine=xelatex -o slides.pdf slides.md
.PHONY:pdf
