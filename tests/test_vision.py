
import cv2
from src.vision.detector import RoadHazardDetector

detector = RoadHazardDetector(confidence=0.10)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Camera could not be opened")

print("ROADGUARD CAMERA STARTED")
print("Press Q to quit")

while True:

    ret, frame = camera.read()

    if not ret:
        break

    result = detector.detect(frame)

    output = detector.draw_detections(frame, result)

    cv2.imshow("ROADGUARD - Pothole Detection", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
