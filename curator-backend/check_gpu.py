import torch

print(f'CUDA disponible: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'GPU: {torch.cuda.get_device_name(0)}')
    print(f'VRAM totale: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB')
else:
    print('GPU: None')
