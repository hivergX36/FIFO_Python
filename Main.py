from fifo import *

fifo_instance = fifo(5)

fifo_instance.parse_data("data1.txt")
print("size:",fifo_instance.size)
print("fifo:", fifo_instance.queue)