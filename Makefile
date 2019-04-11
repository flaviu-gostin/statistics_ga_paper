.PHONY: all analysis

all:
	make analysis

analysis:
	cd src && python overpot_calc.py
	cd src && python scatter_plots.py 
	cd src && python statistics.py > ../results/statistics.txt
