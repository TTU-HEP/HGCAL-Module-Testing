import uproot
import matplotlib.pyplot as plt


listofmodules_root= [
    '320-ML-F3CX-TT-0014/Completely_Encapsulated_2025-03-06/chamber_test1/pedestal_run/run_20250306_150110',
    '320-ML-F3CX-TT-0015/Completely_Encapsulated_2025-03-06/chamber_test1/pedestal_run/run_20250306_122700',
    '320-ML-F3CX-TT-0016/Completely_Encapsulated_2025-03-06/chamber_test1/pedestal_run/run_20250306_155057',
    '320-ML-F3CX-TT-0017/Completely_Encapsulated_2025-03-07/chamber_test1/pedestal_run/run_20250307_093315',
    '320-ML-F3CX-TT-0018/Completely_Encapsulated_2025-03-07/chamber_test2/pedestal_run/run_20250307_154026',
    '320-ML-F3CX-TT-0019/Completely_Encapsulated_2025-03-07/chamber_test1/pedestal_run/run_20250307_133145',
    '320-ML-F3CX-TT-0020/Completely_Encapsulated_2025-03-07/chamber_test1/pedestal_run/run_20250307_143023',
    '320-ML-F3CX-TT-0021/Bolted_2025-03-03/Official/pedestal_run/run_20250303_183643',
    '320-ML-F3CX-TT-0022/Frontside_Encapsulated_2025-01-08/stp_dummy2/pedestal_run/run_20250108_164408',
    '320-ML-F3CX-TT-0023/Bolted_2025-03-05/chamber_test1/pedestal_run/run_20250305_142603',
    '320-ML-F3CX-TT-0024/Completely_Encapsulated_2025-03-03/chamber_test3/pedestal_run/run_20250303_123331_BV500_RH0_T20_untrimmed',
    '320-ML-F3CX-TT-0025/Completely_Encapsulated_2025-03-03/chamber_test1/pedestal_run/run_20250303_163021',
    '320-ML-F3CX-TT-0026/Bolted_2025-03-05/chamber_test1/pedestal_run/run_20250305_154028',
    '320-ML-F3CX-TT-0027/Bolted_2025-03-05/pedestal_run/run_20250305_130824',
    '320-ML-F3CX-TT-0028/Bolted_2025-03-05/Chamber_test_1/pedestal_run/run_20250305_115527',
    '320-ML-F3CX-TT-0029/Completely_Encapsulated_2025-03-05/chamber_test1/pedestal_run/run_20250305_104557',
    '320-ML-F3CX-TT-0030/Completely_Encapsulated_2025-03-03/chamber_test1/pedestal_run/run_20250303_133931',
    '320-ML-F3CX-TT-0031/Completely_Encapsulated_2025-03-03/chamber_test1/pedestal_run/run_20250303_150936',
    '320-ML-F3CX-TT-0032/Completely_Bonded_2025-03-07/chamber_test1/pedestal_run/run_20250307_115457',
    #'320-ML-F3CX-TT-0016/Completely_Encapsulated_2025-03-06/chamber_test1/',
    ]

mods = ['320-ML-F3CX-TT-0014','320-ML-F3CX-TT-0015','320-ML-F3CX-TT-0016','320-ML-F3CX-TT-0017','320-ML-F3CX-TT-0019','320-ML-F3CX-TT-0020'
,'320-ML-F3CX-TT-M21','320-ML-F3CX-TT-M22','320-ML-F3CX-TT-M23','320-ML-F3CX-TT-M24','320-ML-F3CX-TT-M25','320-ML-F3CX-TT-0026'
,'320-ML-F3CX-TT-0027','320-ML-F3CX-TT-0028','320-ML-F3CX-TT-0030','320-ML-F3CX-TT-0029','320-ML-F3CX-TT-0031','320-ML-F3CX-TT-0032'
]

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

plt.figure(figsize=(12, 6))
for mod_file,mod in zip(listofmodules_root,mods):
    fname = '/home/daq3/hgcal/data/'+mod_file+'/pedestal_run0.root'
    adc_mean,adc_stdd= noisetudy(fname)
    plt.hist(adc_mean,bins = 50,histtype = 'step',label=mod)
    plt.xlabel('adc_mean ')
    plt.ylabel('Entries')
    plt.title('ADC Mean')
    #plt.xticks(rotation=90, fontsize=8)  
    plt.legend()

output_pdf = "adc_mean.pdf"
plt.savefig(output_pdf, format="pdf", bbox_inches="tight")
print(adc_mean)
print(adc_stdd)



