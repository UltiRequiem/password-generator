import secrets
import string

import PySimpleGUI as sg

import pyperclip


def make_password(length: int):
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


sg.theme("DarkAmber")

layout = [
    [
        sg.Text(
            "Password Generator",
            size=(50, 1),
            font=("Arial", 20),
            justification="center",
        )
    ],
    [sg.Text("Enter the password length:")],
    [
        sg.Text("       "),
        sg.Slider(
            key="length",
            orientation="horizontal",
            range=(1, 100),
            default_value=10,
            enable_events=True,
        ),
    ],
    [
        sg.Text("       ", size=(1, 1)),
    ],
    [sg.Button("Copy", key="copy")],
    [sg.Text("", key="password", size=(200))],
    [sg.Text("Made by UltiRequiem", justification="center", size=(50))],
]

window = sg.Window("Password Generator", layout, size=(800, 250))

password = make_password(10)

while True:
    window_data = window.read()

    if not window_data:
        break

    event, values = window_data

    if event == sg.WIN_CLOSED:
        break

    if event == "length":

        length = int(values["length"])

        password = make_password(length)

        window["password"].update(password)

    if event == "copy":
        pyperclip.copy(password)

window.close()
