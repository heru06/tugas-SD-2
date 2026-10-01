import unittest

class Undo:
    def __init__(self):
        self.riwayat = []

    def push(self, data):
        self.riwayat.append(data)

    def pop(self):
        if self.riwayat:
            return self.riwayat.pop()

    def peek(self):
        if self.riwayat:
            return self.riwayat[-1]

    def is_empty(self):
        return len(self.riwayat) == 0


class TestUndo(unittest.TestCase):

    # 1. Pengujian Penambahan Data
    def test_push(self):
        undo = Undo()
        undo.push("Ahmad")
        undo.push("Budi")
        self.assertEqual(undo.riwayat, ["Ahmad", "Budi"])

    # 2. Pengujian Penghapusan Data
    def test_pop(self):
        undo = Undo()
        undo.push("Ahmad")
        undo.push("Budi")
        self.assertEqual(undo.pop(), "Budi")

    # 3. Pengujian Melihat Data Teratas
    def test_peek(self):
        undo = Undo()
        undo.push("Ahmad")
        undo.push("Budi")
        self.assertEqual(undo.peek(), "Budi")

    # 4. Pengujian Kondisi Kosong
    def test_is_empty(self):
        undo = Undo()
        self.assertTrue(undo.is_empty())
        undo.push("Citra")
        self.assertFalse(undo.is_empty())


if __name__ == "__main__":
    unittest.main(verbosity=2)