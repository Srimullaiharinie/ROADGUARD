
import cv2
from src.vision.image_quality import ImageQualityAnalyzer

analyzer = ImageQualityAnalyzer()

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Camera not available")

print("ROADGUARD IMAGE QUALITY ANALYSIS")
print("Press Q to exit")

while True:

    ret, frame = camera.read()

    if not ret:
        break

    result = analyzer.analyze(frame)

    print(result)

    cv2.putText(
        frame,
        f"Quality: {result['quality_score']:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("ROADGUARD Camera Quality", frame)

    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
