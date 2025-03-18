import uproot
import matplotlib.pyplot as plt
import numpy as np
#import ROOT no ROOT :(

listofmodules_root= [
    'data/320-XL-F42-MH-00212/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_140258',
    'data/320-XL-F42-MH-00213/Untaped_2025-03-14/qc_test2/pedestal_run/run_20250314_141709',
    'data/320-XL-F42-MH-00214/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_142400',
    'data/320-XL-F42-MH-00229/Taped_2025-02-17/pedestal_run/run_20250217_181639',#dummy mod now
    'data/320-XL-F42-MH-00230/Taped_2025-03-10/qc_test/pedestal_run/run_20250310_172127',#dummy now 
    'data/320-XL-F42-MH-00239/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_095644',
    'data/320-XL-F42-MH-00240/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_100337',
    'data/320-XL-F42-MH-00241/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_101458',
    'data/320-XL-F42-MH-00242/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_102221',
    'data/320-XL-F42-MH-00253/Untaped_2025-03-13/qc_test7/pedestal_run/run_20250313_154013',
    'data/320-XL-F42-MH-00254/Untaped_2025-03-13/qc_test3/pedestal_run/run_20250313_154936',
    'data/320-XL-F42-MH-00261/Taped_2025-03-10/qc_test/pedestal_run/run_20250310_171326', #dummy
    'data/320-XL-F42-MH-00262/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_110923',
    'data/320-XL-F42-MH-00263/Taped_2025-02-17/pedestal_run/run_20250217_180840', #dummy mod
    'data/320-XL-F42-MH-00264/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_130328',
    'data/320-XL-F42-MH-00268/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_123226',
    'data/320-XL-F42-MH-00269/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_123932',
    'data/320-XL-F42-MH-00275/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_131033',
    'data/320-XL-F42-MH-00276/Untaped_2025-03-14/qc_test3/pedestal_run/run_20250314_135603',
    'data/320-XL-F42-MH-00277/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_124616',
    'data/320-XL-F42-MH-00278/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_125342',
    'data/320-XL-F42-MH-00283/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_150601',
    'data/320-XL-F42-MH-00284/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_151215',
    'data/320-XL-F42-MH-00285/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_151909',
    'data/320-XL-F42-MH-00286/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_152515',



    'data/320-XL-F42-QH-00225/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_094557',
    'data/320-XL-F42-QH-00231/Untaped_2025-03-13/qc_test3/pedestal_run/run_20250313_161303',
    'data/320-XL-F42-QH-00232/Untaped_2025-03-13/qc_test2/pedestal_run/run_20250313_160301',
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
    'data/320-XL-F42-QH-00278/Untaped_2025-03-14/qc_test2/pedestal_run/run_20250314_145010',
    'data/320-XL-F42-QH-00279/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_145801',
    'data/320-XL-F42-QH-00284/Untaped_2025-03-13/qc_test3/pedestal_run/run_20250313_162907',
    'data/320-XL-F42-QH-00285/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_092823',
    'data/320-XL-F42-QH-00286/Untaped_2025-03-14/qc_test/pedestal_run/run_20250314_093600',
    'data/320-XL-F42-QH-00287/Untaped_2025-03-13/qc_test2/pedestal_run/run_20250313_163622',
    #'320-ML-F3CX-TT-0016/Completely_Encapsulated_2025-03-06/chamber_test1/',
    ]


print(f'total number of modules = {len(listofmodules_root)}')
hxbs = [
    "320XLF42MH00212", "320XLF42MH00213", "320XLF42MH00214", "320XLF42MH00229",
    "320XLF42MH00230", "320XLF42MH00239", "320XLF42MH00240", "320XLF42MH00241",
    "320XLF42MH00242", "320XLF42MH00253", "320XLF42MH00254", "320XLF42MH00261",
    "320XLF42MH00262", "320XLF42MH00263", "320XLF42MH00264", "320XLF42MH00268",
    "320XLF42MH00269", "320XLF42MH00275", "320XLF42MH00276", "320XLF42MH00277",
    "320XLF42MH00278", "320XLF42MH00283", "320XLF42MH00284", "320XLF42MH00285",
    "320XLF42MH00286", "320XLF42QH00225",                    "320XLF42QH00231",
    "320XLF42QH00232", "320XLF42QH00253", "320XLF42QH00254", "320XLF42QH00255",
    "320XLF42QH00256", "320XLF42QH00268", "320XLF42QH00269", "320XLF42QH00270",
    "320XLF42QH00272", "320XLF42QH00273", "320XLF42QH00274", "320XLF42QH00275",
    "320XLF42QH00276", "320XLF42QH00277", "320XLF42QH00278", "320XLF42QH00279",
    "320XLF42QH00284", "320XLF42QH00285", "320XLF42QH00286", "320XLF42QH00287"
]
print(f'# of hxbs = {len(hxbs)}')
def create_masks(df_data):

    # create the masks
    norm_mask = df_data["channeltype"] == 0 

    calib_mask = df_data["channeltype"] == 1

    cm0_mask = df_data["channeltype"] == 100
    cm0_mask &= df_data["channel"] % 2 == 0

    cm1_mask = df_data["channeltype"] == 100
    cm1_mask &= df_data["channel"] % 2 == 1

    nc_mask = df_data["channeltype"] == 0
    nc_mask &= df_data["pad"] < 0

    return norm_mask, calib_mask, cm0_mask, cm1_mask, nc_mask
    

