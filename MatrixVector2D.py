import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib

matplotlib.use('TkAgg')

class MultiplicationVectorByMatrix2D:
    def __init__(self, x1, y1, x2, y2, vectorX, vectorY):
        self.vec1 = np.array([vectorX, vectorY])
        self.matrix = [[x1, y1], [x2, y2]]

        # Create the figure and axis
        self.fig, self.ax = plt.subplots()

        manager = plt.get_current_fig_manager()
        manager.window.state('zoomed')

        # Set dark background
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')

        # Define the scatter plot for the vectors

        self.q1 = self.ax.scatter(vectorX, vectorY, color='red')

        self.x = self.vec1[0] * x1 + self.vec1[0] * x2
        self.y = self.vec1[1] * y1 + self.vec1[1] * y2

        self.lineX = self.ax.plot([0, self.x], [self.y, self.y], 'r:', label='line', linewidth = 1)
        self.lineY = self.ax.plot([self.x, self.x], [0, self.y], 'r:', label='line', linewidth = 1)
        self.startLineX = self.ax.plot([0, vectorX], [vectorY, vectorY], 'r:', label='line', linewidth=1)
        self.startLineY = self.ax.plot([vectorX, vectorX], [0, vectorY], 'r:', label='line', linewidth=1)
        self.lineX[0].set_visible(False)
        self.lineY[0].set_visible(False)

        arrayX = [self.vec1[0], x1, x2, self.vec1[0] * x1 + self.vec1[0] * x2, 0]
        arrayY = [self.vec1[1], y1, y2, self.vec1[1] * y1 + self.vec1[1] * y2, 0]
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

        if(fsxMax > 100):
            fsx = 4
        elif(fsxMax > 75):
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

        self.label = r'$\genfrac{(}{)}{0}{1}{\mathtt{\,' + str(x1) + "\ \;" + str(x2) + '}}{\mathtt{\,' + \
                     str(y1) + "\ \;" + str(y2) + '}}\;\cdot\;\genfrac{(}{)}{0}{1}{\mathtt{\,'+\
                     str(vectorX)+'}}{\mathtt{\,'+str(vectorY)+'}}}}$'

        self.labelFinal = r'$\genfrac{(}{)}{0}{1}{\mathtt{\,' + str(x1) + "\ \;" + str(x2) + '}}{\mathtt{\,' + \
                     str(y1) + "\ \;" + str(y2) + '}}\;\cdot\;\genfrac{(}{)}{0}{1}{\mathtt{\,'+\
                     str(vectorX)+'}}{\mathtt{\,'+str(vectorY)+'}}\,=\,\genfrac{(}{)}{0}{1}{\mathtt{\,'+\
                     str(self.x)+'}}{\mathtt{\,'+str(self.y)+'}}}}$'

        self.ax.set_title(label=self.labelFinal, color='yellow', pad=30, fontsize=40)

        plt.subplots_adjust(top=0.87)

        #equalize the scales of the x-axis and y-axis
        self.ax.set_aspect('equal', adjustable='box')

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
            newOfset = np.c_[self.vec1[0], self.vec1[1]]
            self.q1.set_offsets(newOfset)
            self.lineX[0].set_visible(False)
            self.lineY[0].set_visible(False)
            self.startLineX[0].set_visible(True)
            self.startLineY[0].set_visible(True)
        elif(myFrame == 1):
            self.startLineX[0].set_visible(False)
            self.startLineY[0].set_visible(False)

        # Calculate the time parameter
        if(myFrame <= 100):
            tx = (abs(self.vec1[0]-self.x) * (myFrame) / 100.0) + self.vec1[0]
            ty = (abs(self.vec1[1] - self.y) * (myFrame) / 100.0) + self.vec1[1]
            newOfset = np.c_[tx, ty]
            self.q1.set_offsets(newOfset)
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

#MultiplicationVectorByMatrix2D(2, 3, 4, 6, 1, 10)