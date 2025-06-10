# Leaf Classification

Proyek ini bertujuan untuk mengklasifikasikan jenis daun menggunakan deep learning dengan berbagai arsitektur CNN. Terdapat dua jenis preprocessing: standar dan multicolor (khusus daun Dracaena/bambu rezeki putih).

---

## Preprocessing

### 1. Preprocessing Standar
Digunakan untuk sebagian besar daun:
- **Cropping & Rotate:** Memotong dan merotasi gambar agar objek daun terpusat.
- **Brightening:** Meningkatkan kecerahan gambar.
- **Median Blur (Denoising):** Mengurangi noise pada gambar.
- **Thresholding Binary (Binarize):** Mengubah gambar menjadi biner (hitam-putih).
- **Get Biggest Scratch:** Mengambil area daun terbesar.
- **Replace White:** Mengganti latar belakang putih.

### 2. Multicolor Preprocessing (Khusus Dracaena)
Digunakan untuk daun Dracaena/bambu rezeki putih:
- **Cropping & Rotate**
- **Brightening**
- **Binarize Multicolor**
- **Denoising Colored**
- **Gaussian Blur**
- **Conversion to HSV**
- **Thresholding Yellow Color**
- **Morphology Closing**
- **Get Biggest Scratch**
- **Replace White**

> **Catatan:**  
> Multicolor preprocessing hanya digunakan untuk daun Dracaena/bambu rezeki putih.

---

## Workflow

1. **Split Data**
   - Pisahkan data menjadi train, test, dan validating.
   - Lakukan split data ke train & test.

2. **Preprocessing**
   - Terapkan preprocessing standar untuk daun biasa.
   - Terapkan multicolor preprocessing untuk daun Dracaena.

3. **Training**
   - Latih model dengan berbagai arsitektur CNN (AlexNet, LeNet5, ResNet50, LeafNet, Custom1, Custom2).

4. **Validation**
   - Validasi model menggunakan data validasi.

5. **Predict**
   - Prediksi jenis daun pada data baru menggunakan model terlatih.

---

## Kebutuhan

- Python 2.x & Python 3.x
- Keras & TensorFlow
- OpenCV
- NumPy
- scikit-learn
- Google Colab (disarankan)

---

## Implementasi API

Implementasi API untuk proyek ini tersedia di [https://github.com/hafiizhekom/daunesia-api](https://github.com/hafiizhekom/daunesia-api).