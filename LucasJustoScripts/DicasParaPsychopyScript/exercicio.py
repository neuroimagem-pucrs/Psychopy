from psychopy import visual,core,event,data,clock

#CRIANDO OBJETOS IMPORTANTES
window = visual.Window([1200,900],allowGUI=True, color="black")#criando a janela onde tudo aparecerá, com tamanho 1200x900 e cor preta.
storage = data.ExperimentHandler(name="exercicio") #criando um armazenador de dados para poder salvar em txt depois.
clock = core.Clock()#criando o clock usado para controle do tempo no experimento.

#PRIMEIRA APARIÇÃO DA TELA
message=visual.TextStim(window,text="Hello Stimuli!",font="Times New Roman",pos=(0.5,0.5),height=0.2)#Criando mensagem na janela principal, com fonte modificada, tamanho modificado e posição modificada.
#sobre a fonte: tem que digitar uma que tenha no sistema ou importar arquivos que contenham a fonte.
#sobre o tamanho: voce só pode escolher a altura, e a largura se adapta à ela. 0.1 é a altura padrao.
#sobre a posição: 0.0 é o centro.
message.draw()#botando a mensagem  na janela.
window.flip()#atualizando a janela para mensagem realmente aparecer.
clock.reset()#fazendo o clock ficar com tempo 0.0, no momento em que aparece a primeira imagem.
event.waitKeys(maxWait=2,keyList=['space'])#esperando a tecla space para ir para a proxima mudança de tela.(se demorar mais de 2 segundos avança sozinho)

#SEGUNDA APARIÇÃO NA TELA(COM IMAGEM)
message2 = visual.ImageStim(window,image="exercicio.jpg")#Criando imagem ao em vez de texto.
message2.draw()
window.flip()
event.waitKeys(maxWait=2,keyList=['space'])

#TERCEIRA APARIÇÃO NA TELA(SALVANDO RESPOSTA DO USUÁRIO EM TXT)
message3=visual.TextStim(window,text="press 1 or 2")
message3.draw()
window.flip()
key=event.waitKeys(maxWait=3,keyList=['1','2'],timeStamped=clock)#armazenando a primeira tecla pressionada(entre as teclas da lista) e armazena em outra lista de tuplas (fromato: [tecla,tempo desde o inicio do clock).

#PASSANDO A RESPOSTA PARA UM EXPERIMENTHANDLER E DO EXPERIMENTHANDLER PRO TXT.
storage.addData('key',key)#armazenando a tupla [tecla,tempo] no handler.
storage.saveAsWideText(fileName="exercicio.txt",appendFile=True)#passando do handler pro txt.

