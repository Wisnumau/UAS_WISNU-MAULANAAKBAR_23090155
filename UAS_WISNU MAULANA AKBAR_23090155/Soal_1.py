def input_data_mahasiswa():
    mahasiswa = []
    
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        
        mahasiswa.append({"NIM": nim, "Nama": nama})
        
        tambah_lagi = input("Ingin tambah lagi? (iya/tidak): ").lower()
        if tambah_lagi != 'iya':
            break
    
    print("\nData Mahasiswa:")
    for data in mahasiswa:
        print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")

if __name__ == "__main__":
    input_data_mahasiswa()
