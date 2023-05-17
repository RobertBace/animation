import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import ctypes

import matplotlib

matplotlib.use('TkAgg')

class MultiplicationVectorByMatrix2D:

    def __init__(self, x1, y1, x2, y2, vectorX, vectorY):
        self.vec1 = np.array([vectorX, vectorY])
        self.matrix = [[x1, y1], [x2, y2]]

        # Create the figure and axis
        self.fig, self.ax = plt.subplots()

        self.manager = plt.get_current_fig_manager()
        self.manager.window.state('zoomed')


        # Set dark background
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')

        # Define the scatter plot for the vectors

        self.q1 = self.ax.scatter(vectorX, vectorY, color='red')
        self.q3 = self.ax.quiver(0, 0, self.matrix[0][0], self.matrix[0][1], angles='xy', scale_units='xy', scale=1, color='green')
        self.q4 = self.ax.quiver(0, 0, self.matrix[1][0], self.matrix[1][1], angles='xy', scale_units='xy', scale=1, color='blue')

        self.x = vectorX * x1 + vectorY * x2
        self.y = vectorX * y1 + vectorY * y2

        self.q2 = self.ax.scatter(self.x, self.y, color='red')
        self.q2.set_visible(False)

        self.lineX = self.ax.plot([0, self.x], [self.y, self.y], 'r:', label='line', linewidth = 1)
        self.lineY = self.ax.plot([self.x, self.x], [0, self.y], 'r:', label='line', linewidth = 1)
        self.startLineX = self.ax.plot([0, vectorX], [vectorY, vectorY], 'r:', label='line', linewidth=1)
        self.startLineY = self.ax.plot([vectorX, vectorX], [0, vectorY], 'r:', label='line', linewidth=1)
        self.lineX[0].set_visible(False)
        self.lineY[0].set_visible(False)

        arrayX = [self.vec1[0], x1, x2, self.x, 0,self.vec1[0]* x1,self.vec1[1]* x2]
        arrayY = [self.vec1[1], y1, y2, self.y, 0,self.vec1[0]* y1,self.vec1[1]* y2]

        lin = self.axis(min(arrayX) - 1, max(arrayX) + 2, min(arrayY) - 1, max(arrayY) + 2, x1, y1)
        self.ax.plot(lin[0], lin[1],"w-", linewidth=1)
        lin = self.axis(min(arrayX) - 1, max(arrayX) + 2, min(arrayY) - 1, max(arrayY) + 2, x2, y2)
        self.ax.plot(lin[0], lin[1], 'w-', linewidth=1)
        self.ax.plot([self.x, self.vec1[0]* x1], [self.y, self.vec1[0]* y1], 'w:', linewidth=1)
        self.ax.plot([self.x, self.vec1[1]* x2], [self.y, self.vec1[1]* y2], 'w:', linewidth=1)

        fsxMax = (max(arrayX) + 2) - (min(arrayX) - 1)
        fsyMax = (max(arrayY) + 2) - (min(arrayY) - 1)

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


        self.pause = False

        self.ani = None

        self.ani = animation.FuncAnimation(self.fig, self.update, frames=203, interval=5)

        # Connect the mouse button click event to the onClick function
        self.fig.canvas.mpl_connect('key_press_event', self.onClick)

        self.label = r'$\genfrac{(}{)}{0}{1}{\mathtt{\,' + str(x1) + "\ \;" + str(x2) + '}}{\mathtt{\,' + \
                     str(y1) + "\ \;" + str(y2) + '}}\;\cdot\;\genfrac{(}{)}{0}{1}{\mathtt{\,'+\
                     str(vectorX)+'}}{\mathtt{\,'+str(vectorY)+'}}}}$'

        self.labelFinal = r'$\genfrac{(}{)}{0}{1}{\mathtt{\,' + str(x1) + "\ \;" + str(x2) + '}}{\mathtt{\,' + \
                     str(y1) + "\ \;" + str(y2) + '}}\;\cdot\;\genfrac{(}{)}{0}{1}{\mathtt{\,'+\
                     str(vectorX)+'}}{\mathtt{\,'+str(vectorY)+'}}\,=\,\genfrac{(}{)}{0}{1}{\mathtt{\,'+\
                     str(self.x)+'}}{\mathtt{\,'+str(self.y)+'}}}}$'

        plt.xlim([min(arrayX) - 1, max(arrayX) + 2])
        plt.ylim([min(arrayY) - 1, max(arrayY) + 2])

        self.ax.set_title(label=self.label, color='yellow', pad=30, fontsize=40)
        plt.subplots_adjust(top=0.8)

        #equalize the scales of the x-axis and y-axis
        #self.ax.set_aspect('equal', adjustable='box')
        plt.pause(0.0001)
        self.drawAxis(fsxMax, fsyMax, arrayX)
        
        plt.show(block=False)

    def drawAxis(self, fsxMax, fsyMax, arrayX):
        w, h = self.manager.canvas.get_width_height()
        w = (w * self.ax.get_position().width) / (fsxMax)
        h = (h * self.ax.get_position().height) / (fsyMax)
        alfa = math.atan((self.matrix[0][1] * h) / (self.matrix[0][0] * w)) * 180 / math.pi
        for i in range(min(arrayX) - 1 - self.mod(min(arrayX) - 1, abs(self.matrix[0][0])), max(arrayX) + 2,
                       self.matrix[0][0]):
            if (i != 0):
                angle = math.atan(self.matrix[0][1] / self.matrix[0][0]) * 180 / math.pi
                self.ax.plot([i, i + math.cos(math.radians(alfa - 90)) / w * 10],
                             [i * (self.matrix[0][1] / self.matrix[0][0]),
                              i * (self.matrix[0][1] / self.matrix[0][0]) + math.sin(math.radians(alfa - 90)) / h * 10],
                             'w-', linewidth=1)

                anotX = i + math.cos(math.radians(alfa - 90)) / w * 30
                anotY = i * (self.matrix[0][1] / self.matrix[0][0]) + math.sin(math.radians(alfa - 90)) / h * 30
                self.ax.annotate(str(i), xy=(anotX, anotY),
                                 xytext=(anotX, anotY), color='white', fontsize=14, rotation=alfa, ha='center',
                                 va='center')

        w, h = self.manager.canvas.get_width_height()
        w = (w * self.ax.get_position().width) / (fsxMax)
        h = (h * self.ax.get_position().height) / (fsyMax)
        alfa = math.atan((self.matrix[1][1] * h) / (self.matrix[1][0] * w)) * 180 / math.pi
        for i in range(min(arrayX) - 1 - self.mod(min(arrayX) - 1, abs(self.matrix[1][0])), max(arrayX) + 2,
                       self.matrix[1][0]):
            if (i != 0):
                angle = math.atan(self.matrix[1][1] / self.matrix[1][0]) * 180 / math.pi
                self.ax.plot([i, i + math.cos(math.radians(alfa - 90)) / w * 10],
                             [i * (self.matrix[1][1] / self.matrix[1][0]),
                              i * (self.matrix[1][1] / self.matrix[1][0]) + math.sin(math.radians(alfa - 90)) / h * 10],
                             'w-', linewidth=1)

                anotX = i + math.cos(math.radians(alfa - 90)) / w * 30
                anotY = i * (self.matrix[1][1] / self.matrix[1][0]) + math.sin(math.radians(alfa - 90)) / h * 30
                self.ax.annotate(str(i), xy=(anotX, anotY),
                                 xytext=(anotX, anotY), color='white', fontsize=14, rotation=alfa, ha='center',
                                 va='center')

    def update(self, frame):
        if (frame >= 1):
            myFrame = frame - 1
        else:
            myFrame = -1

        if (self.ani):
            # self.ani.event_source.stop()
            if (myFrame == 0):
                self.pause = True
                self.ani.event_source.stop()

        if(myFrame == 0):
            if (self.ani):
                self.q2.set_visible(False)
                self.q3.set_visible(True)
                self.q4.set_visible(True)
                self.q4.set_offsets([0, 0])
                self.q1.set_visible(True)
                self.lineX[0].set_visible(False)
                self.lineY[0].set_visible(False)
                self.startLineX[0].set_visible(True)
                self.startLineY[0].set_visible(True)
                self.ax.set_title(label=self.label, color='yellow', pad=30, fontsize=40)
        elif(myFrame == 1):
            self.startLineX[0].set_visible(False)
            self.startLineY[0].set_visible(False)
            self.q1.set_visible(False)

        # Calculate the time parameter
        if(myFrame <= 100):
            if (self.ani):
                t = [((self.vec1[0] - 1) * (myFrame) / 100.0) * i for i in self.matrix[0]]
                t = [t[0] + self.matrix[0][0], t[1] + self.matrix[0][1]]
                self.q3.set_UVC(t[0], t[1])

                t = [((self.vec1[1] - 1) * (myFrame) / 100.0) * i for i in self.matrix[1]]
                t = [t[0] + self.matrix[1][0], t[1] + self.matrix[1][1]]
                self.q4.set_UVC(t[0], t[1])
        elif (myFrame <= 200):
            t = [((myFrame - 100) / 100.0) * self.vec1[0] * i for i in self.matrix[0]]
            self.q4.set_offsets(t)


        if(myFrame == 200):

            if (self.ani):
                self.ax.set_title(label=self.labelFinal, color='yellow', pad=30, fontsize=40)
            self.pause = True
            self.ani.event_source.stop()
            # Redraw the plot

        if (myFrame == 201):
            self.q1.set_visible(True)
            self.startLineX[0].set_visible(True)
            self.startLineY[0].set_visible(True)
            self.lineX[0].set_visible(True)
            self.lineY[0].set_visible(True)
            self.q2.set_visible(True)
            self.q3.set_visible(False)
            self.q4.set_visible(False)
            self.pause = True
            self.ani.event_source.stop()

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

    def axis(self, xmin, xmax, ymin, ymax, x, y):
        a = x / y

        if (a < 0.5):
            rx1 = ymin * a
            rx2 = ymax * a
            ry1 = ymin
            ry2 = ymax
        else:
            rx1 = xmin
            rx2 = xmax
            ry1 = xmin / a
            ry2 = xmax / a
        return [[rx1, rx2], [ry1, ry2]]

    def mod(self, a, b):
        result = a % b
        if result == 0:
            return 0
        elif a < 0:
            return b - abs(result)
        else:
            return result


