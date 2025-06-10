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

## Requirements

- Python 2.x & Python 3.x
- Keras & TensorFlow
- OpenCV
- NumPy
- scikit-learn
- Google Colab (disarankan)

---

## Hasil Akurasi & Loss Model

| Architecture     | Top 1 Acc | Top 1 Loss | Top 1 Val Acc | Top 1 Val Loss | Top 5 Acc | Top 5 Loss | Top 5 Val Acc | Top 5 Val Loss |
|-----------|-----------|------------|---------------|---------------|-----------|------------|---------------|---------------|
| LeNet5    | 0.9853    | 0.0446     | 0.2423        | 10.4603       | 0.9915    | 0.0248     | 0.2924        | 10.2835       |
| AlexNet   | 0.9722    | 0.0818     | 0.9499        | 0.1995        | 0.9775    | 0.0587     | 0.9788        | 0.1767        |
| LeafNet   | 0.9698    | 0.0928     | 0.7428        | 1.1867        | 0.9728    | 0.0998     | 0.9237        | 0.2735        |
| ResNet50  | 0.9848    | 0.0427     | 0.7839        | 0.9675        | 0.9890    | 0.0408     | 0.9499        | 0.1173        |
| Custom1   | 0.9706    | 0.0733     | 0.9453        | 0.2361        | 0.9754    | 0.0737     | 0.9537        | 0.1060        |
| Custom2   | 0.9738    | 0.0689     | 0.9060        | 0.2579        | 0.9765    | 0.0638     | 0.9198        | 0.2935        |

**Keterangan:**
- **Acc:** Akurasi pada data training
- **Loss:** Loss pada data training
- **Val Acc:** Akurasi pada data validasi
- **Val Loss:** Loss pada data validasi

---

Tabel di atas menunjukkan performa masing-masing arsitektur model pada klasifikasi daun, baik untuk Top 1 maupun Top 5 prediksi terbaik.

---

## Confusion Matrix

Berikut adalah contoh confusion matrix beserta akurasi dari beberapa arsitektur CNN yang digunakan:

| AlexNet | LeNet5 | ResNet50 |
|---------|--------|----------|
| ![alexnet](./confusion_matrix/alexnet.png) | ![lenet5](./confusion_matrix/lenet5.png) | ![resnet50](./confusion_matrix/resnet50.png) |

| LeafNet | Custom1 | Custom2 |
|---------|---------|---------|
| ![leafnet](./confusion_matrix/leafnet.png) | ![custom1](./confusion_matrix/custom1.png) | ![custom2](./confusion_matrix/custom2.png) |

Setiap gambar menampilkan confusion matrix dan nilai akurasi akhir dari model terkait.

## Implementasi API

Implementasi API untuk proyek ini tersedia di [https://github.com/hafiizhekom/daunesia-api](https://github.com/hafiizhekom/daunesia-api).

---
