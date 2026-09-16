#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:24:39 2026

@author: franka
"""

print("Dieses Programm verschlüsstelt einen Text mit dem Caesar-Chiffre. Der verschlüsselte Text wird nur in Kleinbuchstaben ausgegeben.")
eingabe = input("Geben Sie einen Text zum Verschlüsseln ein.\n\n")
step = int(input("Geben Sie eine Zahl zwischen 1 und 25 zur Verschlüsselung an.\n\n"))

text = eingabe.lower()
text_neu = ""

for buchstabe in text:
    if buchstabe.isalpha():
        stelle = ord(buchstabe)
        stelle_neu = (stelle + step - 97) % 26 + 97 
        buchstabe = chr(stelle_neu)
    text_neu = text_neu + buchstabe

print(text_neu)