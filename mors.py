import tkinter as tk

# Mors kodu dönüştürücü fonksiyonları
def mors_kodu_donustur():
    metin = metin_giris.get().upper()
    mors_kodu = ""
    for karakter in metin:
        if karakter == " ":
            mors_kodu += " / "
        elif karakter in morse_dict:
            mors_kodu += morse_dict[karakter] + " "
    sonuc_etiketi.config(text=mors_kodu)

def metne_donustur():
    mors_kodu = mors_giris.get()
    metin = ""
    for kod in mors_kodu.split(" "):
        if kod == "/":
            metin += " "
        elif kod in morse_dict.values():
            for karakter, mors in morse_dict.items():
                if mors == kod:
                    metin += karakter
    sonuc_etiketi.config(text=metin)

# Mors kodu sözlüğü
morse_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
    "-": "-....-", "_": "..--.-", "\"": ".-..-.", "$": "...-..-", "@": ".--.-.",
    " ": "/"
}

# Ana pencereyi oluşturma
pencere = tk.Tk()
pencere.title("Mors Kodu Dönüştürücü")
pencere.geometry("400x400") # Pencere boyutunu ayarlayabilirsiniz

# Üst bölüm
ust_cerceve = tk.Frame(pencere, padx=10, pady=10)
ust_cerceve.pack()

metin_etiketi = tk.Label(ust_cerceve, text="Metin:",bg="#ffcbdb")
metin_etiketi.pack(side="left")
metin_giris = tk.Entry(ust_cerceve)
metin_giris.pack(side="left", padx=5)

donustur_butonu = tk.Button(ust_cerceve, text="Mors Koda Dönüştür", command=mors_kodu_donustur, bg="#f5b0bd", padx=10)
donustur_butonu.pack(side="left", padx=5)

# Orta bölüm
orta_cerceve = tk.Frame(pencere, padx=10, pady=10)
orta_cerceve.pack()

mors_etiketi = tk.Label(orta_cerceve, text="Mors Kodu:",bg="#ffcbdb")
mors_etiketi.pack(side="left")
mors_giris = tk.Entry(orta_cerceve)
mors_giris.pack(side="left", padx=5)

metne_donustur_butonu = tk.Button(orta_cerceve, text="Metne Dönüştür", command=metne_donustur, bg="#f5b0bd", padx=10)
metne_donustur_butonu.pack(side="left", padx=5)

# Alt bölüm
alt_cerceve = tk.Frame(pencere, padx=10, pady=10)
alt_cerceve.pack()

sonuc_etiketi = tk.Label(alt_cerceve, text="sonuç:", wraplength=300, justify="center",bg="#ffcbdb")
sonuc_etiketi.pack()

# Arkaplan rengi ayarla
pencere.configure(bg="#ffe6f2")
ust_cerceve.configure(bg="#ffe6f2")
orta_cerceve.configure(bg="#ffe6f2")
alt_cerceve.configure(bg="#ffe6f2")

# Başlatma kodu
pencere.mainloop()
