# Course Project
Implement a data-similarity and clustering based client selection method for fault-tolerance and efficiency in FL.
Based on original **FLASH** and **FedBalancer** Framework.



## Datasets

We evaluated based on five datasets: ```FEMNIST```,```Shakespeare```.

## How to Run 


1. Go to directory of respective dataset in `data/` for instructions on generating the benchmark dataset
2. Run (please refer to the list of config files in the subdirectory with respective dataset name in ```configs/```, it contains all the config files for the experiment)
```
$ cd models/

# example: python main.py --config=$config-path
```

Add ```CUDA_VISIBLE_DEVICES={GPU_ID} ``` before the command to run the experiment on the specific GPUs. If you set ```GPU_ID``` as ```-1```, the experiment runs on cpus.


