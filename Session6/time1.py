import datetime,pyglet
while True:
    time1 = str(datetime.datetime.now().time())
    print(time1)
    if time1 >= "21:38:50.00000":
        music = pyglet.resource.media('evt.mp3')
        music.play()

        pyglet.app.run()
