import os
import ipywe.fileselector
from scipy.stats.mstats import gmean

from ipywidgets import widgets
from IPython.core.display import display, HTML
import numpy as np
from PIL import Image
import collections

from __code import file_handler
from NeuNorm.normalization import Normalization
import glob


class SequentialCombineImagesUsingMetadata(object):
    working_dir = ''

    def __init__(self, working_dir=''):
        self.working_dir = working_dir
        self.folder_selected = ''

    def select_folder(self):
        self.files_list_widget = ipywe.fileselector.FileSelectorPanel(instruction='select folder of images to combine',
                                                                      start_dir=self.working_dir,
                                                                      type='directory',
                                                                      next=self.info_folder_selected,
                                                                      multiple=False)
        self.files_list_widget.show()

    def info_folder_selected(self, selected):
        display(HTML('<span style="font-size: 20px; color:blue">You selected folder: ' + \
                     selected + '</span>'))
        self.folder_selected = selected

    def select_metadata_to_match(self):
        pass

    def get_list_of_images(self):
        list_of_images = glob.glob(self.folder_selected + "/*.tiff")
        list_of_images.sort()
        return list_of_images

    def display_metadata_list(self):
        self.list_images = self.get_list_of_images()
        list_images = self.list_images

        image0 = list_images[0]
        o_image0 = Image.open(image0)

        info = collections.OrderedDict(sorted(o_image0.tag_v2.items()))
        display_format = []
        for tag, value in info.items():
            display_format.append("{} -> {}".format(tag, value))

        self.box1 = widgets.HBox([widgets.Label("Select Metadata:",
                                                layout=widgets.Layout(width='10%')),
                                  widgets.Dropdown(options=display_format,
                                                   value=display_format[0],
                                                   layout=widgets.Layout(width='50%'))])
        display(self.box1)

    def how_to_combine(self):
        _file = open("__docs/combine_images/geometric_mean.png", 'rb')
        _geo_image = _file.read()
        geo_box = widgets.HBox([widgets.Label("Geometric Mean",
                                              layout=widgets.Layout(width='20%')),
                                widgets.Image(value=_geo_image,
                                              format='png')])
        _file = open("__docs/combine_images/algebric_mean.png", 'rb')
        _alge_image = _file.read()
        alge_box = widgets.HBox([widgets.Label("Arithmetic Mean",
                                              layout=widgets.Layout(width='20%')),
                                widgets.Image(value=_alge_image,
                                              format='png')])

        self.combine_method = widgets.RadioButtons(options=['add', 'arithmetic mean', 'geometric mean'],
                                                   value='arithmetic mean')

        vertical = widgets.VBox([alge_box, geo_box, self.combine_method])
        display(vertical)

    def select_output_folder(self):
        self.output_folder_widget = ipywe.fileselector.FileSelectorPanel(instruction='select where to create the ' + \
                                                                                     'combined image ...',
                                                                         start_dir=self.working_dir,
                                                                         type='directory')

        self.output_folder_widget.show()

    def __get_formated_merging_algo_name(self):
        _algo = self.combine_method.value
        if _algo =='arithmetic mean':
            return 'arithmetic_mean'
        elif _algo == 'geometric mean':
            return 'geometric_mean'
        else:
            return _algo

    def define_output_filename(self):
        list_files = self.files_list_widget.selected
        short_list_files = [os.path.basename(_file) for _file in list_files]

        merging_algo = self.__get_formated_merging_algo_name()
        [default_new_name, ext] = self.__create_merged_file_name(list_files_names=short_list_files)

        top_label = widgets.Label("You have the option to change the default output file name")

        box = widgets.HBox([widgets.Label("Default File Name",
                                          layout=widgets.Layout(width='20%')),
                            widgets.Text(default_new_name,
                                         layout=widgets.Layout(width='60%')),
                            widgets.Label("_{}{}".format(merging_algo, ext),
                                          layout=widgets.Layout(width='20%')),
                            ])
        self.default_filename_ui = box.children[1]
        self.ext_ui = box.children[2]
        vertical_box = widgets.VBox([top_label, box])
        display(vertical_box)

    def merging(self):
        """combine images using algorithm provided"""

        list_files = self.files_list_widget.selected
        nbr_files = len(list_files)

        # get merging algorithm
        merging_algo = self.combine_method.value
        algorithm = self.__add
        if merging_algo =='arithmetic mean':
            algorithm = self.__arithmetic_mean
        elif merging_algo == 'geometric mean':
            algorithm = self.__geo_mean

        # get output folder
        output_folder = os.path.abspath(self.output_folder_widget.selected)

        o_load = Normalization()
        o_load.load(file=list_files, notebook=True)
        _data = o_load.data['sample']['data']

        merging_ui = widgets.HBox([widgets.Label("Merging Progress",
                                                 layout=widgets.Layout(width='20%')),
                                   widgets.IntProgress(max=2)])
        display(merging_ui)
        w1 = merging_ui.children[1]

        combined_data = self.__merging_algorithm(algorithm, _data)
        w1.value = 1

        #_new_name = self.__create_merged_file_name(list_files_names=o_load.data['sample']['file_name'])
        _new_name = self.default_filename_ui.value + self.ext_ui.value
        output_file_name = os.path.join(output_folder, _new_name)

        file_handler.save_data(data=combined_data, filename=output_file_name)

        w1.value = 2

        display(HTML('<span style="font-size: 20px; color:blue">File created: ' + \
                     os.path.basename(output_file_name) + '</span>'))
        display(HTML('<span style="font-size: 20px; color:blue">In Folder: ' + \
                     output_folder + '</span>'))

    def __create_merged_file_name(self, list_files_names=[]):
        """Create the new base name using a combine name of all the input file

        :param list_files_names: ['/Users/j35/image001.fits','/Users/j35/iamge002.fits']
        :return:
            'image001_image002.fits'
        """
        ext = ''
        list_base_name = []
        for _file in list_files_names:
            basename = os.path.basename(_file)
            [_name, ext] = os.path.splitext(basename)
            list_base_name.append(_name)

        return ('_'.join(list_base_name), ext)

    def __add(self, data_array):
        return np.sum(data_array, axis=0)

    def __arithmetic_mean(self, data_array):
        return np.mean(data_array, axis=0)

    def __geo_mean(self, data_array):
        return gmean(data_array, axis=0)

    def __merging_algorithm(self, function_, *args):
        return function_(*args)



