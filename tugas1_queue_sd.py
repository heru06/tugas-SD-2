from collections import deque


# ==========================================
# STRUKTUR DATA ANTREAN MAHASISWA
# ==========================================

class AntreanMahasiswa:

    def __init__(self):
        self.antrean = deque()

    # ======================================
    # ENQUEUE - PENAMBAHAN DATA
    # ======================================

    def enqueue(self, mahasiswa):
        self.antrean.append(mahasiswa)
        print(f"Data '{mahasiswa}' berhasil ditambahkan ke antrean.")

    # ======================================
    # DEQUEUE - PENGHAPUSAN DATA
    # ======================================

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong, tidak ada mahasiswa yang dilayani.")
            return None

        mahasiswa = self.antrean.popleft()
        print(f"Mahasiswa '{mahasiswa}' telah dilayani.")
        return mahasiswa

    # ======================================
    # PEEK - MELIHAT DATA TERDEPAN
    # ======================================

    def peek(self):
        if self.is_empty():
            print("Antrean kosong, tidak ada data terdepan.")
            return None

        mahasiswa = self.antrean[0]
        print(f"Mahasiswa terdepan adalah '{mahasiswa}'.")
        return mahasiswa

    # ======================================
    # ISEMPTY - MEMERIKSA KONDISI KOSONG
    # ======================================

    def is_empty(self):
        return len(self.antrean) == 0

    # ======================================
    # MENAMPILKAN SELURUH ANTREAN
    # ======================================

    def tampilkan(self):
        if self.is_empty():
            print("Antrean: []")
        else:
            print("Antrean:")
            for nomor, mahasiswa in enumerate(self.antrean, start=1):
                print(f"{nomor}. {mahasiswa}")


# ==========================================
# PROGRAM UTAMA
# ==========================================

antrean = AntreanMahasiswa()


print("==========================================")
print("       SISTEM ANTREAN MAHASISWA")
print("==========================================")


# ==========================================
# 1. ENQUEUE / PENAMBAHAN DATA
# ==========================================

print("\n=== 1. ENQUEUE - PENAMBAHAN DATA ===")

antrean.enqueue("001 - Ahmad")
antrean.enqueue("002 - Budi")
antrean.enqueue("003 - Citra")
antrean.enqueue("004 - Deni")
antrean.enqueue("005 - Eka")

print("\nKondisi antrean setelah penambahan:")
antrean.tampilkan()


# ==========================================
# 2. PEEK / MELIHAT DATA TERDEPAN
# ==========================================

print("\n=== 2. PEEK - MELIHAT DATA TERDEPAN ===")

antrean.peek()

print("\nKondisi antrean setelah Peek:")
antrean.tampilkan()


# ==========================================
# 3. DEQUEUE / PENGHAPUSAN DATA
# ==========================================

print("\n=== 3. DEQUEUE - PENGHAPUSAN DATA ===")

antrean.dequeue()

print("\nKondisi antrean setelah Dequeue:")
antrean.tampilkan()


# ==========================================
# 4. ISEMPTY / MEMERIKSA KONDISI KOSONG
# ==========================================

print("\n=== 4. ISEMPTY - MEMERIKSA KONDISI KOSONG ===")

if antrean.is_empty():
    print("Status: Antrean kosong.")
else:
    print("Status: Antrean masih memiliki data.")

print("Nilai is_empty():", antrean.is_empty())