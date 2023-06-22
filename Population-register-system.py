#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import sqlite3


class nufusKayit(QDialog):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Nüfus Kayıt Programı")
        grid = QGridLayout()
        #Sol kısım
        grid.addWidget(QLabel("Ad:"),0,0)
        grid.addWidget(QLabel("Soyad"),1,0)
        grid.addWidget(QLabel("T.C. Kimlik No:"),2,0)
        grid.addWidget(QLabel("Doğum Yeri:"),3,0)
        grid.addWidget(QLabel("Cinsiyet"),4,0)
        grid.addWidget(QLabel("Doğum Tarihi:"),5,0)
        
        
        self.ad = QLineEdit()
        self.soyad = QLineEdit()
        self.tc_no = QLineEdit()
        self.memleket = QLineEdit()
        self.tarih = QDateEdit()
        
        self.erkek = QRadioButton("Erkek")
        self.kadin = QRadioButton("Kadın")
        self.cinsiyet = QButtonGroup()
        self.cinsiyet.addButton(self.erkek)
        self.cinsiyet.addButton(self.kadin)
        
        self.temizle = QPushButton("Temizle")
        self.kaydet = QPushButton("Kaydet")
        self.temizle.clicked.connect(self.temizleme)
        self.kaydet.clicked.connect(self.kaydetme)
        
        
        grid.addWidget(self.ad,0,1,1,2)
        grid.addWidget(self.soyad,1,1,1,2)
        grid.addWidget(self.tc_no,2,1,1,2)
        grid.addWidget(self.memleket,3,1,1,2)
        grid.addWidget(self.erkek,4,1)
        grid.addWidget(self.kadin,4,2)
        grid.addWidget(self.tarih,5,1)
        grid.addWidget(self.kaydet,6,1)
        grid.addWidget(self.temizle,6,2)
        # Orta kısım
        self.kayit_aktar = QPushButton("Kayıt Aktar")
        self.kayit_aktar.clicked.connect(self.kayit_aktarma)
        grid.addWidget(self.kayit_aktar,3,3)
        
        #Sağ kısım
        grid.addWidget(QLabel("Ad:"),0,4)
        grid.addWidget(QLabel("Soyad:"),1,4)
        grid.addWidget(QLabel("T.C. Kimlik No:"),2,4)
        grid.addWidget(QLabel("Doğum Yeri:"),3,4)
        grid.addWidget(QLabel("Cinsiyet"),4,4)
        grid.addWidget(QLabel("Doğum Tarihi:"),5,4)
        
        self.adLabel = QLabel("")
        self.soyadLabel = QLabel("")
        self.tcLabel = QLabel("")
        self.memleketLabel = QLabel("")
        self.cinsiyetLabel = QLabel("")
        self.tarihLabel = QLabel("")
        
        grid.addWidget(self.adLabel,0,5)
        grid.addWidget(self.soyadLabel,1,5)
        grid.addWidget(self.tcLabel,2,5)
        grid.addWidget(self.memleketLabel,3,5)
        grid.addWidget(self.cinsiyetLabel,4,5)
        grid.addWidget(self.tarihLabel,5,5)
        
        self.setLayout(grid)
        self.show()
        
        
    def temizleme(self):
        self.ad.clear()
        self.soyad.clear()
        self.tc_no.clear()
        self.memleket.clear()
        self.tarih.clear()
        
        self.adLabel.setText("")
        self.soyadLabel.setText("")
        self.tcLabel.setText("")
        self.memleketLabel.setText("")
        self.cinsiyetLabel.setText("")
        self.tarihLabel.setText("")
        
    def kaydetme(self):
        ad = self.ad.text()
        soyad = self.soyad.text()
        kimlik = int(self.tc_no.text())
        memleket = self.memleket.text()
        cinsiyet = ""
        if self.erkek.isChecked() == True:
            cinsiyet = "Erkek"
        else:
            cinsiyet = "Kadın"
        t = self.tarih.date()
        tarih =t.toPyDate()
        tarih = str(tarih)
        baglanti = sqlite3.connect("nufus_bilgileri.db")
        isaretci = baglanti.cursor()
        isaretci.execute("INSERT INTO nufus_bilgileri(ad,soyad,tc,dogum_yeri,cinsiyet,dogum_tarihi) VALUES(?,?,?,?,?,?)",(ad,soyad,kimlik,memleket,cinsiyet,tarih))
        baglanti.commit()
        baglanti.close()
        
    def kayit_aktarma(self):
        
        ad = self.ad.text()
        soyad = self.soyad.text()
        kimlik = int(self.tc_no.text())
        memleket = self.memleket.text()
        cinsiyet = ""
        if self.erkek.isChecked() == True:
            cinsiyet = "Erkek"
        elif self.kadin.isChecked() == True:
            cinsiyet = "Kadın"
        t = self.tarih.date()
        tarih =t.toPyDate()
        tarih = str(tarih)
        self.adLabel.setText(ad)
        self.soyadLabel.setText(soyad)
        self.tcLabel.setText(f"{kimlik}")
        self.memleketLabel.setText(memleket)
        self.cinsiyetLabel.setText(cinsiyet)
        self.tarihLabel.setText(tarih)

uygulama = QApplication(sys.argv)
pencere = nufusKayit()

sys.exit(uygulama.exec_())


# In[ ]:


# def kaydetme(self):
#         kod = self.urun_kodu.text()
#         ad = self.urun_ad.text()
#         fiyat = self.urun_fiyati.text()
#         miktar = self.urun_miktari.text()
#         baglanti = mysql.conector.connect(user = "root",password = "",host = "localhost",database = "urun")
#         isaretci = baglanti.cursor()
#         isaretci.execute("""INSERT INTO urun(urun_kodu,urun_adi,urun_miktari,urun_fiyati) VALUES("%s","%s","%s","%s","%s")"""
#                          %(kod,ad,fiyat,miktar))
#         baglanti.commit()
#         baglanti.close()


# In[ ]:


# mydb = mysql.connector.connect(user="root", password="", host = "localhost", database="urun")
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE urun_bilgileri(urun_kodu INTEGER PRIMARY KEY, urun_adi VARCHAR(255), urun_miktari VARCHAR(255), urun_fiyati VARCHAR(255))")


# In[2]:


# import sqlite3

# baglanti = sqlite3.connect("nufus_bilgileri.db")
# imlec = baglanti.cursor()

# imlec.execute("""CREATE TABLE IF NOT EXISTS nufus_bilgileri(ad VARCHAR(50),soyad VARCHAR(50),tc VARCHAR(50), dogum_yeri VARCHAR(50), cinsiyet VARCHAR(10),dogum_tarihi VARCHAR(50))""")
# baglanti.commit()
# baglanti.close()


# In[ ]:




