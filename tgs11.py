import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}
df = pd.DataFrame(data)

# Pertanyaan 1: Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
persentase = 5 / 100  # 5%
Peningkatan_gaji = lambda gaji: gaji * (1 + persentase)

for i in range(len(df['Gaji'])):
    df.loc[i, 'Peningkatan-Gaji'] = Peningkatan_gaji(df.loc[i, 'Gaji'])


# Pertanyaan 2: Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print(f"DataFrame setelah diperbarui:\n{df}")
df['Perubahan-5%'] = df['Peningkatan-Gaji'] - df['Gaji']
print(f"\nRingkasan Perubahan:\n{df}")


# Pertanyaan 3: Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
persentase_tambahan = 2 / 100  # 2%
Peningkatan_gaji_usia = lambda gaji, usia: gaji * (1 + persentase_tambahan) if (usia > 30) else gaji

for i in range(len(df['Gaji'])):
    df.loc[i, 'Peningkatan-Gaji-Usia'] = Peningkatan_gaji_usia(df.loc[i, 'Peningkatan-Gaji'], df.loc[i, 'Usia'])


# Pertanyaan 4: Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print(f"\nDataFrame setelah diperbarui:\n{df}")
df['Perubahan-2%'] = df['Peningkatan-Gaji-Usia'] - df['Peningkatan-Gaji']
print(f"\nRingkasan Perubahan:\n{df}")


"""  Catatan:
Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
Pastikan untuk menyimpan hasil perubahan pada DataFrame.
Tampilkan hasil dan ringkasan dengan jelas.
Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita. """