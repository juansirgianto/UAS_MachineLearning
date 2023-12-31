import torch
import torch.nn as nn
import torch.nn.functional as F

#option 1
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(NeuralNet, self).__init__()
        self.linear1= nn.Linear(input_size, hidden_size)
        self.relu= nn.ReLU()
        nn.Sigmoid
        nn.Softmax
        nn.Tanh
        nn.LeakyReLU
        self.linear2= nn.Linear(hidden_size, 1)
        self.sigmoid= nn.Sigmoid()
    
    def forward(self, x):
        out= self.linear1(x)
        out= self.relu(out)
        out= self.linear2(out)
        out= self.sigmoid(out)
        return out
    
#option 2
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(NeuralNet, self).__init__()
        self.linear1= nn.Linear(input_size, hidden_size)
        self.linear2= nn.Linear(hidden_size, 1)
    
    def forward(self, x):
        F.leaky_relu()
        out= torch.relu(self.linear1(x))
        out= torch.sigmoid(self.linear2(out))
        torch.softmax
        torch.tanh
        
        return out