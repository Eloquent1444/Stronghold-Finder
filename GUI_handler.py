import PySimpleGUI as sg
import finder

sg.theme("DarkGrey15")

layout = [
    [sg.Text("First x :", size=(12, 1)), sg.In("", key="-X1-", size=(8, 1)), sg.Text("First z :", size=(12, 1)), sg.In("", key="-Z1-", size=(8, 1)), sg.Text("First angle :", size=(12, 1)), sg.In("", key="-A1-", size=(5, 1))],
    [sg.Text("Second x :", size=(12, 1)), sg.In("", key="-X2-", size=(8, 1)), sg.Text("Second z :", size=(12, 1)), sg.In("", key="-Z2-", size=(8, 1)), sg.Text("Second angle :", size=(12, 1)), sg.In("", key="-A2-", size=(5, 1))],
    [sg.Button("Search!", key="-START-"), sg.Push(), sg.Checkbox("1.19", default=True, key="-VERSION-"), sg.Text("Range : ", size=(6, 1)), sg.In("3000", key="-RANGE-", size=(5, 1))],
    [sg.Text("_"*67)],
    [sg.Output(size=(64, 10), key="-OUTPUT-")]
    ]

# Create the window
window = sg.Window("Stronghold finder", layout)
# Create an event loop
while True:

    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    elif event == "-START-":
        try:
            #Translating minecraft z to a y on a 2d plane
            x1 = float(values["-X1-"])
            y1 = float(values["-Z1-"])
            ang1 = float(values["-A1-"])

            x2 = values["-X2-"]
            y2 = values["-Z2-"]
            ang2 = values["-A2-"]
            #x1, y2, ang2 could be empty because of one eye finding
            if not x1 or not x2 or not ang2:
                x2 = y2 = ang2 = None
            else:
                x2 = float(x2)
                y2 = float(y2)
                ang2 = float(ang2)

            rang = float(values["-RANGE-"])
            version = values["-VERSION-"]

            find = finder.Finder((x1, y1), ang1, (x2, y2), ang2, rang, version)
            find.find()

            print("\n")

        except ValueError as ve:
            pass

window.close()