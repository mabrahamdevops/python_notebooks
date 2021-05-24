from __code._utilities.parent import Parent
from __code.wave_front_dynamics.get import Get


class Display(Parent):

    def display_current_selected_profile_and_edge_position(self):
        o_get = Get(parent=self.parent)
        edge_calculation_algorithm = o_get.edge_calculation_algorithms()
        park_value_array = self.parent.peak_value_arrays[edge_calculation_algorithm]
        list_of_data_prepared = self.parent.list_of_data_prepared
        file_index_selected = o_get.edge_calculation_file_index_selected()

        edge_position = park_value_array[file_index_selected]
        data_to_plot = list_of_data_prepared[file_index_selected]

        self.parent.ui.calculated_edges_plot.axes.clear()
        self.parent.ui.calculated_edges_plot.axes.plot(data_to_plot, '*')
        self.parent.ui.calculated_edges_plot.axes.axvline(edge_position, color='red')
        self.parent.ui.calculated_edges_plot.axes.set_xlabel("Pixel (relative position) ")
        self.parent.ui.calculated_edges_plot.axes.set_ylabel("Mean counts")
        self.parent.ui.calculated_edges_plot.draw()

    def display_all_edge_positions(self):
        o_get = Get(parent=self.parent)
        edge_calculation_algorithm = o_get.edge_calculation_algorithms()
        park_value_array = self.parent.peak_value_arrays[edge_calculation_algorithm]

        self.parent.ui.recap_edges_plot.axes.clear()
        self.parent.ui.recap_edges_plot.axes.plot(park_value_array, '*')
        self.parent.ui.recap_edges_plot.axes.set_xlabel("File index")
        self.parent.ui.recap_edges_plot.axes.set_ylabel("Wave front position (relative pixel position)")
        self.parent.ui.recap_edges_plot.draw()
