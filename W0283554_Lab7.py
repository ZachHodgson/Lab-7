from guizero import App, Text, Picture, yesno, Box, PushButton
#Step 3:
#app = App(title="Hello World", bg="red", height=200, layout="grid", width=800)

#Step 4:
# def closegui():
#     if yesno("Close", "Do you want to quit?"):
#         app.destroy()
# 
# if __name__=='__main__':
#     app = App("Wanted!")
#     app.bg = "#A0A0A0" #Light gray
#     wanted_text = Text(app, "DROID")
#     wanted_text.text_size = 50
#     wanted_text.font = "Times New Toman"
#     cat = Picture(app, image="Droid.gif")
#     app.when_closed = closegui
#     app.display()

#Step 5:

# def do_nothing():
#     return 0
# 
# app = App(title="My app", height=300, width=300, layout="grid")
# text = Text(app, text="Some text here", grid=[1,0])
# box = Box(app, layout="grid", grid=[1,0])
# 
# button1 = PushButton(box, command=do_nothing, text="1", grid=[0,0])
# button2 = PushButton(box, command=do_nothing, text="2", grid=[1,0])
# button3 = PushButton(box, command=do_nothing, text="3", grid=[2,0])
# button4 = PushButton(box, command=do_nothing, text="4", grid=[0,1])
# button5 = PushButton(box, command=do_nothing, text="5", grid=[1,1])
# button6 = PushButton(box, command=do_nothing, text="6", grid=[2,1])
# app.display

#Step 6.a:
# from gpiozero import LED
# 
# led17 = LED(17)
# 
# def GPIO_17():
#     if button1.text == "GPIO17_ON":
#         button1.text = "GPIO17_OFF"
#         led17.on()
#     else:
#         button1.text="GPIO17_ON"
#         led17.off()
#         
# if __name__== '__main__':
#     app = App("Activation GPIO")
#     
#     button1 = PushButton(app, command=GPIO_17, text="GPIO17_ON")
#     app.display()
#     led17.off()

#Step 6.b
from guizero import App, Text
from gpiozero import Button #import module button
from gpiozero import LED #import module LED

button = Button(2)
led = LED(17)

def scanInput():
    if button.is_pressed:
        text.value = 1 #"GPIO2 ON"
        led.on()
    else:
        text.value = 0 #"GPIO2 OFF"
        led.off()
        
def exitGUI():
    text.destroy()
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
        print("Adios")
        
if __name__ == '__main__':
    app = App("Reading GPIO")
    text = Text(app, text = "1")
    text.repeat(10, scanInput) #schedule call to scan GPIO input every
    app.when_closed = exitGUI
    app.display()