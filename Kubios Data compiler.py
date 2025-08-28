#!/usr/bin/env python
# coding: utf-8

# Instructions (Please read carefully):
# 
# Requirements: 
# Python>=3.0
# Pandas>=2.0
# 
# This code is for compiling the data from each sample from Kubios HRV Scientific to a CSV file. You can select the sample size and how many samples you want to compile. If you are here, that means you know how difficult compiling them is manually without having the pro version. Let me make your life easier for you. Read the instructions below carefully before proceeding:
# 
# This works by taking the data from the results that can be saved using kubios to a CSV file. The code does not sample or extract any data from the Kubios software. You can save the results of a sample in Kubios as a CSV (Ensure you are analysing the correct timestamp -> File -> Save result as -> save the file in CSV format). PLEASE NAME EACH FILE WITH THE CONTEXT FOR RECOGNITION (eg, Ibrahim zone 1 day 1, Chayan zone 1 day 2, Abhay zone 2 day 1, etc.)
# 
# COMPILE ALL THE CSVs IN ONE FOLDER WITHOUT ANY OTHER FILES
# COPY THE FILE PATH (ctrl + shift + c)
# PASTE IT AT THE INPUT 
# And voila, all the data samples have been compiled into one CSV. Hope this save you time.

# In[ ]:


import pandas as pd
import glob
import os
import csv

path_to_csv = input(print("Input Folder with the CSV: ")).strip('"')

path_to_csv = path_to_csv.replace("\\","/")

print("Using path: ", path_to_csv)

if os.path.exists(path_to_csv):
    print("\033[92m Path is valid!")
else:
    print("\033[91m Path not found!")

csv_files = glob.glob(os.path.join(path_to_csv, "*.csv"))

for files in csv_files:
    if os.path.exists(files):
        continue
    else:
        print(files, "\033[91m This is path is not found")
print("\033[92m All files are valid")

out_folder = os.path.join(path_to_csv, "with headers")

os.makedirs(out_folder, exist_ok=True)
print("Creating new folder 'with headers'")

header = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]

for file in os.listdir(path_to_csv):
    if file.endswith(".csv"):
        in_path = os.path.join(path_to_csv, file)

        with open(in_path, "r", newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))


        
        out_path = os.path.join(out_folder, file)
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)   # add header
            writer.writerows(rows)    # add original content


csv_files = glob.glob(os.path.join(out_folder, "*.csv"))

for files in csv_files:
    if os.path.exists(files):
        continue
    else:
        print(files, "\033[91mthis is path is not found")

print("\033[92m All the new files are valid")

file_name = []
timestamp = []
mean_RR = []
SDNN = []
Mean_HR = []
STD_HR = []
Min_HR = []
Max_HR = []
RMSSD = []
NNxx = []
pNNxx = []
HRV_Index = []
TINN = []
Stress_Index = []
LF_Power = []
LF_Power_log = []
LF_Power_percentage = []
LF_Power_nu = []
HF_Power = []
HF_Power_log = []
HF_Power_percentage = []
HF_Power_nu = []
LF_HF_ratio = []
SD1 = []
SD2 = []
SD2_SD1 = []
ApEn = []
SampEn = []
DFA_alpha1 = []
DFA_alpha2 = []


