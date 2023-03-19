import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.font_manager as font_manager

fig = plt.figure(figsize=(7, 7))


# # Create confusion matrix with custom values
# labels = ['NoResponse', 'Response']
data = np.array([[0.88, 0.12], [0.37, 0.63]])

# Create the heatmap
fig, ax = plt.subplots(figsize=(12, 12))
# plt.tight_layout()
font_path = './times.ttf' # Change this to the path of your Times New Roman font file
font_prop = font_manager.FontProperties(fname=font_path, size=25)
sns.set(font=font_prop.get_name(), font_scale=3.5)

sns.heatmap(data, annot=True, cmap='Blues', cbar=False, ax=ax,
            xticklabels=['Response', 'NoResponse'],
            yticklabels=['Response', 'NoResponse'],
            annot_kws={'fontsize': 71}, fmt='.2f', vmin=0, vmax = 1)




label_font = {'family': 'Times New Roman',
        'size': 51}


ax.tick_params(axis='both', which='major', labelsize=25)  # Adjust to fit
ax.xaxis.set_ticklabels(['NoResponse', 'Response'], fontdict=label_font);
ax.yaxis.set_ticklabels(['NoResponse', 'Response'], fontdict=label_font);


label_font = {'family': 'Times New Roman',
        'size': 55}

# Add labels and title
ax.set_xlabel('True Label', fontdict=label_font);
ax.set_ylabel('Predicted Label', fontdict=label_font);


# Show the plot
# plt.show()

name = 'T1-T2-T3-C_new'
plt.savefig(f'./{name}.png')