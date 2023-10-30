import PySimpleGUI as sg

sg.theme('BluePurple')
layout = [
    [(sg.Combo(('EUR', 'BGN'), key = '-CURRENCY-IN-', default_value='EUR'), sg.InputText(key='-IN-'), sg.Input,
    sg.Button('convert'))]
]

window = sg.Window('Money Converter', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()

