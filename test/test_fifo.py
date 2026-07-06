import pytest
import src.fifo as f


def test_fifo_size():
    fifo = f.fifo(0)
    fifo.parse_data("data/data1.txt")
    assert fifo.size == 144


def test_fifo_first_number():
    fifo = f.fifo(0)
    fifo.parse_data("data/data1.txt")
    assert fifo.queue[0] == 39
