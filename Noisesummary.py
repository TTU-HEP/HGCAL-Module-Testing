import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = '/home/daq3/hgcal/python/Summary of module production - TTU.csv'  
df = pd.read_csv(file_path)


print(df.columns)

module_id_col = 'module ID' 
noisy_channels_col = 'Unnamed: 15'  
dead_channels_col = 'Unnamed: 13' 
df = df.dropna(subset=[module_id_col, noisy_channels_col,dead_channels_col])

df[module_id_col] = df[module_id_col].astype(str)

plt.figure(figsize=(12, 6))
module_ids = []
noisy_channel_counts = []
dead_channel_counts = []


for module_id in df[module_id_col].unique():
    module_data = df[df[module_id_col] == module_id]
 
    noisy_channel_count = pd.to_numeric(module_data[noisy_channels_col], errors='coerce').sum()
    dead_channel_count = pd.to_numeric(module_data[dead_channels_col], errors='coerce').sum()
    noisy_channel_counts.append(noisy_channel_count)
    dead_channel_counts.append(dead_channel_count)
    module_ids.append(module_id)

totbad_channel_counts = [x + y for x, y in zip(noisy_channel_counts, dead_channel_counts)]
plt.bar(module_ids, totbad_channel_counts, color='yellow', edgecolor='black', label='Total Bad Channels')
plt.bar(module_ids, noisy_channel_counts, color='red', edgecolor='black', label='Noisy Channels')
plt.bar(module_ids, dead_channel_counts, color='purple', edgecolor='black', label='Dead Channels')
plt.xlabel('Module ID')
plt.ylabel('Number of Noisy Channels')
plt.title('Number of Noisy Channels per Module')
plt.xticks(rotation=90, fontsize=8)
plt.legend()

output_pdf = "NoisyChannels_summary.jpg"
plt.savefig(output_pdf, format="jpg", bbox_inches="tight")