def noisetudy(filename): #this is a root file from GUI
    f = uproot.open(filename)
    tree = f["runsummary"]["summary"]
    df_data = tree.arrays(library='pd')
    #norm_mask, calib_mask, cm0_mask, cm1_mask, nc_mask = create_masks(df_data)

    ##noise

    #column = 'adc_stdd'
    column  = 'adc_mean'
    #zeros = df_data[column] == 0
    #median_noise = df_data[column][norm_mask].median()
    #mean_noise= df_data[column][norm_mask].mean()
    adc_mean = df_data['adc_mean']
    adc_stdd = df_data['adc_stdd']
    #mean_noise= df_data[column].mean()
    #std_noise = df_data[column][norm_mask].std()

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

    # Define histograms
    # hist_adc_mean = ROOT.TH1F(f"adc_mean_{hxb}", f"ADC Mean {hxb}", 70, min(adc_mean), max(adc_mean))
    # hist_adc_stdd = ROOT.TH1F(f"adc_stdd_{hxb}", f"ADC Std {hxb}", 70, min(adc_stdd), max(adc_stdd))

    # # Fill histograms
    # for val in adc_mean:
    #     hist_adc_mean.Fill(val)
    # for val in adc_stdd:
    #     hist_adc_stdd.Fill(val)

    # # Write histograms to the ROOT file
    # hist_adc_mean.Write()
    # hist_adc_stdd.Write()

    # all_adc_means.append(adc_mean)
    # all_adc_stdd.append(adc_stdd)
    # Mean_of_adc_mean.append(mean_val)
    # Mean_of_adc_std.append(std_mean)


    axes[0].hist(adc_mean, bins=70,histtype = 'step', label=f"{hxb}\nMean: {mean_val:.2f}\nStd: {std_val:.2f}")
    axes[0].set_xlabel('adc_mean')
    axes[0].set_ylabel('Entries')
    axes[0].set_title('ADC Mean ')
    #axes[0].set_xlim(0, 200)
    axes[0].legend()

    axes[1].hist(adc_stdd, bins=70, histtype = 'step',label=f"{hxb}\nMean: {std_mean:.2f}\nStd: {std_std:.2f}")
    axes[1].set_xlabel('adc_std(noise)')
    axes[1].set_ylabel('Entries')
    axes[1].set_title('ADC STD')
    #axes[1].set_xlim(0, 200)
    #axes[1].legend(loc = 'upper right')

     
    all_adc_means.append(adc_mean)
    all_adc_stdd.append(adc_stdd)
    #Mean_of_adc_mean.append([mean_val])
    #Mean_of_adc_std.append([std_mean])
    Mean_of_adc_mean.append(mean_val)
    Mean_of_adc_std.append(std_mean)

    output_jpg = f"outputplots/V3b/ADC_for_hxb_{hxb}.jpg"
    plt.savefig(output_jpg, format="jpg", bbox_inches="tight")
    plt.close(fig)
    #print(adc_mean)
    #print(adc_stdd)
    print(len(Mean_of_adc_mean))


fig, axes = plt.subplots(1, 2, figsize=(20, 10))  
#axes[0].hist(Mean_of_adc_mean, bins = 18, histtype = 'step',stacked=True, label=hxbs)
axes[0].hist(Mean_of_adc_mean, histtype = 'step',bins = 22)
axes[0].set_xlabel('adc__mean')
axes[0].set_ylabel('Entries')
axes[0].set_title('Mean of adc_mean values for all V3Bs @ TTU Untrimmed')
#axes[0].set_xlim(0, 250)



#axes[1].hist(Mean_of_adc_std,bins = 18,histtype = 'step',stacked=True, label=hxbs)
axes[1].hist(Mean_of_adc_std,histtype = 'step',bins = 22)
axes[1].set_xlabel('mean value Noise(adc_std)')
axes[1].set_ylabel('Entries')
axes[1].set_title('Mean of Noise(adc_std) values for all V3Bs @ TTU Untrimmed')
axes[1].legend(loc = 'upper right')
#axes[1].legend()
#axes[1].set_xlim(0, 250)
output_jpg = f"outputplots/V3b/SummaryV3b_hxbs.jpg"
plt.savefig(output_jpg, format="jpg", bbox_inches="tight")
plt.close(fig)
#axes[1].legend()



# hist_dict = {}
# hist_summary_mean, bin_edges_summary_mean = np.histogram(Mean_of_adc_mean, bins=22)
# hist_summary_std, bin_edges_summary_std = np.histogram(Mean_of_adc_std, bins=22)

# # Store summary histograms
# hist_dict["Mean_of_adc_mean"] = {
#     "fValues": hist_summary_mean,
#     "fBinEdges": bin_edges_summary_mean
# }
# hist_dict["Mean_of_adc_std"] = {
#     "fValues": hist_summary_std,
#     "fBinEdges": bin_edges_summary_std
# }

# # Write to ROOT file using uproot
# with uproot.recreate("outputplots/V3b/Summary/ADC_Noise_Study.root") as f:
#     for key, hist in hist_dict.items():
#         f[key] = uproot.writing.identify.interpretation_from_histogram(
#             (hist["fValues"], hist["fBinEdges"])
#         )

# print("Histograms saved in ADC_Noise_Study.root ")
