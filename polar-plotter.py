import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the file
file = input("Please insert the name of the file in format './FILE-NAME.csv': ")
data = pd.read_csv(file)

# izoforoms of G-protein - labels on polar plot
izoforms = []
for col in data.columns[1:]:
    izoforms.append(col)
izoforms = [*izoforms, izoforms[0]] # first value has to be on the end to close the plot


# how many ligands?
lig_count = len(data) + 1


# name of ligands
lig_name = []
for row in data["Ligand"]:
    lig_name.append(row)

# transfering values to list
value = data.values.tolist()

# in case of different number of ligands add or delete variable lig*
lig1 = value[0][1:int(lig_count)]
lig2 = value[1][1:int(lig_count)]
lig3 = value[2][1:int(lig_count)]
lig4 = value[3][1:int(lig_count)]
lig5 = value[4][1:int(lig_count)]


lig1 = [*lig1, lig1[0]]
lig2 = [*lig2, lig2[0]]
lig3 = [*lig3, lig3[0]]
lig4 = [*lig4, lig4[0]]
lig5 = [*lig5, lig5[0]]



label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(lig2))

plt.figure(figsize=(8, 8))
ax = plt.subplot(polar=True)

# in case of different number of ligands add or delete plt.plot with specific lig* var
plt.plot(label_loc, lig1, '-o', label=lig_name[0], linewidth=4)
plt.plot(label_loc, lig2, '-o', label=lig_name[1], linewidth=4)
plt.plot(label_loc, lig3, '-o', label=lig_name[2], linewidth=4)
plt.plot(label_loc, lig4, '-o', label=lig_name[3], linewidth=4)
plt.plot(label_loc, lig5, '-o', label=lig_name[4], linewidth=4)


plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
lines = plt.thetagrids(np.degrees(label_loc), labels=izoforms)
plt.legend(fontsize='25', loc='best', bbox_to_anchor=(0.9, 1.05, 0.5, 0.1))

# in case you need to specify ticks of lines use following line:
# ax.set_rticks([50, 100, 150, 200])

plt.show()