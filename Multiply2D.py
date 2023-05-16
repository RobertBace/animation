import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib

matplotlib.use('TkAgg')

class MultiplicationOfTwoVector2D:
    def __init__(self, x1, y1, const):
        self.const = const
        self.vec1 = np.array([x1, y1])

        # Create the figure and axis
        self.fig, self.ax = plt.subplots()

        manager = plt.get_current_fig_manager()
        manager.window.state('zoomed')

        # Set dark background
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')

        # Define the quiver plot for the vectors
        if(const <= 1):
            self.q2 = self.ax.quiver(0, 0, self.vec1[0], self.vec1[1], angles='xy', scale_units='xy', scale=1,color='blue')
            self.q1 = self.ax.quiver(0, 0, self.vec1[0], self.vec1[1], angles='xy', scale_units='xy', scale=1,color='red')
        else:
            self.q1 = self.ax.quiver(0, 0, self.vec1[0], self.vec1[1], angles='xy', scale_units='xy', scale=1, color='red')
            self.q2 = self.ax.quiver(0, 0, self.vec1[0], self.vec1[1], angles='xy', scale_units='xy', scale=1, color='blue')
        self.q2.set_visible(False)

        x = self.vec1[0] * const
        y = self.vec1[1] * const

        self.lineX = self.ax.plot([0, x], [y, y], 'r--', label='line')
        self.lineY = self.ax.plot([x, x], [0, y], 'r--', label='line')
        self.lineX[0].set_visible(False)
        self.lineY[0].set_visible(False)

        arrayX = [self.vec1[0], self.vec1[0] * const, 0]
        arrayY = [self.vec1[1], self.vec1[1] * const, 0]
        plt.xticks(np.arange(min(arrayX) - 1, max(arrayX) + 2, 1))
        plt.yticks(np.arange(min(arrayY) - 1, max(arrayY) + 2, 1))

        self.ax.spines['left'].set_position(('data', 0.0))
        self.ax.spines['bottom'].set_position(('data', 0.0))
        self.ax.spines['left'].set_color('yellow')
        self.ax.spines['bottom'].set_color('yellow')
        self.ax.spines['left'].set_linewidth(3)
        self.ax.spines['bottom'].set_linewidth(3)
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')

        fsxMax = (max(arrayX) + 2) - (min(arrayX) - 1)
        fsyMax = (max(arrayY) + 2) - (min(arrayY) - 1)

        if (fsxMax > 100):
            fsx = 4
        elif (fsxMax > 75):
            fsx = 6
        elif (fsxMax > 50):
            fsx = 8
        elif (fsxMax > 25):
            fsx = 10
        else:
            fsx = 12

        if (fsyMax > 100):
            fsy = 4
        elif (fsyMax > 75):
            fsy = 6
        elif (fsyMax > 50):
            fsy = 8
        elif (fsyMax > 25):
            fsy = 10
        else:
            fsy = 12

        # set numbers color
        self.ax.tick_params(axis='x', colors='yellow', size=8, labelsize=fsx)
        self.ax.tick_params(axis='y', colors='yellow', size=8, labelsize=fsy)

        # Define a flag to indicate if the animation is paused
        self.pause = False

        # Define a variable to store the animation object
        self.ani = None

        # Create the animation

        self.ani = animation.FuncAnimation(self.fig, self.update, frames=102, interval=5)

        # Connect the mouse button click event to the onClick function
        self.fig.canvas.mpl_connect('key_press_event', self.onClick)

        self.label = r'$\genfrac{(}{)}{0}{1}{\mathtt{\,' + str(x1) + '}}{\mathtt{\,' + str(y1) + '}}\;\cdot\;' + str(const) + '}}$'

        self.labelFinal = r'$\genfrac{(}{)}{0}{1}{\mathtt{\,' + str(x1) + '}}{\mathtt{\,' + str(y1) + '}}\;\cdot\;' \
                      ''+ str(const) + '\;=\; \genfrac{(}{)}{0}{3}{\mathtt{\,' + str(x1*const) + '}}{\mathtt{\,' + str(y1*const) + '}}$'


        self.ax.set_title(label=self.label, color='yellow', pad=30, fontsize=40)

        plt.subplots_adjust(top=0.8)

        #equalize the scales of the x-axis and y-axis
        #self.ax.set_aspect('equal', adjustable='box')

        # Display the animation
        plt.show(block=True)



    def update(self, frame):
        if (frame >= 1):
            myFrame = frame - 1
        else:
            myFrame = -1

        if (self.ani):
            # self.ani.event_source.stop()
            if (myFrame == 0 or myFrame == 100):
                self.pause = True
                self.ani.event_source.stop()

        if(myFrame == 0):
            self.q1.set_UVC(self.vec1[0], self.vec1[1])
            self.lineX[0].set_visible(False)
            self.lineY[0].set_visible(False)
            self.q2.set_visible(False)

        # Calculate the time parameter
        if(myFrame <= 100):
            self.q2.set_visible(True)
            t = [((self.const - 1) * (myFrame) / 100.0) * i for i in self.vec1]
            t = t + self.vec1
            self.q1.set_UVC(t[0], t[1])
            if (self.ani):
                self.ax.set_title(label=self.label, color='yellow', pad=30, fontsize=40)

        if(myFrame == 100):
            self.lineX[0].set_visible(True)
            self.lineY[0].set_visible(True)
            if (self.ani):
                self.ax.set_title(label=self.labelFinal, color='yellow', pad=30, fontsize=40)
            # Redraw the plot
        self.fig.canvas.draw()

        return self.q1

    # Define a function to pause the animation when the mouse button is clicked
    def onClick(self, event):
        if event.key == ' ':
            #global self.pause
            self.pause ^= True
            if self.pause:
                self.ani.event_source.stop()
            else:
                self.ani.event_source.start()

#MultiplicationOfTwoVector2D(2, 2, 1)