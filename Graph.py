from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    def __init__(self, df):
        self.data = df

    def display_pie_chart(self, window):
        labels = self.data['Country'].to_numpy()
        sizes = self.data['Co2'].to_numpy()

        fig = Figure(figsize=(9.5, 6), dpi=100)
        plot = fig.add_subplot()
        canvas = FigureCanvasTkAgg(fig, master=window)

        # Plot the pie chart
        plot.pie(sizes, labels=labels, autopct='%1.2f%%',
                 shadow=True, startangle=90,
                 colors={'tab:red', 'tab:orange', 'tab:olive', 'tab:green',
                         'tab:blue', 'tab:purple', 'tab:cyan', 'tab:pink',
                         'tab:brown', 'tab:gray', 'lightgrey'})
        plot.axis('equal')

        # Plot the label
        plot.set_title('CO2 emissions 2017 (% of world)', fontsize=16)

        # Show plot
        canvas.draw()
        canvas.get_tk_widget().pack()