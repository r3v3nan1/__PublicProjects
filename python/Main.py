
#starting with import time - not used
import time    
#not used variable
Running = True
#confirms
print("Operating system")
print("running")
#creates a variable for later use
click = 0
UpgradeStart = 100
NumberOfClick = 1

#to check if there is data
import os

#the file path for the saved data PS. need muliple file paths for more of the data
#this storage system is better for one number..
file_path = "C:\PythoOS\MainResources\SavedData.txt"

#checks for saved data and make sure if the file exist and stop and throw error codes
if os.path.exists(file_path):
    with open("SavedData.txt", "r") as f:
        # Read the number from the file and convert it back to an integer
        number = int(f.read())
        #now python reads the data and computes it back into data
        click = number
        print(click)#put: whatever how many clicks you have of the game
else:
    #stops any error popping up
    print("File does not exist.")

#Saved data for upgrade
file_path2 = "C:\PythoOS\MainResources\SavedUpgradeClickPerSec.txt"

#checks for saved data and make sure if the file exist and stop and throw error codes
if os.path.exists(file_path2):
    with open("SavedUpgradeClickPerSec.txt", "r") as f:
        # Read the number from the file and convert it back to an integer
        number1 = int(f.read())
        #now python reads the data and computes it back into data
        UpgradeStart = number1
        print(UpgradeStart)
else:
    #stops any error popping up
    print("File does not exist.")

#checks for saved data and make sure if the file exist and stop and throw error codes
file_path3 = "C:\PythoOS\MainResources\SavedUpgrade.txt"
if os.path.exists(file_path3):
    with open("SavedUpgrade.txt", "r") as f:
        # Read the number from the file and convert it back to an integer
        number2 = int(f.read())
        #now python reads the data and computes it back into data
        NumberOfClick = number2
        print(NumberOfClick)
else:
    #stops any error popping up
    print("File does not exist.")


#opens the main OPERATION WINDOW

#imports for window


import tkinter as tk
from PIL import ImageTk, Image

# Create the main window
window = tk.Tk()
window.title("PythoOS")

window.resizable(False, False)
window.configure(bg="gray")  # Set background color to black
# Remove title bar
window.overrideredirect(True)

#height and width

OSheight = 750
OSwidth = 1200


ScreenHeight = window.winfo_screenheight()
ScreenWidth =  window.winfo_screenwidth()

x = (ScreenWidth/2) - (OSwidth/2)
y = (ScreenHeight/2) - (OSheight/2)

window.geometry(f'{OSwidth}x{OSheight}+{int(x)}+{int(y)}')

def closewindow():
    window.destory()

# Create a label widget
label1 = tk.Label(window, text="-PythoOS system-", font=("Arial", 20))
label2 = tk.Label(window, text="-PythoOS Version 0.01-", font=("Arial", 10))
"""
pythonFilePath1 = "/workspaces/__PublicProjects/python/Secondary.py"
"""
"""
Needs ursina
pythonFilePath2 = "C:\PythoOS\MainResources\minecraft.py"
"""

#Add to a button on the os to run another python file
"""
def Runfile():
    global pythonFilePath1
    if os.path.exists(pythonFilePath1):
        print("File does exist")
        exec(open('Secondary.py').read())
        closewindow()
    else:
        print("Error: file doesnt exist")
"""
"""
RunButton = tk.Button(window, text="Run - snake" , command= Runfile)
RunButton.place(x=1100,y=10)
"""
def Runfile2():
    global OSheight
    global OSwidth
    
    global pythonFilePath2
    """
    Code needs ursina
    import minecraft.py    
    if os.path.exists(pythonFilePath2):
        print("File does exist")
        exec(open('minecraft.py').read())
    else:
        print("Error: file doesnt exist")
    """
    reset_screen()

RunButton = tk.Button(window, text="Run - minecraft" , command= Runfile2)
RunButton.place(x=1100,y=50)

def reset_screen():
        global x
        global y
        
        #height and width
        window.geometry(f'{OSwidth}x{OSheight}+{int(x)}+{int(y)}')

def DeleteClickerSaveFile():
    global click
    global UpgradeStart
    global NumberOfClick
    file_path = "C:\PythoOS\MainResources\SavedData.txt"
    file_path2 = "C:\PythoOS\MainResources\SavedUpgradeClickPerSec.txt"
    file_path3 = "C:\PythoOS\MainResources\SavedUpgrade.txt"
    # Check if the file exists before deleting
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
        click = 0
    else:
        print(f"File '{file_path}' not found.")


