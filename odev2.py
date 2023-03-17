## Hafta 2 2.Ders Odev

sinifListesi = ["Memati Baş","Polat Alemdar", "Abdülhey Çoban"]

print(f"Sınıf Mevcudu: {len(sinifListesi)}")
ekle = str(input("Adınızı ve soy adınızı giriniz"))
sinifListesi.append(ekle)

print(sinifListesi)
print(f"Sınıf Mevcudu: {len(sinifListesi)}")

sil = str(input("Silmek İstediğiniz Öğrenci Adını giriniz"))
sinifListesi.remove(sil)
print(sinifListesi)

sinifListesi.extend(["Cahit Kaya","Güllü Erhan"])


for list in sinifListesi:
    print(list)





