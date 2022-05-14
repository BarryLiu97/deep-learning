import torch
from torch import nn
# import torch.nn.functional as F


class GenderNet(nn.Module):
    def __init__(self):
        super(GenderNet, self).__init__()
        self.fc = torch.nn.Linear(2, 2)
        
    def forward(self, x):
        x = self.fc(x)
        return x