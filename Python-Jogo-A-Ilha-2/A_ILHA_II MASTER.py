"""
Materia: Laboratorio de programação
                                                Projeto 2

Jogo: A ilha 2 liberdade é escravidão, é um jogo de tabuleiro multijogador
Nome: Grégory Fernandes Ramires TIA: 41706692
Nome: Matheus Gois  TIA: 41741461
Nome: David Couto TIA: 41382722
"""
# --------------------------------import-----------------------------------------------------------

import random
import time
time.sleep(3)
#-------------------------------------------Apresentação-------------------------------------------
print("                            ...----....")
print("                      ..-:'''         '''-..") 
print("                   .-'       A ILHA II     '-.")
print("                 .'      .             .       '.")
print("               .'   .   .LIBERDA É ESCRAVIDÃO.  ''.")
print("             .'  .    .       .   .   .     .   . ..:.")
print("           .' .   . .  .       .   .   ..  .   . ....::.")
print("          ..   .   .      .  .    .     .  ..  . ....:IA.")
print("         .:  .   .    .    .  .  .    .. .  .. .. ....:IA.")
print("        .: .   .   ..   .    .     . . .. . ... ....:.:VHA.")
print("        '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.")
print("       .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.")
print("      .:.... .   . .'::'.. .   .  . .:.:.:II;,. .. ..:IHIMMA")
print("      ':.:.. ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM")
print("     .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM")
print("    .:.:V.:IVHHHHHHHMHMHHH::..:' .:HIHHHHHHHHHHHHHMHHA. .VMMM.")
print("    :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI")
print("    ::V..:VIHHHHHHMMMHHHHHH. .   .I':IIMHHMMHHHHHHHHHHHAPI:WMM")
print("    ::'. .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM")
print("    :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW")
print("    '.  ..:..:.:IHHHHHMMHV' .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV")
print("     :.  .:..:'.:.:TPP'   .AVMMHMMA.:. ' VMMHHHP.:... .. :IVAI")
print("    .:.   '... .:''   .   ..HMMMHMMMA::. .'VHHI:::....  .:IHW'")
print("    ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM")
print("  : .   .''' .:.V'. .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.")
print("  :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV':T::I::.'.:IHIMA")
print("  'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH")
print("    'IHH:.II:.. .:. .  . . . ' :HB"" . . ..PI:.::.:::..:IHHMMV")
print("     :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM")
print("     :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM")
print("     :'VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI")
print( "     :.'VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI")
print("     :..VIHIHMMMI...::.,:.,:!'I:!'I!'I!'V:AI:VAMMMMMMHMMMMMM'")
print("     ':.:HIHIMHHA:'!!'I.:AXXXVVXXXXXXXA:.'HPHIMMMMHHMHMMMMMV")
print("       V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM")
print( "         'I::IVA ASSSSXS41746491SSSSBBMMMBS.VVMMHIMM''")
print("          I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI")
print("         .I::. 'H:XIIXBBMMMMMMMMMMMM41706692GFDGDPHIIMM'")
print( "         :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM")
print("         :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM")
print("         ::.I:.  ':'SSSSSSSIS41382722SDGSBMMB:AHI:..MMM.")
print( "         ::.I:. . ..:'BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI")
print("         :..::.  . ..::':BBBBBSSBBBMMMB:MMMMHHII::IHHMI")
print("         ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV'")
print("           'V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'")
print("            ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM")
print("              '::....::.:::..:..::IIIIIHHHHMMMHHMV")
print("                '::.::.. .. .  ...:::IIHHMMMMHMV")
print("                  'V::... . .I::IHHMMV'........")
print("                    'VHVHHHAHHHHMMV:..........'\n\n")


print("                 ░▄█▀▄      ░▐██▒██░░░░▐█░▐█ ░▄█▀▄ ")
print("                ░▐█▄▄▐█      ░█▌▒██░░░░▐████░▐█▄▄▐█")
print("                ░▐█ ░▐█     ░▐██▒██▄▄█░▐█░▐█░▐█ ░▐█\n\n")
 

print("                             ░▐██░▐██")
print("                              ░█▌ ░█▌")
print("                             ░▐██░▐██\n\n\n")


time.sleep(3)
print("             █▀▄ ▄▀▄ ▄▀▀ █▀▀ ▄▀▄ █▀▄ ▄▀▄     █▀▀ █▄░▄█ ")    
print("             █▀█ █▀█ ░▀▄ █▀▀ █▀█ █░█ █░█     █▀▀ █░█░█  ")   
print("             ▀▀░ ▀░▀ ▀▀░ ▀▀▀ ▀░▀ ▀▀░ ░▀░     ▀▀▀ ▀░░░▀  ")
print("             █▀ ▄▀▄ ▀█▀ ▄▀▄ ▄▀▀     █▀▀▄ █▀▀ ▄▀▄ ▀ ▄▀▀ ")
print("             █▀ █▀█ ░█░ █░█ ░▀▄     █▐█▀ █▀▀ █▀█ █ ░▀▄") 
print("             ▀░ ▀░▀ ░▀░ ░▀░ ▀▀░     ▀░▀▀ ▀▀▀ ▀░▀ ▀ ▀▀░\n\n\n")
time.sleep(3)

#-------------------------------------------------TABULEIRO------------------------------------------------
print("\n\n")
print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")    
tabuleiro = str.upper(input('             DESEJA VER O TABULEIRO? (sim) ou (não) :'))
print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")       
print("\n\n")

while tabuleiro != 'SIM' and tabuleiro != 'NÃO' and tabuleiro != 'NAO':
    tabuleiro = str.upper(input('DESEJA VER O TABULEIRO? (Digite uma entrada válida); (sim) ou (não) :'))
