import uproot
import matplotlib.pyplot as plt
import numpy as np
#import ROOT no ROOT :(

listofmodules_root= [
    'data/320-XL-F4C-MH-00113/Untaped_2025-03-20/chambertest1/pedestal_run/run_20250320_115339',
    'data/320-XL-F4C-MH-00114/Untaped_2025-03-21/chambertest1/pedestal_run/run_20250321_094756',
    'data/320-XL-F4C-MH-00117/Untaped_2025-03-21/chambertest1/pedestal_run/run_20250321_093353',
    'data/320-XL-F4C-MH-00118/Untaped_2025-03-20/test1/pedestal_run/run_20250320_154908',
    'data/320-XL-F4C-MH-00119/Untaped_2025-03-21/chambertest1/pedestal_run/run_20250321_105621',
    'data/320-XL-F4C-MH-00120/Untaped_2025-03-21/chambertest1/pedestal_run/run_20250321_104812',



    'data/320-XL-F4C-QH-00113/Untaped_2025-03-21/chambertest1/pedestal_run/run_20250321_103938',
    'data/320-XL-F4C-QH-00130/Untaped_2025-03-21/chambertest2/pedestal_run/run_20250321_111316',
    'data/320-XL-F4C-QH-00134/Untaped_2025-03-20/test3/pedestal_run/run_20250320_151418',
    'data/320-XL-F44-QH-00133/Untaped_2025-03-20/test3/pedestal_run/run_20250320_145324',
    'data/320-XL-F4C-QH-00137/Untaped_2025-03-21/chambertest1/pedestal_run/run_20250321_095935',
    'data/320-XL-F4C-QH-00138/Untaped_2025-03-21/chambertest1/pedestal_run/run_20250321_101037',
    'data/320-XL-F4C-QH-00140/Untaped_2025-03-20/test4/pedestal_run/run_20250320_153037', 
    'data/320-XL-F4C-QH-00141/Untaped_2025-03-21/chambertest1/pedestal_run/run_20250321_101935',
    'data/320-XL-F4C-QH-00142/Untaped_2025-03-21/chambertest1/pedestal_run/run_20250321_102844', 

    ]


print(f'total number of modules = {len(listofmodules_root)}')

hxbs = [
    "320XLF44MH00113",
    "320XLF44MH00114",
    "320XLF44MH00117",
    "320XLF44MH00118",
    "320XLF44MH00119",
    "320XLF44MH00120",
    "320XLF44QH00113",
    "320XLF44QH00130",
    "320XLF44QH00133",
    "320XLF44QH00134",
    "320XLF44QH00137",
    "320XLF44QH00138",
    "320XLF44QH00140",
    "320XLF44QH00141",
    "320XLF44QH00142"
]

print(f'# of hxbs = {len(hxbs)}')

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

for mod_file,hxb in zip(listofmodules_root,hxbs):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))  
    fname = '/home/daq3/hgcal/'+mod_file+'/pedestal_run0.root'
    adc_mean,adc_stdd= noisetudy(fname)

    mean_val = np.mean(adc_mean)
    std_val = np.std(adc_mean)

    std_mean = np.mean(adc_stdd)
    std_std = np.std(adc_stdd)

    axes[0].hist(adc_mean, bins=70,histtype = 'step', label=f"{hxb}\nMean: {mean_val:.2f}\nStd: {std_val:.2f}")
    axes[0].set_xlabel('adc_mean')
    axes[0].set_ylabel('Entries')
    axes[0].set_title('ADC Mean ')
    #axes[0].set_xlim(0, 200)
    axes[0].legend()
    axes[0].xaxis.set_label_coords(0.95, -0.05)  
    axes[0].yaxis.set_label_coords(-0.05, 0.95) 
    axes[0].minorticks_on()
    axes[0].tick_params(axis='both', which='major', direction='in', length=6, width=1)
    axes[0].tick_params(axis='both', which='minor', direction='in', length=3, width=0.5)

    axes[1].hist(adc_stdd, bins=70, histtype = 'step',label=f"{hxb}\nMean: {std_mean:.2f}\nStd: {std_std:.2f}")
    axes[1].set_xlabel('Noise')
    axes[1].set_ylabel('Entries')
    axes[1].set_title('ADC STD')
    axes[1].legend()
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

    output_jpg = f"outputplots/V3c/ADC_for_hxb_{hxb}.jpg"
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
axes[0].tick_params(axis='both', which='major', direction='in', length=6, width=1)
axes[0].tick_params(axis='both', which='minor', direction='in', length=3, width=0.5)


axes[1].hist(Mean_of_adc_std, bins=22, histtype='step', color='black', linewidth=2)
axes[1].set_xlabel('Mean value Noise', fontsize=14, fontname='Times New Roman')
axes[1].set_ylabel('Entries', fontsize=14, fontname='Times New Roman')
axes[1].set_title('Mean of Noise(Adc Std) values for all V3Cs @ TTU Untrimmed', fontsize=16, fontname='Times New Roman')
axes[1].legend(loc = 'upper right')
axes[1].xaxis.set_label_coords(0.85, -0.05)  
axes[1].yaxis.set_label_coords(-0.05, 0.95) 
axes[1].minorticks_on()
axes[1].minorticks_on()
axes[1].tick_params(axis='both', which='major', direction='in', length=6, width=1)
axes[1].tick_params(axis='both', which='minor', direction='in', length=3, width=0.5)

#axes[1].legend()
#axes[1].set_xlim(0, 250)
plt.rcParams['font.family'] = 'Times New Roman'
output_jpg = f"outputplots/V3c/SummaryV3c_hxbs.jpg"
plt.savefig(output_jpg, format="jpg", bbox_inches="tight")
plt.close(fig)

