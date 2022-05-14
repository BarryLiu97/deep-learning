import torch
from torch.utils.data import Dataset


class GenderDataset(Dataset):
    
    def __init__(self, fname, transform=None, target_transform=None):
        import pandas as pd
        
        self.data = pd.read_csv(fname, header=None, sep=' ')
        self.transform = transform
        self.target_transform = target_transform
               
    def __getitem__(self, idx):
        import os.path as op
        import cv2
        
        feature = self.data.iloc[idx, : 2]
        target = self.data.iloc[idx, 2]
        
        if self.transform is not None:
            feature = self.transform(feature)
            print('here')
        if self.target_transform is not None:
            target = self.target_transform(target)
        
        return torch.FloatTensor(feature), target
        
    def __len__(self):
        return len(self.data)