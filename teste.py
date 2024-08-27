import flet

def main(page: flet.Page):
    page.title = "CleanMax Lavanderia"
    page.update()

    page.add(
        flet.ResponsiveRow(
            flet.Container(
                flet.Text("Testando tamanho da tela"),
                bgcolor="yellow",
                col={"sm": 6, "md": 4, "xl":2}
            )
        )
    )

flet.app(target=main)
