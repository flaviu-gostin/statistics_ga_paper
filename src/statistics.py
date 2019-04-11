""" This script performs various statistical tests """

import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

# Useful tool for slicing MultiIndex data frames
idx = pd.IndexSlice


data = pd.read_csv("../results/corrpitover.csv", sep='\t')

print("\nQuestion: Do the Ga content and/or the sample shape have a significant effect on Ecorr, Epit or npit (pitting overpotential)?  Null hypothesis: the means of Ecorr (Epit, npit) for each Ga content and sample shape are the same.")


print("\n(1) Performing two-way ANOVA.  Factors: Ga content, sample shape.  Results:")
data1 = data.copy()
data1.replace("Ribbon", 1)
data1.replace("Rod", 2)
data2 = data1[data1.Ga_at != 1]

print("(1a) model for Ecorr: Ecorr_mVvsSCE ~ C(Ga_at)*C(sample_shape)")
model = ols('Ecorr_mVvsSCE ~ C(Ga_at)*C(sample_shape)', data2).fit()
print("Overall model F({: .0f},{: .0f}) = {:.1f}, p = {:.1E}".format(model.df_model, model.df_resid, model.fvalue, model.f_pvalue))
print(model.summary())
res = sm.stats.anova_lm(model, typ=2)
print(res)

print("\n(1b) model for Epit: Epit_mVvsSCE ~ C(Ga_at)*C(sample_shape)")
model = ols('Epit_mVvsSCE ~ C(Ga_at)*C(sample_shape)', data2).fit()
print("Overall model F({: .0f},{: .0f}) = {:.1f}, p = {:.1E}".format(model.df_model, model.df_resid, model.fvalue, model.f_pvalue))
print(model.summary())
res = sm.stats.anova_lm(model, typ=2)
print(res)

print("\n(1c) model for npit: npit_mV ~ C(Ga_at)*C(sample_shape)")
model = ols('npit_mV ~ C(Ga_at)*C(sample_shape)', data2).fit()
print("Overall model F({: .0f},{: .0f}) = {:.1f}, p = {:.1E}".format(model.df_model, model.df_resid, model.fvalue, model.f_pvalue))
print(model.summary())
res = sm.stats.anova_lm(model, typ=2)
print(res)


print("\n\n(2) Performing one-way ANOVA.  Factor: Ga content.  Results:")
# Create multiindex, essentially two sets of labels
data.set_index(["Ga_at", "sample_shape"], inplace=True)
data.sort_index(level=data.index.names, inplace=True)
# Perform ANOVA to check effect of Ga for rods
print("Shape\tQuantity\tstatistic\tp-value")
shape = "Rod"
for col in list(data.columns):
    e = col.split('_', maxsplit=1)[0]
    anova_ga = stats.f_oneway(data.loc[(0, "Rod"), col],
                              data.loc[(1, "Rod"), col],
                              data.loc[(2, "Rod"), col],
                              data.loc[(4, "Rod"), col],
                              data.loc[(8, "Rod"), col],
                              data.loc[(10, "Rod"), col])
    print("{}\t{}\t{: .1f}\t{: .3f}".format(shape, e, anova_ga[0], anova_ga[1]))
    shape = " "

# ... and now for ribbons
shape = "Ribbon"
for col in list(data.columns):
    e = col.split('_')[0]
    anova_ga = stats.f_oneway(data.loc[(0, "Ribbon"), col],
                              data.loc[(2, "Ribbon"), col],
                              data.loc[(4, "Ribbon"), col],
                              data.loc[(8, "Ribbon"), col],
                              data.loc[(10, "Ribbon"), col])
    print("{}\t{}\t{: .1f}\t{: .3f}".format(shape, e, anova_ga[0], anova_ga[1]))
    shape = " "
    
print("\n\n(3) Performing two-sample t-tests for rod versus ribbon for all Ga contents grouped together and for each Ga content individually.  Results:")
print("Quantity\tGa (at%)\tstatistic\tp-value")
for e in list(data.columns):
    e_split = e.split('_')[0]
    all_ribb = data.loc[idx[:, "Ribbon"], e]
    all_rod = data.loc[idx[:, "Rod"], e]
    sta = stats.ttest_ind(all_rod, all_ribb)
    print("{}\tall\t{:.1f}\t{:.1E}".format(e_split, sta[0], sta[1]))
    for ga in [0, 2, 4, 8, 10]:
        ribb = data.loc[(ga, "Ribbon"), e]
        rod = data.loc[(ga, "Rod"), e]
        st = stats.ttest_ind(rod, ribb)
        s = list(st)
        print(" \t{}\t{:.1f}\t{:.3f}".format(ga, s[0], s[1]))
