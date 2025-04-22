pip install opencv-python

import cv2
import os

# Kullanıcının masaüstü yolu (platformdan bağımsız)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Burada kendi görsel adını yaz!
image_filename = "add image.jpeg"

# Görselin tam yolu
image_path = os.path.join(desktop_path, image_filename)

# Görseli oku
img = cv2.imread(image_path)

# Görsel okunamadıysa uyarı ver ve çık
if img is None:
    print(f"Görsel yüklenemedi! '{image_path}' yolunu kontrol et.")
    exit()

# Gri tonlamaya çevir
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Negatifini al
inverted_image = 255 - gray_image

# Gaussian Blur uygula
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# Blur'lu resmi tersine çevir
inverted_blurred = 255 - blurred

# Çizim efektini oluştur
sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Sonucu masaüstüne kaydet
output_path = os.path.join(desktop_path, "cizim_hali.jpeg")
cv2.imwrite(output_path, sketch)

# Sonucu göster
cv2.imshow("Çizim Hali", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Çizim başarıyla oluşturuldu: {output_path}")
