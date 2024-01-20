# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Bruxa", what_prefix='"', what_suffix='"')
define n = Character("")
define f = Character("Sapo", what_prefix='"', what_suffix='"')
define y = Character("Você", what_prefix='"', what_suffix='"')
define a = Character("Aldeões", what_prefix='"', what_suffix='"')
image splash = "logo.png"


transform shake:
    ease .06 yoffset 24
    ease .06 yoffset -24
    ease .05 yoffset 20
    ease .05 yoffset -20
    ease .04 yoffset 16
    ease .04 yoffset -16
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0

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
image red = "#FF0000"



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

    "Era mais outro dia qualquer enquanto você andava pelo mercado municipal, seguindo sua rotina usual, até você ouvir pessoas murmurando entre si, como se algo tivesse ocorrido."

    "Empolgado por algo que quebrasse a repetitividade de seu cotidiano, você se mistura no meio do público, discretamente tentando escutar qual era a novidade."

    show silhouette with dissolve

    a "Parece que alguns servos conseguiram escapar do acidente, mas eles deixaram o senhor para trás..."

    a "Meu deus... Será que ele está vivo ainda?"

    a "Bom, naquela floresta, duvido que vá sobreviver por muito tempo..."

    hide silhouette with dissolve

    "Ao escutar as fofocas que corriam pela rua, o que você entendeu foi que, aparentemente, houvera um acidente na floresta envolvendo uma das nobres casas do reino."

    "E como o senhor ainda não fora encontrado, então ele provavelmente estava lá perdido, senão morto."

    "Movido pela expectativa de encontrar ouro e tecidos luxuosos possivelmente deixados na carruagem quebrada, você partiu rapidamente em direção à floresta."

    stop nature fadeout 1.0
    stop music fadeout 1.0
    play audio "sfx-steps.ogg"

    scene bg forestday
    with fade
    play nature forest fadein 1.0
    play music ost1 fadein 1.0

    "Você anda pelos bosques, percorrendo a estrada até ela começar a desaparecer em meio às raízes e folhagem. Antes que você pudesse perceber, o caminho pelo qual você viera já estava fora de vista."

    "Ainda assim, você não se sente muito preocupado. Os raios de luz ainda são visíveis pelas copas das árvores, e os pássaros continuam a cantar. Certamente, não deve haver perigo."

    "Você tenta se guiar, indo à direção em que, teoricamente, teria ocorrido o acidente. Mas não importa para qual lado você fosse, não havia sinal algum de rastros de pessoas ou carruagens."

    "E, como se guiado pelo capricho do destino, o dia comecou a declinar rapidamente enquanto você se dá conta de que, no meio da busca por rastros de rodas e moedas de bronze, você acabou se perdendo."

    stop nature fadeout 1.0
    play nature forestnight fadein 1.0
    scene bg forestnight with dissolve

    "O cantar dos pássaros começa a desaparecer enquanto os animais se preparam para seu sono. E com o adormecer deles, possivelmente virá o despertar de outros..."

    "Você afasta esses pensamentos da mente, decidindo focar em encontrar o caminho de volta para fora da floresta antes que a noite se aprofunde."

    "E lembre-se do dizer, de que quem permanece na floresta após o pôr do sol jamais é visto novamente..."

    play audio "sfx-steps.ogg"

    "Você continua andando até se deparar com dois caminhos."

    "À direita, uma estrada que se assemelha às vias rápidas da Aldeia, ordenada com pedras comuns, como se para registrar sua presença."

    "Já o da esquerda é uma trilha entre árvores retorcidas, algumas delas cortadas de maneira rudimentar para criar uma passagem."

    "Você escolhe..."
    
    menu:
        "Ir à direita":
            jump right
        "Ir à esquerda":
            jump left


    
label right:
    play audio "sfx-steps.ogg"
    scene bg house with fade

    "Seguindo o caminho com uma certa facilidade, você se depara com uma misteriosa cabana no meio da floresta."

    "A tentação de passar a noite lá surge: seria um abrigo seguro dos animais selvagens e te daria mais tempo para encontrar o caminho de volta ao amanhecer."
    
    menu:
        "Abrir a porta":
            jump open
        "Bater na porta":
            jump knock
        
