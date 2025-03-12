import pickle
with open('/home/daq3/hgcal/data/320-ML-F3CX-TT-0022/Frontside_Encapsulated_2025-01-08/stp_dummy2/320-ML-F3CX-TT-0022_IVset_2025-01-08_17:28:12_0.pkl', 'rb') as file:
    data = pickle.load(file)
    data_array = data["data"]
    Bias_Voltage = data_array[:, 0]
    Leakage_current = data_array[:, 2]


for Voltage,Current in zip(Bias_Voltage,Leakage_current):
    print(f"Bias Voltage:{Voltage} Leakage_current: {Current}")