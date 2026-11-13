
import cv2
import numpy as np


class ImageQualityAnalyzer:

    def analyze(self, image):

        if image is None:
            raise ValueError("Invalid image")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 1. Brightness
        brightness = float(np.mean(gray))

        # 2. Blur detection
        blur_score = float(cv2.Laplacian(
            gray, cv2.CV_64F
        ).var())

        # 3. Contrast
        contrast = float(np.std(gray))

        # Normalize individual quality indicators
        brightness_quality = max(
            0.0, 1.0 - abs(brightness - 127.5) / 127.5
        )

        blur_quality = min(blur_score / 150.0, 1.0)

        contrast_quality = min(contrast / 64.0, 1.0)

        # Combined image quality indicator
        quality_score = (
            0.35 * brightness_quality +
            0.40 * blur_quality +
            0.25 * contrast_quality
        )

        return {
            "brightness": round(brightness, 2),
            "blur_score": round(blur_score, 2),
            "contrast": round(contrast, 2),
            "brightness_quality": round(brightness_quality, 3),
            "blur_quality": round(blur_quality, 3),
            "contrast_quality": round(contrast_quality, 3),
            "quality_score": round(quality_score, 3)
        }
