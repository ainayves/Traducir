from flet import *

def row_with_alignment(element : TextField):
        return Container(
                    content=element,
                    alignment=alignment.center,
                    expand=2,
                    width=550,
                    height=500,
                    border_radius=border_radius.all(5),
                )

          
