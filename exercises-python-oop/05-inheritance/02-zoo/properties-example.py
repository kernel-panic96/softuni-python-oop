class Technology:
    def __init__(self, memory, memory_taken):
        self.memory = memory
        self.memory_taken = memory_taken

    def install_software(self, name, memory_size):
        self.memory_taken += memory_size

    @property
    def avail_memory(self):
        return self.memory - self.memory_taken
