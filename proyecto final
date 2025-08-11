import flet as ft
from flet import Icons, Colors
from pyairtable import Api
from pyairtable.formulas import match

API_KEY = "pateHwZtSUTdd1qSx.710caf39c1ecf700672c8553e284c52a1aa5268f6faa075569a13b8b26e76d23"
BASE_ID = "appXcHaDBT7H0uNaI"

tabla_usuarios = Api(API_KEY).base(BASE_ID).table("usuario")
tabla_bioenergias = Api(API_KEY).base(BASE_ID).table("bioenergia")


def main(page: ft.Page):
    page.title = "Sistema de Gestión"
    page.theme_mode = "light"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    usuario_input = ft.TextField(label="Usuario", prefix_icon=Icons.PERSON)
    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        prefix_icon=Icons.LOCK
    )
    mensaje_snack = ft.SnackBar(content=ft.Text(""))

    def mostrar_snack(texto, color=Colors.GREEN):
        mensaje_snack.content = ft.Text(texto, color=color)
        mensaje_snack.open = True
        page.snack_bar = mensaje_snack
        page.update()

    def validar_credenciales(e):
        usuario = usuario_input.value
        password = password_input.value
        if not usuario or not password:
            mostrar_snack("Por favor, ingrese usuario y contraseña.", Colors.RED)
            return

        try:
            formula = match({"clave": usuario, "contra": password})
            registro = tabla_usuarios.first(formula=formula)
            if registro:
                page.go("/menu")
            else:
                mostrar_snack("Usuario o contraseña incorrectos.", Colors.RED)
        except Exception as err:
            mostrar_snack("Error de conexión con Airtable.", Colors.RED)
            print(f"Error de Airtable: {err}")

    def view_login():
        return ft.View(
            route="/",
            controls=[
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Iniciar Sesión", size=24, weight="bold"),
                                usuario_input,
                                password_input,
                                ft.ElevatedButton(
                                    "Ingresar",
                                    icon=Icons.LOGIN,
                                    bgcolor=Colors.GREEN,
                                    color=Colors.WHITE,
                                    on_click=validar_credenciales
                                ),
                                ft.TextButton(
                                    "¿No tienes cuenta? Regístrate aquí",
                                    icon=Icons.PERSON_ADD,
                                    on_click=lambda e: page.go("/agregar_usuario")
                                )
                            ],
                            spacing=20
                        ),
                        padding=20
                    ),
                    elevation=6
                )
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def view_menu():
        return ft.View(
            route="/menu",
            controls=[
                ft.AppBar(title=ft.Text("Menú principal"), bgcolor=Colors.GREEN),
                ft.Column(
                    controls=[
                        ft.ElevatedButton("Agregar nuevo usuario", icon=Icons.PERSON_ADD, on_click=lambda e: page.go("/agregar_usuario")),
                        ft.ElevatedButton("Consultar usuarios", icon=Icons.LIST, on_click=lambda e: page.go("/consultar_usuarios")),
                        ft.Divider(),
                        ft.ElevatedButton("Agregar bioenergía", icon=Icons.ADD, on_click=lambda e: page.go("/agregar_bioenergia")),
                        ft.ElevatedButton("Consultar bioenergías", icon=Icons.TABLE_CHART, on_click=lambda e: page.go("/consultar_bioenergias")),
                        ft.Divider(),
                        ft.ElevatedButton("Cerrar sesión", icon=Icons.LOGOUT, bgcolor=Colors.RED, color=Colors.WHITE, on_click=lambda e: page.go("/"))
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )

    def view_agregar_usuario():
        nombre_field = ft.TextField(label="Nombre")
        clave_field = ft.TextField(label="Usuario (clave)")
        contra_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)

        def registrar_usuario_interno(e):
            if not nombre_field.value or not clave_field.value or not contra_field.value:
                mostrar_snack("Todos los campos son obligatorios.", Colors.RED)
                return

            try:
                tabla_usuarios.create({
                    "nombre": nombre_field.value,
                    "clave": clave_field.value,
                    "contra": contra_field.value
                })
                mostrar_snack("Usuario registrado correctamente.", Colors.GREEN)
                page.go("/menu")
            except Exception as err:
                mostrar_snack(f"Error al registrar: {err}", Colors.RED)

        return ft.View(
            route="/agregar_usuario",
            controls=[
                ft.AppBar(title=ft.Text("Agregar nuevo usuario"), bgcolor=Colors.GREEN),
                nombre_field,
                clave_field,
                contra_field,
                ft.ElevatedButton("Registrar", icon=Icons.SAVE, bgcolor=Colors.GREEN, color=Colors.WHITE, on_click=registrar_usuario_interno),
                ft.ElevatedButton("Volver", icon=Icons.ARROW_BACK, on_click=lambda e: page.go("/menu"))
            ]
        )

    def view_agregar_bioenergia():
        cultivo_field = ft.TextField(label="Cultivo")
        parte_field = ft.TextField(label="Parte")
        cantidad_field = ft.TextField(label="Cantidad", keyboard_type=ft.KeyboardType.NUMBER)
        area_field = ft.TextField(label="Área", keyboard_type=ft.KeyboardType.NUMBER)
        energia_field = ft.TextField(label="Energía", keyboard_type=ft.KeyboardType.NUMBER)
        municipio_field = ft.TextField(label="Municipio")
        latitud_field = ft.TextField(label="Latitud", keyboard_type=ft.KeyboardType.NUMBER)
        longitud_field = ft.TextField(label="Longitud", keyboard_type=ft.KeyboardType.NUMBER)

        def registrar_bioenergia_interno(e):
            if not all([cultivo_field.value, parte_field.value, cantidad_field.value, area_field.value,
                        energia_field.value, municipio_field.value, latitud_field.value, longitud_field.value]):
                mostrar_snack("Todos los campos son obligatorios.", Colors.RED)
                return

            try:
                tabla_bioenergias.create({
                    "cultivo": cultivo_field.value,
                    "parte": parte_field.value,
                    "cantidad": float(cantidad_field.value.replace(",", ".")),
                    "area": float(area_field.value.replace(",", ".")),
                    "energia": float(energia_field.value.replace(",", ".")),
                    "municipio": municipio_field.value,
                    "latitud": float(latitud_field.value.replace(",", ".")),
                    "longitud": float(longitud_field.value.replace(",", "."))
                })
                mostrar_snack("Bioenergía registrada correctamente.", Colors.GREEN)
                page.go("/menu")
            except Exception as err:
                mostrar_snack(f"Error al registrar bioenergía: {err}", Colors.RED)

        return ft.View(
            route="/agregar_bioenergia",
            controls=[
                ft.AppBar(title=ft.Text("Agregar nueva bioenergía"), bgcolor=Colors.GREEN),
                cultivo_field,
                parte_field,
                cantidad_field,
                area_field,
                energia_field,
                municipio_field,
                latitud_field,
                longitud_field,
                ft.ElevatedButton("Registrar", icon=Icons.SAVE, bgcolor=Colors.GREEN, color=Colors.WHITE, on_click=registrar_bioenergia_interno),
                ft.ElevatedButton("Volver", icon=Icons.ARROW_BACK, on_click=lambda e: page.go("/menu"))
            ]
        )


    def view_consultar_usuarios():
        try:
            registros = tabla_usuarios.all()
            filas = [
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(r["fields"].get("nombre", ""))),
                    ft.DataCell(ft.Text(r["fields"].get("clave", ""))),
                    ft.DataCell(ft.Text(r["fields"].get("contra", "")))
                ]) for r in registros
            ]
            return ft.View(
                route="/consultar_usuarios",
                controls=[
                    ft.AppBar(title=ft.Text("Usuarios registrados"), bgcolor=Colors.GREEN),
                    ft.Column(
                        controls=[
                            ft.DataTable(
                                columns=[
                                    ft.DataColumn(ft.Text("Nombre")),
                                    ft.DataColumn(ft.Text("Usuario")),
                                    ft.DataColumn(ft.Text("Contraseña"))
                                ],
                                rows=filas
                            ),
                            ft.ElevatedButton(
                                "Volver",
                                icon=Icons.ARROW_BACK,
                                on_click=lambda e: page.go("/menu")
                            )
                        ],
                        scroll="auto",  
                        expand=True
                    )
                ]
            )
        except Exception as err:
            mostrar_snack("Error al obtener datos de Airtable.", Colors.RED)
            return view_menu()



    def view_consultar_bioenergias():
        try:
            registros = tabla_bioenergias.all()
            filas = []
            for r in registros:
                data = r.get("fields", {})
                filas.append(
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text(str(data.get("cultivo", "")))),
                        ft.DataCell(ft.Text(str(data.get("parte", "")))),
                        ft.DataCell(ft.Text(str(data.get("cantidad", "")))),
                        ft.DataCell(ft.Text(str(data.get("area", "")))),
                        ft.DataCell(ft.Text(str(data.get("energia", "")))),
                        ft.DataCell(ft.Text(str(data.get("municipio", "")))),
                        ft.DataCell(ft.Text(str(data.get("latitud", "")))),
                        ft.DataCell(ft.Text(str(data.get("longitud", ""))))
                    ])
                )
            return ft.View(
                route="/consultar_bioenergias",
                controls=[
                    ft.AppBar(title=ft.Text("Bioenergías registradas"), bgcolor=Colors.GREEN),
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Cultivo")),
                            ft.DataColumn(ft.Text("Parte")),
                            ft.DataColumn(ft.Text("Cantidad")),
                            ft.DataColumn(ft.Text("Área")),
                            ft.DataColumn(ft.Text("Energía")),
                            ft.DataColumn(ft.Text("Municipio")),
                            ft.DataColumn(ft.Text("Latitud")),
                            ft.DataColumn(ft.Text("Longitud"))
                        ],
                        rows=filas
                    ),
                    ft.ElevatedButton("Volver", icon=Icons.ARROW_BACK, on_click=lambda e: page.go("/menu"))
                ]
            )
        except Exception as err:
            mostrar_snack("Error al obtener datos de Airtable.", Colors.RED)
            return view_menu()


    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(view_login())
        elif page.route == "/menu":
            page.views.append(view_menu())
        elif page.route == "/agregar_usuario":
            page.views.append(view_agregar_usuario())
        elif page.route == "/consultar_usuarios":
            page.views.append(view_consultar_usuarios())
        elif page.route == "/agregar_bioenergia":
            page.views.append(view_agregar_bioenergia())
        elif page.route == "/consultar_bioenergias":
            page.views.append(view_consultar_bioenergias())
        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main)
