import torch.nn as nn

architecture_config = [
    (7,64,2,3) #(kernel size,number of filters as output, stride, padding)
    , "M"
    , (3,192,1,1)
    , "M"
    , (1,128,1,0)
    , (3,256,1,1)
    , (1,256,1,0)
    , (3,512,1,1)
    , "M"
    , [(1,256,1,0),(3,512,1,1),4] # tuple1,tuple2,repeat]
    , (1,512,1,0)
    , (3,1024,1,1)
    , "M"
    , [(1,512,1,0),(3,1024,1,1),2]
    , (3,1024,1,1)
    , (3,1024,2,1)
    , (3,1024,1,1)
    , (3,1024,1,1)
]

class CNNBlock(nn.Module):
    def __init__(self,in_channels,out_channels,**kwargs):
        super(CNNBlock,self).__init__()
        self.conv = nn.Conv2d(in_channels,out_channels,bias=False,**kwargs)
        self.batchnorm = nn.BatchNorm2d(out_channels)
        self.leakyrelu = nn.LeakyReLU(0.1)
    
    def forward(self,x):
        return self.leakyrelu(self.batchnorm(self.conv(x)))