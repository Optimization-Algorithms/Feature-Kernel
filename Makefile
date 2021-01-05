.SUFFIXES : .tex .py .csv .png


feasibility-convergence-csv = $(wildcard  test-results/*.csv)
feasibility-convergence-png = $(subst .csv,.png,$(feasibility-convergence-csv))

feasibility-convergence-tex = $(subst .csv,.tex,$(feasibility-convergence-csv))


feature_kernel.pdf: *.tex algorithms/*tex images/*.eps $(feasibility-convergence-png) $(feasibility-convergence-tex)
	@echo "Compile Latex document"
	@latexmk -pdf feature_kernel.tex
	


images/%.eps : %.py
	@echo "Run python scripts"
	@python $<

.csv.png: 
	@echo "Convert Ratio files to Graph"
	@urp --radius 3  --input $? --output $@


.csv.tex:
	@echo "Make Stats table"
	@python usage-ratio-parse.py $? > $@