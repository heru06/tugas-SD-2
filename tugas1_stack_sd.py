# ==========================================
# PROGRAM UNDO MENGGUNAKAN STACK
# ==========================================

# Membuat class Undo
class Undo:
    def __init__(self):
        # List digunakan sebagai Stack untuk menyimpan riwayat
        self.riwayat = []

    # PUSH: menambahkan data ke Stack
    def push(self, data):
        self.riwayat.append(data)

    # POP: menghapus data paling terakhir/teratas
    def pop(self):
        if self.riwayat:
            return self.riwayat.pop()
        return None

    # PEEK: melihat data paling terakhir tanpa menghapusnya
    def peek(self):
        if self.riwayat:
            return self.riwayat[-1]
        return None

    # IS_EMPTY: memeriksa apakah Stack kosong
    def is_empty(self):
        return len(self.riwayat) == 0


# Membuat objek Undo
undo = Undo()

# ==========================================
# 1. PENAMBAHAN DATA (PUSH)
# ==========================================
undo.push("Ahmad")
undo.push("Budi")
undo.push("Citra")
undo.push("Deni")
undo.push("Eka")

print("Setelah Push :", undo.riwayat)

# ==========================================
# 2. MELIHAT DATA TERATAS (PEEK)
# ==========================================
print("Data Teratas :", undo.peek())

# ==========================================
# 3. PENGHAPUSAN DATA (POP)
# ==========================================
print("Data dihapus :", undo.pop())
print("Setelah Pop  :", undo.riwayat)

# ==========================================
# 4. MEMERIKSA KONDISI KOSONG (IS_EMPTY)
# ==========================================
print("Stack kosong :", undo.is_empty())