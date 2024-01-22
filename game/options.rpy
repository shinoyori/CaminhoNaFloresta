

## Nome do jogo na janela
define config.name = _("O Caminho na Floresta")

## Determina se o nome do jogo aparece na tela principal
define gui.show_name = False

## Versão do jogo
define config.version = "1.0"

## Adiciona mais um canal de música para tocar sons de fundo (como o da floresta)
init python:
    renpy.music.register_channel("nature", "music", loop=True)

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")

## Nome para executáveis
define build.name = "CaminhoNaFloresta"



## Sounds and music ############################################################

## Barras de volume
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

## Música do menu principal
define config.main_menu_music = "ost1.ogg"




## Camadas ######################################################################
define config.layer_clipping['master'] = (0, 102, 1920, 876)
define config.layers = [ 'master', 'UI', 'transient', 'screens', 'overlay', 'particles' ]




## Transições #################################################################

## Entrada e saída da tela principal

define config.enter_transition = starTrans
define config.exit_transition = starTrans

## Entre as telas

define config.intra_transition = starTrans


## Depois de carregar

define config.after_load_transition = starTrans


## Quando o jogo acaba

define config.end_game_transition = starTrans
define config.end_splash_transition = dissolve


define config.window = "auto"


## Transição janela de diálogo

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preferências #########################################################

## Velocidade do texto

default preferences.text_cps = 50


## Velocidade do auto

default preferences.afm_time = 15


## Save directory ##############################################################

define config.save_directory = "caminhoNaFloresta-1702444616"


## Ícone ########################################################################

define config.window_icon = "gui/window_icon.png"











## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


