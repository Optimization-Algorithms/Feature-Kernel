.SUFFIXES: .tex .py

feature_kernel.pdf: *.tex algorithms/*tex *py 
	@echo "Compile Latex document"
	@pdflatex  -synctex=1 -interaction=batchmode --shell-escape feature_kernel.tex
	@pdflatex  -synctex=1 -interaction=batchmode --shell-escape feature_kernel.tex

%.py : 
	python $*


