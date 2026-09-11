import torch
import matplotlib.pyplot as plt

# 生成两组不同正态分布张量
tensor1 = torch.normal(mean=2.0, std=1.0, size=(10000,))
tensor2 = torch.normal(mean=6.0, std=1.5, size=(10000,))

plt.figure(figsize=(8, 5))
plt.hist(tensor1.numpy(), bins=50, alpha=0.5, label="dist_1")
plt.hist(tensor2.numpy(), bins=50, alpha=0.5, label="dist_2")
plt.legend()
plt.title("Two different normal distribution")
plt.savefig("distribution.png")
plt.close()
