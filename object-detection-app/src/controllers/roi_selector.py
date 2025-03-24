import cv2
import numpy as np

class ROISelector:
    def __init__(self):
        self.refPt = []
        self.cropping = False
        self.roi = None

    def click_and_crop(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.refPt.append((x, y))
            if len(self.refPt) == 4:
                self.cropping = False
                self.roi = np.array(self.refPt, dtype=np.int32)

    def select_roi(self, frame):
        clone = frame.copy()
        cv2.namedWindow("Selecione a Área")
        cv2.setMouseCallback("Selecione a Área", self.click_and_crop)

        while True:
            clone = frame.copy()
            if len(self.refPt) > 0:
                for pt in self.refPt:
                    cv2.circle(clone, pt, 5, (0, 255, 0), -1)
                if len(self.refPt) == 4:
                    cv2.polylines(clone, [self.roi], isClosed=True, color=(0, 255, 0), thickness=2)
                    cv2.imshow("Selecione a Área", clone)
                    cv2.waitKey(1)
                    break
            cv2.imshow("Selecione a Área", clone)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        cv2.destroyAllWindows()
        return self.roi