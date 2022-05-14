from torch.utils.data import Dataset


class MNISTDataset(Dataset):
    
    def __init__(self, img_dir, annot_path, transform=None, target_transform=None):
        import pandas as pd
        
        self.img_dir = img_dir
        self.annot = pd.read_csv(annot_path, header=None, sep='\t')
        self.transform = transform
        self.target_transform = target_transform
               
    def __getitem__(self, idx):
        import os.path as op
        import cv2
        
        img_path = op.join(self.img_dir, self.annot.iloc[idx, 0])
        target = self.annot.iloc[idx, 1]
        img = cv2.imread(img_path, cv2.COLOR_BGR2RGB)
        
        if self.transform:
            img = self.transform(img)
        if self.target_transform:
            target = self.target_transform(target)
        
        return img, target
        
    def __len__(self):
        return len(self.annot)