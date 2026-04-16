import os
import pandas as pd

# Chiedi in input i numeri delle immagini da rimuovere
print("Inserisci i numeri delle immagini da rimuovere")
print("Esempio: 1 5 12 23 45 (separati da spazi)")
print("O: 1-10 (per un range)")
print()

user_input = input("Numeri da rimuovere: ").strip()

# Parsa l'input
images_to_remove = []

for item in user_input.split():
    if '-' in item:
        # Range (es. 1-10)
        start, end = item.split('-')
        images_to_remove.extend(range(int(start), int(end) + 1))
    else:
        # Numero singolo
        images_to_remove.append(int(item))

images_to_remove = sorted(set(images_to_remove))  # Rimuovi duplicati e ordina

print(f"\nRimoverai {len(images_to_remove)} immagini: {images_to_remove}")
confirm = input("Confermi? (s/n): ").strip().lower()

if confirm != 's':
    print("Operazione annullata!")
    exit()

# Chiedi la cartella
train_path = input("Percorso della cartella (es. dataset/train_data): ").strip()
csv_path = input("Percorso del CSV (es. dataset/train_labels.csv): ").strip()

# Controlla se esistono
if not os.path.exists(train_path):
    print(f"Errore: Cartella {train_path} non trovata!")
    exit()

if not os.path.exists(csv_path):
    print(f"Avviso: CSV {csv_path} non trovato, procederò solo con la rimozione dei file")
    csv_path = None

# Rimuovi immagini e maschere
print("Rimozione immagini e maschere...")
removed_count = 0

for img_num in images_to_remove:
    img_file = f'{train_path}/img_{img_num:04d}.png'
    mask_file = f'{train_path}/mask_{img_num:04d}.png'

    # Rimuovi immagine
    if os.path.exists(img_file):
        os.remove(img_file)
        print(f"Rimosso: {img_file}")
        removed_count += 1

    # Rimuovi maschera
    if os.path.exists(mask_file):
        os.remove(mask_file)
        print(f"Rimosso: {mask_file}")

print(f"\nRimossi {removed_count} file")

# Rimuovi dal CSV
print("\nRimozione etichette dal CSV...")
if csv_path and os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    print(f"Righe prima: {len(df)}")

    # Rimuovi le righe corrispondenti
    df = df[~df.index.isin(images_to_remove)]

    print(f"Righe dopo: {len(df)}")

    # Salva il CSV aggiornato
    df.to_csv(csv_path, index=False)
    print(f"CSV aggiornato: {csv_path}")
else:
    print("CSV non trovato o non specificato!")

print("\nDone!")
