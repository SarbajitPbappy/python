class CPU:
    def __init__(self, model, speed, cores):
        self.model = model
        self.speed = speed
        self.cores = cores

    def __str__(self):
        return f"{self.model} {self.speed}"

class RAM:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"{self.size} GB"

class HARD_DISK:
    def __init__(self, cap):
        self.cap = cap

    def __str__(self):
        return f"{self.cap} GB"

class COMPUTER:
    def __init__(self, model, speed, cores, ram_size, hard_cap):
        self.cpu = CPU(model, speed, cores)
        self.ram = RAM(ram_size)
        self.hard_disk = HARD_DISK(hard_cap)

    def __str__(self):
        return f"{self.cpu} {self.ram} {self.hard_disk}"

mac = COMPUTER("Intel", 3.2, 4, 8, 500)
print(mac)
