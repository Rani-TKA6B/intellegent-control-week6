import cv2
import numpy as np

def canny_edge_detection_real_time():
    """Mendeteksi tepi secara real-time menggunakan metode Canny Edge Detection dengan webcam."""
    cap = cv2.VideoCapture(0)  # Menggunakan kamera default (0)

    if not cap.isOpened():
        print("Error: Kamera tidak dapat dibuka.")
        return

    while True:
        ret, frame = cap.read()  # Membaca frame dari webcam
        if not ret:
            print("Error: Gagal membaca frame dari kamera.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Konversi ke grayscale
        img_blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Mengurangi noise
        edges = cv2.Canny(img_blur, 50, 150)  # Deteksi tepi

        cv2.imshow("Canny Edge Detection - Real Time", edges)  # Menampilkan hasil

        # Tekan 'q' untuk keluar dari loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Menutup kamera
    cv2.destroyAllWindows()  # Menutup semua jendela OpenCV

# Jalankan fungsi real-time
canny_edge_detection_real_time()
