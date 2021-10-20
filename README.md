# FIG_dicoms_relabelling
This script was created to relabel dicoms tags of imaging data generated from the FIG trial, in an attempt to standardise naming across datasets from multiple centre.

Before running the script remember to:
    
    1. set the path to the working directory in the "Set working directory" section
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
    3. check that the names included in the old_name list given in the "Create a for loop to perform image analysis on each subject sequentially" section are consistent with the naming of the "Imaging Sequence" folders you have.
        If it is not, modify the list accordingly.
    4. select the appropriate Study description name at line 65, according to the timepoint of the study