for file in csv_files:
    df = pd.read_csv(file)
    file_name.append(os.path.basename(file))
    timestamp.extend(df.loc[df["1"] == "  Sample limits (hh:mm:ss):   ", "2"].tolist())
    mean_RR.extend(df.loc[df["1"] == "  Mean RR  (ms):              ", "2"].tolist())
    SDNN.extend(df.loc[df["1"] == "  SDNN (ms):                  ", "2"].tolist())
    Mean_HR.extend(df.loc[df["1"] == "  Mean HR (beats/min):        ", "2"].tolist())
    STD_HR.extend(df.loc[df["1"] == "  SD HR (beats/min):          ", "2"].tolist())
    Min_HR.extend(df.loc[df["1"] == "  Min HR (beats/min):         ", "2"].tolist())
    Max_HR.extend(df.loc[df["1"] == "  Max HR (beats/min):         ", "2"].tolist())
    RMSSD.extend(df.loc[df["1"] == "  RMSSD (ms):                 ", "2"].tolist())
    NNxx.extend(df.loc[df["1"] == "  NNxx (beats):               ", "2"].tolist())
    pNNxx.extend(df.loc[df["1"] == "  pNNxx (%):                  ", "2"].tolist())
    HRV_Index.extend(df.loc[df["1"] == "  RR tri index:               ", "2"].tolist())
    TINN.extend(df.loc[df["1"] == "  TINN (ms):                  ", "2"].tolist())
    Stress_Index.extend(df.loc[df["1"] == "  Stress index:               ", "2"].tolist())
    LF_Power.extend(df.loc[df["1"] == "  LF (ms^2):                  ", "2"].tolist())
    LF_Power_log.extend(df.loc[df["1"] == "  LF (log):                   ", "2"].tolist())
    LF_Power_percentage.extend(df.loc[df["1"] == "  LF (%):                     ", "2"].tolist())
    LF_Power_nu.extend(df.loc[df["1"] == "  LF (n.u.):                  ", "2"].tolist())
    HF_Power.extend(df.loc[df["1"] == "  HF (ms^2):                  ", "2"].tolist())
    HF_Power_log.extend(df.loc[df["1"] == "  HF (log):                   ", "2"].tolist())
    HF_Power_percentage.extend(df.loc[df["1"] == "  HF (%):                     ", "2"].tolist())
    HF_Power_nu.extend(df.loc[df["1"] == "  HF (n.u.):                  ", "2"].tolist())
    LF_HF_ratio.extend(df.loc[df["1"] == " LF/HF ratio:                 ", "2"].tolist())
    SD1.extend(df.loc[df["1"] == "  SD1 (ms):                   ", "2"].tolist())
    SD2.extend(df.loc[df["1"] == "  SD2 (ms):                   ", "2"].tolist())
    SD2_SD1.extend(df.loc[df["1"] == "  SD2/SD1 ratio:              ", "2"].tolist())
    ApEn.extend(df.loc[df["1"] == " Approximate entropy (ApEn):  ", "2"].tolist())
    SampEn.extend(df.loc[df["1"] == " Sample entropy (SampEn):     ", "2"].tolist())
    DFA_alpha1.extend(df.loc[df["1"] == "  alpha 1:                    ", "2"].tolist())
    DFA_alpha2.extend(df.loc[df["1"] == "  alpha 2:                    ", "2"].tolist())

all_var = {
    "File Name": file_name,
    "Timestamp of the sample" :timestamp,
    "Mean RR" : mean_RR, "SDNN": SDNN, "Mean HR" :Mean_HR, "STD HR" : STD_HR,"Min HR" :Min_HR, "Max HR": Max_HR, "RMSSD":RMSSD, "NNxx":NNxx,
    "pNNxx": pNNxx,"HRV Triangular Index" : HRV_Index, "TINN": TINN, "Stress Index" :Stress_Index, "LF Power(ms^2)": LF_Power, "LF Power (log)":LF_Power_log,
    "LF Power %": LF_Power_percentage, "LF Power(n.u)": LF_Power_nu, "HF Power(ms^2)": HF_Power, "HF Power (log)":HF_Power_log,
    "HF Power %": HF_Power_percentage, "HF Power(n.u)": HF_Power_nu, "LF/HF ratio": LF_HF_ratio, "SD1" :SD1, "SD2": SD2, "SD2/SD1": SD2_SD1, "ApEn": ApEn,
    "Sample Entropy": SampEn, "DFA alpha 1" :DFA_alpha1, "DFA alpha 2": DFA_alpha2}

check_lens = [len(list) for names, list in all_var.items()]

if len(set(check_lens)) == 1:
    print("\033[92m All Data available")
else:
    for name, var in all_var.items():
        print(f"\033[91m{name}: {len(var)}")
    print("\033[91m Missing data or blank data, make sure all the data is present in the new folder")

df = pd.DataFrame(all_var)

save = input("Save File as: ")
df.to_csv(save+".csv")

print(f"\033[90m File Saved as {save}.csv")


# In[ ]:




