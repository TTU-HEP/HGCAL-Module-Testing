import os
import pickle
import matplotlib.pyplot as plt


plt.ion()

directories = ['/home/daq3/hgcal/data/320-ML-F3CX-TT-0014/Completely_Encapsulated_2025-03-06/chamber_test1/320-ML-F3CX-TT-0014_IVset_2025-03-06_15:03:56_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0015/Completely_Encapsulated_2025-03-06/chamber_test1/320-ML-F3CX-TT-0015_IVset_2025-03-06_12:30:38_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0016/Completely_Encapsulated_2025-03-06/chamber_test1/320-ML-F3CX-TT-0016_IVset_2025-03-06_15:54:05_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0017/Completely_Encapsulated_2025-03-07/chamber_test1/320-ML-F3CX-TT-0017_IVset_2025-03-07_09:38:40_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0019/Completely_Encapsulated_2025-03-07/chamber_test1/320-ML-F3CX-TT-0019_IVset_2025-03-07_13:34:51_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0020/Completely_Encapsulated_2025-03-07/chamber_test1/320-ML-F3CX-TT-0020_IVset_2025-03-07_14:33:39_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0021/Bolted_2025-03-03/Official/320-ML-F3CX-TT-0021_IVset_2025-03-03_19:09:20_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0022/Frontside_Encapsulated_2025-01-08/stp_dummy2/320-ML-F3CX-TT-0022_IVset_2025-01-08_17:28:12_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0023/Frontside_Encapsulated_2025-01-08/standardtestrundummy/320-ML-F3CX-TT-0023_IVset_2025-01-08_15:10:29_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0024/Completely_Encapsulated_2025-03-03/chamber_test3/320-ML-F3CX-TT-0024_IVset_2025-03-03_12:35:39_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0025/Completely_Encapsulated_2025-03-03/chamber_test1/320-ML-F3CX-TT-0025_IVset_2025-03-03_17:03:55_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0026/Bolted_2025-03-05/chamber_test1/320-ML-F3CX-TT-0026_IVset_2025-03-05_15:44:49_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0027/Bolted_2025-03-05/320-ML-F3CX-TT-0027_IVset_2025-03-05_13:11:14_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0028/Bolted_2025-03-05/Chamber_test_1/320-ML-F3CX-TT-0028_IVset_2025-03-05_11:59:05_0.5.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0030/Completely_Encapsulated_2025-03-03/chamber_test1/320-ML-F3CX-TT-0030_IVset_2025-03-03_14:15:24_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0029/Completely_Encapsulated_2025-03-05/chamber_test1/320-ML-F3CX-TT-0029_IVset_2025-03-05_10:50:10_0.pkl',
'/home/daq3/hgcal/data/320-ML-F3CX-TT-0031/Completely_Encapsulated_2025-03-03/chamber_test1/320-ML-F3CX-TT-0031_IVset_2025-03-03_15:43:45_0.pkl',
]

mods = ['320-ML-F3CX-TT-0014','320-ML-F3CX-TT-0015','320-ML-F3CX-TT-0016','320-ML-F3CX-TT-0017','320-ML-F3CX-TT-0019','320-ML-F3CX-TT-0020','320-ML-F3CX-TT-M21','320-ML-F3CX-TT-M22','320-ML-F3CX-TT-M23','320-ML-F3CX-TT-M24','320-ML-F3CX-TT-M25','320-ML-F3CX-TT-0026'
        ,'320-ML-F3CX-TT-0027','320-ML-F3CX-TT-0028','320-ML-F3CX-TT-0030','320-ML-F3CX-TT-0029','320-ML-F3CX-TT-0031'


]


plt.figure(figsize=(20,10))


for pkl_file_path,mod in zip(directories,mods):
    if pkl_file_path:
        with open(pkl_file_path, "rb") as file:
            data = pickle.load(file)
            data_array = data["data"]
            x_values = data_array[:, 0]
            y_values = data_array[:, 2]

            plt.plot(x_values, y_values, label=mod)
            #plt.plot(data, label= directory)                                                                                                                                                                         


plt.xlabel("Bias Voltage [V]")
plt.ylabel("Leakage Current [A]")
plt.title("IV Curves for all Modules tested March 2025 RH: 0% Temp: $20^{\circ}$C")
plt.yscale("log")
plt.legend()
plt.xlim(0, max(x_values) * 1.2)
#plt.grid(True)                                                                                                                                                                                                       


output_pdf = "IVcombined.pdf"
plt.savefig(output_pdf, format="pdf")
#plt.show()