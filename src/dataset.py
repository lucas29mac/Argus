import os
import cv2
import matplotlib.pyplot as plt

# Caminho para a pasta do dataset
dataset_path = "./data/val2017"

# Pegue a primeira imagem do dataset
image_files = os.listdir(dataset_path)
if image_files:
    image_path = os.path.join(dataset_path, image_files[0])
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Corrigir cores no OpenCV

    # Exibir a imagem
    plt.imshow(image)
    plt.axis("off")
    plt.show()
else:
    print("Nenhuma imagem encontrada no dataset.")
