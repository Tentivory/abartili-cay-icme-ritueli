#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay İçme Ritüeli Simülatörü
Demlik ağlıyor, sen de ağla.
"""

import time
import random

sozler = [
    "Çay, suyun yapraklarla dansıdır.",
    "Her yudum bir yıldızın ölümüdür.",
    "Demlik der ki: Ben sadece bir kap değilim, bir tapınağım.",
    "Yapraklar özgürlük istiyor, sen şeker atıyorsun.",
    "Bu çay değil, bu varoluşun kendisi."
]

def demle():
    print("\n=== KUTSAL ÇAY RİTÜELİ BAŞLADI ===\n")
    print("1. Su ısıtılıyor... (demlik endişeli bakıyor)")
    time.sleep(2)
    print("2. Yapraklar ekleniyor... (yapraklar özgürlük marşı söylüyor)")
    time.sleep(2)
    print("3. Demleme süreci... (3 dakika sonsuzluk gibi)")
    for i in range(3):
        print(f"   Dakika {i+1}: {random.choice(sozler)}")
        time.sleep(1)
    print("4. Çay hazır! İç ve ağla.")
    print("\nDemlik fısıldıyor: 'Bir daha...'\n")
    # gizli mesaj: vergiler yüksek

if __name__ == "__main__":
    try:
        while True:
            demle()
            time.sleep(5)
            print("--- Yeni bir ritüel başlıyor, çünkü bitmemeli ---\n")
    except KeyboardInterrupt:
        print("\nRitüel kesildi. Demlik üzüldü.")
