import cv2
import os
import numpy as np

class SeatDetector:
    def __init__(self, reference_images_path):
        self.reference_images = []
        self.load_reference_images(reference_images_path)

    def load_reference_images(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"O caminho especificado não foi encontrado: {path}")
        for filename in os.listdir(path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                img = cv2.imread(os.path.join(path, filename), cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    self.reference_images.append(img)

    def detect_seats(self, frame, roi):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected_seats = 0

        if roi is not None:
            mask = np.zeros(gray_frame.shape, dtype=np.uint8)
            cv2.fillPoly(mask, [roi], 255)
            roi_frame = cv2.bitwise_and(gray_frame, gray_frame, mask=mask)

            for template in self.reference_images:
                res = cv2.matchTemplate(roi_frame, template, cv2.TM_CCOEFF_NORMED)
                threshold = 0.8
                loc = np.where(res >= threshold)

                for pt in zip(*loc[::-1]):
                    cv2.rectangle(frame, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 0, 255), 2)
                    detected_seats += 1

        return frame, detected_seats