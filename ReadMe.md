# Description #

This repository contains (hopefully at least partially correct) solutions to
the exercises of the course
[“Algorithmics”](https://www.ads.tuwien.ac.at/teaching/LVA/186814.html), held
at the Vienna University of Technology in the winter semester of 2012.

# Dependencies #

* [Xelatex](http://www.tug.org/texlive/)
* Various Fonts

If you do not own some of the fonts mentioned in the document, just replace the
font names — they are located under the comment "% -- Fonts --" — with the name
of fonts that are already installed on your system.

# Translation #

	# Convert pseudocode examples to LaTeX
	cd Utilities; ./convert_code_to_tex.sh; cd ..
	# Generate pdf
	xelatex *.tex; biber *.tex; xelatex *.tex
