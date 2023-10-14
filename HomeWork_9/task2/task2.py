import sys

print(f'Before directory: {sys.path}')
sys.path.pop(0)
print(f'After directory: {sys.path}')
