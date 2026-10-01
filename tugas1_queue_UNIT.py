import unittest
from collections import deque

class Antrean:
    def __init__(self):
        self.data = deque()

    def enqueue(self, mahasiswa):
        self.data.append(mahasiswa)

    def dequeue(self):
        if self.data:
            return self.data.popleft()

    def peek(self):
        if self.data:
            return self.data[0]

    def is_empty(self):
        return len(self.data) == 0


class TestAntrean(unittest.TestCase):

    # 1. Pengujian Penambahan Data
    def test_enqueue(self):
        antrean = Antrean()
        antrean.enqueue("Ahmad")
        antrean.enqueue("Budi")
        self.assertEqual(list(antrean.data), ["Ahmad", "Budi"])

    # 2. Pengujian Penghapusan Data
    def test_dequeue(self):
        antrean = Antrean()
        antrean.enqueue("Ahmad")
        antrean.enqueue("Budi")
        self.assertEqual(antrean.dequeue(), "Ahmad")

    # 3. Pengujian Melihat Data Terdepan
    def test_peek(self):
        antrean = Antrean()
        antrean.enqueue("Ahmad")
        antrean.enqueue("Budi")
        self.assertEqual(antrean.peek(), "Ahmad")

    # 4. Pengujian Kondisi Kosong
    def test_is_empty(self):
        antrean = Antrean()
        self.assertTrue(antrean.is_empty())
        antrean.enqueue("Citra")
        self.assertFalse(antrean.is_empty())


if __name__ == "__main__":
    unittest.main(verbosity=2)