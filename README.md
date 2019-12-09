# Statistical calculations for an article

Article: Wei, Q. et al, The Influence of Partial Replacement of Cu
with Ga on the Corrosion Behavior of
Ti<sub>40</sub>Zr<sub>10</sub>Cu<sub>36</sub>Pd<sub>14</sub> Metallic
Glasses, Journal of the Electrochemical Society, 2019, vol. 166,
pp. C485-C491. DOI:
[10.1149/2.0461914jes](http://dx.doi.org/10.1149/2.0461914jes)

This very small project calculates statistics on a small dataset
containing two independent and three dependent variables.  Analyses:
two-way ANOVA, one-way ANOVA, t-tests.

## To repeat the calculation:

I only tested this project under GNU/Linux with Python3.5.2
It will most probably not work with Python2

- open a terminal
- `cd Desktop` or choose another directory where you want this project
- `git clone https://github.com/cracrai/statistics_ga_paper.git`.  This will
create a new directory named *statistics_ga_paper/*
- `cd statistics_ga_paper`
- `virtualenv --python=python3 venv` to create a virtual environment
- `source venv/bin/activate` to activate the virtual environment
- `pip install -r requirements.txt` to install required libraries
- `make analysis` to perform the calculations and generate scatter plots for
exploratory data analysis.

If you encounter any problems, please create an "issue".  See the tab "Issues" above.