label open:
    "Sem hesitar, você empurra a porta lentamente."

    play audio "sfx-dooropen.ogg"
    scene bg room with fade

    "O interior está escuro e sombrio, mas você avança."

    with vpunch
    "De repente, uma voz estridente ecoa pela casa e, antes que você possa reagir, uma figura sombria salta na sua direção."

    scene white with dissolve

    "Ofuscado por luzes intensas, você de repente sente uma sensação estranha, seu corpo diminuindo rapidamente."

    scene bg room with dissolve

    "Em meio ao pânico, você tenta articular palavras mas o que você acaba ouvindo é..."

    play audio "sfx-frog.ogg"
    y "{i}Croac{/i}..?"

    "Com horror, você percebe que foi transformado em um sapo!"

    show bruxa dark with dissolve

    "Após soltar um breve suspiro, a figura a sua frente encara você, com um olhar desinteressado."

    s "De novo outro...?"

    "Ela resmunga, quase num murmúrio:"

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

    "Decidindo bater na porta, você ouve ruídos estranhos vindos de dentro da casa."

    play audio "sfx-dooropen.ogg"

    scene bg room with dissolve

    "Após um breve momento, a porta se abre lentamente, revelando uma jovem com vestimentas pesadas, de cor escura e adornada por símbolos."

    "Ela te encara, confusa."

    show witch confused with dissolve

    s "Como um simples aldeão conseguiu achar o caminho para cá?"

    "Ela pondera, te ignorando completamente."

    show witch serious with dissolve

    s "Talvez eu tenha esquecido de renovar meu feitiço de defesa semana passada."

    show bruxa confused2 with dissolve

    s "Ou..."

    show witch happy
    hide bruxa confused2 with dissolve

    

    "Apesar da desconfiança inicial, seu rosto se ilumina de repente com uma expressão animada."

    s "Entendi! Você veio pedir para ser meu aprendiz, não é? Te expulsaram da Aldeia?"

    show witch smile with dissolve

    s "Não se preocupe, pra sua sorte no momento eu estou com as mãos cheias e aceitando assistência para feitiços menores."

    "Parece que a bruxa entendeu suas intenções erroneamente... Mas a oferta dela parece ser considerável."

    menu:
        "Esclarecer que na verdade está perdido, e pedir ajuda para voltar pra casa.":
            jump lost
        "Aceitar ser um assistente para uma bruxa desconhecida e deixar sua vida na Aldeia para trás.":
            jump assistant
        


label lost:

    show witch confused with dissolve

    s "Voltar para a aldeia? ...Sério mesmo?"

    s "Você vai mesmo negar a oportunidade de aprender magia... Pra passar o resto da vida limpando estrume de vaca?"

    s "Acordar antes do sol nascer, trabalhar de manhã até a noite para que esses nobres corruptos tenham mais uma moeda de ouro no seu estoque?"

    "A Bruxa continua te encarando, desacreditada."

    show bruxa confused2 with dissolve

    "Após um momento de silêncio, ela ergue a mão."

    show witch serious 
    hide bruxa confused2 with dissolve

    s "Tudo bem então, você voltará para sua aldeia. Uma pessoa como você não faria um bom aprendiz de qualquer jeito."

    "A bruxa realiza um gesto mágico com a mão, sua visão começa a ser ofuscada por luzes brilhantes e de repente você perde sua consciência."


    play audio "sfx-magic.ogg"
    stop nature fadeout 1.0
    stop music fadeout 1.0
    scene white with Dissolve(3.0)
    pause 1.0
    scene bg shop with starTrans
    play nature village fadein 1.0
    play music ost4 fadein 1.0

    "Quando você desperta de novo, após o que parecia ser um piscar de olhos, você se encontra de volta na Aldeia."

    "No entanto, seu retorno mágico não passa despercebido pelos aldeões."

    show silhouette with dissolve

    a "De onde aquele cara veio...?"

    a "Você também viu? Ele apareceu do nada..."

    a "É um bruxo! Não há outra explicação!!!"

    hide silhouette with dissolve

    "Todos ficam surpresos com sua súbita aparição, alimentando suspeitas sobre sua conexão com forças sombrias."

    "Por todo lugar que você vai, você é seguido por olhares de escórnia ou medo. Os rumores se espalham cada vez mais com o passar dos dias."

    "Convencidos de que você fez um pacto com o diabo ou algo similar, os aldeões se reúnem para organizar o seu julgamento."

    "Não disposto a virar espetinho de churrasco, você abandona sua casa no meio da noite, buscando uma nova aldeia para recomeçar sua vida."

    scene black with fade 

    stop music fadeout 1.0
    stop nature fadeout 1.0
    
    pause 1.0

    scene bg end2 with dissolve

    $ cinematic = True
    
    n "Final 2: Ovelha Negra"

    return


