# m8l1-portfolio-websitesi

## GitBash İndirmek
1- Bu Github deposunu local'e yani bilgisayarınıza indirebilmek için Git Bash programına ihtiyahıcınız var.
Bu linke tıklayarak indirebilirsiniz:
#### Windows kullananlar için:
https://git-scm.com/download/win
#### MacOS kullananlar için:
https://git-scm.com/download/mac
#### Linux/Unix kullananlar için:
[https://git-scm.com/download/mac](https://git-scm.com/download/linux)

## Projenizi kaydetmek istediğiniz klasöre gitmek:
1-Terminalde projenizi kaydetmek istediğiniz yere gidiniz
İşinize yarayan komutlar
`cd <klasör_ismi>` sizi klasörün içine alacak
`ls` Bulunduğunuz klasörün içindeki dosyları gösterecek 
`pwd` Bulunduğunuz klasörün adresi
`mkdir <klasör_ismi>` Yeni bir klasör oluşturmak

Önreğin, ben masaüstünde kaydetmek için bu komutları kullandım:
```
cd Desktop
mkdir Bitirme_Projesi
cd Bitirme_Projesi
```

## Github deposunu localinize indirmek

Projeyi kaydet istediğiniz klasörün içindeyseniz, aşağıdaki komutu girerek bu github deposunu bilgisayarınıza indirebilirsiniz:
```
git clone https://github.com/Kodland-Codes/m8l1-portfolio-websitesi.git
```

## Sanal ortamı aktifleştirmek ve kütüphaneleri indirmek

Projenizi VSCode'da açınız ve aşağıdaki komutu giriniz
NOT: `bilgisayarı kapatıp açtığınz zaman da bu komutu her zaman girmeniz gerekiyor`

### Mac kullananlar için: 
```
source venv/bin/activate
pip install -r requirements.txt
```

### Windows kullananlar için: 
```
venv\Scripts\activate
pip install -r requirements.txt
```


## Projeyi çalıştırmak
### Yöntem 1: VSCode terminalinden
NOT: VScode terminalinde projenin klasöründe olduğunuzdan ve doğru sanal ortamı kullandığınızdan emin olunuz.
Bu konmutu VSCode terminalinde yazarak projeyi çalıştırabilirsiniz:
```
python main.py
```

### Yöntem 2: VScode çalıştır butonundan
Eğer bu yöntemi kullanmak istiyorsanız VSCode'da kullandığınız İnterpreter'ın VENV (Sanal ortamımızın ismi) olması gerekiyor
1- `CTRL + SHIFT + P`'ye tıklayınız
2- Python Select Interpreter'e tıklayınız
3- VENV adındaki sanal ortamı seçiniz



