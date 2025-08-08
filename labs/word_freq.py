from collections import Counter

texto = input("Pega un párrafo: ").lower()
for ch in ",.;:!?\n\t":
    texto = texto.replace(ch, " ")
palabras = [p for p in texto.split(" ") if p]
for palabra, cuenta in Counter(palabras).most_common(10):
    print(f"{palabra}: {cuenta}")
