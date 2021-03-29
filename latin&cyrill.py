"""
Created on Sat Mar 27 2021

@author: acer
"""
from transliterate import to_latin, to_cyrillic

print("Salom siz Lotin->Kirill va Kirill->Lotin tarjimon dasturini ishlatyapsiz!")

while True:
    text = input("Trajima qilmoqchi bo'lgan matningizni kiriting:\n>> ")
    
    if text.isascii():
        print("<< " + to_cyrillic(text))
    else:
        print("<< " + to_latin(text))
    
    repeat = int(input("\nYana matn tarjima qilasizmi? ha(1)/yo'q(0)"))
    
    if repeat == 0:
        break