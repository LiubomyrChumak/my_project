import PySimpleGUI as sg
import csv

sg.theme('Light blue')

# layouts

main_layout = [[sg.Text('Hello, what you would to do?',),
                sg.Text(size=(15,1), key='-OUTPUT-', )],
               [sg.Button('Add expense'), sg.Button('Add income'), sg.Button('Quit')]]

# windows

main_window = sg.Window("Expense tracker", main_layout, grab_anywhere=True, size=(400, 300), text_justification='center')
win2_active = False
win3_active = False
i = 0
# loop

while True:
    event, values = main_window.read(timeout=100)
    if event != sg.TIMEOUT_KEY:
        print(i, event, values)
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    elif event == 'Add expense'and not win2_active:
        win2_active = True
        layout_2 = [
            [sg.Text('How much money you spend that time?', justification='center'),
             sg.Text(size=(15, 1), key='-OUTPUT-')],
            [sg.Text("Expense", relief=sg.RELIEF_RAISED), sg.Input(key='-EXPENSE-', background_color='white',
            text_color='black')],
            [sg.CalendarButton("Data"), sg.Input(key='-DATA-', background_color='white', text_color='black')],
            [sg.Text("Description"), sg.Input(key='-DESCRIPTION-', background_color='white', text_color='black')],
            [sg.Button('Add expense'), sg.Button('Back')]
        ]
        window2 = sg.Window('Add expense', layout_2)
    if win2_active:
        event, values = window2.read(timeout=100)
        if event != sg.TIMEOUT_KEY:
            print("win2 ", event)
        if event == 'Add expense':
            fields = ['Expense', 'Data', 'Description']
            with open(r'name', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
            sg.popup('Your expense successfully added')
            window2.close()
        if event == 'Back' or event == sg.WIN_CLOSED:
            win2_active = False
            window2.close()
    elif event == 'Add income'and not win3_active:
        win3_active = True
        layout_3 = [
            [sg.Text('How much money you earned that time?', justification='center'),
             sg.Text(size=(15, 1), key='-OUTPUT-')],
            [sg.Text("Earned", relief=sg.RELIEF_RAISED), sg.Input(key='-EARN-', background_color='white',
            text_color='black')],
            [sg.CalendarButton("Data"), sg.Input(key='-DATA-', background_color='white', text_color='black')],
            [sg.Text("Description"), sg.Input(key='-DESCRIPTION-', background_color='white', text_color='black')],
            [sg.Button('Add income'), sg.Button('Back')]
        ]
        window3 = sg.Window('Add expense', layout_3)
    if win3_active:
        event, values = window3.read(timeout=100)
        if event != sg.TIMEOUT_KEY:
            print("win3 ", event)
        if event == 'Add income':
            sg.popup('Your earned money successfully added')
            window3.close()
        if event == 'Back' or event == sg.WIN_CLOSED:
            win3_active = False
            window3.close()





main_window.close()