sozluk = {
            "AFK": "away from keyboard (klavyeden uzakta)",
            "solo": "tek başına üst veya orta koridor tutmak",
            "nickname": "kullanıcı adı",
            "google": "en sık kullanılan arama motoru",
            "steam": "oyun istemcisi"
    }

kelime = input("Anlamadığınız bir kelime yazın (doğru yazdığnızdan emin olun): ")

if kelime in sozluk.keys():
    print("kelime sozlukte var:", sozluk[kelime])
    
else:
    print("kelime sozlukte yok")