label assistant:

    show witch smile with dissolve

    s "Ótimo! Estou contando com você a partir de hoje."

    show witch happy with dissolve 

    "Ao se deparar com a proposta da bruxa, você olha para a sua vida monótona na Aldeia e decide jogar tudo para o alto!"

    "Foi-se o tempo que a sua maior preocupação era tender a colheita e se preocupar se teria grãos o suficiente para passar o inverno."

    stop nature fadeout 1.0
    stop music fadeout 1.0
    play music  ost4 fadein 1.0
    scene bg room with fade

    "Após meses imerso na magia, você aprende uma série de truques e feitiços, mas percebe que algo está faltando."

    y "Bruxa, eu... Tenho estudado bastante e quero avançar nos estudos de magia. Quando poderei aprender feitiços mais complexos?"

    show witch serious with dissolve

    "Meio ano se passou desde aquele fatídico dia em você que aceitou ser aprendiz da Bruxa."
    
    "Além de colher ervas e dominar alguns feitiços menores, você não progrediu em quase nada."

    show witch happy with dissolve 

    s "Oh, jovem aprendiz, compreendo sua curiosidade e vontade de avançar."

    s "No entanto, a magia é um universo vasto, e sua jornada ainda está no começo."

    "Lá vem ela de novo... Você começava a suspeitar que a Bruxa precisava mais de um empregado do que de um aprendiz de fato."

    y "Mas tenho me esforçado muito. Acredito que estou pronto para aprender mais, para ir além."

    y "Além de limpar a cabana e cozinhar o almoço, é claro."

    show bruxa serious2 with dissolve

    s "A pressa nem sempre é uma aliada na magia, meu caro."

    show witch serious 
    hide bruxa serious2 with dissolve

    s "Para dominar feitiços complexos, é preciso mais do que apenas estudo."

    s "É necessário tempo, prática e experiência para manipular as energias místicas."

    y "O que mais eu preciso fazer? Como posso mostrar que estou pronto?"

    s "Provar-se não é apenas sobre vontade ou estudo."

    show witch smile with dissolve

    s "É sobre experiência real, enfrentar desafios e compreender profundamente o equilíbrio entre o mundo natural e o mágico."

    y "Entendi..."

    "Você claro, fingiu que entendeu, mas, assim que a Bruxa se distraiu, fugiu com seus poucos pertences em direção à fronteira da Floresta."

    play audio "sfx-steps.ogg"
    scene bg forestday with fade
    play nature forest fadein 1.0

    y "Com os poucos truques que consegui aprender, eu tenho certeza de que consigo fazer uma fortuna como artista de rua ou até mais na Capital!"

    y "Afinal, estávamos falando de verdadeira magia!"

    "Mesmo os feitiços sendo de baixo nível, sua fé nos bolsos fundos dos nobres entediados da capital o motivava."

    "Ao pensar nas várias moedas de ouro que receberia no futuro, você sorriu."

    "Porém... A Floresta te impede de sair."

    "Você dá voltas e voltas mas sempre acaba se encontrando no mesmo lugar."

    "Retornando ao único caminho pelo qual você consegue seguir, você se encontra de volta na frente da cabana da Bruxa."

    scene bg house with fade

    show witch happy with dissolve

    s "Vejo que você se perdeu novamente, Aprendiz!"

    show witch smile with dissolve
    
    s "Mas não se preocupe, a Floresta só permite a saída de seres poderosos, como eu, ou seres completamente desprovidos de magia, como você era antes do seu despertar mágico."

    "Preso na floresta, você as vezes se pergunta se não seria mais fácil ter continuado no seu caminho e roubado os pertences do nobre que se acidentou."

    show witch happy with dissolve

    s "Veja pelo lado bom, em apenas 57 anos, você estará pronto para aprender os feitiços mais complexos!"

    "A busca por liberdade, agora, parece um sonho distante."

    scene black with fade 

    stop nature fadeout 1.0
    
    pause 1.0

    scene bg end3 with dissolve

    $ cinematic = True
    
    n "Final 3: Assistente da Bruxa"

    return



