import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

import matplotlib

matplotlib.use('TkAgg')

class AditionOfTwoVector2D:
    def __init__(self, x1, y1, x2, y2, sub):
        self.vec1 = np.array([x1, y1])
        self.vec2 = np.array([x2, y2])

        # Create the figure and axis
        self.fig, self.ax = plt.subplots()

        manager = plt.get_current_fig_manager()
        manager.window.state('zoomed')

        # Set dark background
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')

        # Define the quiver plot for the vectors
        self.q1 = self.ax.quiver(0, 0, self.vec1[0], self.vec1[1], angles='xy', scale_units='xy', scale=1, color='blue')
        self.q2 = self.ax.quiver(0, 0, self.vec2[0], self.vec2[1], angles='xy', scale_units='xy', scale=1, color='green')
        self.q3 = self.ax.quiver(0, 0, self.vec1[0] + self.vec2[0], self.vec1[1] + self.vec2[1], angles='xy',
                                 scale_units='xy',scale=1, color='red')
        self.q4 = self.ax.quiver(0, 0, self.vec1[0] - self.vec2[0], self.vec1[1] - self.vec2[1], angles='xy',
                                 scale_units='xy',scale=1, color='red')
        self.q3.set_visible(False)
        self.q4.set_visible(False)

        if(sub):
            x = self.vec1[0] - self.vec2[0]
            y = self.vec1[1] - self.vec2[1]
        else:
            x = self.vec1[0] + self.vec2[0]
            y = self.vec1[1] + self.vec2[1]
        self.lineX = self.ax.plot([0, x], [y, y], 'r--', label='line')
        self.lineY = self.ax.plot([x, x], [0, y], 'r--', label='line')
        self.lineX[0].set_visible(False)
        self.lineY[0].set_visible(False)

        if(sub):
            arrayX = [self.vec1[0], self.vec2[0], self.vec1[0] + self.vec2[0], self.vec1[0] - self.vec2[0], 0]
            arrayY = [self.vec1[1], self.vec2[1], self.vec1[1] + self.vec2[1], self.vec1[1] - self.vec2[1], 0]
            plt.xticks(np.arange(min(arrayX) - 1, max(arrayX) + 2, 1))
            plt.yticks(np.arange(min(arrayY) - 1, max(arrayY) + 2, 1))
        else:
            arrayX = [self.vec1[0], self.vec2[0], self.vec1[0] + self.vec2[0],0]
            arrayY = [self.vec1[1], self.vec2[1], self.vec1[1] + self.vec2[1],0]
            plt.xticks(np.arange(min(arrayX)-1, max(arrayX)+2, 1))
            plt.yticks(np.arange(min(arrayY)-1, max(arrayY)+2, 1))

        self.ax.spines['left'].set_position(('data', 0.0))
        self.ax.spines['bottom'].set_position(('data', 0.0))
        self.ax.spines['left'].set_color('yellow')
        self.ax.spines['bottom'].set_color('yellow')
        self.ax.spines['left'].set_linewidth(3)
        self.ax.spines['bottom'].set_linewidth(3)
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')

        # set numbers color
        self.ax.tick_params(axis='x', colors='yellow', size=8, labelsize=14)
        self.ax.tick_params(axis='y', colors='yellow', size=8, labelsize=14)

        # Define a flag to indicate if the animation is paused
        self.pause = False

        # Define a variable to store the animation object
        self.ani = None

        # Create the animation
        if (sub):
            self.ani = animation.FuncAnimation(self.fig, self.updateSub, frames=203, interval=1, blit=True)
        else:
            self.ani = animation.FuncAnimation(self.fig, self.updateAdd, frames=102, interval=1, blit=True) # frames - 102 (0-100)[101] + 1 (vykreslovanie)

        # Connect the mouse button click event to the onClick function
        self.fig.canvas.mpl_connect('key_press_event', self.onClick)

        # Display the animation

        if(sub):
            sign = ' - '
        else:
            sign = ' + '

        self.label = r'$\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(x1)+'}}{\mathtt{\,'+str(y1)+'}}'+sign+'' \
                 '\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(x2)+'}}{\mathtt{\,'+str(y2)+'}} =}}$'

        if(sub):
            self.labelFinal = r'$\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(x1)+'}}{\mathtt{\,'+str(y1)+'}}'+sign+'' \
                          '\genfrac{(}{)}{0}{3}{\mathtt{\,' + str(x2) + '}}{\mathtt{\,' + str(y2) + '}} = ' \
                          '\genfrac{(}{)}{0}{3}{\mathtt{\,' + str(x1 - x2) + '}}{\mathtt{\,' + str(y1 - y2) + '}}$'
        else:
            self.labelFinal = r'$\genfrac{(}{)}{0}{3}{\mathtt{\,' + str(x1) + '}}{\mathtt{\,' + str(y1) + '}}' + sign + '' \
                                '\genfrac{(}{)}{0}{3}{\mathtt{\,' + str(x2) + '}}{\mathtt{\,' + str(y2) + '}} = ' \
                                '\genfrac{(}{)}{0}{3}{\mathtt{\,' + str(x1 - x2) + '}}{\mathtt{\,' + str(y1 - y2) + '}}$'


        self.ax.set_title(label=self.label, color='yellow', pad=30, fontsize=40)

        # equalize the scales of the x-axis and y-axis
        self.ax.set_aspect('equal', adjustable='box')

        plt.subplots_adjust(top=0.8)

        plt.show(block=True)

    # Define the update function for the animation
    def updateAdd(self, frame):
        if(frame >= 1):
            myFrame = frame - 1
        else:
            myFrame = -1

        if (self.ani):
            #self.ani.event_source.stop()
            if (myFrame == 0 or myFrame == 100):
                self.pause = True
                self.ani.event_source.stop()

        if(myFrame <= 100 and myFrame >= 0):
            t = ((myFrame) / 100.0) * self.vec1
            self.q2.set_offsets(t)

            if np.array_equal(t, self.vec1):
                self.q3.set_visible(True)
                self.lineX[0].set_visible(True)
                self.lineY[0].set_visible(True)
                self.ax.set_title(label=self.labelFinal, color='yellow', pad=30, fontsize=40)
                self.fig.canvas.draw()
            else:
                self.q3.set_visible(False)
                self.lineX[0].set_visible(False)
                self.lineY[0].set_visible(False)
                if (self.ani):
                    self.ax.set_title(label=self.label, color='yellow', pad=30, fontsize=40)
                self.fig.canvas.draw()

            # Redraw the plot
            #self.fig.canvas.draw()

        return self.q1, self.q2, self.q3, self.lineX[0], self.lineY[0]

    def updateSub(self, frame):
        if (frame >= 1):
            myFrame = frame - 1
        else:
            myFrame = -1

        if (self.ani):
            # self.ani.event_source.stop()
            if (myFrame == 0 or myFrame == 201):
                self.pause = True
                self.ani.event_source.stop()



        if(myFrame == 0):
            self.q2.set_UVC(self.vec2[0], self.vec2[1])
            self.q4.set_visible(False)
            self.lineX[0].set_visible(False)
            self.lineY[0].set_visible(False)
        # Calculate the time parameter
        if(myFrame <= 100):
            t = ((myFrame) / 100.0) * self.vec1
            self.q2.set_offsets(t)
            if (self.ani):
                self.ax.set_title(label=self.label, color='yellow', pad=30, fontsize=40)
            # Redraw the plot
            self.fig.canvas.draw()

        elif(myFrame <= 200):
            t = (100 - (myFrame - 100) * 2)/100.0 * self.vec2
            self.q2.set_UVC(t[0], t[1])

            # Redraw the plot
            self.fig.canvas.draw()
        else:
            self.q4.set_visible(True)
            self.lineX[0].set_visible(True)
            self.lineY[0].set_visible(True)
            if (self.ani):
                self.ax.set_title(label=self.labelFinal, color='yellow', pad=30, fontsize=40)
            self.fig.canvas.draw()


            #plt.show()
        return self.q1, self.q2, self.q3, self.q4, self.lineX[0], self.lineY[0]

    # Define a function to pause the animation when the mouse button is clicked
    def onClick(self, event):
        if event.key == ' ':
            #global self.pause
            self.pause ^= True
            if self.pause:
                self.ani.event_source.stop()
            else:
                self.ani.event_source.start()

#AditionOfTwoVector2D(1,3,3,1,0)