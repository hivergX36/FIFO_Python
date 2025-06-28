class fifo:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def push(self, item):
        if len(self.queue) >= self.size:
            self.queue.pop(0)  # Remove the oldest item
        self.queue.append(item)

    def pop(self):
        if not self.queue:
            return None
        return self.queue.pop(0)  # Remove and return the oldest item

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)