label left:
    play audio "sfx-steps.ogg"
    scene bg darkforest with fade

    "Você seguiu o caminho à esquerda com certa dificuldade, quase tropeçando em vários momentos."

    "Enquanto você se esforça para passar em meio aos troncos recurvados, algo vermelho no mato chama sua atenção..."

    "Ao abaixar e tentar observar isso de perto, você percebe que são farrapos de tecidos, dos luxuosos ainda!"

    y "É isso! Deve ser por aqui..."

    "Você empolgadamente segue atrás da trilha de pedaços rasgados de panos, até ouvir um barulho."

    play audio "sfx-frog.ogg"

    y "...Croak?"

    "Você olha para baixo mais uma vez, notando um bando de sapos de diversos tamanhos e cores. Eles saltam em sua direção, se agrupando a sua volta."

    play audio "sfx-frogs.ogg"

    y "...?"

    "A estranha situação em que você se encontra te deixa parado, confuso enquanto pensa sobre o que é que esses sapos viram em você."

    "Eles não parecem hostis, apenas que querem muito sua atenção. Você continua caminhando pela floresta, ignorando os sapos que continuam te seguindo."

    "Até que, de repente, todos eles começam a se dispersar. Em poucos segundos, não há mais nenhum a sua volta."

    "Mas isso não significava que você agora estava em paz. Muito pelo contrário, aliás."

    play audio "sfx-monstersteps.ogg"
    stop music fadeout 1.0
    

    "O som de pegadas de algo claramente maior do que sua mente poderia imaginar estrondeavam pela floresta. A cada passo, você sentia a criatura chegando mais perto."

    play music  ost5 fadein 1.0
    play audio "sfx-monstersteps.ogg"

    "Você tenta correr mas as árvores ao seu caminho se mostram cada vez mais recurvas, e a passagem se torna gradualmente mais difícil... E, finalmente, impossível."

    "De costas viradas a troncos e vinhas, a criatura se aproxima enquanto você não tem opção além de esperar seu encontro."

    play audio "sfx-monstersteps.ogg"
    show sapo with dissolve

    "De cara a cara com o monstro, você percebe que ele é um... sapo? Só que bem maior... Talvez no mínimo duas ou três vezes sua altura."

    "Enquanto seus pensamentos correm tentando processar a absurdez de sua situação, eles logo são interrompidos por um rugido do sapo que quase estoura seus tímpanos."

    show sapo at shake
    play audio "sfx-monster2.ogg"
    with hpunch
    y "...!"

    "Nesses segundos que pareciam passar como horas, sua mente pensava em todo cenário possível, desesperadamente tentando encontrar uma rota de fuga."

    show sapo at shake
    play audio "sfx-monster.ogg" 

    "Até que o sapo solta mais outro rugido, só que desta vez mais agudo e... Trêmulo?"

    show sapo at shake
    f "Uu..."

    "Por alguma razão, você consegue sentir... algo, vindo da criatura. Talvez aquilo não era um rugido, e sim, um choro. De medo? Ou quem sabe, desespero..."

    "Sua mão sente a textura de cipós e vinhas logo às suas costas. Você então é confrontando com uma decisão:"

    menu:
        "Encarar a criatura.":
            jump stay
        "Escalar a árvore.":
            jump run

label stay:
    stop music fadeout 1.0
    play music ost1 fadein 1.0

    "Você encara a criatura com apreensão. Talvez esses olhos molhados, como se lacrimejando, que você observa sejam apenas parte da natureza do monstro como um sapo. Mas você sente que há algo a mais..."

    show sapo:
        ease 1.5 zoom 1.2 yoffset 120

    "De pernas trêmulas mas com um resquício de esperança, você dá um passo à frente."

    "Mas inesperadamente, o monstro que estava apenas te observando de volta com seus olhos suplicantes, solta mais um rugido que varre pela floresta."

    play audio "sfx-monster2.ogg"
    with hpunch
    "Você instintivamente vira seu rosto e fecha os olhos em reação."

    "Quando você os abre de novo, o olhar que a criatura te dá não é mais o mesmo."

    show sapo:
        ease 1.5 zoom 1.5 yoffset 300

    "Como se em um transe, os olhos do monstro transbordam sedentos, saliva escorrendo pela sua boca que começa a abrir, lentamente indo a sua direção."

    "E antes que você possa reagir, a única coisa que você consegue sentir é a mandíbula do sapo estilhaçando sua espinha."

    stop nature fadeout 0.5
    stop music fadeout 0.5
    play audio "sfx-bones.ogg"
    scene red with Dissolve(0.1)
    pause 3.0

    scene black with fade 

   
    
    pause 1.0

    scene bg end4 with dissolve

    $ cinematic = True
    
    n "Final 4: Banquete de Sapo"

    return

















    

