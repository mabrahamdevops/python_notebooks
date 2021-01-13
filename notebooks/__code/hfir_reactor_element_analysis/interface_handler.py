from qtpy.QtWidgets import QMainWindow, QVBoxLayout, QProgressBar, QApplication
import os
import numpy as np
from lmfit import Model

from __code import load_ui
from __code.hfir_reactor_element_analysis.initialization import Initialization
from __code.hfir_reactor_element_analysis.event_handler import EventHandler
from __code.hfir_reactor_element_analysis.fitting_functions import sin_fit


class InterfaceHandler:

    def __init__(self, working_dir=None, o_selection=None):
        o_interface = Interface(o_selection=o_selection,
                                working_dir=working_dir)
        o_interface.show()
        self.o_interface = o_interface


class Interface(QMainWindow):

    def __init__(self, parent=None, o_selection=None, working_dir=None):
        self.o_selection = o_selection
        self.o_pandas = o_selection.pandas_obj
        self.working_dir = working_dir
        self.list_angles = self.o_pandas.index

        super(Interface, self).__init__(parent)

        ui_full_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                    os.path.join('ui',
                                                 'ui_hfir_reactor_element_fitting.ui'))
        self.ui = load_ui(ui_full_path, baseinstance=self)
        self.setWindowTitle("Data fitting")

        o_init = Initialization(parent=self)
        o_init.matplotlib()
        o_init.widgets()
        o_init.fitting()

    # event handler
    def list_of_images_selection_changed(self):
        o_event = EventHandler(parent=self)
        o_event.list_of_images_selection_changed()

    def plot_type_changed(self):
        self.list_of_images_selection_changed()

    def list_of_images_right_click(self, position=None):
        o_event = EventHandler(parent=self)
        o_event.list_of_images_right_click()

    def get_list_file_index_selected(self):
        nbr_row = self.ui.listWidget.count()
        list_file_selected = []
        for _row in np.arange(nbr_row):
            _item = self.ui.listWidget.item(_row)
            if _item.isSelected():
                list_file_selected.append(_row)
        return list_file_selected

    def get_angle_range_index(self):
        from_angle_index = self.ui.from_angle_slider.value()
        to_angle_index = self.ui.to_angle_slider.value()
        return [from_angle_index, to_angle_index]

    def automatic_fit_clicked(self):
        # range of files to use to fit
        list_file_index_selected = self.get_list_file_index_selected()
        angle_range = self.get_angle_range_index()

        list_of_files = self.o_selection.column_labels[1:]

        data_to_use = []
        pandas_obj = self.o_selection.pandas_obj
        for _file_index  in list_file_index_selected:
            _file = list_of_files[_file_index]
            _data = np.array(pandas_obj[_file])
            _data = _data[angle_range[0]: angle_range[1]+1]
            data_to_use.append(_data)

        data_to_fit = np.mean(data_to_use, axis=0)

        x_axis = pandas_obj.index[angle_range[0]: angle_range[1]+1]
        y_axis = data_to_fit

        gmodel = Model(sin_fit, missing='drop', nan_policy='propagate')
        params = gmodel.make_params()

        params.add('a',
                   value=np.float(str(self.ui.automatic_initial_guess_a_lineEdit.text())),
                   vary=not self.ui.auto_a_lock_checkBox.isChecked())

        params.add('m',
                   value=np.float(str(self.ui.automatic_initial_guess_m_lineEdit.text())),
                   vary=not self.ui.auto_m_lock_checkBox.isChecked())

        params.add('p',
                   value=np.float(str(self.ui.automatic_initial_guess_p_lineEdit.text())),
                   vary=not self.ui.auto_p_lock_checkBox.isChecked())

        params.add('b',
                   value=np.float(str(self.ui.automatic_initial_guess_b_lineEdit.text())),
                   vary=not self.ui.auto_b_lock_checkBox.isChecked())

        # # for debugging
        # import json
        # debug_fit = {'x_axis': list(x_axis),
        #              'y_axis': list(y_axis)}
        # output_file = "/Users/j35/Desktop/debug_fit.json"
        # with open(output_file, 'w') as json_file:
        #     json.dump(debug_fit, json_file)

        # result = gmodel.fit(y_axis, params, angle=x_axis)
        # print(f"result: {result}")
        #
        # print(f"a: {result.params['a'].value}")
        # print(f"m: {result.params['m'].value}")
        # print(f"p: {result.params['p'].value}")
        # print(f"b: {result.params['b'].value}")

    def automatic_a_value_changed(self, text):
        self.check_status_of_automatic_fit()

    def automatic_m_value_changed(self, text):
        self.check_status_of_automatic_fit()

    def automatic_p_value_changed(self, text):
        self.check_status_of_automatic_fit()

    def automatic_b_value_changed(self, text):
        self.check_status_of_automatic_fit()

    def automatic_a_value_estimate(self):
        o_event = EventHandler(parent=self)
        o_event.calculate_a_value_estimate()

    def automatic_b_value_estimate(self):
        o_event = EventHandler(parent=self)
        o_event.calculate_b_value_estimate()

    def check_status_of_automatic_fit(self):
        enabled_automatic_button = self.get_check_status_of_automatic_fit()
        self.ui.automatic_fit_pushButton.setEnabled(enabled_automatic_button)

    def get_check_status_of_automatic_fit(self):
        a_value = str(self.ui.automatic_initial_guess_a_lineEdit.text()).strip()
        if a_value == "":
            return False

        m_value = str(self.ui.automatic_initial_guess_m_lineEdit.text()).strip()
        if m_value == "":
            return False

        p_value = str(self.ui.automatic_initial_guess_p_lineEdit.text()).strip()
        if p_value == "":
            return False

        b_value = str(self.ui.automatic_initial_guess_b_lineEdit.text()).strip()
        if b_value == "":
            return False

        a_lock = self.ui.auto_a_lock_checkBox.isChecked()
        m_lock = self.ui.auto_m_lock_checkBox.isChecked()
        p_lock = self.ui.auto_p_lock_checkBox.isChecked()
        b_lock = self.ui.auto_b_lock_checkBox.isChecked()
        if a_lock and m_lock and p_lock and b_lock:
            return False

        return True

    def automatic_fit_lock_value_clicked(self):
        self.check_status_of_automatic_fit()

    def from_angle_slider_moved(self, from_angle):
        self.ui.from_angle_label.setText("From {:.2f}".format(self.list_angles[from_angle]) + u"\u00B0")
        # make sure the to_angle stays larger by at least 20
        to_angle = self.ui.to_angle_slider.value()
        if from_angle > (to_angle - 20):
            to_angle = from_angle + 20
            self.to_angle_slider.setValue(to_angle)
            self.to_angle_slider_moved(to_angle)

    def to_angle_slider_moved(self, to_angle):
        self.ui.to_angle_label.setText("To {:.2f}".format(self.list_angles[to_angle]) + u"\u00B0")
        # make sure the from angle stays smaller by at least 20
        from_angle = self.ui.from_angle_slider.value()
        if to_angle < (from_angle + 20):
            from_angle = to_angle - 20
            self.from_angle_slider.setValue(from_angle)
            self.from_angle_slider_moved(from_angle)
