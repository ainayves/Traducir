import flet as ft
from base import Translating
from lib.widgets.main_rows import (
    row_with_alignment)


def main(page: ft.Page):
    page.title = "TRADUCIR"
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

    
    def translate(e):

        # translation object

        traduction_obj = Translating(origin_lang.value, select_lang.value)
        traduction_result =traduction_obj.traducir()
        res = traduction_result.choices[0].text

        # update screen information

        origin_lang.value = ""
        target_lang.value = res
        page.update()
        origin_lang.focus()


    page.add(ft.Column([
        ft.Row([row_with_alignment(origin_lang),
                row_with_alignment(target_lang),
                ft.Container(
                    content=select_lang
                    )
                ],
        alignment=ft.alignment.center

        ), ft.ElevatedButton("Translate", on_click=translate)])
    )


ft.app(target=main)