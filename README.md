# Pothole
A Hybrid Method to calculate the depth of pothole using LiDAR and Point Cloud
This study presents an automated approach for
detecting potholes and estimating their depth using LiDAR point
cloud data. The methodology involves pre-processing raw LiDAR
data, segmenting the road surface, clustering pothole regions, and
calculating their dimensions. The proposed system utilizes
DBSCAN clustering and convex hull techniques to accurately
identify and measure potholes. The methodology involves
collecting 3D point cloud data from LiDAR sensors, specifically
from .las files, to ensure accurate surface reconstruction. The preprocessing stage applies voxel down-sampling, statistical noise
removal, and plane segmentation using RANSAC to differentiate
road surfaces from potholes. The DBSCAN clustering algorithm is
then utilized to identify pothole regions, and convex hull estimation
aids in extracting the precise dimensions of potholes. The preprocessing stage applies voxel down-sampling, statistical noise
removal, and plane segmentation using RANSAC to differentiate
road surfaces from potholes. The DBSCAN clustering algorithm is
then utilized to identify pothole regions, and convex hull estimation
aids in extracting the precise dimensions of potholes. The approach
enables real-time visualization and accurate depth calculation of
potholes, which is crucial for road safety and maintenance.

Features
- Captures LiDAR data and processes 3D point clouds
- Uses DBSCAN clustering for pothole detection
- Supports .las

Installation  
Clone the repository and install dependencies:  

```bash
pip install -r requirements.txt

Dependencies  
- Python 3.10
- Open3D  
- NumPy  
- Matplotlib  
- Scikit-learn  
- SciPy  
- laspy
```
Step 1: Capture LiDAR Data
Use Lidar sensor to capture 3d point cloud data of potholes.

Step 2: Preprocess the .las File
Load the .las file into visulaization.py to vizulaize the pothole.
![ScreenCapture_2025-03-18-22-22-16](https://github.com/user-attachments/assets/773429a6-e1d3-450f-b4f2-863e1aba9205)

![ScreenCapture_2025-03-18-22-22-06](https://github.com/user-attachments/assets/0c1e67bf-df48-443d-8653-514b06326609)

Step 3: Input Data into depth.ipynb
Load the processed point cloud into depth.ipynb for depth estimation.
Run depth estimation and pothole detection.
Extract pothole depth in meters.

Step 4: Visualize & Analyze Results
![output](https://github.com/user-attachments/assets/9a769c5a-b9e6-4370-b07b-c2786fc2b67a)

RESULT
```Table
Measurements	Dimensions in meters
Maximum Depth:	0.077 meters
Average Depth:	0.067 meters
Length:	0.240 meters
Width:	0.200 meters
Surface Area:	0.035 square meters
Approximate Volume:	0.002 cubic meters
```
