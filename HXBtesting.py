import uproot
import matplotlib.pyplot as plt
import numpy as np

listofmodules_root= [
    'data/320-XL-F42-MH-00212/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_140258',
    'data/320-XL-F42-MH-00213/Untaped_2025-03-14/qc_test2/pedestal_run/run_20250314_141709',
    'data/320-XL-F42-MH-00214/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_142400',

    'data/320-XL-F42-MH-00239/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_095644',
    'data/320-XL-F42-MH-00240/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_100337',
    'data/320-XL-F42-MH-00241/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_101458',
    'data/320-XL-F42-MH-00242/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_102221',

    'data/320-XL-F42-QH-00253/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_111825',
    'data/320-XL-F42-QH-00254/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_112557',
    'data/320-XL-F42-QH-00255/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_113224',
    'data/320-XL-F42-QH-00256/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_113901',
    'data/320-XL-F42-QH-00268/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_114921',
    'data/320-XL-F42-QH-00269/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_115734',
    'data/320-XL-F42-QH-00270/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_120409',
    'data/320-XL-F42-QH-00272/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_103001',
    'data/320-XL-F42-QH-00273/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_103756',
    'data/320-XL-F42-QH-00274/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_104516',
    'data/320-XL-F42-QH-00275/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_105354',
    'data/320-XL-F42-QH-00276/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_143205',
    'data/320-XL-F42-QH-00277/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_143750',


    'data/320-XL-F42-QH-00285/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_092823',
    'data/320-XL-F42-QH-00286/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_093600',
    #'320-ML-F3CX-TT-0016/Completely_Encapsulated_2025-03-06/chamber_test1/',
    ]


print(f'total number of modules = {len(listofmodules_root)}')
# mods = ['320-ML-F3CX-TT-0014','320-ML-F3CX-TT-0015','320-ML-F3CX-TT-0016','320-ML-F3CX-TT-0017','320-ML-F3CX-TT-0019','320-ML-F3CX-TT-0020'
# ,'320-ML-F3CX-TT-M0021','320-ML-F3CX-TT-M0022','320-ML-F3CX-TT-M0023','320-ML-F3CX-TT-M0024','320-ML-F3CX-TT-M0025','320-ML-F3CX-TT-0026'
# ,'320-ML-F3CX-TT-0027','320-ML-F3CX-TT-0028','320-ML-F3CX-TT-0030','320-ML-F3CX-TT-0029','320-ML-F3CX-TT-0031','320-ML-F3CX-TT-0032'
# ]

# def create_masks(df_data):

#     # create the masks
#     norm_mask = df_data["channeltype"] == 0 

#     calib_mask = df_data["channeltype"] == 1

#     cm0_mask = df_data["channeltype"] == 100
#     cm0_mask &= df_data["channel"] % 2 == 0

#     cm1_mask = df_data["channeltype"] == 100
#     cm1_mask &= df_data["channel"] % 2 == 1

#     nc_mask = df_data["channeltype"] == 0
#     nc_mask &= df_data["pad"] < 0

#     return norm_mask, calib_mask, cm0_mask, cm1_mask, nc_mask
    

# def noisetudy(filename): #this is a root file from GUI
#     f = uproot.open(filename)
#     tree = f["runsummary"]["summary"]
#     df_data = tree.arrays(library='pd')
#     #norm_mask, calib_mask, cm0_mask, cm1_mask, nc_mask = create_masks(df_data)

#     ##noise

#     #column = 'adc_stdd'
#     column  = 'adc_mean'
#     #zeros = df_data[column] == 0
#     #median_noise = df_data[column][norm_mask].median()
#     #mean_noise= df_data[column][norm_mask].mean()
#     adc_mean = df_data['adc_mean']
#     adc_stdd = df_data['adc_stdd']
#     #mean_noise= df_data[column].mean()
#     #std_noise = df_data[column][norm_mask].std()

#     return adc_mean,adc_stdd

# #fig, axes = plt.subplots(1, 2, figsize=(12, 6)) 
# all_adc_means = []
# all_adc_stdd = [] 

# Mean_of_adc_mean = []
# Mean_of_adc_std = []

# for mod_file,mod in zip(listofmodules_root,mods):
#     fig, axes = plt.subplots(1, 2, figsize=(12, 6))  
#     fname = '/home/daq3/hgcal/'+mod_file+'/pedestal_run0.root'
#     adc_mean,adc_stdd= noisetudy(fname)

#     mean_val = np.mean(adc_mean)
#     std_val = np.std(adc_mean)

#     std_mean = np.mean(adc_stdd)
#     std_std = np.std(adc_stdd)
#     axes[0].hist(adc_mean, bins=70,histtype = 'step', label=f"{mod}\nMean: {mean_val:.2f}\nStd: {std_val:.2f}")
#     axes[0].set_xlabel('adc_mean')
#     axes[0].set_ylabel('Entries')
#     axes[0].set_title('ADC Mean ')
#     axes[0].set_xlim(0, 200)
#     axes[0].legend()

#     axes[1].hist(adc_stdd, bins=70, histtype = 'step',label=f"{mod}\nMean: {std_mean:.2f}\nStd: {std_std:.2f}")
#     axes[1].set_xlabel('adc_std(noise)')
#     axes[1].set_ylabel('Entries')
#     axes[1].set_title('ADC STD')
#     axes[1].set_xlim(0, 200)
#     axes[1].legend(loc = 'upper right')
#     all_adc_means.append(adc_mean)
#     all_adc_stdd.append(adc_stdd)
#     Mean_of_adc_mean.append([mean_val])
#     Mean_of_adc_std.append([std_mean])

#     output_jpg = f"outputplots/ADC_for_mod_{mod}.jpg"
#     plt.savefig(output_jpg, format="jpg", bbox_inches="tight")
#     #print(adc_mean)
#     #print(adc_stdd)
#     print(len(Mean_of_adc_mean))


# fig, axes = plt.subplots(1, 2, figsize=(20, 10))  
# axes[0].hist(Mean_of_adc_mean, bins = 18, histtype = 'step',stacked=True, label=mods)
# axes[0].set_xlabel('adc__mean')
# axes[0].set_ylabel('Entries')
# axes[0].set_title('Mean of adc_mean values for all V3As @ TTU Untrimmed')
# #axes[0].set_xlim(0, 250)



# axes[1].hist(Mean_of_adc_std,bins = 18,histtype = 'step',stacked=True, label=mods)
# axes[1].set_xlabel('mean value Noise(adc_std)')
# axes[1].set_ylabel('Entries')
# axes[1].set_title('Mean of Noise(adc_std) values for all V3As @ TTU Untrimmed')
# axes[1].legend(loc = 'upper right')
# #axes[1].legend()
# #axes[1].set_xlim(0, 250)
# output_jpg = f"outputplots/ADC_all_mods.jpg"
# plt.savefig(output_jpg, format="jpg", bbox_inches="tight")

# #axes[1].legend()






