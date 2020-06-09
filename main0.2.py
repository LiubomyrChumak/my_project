import PySimpleGUI as sg
import csv
import os
import sys
import pandas
import subprocess


# csv files
EX_file = 'expensedata.csv'
IN_file = 'incomedata.csv'

# theme
sg.theme('Light blue')



# menu toolbar

menu_def = [['File', ['Open', 'Exit']],
            ['Help', 'About...'], ]



main_layout =[   [sg.Menu(menu_def, tearoff=True)],
               [sg.Text('Hello, what you want to do?', size=(50, 1), font=30)],
               [sg.Button('Add expense', border_width=3, pad=((0, 0), (20, 0))),
                sg.Button('Add income', border_width=3, pad=((75, 0), (20, 0)))],
               [sg.Button('Quit', border_width=3, pad=((240, 0), (60, 0)))]
            ]

# windows
main_window = sg.Window("Expense tracker", main_layout, grab_anywhere=False, size=(300, 200))
menu_window = False
win2_active = False
win3_active = False
i = 0

# loop

while True:
    event, values = main_window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    elif event == 'Exit':
        break
    elif event == 'Open' and not menu_window:
        menu_window = True
        event, values = sg.Window('Find files', [[sg.Text('What file you want open?')], [sg.InputText(key='-PATH-'),
                                                                                     sg.FileBrowse()],
                                             [sg.OK(), sg.Cancel()]], size=(450, 150)).read(close=True)
        source = values['-PATH-']
        subprocess.call(["xdg-open", source])

    elif event == 'Add expense' and not win2_active:
        win2_active = True

        layout_2 = [[sg.Text('How much money you spend that time?', justification='center'), sg.Text(size=(15, 1))],
                   [sg.Text("Expense"), sg.Input(key='-EXPENSE-', background_color='white',
                    text_color='black', pad=(16, 0))], [sg.CalendarButton("Data", format='%d.%m.%y'),
                    sg.Input(key='-DATA-', background_color='white', text_color='black', pad=(16, 0))],
                    [sg.Text("Description"), sg.Input(key='-DESCRIPTION-', background_color='white', text_color='black',
                                                      pad=(0, 0))],
                    [sg.Button('Add expense'), sg.Button('Back', pad=(10, 0))]]

        window2 = sg.Window('Add expense', layout_2, size=(450, 150))
        if win2_active:
            event, values = window2.read()
            if event != sg.TIMEOUT_KEY:
                print('win2', event)
            if event == 'Add expense':
                with open(EX_file, 'w', newline='') as f:
                    fieldnames = ['Expense', 'Data', 'Description']
                    thewriter_1 = csv.DictWriter(f, fieldnames=fieldnames, delimiter=' ')
                    thewriter_1.writeheader()
                    thewriter_1.writerow({'Expense': values['-EXPENSE-'],
                                      'Data': values['-DATA-'],
                                      'Description': values['-DESCRIPTION-']})
                sg.popup('Your expense successfully added')
                window2.close()
            if event == 'Back' or event == sg.WIN_CLOSED:
                win2_active = False
                window2.close()

    elif event == 'Add income' and not win3_active:
        win3_active = True

        layout_3 = [[sg.Text('How much money you earned that time?', justification='center'), sg.Text(size=(15, 1))],
                    [sg.Text("Earned"), sg.Input(key='-EARN-', background_color='white',
                    text_color='black', pad=(25, 0))], [sg.CalendarButton("Data", format='%d.%m.%y'),
                    sg.Input(key='-DATA-', background_color='white', text_color='black', pad=(16, 0))],
                    [sg.Text("Description"), sg.Input(key='-DESCRIPTION-', background_color='white', text_color='black',
                    pad=(0, 0))],[sg.Button('Add income'), sg.Button('Back', pad=(10, 0))]]

        window3 = sg.Window('Add income', layout_3, size=(450, 150))
        if win3_active:
            event, values = window3.read()
            if event != sg.TIMEOUT_KEY:
                print('win3', event)
            if event == 'Add income':
                with open(IN_file, 'w', newline='') as fi:
                    fieldnames = ['Earned', 'Data', 'Description']
                    thewriter_2 = csv.DictWriter(fi, fieldnames=fieldnames, delimiter='|')
                    thewriter_2.writeheader()
                    thewriter_2.writerow({'Earned': values['-EARN-'],
                                      'Data': values['-DATA-'],
                                      'Description': values['-DESCRIPTION-']})
                sg.popup('Your earned money successfully added')
                window3.close()
            if event == 'Back' or event == sg.WIN_CLOSED:
                win3_active = False
                window3.close()

main_window.close()



