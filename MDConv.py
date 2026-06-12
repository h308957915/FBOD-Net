class MDConv(nn.Module):
    def __init__(self, dim, k=1, s=1, p=None, g=1, d=1, act=True):
        super().__init__()
        self.conv0 = Conv(dim, dim // 2, 1)
        self.conv1 = Conv(dim // 2, dim // 2, 3, d=2)
        self.conv2 = Conv(dim // 2, dim // 2, 3, d=3)
        self.conv3 = Conv(dim // 2, dim // 2, 3, d=4)
        self.conv4 = Conv(dim // 2, dim, 1)
    def forward(self, x):
        x1 = self.conv0(x)
        x2 = self.conv1(x1)
        x3 = self.conv2(x2)
        x4 = self.conv3(x3)
        x5 = self.conv4(x4)
        x6 = x5 + x
        return x6