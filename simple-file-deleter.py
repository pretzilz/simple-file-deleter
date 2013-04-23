from tkinter import *

class Application(Frame):
    """Simple file deleter."""
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
        #Sample Frame:
        #Frame(height=2, bd=1, relief=SUNKEN
        #      ).grid(row = 0, column = 2, sticky = W)

        #An Example Drop Down Menu
        #OptionMenu(self, "default selection", "one", "two", "three"
        #          ).grid(row = 5, column = 2, sticky = W)

        #Deleting a specific type of file:
        self.FileExtention = IntVar() 
        Checkbutton(self, text = "By file extention:",
                                          variable = self.FileExtention
                                          ).grid(row = 2, column = 0, sticky = W)
        self.userFileExtention = Entry(self)
        self.userFileExtention.grid(row = 3, column = 0, sticky = W)


        self.FilenameContains = IntVar()
        Checkbutton(self, text = "Filename contains:",
                                        variable = self.FilenameContains
                                        ).grid(row = 5, column = 0, sticky = W)
        self.UserFilenameContains = Entry(self)
        self.UserFilenameContains.grid(row = 6, column = 0, sticky = W)


        self.OlderThan = IntVar()
        Checkbutton(self, text = "Files older than:",
                                      variable = self.OlderThan
                                      ).grid(row = 7, column = 0, sticky = W)
        #For older than, we need a drop down with presets (one day, week, month, six months, year)
        ###################################
        #Presets: (For these, no entry is needed)
        
        self.DeleteAllTorrents = IntVar()
        Checkbutton(self, text = "Delete all .torrent files",
                                              variable = self.DeleteAllTorrents
                                              ).grid(row = 2, column = 3, sticky = W)

        self.DeleteAllInstallers = IntVar()
        Checkbutton(self, text = "Delete all installers",
                                                variable = self.DeleteAllInstallers
                                                ).grid(row = 3, column = 3, sticky = W)

        self.DeleteAllDocuments = IntVar()
        Checkbutton(self, text = "Delete all documents",
                                               variable = self.DeleteAllDocuments
                                               ).grid(row = 4, column = 3, sticky = W)
        

        self.DeleteAllPictures = IntVar()
        Checkbutton(self, text = "Delete all pictures",
                                              variable = self.DeleteAllPictures
                                              ).grid(row = 5, column = 3, sticky = W)

        
        #Any other options?
        ####################################
        #Need divider here to separate bottom from top

        #CAUTION: THIS NEEDS TO BE MODIFIED EVERYTIME A BUTTON IS ADDED

        Label(self,
              text = "Global Options:"
              ).grid(row = 8, column = 2, sticky = W)

        self.MoveToRecycle = IntVar()
        Checkbutton(self, text = "Move deleted files to recycle bin",
                                                     variable = self.MoveToRecycle
                                                     ).grid(row = 9, column = 0, sticky = W)

        self.DeleteSubDirectories = IntVar()
        Checkbutton(self, text = "Delete files from all subdirectories",
                                                    variable = self.DeleteSubDirectories
                                                    ).grid(row = 9, column = 3, sticky = W)

        Button(self,
               text = "Delete",
               command = self.init_delete
               ).grid(row = 10, column = 2, sticky = W)




    def init_delete(self):
        if self.DeleteAllDocuments.get() == 1:
            self.delete("documents")
        elif self.DeleteAllPictures.get() == 1:
            self.delete("pictures")
        elif self.DeleteAllTorrents.get() == 1:
            self.delete("torrents")
        elif self.FileExtention.get() == 1:
            self.delete("extention")
        elif self.FilenameContains.get() == 1:
            self.delete("filename")
        elif self.DeleteAllInstallers.get() == 1:
            self.delete("installers")




    def delete(self, Filetype):
        
        #Delete things in subdirectories? (Include as global option)
        #http://tuxbalaji.wordpress.com/2012/10/28/how-to-delete-files-in-python/

        #Consider adding file extentions to a data file
        import os
        import re
        if Filetype == "documents": #Deletes all documents
            filelist = [f for f in os.listdir(".") if f.endswith(".doc")
                        or f.endswith(".txt") or f.endswith(".docx")]
            for f in filelist:
                os.remove(f)
                
        if Filetype == "pictures": #Deletes all pictures
            filelist = [f for f in os.listdir(".") if f.endswith(".jpg")
                        or f.endswith(".gif") or f.endswith(".png")
                        or f.endswith(".bmp") or f.endswith(".tiff")]
            for f in filelist:
                os.remove(f)

        if Filetype == "torrents": #Deletes all pictures
            filelist = [f for f in os.listdir(".") if f.endswith(".torrent")]
            for f in filelist:
                os.remove(f)
        
        if Filetype == "extention":
            
            userExtention = self.userFileExtention.get()
            #Need exception if what user enters does not start with a period
            filelist = [f for f in os.listdir(".") if f.endswith(userExtention)]
            for f in filelist:
                os.remove(f)



        if Filetype == "filename":
            userFilename = self.UserFilenameContains.get()
            filelist = [f for f in os.listdir(".")] #Lists all files in the directory
            for f in filelist:
                current_file = os.path.splitext(f)[0] #Saves only the filename without the extention
                if re.search(userFilename, current_file): #Scans for the file
                    os.remove(f)

        if Filetype == "installers":
            filelist = [f for f in os.listdir(".")] #Lists all files in the directory
            for f in filelist:
                current_file = os.path.splitext(f)[0] #Saves only the filename without the extention
                if re.search('install', current_file) or re.search('setup', current_file): #Works for now
                    os.remove(f)

# main
root = Tk()
root.title("File Deleter") #Sets title of window
app = Application(root)
root.mainloop() #Begins application
