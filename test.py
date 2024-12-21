import os

print("consola-1.0") 
def basit_yapay_zeka(input_veri):
    if input_veri.lower() == "ver":
        return "VER= 1.0"
    elif input_veri.lower() == "ver -i":
        return "Ahmet Sabri Azaklı, the creator."
    elif input_veri.lower() == "usermod":
        kullanici_adi = os.getlogin()  # Kullanıcı adını alıyoruz
    elif input_veri.lower() == "usertree":
        xde_s = os.getcwd()
    elif input_veri.lower() == "link":
        xdg_s = os.listdir()
    else:
        return "Bad command."
    


# Kullanıcıdan giriş alıyoruz
kullanici_girisi = input("# ")

# Fonksiyonu çağırıyoruz
cevap = basit_yapay_zeka(kullanici_girisi)

# Cevabı yazdırıyoruz
print(cevap)
