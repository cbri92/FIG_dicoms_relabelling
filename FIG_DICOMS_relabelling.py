# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:38:51 2021

@author: Caterina Brighi
"""

#%% Import functions 

import os
import glob
import pydicom
from pathlib import Path

'''Before running the script remember to:
    
    1. set the path to the working directory in the following section
    2. check that the folder structure you start with is:
                Dataset from site N
                    Patient X
                        Imaging Sequence
                            xxx.dcm
                
        for example:
                Liverpool data
                    GBM01
                        3D T1
                            1-01.dcm
    3. check that the names included in the old_name list given in the section below are consistent with the naming of the "Imaging Sequence" folders you have.
        If it is not, modify the list accordingly.
    4. select the appropriate Study description name in the last section, according to the timepoint of the study
    '''

#%% Set Working directory
        
data_supradir = 'Insert here absolute path to directory containing patients subfolders' #Set working directory

subjs_path = [ f.path for f in os.scandir(data_supradir) if f.is_dir() ] #Create a list of the paths to the patients directories
subjs_name = [ f.name for f in os.scandir(data_supradir) if f.is_dir() ] #Create a list of patients names


#%%Create a for loop to perform image analysis on each subject sequentially

for current in subjs_name:
    subj_dir = data_supradir+current
    subj_name = current
    
    old_name = ['*3D T1*', '*flair*', '*Ax 2D DWI*', '*DCE*', '*DSC*', '*Ax T2*', '*T1 C*', '*FET PET*', '*FET CT*']
    new_name = ['3D T1', 'FLAIR', 'DWI', 'DCE', 'DSC', 'T2', 'T1 C', 'FET PET', 'FET CT']
    for old, new in zip(old_name, new_name):
        x = glob.glob(subj_dir+'/'+old)
        x = str(x[0])
        os.rename(x, subj_dir+'/'+new)

    subj_dir_path = Path(subj_dir)
    
    for seq in new_name:
        for dcm_file in subj_dir_path.glob(seq+"/*.dcm"): # This will get each original dicom file for this patient and sequence
            ds = pydicom.read_file(dcm_file) # pydicom should be able to now read these Path objects, if not try updating your pydicom version :)

            # Now ds is the Dicom object, you can update the headers
            ds.PatientID = subj_name #This updates the patient ID to the name of the patient folder
            ds.PatientName = subj_name #This updates the patient name to the name of the patient folder
            ds.SeriesDescription = seq #This updates the Series description DICOM tag to the name of the specific sequence
            ds.StudyDescription = 'MRI1/MRI2/MRI3/FET1/FET2/FET3' #This updates the Study description DICOM tag to the study timepoint to select between the options given

            # Now we can save the Dicom file (note: this will overwrite the existing dicom file)
            ds.save_as(dcm_file)

 