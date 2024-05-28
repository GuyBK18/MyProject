import numpy as np
import torch
import matplotlib.pyplot as plt
import wandb
wandb.init(
        #set the wandb project where this run will be logged
        project="New2",
        resume=False,
        id=f"New2 {111}"
    )
Directory = 'Data'
Files_num = [3]
results_path = []
random_results_path = []
for num in Files_num:
    file = f'results_{num}.pth'
    results_path.append(file)
    file = f'random_results_{num}.pth'
    random_results_path.append(file)

results = []
for path in results_path:
    results.append(torch.load(Directory+'/'+path))

random_results = []
for path in random_results_path:
    random_results.append(torch.load(Directory+'/'+path))


print(results[0]['results'])
for item in results[0]['results']:
               wandb.log ({
             "result": item
                 }
               )

