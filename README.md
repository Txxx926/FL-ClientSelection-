# Course Project
Implement a data-similarity and clustering based client selection method for fault-tolerance and efficiency in FL.
Based on original **FLASH** and **FedBalancer** Framework.



## Datasets

We evaluated based on five datasets: ```FEMNIST```, ```Celeba```, ```Reddit```, ```Shakespeare```, ```UCI-HAR```.

## How to Run the Experiments

### Running the main experiment of the paper in Section 4.2 and 4.3 one by one

1. Go to directory of respective dataset in `data/` for instructions on generating the benchmark dataset
2. Run (please refer to the list of config files in the subdirectory with respective dataset name in ```configs/```, it contains all the config files for the experiment)
```
$ cd models/

# FedAvg + 1T experiment in Section 4.2 and 4.3 with random seed 0
# candidate {dataset_name}: femnist/celeba/reddit/shakespeare/har

$ python main.py --config=configs/{dataset_name}/{dataset_name}_fedavg_1T_seed0.cfg
# example: python main.py --config=configs/har/har_fedavg_1T_seed0.cfg

# FedBalancer experiment in Section 4.2 and 4.3 with random seed 0
# candidate {dataset_name}: femnist/celeba/reddit/shakespeare/har

$ python main.py --config=configs/{dataset_name}/{dataset_name}_fedbalancer_seed0.cfg
# example: python main.py --config=configs/har/har_fedbalancer_seed0.cfg
```

Add ```CUDA_VISIBLE_DEVICES={GPU_ID} ``` before the command to run the experiment on the specific GPUs. If you set ```GPU_ID``` as ```-1```, the experiment runs on cpus.

Note that you could change the parameters of fedbalancer config file to test another parameters. 

