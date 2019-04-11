# Perform Tukey HSD test on the effect of Ga on Ecorr for rods
sel = data.loc[([0, 1, 2, 4, 8, 10], r), ecorr_col]
mc = MultiComparison(sel, sel.index.get_level_values("Ga (at%)"))
mc_results = mc.tukeyhsd()
print("Tukey HSD on effect of Ga on Ecorr for rods\n", mc_results, "\n")


# Perform simple 2-sample t-test between rod 2Ga and 10Ga
ga_2vs10 = stats.ttest_ind(data.loc[(2, r), ecorr_col], data.loc[(10, r), ecorr_col])
print("2-samp t-test on rod 2Ga vs 10Ga\n", ga_2vs10, "\n")
