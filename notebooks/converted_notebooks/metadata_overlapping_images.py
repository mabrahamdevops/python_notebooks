# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] run_control={"frozen": false, "read_only": false}
# [![Notebook Tutorial](__code/__all/notebook_tutorial.png)](https://neutronimaging.pages.ornl.gov/tutorial/notebooks/metadata_overlapping_images/)

# + [markdown] run_control={"frozen": false, "read_only": false}
# <img src='__docs/__all/notebook_rules.png' />

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select your IPTS 

# + run_control={"frozen": false, "read_only": false}
from __code.ipywe.myfileselector import FileSelection
from __code.metadata_overlapping_images.metadata_overlapping_images import MetadataOverlappingImagesUi

from __code import system
system.System.select_working_dir()
from __code.__all import custom_style
custom_style.style()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Python Import 

# + run_control={"frozen": false, "read_only": false}
# %gui qt

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Images to Process

# + run_control={"frozen": false, "read_only": false}
o_selection = FileSelection(working_dir=system.System.get_working_dir())
o_selection.select_data()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Launch UI 

# + run_control={"frozen": false, "read_only": false}
o_profile = MetadataOverlappingImagesUi(working_dir=system.System.get_working_dir(),
                                        data_dict=o_selection.data_dict['sample'])
o_profile.show()
# -


