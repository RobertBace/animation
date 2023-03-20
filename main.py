import tkinter as tk
import Add2D
import Add3D
import Multiply2D
import LC2D


class main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.root.configure(background="darkgray")

        self.mainMenu()

        self.root.mainloop()


    def mainMenu(self):
        self.clear_all()

        n_rows = 4
        n_columns = 1
        for i in range(n_rows):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(n_columns):
            self.root.grid_columnconfigure(i, weight=1)

        #self.root.geometry("500x500")

        button1 = tk.Button(self.root, text="Sčítanie / Odčítanie 2 vektorov [ 2D ]",
                           command= self.addition2D, bg="chartreuse1", font=12, width=50)
        button1.grid(row=0, pady=(30, 5), padx=50)



        button4 = tk.Button(self.root, text="Násobenie vektora [ 2D ]",
                            command= self.multiplication2D, bg="chartreuse1", font=12, width=50)
        button4.grid(row=1, pady=5, padx=50)


        button3 = tk.Button(self.root, text="Lineárna kombinácia [ 2D ]",
                            command= self.linearCombination2D, bg="chartreuse1", font=12, width=50)
        button3.grid(row=2, pady=5, padx=50)


        button2 = tk.Button(self.root, text="Sčítanie 2 vektorov [ 3D ]",
                            command=self.addition3D, bg="chocolate1", font=12, width=50)
        button2.grid(row=3, pady=(5, 30), padx=50)

    def addition2D(self):
        self.clear_all()

        n_rows = 4
        n_columns = 7
        for i in range(n_rows):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(n_columns):
                self.root.grid_columnconfigure(i, weight=1)

        #self.root.geometry("200x190")

        labelL1 = tk.Label(self.root, text=" (", font=("Arial", 40), bg="darkgray")
        labelL1.grid(row=0, column=0, rowspan=2, pady=(0, 5))
        inputx1 = tk.Entry(self.root, width= 3, justify='center')
        inputx1.grid(row=0, column=1, pady=(5, 0))
        inputy1 = tk.Entry(self.root, width=3, justify='center')
        inputy1.grid(row=1, column=1)
        labelR1 = tk.Label(self.root, text=") ", font=("Arial", 40), bg="darkgray")
        labelR1.grid(row=0, column=2, rowspan=2, pady=(0, 5))

        input = tk.Entry(self.root, width=3, justify='center')
        input.grid(row=0, column=3, rowspan=2)

        labelL2 = tk.Label(self.root, text=" (", font=("Arial", 40), bg="darkgray")
        labelL2.grid(row=0, column=4, rowspan=2, pady=(0, 5))
        inputx2 = tk.Entry(self.root, width=3, justify='center')
        inputx2.grid(row=0, column=5, pady=(5, 0))
        inputy2 = tk.Entry(self.root, width=3, justify='center')
        inputy2.grid(row=1, column=5)
        labelR2 = tk.Label(self.root, text=") ", font=("Arial", 40), bg="darkgray")
        labelR2.grid(row=0, column=6, rowspan=2, pady=(0, 5))


        # Add the button to the main menu
        # Create the button

        button = tk.Button(self.root, text="Launch Plot",
                           command= lambda: self.launch_plot2Dadd(inputx1, inputy1, inputx2, inputy2, input.get()),
                           bg="green", width=20)
        button.grid(row= 2, column=0, columnspan=7, pady=(20,5))


        mainBut = tk.Button(self.root, text="Menu", command=self.mainMenu, bg="orange", width=20)
        mainBut.grid(row= 3, column=0, columnspan=7, pady=(5,20))

    def multiplication2D(self):
        self.clear_all()

        n_rows = 4
        n_columns = 5
        for i in range(n_rows):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(n_columns):
                self.root.grid_columnconfigure(i, weight=1)

        #self.root.geometry("200x190")

        labelL1 = tk.Label(self.root, text=" (", font=("Arial", 40), bg="darkgray")
        labelL1.grid(row=0, column=0, rowspan=2, pady=(0, 5))
        inputx1 = tk.Entry(self.root, width=3, justify='center')
        inputx1.grid(row=0, column=1, pady=(5, 0))
        inputy1 = tk.Entry(self.root, width=3, justify='center')
        inputy1.grid(row=1, column=1)
        labelR1 = tk.Label(self.root, text=") ", font=("Arial", 40), bg="darkgray")
        labelR1.grid(row=0, column=2, rowspan=2, pady=(0, 5))

        label = tk.Label(self.root, text="x ", font=("Arial", 20), bg="darkgray")
        label.grid(row=0, column=3, rowspan=2, pady=(0, 5))

        inputC = tk.Entry(self.root, width=2,font=('Arial 24'), justify='center')
        inputC.grid(row=0, column=4, rowspan=2 , padx=(0,10))


        # Add the button to the main menu
        # Create the button
        button = tk.Button(self.root, text="Launch Plot",
                           command= lambda: self.launch_plot2DMulti(inputx1, inputy1, inputC),
                           bg="green", width=15)
        button.grid(row=2, column=0, columnspan=7, pady=(20, 5))

        mainBut = tk.Button(self.root, text="Menu", command=self.mainMenu, bg="orange", width=15)
        mainBut.grid(row=3, column=0, columnspan=7, pady=(5, 15))

    def linearCombination2D(self):
        self.clear_all()

        n_rows = 4
        n_columns = 15
        for i in range(n_rows):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(n_columns):
            self.root.grid_columnconfigure(i, weight=1)

        # self.root.geometry("200x190")

        labelL1 = tk.Label(self.root, text=" (", font=("Arial", 40), bg="darkgray")
        labelL1.grid(row=0, column=0, rowspan=2, pady=(0, 5))
        inputx1 = tk.Entry(self.root, width=3, justify='center')
        inputx1.grid(row=0, column=1, pady=(5, 0))
        inputy1 = tk.Entry(self.root, width=3, justify='center')
        inputy1.grid(row=1, column=1)
        labelR1 = tk.Label(self.root, text=")", font=("Arial", 40), bg="darkgray")
        labelR1.grid(row=0, column=2, rowspan=2, pady=(0, 5))

        label1 = tk.Label(self.root, text="x", font=("Arial", 20), bg="darkgray")
        label1.grid(row=0, column=3, rowspan=2, pady=(0, 5))

        inputC1 = tk.Entry(self.root, width=2, font=('Arial 20'), justify='center')
        inputC1.grid(row=0, column=4, rowspan=2, padx=(0, 0))

        label1 = tk.Label(self.root, text="+", font=("Arial", 20), bg="darkgray")
        label1.grid(row=0, column=5, rowspan=2, pady=(0, 5))

        labelL2 = tk.Label(self.root, text="(", font=("Arial", 40), bg="darkgray")
        labelL2.grid(row=0, column=6, rowspan=2, pady=(0, 5))
        inputx2 = tk.Entry(self.root, width=3, justify='center')
        inputx2.grid(row=0, column=7, pady=(5, 0))
        inputy2 = tk.Entry(self.root, width=3, justify='center')
        inputy2.grid(row=1, column=7)
        labelR2 = tk.Label(self.root, text=")", font=("Arial", 40), bg="darkgray")
        labelR2.grid(row=0, column=8, rowspan=2, pady=(0, 5))

        label2 = tk.Label(self.root, text="x", font=("Arial", 20), bg="darkgray")
        label2.grid(row=0, column=9, rowspan=2, pady=(0, 5))

        inputC2 = tk.Entry(self.root, width=2, font=('Arial 20'), justify='center')
        inputC2.grid(row=0, column=10, rowspan=2, padx=(0, 0))

        label3 = tk.Label(self.root, text="=", font=("Arial", 20), bg="darkgray")
        label3.grid(row=0, column=11, rowspan=2, pady=(0, 5))

        labelL3 = tk.Label(self.root, text="(", font=("Arial", 40), bg="darkgray")
        labelL3.grid(row=0, column=12, rowspan=2, pady=(0, 5))
        resx = tk.Entry(self.root, width=3, justify='center')
        resx.grid(row=0, column=13, pady=(5, 0))
        resy = tk.Entry(self.root, width=3, justify='center')
        resy.grid(row=1, column=13)
        labelR3 = tk.Label(self.root, text=")", font=("Arial", 40), bg="darkgray")
        labelR3.grid(row=0, column=14, rowspan=2, pady=(0, 5))

        # Add the button to the main menu
        # Create the button

        button = tk.Button(self.root, text="Launch Plot",
                           command=lambda: self.launch_plot2DLC(inputx1, inputy1, inputC1, inputx2, inputy2, inputC2,
                                                                resx, resy),
                           bg="green", width=30)
        button.grid(row=2, column=0, columnspan=15, pady=(20, 5))

        mainBut = tk.Button(self.root, text="Menu", command=self.mainMenu, bg="orange", width=30)
        mainBut.grid(row=3, column=0, columnspan=15, pady=(5, 20))

    def addition3D(self):
        self.clear_all()

        n_rows = 4
        n_columns = 7
        for i in range(n_rows):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(n_columns):
            self.root.grid_columnconfigure(i, weight=1)

        labelx1 = tk.Label(self.root, text="1. vector: x - ", font=14, bg="darkgray")
        labelx1.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))
        inputx1 = tk.Entry(self.root, width=5, justify='center')
        inputx1.grid(row=0, column=1, pady=(10, 0))

        labely1 = tk.Label(self.root, text="; y - ", font=14, bg="darkgray")
        labely1.grid(row=0, column=2, pady=(10, 0))
        inputy1 = tk.Entry(self.root,width=5, justify='center')
        inputy1.grid(row=0, column=3, pady=(10, 0))

        labelx2 = tk.Label(self.root, text="2. vector: x - ", font=14, bg="darkgray")
        labelx2.grid(row=1, column=0, padx=(10, 0))
        inputx2 = tk.Entry(self.root, width=5, justify='center')
        inputx2.grid(row=1, column=1)

        labely2 = tk.Label(self.root, text="; y - ", font=14, bg="darkgray")
        labely2.grid(row=1, column=2)
        inputy2 = tk.Entry(self.root, width=5, justify='center')
        inputy2.grid(row=1, column=3)

        labelz1 = tk.Label(self.root, text="; z - ", font=14, bg="darkgray")
        labelz1.grid(row=0, column=4, pady=(10, 0))
        inputz1 = tk.Entry(self.root,width=5, justify='center')
        inputz1.grid(row=0, column=5,padx=(0, 10), pady=(10, 0))

        labelz2 = tk.Label(self.root, text="; z - ", font=14, bg="darkgray")
        labelz2.grid(row=1, column=4)
        inputz2 = tk.Entry(self.root, width=5, justify='center')
        inputz2.grid(row=1, column=5, padx=(0, 10))


        button = tk.Button(self.root, text="Launch Plot",
                           command= lambda: self.launch_plot3Dadd(inputx1, inputy1, inputz1, inputx2, inputy2, inputz2),
                           bg="green", width=10)
        button.grid(row=2, column=0, columnspan=7, pady=(20, 5))

        mainBut = tk.Button(self.root, text="Menu", command=self.mainMenu, bg="orange", width=10)
        mainBut.grid(row=3, column=0, columnspan=7, pady=(5, 20))



    def clear_all(self):
        for item in self.root.winfo_children():
            item.destroy()

    def launch_plot2Dadd(self, inputx1, inputy1, inputx2, inputy2, sub):
        if (sub == "+"):
            sub = False
            sign = True
        elif (sub == "-"):
            sub = True
            sign = True
        else:
            sign = False
            print("Bad choosen sign")
        try:
            x1 = float(inputx1.get())
            y1 = float(inputy1.get())
            x2 = float(inputx2.get())
            y2 = float(inputy2.get())
            correct = True
        except ValueError:
            correct = False
            print("Not a float")

        if(correct and sign):
            Add2D.AditionOfTwoVector2D(x1, y1, x2, y2,sub)

    def launch_plot2DMulti(self, inputx1, inputy1, inputC):
        try:
            x1 = float(inputx1.get())
            y1 = float(inputy1.get())
            c = float(inputC.get())
            correct = True
        except ValueError:
            correct = False
            print("Not a float")

        if(correct):
            Multiply2D.MultiplicationOfTwoVector2D(x1, y1, c)

    def launch_plot2DLC(self, inputx1, inputy1, inputC1, inputx2, inputy2, inputC2, resx, resy):
        try:
            x1 = float(inputx1.get())
            y1 = float(inputy1.get())
            c1 = float(inputC1.get())
            x2 = float(inputx2.get())
            y2 = float(inputy2.get())
            c2 = float(inputC2.get())
            resX = float(resx.get())
            resY = float(resy.get())
            correct = True
        except ValueError:
            correct = False
            print("Not a float")

        if(correct):
            LC2D.LinearCombination2D(x1,y1,c1,x2,y2,c2,resX,resY)

    def launch_plot3Dadd(self, inputx1, inputy1, inputz1, inputx2, inputy2, inputz2):
        try:
            x1 = float(inputx1.get())
            y1 = float(inputy1.get())
            z1 = float(inputz1.get())
            x2 = float(inputx2.get())
            y2 = float(inputy2.get())
            z2 = float(inputz2.get())
        except ValueError:
            print("Not a float")

        Add3D.AditionOfTwoVector3D(x1, y1, x2, y2, z1, z2)

menu = main()

#pridať label s vektormi ------------------------------------------> DONE
#nie cyklus ale zastaviť a na stlačenie klavesy spustiť -----------> DONE
#spustit ----------------------------------------------------------> DONE
# tmave pozadie ---------------------------------------------------> DONE
# po animacii vysledok --------------------------------------------> DONE
# (linearna kombinacia) -------------------------------------------> DONE
# 3 vektory c.() + cx() = vec -------------------------------------> DONE
# refactoring substraction, multiplication ------------------------> DONE