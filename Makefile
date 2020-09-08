.SUFFIXES : .tex .py


feature_kernel.pdf: *.tex algorithms/*tex images/*.eps
	@echo "Compile Latex document"
	@latexmk -pdf feature_kernel.tex
	


images/%.eps : %.py
	@echo "Run python scripts"
	@python $<


