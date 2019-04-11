""" Plot Ecorr, Epit and npit (overpotential) vs Ga content """

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
from pandas import plotting


df = pd.read_csv("../results/corrpitover.csv", sep="\t")

# Assign colours to data points. e.g. blue points for rods
colours = ["blue" if i == "Rod" else ("red" if i == "Ribbon" else "black") for i in df["sample_shape"]]

plotting.scatter_matrix(df[["Ga_at", "sample_shape", "Ecorr_mVvsSCE", "Epit_mVvsSCE", "npit_mV"]], c=colours, s=100)

# Create legend
blue_patch = mpatches.Patch(color="blue", label="rod")
red_patch = mpatches.Patch(color="red", label="ribbon")
black_patch = mpatches.Patch(color="black", label="??")
h = [blue_patch, red_patch]
if "black" in colours:
    h.append(black_patch)
plt.legend(handles=h)

plt.savefig("../results/scatter_matrix.png", dpi=500)
