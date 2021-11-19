#Import relevant libraries and define settings for plotting.
%matplotlib inline
import sys
print(sys.version)

import numpy as np
print ('Numpy version:'), np.__version__

import pandas as pd
print ('Pandas version:'), pd.__version__

import matplotlib as mpl
import matplotlib.pyplot as plt
print ('Matplotlib version:'), mpl.__version__

import seaborn as sns
print ('Seaborn version:'), sns.__version__

import datetime
import time

sns.set()
pal = sns.hls_palette(10, h=.5)
sns.set_palette(pal)

#Avoid display of scientific notation and show precision of 4 decimals:
pd.set_option('display.float_format', lambda x: '%.4f' % x)

import urllib.request
url = 'https://s3.amazonaws.com/nyc-tlc/misc/uber_nyc_data.csv'
filename = 'uber_nyc_data.csv'
urllib.request.urlretrieve(url, filename)

df_uber = pd.read_csv('uber_nyc_data.csv')
df_uber.info() 
df_uber.head()