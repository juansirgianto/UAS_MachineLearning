import torch

weight = torch.ones(4, requires_grad=True)

for epoch in range(3):
    model_output=(weight*3).sum()
    model_output.backward()
    print(weight.grad)
    weight.grad.zero_()