#commands for buttons - window SETTINGS
def button_setting():
    root = tk.Tk()
    root.title("PythoOS")
    root.geometry("700x650")  # Width x Height
    root.resizable(False, False)

    #label have setting - WIP
    label3 = tk.Label(root, text=" -Settings-", font=("Arial", 30))
    label3.place(x=0,y=0)
    label4 = tk.Label(root, text=" no settings (WIP)", font=("Arial", 20))
    label4.place(x=0,y=60)

        # Check if the file exists before deleting
    if os.path.exists(file_path2):
            os.remove(file_path2)
            print(f"File '{file_path2}' deleted successfully.")
            UpgradeStart = 100
    else:
            print(f"File '{file_path2}' not found.")

        # Check if the file exists before deleting
    if os.path.exists(file_path3):
            os.remove(file_path3)
            print(f"File '{file_path3}' deleted successfully.")
            NumberOfClick = 1
    else:
            print(f"File '{file_path3}' not found.")

    buttonD = tk.Button(root, text="delete save files", command= DeleteClickerSaveFile)
    buttonD.place(x=0,y=120)


#button to change things
#another command - window INFO
def button_info():
    root1 = tk.Tk()
    root1.title("PythoOS")
    root1.geometry("700x500")  # Width x Height
    root1.resizable(False, False)
    root1.configure(bg="gray")  # Set background color to black
    #label have info - Version, version type, 
    label2 = tk.Label(root1, text=" - Version 0.01", font=("Arial", 30))
    label2.place(x=0,y=0)
    label6 = tk.Label(root1, text=f'Screen Width:{ScreenWidth} & Screen Height:{ScreenHeight}', font=("Arial", 10))
    label6.place(x=0,y=60)

#The clicker game
def button_ClickerGame():
    global UpgradeStart
    #command for button for game
    def Click_Change():
        global click
        click = click + NumberOfClick
        label5.config(text="Time clicked : " + str(click))
    def upgradeClickPerSec():
        global UpgradeStart
        global NumberOfClick
        global click
        if (UpgradeStart == click or UpgradeStart <= click):
            click = click - UpgradeStart
            UpgradeStart = UpgradeStart*2
            NumberOfClick = NumberOfClick*2
            print("upgraded click")
            label5.config(text="Time clicked : " +str(click))
            button5.config(text="Upgrade click " + str(UpgradeStart), command= upgradeClickPerSec)
    #opens window for game to run
    root2 = tk.Tk()
    root2.title("PythoOS")
    root2.geometry("700x650")  # Width x Height
    root2.resizable(False, False)
    root2.configure(bg="Gray")  # Set background color to black
    label5 = tk.Label(root2, text="Time clicked : " + str(click), font=("Arial", 30))
    label5.pack()
    
    button4 = tk.Button(root2, text="click me", command=Click_Change, font=("Arial", 20))
    button4.place(relx=0.5, rely=0.5, anchor="center")
    button5 = tk.Button(root2, text="Upgrade click " + str(UpgradeStart), command= upgradeClickPerSec)
    button5.place(x=550,y=10)

# Creating a button widget
button1 = tk.Button(window, text="Menu", command=button_setting, font=("Arial", 20))
button1.place(x=0, y=0)

button2 = tk.Button(window, text="info", command=button_info, font=("Arial", 20))
button2.place(x=0, y=60)

button3 = tk.Button(window, text="Clicker game", command=button_ClickerGame, font=("Arial", 20))
button3.place(x=0, y=120)

Button = tk.Button(window, text="Quit", command=window.destroy).pack() #button to close the window

Button4 = tk.Button(window, text="reset screen", command=reset_screen()).place(x=200, y=200) #button to close the window

# Place the label on the window
label1.pack()
label2.place(x=1050,y=715)

# Open the image
image = Image.open("C:\PythoOS\Photos\PythoOS.jpg")

# Resize the image
new_size = (400, 250)  # Width, Height
image2 = image.resize(new_size)

# Save the resized image
image2.save("image2.jpg")

image = Image.open("C:\PythoOS\MainResources\image2.jpg")
photo = ImageTk.PhotoImage(image)

label2 = tk.Label(window, image=photo)
label2.place(relx=0.5, rely=0.5, anchor="center")

# Start the GUI event loop
window.mainloop()

number = click
if (click != 0):
    # Open a file for writing
    with open("SavedData.txt", "w") as f:
      # Write the number to the file
      f.write(str(number))
    if os.path.exists(file_path):
        print("File exists!")
    else:
        print("File does not exist.")

if (UpgradeStart != 100): 
    
    # Open a file for writing
    with open("SavedUpgradeClickPerSec.txt", "w") as f:
      # Write the number to the file
      f.write(str(UpgradeStart))
    if os.path.exists(file_path2):
        print("File exists!")
    else:
        print("File does not exist.")

        
# Open a file for writing
    with open("SavedUpgrade.txt", "w") as f:
      # Write the number to the file
      f.write(str(NumberOfClick))
      if os.path.exists(file_path3):
            print("File exists!")
      else:
            print("File does not exist.")









