import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

import matplotlib

matplotlib.use('TkAgg')

class LinearCombination2D:
    def __init__(self, x1, y1, c1, x2, y2, c2, resX, resY):
        self.vec1 = np.array([x1, y1])
        self.vec2 = np.array([x2, y2])
        self.vec3 = np.array([resX, resY])
        self.const1 = c1
        self.const2 = c2

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
        self.q3 = self.ax.quiver(0, 0, self.vec3[0], self.vec3[1], angles='xy',scale_units='xy',scale=1, color='red')
        self.q3.set_visible(False)

        x = self.vec3[0]
        y = self.vec3[1]
        self.lineXR = self.ax.plot([0, x], [y, y], 'r--', label='line')
        self.lineYR = self.ax.plot([x, x], [0, y], 'r--', label='line')
        self.lineXR[0].set_visible(False)
        self.lineYR[0].set_visible(False)

        x = self.vec1[0]*c1 + self.vec2[0]*c2
        y = self.vec1[1]*c1 + self.vec2[1]*c2
        self.lineX = self.ax.plot([0, x], [y, y], 'g--', label='line')
        self.lineY = self.ax.plot([x, x], [0, y], 'g--', label='line')
        self.lineX[0].set_visible(False)
        self.lineY[0].set_visible(False)


        arrayX = [self.vec1[0], self.vec2[0], self.vec1[0]*c1, self.vec2[0]*c2, self.vec1[0]*c1 + self.vec2[0]*c2, 0]
        arrayY = [self.vec1[1], self.vec2[1], self.vec1[1]*c1, self.vec2[1]*c2, self.vec1[1]*c1 + self.vec2[1]*c2, 0]
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

        self.ani = animation.FuncAnimation(self.fig, self.update, frames=202, interval=1, blit=True) # frames - 102 (0-100)[101] + 1 (vykreslovanie)

        # Connect the mouse button click event to the onClick function
        self.fig.canvas.mpl_connect('key_press_event', self.onClick)

        # Display the animation

        self.label = r'$\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(x1)+'}}{\mathtt{\,'+str(y1)+'}}\;x\;' + str(c1) + '\;+\;' \
                 '\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(x2)+'}}{\mathtt{\,'+str(y2)+'}}\;x\;' + str(c1) + '\;=\;''}}$'

        if(x1*c1 + x2*c2 == resX  and y1*c1 + y2*c2 == resY):
            self.labelFinal = r'$\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(x1)+'}}{\mathtt{\,'+str(y1)+'}}\;x\;' + str(c1) + '\;+\;' \
                 '\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(x2)+'}}{\mathtt{\,'+str(y2)+'}}\;x\;' + str(c1) + '\;=\;''' \
                 '\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(resX)+'}}{\mathtt{\,'+str(resY)+'}}}}$'
        else:
            self.labelFinal = r'$\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(x1)+'}}{\mathtt{\,'+str(y1)+'}}\;x\;' + str(c1) + '\;+\;' \
                 '\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(x2)+'}}{\mathtt{\,'+str(y2)+'}}\;x\;' + str(c1) + '\;≠\;''' \
                 '\genfrac{(}{)}{0}{3}{\mathtt{\,'+str(resX)+'}}{\mathtt{\,'+str(resY)+'}}}}$'


        self.ax.set_title(label=self.label, color='yellow', pad=30, fontsize=40)

        plt.subplots_adjust(top=0.8)

        # equalize the scales of the x-axis and y-axis
        self.ax.set_aspect('equal', adjustable='box')

        plt.show(block=True)

    # Define the update function for the animation
    def update(self, frame):

        if(frame >= 1):
            myFrame = frame - 1
        else:
            myFrame = -1
        if(myFrame >= 0):
            if (self.ani):
                #self.ani.event_source.stop()
                if (myFrame == 0 or myFrame == 200):
                    self.pause = True
                    self.ani.event_source.stop()

            if (myFrame == 0):
                self.q2.set_offsets([0,0])
                self.lineX[0].set_visible(False)
                self.lineY[0].set_visible(False)
                self.lineXR[0].set_visible(False)
                self.lineYR[0].set_visible(False)
                self.q3.set_visible(False)
                if (self.ani):
                    self.ax.set_title(label=self.label, color='yellow', pad=30, fontsize=40)

            if (myFrame <= 100):
                t = [((self.const1 - 1) * (myFrame) / 100.0) * i for i in self.vec1]
                t = t + self.vec1
                self.q1.set_UVC(t[0], t[1])

                t = [((self.const2 - 1) * (myFrame) / 100.0) * i for i in self.vec2]
                t = t + self.vec2
                self.q2.set_UVC(t[0], t[1])
            elif(myFrame <= 200):
                t = ((myFrame-100) / 100.0) * self.vec1*self.const1
                self.q2.set_offsets(t)
                if(frame == 200):
                    self.q3.set_visible(True)
                    self.lineX[0].set_visible(True)
                    self.lineY[0].set_visible(True)
                    self.lineXR[0].set_visible(True)
                    self.lineYR[0].set_visible(True)
                    if (self.ani):
                        self.ax.set_title(label=self.labelFinal, color='yellow', pad=30, fontsize=40)

        self.fig.canvas.draw()

        return self.q1, self.q2, self.q3, self.lineX[0], self.lineY[0], self.lineXR[0], self.lineYR[0]



    # Define a function to pause the animation when the mouse button is clicked
    def onClick(self, event):
        if event.key == ' ':
            #global self.pause
            self.pause ^= True
            if self.pause:
                self.ani.event_source.stop()
            else:
                self.ani.event_source.start()

#LinearCombination2D(2,3,2,3,1,2,8,8)