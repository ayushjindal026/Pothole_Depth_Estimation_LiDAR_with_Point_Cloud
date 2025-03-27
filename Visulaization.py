import laspy
import numpy as np
import open3d as o3d

# Load the .las file
las_file = r"C:\Users\Shashank\Downloads\Untitled_Scan_13_13_09.las"  # Replace with your .las file path
las = laspy.read(las_file)

# Extract X, Y, Z coordinates
points = np.vstack((las.x, las.y, las.z)).T

# Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd], window_name="LAS Point Cloud")
