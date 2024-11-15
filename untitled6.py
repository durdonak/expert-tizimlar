# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Sq9UAhnV03RXdY6vYGYdeH0zdEAS4M8b
"""

def tashxis(belgi):
  if belgi=="Istima":
    return "parasetamol iching"
  elif belgi=="bosh og'rig'i":
    return "Bolnol iching"
  elif belgi=="Tish og'rig'i":
    return "Quepen iching"
  else:
    return "SHifokorga murojaat qiling"


belgi = input("Kasallik belgisini kiriting")
print(tashxis(belgi))

!pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
def kitob(nomi):
    match nomi:
        case 1:
            return "Taylor Jenkins Reid"
        case 2:
            return "James Clear"
        case 3:
            return "Matt Haig"
        case 4:
            return "Alex Michaelides"
        case 5:
            return "Colleen Hoover"
        case 6:
            return "Tara Westover"
        case 7:
            return "Don Miguel Ruiz"
        case 8:
            return "Colleen Hoover"
        case _:
            return "Invalid choice. Please enter a number between 1 and 8."


try:
    nom = int(input(f"""
1. The Seven Husbands of Evelyn Hugo
2. Atomic Habits
3. The Midnight Library
4. The Silent Patient
5. Verity
6. Educated
7. The Four Agreements
8. It Ends with Us
Choose a book (1-8): """))

    print(kitob(nom))

except ValueError:
    print("Please enter a valid number.")

import cv2
import matplotlib.pyplot as plt
import requests
import numpy as np

def kitob(nomi):
    books = {
        1: ("Taylor Jenkins Reid", "https://images-na.ssl-images-amazon.com/images/I/81WcnNQ-TBL.jpg"),
        2: ("James Clear", "https://m.media-amazon.com/images/I/81ANaVZk5LL._SY466_.jpg"),
        3: ("Matt Haig", "https://m.media-amazon.com/images/I/519oM5hbD1L._SY445_SX342_.jpg"),
        4: ("Alex Michaelides", "https://m.media-amazon.com/images/I/41bsvxNUSdL._SY445_SX342_.jpg"),
        5: ("Colleen Hoover", "https://m.media-amazon.com/images/I/41qVSyYeQVL._SY445_SX342_.jpg"),
        6: ("Tara Westover", "https://m.media-amazon.com/images/I/41GE5-l2ptL._SY445_SX342_.jpg"),
        7: ("Don Miguel Ruiz", "https://m.media-amazon.com/images/I/517MwXYNucL._SY445_SX342_.jpg"),
        8: ("Colleen Hoover", "https://m.media-amazon.com/images/I/51LCO+afezL._SY445_SX342_.jpg"),
    }

    if nomi in books:
        author, image_url = books[nomi]
        return author, image_url
    else:
        return None, None

def show_book_info(book_choice):
    author, image_url = kitob(book_choice)

    if author is not None:

        try:
            img_data = requests.get(image_url).content
            img_array = np.frombuffer(img_data, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            if img is None:
                print("Error loading image.")
                return


            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


            plt.figure(figsize=(10, 8))
            plt.imshow(img_rgb)
            plt.title(f"Book: {image_url.split('/')[-1].split('.')[0]} \nAuthor: {author}", fontsize=16)
            plt.axis('off')
            plt.show()
        except Exception as e:
            print(f"Error loading image from URL: {e}")
    else:
        print("Invalid choice or no image available.")

try:
    nom = int(input(f"""
1. The Seven Husbands of Evelyn Hugo
2. Atomic Habits
3. The Midnight Library
4. The Silent Patient
5. Verity
6. Educated
7. The Four Agreements
8. It Ends with Us
Choose a book (1-8): """))

    show_book_info(nom)

except ValueError:
    print("Please enter a valid number.")