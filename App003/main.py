import flet as ft

def main(page: ft.Page):
    page.title="App003"  
    page.bgcolor="purple"
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    lbl1=ft.Text("Sumar",
                style=ft.TextStyle(size=40,weight="bold"))
    lbl2=ft.Text("ingresa el primer numero ",
                style=ft.TextStyle(size=40,weight="bold"))
    
    Img1=ft.Image(src="cerdo.jpg",width=300,height=300)
    
    
    btnSi=ft.ElevatedButton("Sumar",
                            color="green",
                            width=100,
                            height=50)
    btnNo=ft.ElevatedButton("limpiar",
                            color="red",
                            width=100,
                            height=50)
    def no(e):
        page.update()
    def si(e):
        Img1.src="cerdo.jpg"
        page.update()
        
    btnSi.on_click=si
    btnNo.on_click=no
    page.update()
    
    page.add(
        ft.Column(
            [
                lbl1,
                Img1,
                lbl2,
                ft.Row([btnSi,btnNo],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
            ],
            
        )
    )

ft.app(main)
