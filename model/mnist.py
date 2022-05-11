import torch
from torch import nn
import torch.nn.functional as F


class BaseModel(nn.Module):
    def __init__(self, input_size=3):
        super(BaseModel, self).__init__()
        self.conv1 = torch.nn.Conv2d(input_size, 10, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(10, 20, kernel_size=5)
        self.pooling = torch.nn.MaxPool2d(2)
        self.fc = torch.nn.Linear(320, 10)# 320是经过maxpooling后的元素数量：20*4*4
        
    def forward(self, x):
        batch_size = x.size(0)

        x = F.relu(self.pooling(self.conv1(x)))  # 先relu再池化与先池化再relu区别不大？
        x = F.relu(self.pooling(self.conv2(x)))
        x = x.view(batch_size, -1) # flatten
        x = self.fc(x)
        return x
    

class Model(nn.Module):
    
    def __init__(self, input_size=3, init=True):
        super(Model, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(input_size, 32, kernel_size=3, stride=1),
            nn.BatchNorm2d(32),  # 加了batchnorm 收敛速度明显加快
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, stride=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.dense = nn.Sequential(
            nn.Linear(1600, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )
        
        if init:
            for m in self.modules():
                if isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
                    nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='leaky_relu')
                elif isinstance(m, nn.BatchNorm2d):
                    nn.init.constant_(m.weight, 1)
                    nn.init.constant_(m.bias, 0)
        
    def forward(self, x):
        batch_size = x.size(0)
        
        block1 = self.conv1(x)
        block2 = self.conv2(block1)
        block2 = block2.view(batch_size, -1) # flatten
        # print(block2.shape[1])
        block3 = self.dense(block2)
        return block3
