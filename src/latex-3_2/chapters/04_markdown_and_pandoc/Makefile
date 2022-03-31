## Info.md ##
info:
	pandoc -f markdown -t html -o info.html info.md
.PHONY:info

## Shownotes ##

# Plain conversion of shownotes
default:
	pandoc -f markdown -t pdf \
  	--pdf-engine=xelatex \
  	-i shownotes.md  \
  	-o default.pdf
.PHONY:default

# fancy shownotes
shownotes:
	pandoc -f markdown -t pdf \
  	--pdf-engine=xelatex \
  	--pdf-engine-opt="-shell-escape" \
		--highlight-style tango \
  	-H shownotes_settings.tex \
  	-i shownotes.md  \
  	-o shownotes.pdf
	rm -rf _minted-input
.PHONY:shownotes

# Web version
html:
	pandoc -f markdown -t html \
		-s --mathjax --toc \
		-o shownotes.html \
		shownotes.md
.PHONY:html

# Ebook version
epub:
	pandoc -f markdown -t epub \
		--toc \
		-o shownotes.epub \
		shownotes.md
.PHONY:epub

## Presentations ##

# LaTex Beamer PDF version
beamer:
	pandoc -f markdown -t beamer       \
		--pdf-engine=xelatex             \
		-o slides.pdf slides.md
.PHONY:beamer

fancybeamer:
	pandoc -f markdown -t beamer       \
		--pdf-engine=xelatex             \
  	--pdf-engine-opt="-shell-escape" \
  	-H slides_settings.tex           \
		-o slides.pdf slides.md
	rm -rf _minted-input
.PHONY:fancybeamer

# Web versions
slidy:
	pandoc -f markdown -t slidy \
		-s --mathjax \
		-o slidy.html slides.md
.PHONY:slidy

revealjs:
	pandoc -f markdown -t revealjs \
		-s --mathjax                 \
		-o revealjs.html slides.md
.PHONY:revealjs

## Cleanup
clean:
	rm -f info.html
	rm -f default.pdf
	rm -f shownotes.epub
	rm -f shownotes.html
	rm -f shownotes.pdf
	rm -f slides_beamer.pdf
	rm -f slides_revealjs.html
	rm -f slides_slidy.html
.PHONY:clean
