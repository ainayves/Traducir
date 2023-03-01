import flet as ft

def page_elements():
    origin_lang = ft.TextField(
        label="Entrez votre texte",
        multiline=True,)

    target_lang = ft.TextField(multiline=True)
    select_lang = ft.Dropdown(
        label="Choisir une langue",
        label_style=ft.TextStyle(size=10),
        width=100,
        options=[
            ft.dropdown.Option("French"),
            ft.dropdown.Option("Malagasy"),
            ft.dropdown.Option("English"),
            ft.dropdown.Option("Spanish"),
            ft.dropdown.Option("Japanese"),
        ]
    )

    return origin_lang , target_lang , select_lang