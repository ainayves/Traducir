import flet as ft

def page_props(page :ft.Page):

    page.title = "TRADUCIR"
    page.window_width = 200        
    page.window_height = 200       
    page.window_resizable = False
    
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("Traducir"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED)
        
        ],
    )
    return page