if tabuleiro == 'SIM':
    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                                                                       █")
    print(" █                                                                                                       █")
    print(" █                                                                                                       █")
    print(" █                                                                                                       █")
    print(" █                                 ░▐██▒██▄░▒█▌░▐██░▐█▀█░▐██▒▐█▀▀█▌                                      █")
    print(" █                                 ─░█▌▒▐█▒█▒█░─░█▌░▐█───░█▌▒▐█▄▒█▌                                      █")         
    print(" █                                 ░▐██▒██░▒██▌░▐██░▐█▄█░▐██▒▐██▄█▌                                      █")
    print(" █                                                                                                       █")
    print(" █                                                                                                       █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")



    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █                                                    █")
    print(" █             Nada para ser feito aqui             █     Onde deve seguir o conselho do Pensador        █")
    print(" █                                                  █                                                    █")
    print(" █                        ▒▄█░                      █                      ▒▄▀▄                          █")
    print(" █                        ░▒█░                      █                      ░▒▄▀                          █")
    print(" █                        ▒▄█▄                      █                      ▒█▄▄                          █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █                                                    █")
    print(" █             Espere sua próxima jogada            █          tente lamber o seu cotovelo               █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █                                                    █")
    print(" █       Você cruzou o caminho do Sérgio Moro       █             Nada para ser feito aqui               █")
    print(" █              volte ao início do jogo             █                                                    █")
    print(" █                        ▒▄▀▀▄                     █                     ░▒▄▀█░                         █")
    print(" █                        ░░▒▀▌                     █                     ▒█▄▄█▄                         █")
    print(" █                        ▒▀▄▄▀                     █                     ░░░▒█░                         █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █                                                    █")
    print(" █             volte ao início do jogo              █             Espere sua próxima jogada              █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")



    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █             Você encontrou informações           █                                                    █")
    print(" █             cruciais de seu adversário e         █      Você extingue uma reserva na Amazônia para    █")
    print(" █                                                  █                 ampliar exploração,                █")
    print(" █                        ▒█▀▀                      █                      ▒▄▀▀▄                         █")
    print(" █                        ▒▀▀▄                      █                     ░▒█▄▄░                         █")
    print(" █                        ▒▄▄▀                      █                      ▒▀▄▄▀                         █")         
    print(" █                                                  █                                                    █")
    print(" █          ele deve dançar uma música de sua       █               imite uma motossera                  █")
    print(" █                      escolha.                    █        por 10 segundos e avance duas casas.        █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █  Você está sendo investigado por inquérito, faça █                                                    █")
    print(" █  uma imitação de algum famoso, para treinar sua  █            Nada para ser feito aqui                █")
    print(" █     expressãodiante do juiz, caso contrário,     █                                                    █")
    print(" █                        ▒▀▀█                      █                      ▒▄▀▀▄                         █")
    print(" █                        ░▒█░                      █                      ▒▄▀▀▄                         █")
    print(" █                        ▒▐▌░                      █                      ▒▀▄▄▀                         █")         
    print(" █                                                  █                                                    █")
    print(" █                     seu adversário               █                                                    █")
    print(" █         avançará duas casas e você voltará 3     █            Espere sua próxima jogada               █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █ Você está sendo investigado, mas conseguiu apoio █                                                    █")
    print(" █trocando alguns votos por leis mais brandas       █          Nada para ser feito aqui                  █")
    print(" █ao trabalho análogo ao escravos, toda vitória tem █                                                    █")
    print(" █que ser comemorada!     ▒▄▀▀▄                     █                ▒▄█░▒ ▄▀▀▄                          █")
    print(" █escolha uma música para ▒▀▄▄▀                     █                ░▒█░▒▒█ ▒█                          █")
    print(" █seu adversário cantar   ▒▒▄▄▀                     █                ▒▄█▄▒▒▀▄▄▀                          █")         
    print(" █até o final sem errarSe ele acertar ele avança uma█                                                    █")
    print(" █casa e você retornará 3, caso contrário ele       █                                                    █")
    print(" █pagará o pato(pizza).                             █         espere sua próxima jogada                  █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █   É divulgada a Lista Suja do Trabalho Escravo,  █                                                    █")
    print(" █    isso é péssimo para sua campanha. passe essa  █           Nada para ser feito aqui                 █")
    print(" █                                                  █                                                    █")
    print(" █                    ▒▄█░▒▄█░▒                     █                   ▒▄█░▒▒▄▀▄                        █")
    print(" █                    ░▒█░░▒█░▒                     █                   ░▒█░░▒ ▄▀▒                       █")
    print(" █                    ▒▄█▄▒▄█▄▒                     █                   ▒▄█▄▒▒█▄▄                        █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █                                                    █")
    print(" █   rodada com os olhos fechados e volte 5 casas.  █           Espere sua próxima jogada               █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █     Você passa por um processo de impeachment,     █")
    print(" █    Você passa dois dias internado no hospital,   █ escolha alguém para dançar valsa e dançem enquanto █")
    print(" █                                                  █                                                    █")
    print(" █                     ▒▄█░▒▄▀▀▄                    █                ▒▄█░░▒▄▀█░                          █")
    print(" █                     ░▒█░░░▒▀▌                    █                ░▒█░▒█▄▄█▄                          █")
    print(" █                     ▒▄█▄▒▀▄▄▀                    █                ▒▄█▄▒░░░█░                          █")         
    print(" █                                                  █                                                    █")
    print(" █           de 30 passos em qualquer direção       █                                                    █")
    print(" █           para ajudar na sua reabilitação.       █         seu adversário anda duas casas.            █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")



    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █     Aproveite que o uma tentativa de impeachment   █")
    print(" █             Nada para ser feito aqui             █ contra você passou,Toda vitória deve ser comemorada█")
    print(" █                                                  █                                                    █")
    print(" █                     ▒▄█░▒█▀▀                     █                 ▒▄█░▒▄▀▀▄                          █")
    print(" █                     ░▒█░▒▀▀▄                     █                 ░▒█░▒█▄▄░                          █")
    print(" █                     ▒▄█▄▒▄▄▀                     █                 ▒▄█▄▒▀▄▄▀                          █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █   Encene um trecho de filme para todos da sala     █")
    print(" █             Espere sua próxima jogada            █             e avance 3 casas.                      █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")



    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █  Você recebe o presidente boliviano que te acursou █")
    print(" █             Nada para ser feito aqui             █  de golpista isso pega mal para seus partidários,  █")
    print(" █                                                  █                                                    █")
    print(" █                    ▒▄█░▒▀▀█                      █                  ▒▄█░▒▄▀▀▄                         █")
    print(" █                    ░▒█░░▒█░                      █                  ░▒█░▒▄▀▀▄                         █")
    print(" █                    ▒▄█▄▒▐▌░                      █                  ▒▄█▄▒▀▄▄▀                         █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █     você agora tem que ligar para uma pesssoa por  █")
    print(" █             Espere sua próxima jogada            █           whatssap até que ela atenda              █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █                                                    █")
    print(" █             Nada para ser feito aqui             █          Nada para ser feito aqui                  █")
    print(" █                                                  █                                                    █")
    print(" █                    ▒▄█░▒▄▀▀▄                     █                 ▒▄▀▄▒▄▀▀▄                          █")
    print(" █                    ░▒█░▒▀▄▄▀                     █                 ░▒▄▀▒█ ▒█                          █")
    print(" █                    ▒▄█▄▒▒▄▄▀                     █                 ▒█▄▄▒▀▄▄▀                          █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █                                                    █")
    print(" █             Espere sua próxima jogada            █          Espere sua próxima jogada                 █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █  Seus movimentos politicos chamaram a atenção da █    Maia afirma que vai rejeitar os 25 pedidos de   █")
    print(" █     OAB, não seja covarde,finja que está na      █   impeachment que existem contra você, pessa para  █")
    print(" █                                                  █ fazer um discurso chamando a atenção de todos onde █")
    print(" █                    ▒▄▀▄▒▄█░                      █                  ▒▄▀▄▒▄▀▄                          █")
    print(" █                    ░▒▄▀░▒█░                      █                  ░▒▄▀░▒▄▀                          █")
    print(" █                    ▒█▄▄▒▄█▄                      █                  ▒█▄▄▒█▄▄                          █")         
    print(" █                                                  █                                                    █")
    print(" █          balada e mostre como você               █     você se encontra, agradeça essa vitória        █")
    print(" █         faria para chegar em alguém.             █             e avance duas casas                    █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █   O DEM do Maia quer se aliar ao PSDB do Aécio,  █                                                    █")
    print(" █  cante uma canção de ninar para que o Maia durma █           Nada para ser feito aqui                 █")
    print(" █                                                  █                                                    █")
    print(" █                    ▒▄▀▄▒▄▀▀▄                     █                 ▒▄▀▄░▒▄▀█░                         █")
    print(" █                    ░▒▄▀░░▒▀▌                     █                 ░▒▄▀▒█▄▄█▄                         █")
    print(" █                    ▒█▄▄▒▀▄▄▀                     █                 ▒█▄▄░░░▒█░                         █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █                                                    █")
    print(" █   e você consiga manter sua coligação com o PSDB █           espere sua próxima jogada                █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")


    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █ Você escapa de uma investigação do STF, derrotando █")
    print(" █             Nada para ser feito aqui             █ o inimigo sem lutar; seu adversário terá que fazer █")
    print(" █                                                  █ quantas flexões                                    █")
    print(" █                    ▒▄▀▄▒█▀▀                      █                  ▒▄▀▄▒▄▀▀▄                         █")
    print(" █                    ░▒▄▀▒▀▀▄                      █                  ░▒▄▀▒█▄▄░                         █")
    print(" █                    ▒█▄▄▒▄▄▀                      █                  ▒█▄▄▒▀▄▄▀                         █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █                                                    █")
    print(" █             Espere sua próxima jogada            █   ele aguentar em 1 minuto e você avança 1 casas   █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █ Maia o acusa de tentar enfraquecer o DEM, troque o █")
    print(" █             Nada para ser feito aqui             █     status de relacionamento do Facebook, para     █")
    print(" █                                                  █            demonstrar sua lealdade,                █")
    print(" █                    ▒▄▀▄▒▀▀█                      █                  ▒▄▀▄▒▄▀▀▄                         █")
    print(" █                    ░▒▄▀░▒█░                      █                  ░▒▄▀▒▄▀▀▄                         █")
    print(" █                    ▒█▄▄▒▐▌░                      █                  ▒█▄▄▒▀▄▄▀                         █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █     senão seu adversário avançará duas casas,      █")
    print(" █             Espere sua próxima jogada            █           além das 3 que você voltará              █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █ O doleiro Lúcio Funaro afirmou em sua delação que█                                                    █")
    print(" █ você sabia do esquema na Caixa Econômica Federal,█         Nada para ser feito aqui,                  █")
    print(" █          sso enfraquece sua imgem politica,      █                                                    █")
    print(" █                    ▒▄▀▄▒▄▀▀▄                     █                ▒▄▀▀▄▒▄▀▀▄                          █")
    print(" █                    ░▒▄▀▒▀▄▄▀                     █                ░░▒▀▌▒█ ▒█                          █")
    print(" █                    ▒█▄▄▒▒▄▄▀                     █                ▒▀▄▄▀▒▀▄▄▀                          █")         
    print(" █                                                  █                                                    █")
    print(" █      você deve ficar sem olhar o celular         █                                                    █")
    print(" █              até o final do jogo                 █          espere sua próxima jogada                 █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █   A oposição faz nova tentativa falha no STF de  █                                                    █")
    print(" █   fatiar votação da denúncia contra você e seus  █           Nada para ser feito aqui,                █")
    print(" █        ministros,  validando sua autoridade;     █                                                    █")
    print(" █                   ▒▄▀▀▄▒▄█░                      █                 ▒▄▀▀▄▒▄▀▄                          █")
    print(" █                   ░░▒▀▌░▒█░                      █                 ░░▒▀▌░▒▄▀                          █")
    print(" █                   ▒▀▄▄▀▒▄█▄                      █                 ▒▀▄▄▀▒█▄▄                          █")         
    print(" █                                                  █                                                    █")
    print(" █   seu adversário deve postar uma foto feia dele  █                                                    █")
    print(" █ nas redes sociais,enquanto você anda duas casas. █          espere sua próxima jogada                 █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █A Procuradoria da República não obteve provas contra█")
    print(" █             Nada para ser feito aqui             █  você, mas deixou insubordinação na base aliada;   █")
    print(" █                                                  █  lembre do conselho:Quando incapaz finja-se capaz” █")
    print(" █                   ▒▄▀▀▄▒▄▀▀▄                     █                ▒▄▀▀▄░▒▄▀█░                         █")
    print(" █                   ░░▒▀▌░░▒▀▌                     █                ░░▒▀▌▒█▄▄█▄                         █")
    print(" █                   ▒▀▄▄▀▒▀▄▄▀                     █                ▒▀▄▄▀░░░▒█░                         █")         
    print(" █                                                  █      saia da sala e fassa um elogio                █")
    print(" █                                                  █       a uma pessoa desconhecida,                   █")
    print(" █             Espere sua próxima jogada            █          para demonstrar sua audácia               █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")



    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █                                                    █")
    print(" █             Nada para ser feito aqui,            █           Nada para ser feito aqui,                █")
    print(" █                                                  █                                                    █")
    print(" █                   ▒▄▀▀▄▒█▀▀                      █                 ▒▄▀▀▄▒▄▀▀▄                         █")
    print(" █                   ░░▒▀▌▒▀▀▄                      █                 ░░▒▀▌▒█▄▄░                         █")
    print(" █                   ▒▀▄▄▀▒▄▄▀                      █                 ▒▀▄▄▀▒▀▄▄▀                         █")         
    print(" █                                                  █                                                    █")
    print(" █                                                  █                                                    █")
    print(" █             Espere sua próxima jogada            █           Espere sua próxima jogada                █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")


    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █      Você articula e ajuda seu broder Aécio,     █                                                    █")
    print(" █    conseguindo votos no Senado para barrar o     █         Nada para ser feito aqui                   █")
    print(" █afastamento dele;está foi uma grande vitória para █                                                    █")
    print(" █                   ▒▄▀▀▄▒▀▀█                      █                 ▒▄▀▀▄▒▄▀▀▄                         █")
    print(" █                   ░░▒▀▌░▒█░                      █                 ░░▒▀▌▒▄▀▀▄                         █")
    print(" █                   ▒▀▄▄▀▒▐▌░                      █                 ▒▀▄▄▀▒▀▄▄▀                         █")         
    print(" █   sua aliança politica entre seu partido (PSDB)  █                                                    █")
    print(" █  e o dele(PMDB) escolha um desafio que você já   █                                                    █")
    print(" █   cumprido e seu adversário deverá faze-lo       █          Espere sua próxima jogada                 █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █ A dívida pública avança 3,22% em junho desse ano,  █")
    print(" █             Nada para ser feito aqui             █sendo de R$ 3,35 trilhões;esse cenário econômico    █")
    print(" █                                                  █prejudica sua imagem,pensando que sua postura deve  █")
    print(" █                   ▒▄▀▀▄▒▄▀▀▄                     █ser como a água  ░▒▄▀█░▒▄▀▀▄                        █")
    print(" █                   ░░▒▀▌▒▀▄▄▀                     █que não tem      ▒█▄▄█▄▒█ ▒█                        █")
    print(" █                   ▒▀▄▄▀▒▒▄▄▀                     █forma constante, ░░░▒█░ ▀▄▄▀                        █")         
    print(" █                                                  █simule uma pedido de casamento para alguém que não  █")
    print(" █                                                  █seja seu adversário, demonstrando sua flexibilidade,█")
    print(" █             Espere sua próxima jogada            █            com isso avançará 4 casas               █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █A reforma da previdência que você colocou em pauta  █")
    print(" █             Nada para ser feito aqui             █foi aprovada, tendo em mente o pensamento “O gover- █")
    print(" █                                                  █nante esclarecido estabeleceplanos a seguir”.       █")
    print(" █                  ░▒▄▀█░▒▄█░                      █                ░▒▄▀█░▒▄▀▄                          █")
    print(" █                  ▒█▄▄█▄░▒█░                      █                ▒█▄▄█▄░▒▄▀                          █")
    print(" █                  ░░░▒█░▒▄█▄                      █                ░░░▒█░▒█▄▄                          █")         
    print(" █                                                  █  Passe uma rodada falando com algum sotaque ou em  █")
    print(" █                                                  █                                                    █")
    print(" █             Espere sua próxima jogada            █               outro idioma.                        █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")

    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █O TCU quer explicações suas sobre o 'esquema dos  █                                                    █")
    print(" █portos', onde a empresa do seu amigo explora dês- █          Nada para ser feito aqui                  █")
    print(" █de 1998, sendo os últimos 3 anos sem contrato     █                                                    █")
    print(" █                  ░▒▄▀█░▒▄▀▀▄                     █               ░▒▄▀█░░▒▄▀█░                         █")
    print(" █                  ▒█▄▄█▄░░▒▀▌                     █               ▒█▄▄█▄▒█▄▄█▄                         █")
    print(" █                  ░░░▒█░▒▀▄▄▀                     █               ░░░▒█░░░░▒█░                         █")         
    print(" █    seja sútil, para não chamar a atenção dos     █                                                    █")
    print(" █   jornalistas fique sem usar a palavra (não)     █                                                    █")
    print(" █         até o final do jogo.                     █          Espere sua próxima jogada                 █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")



    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █      Você por meio de seus advogados, partiu     █                                                    █")
    print(" █   para um ataque sem precedentes contra o ex-    █           Nada para ser feito aqui,                █")
    print(" █  procurador-geral da República Rodrigo Janot,    █                                                    █")
    print(" █                  ░▒▄▀█░▒█▀▀                      █                ░▒▄▀█░▒▄▀▀▄                         █")
    print(" █                  ▒█▄▄█▄▒▀▀▄                      █                ▒█▄▄█▄▒█▄▄░                         █")
    print(" █                  ░░░▒█░▒▄▄▀                      █                ░░░▒█░▒▀▄▄▀                         █")         
    print(" █  com isso ganha poder sobre seu adversário e ele █                                                    █")
    print(" █     deverá se desculpar na frente de todos       █                                                    █")
    print(" █             da sala de aula                      █           espere sua próxima jogada                █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")



    print("                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("                            █Você foi denunciado pela WikiLeaks como informante█")
    print("                            █   da embaixada Americana no Brasil, invente uma  █")
    print("                            █           poesia que rime como a frase           █")
    print("                            █                  ░▒▄▀█░▒▀▀█                      █")
    print("                            █                  ▒█▄▄█▄░▒█░                      █")
    print("                            █                  ░░░▒█░▒▐▌░                      █")         
    print("                            █        'Tá tranquilo, Tio Sam, tá, tá...'        █")
    print("                            █            enquanto isso volte 8 casas           █")
    print("                            █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")



    print("                                                  ░█▌")
    print("                                                  ░█▌")
    print("                                                █░█░█ █▌")
    print("                                                 ░█▌░█")
    print("                                                  ░█▌")


    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                                                                       █")
    print(" █                                                                                                       █")
    print(" █                               ░▐█▀▀░▐██▒██▄░▒█▌─░▄█▀▄─▒██░░░                                          █")
    print(" █                               ░▐█▀▀─░█▌▒▐█▒█▒█░░▐█▄▄▐█▒██░░░                                          █")
    print(" █                               ░▐█──░▐██▒██░▒██▌░▐█─░▐█▒██▄▄█                                          █")
    print(" █                                                                                                       █")         
    print(" █                                                                                                       █")
    print(" █                                                                                                       █")
    print(" █                                                                                                       █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    input("             PRONTO PARA CONTINUAR...PRESSIONE ENTER")













#-------------------------------------------------REGRAS---------------------------------------------------
print("\n\n")
print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")       
regras = str.upper(input('             DESEJA LER AS REGRAS? (sim) ou (não) :'))
print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")       
print("\n\n")


while regras != 'SIM' and regras != 'NÃO' and regras != 'NAO':
    regras = str.upper(input('DESEJA LER AS REGRAS? (sim) ou (não) :'))

if regras == 'SIM':
    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print(" █                                                  █")
    print(" █                                                  █")
    print(" █     ▒▐█▀▀▄░▐█▀▀░▐█▀▀▀─▒▐█▀▀▄─░▄█▀▄─▒▄█▀▀█        █")
    print(" █     ▒▐█▒▐█░▐█▀▀░▐█░▀█▌▒▐█▒▐█░▐█▄▄▐█▒▀▀█▄▄        █")
    print(" █     ▒▐█▀▄▄░▐█▄▄░▐██▄█▌▒▐█▀▄▄░▐█─░▐█▒█▄▄█▀        █")   
    print(" █                                                  █")
    print(" █                                                  █")
    print(" █     █ PARA CADA DESAFIO NÃO FEITO, VOCÊ RETORNA- █")
    print(" █       RÁ TRÊS CASAS.                             █")
    print(" █                                                  █")
    print(" █                                                  █")
    print(" █     █ VOCÊ TEM 1 MINUTO PARA COMEÇAR O DESAFIO,  █")
    print(" █       CASO NÃO SEJA FEITO, SERÁ DECLARADO COMO   █")
    print(" █       DESISTÊNCIA.                               █")
    print(" █                                                  █")
    print(" █     █ SE VOCÊ CAIR EM UMA CASA QUE AVANCE SUA    █")
    print(" █       POSIÇÃO E CAIR EM UM DESAFIO, ESSE DESAFIO █")
    print(" █       SERÁ ANULADO.                              █")
    print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n\n")
    input("PRONTO PARA CONTINUAR...PRECIONE ENTER")
print("\n\n\n\n\n\n\n")
#-------------------------------------------------Nome dos jogadores---------------------------------------------------
print("╔═══════════════════════════════════════╗")
print("║     Nome do primeiro jogador:         ║")
print("║═══════════════════════════════════════║")
print("║     ████▀░░░░░░░░░░░░░░░░░▀████       ║")
print("║     ███│░░░░░░░░░░░░░░░░░░░│███       ║")
print("║     ██▌│░░░░░░░░░░░░░░░░░░░│▐██       ║")
print("║     ██░└┐░░░░░░░░░░░░░░░░░┌┘░██       ║")
print("║     ██░░└┐░░░░░░░░░░░░░░░┌┘░░██       ║")
print("║     ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██       ║")
print("║     ██▌░│██████▌░░░▐██████│░▐██       ║")
print("║     ███░│▐███▀▀░░▄░░▀▀███▌│░███       ║")
print("║     ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██       ║")
print("║     ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██       ║")
print("║     ████▄─┘██▌░░░░░░░▐██└─▄████       ║")
print("║     █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████       ║")
print("║     ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████       ║")
print("║     █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████       ║")
print("║     ███████▄░░░░░░░░░░░▄███████       ║")                                                
print("║                                       ║")                                                                                     
print("╚═══════════════════════════════════════╝")
print("     ░▐█▀▀▒██▄░▒█▌▒█▀█▀█░▐█▀▀▒▐█▀▀▄")
print("     ░▐█▀▀▒▐█▒█▒█░░░▒█░░░▐█▀▀▒▐█▒▐█")
print("     ░▐█▄▄▒██░▒██▌░▒▄█▄░░▐█▄▄▒▐█▀▄▄║")
nome_jogador1 = input()
print("\n\n\n\n\n\n\n")
print("╔═══════════════════════════════════════╗")
print("║     Nome do segundo jogador:          ║")
print("║═══════════════════════════════════════║")
print("║     ████▀░░░░░░░░░░░░░░░░░▀████       ║")
print("║     ███│░░░░░░░░░░░░░░░░░░░│███       ║")
print("║     ██▌│░░░░░░░░░░░░░░░░░░░│▐██       ║")
print("║     ██░└┐░░░░░░░░░░░░░░░░░┌┘░██       ║")
print("║     ██░░└┐░░░░░░░░░░░░░░░┌┘░░██       ║")
print("║     ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██       ║")
print("║     ██▌░│██████▌░░░▐██████│░▐██       ║")
print("║     ███░│▐███▀▀░░▄░░▀▀███▌│░███       ║")
print("║     ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██       ║")
print("║     ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██       ║")
print("║     ████▄─┘██▌░░░░░░░▐██└─▄████       ║")
print("║     █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████       ║")
print("║     ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████       ║")
print("║     █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████       ║")
print("║     ███████▄░░░░░░░░░░░▄███████       ║")                                                
print("║                                       ║")                                                                                     
print("╚═══════════════════════════════════════╝")
print("     ░▐█▀▀▒██▄░▒█▌▒█▀█▀█░▐█▀▀▒▐█▀▀▄")
print("     ░▐█▀▀▒▐█▒█▒█░░░▒█░░░▐█▀▀▒▐█▒▐█")
print("     ░▐█▄▄▒██░▒██▌░▒▄█▄░░▐█▄▄▒▐█▀▄▄║")
nome_jogador2 = input()
print("\n\n\n\n\n\n\n")


# --------------------------------------------------História-----------------------------------------------------------


print("            ░▐█▀▄─░▐█▀▀▒▐██▄▒▄██▌     ▒▐▌▒▐▌░▐██▒██▄░▒█▌░▐█▀█▄▒▐█▀▀█▌")
print("            ░▐█▀▀▄░▐█▀▀░▒█░▒█░▒█░     ░▒█▒█░─░█▌▒▐█▒█▒█░░▐█▌▐█▒▐█▄▒█▌")
print("            ░▐█▄▄▀░▐█▄▄▒▐█░░░░▒█▌     ░▒▀▄▀░░▐██▒██░▒██▌░▐█▄█▀▒▐██▄█▌\n")


print("                      ─░▄█▀▄─     ░▐██▒██░░░░▐█░▐█─░▄█▀▄─")
print("                      ░▐█▄▄▐█     ─░█▌▒██░░░░▐████░▐█▄▄▐█")
print("                      ░▐█─░▐█     ░▐██▒██▄▄█░▐█░▐█░▐█─░▐█")
time.sleep(3)
print("\n\n\n\n\n\n\n")

print("    {}, após o navio ter lhe resgatado, os tripulantes te dão comida,\n".format(nome_jogador1))
time.sleep(4)
print("     roupas e cuidam de seus machucados, sentindo-se aliviado, após a prova \n")
time.sleep(4)
print("     de sobrevivência que passou. Você sente-se seguro e descança profundamente...\n")
time.sleep(4)
print("       Você não sabe para onde está sendo levado e as pessoas que te \n")
time.sleep(4)
print("     resgataram falam em um u...\n")
time.sleep(4)
print("        Depois de dias navegando em um rio com kilometros de distância entre uma \n")
time.sleep(4)
print("     margem e a outra, você desenbarca em um pequeno povoado... \n")
time.sleep(4)
print("        Lá você ouve falar que está sendo levado a uma fazenda, para trabalhar e\n")
time.sleep(4)
print("     pagar pelo que recebeu....\n")
time.sleep(3)
print("        Já está escurecendo e uma camionete vem buscar você e os outros tirpulantes, \n")
time.sleep(4)
print("        você resiste e diz que quer telefonar para sua familia e eles lhe amarram \n")
print("     com cordas no fundo do carro e o 'Pau-de-arara' começa a se mexer\n")
time.sleep(4)
print("        Você consegue afrouxar as cordas e sem que niguém perceba, você se joga\n")
time.sleep(4)
print("     do carro em movimento.\n")
time.sleep(4)
print("        Após uma boa parte da noite caminhando pela beira da estrada,\n")
time.sleep(4)
print("     você decide descansar um pouco antes que o dia amanheça...\n")
time.sleep(1)
print("                            Derrepente!\n")
time.sleep(1)
print("          Você acorda com latidos e vozes...e percebe que eles estão se aproximando e\n")
time.sleep(2)
print("      logo você começa a correr...\n")
time.sleep(4)
print("        Cães lhe perseguem... ofegante, você se esconde atrás de uma árvore...\n")
time.sleep(4)
print("      logo que os cães passam, um sentimento de alívio bate em seu peito,\n")
time.sleep(4)
print("      no entanto, quando começa a entrar na floresta para ficar em segurança,\n")
time.sleep(4)
print("      um tipo de dardo crava seu pescoço, você sente o chão desaparecer entre os\n")
time.sleep(4)
print("      seus pés e cai já no escuro.\n")
time.sleep(2)
print("        Quando acorda, vê que está estirado em uma cama de um hotel em Brasília.\n")
time.sleep(4)
print("        Um celular em cima do criado mudo ao seu lado toca.\n")
time.sleep(4)
print("        Você atende...A pessoa no outro lado da linha é o seu principal adversário político.\n")
time.sleep(4)
print("        Cujo nome é {}".format(nome_jogador2))
time.sleep(4)
print("        Ele diz que é seu primeiro dia na Câmara dos Deputados e lhe deseja boa sorte,.\n")
time.sleep(4)
print("       porque você vai precisar..!,.\n")
time.sleep(4)
print("        Você então se dá conta de que agora é um político em ascensão.\n")
time.sleep(4)
print("        Sua tarefa é derrotar seu adversário político e consolidar sua carreira política\n")
time.sleep(4)
print("      no atual e assombroso cenário político brasileiro.\n")
time.sleep(4)
print("       A cada rodada, você tomara decisões difíceis, e enfrentará desafios comprometedores,\n")
time.sleep(4)
print("      tudo em nome da democracia !\n")
time.sleep(4)


#----------------------------------------------------Variáveis-----------------------------------------------------------

posicao_jogador1 = 0
posicao_jogador2 = 0
cont = 0
desafio_feito = 0
#===================================================JOGO================================================================

while posicao_jogador1 <= 47 and posicao_jogador2 <= 47:

    # ------------------------------------------------------Jogador 1--------------------------------------------------------
    input("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n"
          "                  {}, AGORA É SUA VEZ! \n APERTE ENTER PARA JOGAR O DADO!           \n"
          "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n".format(nome_jogador1))
    cont += 1
    dado = random.randint(1, 6)
    print("O DADO QUE CAIU FOI:\n")
    if dado == 1:
        
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█       █▒▒▒▒░")
        print("█   ░   █▒▒░░░")
        print("█   █   █▒▒░░▒")
        print("█       █▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 2:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█     █░█▒▒▒▒░")
        print("█       █▒▒░░░")
        print("█       █▒▒░░▒")
        print("█ █░    █▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 3:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█     █░█▒▒▒▒░")
        print("█   ▄   █▒▒░░░")
        print("█   ▀░  █▒▒░░▒")
        print("█ █░    █▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 4:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█ ░   ░ █▒▒▒▒░")
        print("█ █   █ █▒▒░░░")
        print("█       █▒▒░░▒")
        print("█ █░  █░█▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 5:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█ ░   ░ █▒▒▒▒░")
        print("█ █ ░ █ █▒▒░░░")
        print("█   █   █▒▒░░▒")
        print("█ █░  █░█▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 6:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█ █░  █░█▒▒▒▒░")
        print("█ ▄   ▄ █▒▒░░░")
        print("█ ▀   ▀ █▒▒░░▒")
        print("█ █░  █░█▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    print("\n\n")    
        
        
    
    posicao_jogador1 += dado
    #-----------------------------------------------------CASA 1------------------------------------------------------------------

    if posicao_jogador1 == 0:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                                                                       █")
        print(" █                                                                                                       █")
        print(" █                                                                                                       █")
        print(" █                                                                                                       █")
        print(" █                                 ░▐██▒██▄░▒█▌░▐██░▐█▀█░▐██▒▐█▀▀█▌                                      █")
        print(" █                                 ─░█▌▒▐█▒█▒█░─░█▌░▐█───░█▌▒▐█▄▒█▌                                      █")         
        print(" █                                 ░▐██▒██░▒██▌░▐██░▐█▄█░▐██▒▐██▄█▌                                      █")
        print(" █                                                                                                       █")
        print(" █                                                                                                       █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    if posicao_jogador1 == 1:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                      ▒▄█░                        █")
        print(" █                      ░▒█░                        █")
        print(" █                      ▒▄█▄                        █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █            Espere sua próxima jogada             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░\n\n")




    # -----------------------------------------------------CASA 2------------------------------------------------------------------
    if posicao_jogador1 == 2:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █     Você deve seguir o conselho do Pensador        █")
        print(" █                                                    █")
        print(" █                      ▒▄▀▄                          █")
        print(" █                      ░▒▄▀                          █")
        print(" █                      ▒█▄▄                          █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █          tente lamber o seu cotovelo               █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))

        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")






            # -----------------------------------------------------CASA 3------------------------------------------------------------------
    elif posicao_jogador1 == 3:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █       Você cruzou o caminho do Sérgio Moro       █")
        print(" █              volte ao início do jogo             █")
        print(" █                      ▒▄▀▀▄                       █")
        print(" █                      ░░▒▀▌                       █")
        print(" █                      ▒▀▄▄▀                       █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █              volte ao início do jogo             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        posicao_jogador1 = 0
        print("         ░░░░░░░░███████████████░░░░░░░░")
        print("         ░░░░░█████████████████████░░░░░")
        print("         ░░░░████████████████████████░░░")
        print("         ░░░██████████████████████████░░")
        print("         ░░█████████████████████████████")
        print("         ░░███████████▀░░░░░░░░░████████")
        print("         ░░███████████░░░░░░░░░░░░░░░███")
        print("         ░████████████░░░░░░░░░░░░░░░░██")
        print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
        print("         █░░░░█████░░░░░░▄███████░░██░░█")
        print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
        print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
        print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
        print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
        print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
        print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
        print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
        print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
        print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
        print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
        print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
        print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
        print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
        print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
        print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")




    # -----------------------------------------------------CASA 4------------------------------------------------------------------
    elif posicao_jogador1 == 4:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █              Nada para ser feito aqui              █")
        print(" █                                                    █")
        print(" █                       ░▒▄▀█░                       █")
        print(" █                       ▒█▄▄█▄                       █")
        print(" █                       ░░░▒█░                       █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █              Espere sua próxima jogada             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░\n\n")





    # -----------------------------------------------------CASA 5------------------------------------------------------------------
    elif posicao_jogador1 == 5:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █             Você encontrou informações           █")
        print(" █             cruciais de seu adversário e         █")
        print(" █                                                  █")
        print(" █                        ▒█▀▀                      █")
        print(" █                        ▒▀▀▄                      █")
        print(" █                        ▒▄▄▀                      █")         
        print(" █                                                  █")
        print(" █          ele deve dançar uma música de sua       █")
        print(" █                      escolha.                    █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            print("Seu adversário voltou 3 casas, por não ter cumprido o desafio")
            posicao_jogador2 -= 3
        else:
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")




            # ----------------------------------------------------CASA 6-------------------------------------------------------------------
    elif posicao_jogador1 == 6:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █      Você extingue uma reserva na Amazônia para    █")
        print(" █                 ampliar exploração,                █")
        print(" █                      ▒▄▀▀▄                         █")
        print(" █                     ░▒█▄▄░                         █")
        print(" █                      ▒▀▄▄▀                         █")         
        print(" █                                                    █")
        print(" █               imite uma motossera                  █")
        print(" █        por 10 segundos e avance duas casas.        █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n\n")


        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            posicao_jogador1 += 2
            print("          ─────────────────────────▐█")
            print("          ────▄──────────────────▄█▓█")
            print("          ───▐██▄───────────────▄▓░░▓▓")
            print("          ───▐█░██▓────────────▓▓░░░▓▌")
            print("          ───▐█▌░▓██──────────█▓░░░░▓")
            print("          ────▓█▌░░▓█▄███████▄███▓░▓█")
            print("          ────▓██▌░▓██░░░░░░░░░░▓█░▓▌")
            print("          ─────▓█████░░░░░░░░░░░░▓██")
            print("          ─────▓██▓░░░░░░░░░░░░░░░▓█")
            print("          ─────▐█▓░░░░░░█▓░░▓█░░░░▓█▌")
            print("          ─────▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌")
            print("          ─────▓▓░▓██████▓░▓███▓▓▌░█▓")
            print("          ────▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██")
            print("          ────▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌")
            print("          ────▓█▌░▓█████▓░░░▓███▓▀░▓█▓")
            print("          ───▐▓█░░░▀▓██▀░░░░░─▀▓▀░░▓█▓")
            print("          ───▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓")
            print("          ───▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌")
            print("          ───▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓")
            print("          ──▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░██▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓")
            print("          ──██░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ──█▌░░░░░░░░░░░░░░░░░░░░░░░░▐▓▌")
            print("          ─▐▓░░░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ▐█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\n")





            # -----------------------------------------------------CASA 7------------------------------------------------------------------            
    elif posicao_jogador1 == 7:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █  Você está sendo investigado por inquérito, faça █")
        print(" █  uma imitação de algum famoso, para treinar sua  █")
        print(" █     expressãodiante do juiz, caso contrário,     █")
        print(" █                        ▒▀▀█                      █")
        print(" █                        ░▒█░                      █")
        print(" █                        ▒▐▌░                      █")         
        print(" █                                                  █")
        print(" █                 seu adversário                   █")
        print(" █        avançará duas casas e você voltará 3      █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            posicao_jogador2 += 2
            print(
                "Você voltou 3 casas e seu inimigo avançou 3, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")            




            # -----------------------------------------------------CASA 8-------------------------------------------------------------------
    elif posicao_jogador1 == 8:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █            Nada para ser feito aqui                █")
        print(" █                                                    █")
        print(" █                      ▒▄▀▀▄                         █")
        print(" █                      ▒▄▀▀▄                         █")
        print(" █                      ▒▀▄▄▀                         █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █            Espere sua próxima jogada               █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")



    # -----------------------------------------------------CASA 9------------------------------------------------------------------
    elif posicao_jogador1 == 9:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ Você está sendo investigado, mas conseguiu apoio █")
        print(" █trocando alguns votos por leis mais brandas       █")
        print(" █ao trabalho análogo ao escravos, toda vitória tem █")
        print(" █que ser comemorada!     ▒▄▀▀▄                     █")
        print(" █escolha uma música para ▒▀▄▄▀                     █")
        print(" █seu adversário cantar   ▒▒▄▄▀                     █")         
        print(" █até o final sem errar. Se ele acertar ele avança  █")
        print(" █uma casa e você retornará 3, caso contrário ele   █")
        print(" █pagará o pato(pizza).                             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("Seu adversário conseguiu realizar o desafio com sucesso? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("Seu adversário conseguiu realizar o desafio com sucesso? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            posicao_jogador1 += 1
            print("Seu adversário voltou 3 casas, por não ter cumprido o desafio e você avançou 1")
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 
        else:
            posicao_jogador1 -= 3
            posicao_jogador2 += 1
            print("Você voltou 3 casas, por não ter cumprido o desafio e ele avançou 1\n")
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")





            # -----------------------------------------------------CASA 10------------------------------------------------------------------              
    elif posicao_jogador1 == 10:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █              Nada para ser feito aqui              █")
        print(" █                                                    █")
        print(" █                     ▒▄█░▒ ▄▀▀▄                     █")
        print(" █                     ░▒█░▒▒█ ▒█                     █")
        print(" █                     ▒▄█▄▒▒▀▄▄▀                     █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █              espere sua próxima jogada             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")





    # -----------------------------------------------------CASA 11------------------------------------------------------------------              
    elif posicao_jogador1 == 11:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █   É divulgada a Lista Suja do Trabalho Escravo,  █")
        print(" █    isso é péssimo para sua campanha. passe essa  █")
        print(" █                                                  █")
        print(" █                    ▒▄█░▒▄█░▒                     █")
        print(" █                    ░▒█░░▒█░▒                     █")
        print(" █                    ▒▄█▄▒▄█▄▒                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █   rodada com os olhos fechados e volte 5 casas.  █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio vai ser realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 8
            print("Você voltou 8 casas, por não ter cumprido o desafio")
        else:
            posicao_jogador1 -= 5
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")





            # ------------------------------------------------------CASA 12-----------------------------------------------------------------
    elif posicao_jogador1 == 12:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █              Nada para ser feito aqui              █")
        print(" █                                                    █")
        print(" █                     ▒▄█░▒▒▄▀▄                      █")
        print(" █                     ░▒█░░▒ ▄▀▒                     █")
        print(" █                     ▒▄█▄▒▒█▄▄                      █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █            Espere sua próxima jogada               █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")




    # -----------------------------------------------------CASA 13------------------------------------------------------------------
    elif posicao_jogador1 == 13:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █    Você passa dois dias internado no hospital,   █")
        print(" █                                                  █")
        print(" █                     ▒▄█░▒▄▀▀▄                    █")
        print(" █                     ░▒█░░░▒▀▌                    █")
        print(" █                     ▒▄█▄▒▀▄▄▀                    █")         
        print(" █                                                  █")
        print(" █           de 30 passos em qualquer direção       █")
        print(" █           para ajudar na sua reabilitação.       █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("          ─────────────────────────▐█")
            print("          ────▄──────────────────▄█▓█")
            print("          ───▐██▄───────────────▄▓░░▓▓")
            print("          ───▐█░██▓────────────▓▓░░░▓▌")
            print("          ───▐█▌░▓██──────────█▓░░░░▓")
            print("          ────▓█▌░░▓█▄███████▄███▓░▓█")
            print("          ────▓██▌░▓██░░░░░░░░░░▓█░▓▌")
            print("          ─────▓█████░░░░░░░░░░░░▓██")
            print("          ─────▓██▓░░░░░░░░░░░░░░░▓█")
            print("          ─────▐█▓░░░░░░█▓░░▓█░░░░▓█▌")
            print("          ─────▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌")
            print("          ─────▓▓░▓██████▓░▓███▓▓▌░█▓")
            print("          ────▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██")
            print("          ────▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌")
            print("          ────▓█▌░▓█████▓░░░▓███▓▀░▓█▓")
            print("          ───▐▓█░░░▀▓██▀░░░░░─▀▓▀░░▓█▓")
            print("          ───▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓")
            print("          ───▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌")
            print("          ───▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓")
            print("          ──▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░██▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓")
            print("          ──██░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ──█▌░░░░░░░░░░░░░░░░░░░░░░░░▐▓▌")
            print("          ─▐▓░░░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ▐█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\n")





            # -----------------------------------------------------CASA 14------------------------------------------------------------------
    elif posicao_jogador1 == 14:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █     Você passa por um processo de impeachment,     █")
        print(" █ escolha alguém para dançar valsa e dançem enquanto █")
        print(" █                                                    █")
        print(" █                   ▒▄█░░▒▄▀█░                       █")
        print(" █                   ░▒█░▒█▄▄█▄                       █")
        print(" █                   ▒▄█▄▒░░░█░                       █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █         seu adversário anda duas casas.            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        posicao_jogador2 += 2
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("     ░░░░░░░░░░▄▄█▀▀▀▀▀▀▀▀█▄▄░░░░░░░░")
            print("     ░░░░░░░▄▄▀▀░░░░░░░░░░░░▀▀▄▄░░░░░")
            print("     ░░░░░▄█▀░░░░▄▀░░░░▄░░░░░░░▀█░░░░")
            print("     ░░░░██▄▄████░░░░░░▀▄░░░░░░░░█▄░░")
            print("     ░░▄████▀███▄▀▄░░░░░░███▄▄▄▄░░█░░")
            print("     ░▄█████▄████░██░░░▄███▄▄░▀█▀░░█░")
            print("     ▄███████▀▀░█░▄█░▄███▀█████░█░░▀▄")
            print("     █░█▀██▄▄▄▄█▀░█▀█▀██████▀░██▀█░░█")
            print("     █░█░▀▀▀▀▀░░░█▀░█░███▀▀░░▄█▀░█░░█")
            print("     █░░█▄░░░░▄▄▀░░░█░▀██▄▄▄██▀░░█▄░█")
            print("     █░░░░▀█▀▀▀░░░░░░█░░▀▀▀▀░░░░▄█░░█")
            print("     █░░░░░░░░░░░░░░░░▀▄░░░░░░▄█▀░░░█")
            print("     ░█░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▄░░░░█░")
            print("     ░░█░░░░░░▄▄▄▄▄▄▄░░░░░░░░░░░░░▄▀░")
            print("     ░░░▀▄░░░░░▀█▄░░░▀▀██▄░░░░░░░▄▀░░")
            print("     ░░░░░▀▄▄░░░░░▀▀▀▀▀░░░░░░░░▄▀░░░░")
            print("     ░░░░░░░░▀▀▄▄▄░░░░░░░░▄▄▄▀▀█░░░░░")
            print("     ░░░░░░░░░░▄▀▀█████▀▀▀▀░░░░██░░░░")
            print("     ░░░░░░░░░█░░░██░░░█▀▀▀▀▀▀▀▀█░░░░")





            # -----------------------------------------------------CASA 15----------------------------------------------------------------
    elif posicao_jogador1 == 15:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                     ▒▄█░▒█▀▀                     █")
        print(" █                     ░▒█░▒▀▀▄                     █")
        print(" █                     ▒▄█▄▒▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")








    # -----------------------------------------------------CASA 16------------------------------------------------------------------              
    elif posicao_jogador1 == 16:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █     Aproveite que o uma tentativa de impeachment   █")
        print(" █       contra você passou, e pensando que           █")
        print(" █        toda vitória deve ser comemorada            █")
        print(" █                    ▒▄█░▒▄▀▀▄                       █")
        print(" █                    ░▒█░▒█▄▄░                       █")
        print(" █                    ▒▄█▄▒▀▄▄▀                       █")         
        print(" █                                                    █")
        print(" █   Encene um trecho de filme para todos da sala     █")
        print(" █             e avance 3 casas.                      █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")
            
        else:
            posicao_jogador1 += 3
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")            






            # ------------------------------------------------------CASA 17----------------------------------------------------------------
    elif posicao_jogador1 == 17:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                    ▒▄█░▒▀▀█                      █")
        print(" █                    ░▒█░░▒█░                      █")
        print(" █                    ▒▄█▄▒▐▌░                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")








    # -----------------------------------------------------CASA 18------------------------------------------------------------------              
    elif posicao_jogador1 == 18:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █  Você recebe o presidente boliviano que te acursou █")
        print(" █  de golpista isso pega mal para seus partidários,  █")
        print(" █                                                    █")
        print(" █                     ▒▄█░▒▄▀▀▄                      █")
        print(" █                     ░▒█░▒▄▀▀▄                      █")
        print(" █                     ▒▄█▄▒▀▄▄▀                      █")         
        print(" █                                                    █")
        print(" █     você agora tem que ligar para uma pesssoa por  █")
        print(" █           whatssap até que ela atenda.             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 






            # ------------------------------------------------------CASA 19-----------------------------------------------------------------
    elif posicao_jogador1 == 19:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                    ▒▄█░▒▄▀▀▄                     █")
        print(" █                    ░▒█░▒▀▄▄▀                     █")
        print(" █                    ▒▄█▄▒▒▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")





    # -----------------------------------------------------CASA 20------------------------------------------------------------------
    elif posicao_jogador1 == 20:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █          Nada para ser feito aqui                  █")
        print(" █                                                    █")
        print(" █                    ▒▄▀▄▒▄▀▀▄                       █")
        print(" █                    ░▒▄▀▒█ ▒█                       █")
        print(" █                    ▒█▄▄▒▀▄▄▀                       █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █          Espere sua próxima jogada                 █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")




    # -----------------------------------------------------CASA 21------------------------------------------------------------------
    elif posicao_jogador1 == 21:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █  Seus movimentos politicos chamaram a atenção da █")
        print(" █     OAB, não seja covarde,finja que está na      █")
        print(" █                                                  █")
        print(" █                    ▒▄▀▄▒▄█░                      █")
        print(" █                    ░▒▄▀░▒█░                      █")
        print(" █                    ▒█▄▄▒▄█▄                      █")         
        print(" █                                                  █")
        print(" █          balada e mostre como você               █")
        print(" █         faria para chegar em alguém.             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio\n")
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 





            # ------------------------------------------------------CASA 22-----------------------------------------------------------------
    elif posicao_jogador1 == 22:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █  Maia afirma que vai rejeitar os 25 pedidos de     █")
        print(" █   impeachment que existem contra você, pessa para  █")
        print(" █ fazer um discurso chamando a atenção de todos onde █")
        print(" █                    ▒▄▀▄▒▄▀▄                        █")
        print(" █                    ░▒▄▀░▒▄▀                        █")
        print(" █                    ▒█▄▄▒█▄▄                        █")         
        print(" █                                                    █")
        print(" █     você se encontra, agradeça essa vitória        █")
        print(" █             e avance duas casas                    █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa\n")
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")
        else:
            posicao_jogador1 += 2
            print("Você avançou 2 casas, por ter cumprido o desafio\n")
            
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 





            # -------------------------------------------------------CASA 23----------------------------------------------------------------
    elif posicao_jogador1 == 23:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █   O DEM do Maia quer se aliar ao PSDB do Aécio,  █")
        print(" █  cante uma canção de ninar para que o Maia durma █")
        print(" █                                                  █")
        print(" █                    ▒▄▀▄▒▄▀▀▄                     █")
        print(" █                    ░▒▄▀░░▒▀▌                     █")
        print(" █                    ▒█▄▄▒▀▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █   e você consiga manter sua coligação com o PSDB █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 



            # -------------------------------------------------------CASA 24----------------------------------------------------------------
    elif posicao_jogador1 == 24:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █           Nada para ser feito aqui                 █")
        print(" █                                                    █")
        print(" █                    ▒▄▀▄░▒▄▀█░                      █")
        print(" █                    ░▒▄▀▒█▄▄█▄                      █")
        print(" █                    ▒█▄▄░░░▒█░                      █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █           espere sua próxima jogada                █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")





    # --------------------------------------------------------CASA 25------------------------------------------------------------------
    elif posicao_jogador1 == 25:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                    ▒▄▀▄▒█▀▀                      █")
        print(" █                    ░▒▄▀▒▀▀▄                      █")
        print(" █                    ▒█▄▄▒▄▄▀                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")



    # -----------------------------------------------------CASA 26------------------------------------------------------------------
    elif posicao_jogador1 == 26:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ Você escapa de uma investigação do STF, derrotando █")
        print(" █ o inimigo sem lutar; seu adversário terá que fazer █")
        print(" █ quantas flexões                                    █")
        print(" █                  ▒▄▀▄▒▄▀▀▄                         █")
        print(" █                  ░▒▄▀▒█▄▄░                         █")
        print(" █                  ▒█▄▄▒▀▄▄▀                         █")         
        print(" █                                                    █")
        print(" █   ele aguentar em 1 minuto e você avança 1 casas,  █")
        print(" █    se ele não fizer, voltará tres                  █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        posicao_jogador2 += 1

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")             





            # -------------------------------------------------------CASA 27----------------------------------------------------------------
    elif posicao_jogador1 == 27:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                    ▒▄▀▄▒▀▀█                      █")
        print(" █                    ░▒▄▀░▒█░                      █")
        print(" █                    ▒█▄▄▒▐▌░                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")





    # -------------------------------------------------------CASA 28------------------------------------------------------------------
    elif posicao_jogador1 == 28:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ Maia o acusa de tentar enfraquecer o DEM, troque o █")
        print(" █     status de relacionamento do Facebook, para     █")
        print(" █            demonstrar sua lealdade,                █")
        print(" █                    ▒▄▀▄▒▄▀▀▄                       █")
        print(" █                    ░▒▄▀▒▄▀▀▄                       █")
        print(" █                    ▒█▄▄▒▀▄▄▀                       █")         
        print(" █                                                    █")
        print(" █     senão seu adversário avançará duas casas,      █")
        print(" █           além das 3 que você voltará.             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            posicao_jogador2 += 2
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 
    
    
    
    
    
                # --------------------------------------------------------CASA 29---------------------------------------------------------------
    elif posicao_jogador1 == 29:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ O doleiro Lúcio Funaro afirmou em sua delação que█")
        print(" █ você sabia do esquema na Caixa Econômica Federal,█")
        print(" █          isso enfraquece sua imgem politica,     █")
        print(" █                    ▒▄▀▄▒▄▀▀▄                     █")
        print(" █                    ░▒▄▀▒▀▄▄▀                     █")
        print(" █                    ▒█▄▄▒▒▄▄▀                     █")         
        print(" █                                                  █")
        print(" █      você deve ficar sem olhar o celular         █")
        print(" █  até o final do jogo, para tentar repara-la.     █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio será realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio\n")
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")
    
    
    
    
    
                # ---------------------------------------------------------CASA 30------------------------------------------------------------
    elif posicao_jogador1 == 30:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █               Nada para ser feito aqui,            █")
        print(" █                                                    █")
        print(" █                    ▒▄▀▀▄▒▄▀▀▄                      █")
        print(" █                    ░░▒▀▌▒█ ▒█                      █")
        print(" █                    ▒▀▄▄▀▒▀▄▄▀                      █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █             espere sua próxima jogada              █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")

    
    
    
    
    
    
    
        # ---------------------------------------------------------CASA 31------------------------------------------------------------------
    elif posicao_jogador1 == 31:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █   A oposição faz nova tentativa falha no STF de  █")
        print(" █  fatiar a votação da denúncia contra você e seus █")
        print(" █        ministros,  validando sua autoridade;     █")
        print(" █                   ▒▄▀▀▄▒▄█░                      █")
        print(" █                   ░░▒▀▌░▒█░                      █")
        print(" █                   ▒▀▄▄▀▒▄█▄                      █")         
        print(" █                                                  █")
        print(" █   seu adversário deve postar uma foto feia dele  █")
        print(" █ nas redes sociais,enquanto você anda duas casas. █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
    
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        posicao_jogador1 += 2
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Seu adversário voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            print("┐└┐└┐└┐└┐└┐└┐└┐└┐└┐┐▌▌┐└┐└┐└┐└┐└┐└┐└┐└┐└")
            print("└┐└┐└┐└┐└┐└┐└┐└▌██████████▌┐└┐└┐└┐└┐└┐└┐")
            print("┐└┐└┐└┐└┐└┐└┐█████▌┐┐┐┐▌████▌└┐└┐└┐└┐└┐└")
            print("└┐└┐└┐└┐└┐└┐███┐└┐└┐└┐└┐└▌▌███▌┐└┐└┐└┐└┐")
            print("┐└┐└┐└┐└┐└┐██┐┐└┐└┐└┐└▌████▌▌███┐└┐└┐└┐└")
            print("└┐└┐└┐└┐████└┐└┐└┐└┐└█▌┐└▌██▌████┐└┐└┐└┐")
            print("┐└┐└┐└┐████└┐└┐└┐└┐└┐▌███▌┐▌█▌████┐└┐└┐└")
            print("└┐└┐└┐█████▌└┐└┐└┐┐┐└┐██▌██┐▌█▌███▌┐└┐└┐")
            print("┐└┐└┐███████┐└┐└┐└┐└┐└┐▌████▌██████┐┐└┐└")
            print("└┐└┐█████▌█┐└┐└┐└┐┐┐┐▌▌┐└██▌██████▌█└┐└┐")
            print("┐└┐▌███▌┐▌┐└┐█┐└┐└┐▌▌▌███▌██████████▌└┐└")
            print("└┐└██▌▌┐█┐▌█▌██┐└█└┐██▌████████████▌▌┐└┐")
            print("┐└▌██┐┐█┐▌█▌███▌┐▌█┐┐██▌████████████▌┐┐└")
            print("└┐██▌┐▌▌└████▌██▌▌██▌┐██████████████▌▌└┐")
            print("┐┐██┐└█└█████└████▌███┐███████████████┐└")
            print("└███┐▌▌▌█████┐└████████▌▌█████████████▌┐")
            print("┐███┐███████▌└┐▌███████████████████████└")
            print("▌██▌┐███████└┐└┐▌██████████████████████┐")
            print("███▌████████┐└┐┐┐▌█████████████████████┐")
            print("███▌███████┐└┐▌▌└┐▌████████████████████▌")
            print("███▌███████└┐▌▌└┐└┐▌████▌██████████████▌")
            print("██████████┐┐▌┐└┐└┐└┐▌█▌▌└┐└┐└▌██████████")
            print("█████████┐┐└┐└▌└┐└┐└┐└┐└┐└┐└┐└┐▌████████")
            print("████████▌┐└▌██████▌┐└┐└┐└┐└┐└┐└┐▌███████")
            print("████████┐└┐██████▌██┐└┐└┐└┐▌███┐┐███████")
            print("████████▌▌███┐███┐└█▌┐└┐└┐██└███└┐██████")
            print("███████▌┐┐████▌▌██▌└█└┐└┐▌██▌█▌└┐└██████")
            print("███████┐└┐└┐└┐└┐└┐███┐└┐└███▌┐└┐└┐┐█████")
            print("███████└┐└┐└┐└┐└┐└┐▌┐└┐└┐█┐└┐└┐└┐└┐▌████")
            print("███████┐└┐└┐└┐└┐└┐└┐└┐└┐└▌└┐└┐└┐└┐└┐▌███")
            print("███████└▌┐┐└┐└┐└┐└┐└┐└┐└┐█┐└┐└┐└┐└┐└┐███")
            print("███████┐██└┐└┐└┐└┐┐┐└┐└┐└█▌┐└┐└┐└┐└┐└███")
            print("███████└██▌└┐└┐└┐└┐└┐└┐└┐┐█└┐└┐└┐┐┐└┐███")
            print("███████┐█▌█┐└┐└┐└┐└┐└┐└┐└┐█▌└┐└┐┐█▌┐└███")
            print("███████└█└██┐└┐└┐└▌▌┐└┐└┐└█▌┐└┐└▌█┐└▌███")
            print("██████▌┐██└██┐└┐└┐██┐█▌┐└┐█┐└┐└┐██└┐████")
            print("███████└▌█┐└██▌└┐└▌▌┐▌┐└┐██└┐└┐└█▌┐└███▌")
            print("███████┐└██▌┐███▌┐└┐└┐└┐└█▌┐└┐└██▌└┐███▌")
            print("███████└┐████└▌████┐┐└┐└┐└┐└┐┐█▌█▌┐┐███▌")
            print("███████┐└▌████└┐└███████┐┐┐▌███┐█┐└▌███┐")
            print("███████└┐└█████└┐└┐└┐└▌████▌┐└┐└█┐┐▌███└")
            print("███████┐└┐▌██████▌└┐└┐└┐└▌└┐└┐└┐█┐└████┐")
            print("███████└┐└┐████████└┐└▌└┐└┐└┐▌▌██└┐████└")
            print("███████┐└┐└██▌██████████▌████████┐└████┐")
            print("▌██████▌┐└┐└█└┐└█████████████████└┐████└")
            print("▌███████└┐└┐┐█└┐┐█▌██████████████┐└████┐")
            print("▌███████┐└┐└┐██└┐└┐└┐██████████▌█└┐████└")
            print("└███████▌┐└┐└┐██▌┐└┐└┐└┐└▌└┐█▌└┐█┐└████┐")
            print("┐▌█████▌▌└┐└┐└┐▌██┐└┐└┐└┐└┐└┐└┐┐█└┐████└")
            print("└▌██████└█└┐└┐└┐└███▌┐└┐└┐└┐└┐┐█▌┐└████┐")
            print("┐▌██████┐█▌└┐└┐┐▌└┐█████▌▌▌████▌┐▌┐████└")
            print("└┐██████└┐█┐└┐└┐██└┐└┐▌██████▌└┐┐▌└████┐")
            print("┐└██████▌└▌█┐└┐└┐██▌┐└┐└┐└┐└┐└┐└█└┐████└")
            print("└┐██████▌┐└██┐└┐┐┐┐██▌└┐└┐└┐└┐└██┐▌████┐")
            print("┐└▌██████└┐└██┐└┐└┐└▌████▌┐┐┐███┐└▌████└")
            print("└┐└██████┐└┐└██┐└┐└┐└┐┐▌██████▌┐└┐█████┐")
            print("┐└┐██████└┐└┐└██▌└┐└┐└┐└┐└┐└┐└┐└┐└███▌█└")
            print("└┐└██████▌└┐└┐└▌██└┐└┐└┐└┐└┐└┐└┐└████▌█┐")
            print("┐└┐██▌█▌█▌┐└┐└┐└┐██┐┐└┐└┐└┐└┐└┐└┐█┐██└█└")
            print("└┐└██▌█▌██└┐└┐└┐└┐▌██▌└┐└┐└┐└┐└┐┐█└██┐█┐")
            print("┐└┐██▌█▌██┐└┐└┐└┐└┐└███▌┐└┐└┐└┐└█▌┐▌█└▌┐")
            print("└┐└▌██▌┐██└┐└┐└┐└┐└┐└┐▌██▌▌┐└┐┐██┐└┐▌┐▌┐")
            print("┐└┐▌█▌▌└██┐└┐└┐└┐└┐└┐└┐└┐██████▌┐└┐┐▌└┐┐")
            print("└┐└┐█▌▌┐██▌┐└┐└┐└┐└┐└┐└┐└┐└▌▌▌└┐└┐└┐┐┐└┐")
            print("┐└┐└█▌┐└▌█▌└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└?")
        
        
    
        # -----------------------------------------------------------CASA 32------------------------------------------------------------
    elif posicao_jogador1 == 32:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █              Nada para ser feito aqui,             █")
        print(" █                                                    █")
        print(" █                   ▒▄▀▀▄▒▄▀▄                        █")
        print(" █                   ░░▒▀▌░▒▄▀                        █")
        print(" █                   ▒▀▄▄▀▒█▄▄                        █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █             espere sua próxima jogada              █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 33------------------------------------------------------------------
    elif posicao_jogador1 == 33:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                   ▒▄▀▀▄▒▄▀▀▄                     █")
        print(" █                   ░░▒▀▌░░▒▀▌                     █")
        print(" █                   ▒▀▄▄▀▒▀▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 34------------------------------------------------------------------              
    elif posicao_jogador1 == 34:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █A Procuradoria da República não obteve provas contra█")
        print(" █  você, mas deixou insubordinação na base aliada;   █")
        print(" █  lembre do conselho:Quando incapaz finja-se capaz” █")
        print(" █                 ▒▄▀▀▄░▒▄▀█░                        █")
        print(" █                 ░░▒▀▌▒█▄▄█▄                        █")
        print(" █                 ▒▀▄▄▀░░░▒█░                        █")         
        print(" █      saia da sala e fassa um elogio                █")
        print(" █       a uma pessoa desconhecida,                   █")
        print(" █          para demonstrar sua audácia               █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
            print("░░░░░░░░░░░░░░░░░░░▒▓▓█████████████▓▓▒░░░░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░▒████▓▓▒▒░▒▒▒░▒▒▒▒▒▒▓▓████▓▒░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░▒███▓░░░░░░░░░░░░░░░░░░░░░░▒███████▓▓▒░░░░░░░░░░░")
            print("░░░░░░░░░▒██▓░░░░▒▒███▓▓▒░░░░░░░░░░░░░▓▓▒▒▒▒▒▓██████▓░░░░░░░")
            print("░░░░░░░▒██▓░░░▓███▓▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▓▓███▓████▒▒░░░")
            print("░░░░░░██▓░░▒▓██▓░░▒▓██████▓░░░░░░░▒░░░░░░▒██▓▒░░░▓███▒▓▒░░░░")
            print("░░░░░██░░▓███▒░░▒██▒░░░░▒▒██▓░░░░░░░░░░░██▒░░░░▒████▒█░░░░░░")
            print("░░░░██░▒▓▒▓▓░░░██░░░░░░░░░░░█▓░░░░░░░░░██░░░░░░▒███░░█▒░░░░░")
            print("░░░▓█░░░░░░░░░██░░░░░░░░░░░░▓█░░░░░░░░██░░░░░░░░░░░░░█▒░░░░░")
            print("░░░█▓░░░░░░░░░█▒░░████░░░░░░░█▒░░░░░░░██░░░░░░░░░░░░███░░░░░")
            print("░░▒█░░░░░░░▒▓▒█▓░▓████▓░░░░░▒█░░░░░░░░▒█▒░░░░░░░░░░██░█▒░░░░")
            print("░░██░░░░░▒▓▒▓▒██▒▒▓▓▓░░░░░░░██░░░░░░░░░▒████▓███████▓░█▒░░░░")
            print("░░█▓░░░░░▒░░░▒░▒██▓▒░░░░░▒██▓░░░░░░░░░░░░░░██▓░░░░░░▒██▓░░░░")
            print("░░█░░░░░░░░░▓▒░░░░▒▓██████▓░░░░░░░░░░░░░░▒██░░░▓█▓▓▒░░░██░░░")
            print("░▒█░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒▓▒▒▒▒▒▓▓▓▓██░░▓█▓░▒▒██▒░░██░░")
            print("░▓█░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▒░░██░░██▓░▒░▒░██░░▒█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░▒▓▒▒▒▒▒▒▒▒░░░██░░▓█░█▓░█▒█▓█▓░░█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░▒▒░░▓█▓░░██░█▒▒█▒█▒▓█░░█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░▓█░░░█▒░░░░▒▒░░▒█░▓█░░")
            print("░▒█░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░█▒░░█▒░░░░░░░░▓█░█▓░░")
            print("░░█▓░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█░░█▒░░░░░░░░█░▒█░░░")
            print("░░▓█░░▒░░▒▒░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░░█▓░█▓░░░")
            print("░░░█▒░░▒░░▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░▓█░░█░░░░")
            print("░░░██░░░▒░▒░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░██░░█░░░░")
            print("░░░░█▓░░░▒░▒░░░░▒▒░░░░░▒▒▒▒▒▒░░░░░░░░░░▒█░▒█░░░░░░░█▒░░█▓░░░")
            print("░░░░▓█░░░░▒▒░░░░░▒▒░░░░░░▒▒▒▓▓▓▒░░░░░░░██░██░░░░░░░██░░▓█░░░")
            print("░░░░░██░░░▒░▒░░░░░▒░░░░░░░░▒░▒▒▓█▒░░░░▒█░░█▓▒▓▓▓▒░░▓█░░░█▒░░")
            print("░░░░░▒█▒░░░▒▒▒░░░░▒░░░░░░░░░░▒▒▒░▒▓░░░██░▒█░░░░▒▓▓░░██░░█▒░░")
            print("░░░░░░▒█▒░░░▒░▒░░░▒░░░░░░▒▒▒░░░░▒▒░░░▒█░░██░░░░░░░█░▒█░░█▒░░")
            print("░░░░░░░▓█░░░▒░▒░░░░▒▒░░░░▓▒▒▓▓▓▒░░▓▒░██░░██▒▒▒▒▓▒▓▓███░░█▒░░")
            print("░░░░░░░░██░░░▒░▒░░░░░▒▒░░░░░░░░▓█▓░░░█▓░░██░▓█░█░█░░█▒░░█▒░░")
            print("░░░░░░░░░██░░░░▒▒░░░░░░▒▒░░░░░░░░▒█▓░█▓░░▓█▒▒█▒█░█▒██░░▒█░░░")
            print("░░░░░░░░░░██▒░░░░▒░░░▒░░░▒▒░░░░░░░░▒▓██░░░██░░░░▒▒██░░░██░░░")
            print("░░░░░░░░░░░▓██░░░░░░░░▒▒░░░▒░░░░░░░░░▓█░░░░▓███▓▓██░░░██░░░░")
            print("░░░░░░░░░░░░░▓██▒░░░░░░▒▒▒▒▒░░░░░░░░░░██░░░░░░▒▒▒░░░░██░░░░░")
            print("░░░░░░░░░░░░░░░▓███▒░░░░░░░▒▒▒▒▒▒▒▒░░░░▓██▒░░░░░░░▒███░░░░░░")
            print("░░░░░░░░░░░░░░░░░▒▓███▓▒░░░░░░░▒░░▒▒▒▒░░░▒██▓██████▓░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░▒████▓▒▒░░░░░░░░░░░░░░░▓██▒░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░▒▓████▓░░░░░░░▓█████▒░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█████████▒░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░")


        else:
            print("     ░░░░░░░░░░▄▄█▀▀▀▀▀▀▀▀█▄▄░░░░░░░░")
            print("     ░░░░░░░▄▄▀▀░░░░░░░░░░░░▀▀▄▄░░░░░")
            print("     ░░░░░▄█▀░░░░▄▀░░░░▄░░░░░░░▀█░░░░")
            print("     ░░░░██▄▄████░░░░░░▀▄░░░░░░░░█▄░░")
            print("     ░░▄████▀███▄▀▄░░░░░░███▄▄▄▄░░█░░")
            print("     ░▄█████▄████░██░░░▄███▄▄░▀█▀░░█░")
            print("     ▄███████▀▀░█░▄█░▄███▀█████░█░░▀▄")
            print("     █░█▀██▄▄▄▄█▀░█▀█▀██████▀░██▀█░░█")
            print("     █░█░▀▀▀▀▀░░░█▀░█░███▀▀░░▄█▀░█░░█")
            print("     █░░█▄░░░░▄▄▀░░░█░▀██▄▄▄██▀░░█▄░█")
            print("     █░░░░▀█▀▀▀░░░░░░█░░▀▀▀▀░░░░▄█░░█")
            print("     █░░░░░░░░░░░░░░░░▀▄░░░░░░▄█▀░░░█")
            print("     ░█░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▄░░░░█░")
            print("     ░░█░░░░░░▄▄▄▄▄▄▄░░░░░░░░░░░░░▄▀░")
            print("     ░░░▀▄░░░░░▀█▄░░░▀▀██▄░░░░░░░▄▀░░")
            print("     ░░░░░▀▄▄░░░░░▀▀▀▀▀░░░░░░░░▄▀░░░░")
            print("     ░░░░░░░░▀▀▄▄▄░░░░░░░░▄▄▄▀▀█░░░░░")
            print("     ░░░░░░░░░░▄▀▀█████▀▀▀▀░░░░██░░░░")
            print("     ░░░░░░░░░█░░░██░░░█▀▀▀▀▀▀▀▀█░░░░")
    
    
    
    
    
    # ------------------------------------------------------CASA 35-----------------------------------------------------------------
    elif posicao_jogador1 == 35:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui,            █")
        print(" █                                                  █")
        print(" █                   ▒▄▀▀▄▒█▀▀                      █")
        print(" █                   ░░▒▀▌▒▀▀▄                      █")
        print(" █                   ▒▀▄▄▀▒▄▄▀                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 36------------------------------------------------------------------
    elif posicao_jogador1 == 36:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █              Nada para ser feito aqui,             █")
        print(" █                                                    █")
        print(" █                   ▒▄▀▀▄▒▄▀▀▄                       █")
        print(" █                   ░░▒▀▌▒█▄▄░                       █")
        print(" █                   ▒▀▄▄▀▒▀▄▄▀                       █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █             Espere sua próxima jogada              █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
        
        # -----------------------------------------------------CASA 37------------------------------------------------------------------
    elif posicao_jogador1 == 37:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █      Você articula e ajuda seu broder Aécio,     █")
        print(" █    conseguindo votos no Senado para barrar o     █")
        print(" █afastamento dele;está foi uma grande vitória para █")
        print(" █                   ▒▄▀▀▄▒▀▀█                      █")
        print(" █                   ░░▒▀▌░▒█░                      █")
        print(" █                   ▒▀▄▄▀▒▐▌░                      █")         
        print(" █   sua aliança politica entre seu partido (PSDB)  █")
        print(" █  e o dele(PMDB) escolha um desafio que você já   █")
        print(" █   cumprido e seu adversário deverá faze-lo       █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O seu adversário cumpriu o desafio? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Ele voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("┐└┐└┐└┐└┐└┐└┐└┐└┐└┐┐▌▌┐└┐└┐└┐└┐└┐└┐└┐└┐└")
            print("└┐└┐└┐└┐└┐└┐└┐└▌██████████▌┐└┐└┐└┐└┐└┐└┐")
            print("┐└┐└┐└┐└┐└┐└┐█████▌┐┐┐┐▌████▌└┐└┐└┐└┐└┐└")
            print("└┐└┐└┐└┐└┐└┐███┐└┐└┐└┐└┐└▌▌███▌┐└┐└┐└┐└┐")
            print("┐└┐└┐└┐└┐└┐██┐┐└┐└┐└┐└▌████▌▌███┐└┐└┐└┐└")
            print("└┐└┐└┐└┐████└┐└┐└┐└┐└█▌┐└▌██▌████┐└┐└┐└┐")
            print("┐└┐└┐└┐████└┐└┐└┐└┐└┐▌███▌┐▌█▌████┐└┐└┐└")
            print("└┐└┐└┐█████▌└┐└┐└┐┐┐└┐██▌██┐▌█▌███▌┐└┐└┐")
            print("┐└┐└┐███████┐└┐└┐└┐└┐└┐▌████▌██████┐┐└┐└")
            print("└┐└┐█████▌█┐└┐└┐└┐┐┐┐▌▌┐└██▌██████▌█└┐└┐")
            print("┐└┐▌███▌┐▌┐└┐█┐└┐└┐▌▌▌███▌██████████▌└┐└")
            print("└┐└██▌▌┐█┐▌█▌██┐└█└┐██▌████████████▌▌┐└┐")
            print("┐└▌██┐┐█┐▌█▌███▌┐▌█┐┐██▌████████████▌┐┐└")
            print("└┐██▌┐▌▌└████▌██▌▌██▌┐██████████████▌▌└┐")
            print("┐┐██┐└█└█████└████▌███┐███████████████┐└")
            print("└███┐▌▌▌█████┐└████████▌▌█████████████▌┐")
            print("┐███┐███████▌└┐▌███████████████████████└")
            print("▌██▌┐███████└┐└┐▌██████████████████████┐")
            print("███▌████████┐└┐┐┐▌█████████████████████┐")
            print("███▌███████┐└┐▌▌└┐▌████████████████████▌")
            print("███▌███████└┐▌▌└┐└┐▌████▌██████████████▌")
            print("██████████┐┐▌┐└┐└┐└┐▌█▌▌└┐└┐└▌██████████")
            print("█████████┐┐└┐└▌└┐└┐└┐└┐└┐└┐└┐└┐▌████████")
            print("████████▌┐└▌██████▌┐└┐└┐└┐└┐└┐└┐▌███████")
            print("████████┐└┐██████▌██┐└┐└┐└┐▌███┐┐███████")
            print("████████▌▌███┐███┐└█▌┐└┐└┐██└███└┐██████")
            print("███████▌┐┐████▌▌██▌└█└┐└┐▌██▌█▌└┐└██████")
            print("███████┐└┐└┐└┐└┐└┐███┐└┐└███▌┐└┐└┐┐█████")
            print("███████└┐└┐└┐└┐└┐└┐▌┐└┐└┐█┐└┐└┐└┐└┐▌████")
            print("███████┐└┐└┐└┐└┐└┐└┐└┐└┐└▌└┐└┐└┐└┐└┐▌███")
            print("███████└▌┐┐└┐└┐└┐└┐└┐└┐└┐█┐└┐└┐└┐└┐└┐███")
            print("███████┐██└┐└┐└┐└┐┐┐└┐└┐└█▌┐└┐└┐└┐└┐└███")
            print("███████└██▌└┐└┐└┐└┐└┐└┐└┐┐█└┐└┐└┐┐┐└┐███")
            print("███████┐█▌█┐└┐└┐└┐└┐└┐└┐└┐█▌└┐└┐┐█▌┐└███")
            print("███████└█└██┐└┐└┐└▌▌┐└┐└┐└█▌┐└┐└▌█┐└▌███")
            print("██████▌┐██└██┐└┐└┐██┐█▌┐└┐█┐└┐└┐██└┐████")
            print("███████└▌█┐└██▌└┐└▌▌┐▌┐└┐██└┐└┐└█▌┐└███▌")
            print("███████┐└██▌┐███▌┐└┐└┐└┐└█▌┐└┐└██▌└┐███▌")
            print("███████└┐████└▌████┐┐└┐└┐└┐└┐┐█▌█▌┐┐███▌")
            print("███████┐└▌████└┐└███████┐┐┐▌███┐█┐└▌███┐")
            print("███████└┐└█████└┐└┐└┐└▌████▌┐└┐└█┐┐▌███└")
            print("███████┐└┐▌██████▌└┐└┐└┐└▌└┐└┐└┐█┐└████┐")
            print("███████└┐└┐████████└┐└▌└┐└┐└┐▌▌██└┐████└")
            print("███████┐└┐└██▌██████████▌████████┐└████┐")
            print("▌██████▌┐└┐└█└┐└█████████████████└┐████└")
            print("▌███████└┐└┐┐█└┐┐█▌██████████████┐└████┐")
            print("▌███████┐└┐└┐██└┐└┐└┐██████████▌█└┐████└")
            print("└███████▌┐└┐└┐██▌┐└┐└┐└┐└▌└┐█▌└┐█┐└████┐")
            print("┐▌█████▌▌└┐└┐└┐▌██┐└┐└┐└┐└┐└┐└┐┐█└┐████└")
            print("└▌██████└█└┐└┐└┐└███▌┐└┐└┐└┐└┐┐█▌┐└████┐")
            print("┐▌██████┐█▌└┐└┐┐▌└┐█████▌▌▌████▌┐▌┐████└")
            print("└┐██████└┐█┐└┐└┐██└┐└┐▌██████▌└┐┐▌└████┐")
            print("┐└██████▌└▌█┐└┐└┐██▌┐└┐└┐└┐└┐└┐└█└┐████└")
            print("└┐██████▌┐└██┐└┐┐┐┐██▌└┐└┐└┐└┐└██┐▌████┐")
            print("┐└▌██████└┐└██┐└┐└┐└▌████▌┐┐┐███┐└▌████└")
            print("└┐└██████┐└┐└██┐└┐└┐└┐┐▌██████▌┐└┐█████┐")
            print("┐└┐██████└┐└┐└██▌└┐└┐└┐└┐└┐└┐└┐└┐└███▌█└")
            print("└┐└██████▌└┐└┐└▌██└┐└┐└┐└┐└┐└┐└┐└████▌█┐")
            print("┐└┐██▌█▌█▌┐└┐└┐└┐██┐┐└┐└┐└┐└┐└┐└┐█┐██└█└")
            print("└┐└██▌█▌██└┐└┐└┐└┐▌██▌└┐└┐└┐└┐└┐┐█└██┐█┐")
            print("┐└┐██▌█▌██┐└┐└┐└┐└┐└███▌┐└┐└┐└┐└█▌┐▌█└▌┐")
            print("└┐└▌██▌┐██└┐└┐└┐└┐└┐└┐▌██▌▌┐└┐┐██┐└┐▌┐▌┐")
            print("┐└┐▌█▌▌└██┐└┐└┐└┐└┐└┐└┐└┐██████▌┐└┐┐▌└┐┐")
            print("└┐└┐█▌▌┐██▌┐└┐└┐└┐└┐└┐└┐└┐└▌▌▌└┐└┐└┐┐┐└┐")
            print("┐└┐└█▌┐└▌█▌└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└?")
    
    
    
    
    
    # -------------------------------------------------------CASA 38---------------------------------------------------------------
    
    if posicao_jogador1 == 38:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                     █")
        print(" █              Nada para ser feito aqui               █")
        print(" █                                                     █")
        print(" █                   ▒▄▀▀▄▒▄▀▀▄                        █")
        print(" █                   ░░▒▀▌▒▄▀▀▄                        █")
        print(" █                   ▒▀▄▄▀▒▀▄▄▀                        █")         
        print(" █                                                     █")
        print(" █                                                     █")
        print(" █             Espere sua próxima jogada               █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 39------------------------------------------------------------------
    if posicao_jogador1 == 39:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                   ▒▄▀▀▄▒▄▀▀▄                     █")
        print(" █                   ░░▒▀▌▒▀▄▄▀                     █")
        print(" █                   ▒▀▄▄▀▒▒▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 40------------------------------------------------------------------
    if posicao_jogador1 == 40:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ A dívida pública avança 3,22% em junho desse ano,  █")
        print(" █sendo de R$ 3,35 trilhões;esse cenário econômico    █")
        print(" █prejudica sua imagem,pensando que sua postura deve  █")
        print(" █ser como a água  ░▒▄▀█░▒▄▀▀▄                        █")
        print(" █que não tem      ▒█▄▄█▄▒█ ▒█                        █")
        print(" █forma constante, ░░░▒█░ ▀▄▄▀                        █")         
        print(" █simule uma pedido de casamento para alguém que não  █")
        print(" █seja seu adversário, demonstrando sua flexibilidade,█")
        print(" █            com isso avançará 4 casas               █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa\n")
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")
        else:
            posicao_jogador1 += 4
            print("Você voltou 3 casas, por não ter cumprido o desafio")
            print("░░░░░░░░░░░░░░░░░░░▒▓▓█████████████▓▓▒░░░░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░▒████▓▓▒▒░▒▒▒░▒▒▒▒▒▒▓▓████▓▒░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░▒███▓░░░░░░░░░░░░░░░░░░░░░░▒███████▓▓▒░░░░░░░░░░░")
            print("░░░░░░░░░▒██▓░░░░▒▒███▓▓▒░░░░░░░░░░░░░▓▓▒▒▒▒▒▓██████▓░░░░░░░")
            print("░░░░░░░▒██▓░░░▓███▓▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▓▓███▓████▒▒░░░")
            print("░░░░░░██▓░░▒▓██▓░░▒▓██████▓░░░░░░░▒░░░░░░▒██▓▒░░░▓███▒▓▒░░░░")
            print("░░░░░██░░▓███▒░░▒██▒░░░░▒▒██▓░░░░░░░░░░░██▒░░░░▒████▒█░░░░░░")
            print("░░░░██░▒▓▒▓▓░░░██░░░░░░░░░░░█▓░░░░░░░░░██░░░░░░▒███░░█▒░░░░░")
            print("░░░▓█░░░░░░░░░██░░░░░░░░░░░░▓█░░░░░░░░██░░░░░░░░░░░░░█▒░░░░░")
            print("░░░█▓░░░░░░░░░█▒░░████░░░░░░░█▒░░░░░░░██░░░░░░░░░░░░███░░░░░")
            print("░░▒█░░░░░░░▒▓▒█▓░▓████▓░░░░░▒█░░░░░░░░▒█▒░░░░░░░░░░██░█▒░░░░")
            print("░░██░░░░░▒▓▒▓▒██▒▒▓▓▓░░░░░░░██░░░░░░░░░▒████▓███████▓░█▒░░░░")
            print("░░█▓░░░░░▒░░░▒░▒██▓▒░░░░░▒██▓░░░░░░░░░░░░░░██▓░░░░░░▒██▓░░░░")
            print("░░█░░░░░░░░░▓▒░░░░▒▓██████▓░░░░░░░░░░░░░░▒██░░░▓█▓▓▒░░░██░░░")
            print("░▒█░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒▓▒▒▒▒▒▓▓▓▓██░░▓█▓░▒▒██▒░░██░░")
            print("░▓█░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▒░░██░░██▓░▒░▒░██░░▒█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░▒▓▒▒▒▒▒▒▒▒░░░██░░▓█░█▓░█▒█▓█▓░░█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░▒▒░░▓█▓░░██░█▒▒█▒█▒▓█░░█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░▓█░░░█▒░░░░▒▒░░▒█░▓█░░")
            print("░▒█░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░█▒░░█▒░░░░░░░░▓█░█▓░░")
            print("░░█▓░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█░░█▒░░░░░░░░█░▒█░░░")
            print("░░▓█░░▒░░▒▒░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░░█▓░█▓░░░")
            print("░░░█▒░░▒░░▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░▓█░░█░░░░")
            print("░░░██░░░▒░▒░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░██░░█░░░░")
            print("░░░░█▓░░░▒░▒░░░░▒▒░░░░░▒▒▒▒▒▒░░░░░░░░░░▒█░▒█░░░░░░░█▒░░█▓░░░")
            print("░░░░▓█░░░░▒▒░░░░░▒▒░░░░░░▒▒▒▓▓▓▒░░░░░░░██░██░░░░░░░██░░▓█░░░")
            print("░░░░░██░░░▒░▒░░░░░▒░░░░░░░░▒░▒▒▓█▒░░░░▒█░░█▓▒▓▓▓▒░░▓█░░░█▒░░")
            print("░░░░░▒█▒░░░▒▒▒░░░░▒░░░░░░░░░░▒▒▒░▒▓░░░██░▒█░░░░▒▓▓░░██░░█▒░░")
            print("░░░░░░▒█▒░░░▒░▒░░░▒░░░░░░▒▒▒░░░░▒▒░░░▒█░░██░░░░░░░█░▒█░░█▒░░")
            print("░░░░░░░▓█░░░▒░▒░░░░▒▒░░░░▓▒▒▓▓▓▒░░▓▒░██░░██▒▒▒▒▓▒▓▓███░░█▒░░")
            print("░░░░░░░░██░░░▒░▒░░░░░▒▒░░░░░░░░▓█▓░░░█▓░░██░▓█░█░█░░█▒░░█▒░░")
            print("░░░░░░░░░██░░░░▒▒░░░░░░▒▒░░░░░░░░▒█▓░█▓░░▓█▒▒█▒█░█▒██░░▒█░░░")
            print("░░░░░░░░░░██▒░░░░▒░░░▒░░░▒▒░░░░░░░░▒▓██░░░██░░░░▒▒██░░░██░░░")
            print("░░░░░░░░░░░▓██░░░░░░░░▒▒░░░▒░░░░░░░░░▓█░░░░▓███▓▓██░░░██░░░░")
            print("░░░░░░░░░░░░░▓██▒░░░░░░▒▒▒▒▒░░░░░░░░░░██░░░░░░▒▒▒░░░░██░░░░░")
            print("░░░░░░░░░░░░░░░▓███▒░░░░░░░▒▒▒▒▒▒▒▒░░░░▓██▒░░░░░░░▒███░░░░░░")
            print("░░░░░░░░░░░░░░░░░▒▓███▓▒░░░░░░░▒░░▒▒▒▒░░░▒██▓██████▓░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░▒████▓▒▒░░░░░░░░░░░░░░░▓██▒░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░▒▓████▓░░░░░░░▓█████▒░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█████████▒░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░")
    
    # --------------------------------------------------CASA 41---------------------------------------------------------------------
    if posicao_jogador1 == 41:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                   ░▒▄▀█░▒▄█░                     █")
        print(" █                   ▒█▄▄█▄░▒█░                     █")
        print(" █                   ░░░▒█░▒▄█▄                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 42------------------------------------------------------------------
    if posicao_jogador1 == 42:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █A reforma da previdência que você colocou em pauta  █")
        print(" █foi aprovada, tendo em mente o pensamento “O gover- █")
        print(" █nante esclarecido estabeleceplanos a seguir”.       █")
        print(" █                  ░▒▄▀█░▒▄▀▄                        █")
        print(" █                  ▒█▄▄█▄░▒▄▀                        █")
        print(" █                  ░░░▒█░▒█▄▄                        █")         
        print(" █  Passe uma rodada falando com algum sotaque ou em  █")
        print(" █                                                    █")
        print(" █               outro idioma.                        █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")
    
    
    
    
    
    
    # --------------------------------------------------------CASA 43---------------------------------------------------------------
    if posicao_jogador1 == 43:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █O TCU quer explicações suas sobre o 'esquema dos  █")
        print(" █portos', onde a empresa do seu amigo explora dês- █")
        print(" █de 1998, sendo os últimos 3 anos sem contrato,    █")
        print(" █                  ░▒▄▀█░▒▄▀▀▄                     █")
        print(" █                  ▒█▄▄█▄░░▒▀▌                     █")
        print(" █                  ░░░▒█░▒▀▄▄▀                     █")         
        print(" █    seja sútil, para não chamar a atenção dos     █")
        print(" █   jornalistas fique sem usar a palavra (não)     █")
        print(" █         até o final do jogo.                     █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    
    # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio será realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")
    
    
    
    
    
    # ---------------------------------------------------------CASA 44--------------------------------------------------------------
    if posicao_jogador1 == 44:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █               Nada para ser feito aqui             █")
        print(" █                                                    █")
        print(" █                  ░▒▄▀█░░▒▄▀█░                      █")
        print(" █                  ▒█▄▄█▄▒█▄▄█▄                      █")
        print(" █                  ░░░▒█░░░░▒█░                      █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █               Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 45------------------------------------------------------------------
    if posicao_jogador1 == 45:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █      Você por meio de seus advogados, partiu     █")
        print(" █   para um ataque sem precedentes contra o ex-    █")
        print(" █  procurador-geral da República Rodrigo Janot,    █")
        print(" █                  ░▒▄▀█░▒█▀▀                      █")
        print(" █                  ▒█▄▄█▄▒▀▀▄                      █")
        print(" █                  ░░░▒█░▒▄▄▀                      █")         
        print(" █  com isso ganha poder sobre seu adversário e ele █")
        print(" █     deverá se desculpar na frente de todos       █")
        print(" █      da sala de aula, senão ele voltará 3 casas. █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    
    # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            print("11111111111111111111111111111")                
            print("11111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")         
            print("1111111111¶¶¶¶¶111_________________¶¶")        
            print("11111111¶¶1_______1111______111_____¶¶")       
            print("111111¶¶______11_________11111111____¶1")      
            print("111111¶____11___1_____11______1111___1¶")      
            print("11111¶1___1_____1_____1_________1_____¶1")     
            print("11111¶__________________1¶¶¶¶1________1¶ ")    
            print("1111¶¶_____¶¶¶¶1______1¶¶_¶¶¶¶¶1_______¶¶ ")   
            print("111¶¶_1_1_¶¶¶¶¶¶¶_1___¶__1¶¶¶¶¶¶111____1¶¶  ") 
            print("111¶_1________11¶¶1___¶¶¶1__1_____1¶¶¶1__1¶  ") 
            print("11¶1__1¶¶1______11_____1____¶¶__1¶¶1__¶¶__1¶ ")
            print("11¶1__111¶¶¶¶___¶1___________1¶¶1___¶__¶1__¶ ")
            print("11¶1____1_11___¶¶_____1¶1_________¶¶¶1__¶__¶1")
            print("111¶_1__¶____1¶¶______11¶1_____1¶¶1_¶¶¶1¶__¶1")
            print("111¶1__¶¶___11¶¶____¶¶¶_¶___1¶¶¶1___¶__¶___¶1")
            print("111¶¶__¶¶¶1_____¶¶1_____11¶¶¶1_¶__1¶¶_____¶11")
            print("1111¶__¶¶1¶¶¶1___¶___1¶¶¶¶1____¶¶¶¶¶_____¶¶11")
            print("1111¶__¶_1__¶¶¶¶¶¶¶¶¶11__¶__1¶¶¶1_¶_____¶¶111")
            print("1111¶1_¶¶¶__1___¶___1____¶¶¶¶¶1¶_¶¶____¶¶1111")
            print("1111¶1_¶¶¶¶¶¶¶1¶¶11¶¶1¶¶¶¶¶1___1¶¶_____¶11111")
            print("1111¶1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_¶____¶¶_____¶¶11111")
            print("1111¶1_¶¶¶¶¶¶¶¶¶¶¶¶1¶1____¶__1¶¶______¶111111")
            print("1111¶__1¶¶_¶_¶__¶___11____1¶¶¶______1¶1111111")
            print("1111¶___¶¶1¶_11_11__1¶__1¶¶¶1___11_1¶11111111")
            print("1111¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1___11111¶¶111111111")
            print("1111¶__________11111_______111_1¶¶11111111111")
            print("1111¶_1__11____________1111__1¶¶1111111111111")
            print("1111¶__11__1________1111___1¶¶111111111111111")
            print("1111¶___1111_____________1¶¶11111111111111111")
            print("1111¶¶_______________11¶¶¶1111111111111111111")
            print("11111¶¶__________1¶¶¶¶¶1111111111111111111111")
            print("1111111¶¶¶¶¶¶¶¶¶¶¶111111111111111111111111111")
    
    
    
    
    
    
    
    # -------------------------------------------------------CASA 46----------------------------------------------------------------
    if posicao_jogador1 == 46:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █               Nada para ser feito aqui,            █")
        print(" █                                                    █")
        print(" █                    ░▒▄▀█░▒▄▀▀▄                     █")
        print(" █                    ▒█▄▄█▄▒█▄▄░                     █")
        print(" █                    ░░░▒█░▒▀▄▄▀                     █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █               espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 47------------------------------------------------------------------
    if posicao_jogador1 == 47:
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("█Você foi denunciado pela WikiLeaks como informante█")
        print("█   da embaixada Americana no Brasil, invente uma  █")
        print("█           poesia que rime como a frase           █")
        print("█                    ░▒▄▀█░▒▀▀█                    █")
        print("█                    ▒█▄▄█▄░▒█░                    █")
        print("█                    ░░░▒█░▒▐▌░                    █")         
        print("█        'Tá tranquilo, Tio Sam, tá, tá...'        █")
        print("█            enquanto isso volte 8 casas           █")
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        posicao_jogador1 -= 8
    
    # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 11 casas, por não ter cumprido o desafio.\n")
            print("          ─────────────────────────▐█")
            print("          ────▄──────────────────▄█▓█")
            print("          ───▐██▄───────────────▄▓░░▓▓")
            print("          ───▐█░██▓────────────▓▓░░░▓▌")
            print("          ───▐█▌░▓██──────────█▓░░░░▓")
            print("          ────▓█▌░░▓█▄███████▄███▓░▓█")
            print("          ────▓██▌░▓██░░░░░░░░░░▓█░▓▌")
            print("          ─────▓█████░░░░░░░░░░░░▓██")
            print("          ─────▓██▓░░░░░░░░░░░░░░░▓█")
            print("          ─────▐█▓░░░░░░█▓░░▓█░░░░▓█▌")
            print("          ─────▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌")
            print("          ─────▓▓░▓██████▓░▓███▓▓▌░█▓")
            print("          ────▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██")
            print("          ────▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌")
            print("          ────▓█▌░▓█████▓░░░▓███▓▀░▓█▓")
            print("          ───▐▓█░░░▀▓██▀░░░░░─▀▓▀░░▓█▓")
            print("          ───▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓")
            print("          ───▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌")
            print("          ───▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓")
            print("          ──▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░██▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓")
            print("          ──██░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ──█▌░░░░░░░░░░░░░░░░░░░░░░░░▐▓▌")
            print("          ─▐▓░░░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ▐█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\n")



    if posicao_jogador1 > 47:
        break



        print("\n\n")
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("            {}, SUA POSIÇÂO ATUAL É {} ")
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")    
        print("\n\n")











































    
#------------------------------------------jogador 2-----------------------------------------------------------------------------
    input("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n"
          "                  {}, AGORA É SUA VEZ! \n APERTE ENTER PARA JOGAR O DADO!           \n"
          "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n".format(nome_jogador2))
    cont += 1
    dado = random.randint(1, 6)
    print("O DADO QUE CAIU FOI:\n")
    if dado == 1:
        
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█       █▒▒▒▒░")
        print("█   ░   █▒▒░░░")
        print("█   █   █▒▒░░▒")
        print("█       █▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 2:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█     █░█▒▒▒▒░")
        print("█       █▒▒░░░")
        print("█       █▒▒░░▒")
        print("█ █░    █▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 3:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█     █░█▒▒▒▒░")
        print("█   ▄   █▒▒░░░")
        print("█   ▀░  █▒▒░░▒")
        print("█ █░    █▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 4:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█ ░   ░ █▒▒▒▒░")
        print("█ █   █ █▒▒░░░")
        print("█       █▒▒░░▒")
        print("█ █░  █░█▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 5:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█ ░   ░ █▒▒▒▒░")
        print("█ █ ░ █ █▒▒░░░")
        print("█   █   █▒▒░░▒")
        print("█ █░  █░█▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    elif dado == 6:
        print("    ░░▒░▒░░▒░▒")
        print(" ░▒░▒░▒▀░░▒▒░░")
        print("█▀▀▀▀▀▀▀█▒▒░█░")
        print("█ █░  █░█▒▒▒▒░")
        print("█ ▄   ▄ █▒▒░░░")
        print("█ ▀   ▀ █▒▒░░▒")
        print("█ █░  █░█▒█▒░")
        print("█▄▄▄▄▄▄▄█▒░")
    print("\n\n")    
        
        
    
    posicao_jogador2 += dado
    #-----------------------------------------------------CASA 1------------------------------------------------------------------
    print("{}, SUA POSIÇÃO ATUAL É : \n".format(nome_jogador2))
    if posicao_jogador1 == 0:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                                                                       █")
        print(" █                                                                                                       █")
        print(" █                                                                                                       █")
        print(" █                                                                                                       █")
        print(" █                                 ░▐██▒██▄░▒█▌░▐██░▐█▀█░▐██▒▐█▀▀█▌                                      █")
        print(" █                                 ─░█▌▒▐█▒█▒█░─░█▌░▐█───░█▌▒▐█▄▒█▌                                      █")         
        print(" █                                 ░▐██▒██░▒██▌░▐██░▐█▄█░▐██▒▐██▄█▌                                      █")
        print(" █                                                                                                       █")
        print(" █                                                                                                       █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")


    if posicao_jogador2 == 1:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █              Nada para ser feito aqui            █")
        print(" █                                                  █")
        print(" █                        ▒▄█░                      █")
        print(" █                        ░▒█░                      █")
        print(" █                        ▒▄█▄                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █              Espere sua próxima jogada           █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("           ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░\n\n")




    # -----------------------------------------------------CASA 2------------------------------------------------------------------
    if posicao_jogador2 == 2:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █     Você deve seguir o conselho do Pensador        █")
        print(" █                                                    █")
        print(" █                      ▒▄▀▄                          █")
        print(" █                      ░▒▄▀                          █")
        print(" █                      ▒█▄▄                          █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █          tente lamber o seu cotovelo               █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))

        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")






            # -----------------------------------------------------CASA 3------------------------------------------------------------------
    elif posicao_jogador2 == 3:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █       Você cruzou o caminho do Sérgio Moro       █")
        print(" █              volte ao início do jogo             █")
        print(" █                     ▒▄▀▀▄                        █")
        print(" █                     ░░▒▀▌                        █")
        print(" █                     ▒▀▄▄▀                        █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             volte ao início do jogo              █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        posicao_jogador2 = 0
        print("         ░░░░░░░░███████████████░░░░░░░░")
        print("         ░░░░░█████████████████████░░░░░")
        print("         ░░░░████████████████████████░░░")
        print("         ░░░██████████████████████████░░")
        print("         ░░█████████████████████████████")
        print("         ░░███████████▀░░░░░░░░░████████")
        print("         ░░███████████░░░░░░░░░░░░░░░███")
        print("         ░████████████░░░░░░░░░░░░░░░░██")
        print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
        print("         █░░░░█████░░░░░░▄███████░░██░░█")
        print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
        print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
        print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
        print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
        print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
        print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
        print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
        print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
        print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
        print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
        print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
        print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
        print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
        print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
        print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")




    # -----------------------------------------------------CASA 4------------------------------------------------------------------
    elif posicao_jogador2 == 4:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █             Nada para ser feito aqui               █")
        print(" █                                                    █")
        print(" █                     ░▒▄▀█░                         █")
        print(" █                     ▒█▄▄█▄                         █")
        print(" █                     ░░░▒█░                         █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █             Espere sua próxima jogada              █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░\n\n")





    # -----------------------------------------------------CASA 5------------------------------------------------------------------
    elif posicao_jogador2 == 5:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █             Você encontrou informações           █")
        print(" █             cruciais de seu adversário e         █")
        print(" █                                                  █")
        print(" █                        ▒█▀▀                      █")
        print(" █                        ▒▀▀▄                      █")
        print(" █                        ▒▄▄▀                      █")         
        print(" █                                                  █")
        print(" █          ele deve dançar uma música de sua       █")
        print(" █                      escolha.                    █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            print("Seu adversário voltou 3 casas, por não ter cumprido o desafio")
            posicao_jogador2 -= 3
        else:
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")




            # ----------------------------------------------------CASA 6-------------------------------------------------------------------
    elif posicao_jogador2 == 6:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █      Você extingue uma reserva na Amazônia para    █")
        print(" █                 ampliar exploração,                █")
        print(" █                      ▒▄▀▀▄                         █")
        print(" █                     ░▒█▄▄░                         █")
        print(" █                      ▒▀▄▄▀                         █")         
        print(" █                                                    █")
        print(" █                imite uma motossera                 █")
        print(" █        por 10 segundos e avance duas casas.        █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n\n")


        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            posicao_jogador2 += 2
            print("          ─────────────────────────▐█")
            print("          ────▄──────────────────▄█▓█")
            print("          ───▐██▄───────────────▄▓░░▓▓")
            print("          ───▐█░██▓────────────▓▓░░░▓▌")
            print("          ───▐█▌░▓██──────────█▓░░░░▓")
            print("          ────▓█▌░░▓█▄███████▄███▓░▓█")
            print("          ────▓██▌░▓██░░░░░░░░░░▓█░▓▌")
            print("          ─────▓█████░░░░░░░░░░░░▓██")
            print("          ─────▓██▓░░░░░░░░░░░░░░░▓█")
            print("          ─────▐█▓░░░░░░█▓░░▓█░░░░▓█▌")
            print("          ─────▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌")
            print("          ─────▓▓░▓██████▓░▓███▓▓▌░█▓")
            print("          ────▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██")
            print("          ────▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌")
            print("          ────▓█▌░▓█████▓░░░▓███▓▀░▓█▓")
            print("          ───▐▓█░░░▀▓██▀░░░░░─▀▓▀░░▓█▓")
            print("          ───▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓")
            print("          ───▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌")
            print("          ───▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓")
            print("          ──▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░██▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓")
            print("          ──██░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ──█▌░░░░░░░░░░░░░░░░░░░░░░░░▐▓▌")
            print("          ─▐▓░░░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ▐█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\n")





            # -----------------------------------------------------CASA 7------------------------------------------------------------------            
    elif posicao_jogador2 == 7:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █  Você está sendo investigado por inquérito, faça █")
        print(" █  uma imitação de algum famoso, para treinar sua  █")
        print(" █     expressãodiante do juiz, caso contrário,     █")
        print(" █                        ▒▀▀█                      █")
        print(" █                        ░▒█░                      █")
        print(" █                        ▒▐▌░                      █")         
        print(" █                                                  █")
        print(" █                     seu adversário               █")
        print(" █         avançará duas casas e você voltará 3     █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            posicao_jogador1 += 2
            print(
                "Você voltou 3 casas e seu inimigo avançou 3, por não ter cumprido o desafio, além de perder o beneficio da casa")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")            




            # -----------------------------------------------------CASA 8-------------------------------------------------------------------
    elif posicao_jogador2 == 8:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █            Nada para ser feito aqui                █")
        print(" █                                                    █")
        print(" █                      ▒▄▀▀▄                         █")
        print(" █                      ▒▄▀▀▄                         █")
        print(" █                      ▒▀▄▄▀                         █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █            Espere sua próxima jogada               █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")



    # -----------------------------------------------------CASA 9------------------------------------------------------------------
    elif posicao_jogador2 == 9:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ Você está sendo investigado, mas conseguiu apoio █")
        print(" █trocando alguns votos por leis mais brandas       █")
        print(" █ao trabalho análogo ao escravos, toda vitória tem █")
        print(" █que ser comemorada!     ▒▄▀▀▄                     █")
        print(" █escolha uma música para ▒▀▄▄▀                     █")
        print(" █seu adversário cantar   ▒▒▄▄▀                     █")         
        print(" █até o final sem errar. Se ele acertar ele avança  █")
        print(" █uma casa e você retornará 3, caso contrário ele   █")
        print(" █pagará o pato(pizza).                             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("Seu adversário conseguiu realizar o desafio com sucesso? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("Seu adversário conseguiu realizar o desafio com sucesso? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            posicao_jogador2 += 1
            print("Seu adversário voltou 3 casas, por não ter cumprido o desafio e você avançou 1")
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 
        else:
            posicao_jogador2 -= 3
            posicao_jogador1 += 1
            print("Você voltou 3 casas, por não ter cumprido o desafio e ele avançou 1\n")
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")





            # -----------------------------------------------------CASA 10------------------------------------------------------------------              
    elif posicao_jogador2 == 10:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █               Nada para ser feito aqui             █")
        print(" █                                                    █")
        print(" █                   ▒▄█░▒ ▄▀▀▄                       █")
        print(" █                   ░▒█░▒▒█ ▒█                       █")
        print(" █                   ▒▄█▄▒▒▀▄▄▀                       █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █              espere sua próxima jogada             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")





    # -----------------------------------------------------CASA 11------------------------------------------------------------------              
    elif posicao_jogador2 == 11:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █   É divulgada a Lista Suja do Trabalho Escravo,  █")
        print(" █    isso é péssimo para sua campanha. passe essa  █")
        print(" █                                                  █")
        print(" █                    ▒▄█░▒▄█░▒                     █")
        print(" █                    ░▒█░░▒█░▒                     █")
        print(" █                    ▒▄█▄▒▄█▄▒                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █   rodada com os olhos fechados e volte 5 casas.  █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio vai ser realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 8
            print("Você voltou 8 casas, por não ter cumprido o desafio")
        else:
            posicao_jogador2 -= 5
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")





            # ------------------------------------------------------CASA 12-----------------------------------------------------------------
    elif posicao_jogador2 == 12:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █               Nada para ser feito aqui             █")
        print(" █                                                    █")
        print(" █                     ▒▄█░▒▒▄▀▄                      █")
        print(" █                     ░▒█░░▒ ▄▀▒                     █")
        print(" █                     ▒▄█▄▒▒█▄▄                      █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █               Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")




    # -----------------------------------------------------CASA 13------------------------------------------------------------------
    elif posicao_jogador2 == 13:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █    Você passa dois dias internado no hospital,   █")
        print(" █                                                  █")
        print(" █                     ▒▄█░▒▄▀▀▄                    █")
        print(" █                     ░▒█░░░▒▀▌                    █")
        print(" █                     ▒▄█▄▒▀▄▄▀                    █")         
        print(" █                                                  █")
        print(" █           de 30 passos em qualquer direção       █")
        print(" █           para ajudar na sua reabilitação.       █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("          ─────────────────────────▐█")
            print("          ────▄──────────────────▄█▓█")
            print("          ───▐██▄───────────────▄▓░░▓▓")
            print("          ───▐█░██▓────────────▓▓░░░▓▌")
            print("          ───▐█▌░▓██──────────█▓░░░░▓")
            print("          ────▓█▌░░▓█▄███████▄███▓░▓█")
            print("          ────▓██▌░▓██░░░░░░░░░░▓█░▓▌")
            print("          ─────▓█████░░░░░░░░░░░░▓██")
            print("          ─────▓██▓░░░░░░░░░░░░░░░▓█")
            print("          ─────▐█▓░░░░░░█▓░░▓█░░░░▓█▌")
            print("          ─────▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌")
            print("          ─────▓▓░▓██████▓░▓███▓▓▌░█▓")
            print("          ────▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██")
            print("          ────▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌")
            print("          ────▓█▌░▓█████▓░░░▓███▓▀░▓█▓")
            print("          ───▐▓█░░░▀▓██▀░░░░░─▀▓▀░░▓█▓")
            print("          ───▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓")
            print("          ───▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌")
            print("          ───▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓")
            print("          ──▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░██▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓")
            print("          ──██░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ──█▌░░░░░░░░░░░░░░░░░░░░░░░░▐▓▌")
            print("          ─▐▓░░░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ▐█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\n")





            # -----------------------------------------------------CASA 14------------------------------------------------------------------
    elif posicao_jogador2 == 14:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █     Você passa por um processo de impeachment,     █")
        print(" █ escolha alguém para dançar valsa e dançem enquanto █")
        print(" █                                                    █")
        print(" █                    ▒▄█░░▒▄▀█░                      █")
        print(" █                    ░▒█░▒█▄▄█▄                      █")
        print(" █                    ▒▄█▄▒░░░█░                      █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █         seu adversário anda duas casas.            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        posicao_jogador1 += 2
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("     ░░░░░░░░░░▄▄█▀▀▀▀▀▀▀▀█▄▄░░░░░░░░")
            print("     ░░░░░░░▄▄▀▀░░░░░░░░░░░░▀▀▄▄░░░░░")
            print("     ░░░░░▄█▀░░░░▄▀░░░░▄░░░░░░░▀█░░░░")
            print("     ░░░░██▄▄████░░░░░░▀▄░░░░░░░░█▄░░")
            print("     ░░▄████▀███▄▀▄░░░░░░███▄▄▄▄░░█░░")
            print("     ░▄█████▄████░██░░░▄███▄▄░▀█▀░░█░")
            print("     ▄███████▀▀░█░▄█░▄███▀█████░█░░▀▄")
            print("     █░█▀██▄▄▄▄█▀░█▀█▀██████▀░██▀█░░█")
            print("     █░█░▀▀▀▀▀░░░█▀░█░███▀▀░░▄█▀░█░░█")
            print("     █░░█▄░░░░▄▄▀░░░█░▀██▄▄▄██▀░░█▄░█")
            print("     █░░░░▀█▀▀▀░░░░░░█░░▀▀▀▀░░░░▄█░░█")
            print("     █░░░░░░░░░░░░░░░░▀▄░░░░░░▄█▀░░░█")
            print("     ░█░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▄░░░░█░")
            print("     ░░█░░░░░░▄▄▄▄▄▄▄░░░░░░░░░░░░░▄▀░")
            print("     ░░░▀▄░░░░░▀█▄░░░▀▀██▄░░░░░░░▄▀░░")
            print("     ░░░░░▀▄▄░░░░░▀▀▀▀▀░░░░░░░░▄▀░░░░")
            print("     ░░░░░░░░▀▀▄▄▄░░░░░░░░▄▄▄▀▀█░░░░░")
            print("     ░░░░░░░░░░▄▀▀█████▀▀▀▀░░░░██░░░░")
            print("     ░░░░░░░░░█░░░██░░░█▀▀▀▀▀▀▀▀█░░░░")





            # -----------------------------------------------------CASA 15----------------------------------------------------------------
    elif posicao_jogador2 == 15:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                     ▒▄█░▒█▀▀                     █")
        print(" █                     ░▒█░▒▀▀▄                     █")
        print(" █                     ▒▄█▄▒▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")








    # -----------------------------------------------------CASA 16------------------------------------------------------------------              
    elif posicao_jogador2 == 16:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █     Aproveite que o uma tentativa de impeachment   █")
        print(" █       contra você passou, e pensando que           █")
        print(" █        toda vitória deve ser comemorada            █")
        print(" █                    ▒▄█░▒▄▀▀▄                       █")
        print(" █                    ░▒█░▒█▄▄░                       █")
        print(" █                    ▒▄█▄▒▀▄▄▀                       █")         
        print(" █                                                    █")
        print(" █   Encene um trecho de filme para todos da sala     █")
        print(" █             e avance 3 casas.                      █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa")
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")
            
        else:
            posicao_jogador2 += 3
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")            






            # ------------------------------------------------------CASA 17----------------------------------------------------------------
    elif posicao_jogador2 == 17:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                    ▒▄█░▒▀▀█                      █")
        print(" █                    ░▒█░░▒█░                      █")
        print(" █                    ▒▄█▄▒▐▌░                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")








    # -----------------------------------------------------CASA 18------------------------------------------------------------------              
    elif posicao_jogador2 == 18:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █  Você recebe o presidente boliviano que te acursou █")
        print(" █  de golpista isso pega mal para seus partidários,  █")
        print(" █                                                    █")
        print(" █                  ▒▄█░▒▄▀▀▄                         █")
        print(" █                  ░▒█░▒▄▀▀▄                         █")
        print(" █                  ▒▄█▄▒▀▄▄▀                         █")         
        print(" █                                                    █")
        print(" █     você agora tem que ligar para uma pesssoa por  █")
        print(" █           whatssap até que ela atenda.             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 






            # ------------------------------------------------------CASA 19-----------------------------------------------------------------
    elif posicao_jogador2 == 19:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                    ▒▄█░▒▄▀▀▄                     █")
        print(" █                    ░▒█░▒▀▄▄▀                     █")
        print(" █                    ▒▄█▄▒▒▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")





    # -----------------------------------------------------CASA 20------------------------------------------------------------------
    elif posicao_jogador2 == 20:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █              Nada para ser feito aqui              █")
        print(" █                                                    █")
        print(" █                    ▒▄▀▄▒▄▀▀▄                       █")
        print(" █                    ░▒▄▀▒█ ▒█                       █")
        print(" █                    ▒█▄▄▒▀▄▄▀                       █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █             Espere sua próxima jogada              █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")




    # -----------------------------------------------------CASA 21------------------------------------------------------------------
    elif posicao_jogador2 == 21:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █  Seus movimentos politicos chamaram a atenção da █")
        print(" █     OAB, não seja covarde,finja que está na      █")
        print(" █                                                  █")
        print(" █                    ▒▄▀▄▒▄█░                      █")
        print(" █                    ░▒▄▀░▒█░                      █")
        print(" █                    ▒█▄▄▒▄█▄                      █")         
        print(" █                                                  █")
        print(" █          balada e mostre como você               █")
        print(" █         faria para chegar em alguém.             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio\n")
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 





            # ------------------------------------------------------CASA 22-----------------------------------------------------------------
    elif posicao_jogador2 == 22:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █  Maia afirma que vai rejeitar os 25 pedidos de     █")
        print(" █   impeachment que existem contra você, pessa para  █")
        print(" █ fazer um discurso chamando a atenção de todos onde █")
        print(" █                   ▒▄▀▄▒▄▀▄                         █")
        print(" █                   ░▒▄▀░▒▄▀                         █")
        print(" █                   ▒█▄▄▒█▄▄                         █")         
        print(" █                                                    █")
        print(" █     você se encontra, agradeça essa vitória        █")
        print(" █             e avance duas casas                    █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa\n")
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")
        else:
            posicao_jogador2 += 2
            print("Você avançou 2 casas, por ter cumprido o desafio\n")
            
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 





            # -------------------------------------------------------CASA 23----------------------------------------------------------------
    elif posicao_jogador2 == 23:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █   O DEM do Maia quer se aliar ao PSDB do Aécio,  █")
        print(" █  cante uma canção de ninar para que o Maia durma █")
        print(" █                                                  █")
        print(" █                    ▒▄▀▄▒▄▀▀▄                     █")
        print(" █                    ░▒▄▀░░▒▀▌                     █")
        print(" █                    ▒█▄▄▒▀▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █   e você consiga manter sua coligação com o PSDB █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 



            # -------------------------------------------------------CASA 24----------------------------------------------------------------
    elif posicao_jogador2 == 24:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █             Nada para ser feito aqui               █")
        print(" █                                                    █")
        print(" █                  ▒▄▀▄░▒▄▀█░                        █")
        print(" █                  ░▒▄▀▒█▄▄█▄                        █")
        print(" █                  ▒█▄▄░░░▒█░                        █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █           espere sua próxima jogada                █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")





    # --------------------------------------------------------CASA 25------------------------------------------------------------------
    elif posicao_jogador2 == 25:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                    ▒▄▀▄▒█▀▀                      █")
        print(" █                    ░▒▄▀▒▀▀▄                      █")
        print(" █                    ▒█▄▄▒▄▄▀                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("\n\n   ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")



    # -----------------------------------------------------CASA 26------------------------------------------------------------------
    elif posicao_jogador2 == 26:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ Você escapa de uma investigação do STF, derrotando █")
        print(" █ o inimigo sem lutar; seu adversário terá que fazer █")
        print(" █ quantas flexões                                    █")
        print(" █                  ▒▄▀▄▒▄▀▀▄                         █")
        print(" █                  ░▒▄▀▒█▄▄░                         █")
        print(" █                  ▒█▄▄▒▀▄▄▀                         █")         
        print(" █                                                    █")
        print(" █   ele aguentar em 1 minuto e você avança 1 casas,  █")
        print(" █    se ele não fizer, voltará tres.                 █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        posicao_jogador2 += 1

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n")             





            # -------------------------------------------------------CASA 27----------------------------------------------------------------
    elif posicao_jogador2 == 27:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                    ▒▄▀▄▒▀▀█                      █")
        print(" █                    ░▒▄▀░▒█░                      █")
        print(" █                    ▒█▄▄▒▐▌░                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")





    # -------------------------------------------------------CASA 28------------------------------------------------------------------
    elif posicao_jogador2 == 28:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ Maia o acusa de tentar enfraquecer o DEM, troque o █")
        print(" █     status de relacionamento do Facebook, para     █")
        print(" █            demonstrar sua lealdade,                █")
        print(" █                   ▒▄▀▄▒▄▀▀▄                        █")
        print(" █                   ░▒▄▀▒▄▀▀▄                        █")
        print(" █                   ▒█▄▄▒▀▄▄▀                        █")         
        print(" █                                                    █")
        print(" █     senão seu adversário avançará duas casas,      █")
        print(" █           além das 3 que você voltará              █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            posicao_jogador1 += 2
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("         ░░░░░░░░███████████████░░░░░░░░")
            print("         ░░░░░█████████████████████░░░░░")
            print("         ░░░░████████████████████████░░░")
            print("         ░░░██████████████████████████░░")
            print("         ░░█████████████████████████████")
            print("         ░░███████████▀░░░░░░░░░████████")
            print("         ░░███████████░░░░░░░░░░░░░░░███")
            print("         ░████████████░░░░░░░░░░░░░░░░██")
            print("         ░█░░███████░░░░░░░░░░░▄▄░░░░░██")
            print("         █░░░░█████░░░░░░▄███████░░██░░█")
            print("         █░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
            print("         █░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
            print("         █░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
            print("         █░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
            print("         ░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
            print("         ░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
            print("         ░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
            print("         ░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
            print("         ░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
            print("         ░░░██░░░░░░░█░░▀████████░░█░░░░")
            print("         ░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
            print("         ░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
            print("         ░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
            print("         ░░░░░░░░░░░░░░░░████████░░░░░░░\n\n") 
    
    
    
    
    
                # --------------------------------------------------------CASA 29---------------------------------------------------------------
    elif posicao_jogador2 == 29:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ O doleiro Lúcio Funaro afirmou em sua delação que█")
        print(" █ você sabia do esquema na Caixa Econômica Federal,█")
        print(" █          isso enfraquece sua imgem politica,     █")
        print(" █                    ▒▄▀▄▒▄▀▀▄                     █")
        print(" █                    ░▒▄▀▒▀▄▄▀                     █")
        print(" █                    ▒█▄▄▒▒▄▄▀                     █")         
        print(" █                                                  █")
        print(" █      você deve ficar sem olhar o celular         █")
        print(" █  até o final do jogo, para tentar repara-la.     █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio será realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio\n")
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")
    
    
    
    
    
                # ---------------------------------------------------------CASA 30------------------------------------------------------------
    elif posicao_jogador2 == 30:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █           Nada para ser feito aqui,                █")
        print(" █                                                    █")
        print(" █                   ▒▄▀▀▄▒▄▀▀▄                       █")
        print(" █                   ░░▒▀▌▒█ ▒█                       █")
        print(" █                   ▒▀▄▄▀▒▀▄▄▀                       █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █             espere sua próxima jogada              █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")

    
    
    
    
    
    
    
        # ---------------------------------------------------------CASA 31------------------------------------------------------------------
    elif posicao_jogador2 == 31:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █   A oposição faz nova tentativa falha no STF de  █")
        print(" █  fatiar a votação da denúncia contra você e seus █")
        print(" █        ministros,  validando sua autoridade;     █")
        print(" █                   ▒▄▀▀▄▒▄█░                      █")
        print(" █                   ░░▒▀▌░▒█░                      █")
        print(" █                   ▒▀▄▄▀▒▄█▄                      █")         
        print(" █                                                  █")
        print(" █   seu adversário deve postar uma foto feia dele  █")
        print(" █ nas redes sociais,enquanto você anda duas casas. █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
    
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        posicao_jogador2 += 2
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador1 -= 3
            print("Seu adversário voltou 3 casas, por não ter cumprido o desafio enquanto você avança duas")
            
        else:
            print("┐└┐└┐└┐└┐└┐└┐└┐└┐└┐┐▌▌┐└┐└┐└┐└┐└┐└┐└┐└┐└")
            print("└┐└┐└┐└┐└┐└┐└┐└▌██████████▌┐└┐└┐└┐└┐└┐└┐")
            print("┐└┐└┐└┐└┐└┐└┐█████▌┐┐┐┐▌████▌└┐└┐└┐└┐└┐└")
            print("└┐└┐└┐└┐└┐└┐███┐└┐└┐└┐└┐└▌▌███▌┐└┐└┐└┐└┐")
            print("┐└┐└┐└┐└┐└┐██┐┐└┐└┐└┐└▌████▌▌███┐└┐└┐└┐└")
            print("└┐└┐└┐└┐████└┐└┐└┐└┐└█▌┐└▌██▌████┐└┐└┐└┐")
            print("┐└┐└┐└┐████└┐└┐└┐└┐└┐▌███▌┐▌█▌████┐└┐└┐└")
            print("└┐└┐└┐█████▌└┐└┐└┐┐┐└┐██▌██┐▌█▌███▌┐└┐└┐")
            print("┐└┐└┐███████┐└┐└┐└┐└┐└┐▌████▌██████┐┐└┐└")
            print("└┐└┐█████▌█┐└┐└┐└┐┐┐┐▌▌┐└██▌██████▌█└┐└┐")
            print("┐└┐▌███▌┐▌┐└┐█┐└┐└┐▌▌▌███▌██████████▌└┐└")
            print("└┐└██▌▌┐█┐▌█▌██┐└█└┐██▌████████████▌▌┐└┐")
            print("┐└▌██┐┐█┐▌█▌███▌┐▌█┐┐██▌████████████▌┐┐└")
            print("└┐██▌┐▌▌└████▌██▌▌██▌┐██████████████▌▌└┐")
            print("┐┐██┐└█└█████└████▌███┐███████████████┐└")
            print("└███┐▌▌▌█████┐└████████▌▌█████████████▌┐")
            print("┐███┐███████▌└┐▌███████████████████████└")
            print("▌██▌┐███████└┐└┐▌██████████████████████┐")
            print("███▌████████┐└┐┐┐▌█████████████████████┐")
            print("███▌███████┐└┐▌▌└┐▌████████████████████▌")
            print("███▌███████└┐▌▌└┐└┐▌████▌██████████████▌")
            print("██████████┐┐▌┐└┐└┐└┐▌█▌▌└┐└┐└▌██████████")
            print("█████████┐┐└┐└▌└┐└┐└┐└┐└┐└┐└┐└┐▌████████")
            print("████████▌┐└▌██████▌┐└┐└┐└┐└┐└┐└┐▌███████")
            print("████████┐└┐██████▌██┐└┐└┐└┐▌███┐┐███████")
            print("████████▌▌███┐███┐└█▌┐└┐└┐██└███└┐██████")
            print("███████▌┐┐████▌▌██▌└█└┐└┐▌██▌█▌└┐└██████")
            print("███████┐└┐└┐└┐└┐└┐███┐└┐└███▌┐└┐└┐┐█████")
            print("███████└┐└┐└┐└┐└┐└┐▌┐└┐└┐█┐└┐└┐└┐└┐▌████")
            print("███████┐└┐└┐└┐└┐└┐└┐└┐└┐└▌└┐└┐└┐└┐└┐▌███")
            print("███████└▌┐┐└┐└┐└┐└┐└┐└┐└┐█┐└┐└┐└┐└┐└┐███")
            print("███████┐██└┐└┐└┐└┐┐┐└┐└┐└█▌┐└┐└┐└┐└┐└███")
            print("███████└██▌└┐└┐└┐└┐└┐└┐└┐┐█└┐└┐└┐┐┐└┐███")
            print("███████┐█▌█┐└┐└┐└┐└┐└┐└┐└┐█▌└┐└┐┐█▌┐└███")
            print("███████└█└██┐└┐└┐└▌▌┐└┐└┐└█▌┐└┐└▌█┐└▌███")
            print("██████▌┐██└██┐└┐└┐██┐█▌┐└┐█┐└┐└┐██└┐████")
            print("███████└▌█┐└██▌└┐└▌▌┐▌┐└┐██└┐└┐└█▌┐└███▌")
            print("███████┐└██▌┐███▌┐└┐└┐└┐└█▌┐└┐└██▌└┐███▌")
            print("███████└┐████└▌████┐┐└┐└┐└┐└┐┐█▌█▌┐┐███▌")
            print("███████┐└▌████└┐└███████┐┐┐▌███┐█┐└▌███┐")
            print("███████└┐└█████└┐└┐└┐└▌████▌┐└┐└█┐┐▌███└")
            print("███████┐└┐▌██████▌└┐└┐└┐└▌└┐└┐└┐█┐└████┐")
            print("███████└┐└┐████████└┐└▌└┐└┐└┐▌▌██└┐████└")
            print("███████┐└┐└██▌██████████▌████████┐└████┐")
            print("▌██████▌┐└┐└█└┐└█████████████████└┐████└")
            print("▌███████└┐└┐┐█└┐┐█▌██████████████┐└████┐")
            print("▌███████┐└┐└┐██└┐└┐└┐██████████▌█└┐████└")
            print("└███████▌┐└┐└┐██▌┐└┐└┐└┐└▌└┐█▌└┐█┐└████┐")
            print("┐▌█████▌▌└┐└┐└┐▌██┐└┐└┐└┐└┐└┐└┐┐█└┐████└")
            print("└▌██████└█└┐└┐└┐└███▌┐└┐└┐└┐└┐┐█▌┐└████┐")
            print("┐▌██████┐█▌└┐└┐┐▌└┐█████▌▌▌████▌┐▌┐████└")
            print("└┐██████└┐█┐└┐└┐██└┐└┐▌██████▌└┐┐▌└████┐")
            print("┐└██████▌└▌█┐└┐└┐██▌┐└┐└┐└┐└┐└┐└█└┐████└")
            print("└┐██████▌┐└██┐└┐┐┐┐██▌└┐└┐└┐└┐└██┐▌████┐")
            print("┐└▌██████└┐└██┐└┐└┐└▌████▌┐┐┐███┐└▌████└")
            print("└┐└██████┐└┐└██┐└┐└┐└┐┐▌██████▌┐└┐█████┐")
            print("┐└┐██████└┐└┐└██▌└┐└┐└┐└┐└┐└┐└┐└┐└███▌█└")
            print("└┐└██████▌└┐└┐└▌██└┐└┐└┐└┐└┐└┐└┐└████▌█┐")
            print("┐└┐██▌█▌█▌┐└┐└┐└┐██┐┐└┐└┐└┐└┐└┐└┐█┐██└█└")
            print("└┐└██▌█▌██└┐└┐└┐└┐▌██▌└┐└┐└┐└┐└┐┐█└██┐█┐")
            print("┐└┐██▌█▌██┐└┐└┐└┐└┐└███▌┐└┐└┐└┐└█▌┐▌█└▌┐")
            print("└┐└▌██▌┐██└┐└┐└┐└┐└┐└┐▌██▌▌┐└┐┐██┐└┐▌┐▌┐")
            print("┐└┐▌█▌▌└██┐└┐└┐└┐└┐└┐└┐└┐██████▌┐└┐┐▌└┐┐")
            print("└┐└┐█▌▌┐██▌┐└┐└┐└┐└┐└┐└┐└┐└▌▌▌└┐└┐└┐┐┐└┐")
            print("┐└┐└█▌┐└▌█▌└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└?")
        
        
    
        # -----------------------------------------------------------CASA 32------------------------------------------------------------
    elif posicao_jogador2 == 32:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █           Nada para ser feito aqui,                █")
        print(" █                                                    █")
        print(" █                 ▒▄▀▀▄▒▄▀▄                          █")
        print(" █                 ░░▒▀▌░▒▄▀                          █")
        print(" █                 ▒▀▄▄▀▒█▄▄                          █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █          espere sua próxima jogada                 █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 33------------------------------------------------------------------
    elif posicao_jogador2 == 33:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                   ▒▄▀▀▄▒▄▀▀▄                     █")
        print(" █                   ░░▒▀▌░░▒▀▌                     █")
        print(" █                   ▒▀▄▄▀▒▀▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 34------------------------------------------------------------------              
    elif posicao_jogador2 == 34:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █A Procuradoria da República não obteve provas contra█")
        print(" █  você, mas deixou insubordinação na base aliada;   █")
        print(" █  lembre do conselho:Quando incapaz finja-se capaz” █")
        print(" █                  ▒▄▀▀▄░▒▄▀█░                       █")
        print(" █                  ░░▒▀▌▒█▄▄█▄                       █")
        print(" █                  ▒▀▄▄▀░░░▒█░                       █")         
        print(" █           saia da sala e fassa um elogio           █")
        print(" █             a uma pessoa desconhecida,             █")
        print(" █            para demonstrar sua audácia             █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
            print("░░░░░░░░░░░░░░░░░░░▒▓▓█████████████▓▓▒░░░░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░▒████▓▓▒▒░▒▒▒░▒▒▒▒▒▒▓▓████▓▒░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░▒███▓░░░░░░░░░░░░░░░░░░░░░░▒███████▓▓▒░░░░░░░░░░░")
            print("░░░░░░░░░▒██▓░░░░▒▒███▓▓▒░░░░░░░░░░░░░▓▓▒▒▒▒▒▓██████▓░░░░░░░")
            print("░░░░░░░▒██▓░░░▓███▓▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▓▓███▓████▒▒░░░")
            print("░░░░░░██▓░░▒▓██▓░░▒▓██████▓░░░░░░░▒░░░░░░▒██▓▒░░░▓███▒▓▒░░░░")
            print("░░░░░██░░▓███▒░░▒██▒░░░░▒▒██▓░░░░░░░░░░░██▒░░░░▒████▒█░░░░░░")
            print("░░░░██░▒▓▒▓▓░░░██░░░░░░░░░░░█▓░░░░░░░░░██░░░░░░▒███░░█▒░░░░░")
            print("░░░▓█░░░░░░░░░██░░░░░░░░░░░░▓█░░░░░░░░██░░░░░░░░░░░░░█▒░░░░░")
            print("░░░█▓░░░░░░░░░█▒░░████░░░░░░░█▒░░░░░░░██░░░░░░░░░░░░███░░░░░")
            print("░░▒█░░░░░░░▒▓▒█▓░▓████▓░░░░░▒█░░░░░░░░▒█▒░░░░░░░░░░██░█▒░░░░")
            print("░░██░░░░░▒▓▒▓▒██▒▒▓▓▓░░░░░░░██░░░░░░░░░▒████▓███████▓░█▒░░░░")
            print("░░█▓░░░░░▒░░░▒░▒██▓▒░░░░░▒██▓░░░░░░░░░░░░░░██▓░░░░░░▒██▓░░░░")
            print("░░█░░░░░░░░░▓▒░░░░▒▓██████▓░░░░░░░░░░░░░░▒██░░░▓█▓▓▒░░░██░░░")
            print("░▒█░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒▓▒▒▒▒▒▓▓▓▓██░░▓█▓░▒▒██▒░░██░░")
            print("░▓█░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▒░░██░░██▓░▒░▒░██░░▒█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░▒▓▒▒▒▒▒▒▒▒░░░██░░▓█░█▓░█▒█▓█▓░░█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░▒▒░░▓█▓░░██░█▒▒█▒█▒▓█░░█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░▓█░░░█▒░░░░▒▒░░▒█░▓█░░")
            print("░▒█░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░█▒░░█▒░░░░░░░░▓█░█▓░░")
            print("░░█▓░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█░░█▒░░░░░░░░█░▒█░░░")
            print("░░▓█░░▒░░▒▒░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░░█▓░█▓░░░")
            print("░░░█▒░░▒░░▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░▓█░░█░░░░")
            print("░░░██░░░▒░▒░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░██░░█░░░░")
            print("░░░░█▓░░░▒░▒░░░░▒▒░░░░░▒▒▒▒▒▒░░░░░░░░░░▒█░▒█░░░░░░░█▒░░█▓░░░")
            print("░░░░▓█░░░░▒▒░░░░░▒▒░░░░░░▒▒▒▓▓▓▒░░░░░░░██░██░░░░░░░██░░▓█░░░")
            print("░░░░░██░░░▒░▒░░░░░▒░░░░░░░░▒░▒▒▓█▒░░░░▒█░░█▓▒▓▓▓▒░░▓█░░░█▒░░")
            print("░░░░░▒█▒░░░▒▒▒░░░░▒░░░░░░░░░░▒▒▒░▒▓░░░██░▒█░░░░▒▓▓░░██░░█▒░░")
            print("░░░░░░▒█▒░░░▒░▒░░░▒░░░░░░▒▒▒░░░░▒▒░░░▒█░░██░░░░░░░█░▒█░░█▒░░")
            print("░░░░░░░▓█░░░▒░▒░░░░▒▒░░░░▓▒▒▓▓▓▒░░▓▒░██░░██▒▒▒▒▓▒▓▓███░░█▒░░")
            print("░░░░░░░░██░░░▒░▒░░░░░▒▒░░░░░░░░▓█▓░░░█▓░░██░▓█░█░█░░█▒░░█▒░░")
            print("░░░░░░░░░██░░░░▒▒░░░░░░▒▒░░░░░░░░▒█▓░█▓░░▓█▒▒█▒█░█▒██░░▒█░░░")
            print("░░░░░░░░░░██▒░░░░▒░░░▒░░░▒▒░░░░░░░░▒▓██░░░██░░░░▒▒██░░░██░░░")
            print("░░░░░░░░░░░▓██░░░░░░░░▒▒░░░▒░░░░░░░░░▓█░░░░▓███▓▓██░░░██░░░░")
            print("░░░░░░░░░░░░░▓██▒░░░░░░▒▒▒▒▒░░░░░░░░░░██░░░░░░▒▒▒░░░░██░░░░░")
            print("░░░░░░░░░░░░░░░▓███▒░░░░░░░▒▒▒▒▒▒▒▒░░░░▓██▒░░░░░░░▒███░░░░░░")
            print("░░░░░░░░░░░░░░░░░▒▓███▓▒░░░░░░░▒░░▒▒▒▒░░░▒██▓██████▓░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░▒████▓▒▒░░░░░░░░░░░░░░░▓██▒░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░▒▓████▓░░░░░░░▓█████▒░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█████████▒░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░")


        else:
            print("     ░░░░░░░░░░▄▄█▀▀▀▀▀▀▀▀█▄▄░░░░░░░░")
            print("     ░░░░░░░▄▄▀▀░░░░░░░░░░░░▀▀▄▄░░░░░")
            print("     ░░░░░▄█▀░░░░▄▀░░░░▄░░░░░░░▀█░░░░")
            print("     ░░░░██▄▄████░░░░░░▀▄░░░░░░░░█▄░░")
            print("     ░░▄████▀███▄▀▄░░░░░░███▄▄▄▄░░█░░")
            print("     ░▄█████▄████░██░░░▄███▄▄░▀█▀░░█░")
            print("     ▄███████▀▀░█░▄█░▄███▀█████░█░░▀▄")
            print("     █░█▀██▄▄▄▄█▀░█▀█▀██████▀░██▀█░░█")
            print("     █░█░▀▀▀▀▀░░░█▀░█░███▀▀░░▄█▀░█░░█")
            print("     █░░█▄░░░░▄▄▀░░░█░▀██▄▄▄██▀░░█▄░█")
            print("     █░░░░▀█▀▀▀░░░░░░█░░▀▀▀▀░░░░▄█░░█")
            print("     █░░░░░░░░░░░░░░░░▀▄░░░░░░▄█▀░░░█")
            print("     ░█░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▄░░░░█░")
            print("     ░░█░░░░░░▄▄▄▄▄▄▄░░░░░░░░░░░░░▄▀░")
            print("     ░░░▀▄░░░░░▀█▄░░░▀▀██▄░░░░░░░▄▀░░")
            print("     ░░░░░▀▄▄░░░░░▀▀▀▀▀░░░░░░░░▄▀░░░░")
            print("     ░░░░░░░░▀▀▄▄▄░░░░░░░░▄▄▄▀▀█░░░░░")
            print("     ░░░░░░░░░░▄▀▀█████▀▀▀▀░░░░██░░░░")
            print("     ░░░░░░░░░█░░░██░░░█▀▀▀▀▀▀▀▀█░░░░")
    
    
    
    
    
    # ------------------------------------------------------CASA 35-----------------------------------------------------------------
    elif posicao_jogador2 == 35:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui,            █")
        print(" █                                                  █")
        print(" █                   ▒▄▀▀▄▒█▀▀                      █")
        print(" █                   ░░▒▀▌▒▀▀▄                      █")
        print(" █                   ▒▀▄▄▀▒▄▄▀                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 36------------------------------------------------------------------
    elif posicao_jogador2 == 36:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █           Nada para ser feito aqui,                █")
        print(" █                                                    █")
        print(" █                 ▒▄▀▀▄▒▄▀▀▄                         █")
        print(" █                 ░░▒▀▌▒█▄▄░                         █")
        print(" █                 ▒▀▄▄▀▒▀▄▄▀                         █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █           Espere sua próxima jogada                █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
        
        # -----------------------------------------------------CASA 37------------------------------------------------------------------
    elif posicao_jogador2 == 37:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █      Você articula e ajuda seu broder Aécio,     █")
        print(" █    conseguindo votos no Senado para barrar o     █")
        print(" █afastamento dele;está foi uma grande vitória para █")
        print(" █                   ▒▄▀▀▄▒▀▀█                      █")
        print(" █                   ░░▒▀▌░▒█░                      █")
        print(" █                   ▒▀▄▄▀▒▐▌░                      █")         
        print(" █   sua aliança politica entre seu partido (PSDB)  █")
        print(" █  e o dele(PMDB) escolha um desafio que você já   █")
        print(" █   cumprido e seu adversário deverá faze-lo       █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        
        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O seu adversário cumpriu o desafio? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("┐└┐└┐└┐└┐└┐└┐└┐└┐└┐┐▌▌┐└┐└┐└┐└┐└┐└┐└┐└┐└")
            print("└┐└┐└┐└┐└┐└┐└┐└▌██████████▌┐└┐└┐└┐└┐└┐└┐")
            print("┐└┐└┐└┐└┐└┐└┐█████▌┐┐┐┐▌████▌└┐└┐└┐└┐└┐└")
            print("└┐└┐└┐└┐└┐└┐███┐└┐└┐└┐└┐└▌▌███▌┐└┐└┐└┐└┐")
            print("┐└┐└┐└┐└┐└┐██┐┐└┐└┐└┐└▌████▌▌███┐└┐└┐└┐└")
            print("└┐└┐└┐└┐████└┐└┐└┐└┐└█▌┐└▌██▌████┐└┐└┐└┐")
            print("┐└┐└┐└┐████└┐└┐└┐└┐└┐▌███▌┐▌█▌████┐└┐└┐└")
            print("└┐└┐└┐█████▌└┐└┐└┐┐┐└┐██▌██┐▌█▌███▌┐└┐└┐")
            print("┐└┐└┐███████┐└┐└┐└┐└┐└┐▌████▌██████┐┐└┐└")
            print("└┐└┐█████▌█┐└┐└┐└┐┐┐┐▌▌┐└██▌██████▌█└┐└┐")
            print("┐└┐▌███▌┐▌┐└┐█┐└┐└┐▌▌▌███▌██████████▌└┐└")
            print("└┐└██▌▌┐█┐▌█▌██┐└█└┐██▌████████████▌▌┐└┐")
            print("┐└▌██┐┐█┐▌█▌███▌┐▌█┐┐██▌████████████▌┐┐└")
            print("└┐██▌┐▌▌└████▌██▌▌██▌┐██████████████▌▌└┐")
            print("┐┐██┐└█└█████└████▌███┐███████████████┐└")
            print("└███┐▌▌▌█████┐└████████▌▌█████████████▌┐")
            print("┐███┐███████▌└┐▌███████████████████████└")
            print("▌██▌┐███████└┐└┐▌██████████████████████┐")
            print("███▌████████┐└┐┐┐▌█████████████████████┐")
            print("███▌███████┐└┐▌▌└┐▌████████████████████▌")
            print("███▌███████└┐▌▌└┐└┐▌████▌██████████████▌")
            print("██████████┐┐▌┐└┐└┐└┐▌█▌▌└┐└┐└▌██████████")
            print("█████████┐┐└┐└▌└┐└┐└┐└┐└┐└┐└┐└┐▌████████")
            print("████████▌┐└▌██████▌┐└┐└┐└┐└┐└┐└┐▌███████")
            print("████████┐└┐██████▌██┐└┐└┐└┐▌███┐┐███████")
            print("████████▌▌███┐███┐└█▌┐└┐└┐██└███└┐██████")
            print("███████▌┐┐████▌▌██▌└█└┐└┐▌██▌█▌└┐└██████")
            print("███████┐└┐└┐└┐└┐└┐███┐└┐└███▌┐└┐└┐┐█████")
            print("███████└┐└┐└┐└┐└┐└┐▌┐└┐└┐█┐└┐└┐└┐└┐▌████")
            print("███████┐└┐└┐└┐└┐└┐└┐└┐└┐└▌└┐└┐└┐└┐└┐▌███")
            print("███████└▌┐┐└┐└┐└┐└┐└┐└┐└┐█┐└┐└┐└┐└┐└┐███")
            print("███████┐██└┐└┐└┐└┐┐┐└┐└┐└█▌┐└┐└┐└┐└┐└███")
            print("███████└██▌└┐└┐└┐└┐└┐└┐└┐┐█└┐└┐└┐┐┐└┐███")
            print("███████┐█▌█┐└┐└┐└┐└┐└┐└┐└┐█▌└┐└┐┐█▌┐└███")
            print("███████└█└██┐└┐└┐└▌▌┐└┐└┐└█▌┐└┐└▌█┐└▌███")
            print("██████▌┐██└██┐└┐└┐██┐█▌┐└┐█┐└┐└┐██└┐████")
            print("███████└▌█┐└██▌└┐└▌▌┐▌┐└┐██└┐└┐└█▌┐└███▌")
            print("███████┐└██▌┐███▌┐└┐└┐└┐└█▌┐└┐└██▌└┐███▌")
            print("███████└┐████└▌████┐┐└┐└┐└┐└┐┐█▌█▌┐┐███▌")
            print("███████┐└▌████└┐└███████┐┐┐▌███┐█┐└▌███┐")
            print("███████└┐└█████└┐└┐└┐└▌████▌┐└┐└█┐┐▌███└")
            print("███████┐└┐▌██████▌└┐└┐└┐└▌└┐└┐└┐█┐└████┐")
            print("███████└┐└┐████████└┐└▌└┐└┐└┐▌▌██└┐████└")
            print("███████┐└┐└██▌██████████▌████████┐└████┐")
            print("▌██████▌┐└┐└█└┐└█████████████████└┐████└")
            print("▌███████└┐└┐┐█└┐┐█▌██████████████┐└████┐")
            print("▌███████┐└┐└┐██└┐└┐└┐██████████▌█└┐████└")
            print("└███████▌┐└┐└┐██▌┐└┐└┐└┐└▌└┐█▌└┐█┐└████┐")
            print("┐▌█████▌▌└┐└┐└┐▌██┐└┐└┐└┐└┐└┐└┐┐█└┐████└")
            print("└▌██████└█└┐└┐└┐└███▌┐└┐└┐└┐└┐┐█▌┐└████┐")
            print("┐▌██████┐█▌└┐└┐┐▌└┐█████▌▌▌████▌┐▌┐████└")
            print("└┐██████└┐█┐└┐└┐██└┐└┐▌██████▌└┐┐▌└████┐")
            print("┐└██████▌└▌█┐└┐└┐██▌┐└┐└┐└┐└┐└┐└█└┐████└")
            print("└┐██████▌┐└██┐└┐┐┐┐██▌└┐└┐└┐└┐└██┐▌████┐")
            print("┐└▌██████└┐└██┐└┐└┐└▌████▌┐┐┐███┐└▌████└")
            print("└┐└██████┐└┐└██┐└┐└┐└┐┐▌██████▌┐└┐█████┐")
            print("┐└┐██████└┐└┐└██▌└┐└┐└┐└┐└┐└┐└┐└┐└███▌█└")
            print("└┐└██████▌└┐└┐└▌██└┐└┐└┐└┐└┐└┐└┐└████▌█┐")
            print("┐└┐██▌█▌█▌┐└┐└┐└┐██┐┐└┐└┐└┐└┐└┐└┐█┐██└█└")
            print("└┐└██▌█▌██└┐└┐└┐└┐▌██▌└┐└┐└┐└┐└┐┐█└██┐█┐")
            print("┐└┐██▌█▌██┐└┐└┐└┐└┐└███▌┐└┐└┐└┐└█▌┐▌█└▌┐")
            print("└┐└▌██▌┐██└┐└┐└┐└┐└┐└┐▌██▌▌┐└┐┐██┐└┐▌┐▌┐")
            print("┐└┐▌█▌▌└██┐└┐└┐└┐└┐└┐└┐└┐██████▌┐└┐┐▌└┐┐")
            print("└┐└┐█▌▌┐██▌┐└┐└┐└┐└┐└┐└┐└┐└▌▌▌└┐└┐└┐┐┐└┐")
            print("┐└┐└█▌┐└▌█▌└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└┐└?")
    
    
    
    
    
    # -------------------------------------------------------CASA 38---------------------------------------------------------------
    
    if posicao_jogador2 == 38:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                     █")
        print(" █         Nada para ser feito aqui                    █")
        print(" █                                                     █")
        print(" █                 ▒▄▀▀▄▒▄▀▀▄                          █")
        print(" █                 ░░▒▀▌▒▄▀▀▄                          █")
        print(" █                 ▒▀▄▄▀▒▀▄▄▀                          █")         
        print(" █                                                     █")
        print(" █                                                     █")
        print(" █          Espere sua próxima jogada                  █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 39------------------------------------------------------------------
    if posicao_jogador2 == 39:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                   ▒▄▀▀▄▒▄▀▀▄                     █")
        print(" █                   ░░▒▀▌▒▀▄▄▀                     █")
        print(" █                   ▒▀▄▄▀▒▒▄▄▀                     █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 40------------------------------------------------------------------
    if posicao_jogador2 == 40:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █ A dívida pública avança 3,22% em junho desse ano,  █")
        print(" █sendo de R$ 3,35 trilhões;esse cenário econômico    █")
        print(" █prejudica sua imagem,pensando que sua postura deve  █")
        print(" █ser como a água  ░▒▄▀█░▒▄▀▀▄                        █")
        print(" █que não tem      ▒█▄▄█▄▒█ ▒█                        █")
        print(" █forma constante, ░░░▒█░ ▀▄▄▀                        █")         
        print(" █simule uma pedido de casamento para alguém que não  █")
        print(" █seja seu adversário, demonstrando sua flexibilidade,█")
        print(" █            com isso avançará 4 casas               █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio, além de perder o beneficio da casa\n")
            print("        ░░█▀░░░░░░░░░░░▀▀███████░░░░ ")
            print("        ░░█▌░░░░░░░░░░░░░░░▀██████░░░ ")
            print("        ░█▌░░░░░░░░░░░░░░░░███████▌░░ ")
            print("        ░█░░░░░░░░░░░░░░░░░████████░░ ")
            print("        ▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ ")
            print("        ░▌▄███▌░░░░▀████▄░░░░▀████▌░░ ")
            print("        ▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ ")
            print("        ▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ ")
            print("        ▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ ")
            print("        ▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ ")
            print("        ░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ ")
            print("        ░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ ")
            print("        ░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ ")
            print("        ░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ ")
            print("        ░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ ")
            print("        ░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ ")
            print("        ░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ ")
            print("        ░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ ")
            print("        ░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ ")
            print("        ▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ ")
            print("        ░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ ")
            print("        ░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ ")
            print("        ░░▄▌████████▄▄▄███████▌░░░░░▄ ")
            print("        ░▄▀░██████████████████▌▀▄░░░░ ")
            print("        ▀░░░█████▀▀░░░▀███████░░░▀▄░░ ")
            print("        ░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ ")
            print("        ░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ ")
            print("        ░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ ")
            print("        ░░░░░░╔╗░░╔═╗░╦═╗░░░░░░░░░░░░ ")
            print("        ░░░░░░╠╩╗░╠═╣░║░║░░░░░░░░░░░░ ")
            print("        ░░░░░░╚═╝░║░║░╩═╝░░░░░░░░░░░░ ")
        else:
            posicao_jogador2 += 4
            print("Parabéns, por ter cumprido o desafio você avançou 4 casas")
            print("░░░░░░░░░░░░░░░░░░░▒▓▓█████████████▓▓▒░░░░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░▒████▓▓▒▒░▒▒▒░▒▒▒▒▒▒▓▓████▓▒░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░▒███▓░░░░░░░░░░░░░░░░░░░░░░▒███████▓▓▒░░░░░░░░░░░")
            print("░░░░░░░░░▒██▓░░░░▒▒███▓▓▒░░░░░░░░░░░░░▓▓▒▒▒▒▒▓██████▓░░░░░░░")
            print("░░░░░░░▒██▓░░░▓███▓▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▓▓███▓████▒▒░░░")
            print("░░░░░░██▓░░▒▓██▓░░▒▓██████▓░░░░░░░▒░░░░░░▒██▓▒░░░▓███▒▓▒░░░░")
            print("░░░░░██░░▓███▒░░▒██▒░░░░▒▒██▓░░░░░░░░░░░██▒░░░░▒████▒█░░░░░░")
            print("░░░░██░▒▓▒▓▓░░░██░░░░░░░░░░░█▓░░░░░░░░░██░░░░░░▒███░░█▒░░░░░")
            print("░░░▓█░░░░░░░░░██░░░░░░░░░░░░▓█░░░░░░░░██░░░░░░░░░░░░░█▒░░░░░")
            print("░░░█▓░░░░░░░░░█▒░░████░░░░░░░█▒░░░░░░░██░░░░░░░░░░░░███░░░░░")
            print("░░▒█░░░░░░░▒▓▒█▓░▓████▓░░░░░▒█░░░░░░░░▒█▒░░░░░░░░░░██░█▒░░░░")
            print("░░██░░░░░▒▓▒▓▒██▒▒▓▓▓░░░░░░░██░░░░░░░░░▒████▓███████▓░█▒░░░░")
            print("░░█▓░░░░░▒░░░▒░▒██▓▒░░░░░▒██▓░░░░░░░░░░░░░░██▓░░░░░░▒██▓░░░░")
            print("░░█░░░░░░░░░▓▒░░░░▒▓██████▓░░░░░░░░░░░░░░▒██░░░▓█▓▓▒░░░██░░░")
            print("░▒█░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒▓▒▒▒▒▒▓▓▓▓██░░▓█▓░▒▒██▒░░██░░")
            print("░▓█░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▒░░██░░██▓░▒░▒░██░░▒█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░▒▓▒▒▒▒▒▒▒▒░░░██░░▓█░█▓░█▒█▓█▓░░█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░▒▒░░▓█▓░░██░█▒▒█▒█▒▓█░░█░░")
            print("░██░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░▓█░░░█▒░░░░▒▒░░▒█░▓█░░")
            print("░▒█░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░█▒░░█▒░░░░░░░░▓█░█▓░░")
            print("░░█▓░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█░░█▒░░░░░░░░█░▒█░░░")
            print("░░▓█░░▒░░▒▒░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░░█▓░█▓░░░")
            print("░░░█▒░░▒░░▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░▓█░░█░░░░")
            print("░░░██░░░▒░▒░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░█░░█▒░░░░░░██░░█░░░░")
            print("░░░░█▓░░░▒░▒░░░░▒▒░░░░░▒▒▒▒▒▒░░░░░░░░░░▒█░▒█░░░░░░░█▒░░█▓░░░")
            print("░░░░▓█░░░░▒▒░░░░░▒▒░░░░░░▒▒▒▓▓▓▒░░░░░░░██░██░░░░░░░██░░▓█░░░")
            print("░░░░░██░░░▒░▒░░░░░▒░░░░░░░░▒░▒▒▓█▒░░░░▒█░░█▓▒▓▓▓▒░░▓█░░░█▒░░")
            print("░░░░░▒█▒░░░▒▒▒░░░░▒░░░░░░░░░░▒▒▒░▒▓░░░██░▒█░░░░▒▓▓░░██░░█▒░░")
            print("░░░░░░▒█▒░░░▒░▒░░░▒░░░░░░▒▒▒░░░░▒▒░░░▒█░░██░░░░░░░█░▒█░░█▒░░")
            print("░░░░░░░▓█░░░▒░▒░░░░▒▒░░░░▓▒▒▓▓▓▒░░▓▒░██░░██▒▒▒▒▓▒▓▓███░░█▒░░")
            print("░░░░░░░░██░░░▒░▒░░░░░▒▒░░░░░░░░▓█▓░░░█▓░░██░▓█░█░█░░█▒░░█▒░░")
            print("░░░░░░░░░██░░░░▒▒░░░░░░▒▒░░░░░░░░▒█▓░█▓░░▓█▒▒█▒█░█▒██░░▒█░░░")
            print("░░░░░░░░░░██▒░░░░▒░░░▒░░░▒▒░░░░░░░░▒▓██░░░██░░░░▒▒██░░░██░░░")
            print("░░░░░░░░░░░▓██░░░░░░░░▒▒░░░▒░░░░░░░░░▓█░░░░▓███▓▓██░░░██░░░░")
            print("░░░░░░░░░░░░░▓██▒░░░░░░▒▒▒▒▒░░░░░░░░░░██░░░░░░▒▒▒░░░░██░░░░░")
            print("░░░░░░░░░░░░░░░▓███▒░░░░░░░▒▒▒▒▒▒▒▒░░░░▓██▒░░░░░░░▒███░░░░░░")
            print("░░░░░░░░░░░░░░░░░▒▓███▓▒░░░░░░░▒░░▒▒▒▒░░░▒██▓██████▓░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░▒████▓▒▒░░░░░░░░░░░░░░░▓██▒░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░▒▓████▓░░░░░░░▓█████▒░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█████████▒░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░")
    
    # --------------------------------------------------CASA 41---------------------------------------------------------------------
    if posicao_jogador2 == 41:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                  █")
        print(" █             Nada para ser feito aqui             █")
        print(" █                                                  █")
        print(" █                  ░▒▄▀█░▒▄█░                      █")
        print(" █                  ▒█▄▄█▄░▒█░                      █")
        print(" █                  ░░░▒█░▒▄█▄                      █")         
        print(" █                                                  █")
        print(" █                                                  █")
        print(" █             Espere sua próxima jogada            █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 42------------------------------------------------------------------
    if posicao_jogador2 == 42:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █A reforma da previdência que você colocou em pauta  █")
        print(" █foi aprovada, tendo em mente o pensamento “O gover- █")
        print(" █nante esclarecido estabeleceplanos a seguir”.       █")
        print(" █                ░▒▄▀█░▒▄▀▄                          █")
        print(" █                ▒█▄▄█▄░▒▄▀                          █")
        print(" █                ░░░▒█░▒█▄▄                          █")         
        print(" █  Passe uma rodada falando com algum sotaque ou em  █")
        print(" █                                                    █")
        print(" █               outro idioma.                        █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")
    
    
    
    
    
    
    # --------------------------------------------------------CASA 43---------------------------------------------------------------
    if posicao_jogador2 == 43:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █O TCU quer explicações suas sobre o 'esquema dos  █")
        print(" █portos', onde a empresa do seu amigo explora dês- █")
        print(" █de 1998, sendo os últimos 3 anos sem contrato,    █")
        print(" █                  ░▒▄▀█░▒▄▀▀▄                     █")
        print(" █                  ▒█▄▄█▄░░▒▀▌                     █")
        print(" █                  ░░░▒█░▒▀▄▄▀                     █")         
        print(" █    seja sútil, para não chamar a atenção dos     █")
        print(" █   jornalistas fique sem usar a palavra (não)     █")
        print(" █         até o final do jogo.                     █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    
    # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio será realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("    ░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
            print("    ░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
            print("    ░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
            print("    ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
            print("    ░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
            print("    ██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
            print("    █░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
            print("    █░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    █░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
            print("    █░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
            print("    █░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
            print("    ██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
            print("    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
            print("    ░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
            print("    ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
            print("    ░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
            print("    ░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
            print("    ░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
            print("    ░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
            print("    ░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
            print("    ░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░\n\n")
    
    
    
    
    
    # ---------------------------------------------------------CASA 44--------------------------------------------------------------
    if posicao_jogador2 == 44:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █          Nada para ser feito aqui                  █")
        print(" █                                                    █")
        print(" █               ░▒▄▀█░░▒▄▀█░                         █")
        print(" █               ▒█▄▄█▄▒█▄▄█▄                         █")
        print(" █               ░░░▒█░░░░▒█░                         █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █          Espere sua próxima jogada                 █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 45------------------------------------------------------------------
    if posicao_jogador2 == 45:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █      Você por meio de seus advogados, partiu     █")
        print(" █   para um ataque sem precedentes contra o ex-    █")
        print(" █  procurador-geral da República Rodrigo Janot,    █")
        print(" █                  ░▒▄▀█░▒█▀▀                      █")
        print(" █                  ▒█▄▄█▄▒▀▀▄                      █")
        print(" █                  ░░░▒█░▒▄▄▀                      █")         
        print(" █  com isso ganha poder sobre seu adversário e ele █")
        print(" █     deverá se desculpar na frente de todos       █")
        print(" █      da sala de aula, senão ele voltará 3 casas. █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

    
    # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 3 casas, por não ter cumprido o desafio")
        else:
            print("11111111111111111111111111111")                
            print("11111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")         
            print("1111111111¶¶¶¶¶111_________________¶¶")        
            print("11111111¶¶1_______1111______111_____¶¶")       
            print("111111¶¶______11_________11111111____¶1")      
            print("111111¶____11___1_____11______1111___1¶")      
            print("11111¶1___1_____1_____1_________1_____¶1")     
            print("11111¶__________________1¶¶¶¶1________1¶ ")    
            print("1111¶¶_____¶¶¶¶1______1¶¶_¶¶¶¶¶1_______¶¶ ")   
            print("111¶¶_1_1_¶¶¶¶¶¶¶_1___¶__1¶¶¶¶¶¶111____1¶¶  ") 
            print("111¶_1________11¶¶1___¶¶¶1__1_____1¶¶¶1__1¶  ") 
            print("11¶1__1¶¶1______11_____1____¶¶__1¶¶1__¶¶__1¶ ")
            print("11¶1__111¶¶¶¶___¶1___________1¶¶1___¶__¶1__¶ ")
            print("11¶1____1_11___¶¶_____1¶1_________¶¶¶1__¶__¶1")
            print("111¶_1__¶____1¶¶______11¶1_____1¶¶1_¶¶¶1¶__¶1")
            print("111¶1__¶¶___11¶¶____¶¶¶_¶___1¶¶¶1___¶__¶___¶1")
            print("111¶¶__¶¶¶1_____¶¶1_____11¶¶¶1_¶__1¶¶_____¶11")
            print("1111¶__¶¶1¶¶¶1___¶___1¶¶¶¶1____¶¶¶¶¶_____¶¶11")
            print("1111¶__¶_1__¶¶¶¶¶¶¶¶¶11__¶__1¶¶¶1_¶_____¶¶111")
            print("1111¶1_¶¶¶__1___¶___1____¶¶¶¶¶1¶_¶¶____¶¶1111")
            print("1111¶1_¶¶¶¶¶¶¶1¶¶11¶¶1¶¶¶¶¶1___1¶¶_____¶11111")
            print("1111¶1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_¶____¶¶_____¶¶11111")
            print("1111¶1_¶¶¶¶¶¶¶¶¶¶¶¶1¶1____¶__1¶¶______¶111111")
            print("1111¶__1¶¶_¶_¶__¶___11____1¶¶¶______1¶1111111")
            print("1111¶___¶¶1¶_11_11__1¶__1¶¶¶1___11_1¶11111111")
            print("1111¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1___11111¶¶111111111")
            print("1111¶__________11111_______111_1¶¶11111111111")
            print("1111¶_1__11____________1111__1¶¶1111111111111")
            print("1111¶__11__1________1111___1¶¶111111111111111")
            print("1111¶___1111_____________1¶¶11111111111111111")
            print("1111¶¶_______________11¶¶¶1111111111111111111")
            print("11111¶¶__________1¶¶¶¶¶1111111111111111111111")
            print("1111111¶¶¶¶¶¶¶¶¶¶¶111111111111111111111111111")
    
    
    
    
    
    
    
    # -------------------------------------------------------CASA 46----------------------------------------------------------------
    if posicao_jogador2 == 46:
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" █                                                    █")
        print(" █           Nada para ser feito aqui,                █")
        print(" █                                                    █")
        print(" █                ░▒▄▀█░▒▄▀▀▄                         █")
        print(" █                ▒█▄▄█▄▒█▄▄░                         █")
        print(" █                ░░░▒█░▒▀▄▄▀                         █")         
        print(" █                                                    █")
        print(" █                                                    █")
        print(" █           espere sua próxima jogada                █")
        print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        print("       ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░")
        print("       ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░")
        print("       ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░")
        print("       ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░")
        print("       ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░")
        print("       ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░")
        print("       ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░")
        print("       █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█")
        print("       █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█")
        print("       █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█")
        print("       █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█")
        print("       ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░")
        print("       ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░")
        print("       ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░")
        print("       ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░")
        print("       ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░")
    
    # -----------------------------------------------------CASA 47------------------------------------------------------------------
    if posicao_jogador2 == 47:
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("█Você foi denunciado pela WikiLeaks como informante█")
        print("█   da embaixada Americana no Brasil, invente uma  █")
        print("█           poesia que rime como a frase           █")
        print("█                  ░▒▄▀█░▒▀▀█                      █")
        print("█                  ▒█▄▄█▄░▒█░                      █")
        print("█                  ░░░▒█░▒▐▌░                      █")         
        print("█        'Tá tranquilo, Tio Sam, tá, tá...'        █")
        print("█            enquanto isso volte 8 casas           █")
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

        posicao_jogador2 -= 8
    
    # --------------------------------------Desafio cumprido?--------------------------------------------------
        desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): "))
        while desafio_feito != "SIM" and desafio_feito != "NÂO" and desafio_feito != "NAO":
            desafio_feito = str.upper(input("O desafio foi realizado? (sim/não): (Digite uma entrada válida!)"))
        if desafio_feito == "NÂO" or desafio_feito == "NAO":
            posicao_jogador2 -= 3
            print("Você voltou 11 casas, por não ter cumprido o desafio.\n")
            print("          ─────────────────────────▐█")
            print("          ────▄──────────────────▄█▓█")
            print("          ───▐██▄───────────────▄▓░░▓▓")
            print("          ───▐█░██▓────────────▓▓░░░▓▌")
            print("          ───▐█▌░▓██──────────█▓░░░░▓")
            print("          ────▓█▌░░▓█▄███████▄███▓░▓█")
            print("          ────▓██▌░▓██░░░░░░░░░░▓█░▓▌")
            print("          ─────▓█████░░░░░░░░░░░░▓██")
            print("          ─────▓██▓░░░░░░░░░░░░░░░▓█")
            print("          ─────▐█▓░░░░░░█▓░░▓█░░░░▓█▌")
            print("          ─────▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌")
            print("          ─────▓▓░▓██████▓░▓███▓▓▌░█▓")
            print("          ────▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██")
            print("          ────▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌")
            print("          ────▓█▌░▓█████▓░░░▓███▓▀░▓█▓")
            print("          ───▐▓█░░░▀▓██▀░░░░░─▀▓▀░░▓█▓")
            print("          ───▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓")
            print("          ───▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌")
            print("          ───▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓")
            print("          ──▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░██▓")
            print("          ──▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓")
            print("          ──██░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ──█▌░░░░░░░░░░░░░░░░░░░░░░░░▐▓▌")
            print("          ─▐▓░░░░░░░░░░░░░░░░░░░░░░░░░░█▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ─█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓")
            print("          ▐█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\n")




        print("\n\n")
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("            {}, SUA POSIÇÂO ATUAL É {} ")
        print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")    
        print("\n\n")

#=================================================FIM DE JOGO===========================================================
            





print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("█                                                                                            █")
print("█            ░▐█▀▀░▐██▒▐██▄▒▄██▌     ░▐█▀█▄░▐█▀▀     ░░▒██▌▒▐█▀▀█▌░▐█▀▀▀─▒▐█▀▀█▌             █")
print("█            ░▐█▀▀─░█▌░▒█░▒█░▒█░     ░▐█▌▐█░▐█▀▀     ▒▄▒▐█▌▒▐█▄▒█▌░▐█░▀█▌▒▐█▄▒█▌             █")
print("█            ░▐█──░▐██▒▐█░░░░▒█▌     ░▐█▄█▀░▐█▄▄     ▒████▌▒▐██▄█▌░▐██▄█▌▒▐██▄█▌             █")
print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")



if posicao_jogador1 > posicao_jogador2:
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("▄                                 ",nome_jogador1,"                                 ▄")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n")
 
    print("                                  ▀▀        █         █")
    print("             ▒▐▌▒▐▌▒▐█▀▀█▌░▐█▀█░▐█▀▀     ░▐█▀▀     ░▐█▀▀▒▐█▀█░▐██░▐█▀█▒▐█▀▀█▌")
    print("             ░▒█▒█░▒▐█▄▒█▌░▐█──░▐█▀▀     ░▐█▀▀     ░▐█▀▀▒▐█▄█─░█▌░▐█──▒▐█▄▒█▌")
    print("             ░▒▀▄▀░▒▐██▄█▌░▐█▄█░▐█▄▄     ░▐█▄▄     ░▐█▄▄▒▐█░░░▐██░▐█▄█▒▐██▄█▌\n")



    print(" '        ''   $$|   ''   ~       `'                     ''$$")
    print("               $S|                                         |$$   ,x$.")
    print("         $$%. l$$|                                         $$& .x$'")
    print("         `$$$.]$$'    .                                    $$.x$$'")
    print("           Y$$$$Y .x$$[                                   |$$$$")
    print("     m$Ax,. $$$$',$$$'                   .x$S       .xxxxx.$$$$$S$$$$x")
    print("     '$$$$$$$$$$$'    xSS$$$Sx.        x$$$' `S$S.  S$$$$$$$$$$$$$'~~~")
    print("        .$$$^`$$     :$SSSSSS$$$$$    S$$$$$$$$$$         ''$$$$.")
    print("      o$$$$  $%       .xSS$$$$$$$S ^^'#$^~'S$$$$$$x     f    ~'$$$x")
    print("  .o$$$#^     $%    $$$$$$~    '!        xXx$S$$$$$$x d'        S'")
    print("  $$$^        ^$%.  ~`:$$$>      '#&&Y'       .`$$$$$$$'")
    print("               ^$%.  a$$$$                     $#$$$$$$$.")
    print("                ^$.x%$$$$(                   .]$$$$$$$$$|")
    print("                 ^$$$$$$$.\                  ' $$$$$$$$$|")
    print("                  .$$$$$$$                   .$$$$$$x $")
    print("                 :$$^$$| '$x.    `S$$     ,xx'$$$$$$$")
    print("                   ~ $$$    ''SS$@$$S SS#'   $$$$| Y'")
    print("                     S  $x$x               .$")
    print("                    |$   $$$x      x     x$$")
    print("                     |    '$$$,   $$   @$',")
    print("                             $S. $$|  $ '")
    print("                             'S'.$$ $")
    print("                               |O$$  $S")
    print("                                |$$ $")
    print("                                |$[ $")
    print("                                `$| $")
    print("                                 `$d'")
    print("                                 x$$x")
    print("                               x$'YY 'x")
    print("                              $'   '  '$")
    print("                             $         $$")
    print("                           .$$|       '#$$.")
    print("                          x$$'           $x")
    print("                         $$$              $x")
    print("                        $$'.              '`$.f' .x..")
    print("                 xx$$$$$$$$$$x ,         $$$$$$$$$$$$:")
    print("                 `$$$$$#'   ''                '$$$$$$\n\n")

else:

    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("▄                                 ", nome_jogador2, "                                 ▄")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n")

    print("                                  ▀▀        █         █")
    print("             ▒▐▌▒▐▌▒▐█▀▀█▌░▐█▀█░▐█▀▀     ░▐█▀▀     ░▐█▀▀▒▐█▀█░▐██░▐█▀█▒▐█▀▀█▌")
    print("             ░▒█▒█░▒▐█▄▒█▌░▐█──░▐█▀▀     ░▐█▀▀     ░▐█▀▀▒▐█▄█─░█▌░▐█──▒▐█▄▒█▌")
    print("             ░▒▀▄▀░▒▐██▄█▌░▐█▄█░▐█▄▄     ░▐█▄▄     ░▐█▄▄▒▐█░░░▐██░▐█▄█▒▐██▄█▌\n")

    print(" '        ''   $$|   ''   ~       `'                     ''$$")
    print("               $S|                                         |$$   ,x$.")
    print("         $$%. l$$|                                         $$& .x$'")
    print("         `$$$.]$$'    .                                    $$.x$$'")
    print("           Y$$$$Y .x$$[                                   |$$$$")
    print("     m$Ax,. $$$$',$$$'                   .x$S       .xxxxx.$$$$$S$$$$x")
    print("     '$$$$$$$$$$$'    xSS$$$Sx.        x$$$' `S$S.  S$$$$$$$$$$$$$'~~~")
    print("        .$$$^`$$     :$SSSSSS$$$$$    S$$$$$$$$$$         ''$$$$.")
    print("      o$$$$  $%       .xSS$$$$$$$S ^^'#$^~'S$$$$$$x     f    ~'$$$x")
    print("  .o$$$#^     $%    $$$$$$~    '!        xXx$S$$$$$$x d'        S'")
    print("  $$$^        ^$%.  ~`:$$$>      '#&&Y'       .`$$$$$$$'")
    print("               ^$%.  a$$$$                     $#$$$$$$$.")
    print("                ^$.x%$$$$(                   .]$$$$$$$$$|")
    print("                 ^$$$$$$$.\                  ' $$$$$$$$$|")
    print("                  .$$$$$$$                   .$$$$$$x $")
    print("                 :$$^$$| '$x.    `S$$     ,xx'$$$$$$$")
    print("                   ~ $$$    ''SS$@$$S SS#'   $$$$| Y'")
    print("                     S  $x$x               .$")
    print("                    |$   $$$x      x     x$$")
    print("                     |    '$$$,   $$   @$',")
    print("                             $S. $$|  $ '")
    print("                             'S'.$$ $")
    print("                               |O$$  $S")
    print("                                |$$ $")
    print("                                |$[ $")
    print("                                `$| $")
    print("                                 `$d'")
    print("                                 x$$x")
    print("                               x$'YY 'x")
    print("                              $'   '  '$")
    print("                             $         $$")
    print("                           .$$|       '#$$.")
    print("                          x$$'           $x")
    print("                         $$$              $x")
    print("                        $$'.              '`$.f' .x..")
    print("                 xx$$$$$$$$$$x ,         $$$$$$$$$$$$:")
    print("                 `$$$$$#'   ''                '$$$$$$/n")
    print("                Existir não 'ser' se somente vive pra si")


time.sleep(5)
print("                De repente, você acorda em uma cama de palha...\n")
time.sleep(3)
print("             Você ouve gritos vindo do lado de fora da cabana...\n")
time.sleep(3)
print("      Você percebe que é o capataz chamando todos os escravos para trabalho ! \n")
time.sleep(3)
print("  Você então percebe que tudo foi um sonho, e acaba se conformando com a vida de cortador de cana. \n")





















    

