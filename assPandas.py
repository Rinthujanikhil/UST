import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings 
warnings.filterwarnings('ignore')
#Read data from csv file Federal Aviation Authority (FAA) Dataset
data=pd.read_csv('faa_ai_prelim.csv',sep=',')
#b. View content of the data

display(data)
#View the dataset shape
data.shape
#Show all the columns present in the dataset

data.columns
#Extract the following attributes from the dataset:
#'ACFT_MAKE_NAME', 'LOC_STATE_NAME', 'ACFT_MODEL_NAME', 'RMK_TEXT'1 'FLT_PHASE', 'EVENT_TYPE_DESC', 'FATAL_FLAG'
data[['ACFT_MAKE_NAME', 'LOC_STATE_NAME', 'ACFT_MODEL_NAME', 'RMK_TEXT', 'FLT_PHASE', 'EVENT_TYPE_DESC', 'FATAL_FLAG']]
#f
data.isnull().sum()
#g Clean the dataset and replace the fatal flag NaN with “No” 
data.info()
data['FATAL_FLAG'].replace(np.nan,"No")
#i
data[data['ACFT_MAKE_NAME'].isnull().dropna()]
#j
data['ACFT_MAKE_NAME'].value_counts()
#k
data[data['FATAL_FLAG']=="Yes"]
#l
data[(data['EVENT_TYPE_DESC']=='Accident')&(data['FATAL_FLAG']=='Yes')]
