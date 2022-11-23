import json 
import numpy as np
def parse(path):
    with (open(path)) as f:
        data=json.load(f)
    user_name=[]
    data_size=[]
    for k,v in data.items():
        if k=="users":
            user_name.extend(v)
        print(k,len(v))
        if k=="user_data":
            print(len(data['user_data'][user_name[0]]['x']))
            print(len(data['user_data'][user_name[0]]['y']))
            print(len(data['user_data'][user_name[0]]['x'][1]))
            print((data['user_data'][user_name[0]]['y']))
            for name in user_name:
                print(len(data['user_data'][name]['x']))
                data_size.append(len(data['user_data'][name]['x']))
    print(np.min(data_size),np.median(data_size),np.max(data_size))
parse("/research/d1/gds/xtan22/FedBalancer/data/femnist/data/train/all_data_3_niid_2_keep_0_train_9.json")