\# ROADGUARD

\### Quality-Calibrated Reliability-Aware Adaptive Camera–IMU Fusion for Robust Road Hazard Detection



ROADGUARD is an undergraduate research project focused on detecting road hazards using camera, IMU and GPS data.



The system aims to improve road hazard detection reliability through sensor-quality assessment, adaptive multimodal fusion and temporal cross-modal verification.



\## Current Development Status



\*\*Software development – Camera module implemented\*\*



\- YOLO11n-based pothole detection.

\- Custom pothole model trained using a public dataset.

\- Image-quality analysis using brightness, blur and contrast.

\- Camera inference using OpenCV.

\- Real-time webcam detection demonstration.



\## Model Performance



Test dataset results:



| Metric | Score |

|---|---:|

| Precision | 82.01% |

| Recall | 81.86% |

| mAP@50 | 86.96% |

| mAP@50–95 | 61.08% |



Test dataset: 80 images and 204 annotated pothole instances.



These results apply to the pothole detection dataset and do not represent complete real-world road hazard performance.



\## Technology Stack



\- Python

\- PyTorch

\- YOLO11n

\- Ultralytics

\- OpenCV

\- NumPy

\- Scikit-learn (planned for IMU classification)



\## Project Structure



```text

ROADGUARD/

├── models/

│   └── vision/

├── src/

│   ├── vision/

│   ├── imu/

│   ├── reliability/

│   ├── fusion/

│   ├── gps/

│   ├── database/

│   └── utils/

├── tests/

├── datasets/

├── app/

├── requirements.txt

└── main.py

```



\## Current Camera Module



The camera module performs:



1\. Frame acquisition.

2\. Pothole detection using YOLO11n.

3\. Bounding-box generation.

4\. Detection confidence estimation.

5\. Image-quality analysis.



Image-quality indicators currently include brightness, Laplacian-based blur measurement and contrast.



The combined image-quality score is currently heuristic and has not yet been calibrated against detection correctness.



\## Installation



Clone the repository:



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd ROADGUARD

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate it on Windows:



```powershell

venv\\Scripts\\activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



Place the trained YOLO model at:



```text

models/vision/road\_damage.pt

```



Run the camera demonstration:



```bash

python -m tests.test\_vision

```



\## Research Contributions Under Development



\- Quality-calibrated camera reliability estimation.

\- IMU-based road disturbance classification.

\- Reliability-aware adaptive camera–IMU fusion.

\- Temporal association of visual detections and inertial events.

\- GPS-based hazard geotagging.

\- Edge deployment and robustness evaluation.



\## Development Status



The current implementation is an early software prototype. IMU integration, reliability calibration, adaptive fusion, GPS integration and edge deployment remain under development.



\## Research Project



ROADGUARD – Open Labs Advanced Research Project.



