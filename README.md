# hip-joint-dicom-to-stl

A Python pipeline to convert a hip joint CT scan from DICOM format into a 3D model exported as an STL file.

## Objective
Load a DICOM series of an adult hip joint, process the CT scan data, generate a 3D surface model using Marching Cubes algorithm, and export it in STL format.

## Dependencies
- Python 3.9+
- pydicom
- numpy
- scikit-image
- trimesh
- matplotlib

## Installation
Run the following command to install all dependencies:
```
pip install pydicom numpy scikit-image trimesh matplotlib
```

## Dataset
Download the Pelvic Reference Data from TCIA:
https://www.cancerimagingarchive.net/collection/pelvic-reference-data/
Place the .dcm files inside the data/ folder

## How to Run
1. Clone this repository
2. Download the dataset and place .dcm files in data/ folder
3. Run the script:
```
python main.py
```

## Output
- A 3D STL file named `hip_joint.stl` saved in the project root
- The STL file can be viewed in any 3D viewer like Windows 3D Viewer or viewstl.com

## Project Structure
```
hip-joint-dicom-to-stl/
    main.py        - main pipeline script
    data/          - DICOM files (not included)
    README.md      - project documentation
    .gitignore     - git ignore rules
```

## References
- TCIA Pelvic Reference Data
- pydicom documentation
- scikit-image Marching Cubes