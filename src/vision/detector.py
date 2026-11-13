
import cv2
from ultralytics import YOLO
from pathlib import Path


class RoadHazardDetector:

    def __init__(self, confidence=0.10):

        root = Path(__file__).resolve().parents[2]

        model_path = (
            root / "models" / "vision" / "road_damage.pt"
        )

        self.model = YOLO(str(model_path))
        self.confidence = confidence

    def detect(self, image):

        if image is None:
            raise ValueError("Invalid image")

        results = self.model.predict(
            source=image,
            conf=self.confidence,
            verbose=False
        )

        detections = []

        for result in results:
            for box in result.boxes:

                coordinates = box.xyxy[0].cpu().tolist()

                detections.append({
                    "hazard_type": "pothole",
                    "confidence": float(box.conf[0].cpu()),
                    "bbox": [int(v) for v in coordinates]
                })

        return {
            "detected": len(detections) > 0,
            "count": len(detections),
            "detections": detections
        }

    def draw_detections(self, image, result):

        output = image.copy()

        for detection in result["detections"]:

            x1, y1, x2, y2 = detection["bbox"]
            confidence = detection["confidence"]

            cv2.rectangle(
                output,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                output,
                f"Pothole {confidence:.2f}",
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        return output
