import flet as ft


def main(page:ft.Page):

    def mostrar_registro(e:ft.ControlEvent):
        page.clean()
        registro.main(page) 

    page.title= "menu principal"
    page.theme_mode= "light"
    page.appbar=ft.AppBar(
        title=ft.Text ("SISTEMA DE GESTION DE ENERGIAS"),
        leading=ft.Icon("energy_sevings_leaf"),
        color="white",
        bgcolor="purple"
    )

    btn_registro=ft.ElevatedButton("Registro",on_click=mostrar_registro)
    btn_consulta=ft.ElevatedButton("consulta")

    page.add(btn_registro,btn_consulta)
    page.update()

ft.app(target=main)
if __name__ == "__main__":
    ft.app(target=main)