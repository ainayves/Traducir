import flet as ft

def row_with_alignment(element : ft.TextField):
        return ft.Container(
                    content=element,
                    alignment=ft.alignment.center,
                    expand=2,
                    width=550,
                    height=500,
                    border_radius=ft.border_radius.all(5),
                )

          
