# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Bruxa", what_prefix='"', what_suffix='"')
define n = Character("")
define y = Character("Você", what_prefix='"', what_suffix='"')
define a = Character("Aldeões", what_prefix='"', what_suffix='"')
image splash = "logo.png"

image witch smile:
    "bruxa smile"
    pause 7
    "bruxa smile2"
    pause .05
    "bruxa smile1"
    pause .07
    "bruxa smile2"
    pause .05
    repeat

image witch confused:
    "bruxa confused"
    pause 7
    "bruxa confused1"
    pause .05
    "bruxa confused2"
    pause .07
    "bruxa confused1"
    pause .05
    repeat

image witch serious:
    "bruxa serious"
    pause 7
    "bruxa serious1"
    pause .05
    "bruxa serious2"
    pause .07
    "bruxa serious1"
    pause .05
    repeat

image witch happy:
    "bruxa happy"
    pause 7
    "bruxa happy1"
    pause .05
    "bruxa happy2"
    pause .07
    "bruxa happy1"
    pause .05
    repeat

image white = "#ffffff"




label splashscreen:
    show blackborder onlayer UI 
    
    scene blackbg
    with Pause(1)

    show splash with dissolve:
        truecenter
    with Pause(2)

    scene blackbg with dissolve

    return

label start:
    show border onlayer UI 

    play nature village fadein 1.0
    play music ost3 fadein 1.0

    scene bg shop
    with fade

    n "Era mais outro dia qualquer enquanto você andava pelo mercado municipal, seguindo sua rotina usual, até você ouvir pessoas murmurando entre si, como se algo tivesse ocorrido."

    n "Empolgado por algo que quebrasse a repetitividade de seu cotidiano, você se mistura no meio do público, discretamente tentando escutar qual era a novidade."

    show silhouette with dissolve

    a "Parece que alguns servos conseguiram escapar do acidente, mas eles deixaram o senhor para trás..."

    a "Meu deus... Será que ele está vivo ainda?"

    a "Bom, naquela floresta, duvido que vá sobreviver por muito tempo..."

    hide silhouette with dissolve

    n "Ao escutar as fofocas que corriam pela rua, o que você entendeu foi que, aparentemente, houvera um acidente na floresta envolvendo uma das nobres casas do reino."

    n "E como o senhor ainda não fora encontrado, então ele provavelmente estava lá perdido, senão morto."

    n "Movido pela expectativa de encontrar ouro e tecidos luxuosos possivelmente deixados na carruagem quebrada, você partiu rapidamente em direção à floresta."

    stop nature fadeout 1.0
    stop music fadeout 1.0
    play audio "sfx-steps.ogg"

    scene bg forestday
    with fade
    play nature forest fadein 1.0
    play music ost1 fadein 1.0

    n "Você anda pelos bosques, percorrendo a estrada até ela começar a desaparecer em meio às raízes e folhagem. Antes que você pudesse perceber, o caminho pelo qual você viera já estava fora de vista."

    n "Ainda assim, você não se sente muito preocupado. Os raios ainda são visíveis pelas copas das árvores, e os pássaros continuam a cantar. Certamente, não deve haver perigo."

    n "Você tenta se guiar, indo à direção em que, teoricamente, teria ocorrido o acidente. Mas não importa para qual lado você fosse, não havia sinal algum de rastros de pessoas ou carruagens."

    n "E, como se guiado pelo capricho do destino, o dia comecou a declinar rapidamente enquanto você se dá conta de que, no meio da busca por rastros de rodas e moedas de bronze, você acabou se perdendo."

    stop nature fadeout 1.0
    play nature forestnight fadein 1.0
    scene bg forestnight with dissolve

    n "O cantar dos pássaros começa a desaparecer enquanto os animais se preparam para seu sono. E com o adormecer deles, possivelmente virá o despertar de outros..."

    n "Você afasta esses pensamentos da mente, decidindo focar em encontrar o caminho de volta para fora da floresta antes que a noite se aprofunde."

    n "E lembre-se do dizer, de que quem permanece na floresta após o pôr do sol jamais é visto novamente..."

    play audio "sfx-steps.ogg"

    n "Você continua andando até se deparar com dois caminhos."

    n "À direita, uma estrada que se assemelha às vias rápidas da Aldeia, ordenada com pedras comuns, como se para registrar sua presença."

    n "Já o da esquerda é uma trilha entre árvores retorcidas, algumas delas cortadas de maneira rudimentar para criar uma passagem."

    n "Você escolhe..."
    
    menu:
        "Ir à direita":
            jump right
        "Ir à esquerda":
            jump left


    
label right:
    play audio "sfx-steps.ogg"
    scene bg house with fade

    n "Seguindo o caminho com uma certa facilidade, você se depara com uma antiga casa que parece abandonada."

    n "A tentação de passar a noite lá surge: seria um abrigo seguro dos animais selvagens e te daria mais tempo para encontrar o caminho de volta ao amanhecer."
    
    menu:
        "Abrir a porta":
            jump open
        "Bater na porta":
            jump knock
        
label open:
    n "Sem hesitar, você empurra a porta lentamente."

    play audio "sfx-dooropen.ogg"
    scene bg room with fade

    n "O interior está escuro e sombrio, mas você avança."

    with vpunch
    n "De repente, uma voz estridente ecoa pela casa e, antes que você possa reagir, uma figura sombria salta na sua direção."

    scene white with dissolve

    n "Ofuscado por luzes intensas, você de repente sente uma sensação estranha, seu corpo diminuindo rapidamente."

    scene bg room with dissolve

    n "Em meio ao pânico, você tenta articular palavras mas o que você acaba ouvindo é..."

    play audio "sfx-frog.ogg"
    y "{i}Croac{/i}..?"

    n "Com horror, você percebe que foi transformado em um sapo!"

    show bruxa dark with dissolve

    n "Após soltar um breve suspiro, a figura a sua frente encara você, com um olhar desinteressado."

    n "Ela resmunga, quase num murmúrio:"

    s "Detesto visitas indesejadas a essa hora do dia." 

    scene black with fade 

    stop music fadeout 1.0
    
    pause 1.0

    scene bg end1 with dissolve

    $ cinematic = True
    
    n "Final 1: Visita folgada"

    return










    





label left:


    
    
    
    
    
    

    s "However, do NOT resell any portion of this GUI as your own."

    s "Anyway, if you {i}are{/i} going to use it in  a commercial project, please consider tipping my kofi."

    show sprite1 at center with moveinleft

    $ cinematic = True

    s "I'm literally just a college student with no income."

    s "Right now we've entered the UI's cinematic mode."

    s "If you want to use this, add \"$ cinematic = True\" to your script turn it on."

    s "And if you don't want to use it anymore..."

    $ cinematic = False

    s "Just change True to False."

    show sprite1 at left with moveinright

    menu:
        s "This is what menu choices look like if you add text."
        
        "test choice 1":
            pass
        "test choice 2":
            pass
        "test choice 3":
            pass
        "test choice 4":
            pass
        "test choice 5":
            pass

    s "And this is what they look like without it."
    
    menu:
        "test choice 1":
            pass
        "test choice 2":
            pass
        "test choice 3":
            pass
        "test choice 4":
            pass
        "test choice 5":
            pass

    
    s "That's it for this portion."

    s "Try screenshotting and opening up the game menu by clicking the sun below."

    s "Ciao!"

    # This ends the game.

    return
