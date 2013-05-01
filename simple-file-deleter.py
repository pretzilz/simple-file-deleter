################################
# simple-file-deleter.py
# Written by Kurt Kaufman
# V. 1.0 Beta
# 4/30/13
###############################

from tkinter import *
import time, os.path, datetime

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
        #Deleting a specific type of file:
        self.FileExtention = IntVar() 
        Checkbutton(self, text = "By file extention:",
                                          variable = self.FileExtention
                                          ).grid(row = 2, column = 0, sticky = W)
        self.userFileExtention = Entry(self)
        self.userFileExtention.grid(row = 3, column = 0, sticky = W)


        self.FilenameContains = IntVar()
        Checkbutton(self, text = "Filename contains: (Case Sensitive)",
                                        variable = self.FilenameContains
                                        ).grid(row = 5, column = 0, sticky = W)
        self.UserFilenameContains = Entry(self)
        self.UserFilenameContains.grid(row = 6, column = 0, sticky = W)


        self.OlderThan = IntVar()
        Checkbutton(self, text = "Files created before:",
                                      variable = self.OlderThan
                                      ).grid(row = 7, column = 0, sticky = W)
        
        self.SelectedOlderThan = StringVar()
        self.SelectedOlderThan.set('Select A Time...') #Remember that if it equals this when called, raise an error
        choices = ['Select A Day...', 'Today', 'Yesterday', 'One Week', 'One Month','One Year']
        OlderThanDropDown = OptionMenu(self, self.SelectedOlderThan, *choices
                                       ).grid(row = 8, column = 0, sticky = W)


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
        Button(self,
               text = "Delete",
               command = self.init_delete
               ).grid(row = 11, column = 2, sticky = W)

        self.StatusVar = StringVar()
        self.StatusVar.set('')
        self.StatusLabel = Label(self,
                                textvariable = self.StatusVar
                                 ).grid(row = 12, column = 0, sticky = W)
        


    def init_delete(self):
        self.StatusVar.set('Deleting...')
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
        elif self.OlderThan.get() == 1:
            self.delete("olderthan")
        else:
            self.StatusVar.set('Please select an option.')



    def delete(self, Filetype):
        import os
        import re
        if Filetype == "documents": #Deletes all documents
            filelist = [f for f in os.listdir(".") if f.endswith(".doc")
                        or f.endswith(".txt") or f.endswith(".docx")]
            for f in filelist:
                os.remove(f)
            self.StatusVar.set('Deleted.')
                
        if Filetype == "pictures": #Deletes all pictures
            filelist = [f for f in os.listdir(".") if f.endswith(".jpg")
                        or f.endswith(".gif") or f.endswith(".png")
                        or f.endswith(".bmp") or f.endswith(".tiff")]
            for f in filelist:
                os.remove(f)
            self.StatusVar.set('Deleted.')

        if Filetype == "torrents": #Deletes all pictures
            filelist = [f for f in os.listdir(".") if f.endswith(".torrent")]
            for f in filelist:
                os.remove(f)
            self.StatusVar.set('Deleted.')
        
        if Filetype == "extention":
            userExtention = self.userFileExtention.get()
            if not re.search(r'^\.', userExtention):
                self.StatusVar.set('Please enter an extention that begins with a period.')
            else:  
                filelist = [f for f in os.listdir(".") if f.endswith(userExtention)]
                for f in filelist:
                    os.remove(f)
                self.StatusVar.set('Deleted.')

        if Filetype == "filename":
            userFilename = self.UserFilenameContains.get()
            filelist = [f for f in os.listdir(".")] #Lists all files in the directory
            for f in filelist:
                current_file = os.path.splitext(f)[0] #Saves only the filename without the extention
                if re.search(userFilename, current_file): #Scans for the file
                    os.remove(f)
            self.StatusVar.set('Deleted.')

        if Filetype == "installers":
            filelist = [f for f in os.listdir(".")] #Lists all files in the directory
            for f in filelist:
                current_file = os.path.splitext(f) #Saves only the filename without the extention
                if re.search('install', current_file[0], re.IGNORECASE) or re.search('setup', current_file[0], re.IGNORECASE):
                    if current_file[1] == ".exe" or current_file[1] == ".msi" :
                        os.remove(f)
            self.StatusVar.set('Deleted.')

        if Filetype == "olderthan":
            userSelection = self.SelectedOlderThan.get()
            if userSelection == "Select A Time...":
                self.StatusVar.set('Please select a time.')
            else:
                filelist = [f for f in os.listdir(".")]
                today = datetime.datetime.today()
                for f in filelist:
                    created_date = datetime.datetime.fromtimestamp(os.path.getctime(f))
                    time_difference = today - created_date
                    if userSelection == "Today":
                        if time_difference.days >= 1:
                            os.remove(f)
                    elif userSelection == "Yesterday":
                        if time_difference.days >= 2:
                            os.remove(f)
                    elif userSelection == "One Week":
                        if time_difference.days >= 7:
                            os.remove(f)
                    elif userSelection == "One Month":
                        if time_difference.days >= 31: #These are just approximations - Will be *about* accurate
                            os.remove(f)
                    elif userSelection == "One Year":
                        if time_difference.days >= 365:
                            os.remove(f)
                self.StatusVar.set('Deleted.')    

# main
root = Tk()
root.title("simple-file-deleter") #Sets title of window
app = Application(root)
root.mainloop() #Begins application
