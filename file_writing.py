import os
import csv
import time
import datetime
import pandas as pd
from constants import *

def write_to_csv(data):

    folder = f'./outputs/{datetime.date.today()}'

    if not os.path.exists(folder):
        os.makedirs(folder)

    if type(data) is list:
        for idx, res in enumerate(data):
            sub_folder = LOCATIONS[idx]
            if not os.path.exists(f'{folder}/{sub_folder}'):
                os.makedirs(f'{folder}/{sub_folder}')
            write_time = time.time()
            df = pd.DataFrame(res)
            df.to_csv(f'{folder}/{sub_folder}/{write_time}.csv', quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
    
    else:
        write_time = time.time()
        data.to_csv(f'{folder}/{write_time}.csv', quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)