import flet as ft
from base import Translating
from lib.widgets.main_rows import row_with_alignment
from lib.layout.page_elements import page_elements


def main(page: ft.Page):

    """ Initialize the page and elements """
    
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

    def route_change(route):

        page.views.clear()
        page.views.append(
            ft.View(
                    "/",
                    [   ft.Row([
                                
                                ft.Container(expand=2, content=ft.Text(value="Connecté en tant que : Aina")),
                                ft.Container(expand=3),
                                ft.Container(expand=1,
                                content=ft.IconButton(ft.icons.WB_SUNNY_OUTLINED , on_click= lambda _: page.go("/store")))
  
                                ]),

                        ft.Container(
                            content=ft.Column([
                            ft.Row([
                                    row_with_alignment(origin_lang),
                                    row_with_alignment(target_lang),
                                    ft.Container(
                                        content=select_lang
                                        )
                                    ],
                                    alignment=ft.alignment.center),
                    
                    
                            ft.Row([
                                    ft.Container(expand=3),
                                    ft.Container(expand=3,
                                    content=ft.ElevatedButton("Translate", on_click=translate)),
                                    ft.Container(expand=3)
                                    ])
                        
                            ]),
                        )
                    ],
                )
        )
        if page.route == "/store":
                page.views.append( 
                    ft.View(
                        "/store",
                        [
                            ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ],
                    )
                )    
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)