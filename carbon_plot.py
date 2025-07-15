import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------- CSV einlesen ----------
df = pd.read_csv("carbon_profile_example.csv")
df["Depth_cm"] = pd.to_numeric(df["Depth_cm"])
df["Rimmerzmatte"] = pd.to_numeric(df["Rimmerzmatte"])
df["Backfilled"] = pd.to_numeric(df["Backfilled"])

# ---------- Output-Verzeichnis ----------
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# ---------- Plot 1: Linien mit Markern, kein Gitter, kein Display ----------
plt.figure(figsize=(6, 8))
plt.plot(df["Rimmerzmatte"], df["Depth_cm"], label="Rimmerzmatte", color="darkgreen", marker='o')
plt.plot(df["Backfilled"], df["Depth_cm"], label="Backfilled", color="limegreen", linestyle='--', marker='s')
plt.gca().invert_yaxis()
plt.xlabel("% Carbon")
plt.ylabel("Depth (cm)")
plt.title("Plot 1: Linien mit Markern")
plt.grid(False)  # <- Kein Gitter
plt.legend()
plt.tight_layout()

# ---------- Speichern  ----------
plt.savefig(os.path.join(output_dir, "plot1_lines_markers_clean.png"), dpi=300)
plt.close()
