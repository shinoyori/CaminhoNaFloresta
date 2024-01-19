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
    pause 5
    "bruxa smile2"
    pause .05
    "bruxa smile1"
    pause .07
    "bruxa smile2"
    pause .05
    repeat

image witch confused:
    "bruxa confused"
    pause 2
    "bruxa confused1"
    pause .05
    "bruxa confused2"
    pause .07
    "bruxa confused1"
    pause .05
    "bruxa confused"
    pause 3
    repeat

image witch serious:
    "bruxa serious"
    pause 5
    "bruxa serious1"
    pause .05
    "bruxa serious2"
    pause .07
    "bruxa serious1"
    pause .05
    repeat

image witch happy:
    "bruxa happy"
    pause 5
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

    n "Ainda assim, você não se sente muito preocupado. Os raios de luz ainda são visíveis pelas copas das árvores, e os pássaros continuam a cantar. Certamente, não deve haver perigo."

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


label knock:

    play audio "sfx-knock.ogg"

    n "Decidindo bater na porta, você ouve ruídos estranhos vindos de dentro da casa."

    play audio "sfx-dooropen.ogg"

    scene bg room with dissolve

    n "Após um breve momento, a porta se abre lentamente, revelando uma jovem com vestimentas pesadas, de cor escura e adornada por símbolos."

    n "Ela te encara, confusa."

    show witch confused with dissolve

    s "Como um simples aldeão conseguiu achar o caminho para cá?"

    n "Ela pondera, te ignorando completamente."

    show witch serious with dissolve

    s "Talvez eu tenha esquecido de renovar meu feitiço de defesa semana passada."

    show bruxa confused2 with dissolve

    s "Ou..."

    show witch happy
    hide bruxa confused2 with dissolve

    

    n  "Apesar da desconfiança inicial, seu rosto se ilumina de repente com uma expressão animada."

    s "Entendi! Você veio pedir para ser meu aprendiz, não é? Te expulsaram da Aldeia?"

    show witch smile with dissolve

    s "Não se preocupe, pra sua sorte no momento eu estou com as mãos cheias e aceitando assistência para feitiços menores."

    n "Parece que a bruxa entendeu suas intenções erroneamente... Mas a oferta dela parece ser considerável."

    menu:
        "Esclarecer que na verdade está perdido, e pedir ajuda para voltar pra casa.":
            jump lost
        "Aceitar ser um assistente para uma bruxa desconhecida e deixar sua vida na Aldeia para trás.":
            jump assistant
        


label lost:

    show witch confused with dissolve

    s "Voltar para a aldeia? ...Sério mesmo?"

    s "Você vai mesmo negar a oportunidade de aprender magia... Pra passar o resto da vida limpando estrume de vaca?"

    s "Acordar antes do sol nascer, trabalhar de manhã até a noite para o Lorde ter mais uma moeda de ouro no seu estoque?"

    n "A Bruxa continua te encarando, desacreditada."

    show bruxa confused2 with dissolve

    n "Após um momento de silêncio, ela ergue sua mão"

    show witch serious 
    hide bruxa confused2 with dissolve

    s "Tudo bem então, você voltará para sua aldeia. Uma pessoa como você não faria um bom aprendiz de qualquer jeito."

    n "A bruxa realiza um gesto mágico com a mão, sua visão começa a ser ofuscada por luzes brilhantes e de repente você perde sua consciência."


    play audio "sfx-magic.ogg"
    stop nature fadeout 1.0
    scene white with Dissolve(3.0)
    pause 1.0
    scene bg shop with starTrans
    play nature village fadein 1.0

    n "Quando você desperta de novo, após o que parecia ser um piscar de olhos, você se encontra de volta na Aldeia."

    n "No entanto, seu retorno mágico não passa despercebido pelos aldeões."

    show silhouette with dissolve

    a "De onde aquele cara veio...?"

    a "Você também viu? Ele apareceu do nada..."

    hide silhouette with dissolve

    n "Todos ficam surpresos com sua súbita aparição, alimentando suspeitas sobre sua conexão com forças sombrias."

    n "Convencidos de que você fez um pacto com o diabo ou algo similar, os aldeões se reúnem para organizar o seu julgamento."

    n "Não disposto a virar espetinho de churrasco, você abandona sua casa no meio da noite, buscando uma nova aldeia para recomeçar sua vida."

    scene black with fade 

    stop music fadeout 1.0
    stop nature fadeout 1.0
    
    pause 1.0

    scene bg end2 with dissolve

    $ cinematic = True
    
    n "Final 2: Ovelha Negra"

    return


label assistant:
    









    





label left:

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
