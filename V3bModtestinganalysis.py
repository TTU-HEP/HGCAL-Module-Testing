import uproot
import matplotlib.pyplot as plt
import numpy as np
#import ROOT no ROOT :(

listofmodules_root= [
    'data/320-ML-F3W2-TT-0101/Completely_Bonded_2025-03-18/chambertest1/pedestal_run/run_20250318_173228_BV300_RH0_T20_trimmed300',
    'data/320-ML-F3W2-TT-0102/Completely_Encapsulated_2025-03-21/test1/pedestal_run/run_20250321_173316_BV300_RH0_T20_trimmed300',
    'data/320-ML-F3W2-TT-0103/Completely_Encapsulated_2025-03-21/test1/pedestal_run/run_20250321_174951_BV300_RH0_T20_trimmed300',
    'data/320-ML-F3W2-TT-0104/Completely_Bonded_2025-03-28/chambertest1/pedestal_run/run_20250328_104007_BV300_RH37_T21_trimmed300',
    'data/320-ML-F3W2-TT-0105/Completely_Bonded_2025-03-28/chambertest1/pedestal_run/run_20250328_152450_BV300_RH0_T20_trimmed300',
    'data/320-ML-F3W2-TT-0108/Completely_Bonded_2025-03-28/chambertest1/pedestal_run/run_20250328_142217_BV300_RH0_T20_trimmed300',
    ]


print(f'total number of modules = {len(listofmodules_root)}')

mods = [
    'MFL3W2TT0101',
    'MLF3W2TT0102',
    'MLF3W2TT0103',
    "MLF3W2TT0104",
    "MLF3W2TT0105",
    "MLF3W2TT0108",
]

print(f'# of hxbs = {len(mods)}')

def noisetudy(filename): #this is a root file from GUI
    f = uproot.open(filename)
    tree = f["runsummary"]["summary"]
    df_data = tree.arrays(library='pd')
    adc_mean = df_data['adc_mean']
    adc_stdd = df_data['adc_stdd']
    return adc_mean,adc_stdd

#fig, axes = plt.subplots(1, 2, figsize=(12, 6)) 
all_adc_means = []
all_adc_stdd = [] 

Mean_of_adc_mean = []
Mean_of_adc_std = []

for mod_file,mod in zip(listofmodules_root,mods):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))  
    fname = '/home/daq3/hgcal/'+mod_file+'/pedestal_run0.root'
    adc_mean,adc_stdd= noisetudy(fname)

    mean_val = np.mean(adc_mean)
    std_val = np.std(adc_mean)

    std_mean = np.mean(adc_stdd)
    std_std = np.std(adc_stdd)

    axes[0].hist(adc_mean, bins=70,histtype = 'step', label=f"{mod}\nMean: {mean_val:.2f}\nStd: {std_val:.2f}")
    axes[0].set_xlabel('adc_mean')
    axes[0].set_ylabel('Entries')
    axes[0].set_title('ADC Mean ')
    axes[0].set_xlim(0, 400) #same axis as HEXMAP
    axes[0].legend()
    axes[0].xaxis.set_label_coords(0.95, -0.05)  
    axes[0].yaxis.set_label_coords(-0.05, 0.95) 
    axes[0].minorticks_on()
    axes[0].tick_params(axis='both', which='major', direction='in', length=6, width=1)
    axes[0].tick_params(axis='both', which='minor', direction='in', length=3, width=0.5)

    axes[1].hist(adc_stdd, bins=70, histtype = 'step',label=f"{mod}\nMean: {std_mean:.2f}\nStd: {std_std:.2f}")
    axes[1].set_xlabel('Noise')
    axes[1].set_ylabel('Entries')
    axes[1].set_title('ADC STD')
    axes[1].legend()
    axes[1].set_xlim(0,8) #same axis as HEXMAP
    axes[1].xaxis.set_label_coords(0.95, -0.05)  
    axes[1].yaxis.set_label_coords(-0.05, 0.95) 
    axes[1].minorticks_on()
    axes[1].minorticks_on()
    axes[1].tick_params(axis='both', which='major', direction='in', length=6, width=1)
    axes[1].tick_params(axis='both', which='minor', direction='in', length=3, width=0.5)

    #axes[1].set_xlim(0, 200)
    #axes[1].legend(loc = 'upper right')

     
    all_adc_means.append(adc_mean)
    all_adc_stdd.append(adc_stdd)
    #Mean_of_adc_mean.append([mean_val])
    #Mean_of_adc_std.append([std_mean])
    Mean_of_adc_mean.append(mean_val)
    Mean_of_adc_std.append(std_mean)

    output_jpg = f"outputplots/V3b/ADC_for_MOD_{mod}.jpg"
    plt.savefig(output_jpg, format="jpg", bbox_inches="tight")
    plt.close(fig)
    #print(adc_mean)
    #print(adc_stdd)
    print(len(Mean_of_adc_mean))


fig, axes = plt.subplots(1, 2, figsize=(20, 10))  
#axes[0].hist(Mean_of_adc_mean, bins = 18, histtype = 'step',stacked=True, label=hxbs)
axes[0].hist(Mean_of_adc_mean,  bins=22, histtype='step', color='black', linewidth=2)
axes[0].set_xlabel('ADC Mean ', fontsize=14, fontname='Times New Roman')
axes[0].set_ylabel('Entries', fontsize=14, fontname='Times New Roman')
axes[0].set_title('Mean of Adc mean values for all V3Cs @ TTU Untrimmed', fontsize=16, fontname='Times New Roman')
axes[0].xaxis.set_label_coords(0.85, -0.05)  
axes[0].yaxis.set_label_coords(-0.05, 0.95) 
axes[0].minorticks_on()
axes[0].set_xlim(0, 400)
axes[0].tick_params(axis='both', which='major', direction='in', length=6, width=1)
axes[0].tick_params(axis='both', which='minor', direction='in', length=3, width=0.5)


axes[1].hist(Mean_of_adc_std, bins=22, histtype='step', color='black', linewidth=2)
axes[1].set_xlabel('Mean value Noise', fontsize=14, fontname='Times New Roman')
axes[1].set_ylabel('Entries', fontsize=14, fontname='Times New Roman')
axes[1].set_title('Mean of Noise(Adc Std) values for all V3Cs @ TTU Untrimmed', fontsize=16, fontname='Times New Roman')
axes[1].legend(loc = 'upper right')
axes[1].set_ylim(0, 8)
axes[1].xaxis.set_label_coords(0.85, -0.05)  
axes[1].yaxis.set_label_coords(-0.05, 0.95) 
axes[1].minorticks_on()
axes[1].minorticks_on()
axes[1].tick_params(axis='both', which='major', direction='in', length=6, width=1)
axes[1].tick_params(axis='both', which='minor', direction='in', length=3, width=0.5)

#axes[1].legend()
#axes[1].set_xlim(0, 250)
plt.rcParams['font.family'] = 'Times New Roman'
output_jpg = f"outputplots/V3b/SummaryV3b_Mods.jpg"
plt.savefig(output_jpg, format="jpg", bbox_inches="tight")
plt.close(fig)

