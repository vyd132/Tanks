import model,view,controller,time

while True:
    time.sleep(1/60)
    model.model()
    controller.event()
    view.view()