import pandas as pd
import matplotlib.pyplot as plt
import re

//percorso_file = metti il tuo percorso
with open(percorso_file, 'r') as f:
    content = f.read()

clean_content = re.sub(r'\[.*?\]', ' ', content)

values = re.findall(r"[-+]?\d*\.\d+|\d+", clean_content)
all_nums = [float(v) for v in values]

rows = []
for i in range(0, len(all_nums) - 6, 7):
    if all_nums[i] == 6.0:
        rows.append(all_nums[i+1 : i+7])

df = pd.DataFrame(rows, columns=['M1', 'AUC', 'M3', 'MCC', 'M5', 'Accuracy'])

df[['AUC', 'MCC', 'Accuracy']].plot(figsize=(10,5), grid=True)
plt.title("Evoluzione Fine-tuning DNABERT")
plt.show()