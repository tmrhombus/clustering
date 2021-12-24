import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns 

# Before clustering
df = pd.read_csv("twoblobs.csv", header=None)
df.columns = ["Some Random X", "Some Random Y"]
sns.scatterplot(x=df["Some Random X"], 
                y=df["Some Random Y"])
plt.title("Scatterplot of X and Y")

# After clustering
plt.figure()
df = pd.read_csv("output.csv")
sns.scatterplot(x=df.x, y=df.y, 
                hue=df.c, 
                palette=sns.color_palette("hls", n_colors=2))
plt.xlabel("Some Random X")
plt.ylabel("Some Random Y")
plt.title("Clustered: X vs Y")

plt.show()
