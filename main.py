import os
import numpy as np
import pydicom
import pydicom.config
import matplotlib.pyplot as plt
from skimage import measure
import trimesh
pydicom.config.settings.reading_validation_mode = "WARN"

# Path to your DICOM folder
dicom_folder = r"C:\Users\Hp\Desktop\IIT Delhi Assignment\hip-joint-dicom-to-stl\data"

# Load all DICOM files from the folder
dicom_files = []
for filename in sorted(os.listdir(dicom_folder)):
    if filename.endswith(".dcm"):
        filepath = os.path.join(dicom_folder, filename)
        dicom_files.append(pydicom.dcmread(filepath))

print(f"Total slices loaded: {len(dicom_files)}")

# View one slice to verify data loaded correctly
slice_index = 80  # middle slice

plt.imshow(dicom_files[slice_index].pixel_array, cmap="gray")
plt.title(f"CT Slice {slice_index}")
plt.axis("off")
plt.show()

# Stack all slices into a 3D numpy array
slices = []
for dicom_file in dicom_files:
    try:
        slices.append(dicom_file.pixel_array)
    except Exception as e:
        print(f"Skipping file due to error: {e}")

volume = np.stack(slices, axis=0)
print(f"3D Volume shape: {volume.shape}")

# Block 5 - HU Thresholding
bone_threshold_min = 800
bone_threshold_max = 1900
bone_mask = (volume > bone_threshold_min) & (volume < bone_threshold_max)
print(f"Bone mask shape: {bone_mask.shape}")
print(f"Bone voxels found: {np.sum(bone_mask)}")

# Apply Marching Cubes to generate 3D surface mesh
print("Running Marching Cubes... this may take a moment")
verts, faces, normals, values = measure.marching_cubes(bone_mask, level=0.5)

print(f"Vertices: {len(verts)}")
print(f"Faces: {len(faces)}")

# Export 3D mesh as STL file
print("Exporting STL file...")
mesh = trimesh.Trimesh(vertices=verts, faces=faces)
trimesh.smoothing.filter_laplacian(mesh, iterations=3)
mesh.export("hip_joint.stl")
print("STL file saved as hip_joint.stl")