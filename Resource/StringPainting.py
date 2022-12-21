import random
import time
import colorama
from colorama import Fore, Back, Style

#pip install colorama

colorama.init()
colorama.init(autoreset=True)
ColorsList = []
PaintingCollect = []

class Colors:
    
    def ColorCollect():
    #ColorsList.append(Fore.GREEN)
        ColorsList.append(Fore.LIGHTRED_EX)       # pink
        ColorsList.append(Fore.BLUE)       # blue
        ColorsList.append(Fore.GREEN)       # green
        ColorsList.append(Fore.YELLOW)       # yellow
        ColorsList.append(Fore.RED)          # red
        ColorsList.append(Fore.CYAN)        #青色         # 
        ColorsList.append(Fore.RESET)     
        ColorsList.append(Fore.MAGENTA)    #品红
        ColorsList.append(Fore.LIGHTYELLOW_EX) 
        ColorsList.append(Fore.LIGHTBLUE_EX) 
        ColorsList.append(Fore.LIGHTCYAN_EX) 
        ColorsList.append(Style.BRIGHT + Fore.GREEN)
        return ColorsList
        


  
#随机选择字符串画，无聊做的功能，没什么用
class DynamicPainting:
    
    
    def StringCollect():
        time.sleep(0.2)
        randomcolor = random.choice(Colors.ColorCollect())
        PaintingCollect.append(randomcolor + """

))       .-.    (O))  ((O)     ))    W  W       .-.             _      ))     
(o0)-.  c(O_O)c   ||    ||  wWw(Oo)-.(O)(O)    c(O_O)c    /)   _||\ wWw(Oo)-.  
| (_)),'.---.`,  || /\ ||  (O)_| (_)) ||     ,'.---.`, (o)(O)(_'\  (O)_| (_)) 
| .-'/ /|_|_|\ \ ||//\\|| .' __)  .'  | \   / /|_|_|\ \ //\\ .'  |.' __)  .'  
|(   | \_____/ | / /  \ \(  _) )|\\   |  `. | \_____/ ||(__)((_) (  _) )|\||   
    \)  '. `---' .`( /    \ )`.__|/  \) (.-.__)'. `---' .`/,-. |`-`.)`.__|/  \)  
    (     `-...-'   )      (      )      `-'     `-...-' -'   ''   (      )      
        
        """)#字符串画
        
        PaintingCollect.append(randomcolor+ """
.------..------..------..------.     .------..------..------..------..------..------.
|M.--. ||O.--. ||R.--. ||E.--. |.-.  |O.--. ||P.--. ||T.--. ||I.--. ||O.--. ||N.--. |
| (\/) || :/\: || :(): || (\/) ((5)) | :/\: || :/\: || :/\: || (\/) || :/\: || :(): |
| :\/: || :\/: || ()() || :\/: |'-.-.| :\/: || (__) || (__) || :\/: || :\/: || ()() |
| '--'M|| '--'O|| '--'R|| '--'E| ((1)) '--'O|| '--'P|| '--'T|| '--'I|| '--'O|| '--'N|
`------'`------'`------'`------'  '-'`------'`------'`------'`------'`------'`------'`
        """)
        
        PaintingCollect.append(randomcolor + """
    .-------.     ,-----.    .--.     .--.    .-''-.  .-------.     .---.       ,-----         
\  _(`)_ \  .'  .-,  '.  |  |_     |  |  .'_ _   \ |  _ _   \    | ,_|     .'  .-,  '.   
| (_ o._)| / ,-.|  \ _ \ | _( )_   |  | / ( ` )   '| ( ' )  |  ,-./  )    / ,-.|  \ _ |
|  (_,_) /;  \  '_ /  | :|(_ o _)  |  |. (_ o _)  ||(_ o _) /  \  '_ '`) ;  \  '_ /  | |
|   '-.-' |  _`,/ \ _/  || (_,_) \ |  ||  (_,_)___|| (_,_).' __ > (_)  ) |  _`,/ \ _/  |  
|   |     : (  '\_/ \   ;|  |/    \|  |'  \   .---.|  |\ \  |  (  .  .-' : (  '\_/ \   ; 
|   |      \ `"/  \  ) / |  '  /\  `  | \  `-'    /|  | \ `'   /`-'`-'|___\ `"/  \  ) /
/   )       '. \_/``".'  |    /  \    |  \       / |  |  \    /  |        \'. \_/``".' 
`---'         '-----'    `---'    `--`   `'-..-'  ''-'   `'-'   `--------`  '-----'       
                                                                                                                
        """)
        PaintingCollect.append(randomcolor + """

                        ¸,.-·~~~~·.  
                        .·´        ,~,   ' , 
                    (¸,.--~~~·¯--.,¸,'_ 
                        (´'  ( o`, ;´o`, `,¯``· 
                        `·.   ¯,_  ¯  .·'     ;¸¯`,¯`,`·, 
                .  ·  ´  `~·-..-~ ´ `·.  ¸.·`     .·-~´ 
            .·´          .·  ºJNCO° `'     ,.·´ 
            .´´'~-.¸¸,.·,´                `,`·--´ 
            ',     '.      `,¸,..- -~~ - -.,'_ 
        ,·´, ,   `,      `,                  `·, 
        `--~-~·´        /:`,      _____    `. 
                        .'·::;;`·   `·.-------`·.  \ 
•Jnco Boy•      ;·.:::;;  `.   ;         :   '. 
    From          .'··:;:;;;; \   ;_____:    ) 
Jnco Tuffy's   .´··:.::::;;;;'.                ; 
        ßy          ;  .·:::::;;'.}                '·. 
-WùGóÐÐ-    ,'.`.. ·::: ;: '.                 \ 
                    ;  ,~-. .,,¸¸.',¸              ¸ .'¯¯`·. 
                        `··~-· ·,,¸¸..',`·._  . · ´ '-----··· ´| 
                                        `·--´`--´`---´`--´`--··´Æ¨‹

                                    
                                    """)
        PaintingCollect.append(randomcolor +"""            
        O)))))))                               O))                        O))
    O))    O))                             O))                        O))
    O))    O)O))  O))     O)))  O))  O) O))O))     O))      O))       O))
    O))))))O))  O))O))  )  O))O)   O))O))  O))   O))  O)) O))  O))O)) O))
    O))   O))    O)O)) O)  O)O))))) O)O))  O))  O))    O)O))   O)O)   O))
    O))    O))  O))O) O) O)O)O)       O))  O))   O))  O))O))   O)O)   O))
    O))      O))  O)))    O))) O)))) O)))  O)))))))O))     O)) O))O)) O))
                                                                                            
                        
                            """ )
        PaintingCollect.append(randomcolor + """                                                                                                                                                                                                      
            t#,                              ,;                           t#,                     
t         ;##W.                           f#i j.                    i   ;##W.             
ED.      :#L:WE             ;           .E#t  EW,                  LE  :#L:WE         
E#K:    .KG  ,#D          .DL          i#W,   E##j                L#E .KG  ,#D         
E##W;   EE    ;#f f.     :K#L     LWL L#D.    E###D.             G#W. EE    ;#f       
E#E##t f#.     t#iEW:   ;W##L   .E#f:K#Wfff;  E#jG#W;           D#K. f#.     t#i      
E#ti##f:#G     GK E#t  t#KE#L  ,W#; i##WLLLLt E#t t##f         E#K.  :#G     GK     
E#t ;##D;#L   LW. E#t f#D.L#L t#K:   .E#L     E#t  :K#E:     .E#E.    ;#L   LW.     
E#ELLE##Kt#f f#:  E#jG#f  L#LL#G       f#E:   E#KDDDD###i   .K#E       t#f f#:    
E#L;;;;;;,f#D#;   E###;   L###j         ,WW;  E#f,t#Wi,,,  .K#D         f#D#;   
E#t        G#t    E#K:    L#W;           .D#; E#t  ;#W:   .W#G           G#t   
E#t         t     EG      LE.              tt DWi   ,KK: :W##########Wt   t       
                        
                                                                                                        
                            """)
        PaintingCollect.append(randomcolor + """
                                                                                             
`7MM"" "Mq.                                        `7MMF'                             `7MM  
  MM   `MM.                                         MM                                 MM  
  MM   ,M9 ,pW"Wq.`7M'    ,A    `MF'.gP"Ya `7Mb,od8 MM         ,pW"Wq.   ,6"Yb.   ,M""bMM  
  MMmmdM9 6W'   `Wb VA   ,VAA   ,V ,M'   Yb  MM' "' MM        6W'   `Wb 8)   MM ,AP    MM  
  MM      8M     M8  VA ,V  VA ,V  8M""""""  MM     MM      , 8M     M8  ,pm9MM 8MI    MM  
  MM      YA.   ,A9   VVV    VVV   YM.    ,  MM     MM     ,M YA.   ,A9 8M   MM `Mb    MM  
.JMML.     `Ybmd9'     W      W     `Mbmmd'.JMML. .JMMmmmmMMM  `Ybmd9'  `Moo9^Yo.`Wbmd"MML.
                                                                                                                      
                               
                               
                               """)
        PaintingCollect.append(randomcolor + """                                     
    #      #   #                         #       # #   # #             #     
    ####### #   #  ########## ######### #  #     #  #   # #   ###  ########## 
    #     #  #   #          #  #       #  #      #   #   # ####          #     
    # #   #   #   #         #   #       #       ##    #   # #          #  # #   
    ###       #       # #    #       #     ##         #  #         #   #  #  
    ##        #         #     #########   ##          #   #        #   ##   # 
    ##        ##           #              ##          ##     #######      #     
                                                                                                    
                               
                               """)
        PaintingCollect.append(randomcolor + """
            ,   ,-',  
      ,', ,'  ','  ,'   ÅÑGË£ÏÇÄ †(–)Ë ßRÄ† 
    '-',  '      ,' 
        ' -,    ', 
            ' -, ',                                         , - - -, 
           ('''''' ®'''''''')                        ,,,,,    ,-' -,''''''''', 
            ` -„''`„- '                          ',  ,', -' , -,'' ''''''''', 
                "„  " - „                   „ - ",®,-'     `--' '''''''   
               „"         " „         „ - "      ,',,,', 
             „-" " " " " " " - - - " - „       ,' 
          „" –,'' - ,         ;            "      "„ 
          ";      ' - , ,  ; , , , - '' ' ' -,_ ', ', 
         , -' ' ',           ,'    ,'             ',—', ',  
       ,'         ' - , ,•-' /\    ',           •,'¯ ,'   `¸`; 
       ',                            ` ` ` ` ` `      ,-,,,-' 
         '-,                                  ,¬  ,-' 
            ' -,              ~~~~~~' ' `  ,-' 
                `~-,,,,,,,      ,,,,,,,,,,-~' 
      ('('('(,,,             ;    ;                •Å(V)åö• 
       '-, '-,'''      ,-';`,`'ˆˆˆˆˆ ,' ;' ' -,           •97•  
         ;¯ ;      ;  ;  ', ; ; ,'  ;  ‚¸  ' -,        •••  
         ;   ;     ;       '''''''''''    ``'-,',  ,' 
         ;   ;, -¬;    O          O   '-',,,,,,,,,,,, 
         ;        ;            O         ,'           ,' 
          ' - - ' `;    O           O        O    ,' 
               ,-'             O         O        ,'   
            ,-'   O      O        O        O ,'  
         ,-'          O       O        O     ,' 
      ,-'  O    O       O       O        ,-'-, 
       ``¬ -,,,,,,,-¬~,~~~~~~~~~--',)  (' -,  
                    ',   (',                     ' -,    '-, 
                     ',)  (',                        `-,)  ' -, 
                      ',    ',                           `-,  ,',-----, 
                       ',)   ;                              `\,- ---'  
                   ¸,,,,'‡  (;                                   
                  (¸,,,,,';_'\ ß §(V)òó†(–)775 ™˜¤¹                               
                               """)
        PaintingCollect.append(randomcolor +"""
                             ,  ·  ·  ·  ·  ·  , 
                         , '                     ' , 
                  ____;______________;____                 
                 (_______________________)            
                      , '                           ' , 
                    ,'       ~~~        ~~~      ', 
                (¯\;       (¯ø¯)       (¯ø¯)       ;/¯) 
                  )\;               ,'                   ;/( 
                  '·;              ,'                    ';·' 
                    ',             ' · ·'               ,' 
                      ',      ' ; ; ; ; ; ; ; '       ,' 
                        ',       ' · · · · '        ,' 
                          ' ,          )        , ' 
             Ñë§§      ,,/'  ·  ·  ·  ·  · '\,,      *MSøA* 
                ,, ~~ ¯¯                      ¯¯~~,,*97* 
           )¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯( 
        , '                                                       ' ,  
  , '¯¯¯¯¯)                                               (¯¯¯¯¯' , 
  |  ¯¯¯¯¯)                                               (¯¯¯¯¯   | 
  |  ¯¯¯¯¯)                                               (¯¯¯¯¯   | 
  ' ,¯¯¯¯¯)                                                (¯¯¯¯¯ ,' 
     ¯,¯¯¯                                                   ¯¯¯,¯  
        ' ,                                                       , '  
           )______________________________(§Ãž                        
                               """)
        PaintingCollect.append(randomcolor + """
                                              ©________ 
                                       ||             ( 
                                       ll Çãrôù§ël ) 
                                       ll________( 
                       _________ll___________ 
              _____|£££££££££££££££££££££|____ 
             /                                                      \ 
    ____/_________________________________\___ 
 /'''\© © ©  © © © © © ©//'''''\\© © © © © © © © © ©/''\ 
 \   \ © © © ©  © © ©  //       \\ © © © © © © © © /    / 
   \   \© © © © © © © ||          ||© © © © © © © ©\   / 
     \,/© © ©  © © © © \\       // © © © © © © © © \,/ 
       ¯¯¯¯¯¯¯¯|\|¯¯¯¯¯¯ \\    //¯¯¯¯¯¯¯¯¯¯|\|¯¯¯¯¯¯¯ 
    Çãrôù§ël    |\|              ''''''''                   |\| 
   By: Ghost   |\|                                     |\| 
                     |\|                      ,........      |\| 
    ,..';(;((;(;      |\|                   §;§;§§§;§;   |\| 
    );)));););;);)   |\|                  §;§§;§;§§;§§ |\| 
 (;(( o '(;((;((((   |\|      .....      ;§ o  ;§;§§;§  |\|          ,... 
   /    _) )););))))|\|    (;((;(();)    /    _) §§;§§§ |\|       §;§;§; 
  \°_/ \  '(;(((;((_|\|__!!!!(((;(;(   \°_/ \   ;§§;§§_|\|___§§;§§;§; 
         \  ');;));))     ||    ((;(())           \   §§;§§     ||    §§§;§; 
           \   ((((;(    //      ));)))            \   §§;§§  //      §;§§§ 
      ___((     ' =='`(       (;(((        ___((     ' =='`(       §§;§ 
    (  )___|     /_||_/\      / ));)      (  )--_| /   /_||_/\      / §;§§ 
     \  \     |   /   ||   \ \  /               \ (  )__/   ||   \ \   /   ;§; 
       V     | (   //_\\  \ \ \                \ \  \    //_\\  \ \  \ 
              (  )   |\|     ( (  )                \/V      |\|     ( (  ) 
               | |    |\|     / / /                           |\|     / / / 
              /_|    |\|   / /_|                            |\|    / /_| 
     /© © © © © © © © © © © © © © © © © © © © ©\ 
   /© © © © © © © © © © © © © © © © © © © © © ©\ 
 /© © © © © © © © © © © © © © © © © © © © © ©\ 
 ¯¯¯¯¯¯¯¯¯¯¯|£££££££££££££££££££££££|¯¯¯¯¯¯¯¯¯¯ 
                     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯«•š              
                               """)
        PaintingCollect.append(randomcolor + """
                               _ ___ 
       _ _         _@)@) \          /^^\ /^\ /^^\_ 
    _/oo \____/~''. . .  '~\       /'\''  ~ ''~~' -'\_ 
   / '.'. ~.~.~.       .'    ~ |     /'\~~..''''.'' ''  ~\_ 
  ('_'_'_'_'_'_'_'_  ' :   '     \_/' '.''  . '.   .''  '.  ~\_ 
  ~V~V~V~V  \   ~\  '' '~  '   '' ~   `   ~  ''   ~\_ 
    /\~/\~/\~/\~/|/  '   ''  _   ' ~ ''  '    ~  '' __  '  ..  \_ 
 <-- --- ---.---.--/'   ''   /'  '\_ '' ': ~ ;;''    ' /''; \ ;'''''' '' ~\ _ 
    \~ '. . : .:: ~. :.  /_'''_'' \_' :'''_ : _ ''/''_' '_ \:_ '''' ''..\/\/\/~/\~ 
 ~~ \-~ `---~~~---- \(_)(_)(_)/ ~ ~~' ~\(_)(_)(_)\_~_~_~_~_~/˜¤¹                      
                               
                               """)
        PaintingCollect.append(randomcolor +"""
             ¸, . , . , ,¸ 
        (    ###     ' - , 
          ' - ,              ' - , 
               ' -,                '  - . , , ¸  
  ¸ , . ~ ' ' ' ' ' '        ##                  ' ` - .  
 '##                                                   ' - ,  
                                                              ' -, 
                                                            ##    ', 
                                                                      ; 
                                                          ,¸           ; 
          ####              , . - - - · · ,               '-         ; 
  - ~ ~ · · · - ~ ~ ·,·-·'                 '           @)   ,¸    ; 
  Ñë§§           , - '  #            ¸ ,<', ,         ,.-~    ' ' ', 
                   (¸¸¸¸¸¸¸¸¸¸¸¸¸, . - '       )   ' ,- - ,   '-,        ', 
                                             ( ¸¸,-'       ' -,  ' - ,     ', 
                                                               ' - . .'.'.'-'«•š                                                               
                               """)
        PaintingCollect.append(randomcolor +"""                    
       Å ÞRÉÇÎÒÙ§ (V)Ò(V)ÊÑ† 
    Å ÞRËÇÎÓÚ§ Ç(–)ÎRS†(V)Ä§ GÎƒ† 
 
                                         Ò=¸ 
             „- ~·""~-„                 ¶,,,¸ 
         „·"……………"·„              ; ; ; ; 
       „"…………………"·„          ; ;  ; ;   •Å(V)åö• 
     „"  ,·'………………… "·„      ; ;¨¨;  ;      •97• 
   „" ,·'……  „·"¸ ¸ ¸ ¸ „"„"„ … ;   „",'  ,' „"      •••  
  ; ,'…… „·"'·,',',',',',(((„"„"((()) ;„",·'¨¨,' „"  ; 
  ; ',…„·"„"   ¸    ','       ¸   ((()))… ,' „"… ;    
   ; ',"))))   ,'C',         ,'C',  ((())),·'„·"…… ; 
   "„ ;   "„¸   ` `   -~-    ` `  „¸" „"………… ; 
     Ø      "„      ~--~      „" ¸·"……………; 
                "~-„„„„„„„„„-~" ¸·"¸ ……………; 
                   (',)',) (,'(,')¸·" „"…………… ;    
                  "„¸*¸*¸*¸*¸*¸ -" ……………  ; 
                   "„………………………… ;'; 
                     "„…ß §(V)òó†(–)775…  ; 
                       "„……………"„°º°º "„…  ;     
                         "„…ƒòr……  "„°º°º"„… ; 
                           "„  §å(V)åñ†(–)315  „" 
              „·"" "" ""„·"…………………  „" 
            „" ˆ…¨…¨…"„……………… „·"„ 
            ;  ¨…¨…¨… ;………………   ;   
            „"~-„¨„¨„¨„-~"………………  „" 
             "·„ ……………………    „" 
                 "~-„ „ „ „ „ „ „ „ „ „ „-~"§Ãž
                 """)
        PaintingCollect.append(randomcolor +"""
    _____,.-·-.,____,.––. 
   ,.·˜¨¸,.–––,     ,–––––,    .' 
  /    '(       /     /       ·´–-·´ 
  \      )    '/     /______¸ 
   `·..·´' .·´       ____¸,.-·´    ¸,.-, 
          ¯/     /             ,.-·´  ¸,  ',   '.·´¯;    ¸,.,¸         ¸,..,¸        ¸.·´˜¨¯')¸.·´˜¨¯') 
          '/     /              `·.,.-´  \  '.·´.·´'¯ ,·´  ,.-.¸)   ,'·´  ___;      '·. (˜¨¯ '·. (˜¨¯ 
         /     /             ¸,.–.¸   .·´., `·.     '.   (_¸,.-·´;',   (_¸,.-·´;'  _¸,) '·,     ) '·, 
  _¸,.·´     '(________)    .´ (   (  \   ',    `·.,¸_¸,.-·´ '`·.,¸_¸,.-·´ '('_¸,.-·´'  ,·' ,.·' 
(¸________________.·´      `·´   '`·. `·,¸_¸.·.¸    -Excess-   '¸.·.¸_¸,.-·´,.·´ 
   -WDA-n CorpsE                       `·-.,¸¸,.-·'` .·.   '98   .·. ´·-.,¸_¸,.-·´ 
                                                              `·-.`·. * .·´.-·´ 
                                                                  *) Y (* 
                                                                   \.·’·./«•š                                                                                
                               """)
        PaintingCollect.append(randomcolor +"""
' /|¯¯¯¯¯¯¯¯¯¯¯/¯¯/|¯¯¯|/|¯¯¯|\¯¯\'/¯¯/'\¯¯\ 
 | |_____         /     '|'|\__'\|     '|/__/| '  | ''|  ' |  
 |/::·..·::·/       /        `·´¯|_|     |\¯¯\|\__\/__/| 
  ¯¯¯¯¯/     ' '/\        |¯''|¯¯¯|_'| |__|'\|____ |/  
         /       '/ | \''___,\./___/_''|\|__|–•¤›Sephiroth  
       /   ' '' ' /__\'|'¨¨`;´'| |'¯¯`|'___________.'_ 
    ' /|‹»—›Fate Zero  by MaGuS & FuNGii | 
     | |_______________'_'_______'______''| 
     |/ ::·:.·.::..·.··::···.·:·:;·..:·;·..:·.:··.:·.·::·.:'./ 
    ' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ §Ãž                               
                               
                               """)
        PaintingCollect.append(randomcolor +"""
  ' .·---·._.·´¯`·.–DaiR–.·´¯`·._.---._.·-·. °-¤SouM¤-° 
'(       í¯`·.___)        (___.·´¯ì    í¯')   ')°-¤GmA¤-° 
 |`·.    `·-·´¯`·, '||\¯¯`,-'.__.·-,·'  ,·| (_.·' |.·´¯¯`·-·´¯`·. 
 '·.  ':    í¨|`·-·'|·'!\')    )\ `·.   '!    ! | '·---·´!    í¯¯`·._.·'| 
    )·'    '!¨'·---·' .·´  .·'-=;   '·,|·.   '·.        )   `>¯`·--·´  
  (        |     '(___(---.·´__.·|`·!      )     '!    !__.·´¯`·, 
  '|`·—-·'|     '!     '!   !     ! .'  !·—·´|     '|`·-—·´¯`·--·´I 
   `·-----·'      '·---·'    '·---·´     '·—·´      `·-——·´`·–·'«•š                                                                                                                
                               """)
        PaintingCollect.append(randomcolor +"""
                               
 '|¯¯¯¯¯|/'¯¯'|¯'/¯¯¯¯'|¯¯¯¯|¯¯¯¯'|¯¯¯¯|¯¯¯¯¯¯'|¯¯'| 
 '|         |\____'\       |\       \__   '    __|'       |\       \ 
 '|         |/¯¯'|¯\|       |_|     _|.:/      /|:.:|'       |/____/|    
 '|         |\'___'/|       '|¯|   ¯¯|/      /'/¯¯'|       '|:|¯'|¯¯¯| 
 '|         |\|:.::'|/|       '|¯|       |      |/|¯¯¯¯'|     |:|        | 
 '|         |  ¯¯  '|       '|  |       |'     '|/       '/     '|/        /| 
 /___,|_/|'      /__,|_'/| |\__,|_\___|\____\___'|\_____\| 
'|::.::::::|:|      |:::::.:'|:| |:|:::.:::|::.:'|:|:::.:::|::.:eX¡St™::| 
'|:::.:::::|/'      '|::::.::'|/  \|::.::::'|:::.'|\|::::.::|::SøuM 97:'| 
 ¯¯¯¯¯          ¯¯¯¯      ¯¯¯¯ ¯¯¯  ¯¯¯¯ ¯¯¯  ¯¯¯¯¯˜¤¹                               
                                       
                               """)
        return PaintingCollect

    def DynaminString():
        #DynamicPainting.StringCollect()
        time.sleep(0.1)
        return random.choice(DynamicPainting.StringCollect())
      


#print(DynamicPainting.DynaminString())


















