import psutil
def get_size(bytes,suffix="8"):
    factor = 1024
    for unit in ["","K","M","G","T","p"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

svmem = psutil.virtual_memory()
print(f"Total:{get_size(svmem.total)}")
print(f"Available:{get_size(svmem.available)}")
print(f"Used:{get_size(svmem.used)}")
#print(f"Percentange:{svmem.percentange}%")

swap = psutil.swap_memory()
print("\nSwap Partition:")
print(f"Total:{get_size(swap.total)}")
#print(f"Available:{get_size(swap.available)}")
print(f"Used:{get_size(swap.used)}")
#print(f"Percentange:{swap.percentange}%")