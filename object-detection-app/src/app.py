import cv2
from controllers.roi_selector import ROISelector
from models.seat_detector import SeatDetector

def main():
    # URL da câmera
    camera_url = "rtsp://admin:FLEXI%402022@192.168.1.15:80/cam/realmonitor?channel=11&subtype=0"
    reference_images_path = "c:/Users/Flexibase/Documents/GitHub/ObjectDetection/object-detection-app/src/models/seat"  # Caminho atualizado para a pasta de imagens de referência

    # Captura de vídeo
    cap = cv2.VideoCapture(camera_url)
    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        return

    selector = ROISelector()
    detector = SeatDetector(reference_images_path)

    # Seleção da ROI
    roi = None
    while roi is None:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar o frame.")
            break

        roi = selector.select_roi(frame)
        if roi is not None:
            print("Região selecionada:", roi)

    # Continuar exibindo o vídeo em tempo real com detecção de assentos
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar o frame.")
            break

        # Detectar assentos na ROI
        frame, detected_seats = detector.detect_seats(frame, roi)

        # Desenhar a ROI selecionada no frame
        if roi is not None:
            cv2.polylines(frame, [roi], isClosed=True, color=(0, 255, 0), thickness=2)

        # Adicionar texto com métricas no frame
        cv2.putText(frame, "Press 'X' to quit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f"Detected Seats: {detected_seats}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f"ROI: {roi}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("Vídeo em Tempo Real", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("x"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()