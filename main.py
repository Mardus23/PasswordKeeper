import PySimpleGUI as sg

layout = [[sg.T('Choose a password',size=(42,1), justification= 'center')],
          [sg.Button(button_text="Facebook", size=(20,5),key= '_FB_'), sg.Button(button_text="Twitter", size=(20,5), key='_Tw_')],
          [sg.Button(button_text="Instagram", size=(20,5), key= '_Ins_'), sg.Button(button_text="Gmail", size=(20,5), key= '_Gm_')],
          [sg.Button(button_text="Reddit", size=(20,5), key= '_Rdt_'), sg.Button(button_text="LinkdIn", size=(20,5), key= '_Link_')]]

event, values = sg.Window('My first app', font=("Helvetica", 12)).Layout(layout).Read()
