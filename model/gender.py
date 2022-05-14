import torch
from torch import nn
# import torch.nn.functional as F


class GenderNet(nn.Module):
    def __init__(self, do_bn=True):
        super(GenderNet, self).__init__()
        self.do_bn = do_bn
        self.bn = nn.BatchNorm1d(2, eps=1e-5)
        # self.bn = nn.BatchNorm1d(1, eps=0, affine=False, track_running_stats=False)
        self.fc = torch.nn.Linear(2, 2)
        
    def forward(self, x):
        if self.do_bn:
            x = self.bn(x)
        x = self.fc(x)
        return x