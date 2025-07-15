import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# CSV einlesen
df = pd.read_csv("carbon_profile_example.csv")
df["Depth_cm"] = pd.to_numeric(df["Depth_cm"])
df["Rimmerzmatte"] = pd.to_numeric(df["Rimmerzmatte"])
df["Backfilled"] = pd.to_numeric(df["Backfilled"])

# Plot 1: Linien mit Markern
plt.figure(figsize=(6, 8))
plt.plot(df["Rimmerzmatte"], df["Depth_cm"], label="Rimmerzmatte", color="darkgreen", marker='o')
plt.plot(df["Backfilled"], df["Depth_cm"], label="Backfilled", color="limegreen", linestyle='--', marker='s')
plt.gca().invert_yaxis()
plt.xlabel("% Carbon")
plt.ylabel("Depth (cm)")
plt.title("Plot 1: Linien mit Markern")
plt.grid(True, linestyle=':', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: Scatterplot
plt.figure(figsize=(6, 8))
plt.scatter(df["Rimmerzmatte"], df["Depth_cm"], label="Rimmerzmatte", color="darkgreen", marker='o')
plt.scatter(df["Backfilled"], df["Depth_cm"], label="Backfilled", color="limegreen", marker='s')
plt.gca().invert_yaxis()
plt.xlabel("% Carbon")
plt.ylabel("Depth (cm)")
plt.title("Plot 2: Scatterplot")
plt.grid(True, linestyle=':', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 3: Horizontaler Balkenplot
bar_width = 4
y = df["Depth_cm"]
plt.figure(figsize=(8, 6))
plt.barh(y - bar_width/2, df["Rimmerzmatte"], height=bar_width, label="Rimmerzmatte", color="darkgreen")
plt.barh(y + bar_width/2, df["Backfilled"], height=bar_width, label="Backfilled", color="limegreen")
plt.gca().invert_yaxis()
plt.xlabel("% Carbon")
plt.ylabel("Depth (cm)")
plt.title("Plot 3: Horizontale Balken")
plt.grid(True, linestyle=':', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 4: Gefüllte Flächen
x0_rimmer = np.zeros_like(df["Rimmerzmatte"].values)
x0_back = np.zeros_like(df["Backfilled"].values)
plt.figure(figsize=(6, 8))
plt.fill_betweenx(df["Depth_cm"].values, x0_rimmer, df["Rimmerzmatte"].values, color="darkgreen", alpha=0.3, label="Rimmerzmatte")
plt.fill_betweenx(df["Depth_cm"].values, x0_back, df["Backfilled"].values, color="limegreen", alpha=0.3, label="Backfilled")
plt.plot(df["Rimmerzmatte"], df["Depth_cm"], color="darkgreen", linewidth=2)
plt.plot(df["Backfilled"], df["Depth_cm"], color="limegreen", linewidth=2, linestyle='--')
plt.gca().invert_yaxis()
plt.xlabel("% Carbon")
plt.ylabel("Depth (cm)")
plt.title("Plot 4: Gefüllte Flächen")
plt.grid(True, linestyle=':', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
