import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

character = str(input("What character is being assessed?\n"))
setType = str(input("What artifact set is being used?\n"))
print("")

cvList = []
artifacts = ["flower" ,"feather" ,"sands" ,"goblet" ,"circlet"]
artifactsCap = ["Flower" ,"Feather" ,"Sands" ,"Goblet" ,"Circlet"]

def valueEntry():

    print("What is the crit rate on this" + " " + artifacts[i] + "?")
    print("What is the crit damage on this" + " " + artifacts[i] + "?")
    print("")
    
    root = tk.Tk()
    root.geometry("300x150")
    root.resizable(False, False)
    root.title(artifactsCap[i])

    cr = tk.StringVar()
    cd = tk.StringVar()


    enter = ttk.Frame(root)
    enter.pack(padx=10, pady=10, fill='x', expand=True)


    cr_label = ttk.Label(enter, text="Crit Rate:")
    cr_label.pack(fill='x', expand=True)

    cr_entry = ttk.Entry(enter, textvariable=cr)
    cr_entry.pack(fill='x', expand=True)
    cr_entry.focus()


    cd_label = ttk.Label(enter, text="Crit Damage:")
    cd_label.pack(fill='x', expand=True)

    cd_entry = ttk.Entry(enter, textvariable=cd)
    cd_entry.pack(fill='x', expand=True)

           
    login_button = ttk.Button(enter, text="Enter", command=root.destroy)
    login_button.pack(fill='x', expand=True, pady=10)

    root.mainloop()

    cRate = float(cr.get())
    cDmg = float(cd.get())
    cvTemp = []
    cvTemp.append(cRate)
    cvTemp.append(cDmg)
    return cvTemp

def valueRater(value):
    if value == 0:
        print("Useless.")
    elif 0 < value <= 10:
        print("Rated 1 star. Poor.")
    elif 10 < value <= 20:
        print("Rated 2 star. Substandard.")
    elif 20 < value <= 30:
        print("Rated 3 star. Mediocre.")
    elif 30 < value <= 40:
        print("Rated 4 star. Good.")
    elif 40 < value <= 50:
        print("Rated 5 star. Invaluable.")
        
def cvCheck():
    cStats = valueEntry()
    cRate = float(cStats[0])
    cDmg = float(cStats[1])
    totalCV = (cRate * 2) + cDmg
    
    if i == 4:
        totalCV = totalCV * 2
    
    totalCV = str(totalCV)
    print("The total critical value for this", setType, artifacts[i],"is", totalCV + ".")
    totalCV = float(totalCV)
    valueRater(totalCV)
    cvList.append(totalCV)
    print("")

for i in range(0,5):
    cvCheck()

totalChar = sum(cvList)
totalChar = str(round(totalChar,2))

print("Total CV for", character + "'s", setType, "set is", totalChar + ".")

avgCV = float(totalChar) / 5
avgCV = round(avgCV, 2)
avgCV = str(avgCV)
print("Average CV per artifact is", avgCV + ".")

avgCV = float(avgCV)
valueRater(avgCV)

x_ =input("Press enter to exit.")
