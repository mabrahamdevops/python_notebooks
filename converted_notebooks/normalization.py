# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] run_control={"frozen": false, "read_only": false}
# [![Notebook Tutorial](__code/__all/notebook_tutorial.png)](https://neutronimaging.pages.ornl.gov/tutorial/notebooks/normalization)
#
# <img src='__docs/__all/notebook_rules.png' />

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Your IPTS 

# + run_control={"frozen": false, "read_only": false}
from __code.normalization import *

from __code.ui_builder import UiBuilder
o_builder = UiBuilder(ui_name = 'ui_roi_selection.ui')
from __code.roi_selection_ui import Interface

from __code import system
system.System.select_working_dir()
from __code.__all import custom_style
custom_style.style()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Python Import

# + run_control={"frozen": false, "read_only": false}
# %gui qt

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Gamma Filtering Coefficient 

# + run_control={"frozen": false, "read_only": false}
o_gamma = GammaCoefficient()
o_gamma.select_gamma_coefficient()

# + [markdown] run_control={"frozen": false, "read_only": false}
# If you need help figuring out which **gamma coefficient** to use, check the [gamma filtering tool notbeook](gamma_filtering_tool.ipynb)

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Images (Sample, OB, and DF)

# + run_control={"frozen": false, "read_only": false}
files = Files()
sample_panel = SampleSelectionPanel(working_dir=system.System.get_working_dir(), gamma_coefficient=o_gamma.get_coefficient())
sample_panel.init_ui(files=files)
wizard = WizardPanel(sample_panel=sample_panel)

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Select Background Region 

# + run_control={"frozen": false, "read_only": false}
o_norm = sample_panel.o_norm_handler
o_gui = Interface(o_norm=o_norm.o_norm)
o_gui.show()

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Normalization

# + run_control={"frozen": false, "read_only": false}
o_norm.run_normalization(dict_roi=o_gui.roi_selected)

# + [markdown] run_control={"frozen": false, "read_only": false}
# # Export 

# + run_control={"frozen": false, "read_only": false}
o_norm.select_export_folder(ipts_folder=sample_panel.ipts_dir)

# + run_control={"frozen": false, "read_only": false}
o_norm.export()

# + run_control={"frozen": false, "read_only": false}

