# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nlZ4vG8W1TxyOdDJWRjUeMnheeTIUFmU
"""

import pandas as pd
baza={
    "fish":[  "qadanova Zulayho ","Xalilov Durbek "    ],
      "fan nomi": [   "suniy intelekt " , "suniy intelekt "   ],
      "mashg'ulot turi" :[ "amaliy mashgulot" ,"maruza"   ],
    "kafedrasi ":["axbarot texnologyalari ", "axbarot texnologyalari" ],
}
dp=pd.DataFrame (baza)
print ( dp)

import pandas as pd
baza={
    "fish":[  "qadanova Zulayho ","Xalilov Durbek " ,"Abdullayeva Moxigul ","Xontorayev Sardorbek ","Turdimatov Mamirjon ","Araboyev Alisher " ,"Jurayeva Gulnozaxon" ],
      "fan nomi": [   "suniy intelekt " , "suniy intelekt " ,"Malumotlar tuzilmasi " ,"Malumotlar tuzilmasi ","kiber hafsizlik ", "kiber hafsizlik" ,"ELEKTRON SXEMA"],
      "mashg'ulot turi" :[ "amaliy mashgulot" ,"maruza","amaliy ", "maruza", "amaliy ", "amaliy ","amaliy "  ],
    "kafedrasi ":["axbarot texnologyalari ", "axbarot texnologyalari" ,"TABIY FANLAR","axbarot texnologyalari","axbarot texnologyalari","axbarot texnologyalari","KISIF"],
}
dp=pd.DataFrame (baza)
print ( dp)

dp.to_excel("teachers.xlsx")

from google.colab.patches import cv2_imshow
import cv2
def yoshi(belgi) :
  if belgi == "Mahmudov Asliddin ":
    rasm1=cv2.imread("1.jpg")
    cv2_imshow(rasm1)
    return " 19 "
  elif belgi =="Raxmatov Bahodirjon ":
    rasm1=cv2.imread("2.jpg")
    cv2_imshow(rasm1)
    return " 18 "
  elif belgi  == " Matraimov Isomoddin ":
    rasm1=cv2.imread("3.jpg")
    cv2_imshow(rasm1)
    return "25"
  elif belgi == "Sodiqjonov Dilmurod":
    rasm1=cv2.imread("4.jpg")
    cv2_imshow(rasm1)
    return "21 "
  elif belgi == "Mahmudov Dilmurod":
    rasm1=cv2.imread("5.jpg")
    cv2_imshow(rasm1)
    return "21 "
  elif belgi == "Ikromov Dilmurod":
    rasm1=cv2.imread("6.jpg")
    cv2_imshow(rasm1)
    return "24 "
  else:
   return " yoshini chiqorish  "
belgi= input (" Familya Ismini kiriting  ")
natija=yoshi(belgi)
print (natija)