import flet as ft 
def main(page: ft.page):
    page.title="App003"
    page.bgcolor="purple"
    page.horizontal_aligment=ft.MainAxisAlignment.CENTER
    page.vertical_aligment=ft.MainAxisAlignment.CENTER

    lbl1=ft.Text("Sumar",
                 style=ft.TextStyle(size=40,weight="bold"))
    lbl2=ft.Text("Limpiar",
                 style=ft.TextStyle(size=40,weight="bold"))
    Img1=ft.Image(src="cerdo.jpg",width=300,height=300)

def calcular_suma(txt_field,page):
    txt_num1=txt_field.value.Text(f"Introduce el primer numero: ")


    suma=ft.ElevatedButton("Sumar",
                               color="black",
                               width=100,
                               height=50)
    def calcular_suma(txt_num1,txt_num2,txt_respuesta):
        try:
            num1=float(txt_num1.value.strip())
            num2=float(txt_num2.value.strip())
            resultado=num1 + num2 
            txt_respuesta.value=f"Resultado:{resultado}"
        except ValueError:
            txt_respuesta.value="Error:Ingresa Valores Correctos"
    
    limpiar=ft.ElevatedButton("Limpiar",
                                 color="red",
                                 width=100,
                                 height=50)
    def limpiar (txt_num1,txt_num2,txt_respuesta):
        txt_num1.value=""
        txt_num2.value=""
        txt_respuesta.value=f"Resultado: "
        page.update()
    
    
    
ft.app(main)