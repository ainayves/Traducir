from flet import *
from base import Translating
from lib.widgets.main_rows import row_with_alignment
from lib.layout.page_elements import page_elements


def main(page: Page):

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
            View(
                    "/",
                    [   Row([
                                
                                Container(expand=2, content=Text(value="Connecté en tant que : Aina")),
                                Container(expand=3),
                                Container(expand=1,
                                content=IconButton(icons.WB_SUNNY_OUTLINED , on_click= lambda _: page.go("/store")))
  
                                ]),

                        Container(
                            content=Column([
                            Row([
                                    row_with_alignment(origin_lang),
                                    row_with_alignment(target_lang),
                                    Container(
                                        content=select_lang
                                        )
                                    ],
                                    alignment=alignment.center),
                    
                    
                            Row([
                                    Container(expand=3),
                                    Container(expand=3,
                                    content=ElevatedButton("Translate", on_click=translate)),
                                    Container(expand=3)
                                    ])
                        
                            ]),
                        )
                    ],
                )
        )
        if page.route == "/store":
                page.views.append( 
                    View(
                        "/store",
                        [
                            AppBar(title=Text("Store"), bgcolor=colors.SURFACE_VARIANT),
                            ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
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


app(target=main)