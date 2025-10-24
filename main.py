import cv2
from model.video_detector import detect_fake_frame

def main():
    cap = cv2.VideoCapture(0)  # Use webcam
    print("🔍 DF-Guard is running... Press 'q' to exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        fake = detect_fake_frame(frame)
        label = "FAKE" if fake else "REAL"
        color = (0, 0, 255) if fake else (0, 255, 0)

        cv2.putText(frame, f"Status: {label}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow("DF-Guard - Deepfake Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
