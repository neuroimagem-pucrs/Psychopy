from psychopy import visual,core,event

window = visual.Window(color="black")

#TELA 1
message1 = visual.TextStim(window,text="Bem-Vindo",height=0.3)
message1.draw()
window.flip()
event.waitKeys(keyList=['space'])

#TELA 2
message2 = visual.TextStim(window,text="Tarefa Motora",height=0.2)
message2.draw()
window.flip()
event.waitKeys(keyList=['space'])

#TELA 3
message3 = visual.TextStim(window,text="Pre-Scan Pronto?",height=0.15)
message3.draw()
window.flip()
event.waitKeys(keyList=['space'])

#TELA 4
message4 = visual.TextStim(window,text="Aguarde",height=0.2)
message4.draw()
window.flip()
event.waitKeys(keyList=['5'])

#TELA 5
message5 = visual.TextStim(window,text="+",height=0.3)
message5.draw()
window.flip()
core.wait(6)

for i in range(0,4):
    #TELA 6
    message6 = visual.TextStim(window,text="Direita",pos=(0.5,0.0),height=0.2)
    message6.draw()
    window.flip()
    core.wait(15)

    #TELA 7
    message7 = visual.TextStim(window,text="+",height=0.3)
    message7.draw()
    window.flip()
    core.wait(1.5)

    #TELA 8
    message8 = visual.TextStim(window,text="Esquerda",pos=(-0.5,0.0),height=0.2)
    message8.draw()
    window.flip()
    core.wait(15)

    #TELA 9
    message9 = visual.TextStim(window,text="+",height=0.3)
    message9.draw()
    window.flip()
    core.wait(1.5)

    #TELA 10
    message10 = visual.TextStim(window, text="Esquerda",pos=(-0.5,0.0), height=0.2)
    message10.draw()
    message11 = visual.TextStim(window,text="Direita",pos=(0.5,0.0),height=0.2)
    message11.draw()
    window.flip()
    core.wait(15)

    #TELA 11
    message12 = visual.TextStim(window,text="+",height=0.3)
    message12.draw()
    window.flip()
    core.wait(1.5)
