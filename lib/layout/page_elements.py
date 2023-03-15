from flet import *

def page_elements():
    origin_lang = TextField(
        label="Entrez le texte à traduire",
        multiline=True,)

    target_lang = TextField(multiline=True)
    select_lang = Dropdown(
        label="Choisir une langue",
        label_style=TextStyle(size=10),
        width=100,
        options=[
            dropdown.Option("French"),
            dropdown.Option("Malagasy"),
            dropdown.Option("English"),
            dropdown.Option("Spanish"),
            dropdown.Option("Japanese"),
            dropdown.Option("Deutch"),
            dropdown.Option("Chinese"),
        ]
    )

    return origin_lang , target_lang , select_lang