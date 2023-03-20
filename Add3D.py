import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

matplotlib.use('TkAgg')

class AditionOfTwoVector3D:
    def __init__(self, x1, y1, x2, y2, z1, z2):
        # Attaching 3D axis to the figure
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection="3d")

        self.vec1 = np.array([x1, y1, z1])
        self.vec2 = np.array([x2, y2, z2])
        self.q = self.ax.quiver(0, 0, 0, *self.vec1, color='blue')
        self.q1 = self.ax.quiver(0, 0, 0, *self.vec2, color='green')
        self.q2 = self.ax.quiver(0, 0, 0, self.vec1[0] + self.vec2[0], self.vec1[1] +
                                 self.vec2[1], self.vec1[2] + self.vec2[2], color='red')
        self.q2.set_visible(False)

        # Setting the axes properties
        self.ax.set(xlim3d=(0, 8), xlabel='X')
        self.ax.set(ylim3d=(0, 8), ylabel='Y')
        self.ax.set(zlim3d=(0, 8), zlabel='Z')

        # Creating the Animation object
        self.anim_running = True
        self.anim = animation.FuncAnimation(self.fig, self.update, interval=50, frames=100)

        # Adding a button for pausing the animation
        self.fig.canvas.mpl_connect('key_press_event', self.onClick)

        plt.show()
    def update(self, frames):
        t = [round(i * ((frames + 1) / 100.0),2) for i in self.vec1]

        self.q1.remove()
        self.q1 = self.ax.quiver(*t, *self.vec2, color='green')

        if np.array_equal(t+[0.01,0.01,0.01]*self.vec1,self.vec1) or np.array_equal(t, self.vec1):
            self.q2.set_visible(True)
            self.fig.canvas.draw()
        else:
            self.q2.set_visible(False)

        if np.array_equal(t, self.vec1):
            time.sleep(1)
            # q3.set_visible(False)

        return self.q


    def onClick(self, event):
        if event.key == ' ':
            if self.anim_running:
                self.anim.event_source.stop()
                self.anim_running = False
            else:
                self.anim.event_source.start()
                self.anim_running = True