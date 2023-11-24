txt = input()

happy_face = ':)'
sad_face = ':('

if happy_face in txt:
    txt = txt.replace(':)', '🙂')

if sad_face in txt:
    txt = txt.replace(':(', '🙁')

print(txt)
