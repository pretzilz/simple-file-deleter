from tkinter import *

class Application(Frame):
    """Finds permutations of a user-entered word that are english words."""
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  #Initalizing the application
        self.grid()
        self.create_widgets() #Creates the widgets
    def create_widgets(self):
        
        Label(self,
              text = "Delete a specific type of file:"
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,
              text = "Presets:"
              ).grid(row = 0, column = 3, sticky = W)
        #Divide the two parts of the program
        #Frame(height=2, bd=1, relief=SUNKEN
        #      ).grid(row = 0, column = 2, sticky = W)

        #An Example Drop Down Menu
        #OptionMenu(self, "butts", "one", "two", "three"
        #          ).grid(row = 5, column = 2, sticky = W)

        #Deleting a specific type of file:
        FileExtentionButton = Checkbutton(self, text = "By file extention:",
                                          onvalue = 1, offvalue = 0
                                          ).grid(row = 2, column = 0, sticky = W)
        self.userFileExtention = Entry(self)
        self.userFileExtention.grid(row = 3, column = 0, sticky = W)

        FilenameContainsButton = Checkbutton(self, text = "Filename contains:",
                                        onvalue = 1, offvalue = 0
                                        ).grid(row = 5, column = 0, sticky = W)
        self.FilenameContains = Entry(self)
        self.FilenameContains.grid(row = 6, column = 0, sticky = W)
        OlderThanButton = Checkbutton(self, text = "Files older than:",
                                      onvalue = 1, offvalue = 0
                                      ).grid(row = 7, column = 0, sticky = W)
        #For older than, we need a drop down with presets (one day, week, month, six months, year)
        ###################################
        #Presets: (For these, no entry is needed)

        DeleteAllTorrentsButton = Checkbutton(self, text = "Delete all .torrent files",
                                              onvalue = 1, offvalue = 0
                                              ).grid(row = 2, column = 3, sticky = W)
        DeleteAllInstallersButton = Checkbutton(self, text = "Delete all installers",
                                                onvalue = 1, offvalue = 0
                                                ).grid(row = 3, column = 3, sticky = W)
        DeleteAllDocumentsButton = Checkbutton(self, text = "Delete all documents",
                                               onvalue = 1, offvalue = 0
                                               ).grid(row = 4, column = 3, sticky = W)
        DeleteAllPicturesButton = Checkbutton(self, text = "Delete all pictures",
                                              onvalue = 1, offvalue = 0
                                              ).grid(row = 5, column = 3, sticky = W)
        #Any other options?
        ####################################
        #Need divider here to separate bottom from top

        #CAUTION: THIS NEEDS TO BE MODIFIED EVERYTIME A BUTTON IS ADDED

        Label(self,
              text = "Global Options:"
              ).grid(row = 8, column = 2, sticky = W)
        MoveAllFilesToRecycleBinButton = Checkbutton(self, text = "Move deleted files to recycle bin",
                                                     onvalue = 1, offvalue = 0
                                                     ).grid(row = 9, column = 0, sticky = W)

# main
root = Tk()
root.title("File Deleter") #Sets title of window
app = Application(root)
root.mainloop() #Begins application
