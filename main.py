import model,view,controller,time

while True:
    time.sleep(1/60)
    model.model(model.t1)
    model.model(model.t2)

    controller.event()
    view.view()