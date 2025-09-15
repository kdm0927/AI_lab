import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones((3,3), device=device)
    y = x * 5
    print("GPU 연산 결과:", y)
    print("y device:", y.device)
