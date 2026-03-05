import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt
from skimage import measure
import trimesh
# Path to your DICOM folder
dicom_folder = r"C:\Users\Hp\Desktop\IIT Delhi Assignment\hip-joint-dicom-to-stl\data"

# Load all DICOM files from the folder
dicom_files = []
for filename in sorted(os.listdir(dicom_folder)):
    if filename.endswith(".dcm"):
        filepath = os.path.join(dicom_folder, filename)
        dicom_files.append(pydicom.dcmread(filepath))

print(f"Total slices loaded: {len(dicom_files)}")