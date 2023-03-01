import flet as ft
from base import Translating
from lib.widgets.main_rows import row_with_alignment
from lib.layout.page_props import page_props 
from lib.layout.page_elements import page_elements

def main(page: ft.Page):

    """ Initialize the page and elements """
    page = page_props(page)
    origin_lang , target_lang , select_lang =  page_elements()

    """ Handle events """
    def translate(e):

        """  Create Translation object """

        traduction_obj = Translating(origin_lang.value, select_lang.value)
        traduction_result =traduction_obj.traducir()
        res = traduction_result.choices[0].text

        """ Update screen informations """

        origin_lang.value = ""
        target_lang.value = res
        page.update()
        origin_lang.focus()


    page.add(ft.Container(
        
 
            content=ft.Column([
                    ft.Row([
                            row_with_alignment(origin_lang),
                            row_with_alignment(target_lang),
                            ft.Container(
                                content=select_lang
                                )
                            ],
                            alignment=ft.alignment.center),

                    ft.ElevatedButton("Translate", on_click=translate)]),
            )
    )


ft.app(target=main)