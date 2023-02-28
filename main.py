import flet as ft
from plugin import davinci_translate


def main(page: ft.Page):

    origin_lang = ft.TextField(label="Français")
    eng_lang = ft.TextField(label="Anglais")
    spanish_lang = ft.TextField(label="Spanish")
    japanese_lang = ft.TextField(label="Japanese")

    def translate(e):

        result=davinci_translate(origin_lang.value)
        res=result.choices[0].text.split("\n")
        origin_lang.value = ""
        eng_lang.value = res[0]
        spanish_lang.value = res[1].replace("2."," ")
        japanese_lang.value = res[2].replace("3."," ")
        page.update()
        origin_lang.focus()

    page.add(ft.Column([
        ft.Row([origin_lang,
        eng_lang,spanish_lang,japanese_lang]), ft.ElevatedButton("Translate", on_click=translate)])
    )

ft.app(target=main)