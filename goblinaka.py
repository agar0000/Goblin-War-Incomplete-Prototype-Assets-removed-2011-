try:
    import pygame
    import random
    
    pygame.init()
    def niveles():
        #pygame.init()
        pantalla=pygame.display.set_mode((800,600))
        
        misionreader=open('log\misions.txt')
        mision=int(misionreader.readline())
    
        if mision==1:
            imagelevels=pygame.image.load("images/goblinw/niveles1.png").convert_alpha()
        if mision==2:
            imagelevels=pygame.image.load("images/goblinw/niveles2.png").convert_alpha()
        if mision==3:
            imagelevels=pygame.image.load("images/goblinw/niveles3.png").convert_alpha()
        if mision==4:
            imagelevels=pygame.image.load("images/goblinw/niveles4.png").convert_alpha()
        if mision==5:
            imagelevels=pygame.image.load("images/goblinw/niveles5.png").convert_alpha()
        if mision==6:
            imagelevels=pygame.image.load("images/goblinw/niveles6.png").convert_alpha()
        if mision==7:
            imagelevels=pygame.image.load("images/goblinw/niveles7.png").convert_alpha()
        if mision==8:
            imagelevels=pygame.image.load("images/goblinw/niveles8.png").convert_alpha()
        if mision==9:
            imagelevels=pygame.image.load("images/goblinw/niveles9.png").convert_alpha()
        if mision==10:
            imagelevels=pygame.image.load("images/goblinw/niveles10.png").convert_alpha()
        if mision==11:
            imagelevels=pygame.image.load("images/goblinw/niveles11.png").convert_alpha()
        if mision==12:
            imagelevels=pygame.image.load("images/goblinw/niveles12.png").convert_alpha()
        if mision==13:
            imagelevels=pygame.image.load("images/goblinw/niveles13.png").convert_alpha()
    
    
    
        salir=False
        reloj1=pygame.time.Clock()
        rmouse=pygame.Rect(0,0,10,10)
    
        r1=pygame.Rect(50,100,80,80)
        r2=pygame.Rect(180,100,80,80)
        r3=pygame.Rect(310,100,80,80)
        r4=pygame.Rect(440,100,80,80)
        r5=pygame.Rect(560,100,80,80)
        r6=pygame.Rect(690,100,80,80)
    
        r7=pygame.Rect(180,230,80,80)
        r8=pygame.Rect(310,230,80,80)
        r9=pygame.Rect(440,230,80,80)
        r10=pygame.Rect(560,230,80,80)
        #r11=pygame.Rect(560,230,80,80)
        #r12=pygame.Rect(690,230,80,80)
    
        rFINAL=pygame.Rect(310,410,180,180)
        
        rsalir=pygame.Rect(760,570,15,15)
    
        while salir != True:
            (rmouse.left,rmouse.top)=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if rmouse.colliderect(rsalir):
                        menu1()
                    if rmouse.colliderect(r1):
                        guerra1()
                    if rmouse.colliderect(r2) and mision>=2:
                        guerra2()
                    if rmouse.colliderect(r3) and mision>=3:
                        guerra3()
                    if rmouse.colliderect(r4) and mision>=4:
                        guerra4()
                    if rmouse.colliderect(r5) and mision>=5:
                        guerra5()
                    if rmouse.colliderect(r6) and mision>=6:
                        guerra6()
                    if rmouse.colliderect(r7) and mision>=7:
                        guerra7()
                    if rmouse.colliderect(r8) and mision>=8:
                        guerra8()
                    if rmouse.colliderect(r9) and mision>=9:
                        guerra1()
                    if rmouse.colliderect(r10) and mision>=10:
                        guerra1()
                    if rmouse.colliderect(rFINAL) and mision>=11:
                        guerra1()
    
            reloj1.tick(15)#50,100
            pygame.draw.rect(pantalla,(0,0,0),r1)
            pygame.draw.rect(pantalla,(0,0,0),r2)
            pygame.draw.rect(pantalla,(0,0,0),r3)
            pygame.draw.rect(pantalla,(0,0,0),r4)
            pygame.draw.rect(pantalla,(0,0,0),r5)
            pygame.draw.rect(pantalla,(0,0,0),r6)
            pygame.draw.rect(pantalla,(0,0,0),r7)
            pygame.draw.rect(pantalla,(0,0,0),r8)
            pygame.draw.rect(pantalla,(0,0,0),r9)
            pygame.draw.rect(pantalla,(0,0,0),r10)
            pygame.draw.rect(pantalla,(0,0,0),rFINAL)
            
            pygame.draw.rect(pantalla,(0,0,0),rsalir)
            pantalla.blit(imagelevels,(0,0))
            pygame.display.update()
    
        pygame.quit()
        
    #####################################################################
        
    def tienda():
        pygame.init()
        pantalla=pygame.display.set_mode((800,600))
        imagetienda=pygame.image.load("images/goblinw/tienda.png").convert_alpha()
        salir=False
        reloj1=pygame.time.Clock()
        rsalir=pygame.Rect(750,550,25,30)
        rmouse=pygame.Rect(0,0,10,10)
    
        i_disp=pygame.image.load("images/goblinw/disponible.png").convert_alpha()
        i_nodisp=pygame.image.load("images/goblinw/no_disponible.png").convert_alpha()
    
        tiendareader=open('log/shop.txt')
        tienda_i=tiendareader.readlines()
        h_escudo=int(tienda_i[0])
        h_terremoto=int(tienda_i[1])
    
        moneyreader=open('log\money.txt')
        money=int(moneyreader.readline())
        print 'dinero:', money
        moneyreader.close()
    
        datosreader=open('log\datos.txt')
        hpdatos=int(datosreader.readlines()[0])
        print 'hp: ', hpdatos
        datosreader.close()
    
        datosreader=open('log\datos.txt')
        mpdatos=int(datosreader.readlines()[1])
        print 'mp: ', mpdatos
        datosreader.close()
    
        potionsreader=open('log\potions.txt')
        potionshp=int(potionsreader.readlines()[0])
        print 'potions hp: ', potionshp
        potionsreader.close()
        
        potionsreader=open('log\potions.txt')
        potionsmp=int(potionsreader.readlines()[1])
        print 'potions mp: ', potionsmp
        potionsreader.close()
    
        datosreader=open('log\datos.txt')
        listadatos=datosreader.readlines()
        datosreader.close()
    
        s_sell=pygame.mixer.Sound("sounds/goblinw/sell.wav")
        s_error=pygame.mixer.Sound("sounds/goblinw/error.wav")
        
    
        sdisp1=pygame.sprite.Sprite()
        sdisp1.image=i_disp
        sdisp1.rect=i_disp.get_rect()
        sdisp1.rect.top=90
        sdisp1.rect.left=250
        
        sdisp2=pygame.sprite.Sprite()
        sdisp2.image=i_disp
        sdisp2.rect=i_disp.get_rect()
        sdisp2.rect.top=145
        sdisp2.rect.left=250
        
        sdisp3=pygame.sprite.Sprite()
        sdisp3.image=i_disp
        sdisp3.rect=i_disp.get_rect()
        sdisp3.rect.top=220
        sdisp3.rect.left=400
        
        sdisp4=pygame.sprite.Sprite()
        sdisp4.image=i_disp
        sdisp4.rect=i_disp.get_rect()
        sdisp4.rect.top=280
        sdisp4.rect.left=310
        
        sdisp5=pygame.sprite.Sprite()
        sdisp5.image=i_disp
        sdisp5.rect=i_disp.get_rect()
        sdisp5.rect.top=350
        sdisp5.rect.left=340
        
        sdisp6=pygame.sprite.Sprite()
        sdisp6.image=i_disp
        sdisp6.rect=i_disp.get_rect()
        sdisp6.rect.top=400
        sdisp6.rect.left=490
    
    #fuente
        fuente1=pygame.font.SysFont("Arial",20,True,False)
    
        
        
    
        while salir != True:
            if h_escudo==1:
                sdisp3.image=i_nodisp
            
            if h_terremoto==1:
                sdisp6.image=i_nodisp
                
            (rmouse.left,rmouse.top)=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        menu1()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if rmouse.colliderect(rsalir):
                        menu1()
                    if rmouse.colliderect(sdisp1.rect):
                        if money>=100:
                            hpdatos+=25
                            datoswriter=open('log/datos.txt','w')
                            datoswriter.write(str(hpdatos)+'\n'+str(mpdatos))
                            datoswriter.close()
                            money-=100
                            moneywriter=open('log/money.txt','w')
                            moneywriter.write(str(money))
                            moneywriter.close()
                            s_sell.play()
                            print 'hp: ', hpdatos
                            print 'dinero: ', money
                        else:
                            s_error.play()
    
                    if rmouse.colliderect(sdisp2.rect):
                        if money>=100:
                            mpdatos+=25
                            datoswriter=open('log/datos.txt','w')
                            datoswriter.write(str(hpdatos)+'\n'+str(mpdatos))
                            datoswriter.close()
                            money-=100
                            moneywriter=open('log/money.txt','w')
                            moneywriter.write(str(money))
                            moneywriter.close()
                            s_sell.play()
                            print 'mp: ', mpdatos
                            print 'dinero: ', money
                        else:
                            s_error.play()
    
                    if rmouse.colliderect(sdisp3.rect):
                        if money>=1000 and h_escudo==0:
                            shopwriter=open('log/shop.txt','w')
                            h_escudo=1
                            shopwriter.write(str(h_escudo)+'\n'+str(h_terremoto))
                            shopwriter.close()
                            money-=1000
                            moneywriter=open('log/money.txt','w')
                            moneywriter.write(str(money))
                            moneywriter.close()
                            s_sell.play()
                        else:
                            s_error.play()
                        
                        
                    if rmouse.colliderect(sdisp4.rect):
                        if money>=20:
                            potionshp+=1
                            datoswriter=open('log/potions.txt','w')
                            datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                            datoswriter.close()
                            money-=20
                            moneywriter=open('log/money.txt','w')
                            moneywriter.write(str(money))
                            moneywriter.close()
                            s_sell.play()
                            print 'potionshp: ', potionshp
                            print 'dinero: ', money
                        else:
                            s_error.play()
    
                    if rmouse.colliderect(sdisp5.rect):
                        if money>=20:
                            potionsmp+=1
                            datoswriter=open('log/potions.txt','w')
                            datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                            datoswriter.close()
                            money-=20
                            moneywriter=open('log/money.txt','w')
                            moneywriter.write(str(money))
                            moneywriter.close()
                            s_sell.play()
                            print 'potionsmp: ', potionsmp
                            print 'dinero: ', money
                        else:
                            s_error.play()
                            
                    if rmouse.colliderect(sdisp6.rect):
                        if money>=5000 and h_terremoto==0:
                            shopwriter=open('log/shop.txt','w')
                            h_terremoto=1
                            shopwriter.write(str(h_escudo)+'\n'+str(h_terremoto))
                            shopwriter.close()
                            money-=5000
                            moneywriter=open('log/money.txt','w')
                            moneywriter.write(str(money))
                            moneywriter.close()
                            s_sell.play()
                        else:
                            s_error.play()
                        
                        
                    
    
            
            reloj1.tick(15)
            pantalla.blit(imagetienda,(0,0))
            
            pantalla.blit(sdisp1.image,sdisp1.rect)
            pantalla.blit(sdisp2.image,sdisp2.rect)
            pantalla.blit(sdisp3.image,sdisp3.rect)
            pantalla.blit(sdisp4.image,sdisp4.rect)
            pantalla.blit(sdisp5.image,sdisp5.rect)
            pantalla.blit(sdisp6.image,sdisp6.rect)
            
            #creacio de cadenas str per fer els textos
            dinerot=str('Dinero: '+str(money))
            hpt=str('HP: '+str(hpdatos))
            mpt=str('MP: '+str(mpdatos))
            potionhpt=str('Pociones HP: '+str(potionshp))
            potionmpt=str('Pociones MP: '+str(potionsmp))
            
            #creacio de textos
            textodinero=fuente1.render(dinerot,0,(0,0,0))
            textohp=fuente1.render(hpt,0,(0,0,0))
            textomp=fuente1.render(mpt,0,(0,0,0))
            textohpp=fuente1.render(potionhpt,0,(0,0,0))
            textompp=fuente1.render(potionmpt,0,(0,0,0))
            
            #imprimacio
            pantalla.blit(textodinero,(620,5))
            pantalla.blit(textohp,(620,30))
            pantalla.blit(textomp,(620,55))
            pantalla.blit(textohpp,(620,90))
            pantalla.blit(textompp,(620,115))
            
            
            
            
            pygame.display.update()
        pygame.quit()
    
    
            
    #e dakabar aksta funcio
    def creditos():
        pygame.init()
        pantalla=pygame.display.set_mode((800,600))
        salir=False
        reloj1=pygame.time.Clock()
        creditos_i=pygame.image.load("images/goblinw/creditos.png").convert_alpha()
        creditos_f=pygame.image.load("images/goblinw/creditos_f.png").convert_alpha()
        sonido3=pygame.mixer.Sound("sounds/goblinw/BSO_C.wav")
        contG=0
        cont_c=0
        sonido3.play()
        
       
        
    
        while salir != True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        sonido3.stop()
                        menu1()
            
            contG+=2
            reloj1.tick(30)
            pantalla.fill((0,0,0))
            if contG<2550:
                pantalla.blit(creditos_i,(20,600-contG))
            else:
                pantalla.blit(creditos_f,(0,0))
                cont_c+=1
                if cont_c==180:
                    sonido3.stop()
                    menu1()
            pygame.display.update()
    
        pygame.quit()
    #######################---Es la unika k esta akabada---#########################
    def instruccions():
        pygame.init()
        pantalla=pygame.display.set_mode((800,600))
        imageinstruccions=pygame.image.load("images/goblinw/instruccions.png").convert_alpha()
        salir=False
        reloj1=pygame.time.Clock()
        rcruzi=pygame.Rect(10,560,25,25)
        rmouse=pygame.Rect(0,0,10,10)
    
        while salir != True:
            (rmouse.left,rmouse.top)=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if rmouse.colliderect(rcruzi):
                        menu1()
    
            reloj1.tick(15)
            
            pygame.draw.rect(pantalla,(0,0,0),rcruzi)
            pantalla.blit(imageinstruccions,(0,0))
            pygame.display.update()
        pygame.quit()
    
    
     #####################################################################       
    def menu1():
        #pygame.init()
        pantalla=pygame.display.set_mode((800,600))
        icono=pygame.image.load("images/goblinw/icon.png")
        pygame.display.set_caption('GOBLIN W.')
        pygame.display.set_icon(icono)
        salir=False
        reloj1=pygame.time.Clock()
    
        sonido1=pygame.mixer.Sound("sounds/goblinw/Blast.wav")
    
        r1=pygame.Rect(255,267,263,12)
        r2=pygame.Rect(320,300,130,12)
        r3=pygame.Rect(330,330,115,12)
        r4=pygame.Rect(310,370,150,12)
        r5=pygame.Rect(340,400,100,12)
        rreset=pygame.Rect(70,560,20,20)
        
    
        imagemenu=pygame.image.load("images/goblinw/menu.png").convert_alpha()
        rmouse=pygame.Rect(0,0,10,10)
    
        while salir != True:
            (rmouse.left,rmouse.top)=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
    
                if event.type==pygame.KEYDOWN:
    
                    if event.key==pygame.K_SPACE:
                        guerra1()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if rmouse.colliderect(r1):
                        sonido1.play()
                        instruccions()
                    if rmouse.colliderect(r2):
                        sonido1.play()
                        niveles()
                    if rmouse.colliderect(r3):
                        sonido1.play()
                        tienda()
                    if rmouse.colliderect(r4):
                        sonido1.play()
                        creditos()
                    if rmouse.colliderect(r5):
                        sonido1.play()
                        salir=True
                    if rmouse.colliderect(rreset):
                        reset()
                        
    
            pygame.draw.rect(pantalla,(0,0,0),rmouse)
            pygame.draw.rect(pantalla,(0,0,0),r1)
            pygame.draw.rect(pantalla,(0,0,0),r2)
            pygame.draw.rect(pantalla,(0,0,0),r3)
            pygame.draw.rect(pantalla,(0,0,0),r4)
            pygame.draw.rect(pantalla,(0,0,0),r5)
            
            pantalla.blit(imagemenu,(0,0))
            pygame.draw.rect(pantalla,(0,0,0),rreset)
            reloj1.tick(15)
            
            pygame.display.update()
        pygame.quit()
    
            
    
    
    #####################################################################
        ####################################################################
        ###################################################################
        ##################################################################
    def reset():
        pygame.init()
        pantalla=pygame.display.set_mode((800,600))
        icono=pygame.image.load("images/goblinw/icon.png")
        fondo=pygame.image.load("images/goblinw/reset.png")
        pygame.display.set_caption('GOBLIN W.')
        pygame.display.set_icon(icono)
        sonido1=pygame.mixer.Sound("sounds/goblinw/reset.wav")
        salir=False
        rmouse=pygame.Rect(0,0,10,10)
        rsi=pygame.Rect(125,280,165,90)
        rno=pygame.Rect(470,270,165,90)
        reloj1=pygame.time.Clock()
        while salir != True:
            (rmouse.left,rmouse.top)=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if rmouse.colliderect(rsi):
                        sonido1.play()
                        shopwriter=open('log/shop.txt','w')
                        shopwriter.write('0\n0')
                        shopwriter.close()
                        moneywriter=open('log/money.txt','w')
                        moneywriter.write('0')
                        moneywriter.close()
                        datoswriter=open('log/datos.txt','w')
                        datoswriter.write('350\n100')
                        datoswriter.close()
                        misionswriter=open('log/misions.txt','w')
                        misionswriter.write('1')
                        misionswriter.close()
                        potionswriter=open('log/potions.txt','w')
                        potionswriter.write('2\n2')
                        potionswriter.close()
                        menu1()
                        
                    if rmouse.colliderect(rno):
                        menu1()
            
            pygame.draw.rect(pantalla,(0,0,0),rsi)
            pygame.draw.rect(pantalla,(0,0,0),rno)
            pantalla.blit(fondo,(0,0))
            pygame.display.update()
        pygame.quit()
        
    
    def guerra1():
        #pygame.init()
        pygame.key.set_repeat(20)
        pantalla=pygame.display.set_mode((800,600))
        fondo=pygame.image.load("images/goblinw/fonsherba.png")
        icono=pygame.image.load("images/goblinw/icon.png")
        pygame.display.set_caption('GOBLIN W.')
        pygame.display.set_icon(icono)
    
        #rectangles dels arbres
        r_a1=pygame.Rect(80,300,10,30)
        r_a2=pygame.Rect(400,200,10,30)
        r_a3=pygame.Rect(700,400,10,30)
    
        pygame.draw.rect(pantalla,(0,0,0),r_a1)
        pygame.draw.rect(pantalla,(0,0,0),r_a2)
        pygame.draw.rect(pantalla,(0,0,0),r_a3)
    
    
        #SONS
        sonido1=pygame.mixer.Sound("sounds/goblinw/Blast.wav")
        sonido2=pygame.mixer.Sound("sounds/goblinw/explosion.wav")
        sonido3=pygame.mixer.Sound("sounds/goblinw/BSO1.wav")
        sonidodead=pygame.mixer.Sound("sounds/goblinw/deadpj.wav")
        sonidoespada=pygame.mixer.Sound("sounds/goblinw/Sspada.wav")
        sonidoespadaF=pygame.mixer.Sound("sounds/goblinw/SspadaF.wav")
        sonidocrit1=pygame.mixer.Sound("sounds/goblinw/crit1.wav")
        sonidocrit2=pygame.mixer.Sound("sounds/goblinw/crit2.wav")
        sonidocrit3=pygame.mixer.Sound("sounds/goblinw/crit3.wav")
        sonidorun=pygame.mixer.Sound("sounds/goblinw/run.wav")
        sopotion=pygame.mixer.Sound("sounds/goblinw/potion.wav")
        s_terremoto=pygame.mixer.Sound("sounds/goblinw/terremoto.wav")
        #sonidocrit3=pygame.mixer.Sound("sounds/goblinw/.wav")
    
        
        #goblin parat
        goblin1=pygame.image.load("images/goblinw/Idle0.png").convert_alpha()
        goblin2=pygame.image.load("images/goblinw/Idle1.png").convert_alpha()
    
        #goblin caminant cap a la dreta
        goblinwr1=pygame.image.load("images/goblinw/Walk0.png").convert_alpha()
        goblinwr2=pygame.image.load("images/goblinw/Walk1.png").convert_alpha()
        goblinwr3=pygame.image.load("images/goblinw/Walk2.png").convert_alpha()
        goblinwr4=pygame.image.load("images/goblinw/Walk3.png").convert_alpha()
    
        #goblin caminant cap a leskerra
        goblinwl1=pygame.image.load("images/goblinw/Walkl0.png").convert_alpha()
        goblinwl2=pygame.image.load("images/goblinw/Walkl1.png").convert_alpha()
        goblinwl3=pygame.image.load("images/goblinw/Walkl2.png").convert_alpha()
        goblinwl4=pygame.image.load("images/goblinw/Walkl3.png").convert_alpha()
    
        #goblin atakant cap a la dreta
        goblinar1=pygame.image.load("images/goblinw/Attack0.png").convert_alpha()
        goblinar2=pygame.image.load("images/goblinw/Attack1.png").convert_alpha()
        goblinar3=pygame.image.load("images/goblinw/Attack2.png").convert_alpha()
    
        #goblin atacant cap a leskerra
        goblinal1=pygame.image.load("images/goblinw/Attackl0.png").convert_alpha()
        goblinal2=pygame.image.load("images/goblinw/Attackl1.png").convert_alpha()
        goblinal3=pygame.image.load("images/goblinw/Attackl2.png").convert_alpha()
    
        #goblin atacant am magia cap a la dreta
        goblinamr=pygame.image.load("images/goblinw/Attackmr.png").convert_alpha()
    
        #goblin atacant am magia kap a leskerra
        goblinaml=pygame.image.load("images/goblinw/Attackml.png").convert_alpha()
    
        #goblin mort 1
        goblindr=pygame.image.load("images/goblinw/Dead0.png").convert_alpha()
    
        #goblin mort 2
        goblindl=pygame.image.load("images/goblinw/Dead1.png").convert_alpha()
    
        #goblin golpejat 1
        goblinhr=pygame.image.load("images/goblinw/Hurt0.png").convert_alpha()
    
        #goblin golpejat 2
        goblinhl=pygame.image.load("images/goblinw/Hurt1.png").convert_alpha()
    
        
        #bola de foc
        foc1=pygame.image.load("images/goblinw/foc.png").convert_alpha()
    
        #monstres
        
        #POP
        monstruoimage1=pygame.image.load("images/goblinw/monstruo1.png").convert_alpha()
        monstruoimage3=pygame.image.load("images/goblinw/monstruo1_3.png").convert_alpha()
        monstruoimage4=pygame.image.load("images/goblinw/monstruo1_4.png").convert_alpha()
        monstruoimage5=pygame.image.load("images/goblinw/monstruo1_5.png").convert_alpha()
        monstruoimage6=pygame.image.load("images/goblinw/monstruo1_6.png").convert_alpha()
    
        #GUERRER DAURAT
        monstruo2image1=pygame.image.load("images/goblinw/guerrero1.png").convert_alpha()
        monstruo2image2=pygame.image.load("images/goblinw/guerrero1_2.png").convert_alpha()
        monstruo2image3=pygame.image.load("images/goblinw/guerrero1_3.png").convert_alpha()
        monstruo2image4=pygame.image.load("images/goblinw/guerrero1_4.png").convert_alpha()
        monstruo2image5=pygame.image.load("images/goblinw/guerrero1_5.png").convert_alpha()
        monstruo2image6=pygame.image.load("images/goblinw/guerrero1_6.png").convert_alpha()
        monstruo2image7=pygame.image.load("images/goblinw/guerrero1_7.png").convert_alpha()
        monstruo2image8=pygame.image.load("images/goblinw/guerrero1_8.png").convert_alpha()
        monstruo2image9=pygame.image.load("images/goblinw/guerrero1_9.png").convert_alpha()
    
        #monstre 3 (sNakE)
        monstruo3image1=pygame.image.load("images/goblinw/snake.png").convert_alpha()
        monstruo3image2=pygame.image.load("images/goblinw/snake_2.png").convert_alpha()
        monstruo3image3=pygame.image.load("images/goblinw/snake.png").convert_alpha()
        monstruo3image4=pygame.image.load("images/goblinw/snake_2.png").convert_alpha()
        monstruo3image5=pygame.image.load("images/goblinw/snake.png").convert_alpha()
        monstruo3image6=pygame.image.load("images/goblinw/snake_2.png").convert_alpha()
        monstruo3image7=pygame.image.load("images/goblinw/snake.png").convert_alpha()
        monstruo3image8=pygame.image.load("images/goblinw/snake_3.png").convert_alpha()
        monstruo3image9=pygame.image.load("images/goblinw/snake_4.png").convert_alpha()
        monstruo3image10=pygame.image.load("images/goblinw/snake_5.png").convert_alpha()
        monstruo3image11=pygame.image.load("images/goblinw/snake.png").convert_alpha()
    
        #imatges dels arbres
        tree1image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree2image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree3image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
    
    
        #imatge eskut
        escut_i=pygame.image.load("images/goblinw/escudo_m.png").convert_alpha()
        
        
        
        #sprite del goblin
        sprite1=pygame.sprite.Sprite()
        sprite1.image=goblin1
        sprite1.rect=goblin1.get_rect()
        sprite1.rect.top=100
        sprite1.rect.left=50
    
        #sprite de la bola de foc
        spritefoc=pygame.sprite.Sprite()
        spritefoc.image=foc1
        spritefoc.rect=foc1.get_rect()
        spritefoc.rect.top=9999
        spritefoc.rect.left=9999
    
        #sprite de monstre pop 1
        spritemonstruo1=pygame.sprite.Sprite()
        spritemonstruo1.image=monstruoimage1
        spritemonstruo1.rect=monstruoimage1.get_rect()
        spritemonstruo1.rect.top=random.randrange(0,570)
        spritemonstruo1.rect.left=random.randrange(0,770)
    
        #sprite de monstre guerrer 2
        sger=pygame.sprite.Sprite()
        sger.image=monstruo2image1
        sger.rect=monstruo2image1.get_rect()
        sger.rect.top=random.randrange(0,570)
        sger.rect.left=random.randrange(0,770)
    
        #sprite del snake 3
        smonster=pygame.sprite.Sprite()
        smonster.image=monstruo3image1
        smonster.rect=monstruo3image1.get_rect()
        smonster.rect.top=random.randrange(0,570)
        smonster.rect.left=random.randrange(0,770)
    
        #sprite de leskut
        spritee=pygame.sprite.Sprite()
        spritee.image=escut_i
        spritee.rect=escut_i.get_rect()
        spritee.rect.top=sprite1.rect.top
        spritee.rect.left=sprite1.rect.left
    
        #sprites dels arbres
    
        #arbre 1 ########################################################
        sa1=pygame.sprite.Sprite()
        sa1.image=tree1image
        sa1.rect=tree1image.get_rect()
        sa1.rect.top=280
        sa1.rect.left=60
    
        sa2=pygame.sprite.Sprite()
        sa2.image=tree1image
        sa2.rect=tree1image.get_rect()
        sa2.rect.top=95
        sa2.rect.left=372
    
        sa3=pygame.sprite.Sprite()
        sa3.image=tree1image
        sa3.rect=tree1image.get_rect()
        sa3.rect.top=350
        sa3.rect.left=677
    
        r_a1=pygame.Rect(87,320,10,30)
        r_a2=pygame.Rect(400,135,10,30)
        r_a3=pygame.Rect(705,392,10,30)
        
    
        #fuentes
        fuente1=pygame.font.SysFont("Arial",16,True,False)
        fuentevidapj=pygame.font.SysFont("Arial",25,True,False)
        fuenteGO=pygame.font.SysFont("Arial",70,True,False)
    
        
    
        #colors:
        rojo=(255,0,0)
        azul=(0,0,255)
        verde=(0,255,0)
        blanco=(255,255,255)
        negro=(0,0,0)
    
        #textos constants
        textoGO=fuenteGO.render('GAME OVER',0,rojo)
        textoV=fuenteGO.render('NIVEL COMPLETADO',0,azul)
        
    
        #altres variables i contadors
        cont5=0
        cont4=0
        cont3=0
        cont1=0
        cont2=0
        cont6=0
        cont11=0
        cont12=0
        cont13=0
        cont15=0
        cont16=0
        cont17=0
        cont18=0
        cont19=0
        cont20=0
        cont21=0
        cont22=0
        contx=0
        cont23=0
        cont24=0
        cont25=0
        contG=0
        contE1=0
        contE2=0
        contE3=0
        contC1=0
        contC2=0
        contC3=0
        cont_escudo=0
        cont_terremoto=0
        #########
        var1=1
        var2=0
        var3=True  #<---variable per saber si el monstre esta viu
        var3_2=True #<---variable per saber si el monstre 2 esta viu
        var3_3=False #<---variable per saber si el monster 3 esta viu
        var4=0
        vr3=var3
        vr3_2=var3_2
        vr3_3=var3_3
        var7=0
        var8=False # variable k indica si san matat prous pops per finalitzar el nivell
        var8_2=False
        var8_3=False
        var9=False
        var_c1=True
        var_c2=True
        var_c3=True
        var_escudo=False
        var_potion=False
        var_terremoto=False
    
        #variables per saber si sesta atacant o si sa tirat magia
        var_attack=False
        var_magia=False
    
        #vida monstres i pj
        hpmonstruo1=100
        hpmonstruo2=100
        hpmonstruo3=50
    
        #per llegir les pocions
        potionsreader=open('log\potions.txt')
        potionshp=int(potionsreader.readlines()[0])
        print 'potions hp: ', potionshp
        potionsreader.close()
        
        potionsreader=open('log\potions.txt')
        potionsmp=int(potionsreader.readlines()[1])
        print 'potions mp: ', potionsmp
        potionsreader.close()
    
    
    
    
    
    
    
    #escudo i atak terratremol
        tendareader=open('log/shop.txt')
        escudo=int(tendareader.readlines()[0])
        tendareader.close()
        print 'escudo', escudo
        
        tendareader=open('log/shop.txt')
        terremoto=int(tendareader.readlines()[1])
        tendareader.close()
        print 'terremoto', terremoto
        
    
    
    
    
        
    
    #per llegir el hp del pj:
        datosreader=open('log\datos.txt')
        hpdatos=int(datosreader.readlines()[0])
        print 'hp: ', hpdatos
        datosreader.close()
    
        hp_pj=hpdatos
        hpt_pj=hp_pj
    
        #variable del bucle principal
        salir=False
    
        #reloj
        reloj1=pygame.time.Clock()
    
        #grup de sprites de monstres
        grupo_m=pygame.sprite.Group(spritemonstruo1,sger,smonster)
    
        #mp del pj
    
        #per llegir el mp del pj:
    
        datosreader=open('log\datos.txt')
        mpdatos=int(datosreader.readlines()[1])
        print 'mp: ', mpdatos
        datosreader.close()
        
        mptpj=mpdatos
        mppj=mptpj
    
        #variable diners
        moneyreader=open('log\money.txt')
        money=int(moneyreader.readline())
        print 'dinero:', money
        moneyreader.close()
    
        money_t=str(money)
        moneywriter=open('log\money.txt','w')
        moneywriter.write(money_t)
        moneywriter.close()
    
        perdrediners=money
        
    
        sonido3.play()
    
    
        while salir != True:
            
            
            var_potion=False
    
            hp_pjant=hp_pj
    
            if hp_pj<=0 and var1==1:
                sprite1.image=goblindr
    
            if hp_pj<=0 and var1==2:
                sprite1.image=goblindl
                
    
            xant=sprite1.rect.left
            yant=sprite1.rect.top
    
            if hpmonstruo1<0:
                hpmonstruo1==0
            
            if hpmonstruo1==0:
                spritemonstruo1.image=monstruoimage3
    
    
    
            if hpmonstruo2<0:
                hpmonstruo2==0
            
            if hpmonstruo2==0:
                sger.image=monstruo2image9
    
                
    
            if hpmonstruo3<0:
                hpmonstruo3==0
            
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
                
    
            if hp_pj<0:
                hp_pj=0
                
    
    
            xmant1=smonster.rect.left
            ymant1=smonster.rect.top
            xmant2=sger.rect.left
            ymant2=sger.rect.top
            xmant3=spritemonstruo1.rect.left
            ymant3=spritemonstruo1.rect.top
    
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN and hp_pj>0:
    
                    if event.key==pygame.K_LEFT and sprite1.rect.left>0:
                        if cont1==0:
                            sprite1.image=goblinwl1
                        if cont1==1:
                            sprite1.image=goblinwl2
                        if cont1==2:
                            sprite1.image=goblinwl3
                        if cont1==3:
                            sprite1.image=goblinwl4
                        if cont1==4:
                            sprite1.image=goblinwl3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left-=6
                        cont1+=1
                        var1=2
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
                        
    
                    if event.key==pygame.K_RIGHT and sprite1.rect.left<775:
                        if cont1==0:
                            sprite1.image=goblinwr1
                        if cont1==1:
                            sprite1.image=goblinwr2
                        if cont1==2:
                            sprite1.image=goblinwr3
                        if cont1==3:
                            sprite1.image=goblinwr4
                        if cont1==4:
                            sprite1.image=goblinwr3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left+=6
                        cont1+=1
                        var1=1
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_UP and sprite1.rect.top>0:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
                            
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top-=6
                        cont1+=1
                        var4=1
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_DOWN and sprite1.rect.top<555:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top+=6
                        cont1+=1
                        var4=2
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_SPACE:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinar2
                            if cont1==1:
                                sprite1.image=goblinar1
                            if cont1==2:
                                sprite1.image=goblinar1
                            if cont1==3:
                                sprite1.image=goblinar2
                            if cont1==4:
                                sprite1.image=goblinar3
                            if cont1>=5:
                                cont1=0
                                sprite1.image=goblinar2
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinal2
                            if cont1==1:
                                sprite1.image=goblinal1
                            if cont1==2:
                                sprite1.image=goblinal2
                            if cont1==3:
                                sprite1.image=goblinal3
                            if cont1>=4:
                                cont1=0
                                sprite1.image=goblinal2
                                
                        cont1+=1
                        var_attack=True
                        if cont1%2==0:
                            sonidoespadaF.play()
    
                        
                            
    
                        
                    if event.key==pygame.K_m:
                        if cont2<=3:
                            if var1==1:
                                sprite1.image=goblinamr
                            if var1==2:
                                sprite1.image=goblinaml
                        if cont2==4:
                            if var1==1:
                                sprite1.image=goblin1
                            if var1==2:
                                sprite1.image=goblin2
                        if cont2==1 and mppj>=20:
                            var_magia=True
                        cont2+=1
    
                    if event.key==pygame.K_h and potionshp>0 and hp_pj>0:
                        if hp_pj<hpt_pj:
                            potionshp-=1
                            hp_pj+=random.randrange(15,20)
                            var_potion=True
                            
                            sopotion.play()
                            print 'potionshp: ', potionshp
                            if hp_pj>hpt_pj:
                                hp_pj=hpt_pj
    
                    if event.key==pygame.K_j and potionsmp>0 and hp_pj>0:
                        if mppj<mptpj:
                            potionsmp-=1
                            mppj+=random.randrange(10,20)
                            sopotion.play()
                            print 'potionsmp: ', potionsmp
                            
                            if mppj>mptpj:
                                mppj=mptpj
    
                    if event.key==pygame.K_n and escudo==1 and hp_pj>0 and mppj>=60:
                        mppj-=60
                        var_escudo=True
                        print 'escudo activado'
                    
                    if event.key==pygame.K_b and terremoto==1 and hp_pj>0 and mppj>=250 and var_terremoto==False:
                        mppj-=250
                        var_terremoto=True
                        print 'terremoto activado'
    
                    
    
                    if event.key==pygame.K_ESCAPE:
                        sonido3.stop()
                        menu1()
                            
                            
                    
                if event.type==pygame.KEYUP and hp_pj>0:
                    if var1==1:
                        sprite1.image=goblin1
                    if var1==2:
                        sprite1.image=goblin2
                        
                    var_attack=False
                    cont2=0
                    cont1=0
                    
    
            reloj1.tick(17)
            
            
            pantalla.blit(fondo,(0,0))
            if var_terremoto==True:
                if var3==True:
                    hpmonstruo1=0
                if var3_2==True:
                    hpmonstruo2=0
                if var3_3==True and var7==1:
                    hpmonstruo3=0
                s_terremoto.play()
                cont_terremoto+=1
                if cont_terremoto%2==0:
                    pantalla.blit(fondo,(random.randrange(0,5),random.randrange(0,5)))
                else:
                    pantalla.blit(fondo,(0,0))
            if cont_terremoto==10:
                var_terremoto=False
                cont_terremoto=0
    
            pantalla.blit(sprite1.image,sprite1.rect)
    
            
    
            if var3==True:
                pantalla.blit(spritemonstruo1.image,spritemonstruo1.rect)
    
    
            if var3_2==True:
                pantalla.blit(sger.image,sger.rect)
    
            
            
            #MOVIMENTS DEL MONSTRE 1 (pop)
                
            if var3==True and hpmonstruo1>0 and hp_pj>0:
                variable1=random.randrange(0,5)
    
    
                if variable1==0 or variable1==1:
                    if spritemonstruo1.rect.left<770 and sprite1.rect.left>spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left+=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage5
                if variable1==1 or variable1==2:
                    if spritemonstruo1.rect.top<570 and sprite1.rect.top>spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top+=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage1
                if variable1==2 or variable1==3:
                    if spritemonstruo1.rect.top>15 and sprite1.rect.top<spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top-=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage6
                if variable1==3 or variable1==0:
                    if spritemonstruo1.rect.left>15 and sprite1.rect.left<spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left-=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage4
    
            #MOVIMENTS DEL MONSTRE 2 (guerrer daurat)
                
            if var3_2==True and hpmonstruo2>0 and hp_pj>0:
                variable1_2=random.randrange(0,5)
    
    
                if variable1_2==0 or variable1_2==1:
                    if sger.rect.left<770 and sprite1.rect.left>sger.rect.left:
                        sger.rect.left+=random.randrange(0,10)
                        sger.image=monstruo2image2
                if variable1_2==1 or variable1_2==2:
                    if sger.rect.top<570 and sprite1.rect.top>sger.rect.top:
                        sger.rect.top+=random.randrange(0,7)
                        sger.image=monstruo2image1
                if variable1_2==2 or variable1_2==3:
                    if sger.rect.top>15 and sprite1.rect.top<sger.rect.top:
                        sger.rect.top-=random.randrange(0,7)
                        sger.image=monstruo2image6
                if variable1_2==3 or variable1_2==0:
                    if sger.rect.left>15 and sprite1.rect.left<sger.rect.left:
                        sger.rect.left-=random.randrange(0,10)
                        sger.image=monstruo2image1
    
            
                        
                        
            #"INVOCACIO" BOLA DE FOC
                        
            if var_magia==True and cont5==0 and mppj>20:
                #sprite de la bola de foc
                spritefoc=pygame.sprite.Sprite()
                spritefoc.image=foc1
                spritefoc.rect=foc1.get_rect()
                if var4==0:
                    spritefoc.rect.top=sprite1.rect.top+5
                if var4==1 or var4==2:
                    spritefoc.rect.left=sprite1.rect.left+5
    
                if var1==1 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left+20
                if var1==2 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left-20
                if var4==1:
                    spritefoc.rect.top=sprite1.rect.top-20
                if var4==2:
                    spritefoc.rect.top=sprite1.rect.top+20
    
                mppj-=20
                sonido2.play()
                cont5+=1
    
            #MOVIMENTS BOLA DE FOC
            if var_magia==True:
                pantalla.blit(spritefoc.image,spritefoc.rect)
                if cont3==0:
                    cont3+=1
                    if var1==1 and var4==0:
                        var2=1
                    if var1==2 and var4==0:
                        var2=2
                    if var4==1:
                        var2=3
                    if var4==2:
                        var2=4
    
                if cont3>0 and cont4<70:
                    if var2==1:
                        spritefoc.rect.left+=10
                    if var2==2:
                        spritefoc.rect.left-=10
                    if var2==3:
                        spritefoc.rect.top-=10
                    if var2==4:
                        spritefoc.rect.top+=10
                    cont4+=2
    
            if spritefoc.rect.left<0 or spritefoc.rect.left>800 or cont4>=70:
                var_magia=False
                
            if var_magia==False:
                cont3=0
                cont4=0
                cont5=0
                spritefoc.rect.top=99999
                spritefoc.rect.left=99999
    
    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
            var_attackconfirm_l=sprite1.rect.left-spritemonstruo1.rect.left
            var_attackconfirm_t=sprite1.rect.top-spritemonstruo1.rect.top
    
            var_attackconfirm_l_2=sprite1.rect.left-sger.rect.left
            var_attackconfirm_t_2=sprite1.rect.top-sger.rect.top
    
    #accions que infringeixen dany al monstre (pop)
            
            if var3==True:
                if spritefoc.rect.colliderect(spritemonstruo1) and hpmonstruo1>0:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(5,15)
                    if hpmonstruo1<0:
                        hpmonstruo1==0
            
                if var1==1 and var_attackconfirm_l>-20 and var_attackconfirm_l<10 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left+10,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
                if var1==2 and var_attackconfirm_l>-10 and var_attackconfirm_l<20 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left-10)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
    
    #accions que infringeixen dany al monstre (guerrer)
            
            if var3_2==True:
                if spritefoc.rect.colliderect(sger) and hpmonstruo2>0:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(1,4)
                    if hpmonstruo2<0:
                        hpmonstruo2==0
            
                if var1==1 and var_attackconfirm_l_2>-25 and var_attackconfirm_l_2<20 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left+10,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
                if var1==2 and var_attackconfirm_l_2>-20 and var_attackconfirm_l_2<25 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left-10)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
    
    
    #accions que infringeixen dany al pj (pop)
                        
            if var3==True and spritemonstruo1.rect.colliderect(sprite1.rect) and hpmonstruo1>0 and hp_pj>0:
                hp_pj-=random.randrange(0,2)
                sprite1.rect.left-=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo1<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
    
    #accions que infringeixen dany al pj (guerrer d)
                        
            if var3_2==True and sger.rect.colliderect(sprite1.rect) and hpmonstruo2>0 and hp_pj>0:
                hp_pj-=random.randrange(1,4)
                sprite1.rect.left+=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo2<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
            
    
    #axo serveix perk no senkalli el pj en matar el monstre
            #if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6<50 and hpmonstruo1==0:
             #   sprite1.rect.left+=10
                
            #if sprite1.rect.colliderect(sger.rect) and cont6<50 and hpmonstruo2==0:
             #   sprite1.rect.left+=10
            
    #vida dels monstres          
            if var3==True:       
                hpm1=str(str(hpmonstruo1)+'/100')
    
            if var3_2==True:
                hpm2=str(str(hpmonstruo2)+'/100')
    
    #per fer desaparexer el pop un kop mort:
            if hpmonstruo1<=0 and cont6<70:
                hpmonstruo1=0
                cont6+=1
                if cont6==70:
                    cont6=0
                    var3=False
                    spritemonstruo1.rect.top=9999
                    spritemonstruo1.rect.left=9999
    
    #per fer desaparexer el guerrer un kop mort:
            if hpmonstruo2<=0 and cont15<70:
                hpmonstruo2=0
                cont15+=1
                if cont15==70:
                    cont15=0
                    var3_2=False
                    sger.rect.top=9999
                    sger.rect.left=9999
    
    
    #imprimacio de la vida dels monstres
            #pop       
            if var3==True:
                textohp1=fuente1.render(hpm1,0,rojo)
                pantalla.blit(textohp1,(spritemonstruo1.rect.left-10,spritemonstruo1.rect.top-25))
    
            #guerrer
            if var3_2==True:
                textohp2=fuente1.render(hpm2,0,rojo)
                pantalla.blit(textohp2,(sger.rect.left-10,sger.rect.top-25))
    
    
    #sistema k fa k el pj no travessi el monstre
            if hpmonstruo1==0:
                if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6>10 and var_c1==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
            if hpmonstruo2==0:
                if sprite1.rect.colliderect(sger.rect) and cont6>10 and var_c2==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
    
    
            if var3==False and cont11==0:
                cont6=0
                cont11+=1
    
            if var3==False and cont12==0:
                cont6=0
                cont12+=1
    
            if hp_pj==0:
                cont13+=1
    
            if cont13==50:
                sonido3.stop()
                menu1()
    
            if hp_pj<=0:
                pantalla.blit(textoGO,(200,200))
                if cont13==1:
                    sonidodead.play()
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                elif cont13==20:
                    sonidodead.stop()
                
    
    #per saber si sa akabat el nivell:
            if var8==True and var8_2==True and var8_3==True:
                pantalla.blit(textoV,(115,200))
                cont16+=1
                var9=True
                if cont16==60:
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                    sonido3.stop()
                    menu1()
    
    
                
                
            
    ###############################################################################
    ###############################################################################
    
    
            if vr3==False or vr3_2==False:
                    var7=1
                #si el monstre esta viu la imatge simprimex en la pantacha
                    
            if var7==1:
                if var3_3==True:
                    pantalla.blit(smonster.image,smonster.rect)
                    
    
                    #moviments
                        
                    if var3_3==True and hpmonstruo3>0 and hp_pj>0:
                        variable1_3=random.randrange(0,5)
    
                        
                        
                        if variable1_3==0 or variable1_3==1:
                            if smonster.rect.left<770 and sprite1.rect.left>smonster.rect.left:
                                smonster.rect.left+=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image5
                                if variable1_3==1:
                                    smonster.image=monstruo3image8
                        if variable1_3==1 or variable1_3==2:
                            if smonster.rect.top<570 and sprite1.rect.top>smonster.rect.top:
                                smonster.rect.top+=random.randrange(0,25)
                                if variable1_3==0:
                                    smonster.image=monstruo3image5
                                if variable1_3==1:
                                    smonster.image=monstruo3image8
                        if variable1_3==2 or variable1_3==3:
                            if smonster.rect.top>15 and sprite1.rect.top<smonster.rect.top:
                                smonster.rect.top-=random.randrange(0,25)
                                if variable1_3==0:
                                    smonster.image=monstruo3image4
                                if variable1_3==1:
                                    smonster.image=monstruo3image9
                        if variable1==3 or variable1_3==0:
                            if smonster.rect.left>15 and sprite1.rect.left<smonster.rect.left:
                                smonster.rect.left-=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image4
                                if variable1_3==3:
                                    smonster.image=monstruo3image9
    
            
    
    
    
                    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
                    var_attackconfirm_l_3=sprite1.rect.left-smonster.rect.left
                    var_attackconfirm_t_3=sprite1.rect.top-smonster.rect.top
    
                #accions que infringeixen dany al monstre (snake)
    
                    if var3_3==True:
                        if spritefoc.rect.colliderect(smonster) and hpmonstruo3>0:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(5,15)
                            if hpmonstruo3<0:
                                hpmonstruo3==0
    
                        if var1==1 and var_attackconfirm_l_3>-20 and var_attackconfirm_l_3<10 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left+10,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
                        if var1==2 and var_attackconfirm_l_3>-10 and var_attackconfirm_l_3<20 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left-10)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
    
    
                    #accions que infringeixen dany al pj (snake)
                                
                    if var3_3==True and smonster.rect.colliderect(sprite1.rect) and hpmonstruo3>0 and hp_pj>0:
                        hp_pj-=random.randrange(0,2)
                        sprite1.rect.left-=random.randrange(-5,5)
                        sprite1.rect.top+=random.randrange(-5,5)
    
                        if var1==1:
                            sprite1.image=goblinhr
                        if var1==2:
                            sprite1.image=goblinhl
    
                    if hpmonstruo3<0:
                        hpmonstruo3==0
    
    
                    hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    textohppj=fuente1.render(hppjt,0,verde)
                    pantalla.blit(textohppj,(5,5))
    
    
                    #axo serveix perk no senkalli el pj en matar el monstre
                    #if sprite1.rect.colliderect(smonster.rect) and cont6<50 and hpmonstruo3==0:
                     #   sprite1.rect.left+=10
                        
    
                    #vida dels monstres          
                    if var3_3==True:       
                        hpm3=str(str(hpmonstruo3)+'/50')
    
                    #per fer desaparexer el snake un kop mort:
                    
                    if hpmonstruo3<=0 and cont17<70:
                        hpmonstruo3=0
                        cont17+=1
                        if cont17==70:
                            cont17=0
                            var3_3=False
                            smonster.rect.top=9999
                            smonster.rect.left=9999
    
    
                    #imprimacio de la vida dels monstres       
                    if var3_3==True:
                        textohp1=fuente1.render(hpm3,0,rojo)
                        pantalla.blit(textohp1,(smonster.rect.left-10,smonster.rect.top-25))
    
    
                    #sistema k fa k el pj no travessi el monstre
                    if hpmonstruo3==0:
                        if sprite1.rect.colliderect(smonster.rect) and cont6>10 and var_c3==True:
                            sprite1.rect.left=xant
                            sprite1.rect.top=yant
    
                    
    
    
    
    
                    if var3_3==False and cont11==0:
                        cont6=0
                        cont11+=1
    
                    if var3_3==False and cont12==0:
                        cont6=0
                        cont12+=1
    
    
    
            vr3=var3
            vr3_2=var3_2
            vr3_3=var3_3
    
            
    
    
    #si el pop esta mort i sa mort menys de 4 vegades torna a aparexer depen del resultat de f
            if vr3==False and cont19<2:
                f=1
                if f==1:
                    spritemonstruo1=pygame.sprite.Sprite()
                    spritemonstruo1.image=monstruoimage1
                    spritemonstruo1.rect=monstruoimage1.get_rect()
                    spritemonstruo1.rect.top=random.randrange(0,570)
                    spritemonstruo1.rect.left=random.randrange(0,770)
                    hpmonstruo1=100
                    cont6=0
                    var3=True
                    cont19+=1
                    cont23=0
            if cont19==2 and var3==False:
                var8=True
                
    #
            if vr3_2==False and cont20<1:
                f2=1
                if f2==1:
                    sger=pygame.sprite.Sprite()
                    sger.image=monstruo2image1
                    sger.rect=monstruo2image1.get_rect()
                    sger.rect.top=random.randrange(0,570)
                    sger.rect.left=random.randrange(0,770)
                    hpmonstruo2=100
                    cont6=0
                    var3_2=True
                    cont20+=1
                    cont24=0
            if cont20==1 and var3_2==False:
                var8_2=True
    
    
    
            if vr3_3==False and cont21<5:
                f3=1
                if f3==1:
                    smonster=pygame.sprite.Sprite()
                    smonster.image=monstruo3image1
                    smonster.rect=monstruo3image1.get_rect()
                    smonster.rect.top=random.randrange(0,570)
                    smonster.rect.left=random.randrange(0,770)
                    hpmonstruo3=50
                    cont6=0
                    var3_3=True
                    cont21+=1
                    cont25=0
            if cont21==5 and var3_3==False:
                var8_3=True
    
                
    ####AKI ANIRA LU MATEX K LU DEL POP AM ELS ALTRES 2 MONSTRES
    
    #per k es recargi el mp:
            cont18+=1
            if cont18%10==0 and mppj<mpdatos:
                mppj+=1
        
    #imprimacio del mp:
            mppjt=str('MP: '+str(mppj)+'/'+str(mptpj))
            textomppj=fuente1.render(mppjt,0,verde)
            pantalla.blit(textomppj,(700,5))
    
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
    
    #per guardar la kantitat de diners i desblokejar el seguen nivell si sa completat la misio
            if var9==True:
                money_t=str(money)
                moneywriter=open('log\money.txt','w')
                moneywriter.write(money_t)
                moneywriter.close()
            
                moneyreader=open('log\money.txt')
                money=int(moneyreader.readline())
                moneyreader.close()
    
                if mision==1:
                    misionwriter=open('log\misions.txt','w')
                    misionwriter.write('2')
                    misionwriter.close()
    
            
    
    #per sumar diners al matar els monstres:
            if cont23==0 and hpmonstruo1==0:
                cont23+=1
                money+=random.randrange(8,15)
                print 'dinero:', money
    
            if cont24==0 and hpmonstruo2==0:
                cont24+=1
                money+=random.randrange(20,30)
                print 'dinero:', money
    
            if cont25==0 and hpmonstruo3==0:
                cont25+=1
                money+=random.randrange(4,10)
                print 'dinero:', money
    
                
                
    
            if hp_pj==0:
                money=perdrediners
                
                if contx==0:
                    print 'dinero: ', money
                    contx+=1
    
            tttmoney=str('Dinero: '+str(money))
            textomoney=fuente1.render(tttmoney,0,verde)
            pantalla.blit(textomoney,(200,5))
    
            misionreader=open('log\misions.txt')
            mision=int(misionreader.readline())
            misionreader.close()
    
        
            if sprite1.rect.colliderect(r_a1) or sprite1.rect.colliderect(r_a2) or sprite1.rect.colliderect(r_a3):     
                sprite1.rect.left=xant
                sprite1.rect.top=yant
    
    #prk el pj no surti del mapa:
            if sprite1.rect.left<=0:
                sprite1.rect.left=0
            if sprite1.rect.top<=0:
                sprite1.rect.top=0
            if sprite1.rect.left>=780:
                sprite1.rect.left=780
            if sprite1.rect.top>=550:
                sprite1.rect.top=550
    
    #prk els monstres no chokin am les palmeras:
            if smonster.rect.colliderect(r_a1) or smonster.rect.colliderect(r_a2) or smonster.rect.colliderect(r_a3):
                smonster.rect.left=xmant1
                smonster.rect.top=ymant1
                contE3+=1
            else:
                contE3=0
            if sger.rect.colliderect(r_a1) or sger.rect.colliderect(r_a2) or sger.rect.colliderect(r_a3):
                sger.rect.left=xmant2
                sger.rect.top=ymant2
                contE2+=1
            else:
                contE2=0
            if spritemonstruo1.rect.colliderect(r_a1) or spritemonstruo1.rect.colliderect(r_a2) or spritemonstruo1.rect.colliderect(r_a3):
                spritemonstruo1.rect.left=xmant3
                spritemonstruo1.rect.top=ymant3
                contE1+=1
            else:
                contE1=0
    
            #imprimacio dels arbres
            pantalla.blit(sa1.image,sa1.rect)
            pantalla.blit(sa2.image,sa2.rect)
            pantalla.blit(sa3.image,sa3.rect)
    
    #perk el pj no senkalli am els monstres:
            if hpmonstruo1==0 and sprite1.rect.colliderect(spritemonstruo1)==False:
                var_c1=True
            if hpmonstruo2==0 and sprite1.rect.colliderect(sger)==False:
                var_c2=True
            if hpmonstruo3==0 and sprite1.rect.colliderect(smonster)==False:
                var_c3=True
    
            if hpmonstruo1>0:
                var_c1=False
            if hpmonstruo2>0:
                var_c2=False
            if hpmonstruo3>0:
                var_c3=False
    
    #per si el monstre aparex sobre un arbre k es mogi per no enkallarse
            #if contE3==2:
             #   spritemonstruo1.rect.left+=10  
            #if contE2==2:
             #   sger.rect.left+=10
            #if contE1==2:
             #   smonster.rect.left+=10
    
    #perk kridin els monstres kuan morin:
            if hpmonstruo1==0 and contC1==0:
                sonidocrit1.play()
                contC1+=1
            if hpmonstruo1>0:
                contC1=0
    
            if hpmonstruo2==0 and contC2==0:
                sonidocrit2.play()
                contC2+=1
            if hpmonstruo2>0:
                contC2=0
    
            if hpmonstruo3==0 and contC3==0:
                sonidocrit3.play()
                contC3+=1
            if hpmonstruo3>0:
                contC3=0
    
            #textos pocions:
            potionhpt=str('Pociones HP: '+str(potionshp))
            potionmpt=str('Pociones MP: '+str(potionsmp))
            textohpp=fuente1.render(potionhpt,0,verde)
            textompp=fuente1.render(potionmpt,0,verde)
            pantalla.blit(textohpp,(350,5))
            pantalla.blit(textompp,(500,5))
    
    
            if var_escudo==True:
                spritee.rect.top=sprite1.rect.top-15
                spritee.rect.left=sprite1.rect.left-25
            else:
                spritee.rect.top=999999
                spritee.rect.left=999999
    
            if var_escudo==True:
                cont_escudo+=1
                
            if var_escudo==True and var_potion==False:
                hp_pj=hp_pjant
    
            if cont_escudo==100:
                var_escudo=False
                cont_escudo=0
            
            
                
    
            
            
    
            pantalla.blit(spritee.image,spritee.rect)
            
            #per fer k leskut giri :)
            if var_escudo==True:
                escut_i=pygame.transform.rotate(escut_i, 90)
                spritee.image=escut_i
    
            contG+=1
            
            pygame.display.update()
        pygame.quit()
    
        
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    
                            #####segon nivell#####
        
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    
    def guerra2():
        pygame.init()
        pygame.key.set_repeat(20)
        pantalla=pygame.display.set_mode((800,600))
        fondo=pygame.image.load("images/goblinw/fonspedra.png")
        pygame.display.set_caption('GOBLIN W.')
    
        #rectangles dels arbres
        r_a1=pygame.Rect(80,300,10,30)
        r_a2=pygame.Rect(400,200,10,30)
        r_a3=pygame.Rect(700,400,10,30)
    
        #pygame.draw.rect(pantalla,(0,0,0),r_a1)
        #pygame.draw.rect(pantalla,(0,0,0),r_a2)
        #pygame.draw.rect(pantalla,(0,0,0),r_a3)
    
    
        #SONS
        sonido1=pygame.mixer.Sound("sounds/goblinw/Blast.wav")
        sonido2=pygame.mixer.Sound("sounds/goblinw/explosion.wav")
        sonido3=pygame.mixer.Sound("sounds/goblinw/BSO3.wav")
        sonidodead=pygame.mixer.Sound("sounds/goblinw/deadpj.wav")
        sonidoespada=pygame.mixer.Sound("sounds/goblinw/Sspada.wav")
        sonidoespadaF=pygame.mixer.Sound("sounds/goblinw/SspadaF.wav")
        sonidocrit1=pygame.mixer.Sound("sounds/goblinw/crit1.wav")
        sonidocrit2=pygame.mixer.Sound("sounds/goblinw/crit2.wav")
        sonidocrit3=pygame.mixer.Sound("sounds/goblinw/crit3.wav")
        sonidorun=pygame.mixer.Sound("sounds/goblinw/run.wav")
        sopotion=pygame.mixer.Sound("sounds/goblinw/potion.wav")
        s_terremoto=pygame.mixer.Sound("sounds/goblinw/terremoto.wav")
        #sonidocrit3=pygame.mixer.Sound("sounds/goblinw/.wav")
    
        
        #goblin parat
        goblin1=pygame.image.load("images/goblinw/Idle0.png").convert_alpha()
        goblin2=pygame.image.load("images/goblinw/Idle1.png").convert_alpha()
    
        #goblin caminant cap a la dreta
        goblinwr1=pygame.image.load("images/goblinw/Walk0.png").convert_alpha()
        goblinwr2=pygame.image.load("images/goblinw/Walk1.png").convert_alpha()
        goblinwr3=pygame.image.load("images/goblinw/Walk2.png").convert_alpha()
        goblinwr4=pygame.image.load("images/goblinw/Walk3.png").convert_alpha()
    
        #goblin caminant cap a leskerra
        goblinwl1=pygame.image.load("images/goblinw/Walkl0.png").convert_alpha()
        goblinwl2=pygame.image.load("images/goblinw/Walkl1.png").convert_alpha()
        goblinwl3=pygame.image.load("images/goblinw/Walkl2.png").convert_alpha()
        goblinwl4=pygame.image.load("images/goblinw/Walkl3.png").convert_alpha()
    
        #goblin atakant cap a la dreta
        goblinar1=pygame.image.load("images/goblinw/Attack0.png").convert_alpha()
        goblinar2=pygame.image.load("images/goblinw/Attack1.png").convert_alpha()
        goblinar3=pygame.image.load("images/goblinw/Attack2.png").convert_alpha()
    
        #goblin atacant cap a leskerra
        goblinal1=pygame.image.load("images/goblinw/Attackl0.png").convert_alpha()
        goblinal2=pygame.image.load("images/goblinw/Attackl1.png").convert_alpha()
        goblinal3=pygame.image.load("images/goblinw/Attackl2.png").convert_alpha()
    
        #goblin atacant am magia cap a la dreta
        goblinamr=pygame.image.load("images/goblinw/Attackmr.png").convert_alpha()
    
        #goblin atacant am magia kap a leskerra
        goblinaml=pygame.image.load("images/goblinw/Attackml.png").convert_alpha()
    
        #goblin mort 1
        goblindr=pygame.image.load("images/goblinw/Dead0.png").convert_alpha()
    
        #goblin mort 2
        goblindl=pygame.image.load("images/goblinw/Dead1.png").convert_alpha()
    
        #goblin golpejat 1
        goblinhr=pygame.image.load("images/goblinw/Hurt0.png").convert_alpha()
    
        #goblin golpejat 2
        goblinhl=pygame.image.load("images/goblinw/Hurt1.png").convert_alpha()
    
        
        #bola de foc
        foc1=pygame.image.load("images/goblinw/foc.png").convert_alpha()
    
        #monstres
        
        #POP
        monstruoimage1=pygame.image.load("images/goblinw/monstruo2.png").convert_alpha()
        monstruoimage3=pygame.image.load("images/goblinw/monstruo2_3.png").convert_alpha()
        monstruoimage4=pygame.image.load("images/goblinw/monstruo2_4.png").convert_alpha()
        monstruoimage5=pygame.image.load("images/goblinw/monstruo2_5.png").convert_alpha()
        monstruoimage6=pygame.image.load("images/goblinw/monstruo2_6.png").convert_alpha()
    
        #GUERRER DAURAT
        monstruo2image1=pygame.image.load("images/goblinw/guerrero2.png").convert_alpha()
        monstruo2image2=pygame.image.load("images/goblinw/guerrero2_2.png").convert_alpha()
        monstruo2image3=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
        monstruo2image4=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
        monstruo2image5=pygame.image.load("images/goblinw/guerrero2_5.png").convert_alpha()
        monstruo2image6=pygame.image.load("images/goblinw/guerrero2_6.png").convert_alpha()
        monstruo2image7=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
        monstruo2image8=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
        monstruo2image9=pygame.image.load("images/goblinw/guerrero2_7.png").convert_alpha()
    
        #monstre 3 (sNakE)
        monstruo3image1=pygame.image.load("images/goblinw/snake.png").convert_alpha()
        monstruo3image2=pygame.image.load("images/goblinw/snake_2.png").convert_alpha()
        monstruo3image3=pygame.image.load("images/goblinw/snake.png").convert_alpha()
        monstruo3image4=pygame.image.load("images/goblinw/snake_2.png").convert_alpha()
        monstruo3image5=pygame.image.load("images/goblinw/snake.png").convert_alpha()
        monstruo3image6=pygame.image.load("images/goblinw/snake_2.png").convert_alpha()
        monstruo3image7=pygame.image.load("images/goblinw/snake.png").convert_alpha()
        monstruo3image8=pygame.image.load("images/goblinw/snake_3.png").convert_alpha()
        monstruo3image9=pygame.image.load("images/goblinw/snake_4.png").convert_alpha()
        monstruo3image10=pygame.image.load("images/goblinw/snake_5.png").convert_alpha()
        monstruo3image11=pygame.image.load("images/goblinw/snake.png").convert_alpha()
    
        #imatges dels arbres
        tree1image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree2image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree3image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
    
        #imatges de las rokas
        rock1image=pygame.image.load("images/goblinw/roca.png").convert_alpha()
        rock2image=pygame.image.load("images/goblinw/roca2.png").convert_alpha()
    
        #imatge eskut
        escut_i=pygame.image.load("images/goblinw/escudo_m.png").convert_alpha()
        
        #sprite del goblin
        sprite1=pygame.sprite.Sprite()
        sprite1.image=goblin1
        sprite1.rect=goblin1.get_rect()
        sprite1.rect.top=100
        sprite1.rect.left=50
    
        #sprite de la bola de foc
        spritefoc=pygame.sprite.Sprite()
        spritefoc.image=foc1
        spritefoc.rect=foc1.get_rect()
        spritefoc.rect.top=9999
        spritefoc.rect.left=9999
    
        #sprite de monstre pop 1
        spritemonstruo1=pygame.sprite.Sprite()
        spritemonstruo1.image=monstruoimage1
        spritemonstruo1.rect=monstruoimage1.get_rect()
        spritemonstruo1.rect.top=random.randrange(0,570)
        spritemonstruo1.rect.left=random.randrange(0,770)
    
        #sprite de monstre guerrer 2
        sger=pygame.sprite.Sprite()
        sger.image=monstruo2image1
        sger.rect=monstruo2image1.get_rect()
        sger.rect.top=random.randrange(0,570)
        sger.rect.left=random.randrange(0,770)
    
        #sprite del snake 3
        smonster=pygame.sprite.Sprite()
        smonster.image=monstruo3image1
        smonster.rect=monstruo3image1.get_rect()
        smonster.rect.top=random.randrange(0,570)
        smonster.rect.left=random.randrange(0,770)
    
        #sprite de leskut
        spritee=pygame.sprite.Sprite()
        spritee.image=escut_i
        spritee.rect=escut_i.get_rect()
        spritee.rect.top=sprite1.rect.top
        spritee.rect.left=sprite1.rect.left
    
        #sprites de las rokas
        #1
        sr1=pygame.sprite.Sprite()
        sr1.image=rock1image
        sr1.rect=rock1image.get_rect()
        sr1.rect.top=280
        sr1.rect.left=60
        #2
        sr2=pygame.sprite.Sprite()
        sr2.image=rock2image
        sr2.rect=rock2image.get_rect()
        sr2.rect.top=70
        sr2.rect.left=400
        #3
        sr3=pygame.sprite.Sprite()
        sr3.image=rock2image
        sr3.rect=rock2image.get_rect()
        sr3.rect.top=350
        sr3.rect.left=500
        
    
        #arbres k no utilitzu xd
        sa1=pygame.sprite.Sprite()
        sa1.image=tree1image
        sa1.rect=tree1image.get_rect()
        sa1.rect.top=280
        sa1.rect.left=60
    
        sa2=pygame.sprite.Sprite()
        sa2.image=tree1image
        sa2.rect=tree1image.get_rect()
        sa2.rect.top=95
        sa2.rect.left=372
    
        sa3=pygame.sprite.Sprite()
        sa3.image=tree1image
        sa3.rect=tree1image.get_rect()
        sa3.rect.top=350
        sa3.rect.left=677
    
        #r_a1=pygame.Rect(87,320,10,30)
        #r_a2=pygame.Rect(400,135,10,30)
        #r_a3=pygame.Rect(705,392,10,30)
        
    
        #fuentes
        fuente1=pygame.font.SysFont("Arial",16,True,False)
        fuentevidapj=pygame.font.SysFont("Arial",25,True,False)
        fuenteGO=pygame.font.SysFont("Arial",70,True,False)
    
        
    
        #colors:
        rojo=(255,0,0)
        azul=(0,0,255)
        verde=(0,255,0)
        blanco=(255,255,255)
        negro=(0,0,0)
    
        #textos constants
        textoGO=fuenteGO.render('GAME OVER',0,rojo)
        textoV=fuenteGO.render('NIVEL COMPLETADO',0,azul)
    
        #altres variables i contadors
        cont5=0
        cont4=0
        cont3=0
        cont1=0
        cont2=0
        cont6=0
        cont11=0
        cont12=0
        cont13=0
        cont15=0
        cont16=0
        cont17=0
        cont18=0
        cont19=0
        cont20=0
        cont21=0
        cont22=0
        contx=0
        cont23=0
        cont24=0
        cont25=0
        contG=0
        contE1=0
        contE2=0
        contE3=0
        contC1=0
        contC2=0
        contC3=0
        cont_escudo=0
        cont_terremoto=0
        #########
        var1=1
        var2=0
        var3=True  #<---variable per saber si el monstre esta viu
        var3_2=True #<---variable per saber si el monstre 2 esta viu
        var3_3=True #<---variable per saber si el monster 3 esta viu
        var4=0
        vr3=var3
        vr3_2=var3_2
        vr3_3=var3_3
        var7=0
        var8=False # variable k indica si san matat prous pops per finalitzar el nivell
        var8_2=False
        var8_3=False
        var9=False
        var_c1=True
        var_c2=True
        var_c3=True
        var_d2=1
        var_escudo=False
        var_potion=False
        var_terremoto=False
    
        #variables per saber si sesta atacant o si sa tirat magia
        var_attack=False
        var_magia=False
    
        #vida monstres i pj
        hpmonstruo1=120
        hpmonstruo2=100
        hpmonstruo3=50
    
    
        #per llegir les pocions
        potionsreader=open('log\potions.txt')
        potionshp=int(potionsreader.readlines()[0])
        print 'potions hp: ', potionshp
        potionsreader.close()
        
        potionsreader=open('log\potions.txt')
        potionsmp=int(potionsreader.readlines()[1])
        print 'potions mp: ', potionsmp
        potionsreader.close()
    
    
        
    
    
    
    #escudo i atak terratremol
        tendareader=open('log/shop.txt')
        escudo=int(tendareader.readlines()[0])
        tendareader.close()
        print 'escudo', escudo
        
        tendareader=open('log/shop.txt')
        terremoto=int(tendareader.readlines()[1])
        tendareader.close()
        print 'terremoto', terremoto
    
    
    
    
    
        
    
    #per llegir el hp del pj:
        datosreader=open('log\datos.txt')
        hpdatos=int(datosreader.readlines()[0])
        print 'hp: ', hpdatos
        datosreader.close()
    
        hp_pj=hpdatos
        hpt_pj=hp_pj
    
        #variable del bucle principal
        salir=False
    
        #reloj
        reloj1=pygame.time.Clock()
    
        #grup de sprites de monstres
        grupo_m=pygame.sprite.Group(spritemonstruo1,sger,smonster)
    
    #per llegir el mp del pj:
    
        datosreader=open('log\datos.txt')
        mpdatos=int(datosreader.readlines()[1])
        print 'mp: ', mpdatos
        datosreader.close()
        
        #mp del pj
        mptpj=mpdatos
        mppj=mptpj
    
    ######
        #variable diners
        moneyreader=open('log\money.txt')
        money=int(moneyreader.readline())
        print 'dinero:', money
        moneyreader.close()
    
        money_t=str(money)
        moneywriter=open('log\money.txt','w')
        moneywriter.write(money_t)
        moneywriter.close()
    
        perdrediners=money
        
    
        sonido3.play()
    
    
        while salir != True:
            
            var_potion=False
            
            hp_pjant=hp_pj
    
            if hp_pj<=0 and var1==1:
                sprite1.image=goblindr
    
            if hp_pj<=0 and var1==2:
                sprite1.image=goblindl
                
    
            xant=sprite1.rect.left
            yant=sprite1.rect.top
    
            if hpmonstruo1<0:
                hpmonstruo1==0
            
            if hpmonstruo1==0:
                spritemonstruo1.image=monstruoimage3
    
    
    
            if hpmonstruo2<0:
                hpmonstruo2==0
            
            if hpmonstruo2==0:
                sger.image=monstruo2image9
    
                
    
            if hpmonstruo3<0:
                hpmonstruo3==0
            
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
                
    
            if hp_pj<0:
                hp_pj=0
                
    
    
            xmant1=smonster.rect.left
            ymant1=smonster.rect.top
            xmant2=sger.rect.left
            ymant2=sger.rect.top
            xmant3=spritemonstruo1.rect.left
            ymant3=spritemonstruo1.rect.top
    
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN and hp_pj>0:
    
                    if event.key==pygame.K_LEFT and sprite1.rect.left>0:
                        if cont1==0:
                            sprite1.image=goblinwl1
                        if cont1==1:
                            sprite1.image=goblinwl2
                        if cont1==2:
                            sprite1.image=goblinwl3
                        if cont1==3:
                            sprite1.image=goblinwl4
                        if cont1==4:
                            sprite1.image=goblinwl3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left-=6
                        cont1+=1
                        var1=2
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
                        
    
                    if event.key==pygame.K_RIGHT and sprite1.rect.left<775:
                        if cont1==0:
                            sprite1.image=goblinwr1
                        if cont1==1:
                            sprite1.image=goblinwr2
                        if cont1==2:
                            sprite1.image=goblinwr3
                        if cont1==3:
                            sprite1.image=goblinwr4
                        if cont1==4:
                            sprite1.image=goblinwr3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left+=6
                        cont1+=1
                        var1=1
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_UP and sprite1.rect.top>0:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
                            
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top-=6
                        cont1+=1
                        var4=1
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_DOWN and sprite1.rect.top<555:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top+=6
                        cont1+=1
                        var4=2
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_SPACE:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinar2
                            if cont1==1:
                                sprite1.image=goblinar1
                            if cont1==2:
                                sprite1.image=goblinar1
                            if cont1==3:
                                sprite1.image=goblinar2
                            if cont1==4:
                                sprite1.image=goblinar3
                            if cont1>=5:
                                cont1=0
                                sprite1.image=goblinar2
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinal2
                            if cont1==1:
                                sprite1.image=goblinal1
                            if cont1==2:
                                sprite1.image=goblinal2
                            if cont1==3:
                                sprite1.image=goblinal3
                            if cont1>=4:
                                cont1=0
                                sprite1.image=goblinal2
                                
                        cont1+=1
                        var_attack=True
                        if cont1%2==0:
                            sonidoespadaF.play()
    
                        
                            
    
                        
                    if event.key==pygame.K_m:
                        if cont2<=3:
                            if var1==1:
                                sprite1.image=goblinamr
                            if var1==2:
                                sprite1.image=goblinaml
                        if cont2==4:
                            if var1==1:
                                sprite1.image=goblin1
                            if var1==2:
                                sprite1.image=goblin2
                        if cont2==1 and mppj>=20:
                            var_magia=True
                        cont2+=1
    
    
                    if event.key==pygame.K_h and potionshp>0 and hp_pj>0:
                        if hp_pj<hpt_pj:
                            potionshp-=1
                            hp_pj+=random.randrange(15,20)
                            sopotion.play()
                            print 'potionshp: ', potionshp
                            var_potion=True
                            
                            if hp_pj>hpt_pj:
                                hp_pj=hpt_pj
    
                    if event.key==pygame.K_j and potionsmp>0 and hp_pj>0:
                        if mppj<mptpj:
                            potionsmp-=1
                            mppj+=random.randrange(10,20)
                            sopotion.play()
                            print 'potionsmp: ', potionsmp
                            
                            if mppj>mptpj:
                                mppj=mptpj
    
                    if event.key==pygame.K_n and escudo==1 and hp_pj>0 and mppj>=60:
                        mppj-=60
                        var_escudo=True
                        print 'escudo activado'
                        
                    if event.key==pygame.K_b and terremoto==1 and hp_pj>0 and mppj>=250 and var_terremoto==False:
                        mppj-=250
                        var_terremoto=True
                        print 'terremoto activado'
    
    
    
    
    
                    if event.key==pygame.K_ESCAPE:
                        sonido3.stop()
                        menu1()
                            
                            
                    
                if event.type==pygame.KEYUP and hp_pj>0:
                    if var1==1:
                        sprite1.image=goblin1
                    if var1==2:
                        sprite1.image=goblin2
                        
                    var_attack=False
                    cont2=0
                    cont1=0
                    
    
            reloj1.tick(17)
            
            
            pantalla.blit(fondo,(0,0))
            
            if var_terremoto==True:
                if var3==True:
                    hpmonstruo1=0
                if var3_2==True:
                    hpmonstruo2=0
                if var3_3==True and var7==1:
                    hpmonstruo3=0
                s_terremoto.play()
                cont_terremoto+=1
                if cont_terremoto%2==0:
                    pantalla.blit(fondo,(random.randrange(0,5),random.randrange(0,5)))
                else:
                    pantalla.blit(fondo,(0,0))
            if cont_terremoto==10:
                var_terremoto=False
                cont_terremoto=0
    
            pantalla.blit(sprite1.image,sprite1.rect)
    
            
    
            if var3==True:
                pantalla.blit(spritemonstruo1.image,spritemonstruo1.rect)
    
    
            if var3_2==True:
                pantalla.blit(sger.image,sger.rect)
    
            
            
            #MOVIMENTS DEL MONSTRE 1 (pop)
                
            if var3==True and hpmonstruo1>0 and hp_pj>0:
                variable1=random.randrange(0,5)
    
    
                if variable1==0 or variable1==1:
                    if spritemonstruo1.rect.left<770 and sprite1.rect.left>spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left+=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage5
                if variable1==1 or variable1==2:
                    if spritemonstruo1.rect.top<570 and sprite1.rect.top>spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top+=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage1
                if variable1==2 or variable1==3:
                    if spritemonstruo1.rect.top>15 and sprite1.rect.top<spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top-=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage6
                if variable1==3 or variable1==0:
                    if spritemonstruo1.rect.left>15 and sprite1.rect.left<spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left-=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage4
    
            #MOVIMENTS DEL MONSTRE 2 (guerrer daurat)
                
            if var3_2==True and hpmonstruo2>0 and hp_pj>0:
                variable1_2=random.randrange(0,5)
    
    
                if variable1_2==0 or variable1_2==1:
                    if sger.rect.left<770 and sprite1.rect.left>sger.rect.left:
                        sger.rect.left+=random.randrange(0,10)
                        randomvar1=random.randrange(0,2)
                        if randomvar1==0:
                            sger.image=monstruo2image2
                        else:
                            sger.image=monstruo2image3
                        var_d2=1
                            
                if variable1_2==1 or variable1_2==2:
                    if sger.rect.top<570 and sprite1.rect.top>sger.rect.top:
                        sger.rect.top+=random.randrange(0,7)
                        randomvar1=random.randrange(0,2)
                        if var_d2==1:
                            if randomvar1==0:
                                sger.image=monstruo2image2
                            else:
                                sger.image=monstruo2image3
    
                        if var_d2==2:
                            if randomvar1==0:
                                sger.image=monstruo2image1
                            else:
                                sger.image=monstruo2image4
    
                            
                            
                if variable1_2==2 or variable1_2==3:
                    if sger.rect.top>15 and sprite1.rect.top<sger.rect.top:
                        sger.rect.top-=random.randrange(0,7)
                        randomvar1=random.randrange(0,2)
                        if var_d2==1:
                            if randomvar1==0:
                                sger.image=monstruo2image2
                            else:
                                sger.image=monstruo2image3
    
                        if var_d2==2:
                            if randomvar1==0:
                                sger.image=monstruo2image1
                            else:
                                sger.image=monstruo2image4
                        
                        
                            
                if variable1_2==3 or variable1_2==0:
                    if sger.rect.left>15 and sprite1.rect.left<sger.rect.left:
                        sger.rect.left-=random.randrange(0,10)
                        randomvar1=random.randrange(0,2)
                        if randomvar1==0:
                            sger.image=monstruo2image1
                        else:
                            sger.image=monstruo2image4
                        var_d2=2
    
            
                        
                        
            #"INVOCACIO" BOLA DE FOC
                        
            if var_magia==True and cont5==0 and mppj>20:
                #sprite de la bola de foc
                spritefoc=pygame.sprite.Sprite()
                spritefoc.image=foc1
                spritefoc.rect=foc1.get_rect()
                if var4==0:
                    spritefoc.rect.top=sprite1.rect.top+5
                if var4==1 or var4==2:
                    spritefoc.rect.left=sprite1.rect.left+5
    
                if var1==1 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left+20
                if var1==2 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left-20
                if var4==1:
                    spritefoc.rect.top=sprite1.rect.top-20
                if var4==2:
                    spritefoc.rect.top=sprite1.rect.top+20
    
                mppj-=20
                sonido2.play()
                cont5+=1
    
            #MOVIMENTS BOLA DE FOC
            if var_magia==True:
                pantalla.blit(spritefoc.image,spritefoc.rect)
                if cont3==0:
                    cont3+=1
                    if var1==1 and var4==0:
                        var2=1
                    if var1==2 and var4==0:
                        var2=2
                    if var4==1:
                        var2=3
                    if var4==2:
                        var2=4
    
                if cont3>0 and cont4<70:
                    if var2==1:
                        spritefoc.rect.left+=10
                    if var2==2:
                        spritefoc.rect.left-=10
                    if var2==3:
                        spritefoc.rect.top-=10
                    if var2==4:
                        spritefoc.rect.top+=10
                    cont4+=2
    
            if spritefoc.rect.left<0 or spritefoc.rect.left>800 or spritefoc.rect.top>600 or spritefoc.rect.top<0 or cont4>=70 or spritefoc.rect.colliderect(sr1.rect) or spritefoc.rect.colliderect(sr2.rect) or spritefoc.rect.colliderect(sr3.rect):
                var_magia=False
                
            if var_magia==False:
                cont3=0
                cont4=0
                cont5=0
                spritefoc.rect.top=99999
                spritefoc.rect.left=99999
    
    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
            var_attackconfirm_l=sprite1.rect.left-spritemonstruo1.rect.left
            var_attackconfirm_t=sprite1.rect.top-spritemonstruo1.rect.top
    
            var_attackconfirm_l_2=sprite1.rect.left-sger.rect.left
            var_attackconfirm_t_2=sprite1.rect.top-sger.rect.top
    
    #accions que infringeixen dany al monstre (pop)
            
            if var3==True:
                if spritefoc.rect.colliderect(spritemonstruo1) and hpmonstruo1>0:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(5,15)
                    if hpmonstruo1<0:
                        hpmonstruo1==0
            
                if var1==1 and var_attackconfirm_l>-20 and var_attackconfirm_l<10 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left+10,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
                if var1==2 and var_attackconfirm_l>-10 and var_attackconfirm_l<20 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left-10)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
    
    #accions que infringeixen dany al monstre (guerrer)
            
            if var3_2==True:
                if spritefoc.rect.colliderect(sger) and hpmonstruo2>0:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(1,4)
                    if hpmonstruo2<0:
                        hpmonstruo2==0
            
                if var1==1 and var_attackconfirm_l_2>-25 and var_attackconfirm_l_2<20 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left+10,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
                if var1==2 and var_attackconfirm_l_2>-20 and var_attackconfirm_l_2<25 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left-10)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
    
    
    #accions que infringeixen dany al pj (pop)
                        
            if var3==True and spritemonstruo1.rect.colliderect(sprite1.rect) and hpmonstruo1>0 and hp_pj>0:
                hp_pj-=random.randrange(0,2)
                sprite1.rect.left-=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo1<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
    
    #accions que infringeixen dany al pj (guerrer d)
                        
            if var3_2==True and sger.rect.colliderect(sprite1.rect) and hpmonstruo2>0 and hp_pj>0:
                hp_pj-=random.randrange(1,4)
                sprite1.rect.left+=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo2<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
            
    
    #axo serveix perk no senkalli el pj en matar el monstre
            #if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6<50 and hpmonstruo1==0:
             #   sprite1.rect.left+=10
                
            #if sprite1.rect.colliderect(sger.rect) and cont6<50 and hpmonstruo2==0:
             #   sprite1.rect.left+=10
            
    #vida dels monstres          
            if var3==True:       
                hpm1=str(str(hpmonstruo1)+'/120')
    
            if var3_2==True:
                hpm2=str(str(hpmonstruo2)+'/100')
    
    #per fer desaparexer el pop un kop mort:
            if hpmonstruo1<=0 and cont6<70:
                hpmonstruo1=0
                cont6+=1
                if cont6==70:
                    cont6=0
                    var3=False
                    spritemonstruo1.rect.top=9999
                    spritemonstruo1.rect.left=9999
    
    #per fer desaparexer el guerrer un kop mort:
            if hpmonstruo2<=0 and cont15<70:
                hpmonstruo2=0
                cont15+=1
                if cont15==70:
                    cont15=0
                    var3_2=False
                    sger.rect.top=9999
                    sger.rect.left=9999
    
    
    #imprimacio de la vida dels monstres
            #pop       
            if var3==True:
                textohp1=fuente1.render(hpm1,0,rojo)
                pantalla.blit(textohp1,(spritemonstruo1.rect.left-10,spritemonstruo1.rect.top-25))
    
            #guerrer
            if var3_2==True:
                textohp2=fuente1.render(hpm2,0,rojo)
                pantalla.blit(textohp2,(sger.rect.left-10,sger.rect.top-25))
    
    
    #sistema k fa k el pj no travessi el monstre
            if hpmonstruo1==0:
                if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6>10 and var_c1==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
            if hpmonstruo2==0:
                if sprite1.rect.colliderect(sger.rect) and cont6>10 and var_c2==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
    
    
            if var3==False and cont11==0:
                cont6=0
                cont11+=1
    
            if var3==False and cont12==0:
                cont6=0
                cont12+=1
    
            if hp_pj==0:
                cont13+=1
    
            if cont13==50:
                sonido3.stop()
                menu1()
    
            if hp_pj<=0:
                pantalla.blit(textoGO,(200,200))
                if cont13==1:
                    sonidodead.play()
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                elif cont13==20:
                    sonidodead.stop()
                
    
    #per saber si sa akabat el nivell:
            if var8==True and var8_2==True and var8_3==True:
                pantalla.blit(textoV,(115,200))
                cont16+=1
                var9=True
                if cont16==60:
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                    sonido3.stop()
                    menu1()
    
    
                
                
            
    ###############################################################################
    ###############################################################################
    
    
            if vr3==False or vr3_2==False:
                    var7=1
                #si el monstre esta viu la imatge simprimex en la pantalla
                    
            if var7==1:
                if var3_3==True:
                    pantalla.blit(smonster.image,smonster.rect)
    
                    #moviments
                        
                    if var3_3==True and hpmonstruo3>0 and hp_pj>0:
                        variable1_3=random.randrange(0,5)
    
                        
                        
                        if variable1_3==0 or variable1_3==1:
                            if smonster.rect.left<770 and sprite1.rect.left>smonster.rect.left:
                                smonster.rect.left+=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image5
                                if variable1_3==1:
                                    smonster.image=monstruo3image8
                        if variable1_3==1 or variable1_3==2:
                            if smonster.rect.top<570 and sprite1.rect.top>smonster.rect.top:
                                smonster.rect.top+=random.randrange(0,25)
                                if variable1_3==0:
                                    smonster.image=monstruo3image5
                                if variable1_3==1:
                                    smonster.image=monstruo3image8
                        if variable1_3==2 or variable1_3==3:
                            if smonster.rect.top>15 and sprite1.rect.top<smonster.rect.top:
                                smonster.rect.top-=random.randrange(0,25)
                                if variable1_3==0:
                                    smonster.image=monstruo3image4
                                if variable1_3==1:
                                    smonster.image=monstruo3image9
                        if variable1==3 or variable1_3==0:
                            if smonster.rect.left>15 and sprite1.rect.left<smonster.rect.left:
                                smonster.rect.left-=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image4
                                if variable1_3==3:
                                    smonster.image=monstruo3image9
    
            
    
    
    
                    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
                    var_attackconfirm_l_3=sprite1.rect.left-smonster.rect.left
                    var_attackconfirm_t_3=sprite1.rect.top-smonster.rect.top
    
                #accions que infringeixen dany al monstre (snake)
    
                    if var3_3==True:
                        if spritefoc.rect.colliderect(smonster) and hpmonstruo3>0:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(5,15)
                            if hpmonstruo3<0:
                                hpmonstruo3==0
    
                        if var1==1 and var_attackconfirm_l_3>-20 and var_attackconfirm_l_3<10 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left+10,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
                        if var1==2 and var_attackconfirm_l_3>-10 and var_attackconfirm_l_3<20 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left-10)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
    
    
                    #accions que infringeixen dany al pj (snake)
                                
                    if var3_3==True and smonster.rect.colliderect(sprite1.rect) and hpmonstruo3>0 and hp_pj>0:
                        hp_pj-=random.randrange(0,2)
                        sprite1.rect.left-=random.randrange(-5,5)
                        sprite1.rect.top+=random.randrange(-5,5)
    
                        if var1==1:
                            sprite1.image=goblinhr
                        if var1==2:
                            sprite1.image=goblinhl
    
                    if hpmonstruo3<0:
                        hpmonstruo3==0
    
    
                    hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    textohppj=fuente1.render(hppjt,0,verde)
                    pantalla.blit(textohppj,(5,5))
    
    
                    #axo serveix perk no senkalli el pj en matar el monstre
                    #if sprite1.rect.colliderect(smonster.rect) and cont6<50 and hpmonstruo3==0:
                     #   sprite1.rect.left+=10
                        
    
                    #vida dels monstres          
                    if var3_3==True:       
                        hpm3=str(str(hpmonstruo3)+'/50')
    
                    #per fer desaparexer el snake un kop mort:
                    
                    if hpmonstruo3<=0 and cont17<70:
                        hpmonstruo3=0
                        cont17+=1
                        if cont17==70:
                            cont17=0
                            var3_3=False
                            smonster.rect.top=9999
                            smonster.rect.left=9999
    
    
                    #imprimacio de la vida dels monstres       
                    if var3_3==True:
                        textohp1=fuente1.render(hpm3,0,rojo)
                        pantalla.blit(textohp1,(smonster.rect.left-10,smonster.rect.top-25))
    
    
                    #sistema k fa k el pj no travessi el monstre
                    if hpmonstruo3==0:
                        if sprite1.rect.colliderect(smonster.rect) and cont6>10 and var_c3==True:
                            sprite1.rect.left=xant
                            sprite1.rect.top=yant
    
                    
    
    
    
    
                    if var3_3==False and cont11==0:
                        cont6=0
                        cont11+=1
    
                    if var3_3==False and cont12==0:
                        cont6=0
                        cont12+=1
    
    
    
            vr3=var3
            vr3_2=var3_2
            vr3_3=var3_3
    
            
    
    
    #si el pop esta mort i sa mort menys de 4 vegades torna a aparexer depen del resultat de f
            if vr3==False and cont19<3:
                    spritemonstruo1=pygame.sprite.Sprite()
                    spritemonstruo1.image=monstruoimage1
                    spritemonstruo1.rect=monstruoimage1.get_rect()
                    spritemonstruo1.rect.top=random.randrange(0,570)
                    spritemonstruo1.rect.left=random.randrange(0,770)
                    hpmonstruo1=120
                    cont6=0
                    var3=True
                    cont19+=1
                    cont23=0
            if cont19==3 and var3==False:
                var8=True
                
    #
            if vr3_2==False and cont20<2:
                    sger=pygame.sprite.Sprite()
                    sger.image=monstruo2image1
                    sger.rect=monstruo2image1.get_rect()
                    sger.rect.top=random.randrange(0,570)
                    sger.rect.left=random.randrange(0,770)
                    hpmonstruo2=100
                    cont6=0
                    var3_2=True
                    cont20+=1
                    cont24=0
            if cont20==2 and var3_2==False:
                var8_2=True
    
    
    
            if vr3_3==False and cont21<5:
                    smonster=pygame.sprite.Sprite()
                    smonster.image=monstruo3image1
                    smonster.rect=monstruo3image1.get_rect()
                    smonster.rect.top=random.randrange(0,570)
                    smonster.rect.left=random.randrange(0,770)
                    hpmonstruo3=50
                    cont6=0
                    var3_3=True
                    cont21+=1
                    cont25=0
            if cont21==5 and var3_3==False:
                var8_3=True
    
                
    ####AKI ANIRA LU MATEX K LU DEL POP AM ELS ALTRES 2 MONSTRES
    
    #per k es recargi el mp:
            cont18+=1
            if cont18%10==0 and mppj<mpdatos:
                mppj+=1
        
    #imprimacio del mp:
            mppjt=str('MP: '+str(mppj)+'/'+str(mptpj))
            textomppj=fuente1.render(mppjt,0,verde)
            pantalla.blit(textomppj,(700,5))
    
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
    
    #per guardar la kantitat de diners i desblokejar el seguen nivell si sa completat la misio
            if var9==True:
                money_t=str(money)
                moneywriter=open('log\money.txt','w')
                moneywriter.write(money_t)
                moneywriter.close()
            
                moneyreader=open('log\money.txt')
                money=int(moneyreader.readline())
                moneyreader.close()
    
                if mision==2:
                    misionwriter=open('log\misions.txt','w')
                    misionwriter.write('3')
                    misionwriter.close()
    
            
    
    #per sumar diners al matar els monstres:
            if cont23==0 and hpmonstruo1==0:
                cont23+=1
                money+=random.randrange(9,16)
                print 'dinero:', money
    
            if cont24==0 and hpmonstruo2==0:
                cont24+=1
                money+=random.randrange(23,35)
                print 'dinero:', money
    
            if cont25==0 and hpmonstruo3==0:
                cont25+=1
                money+=random.randrange(5,11)
                print 'dinero:', money
    
                
                
    
            if hp_pj==0:
                money=perdrediners
                
                if contx==0:
                    print 'dinero: ', money
                    contx+=1
    
            tttmoney=str('Dinero: '+str(money))
            textomoney=fuente1.render(tttmoney,0,verde)
            pantalla.blit(textomoney,(200,5))
    
            misionreader=open('log\misions.txt')
            mision=int(misionreader.readline())
            misionreader.close()
    
        
            if sprite1.rect.colliderect(sr1.rect) or sprite1.rect.colliderect(sr2.rect) or sprite1.rect.colliderect(sr3.rect):     
                sprite1.rect.left=xant
                sprite1.rect.top=yant
    
    #prk el pj no surti del mapa:
            if sprite1.rect.left<=0:
                sprite1.rect.left=0
            if sprite1.rect.top<=0:
                sprite1.rect.top=0
            if sprite1.rect.left>=780:
                sprite1.rect.left=780
            if sprite1.rect.top>=550:
                sprite1.rect.top=550
    
    #prk els monstres no chokin am les palmeras:
            if smonster.rect.colliderect(sr1.rect) or smonster.rect.colliderect(sr2.rect) or smonster.rect.colliderect(sr3.rect) and contG>0:
                smonster.rect.left=xmant1
                smonster.rect.top=ymant1
                contE3+=1
            else:
                contE3=0
            if sger.rect.colliderect(sr1.rect) or sger.rect.colliderect(sr2.rect) or sger.rect.colliderect(sr3.rect) and contG>0:
                sger.rect.left=xmant2
                sger.rect.top=ymant2
                contE2+=1
            else:
                contE2=0
            if spritemonstruo1.rect.colliderect(sr1.rect) or spritemonstruo1.rect.colliderect(sr2.rect) or spritemonstruo1.rect.colliderect(sr3.rect) and contG>0:
                spritemonstruo1.rect.left=xmant3
                spritemonstruo1.rect.top=ymant3
                contE1+=1
            else:
                contE1=0
    
            #imprimacio de las rokass
            pantalla.blit(sr1.image,sr1.rect)
            pantalla.blit(sr2.image,sr2.rect)
            pantalla.blit(sr3.image,sr3.rect)
    
            #imprimacio dels arbres
            #pantalla.blit(sa1.image,sa1.rect)
            #pantalla.blit(sa2.image,sa2.rect)
            #pantalla.blit(sa3.image,sa3.rect)
            
    
    #perk el pj no senkalli am els monstres:
            if hpmonstruo1==0 and sprite1.rect.colliderect(spritemonstruo1)==False:
                var_c1=True
            if hpmonstruo2==0 and sprite1.rect.colliderect(sger)==False:
                var_c2=True
            if hpmonstruo3==0 and sprite1.rect.colliderect(smonster)==False:
                var_c3=True
    
            if hpmonstruo1>0:
                var_c1=False
            if hpmonstruo2>0:
                var_c2=False
            if hpmonstruo3>0:
                var_c3=False
    
    #per si el monstre aparex sobre una roka k es mogi per no enkallarse
            #if contE1==2:
             #   smonster.rect.left+=10
            #if contE2==2:
             #   sger.rect.left+=10
            #if contE3==2:
                #spritemonstruo1.rect.left+=10
    
    #perk kridin els monstres kuan morin:
            if hpmonstruo1==0 and contC1==0:
                sonidocrit1.play()
                contC1+=1
            if hpmonstruo1>0:
                contC1=0
    
            if hpmonstruo2==0 and contC2==0:
                sonidocrit2.play()
                contC2+=1
            if hpmonstruo2>0:
                contC2=0
    
            if hpmonstruo3==0 and contC3==0:
                sonidocrit3.play()
                contC3+=1
            if hpmonstruo3>0:
                contC3=0
    
    #per fer k el gerrer tingi la imatge de atacant:
            if hpmonstruo2>0 and sger.rect.colliderect(sprite1) and var_d2==1:
                if contG%2==0:
                    sger.image=monstruo2image5
    
            if hpmonstruo2>0 and sger.rect.colliderect(sprite1) and var_d2==2:
                if contG%2==0:
                    sger.image=monstruo2image6
    
            
    
            #textos pocions:
            potionhpt=str('Pociones HP: '+str(potionshp))
            potionmpt=str('Pociones MP: '+str(potionsmp))
            textohpp=fuente1.render(potionhpt,0,verde)
            textompp=fuente1.render(potionmpt,0,verde)
            pantalla.blit(textohpp,(350,5))
            pantalla.blit(textompp,(500,5))
    
    
    
            if var_escudo==True:
                spritee.rect.top=sprite1.rect.top-15
                spritee.rect.left=sprite1.rect.left-25
            else:
                spritee.rect.top=999999
                spritee.rect.left=999999
    
            if var_escudo==True:
                cont_escudo+=1
            if var_escudo==True and var_potion==False:
                hp_pj=hp_pjant
    
            if cont_escudo==100:
                var_escudo=False
                cont_escudo=0
    
            
            
    
            pantalla.blit(spritee.image,spritee.rect)
            
            #per fer k leskut giri :)
            if var_escudo==True:
                escut_i=pygame.transform.rotate(escut_i, 90)
                spritee.image=escut_i
    
            
            contG+=1
            
            pygame.display.update()
        pygame.quit()
    
    
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    
                            #####tercer nivell#####
        
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    #########################################################################
    
    def guerra3():
        pygame.init()
        pygame.key.set_repeat(20)
        pantalla=pygame.display.set_mode((800,600))
        fondo=pygame.image.load("images/goblinw/fons3.png")
        pygame.display.set_caption('GOBLIN W.')
    
        #rectangles dels arbres
        r_a1=pygame.Rect(80,300,10,30)
        r_a2=pygame.Rect(400,200,10,30)
        r_a3=pygame.Rect(700,400,10,30)
    
        #pygame.draw.rect(pantalla,(0,0,0),r_a1)
        #pygame.draw.rect(pantalla,(0,0,0),r_a2)
        #pygame.draw.rect(pantalla,(0,0,0),r_a3)
    
    
        #SONS
        sonido1=pygame.mixer.Sound("sounds/goblinw/Blast.wav")
        sonido2=pygame.mixer.Sound("sounds/goblinw/explosion.wav")
        sonido3=pygame.mixer.Sound("sounds/goblinw/BSO4.wav")
        sonidodead=pygame.mixer.Sound("sounds/goblinw/deadpj.wav")
        sonidoespada=pygame.mixer.Sound("sounds/goblinw/Sspada.wav")
        sonidoespadaF=pygame.mixer.Sound("sounds/goblinw/SspadaF.wav")
        sonidocrit1=pygame.mixer.Sound("sounds/goblinw/crit1.wav")
        sonidocrit2=pygame.mixer.Sound("sounds/goblinw/crit2.wav")
        sonidocrit3=pygame.mixer.Sound("sounds/goblinw/crit3.wav")
        sonidorun=pygame.mixer.Sound("sounds/goblinw/run.wav")
        sopotion=pygame.mixer.Sound("sounds/goblinw/potion.wav")
        s_terremoto=pygame.mixer.Sound("sounds/goblinw/terremoto.wav")
        #sonidocrit3=pygame.mixer.Sound("sounds/goblinw/.wav")
    
        
        #goblin parat
        goblin1=pygame.image.load("images/goblinw/Idle0.png").convert_alpha()
        goblin2=pygame.image.load("images/goblinw/Idle1.png").convert_alpha()
    
        #goblin caminant cap a la dreta
        goblinwr1=pygame.image.load("images/goblinw/Walk0.png").convert_alpha()
        goblinwr2=pygame.image.load("images/goblinw/Walk1.png").convert_alpha()
        goblinwr3=pygame.image.load("images/goblinw/Walk2.png").convert_alpha()
        goblinwr4=pygame.image.load("images/goblinw/Walk3.png").convert_alpha()
    
        #goblin caminant cap a leskerra
        goblinwl1=pygame.image.load("images/goblinw/Walkl0.png").convert_alpha()
        goblinwl2=pygame.image.load("images/goblinw/Walkl1.png").convert_alpha()
        goblinwl3=pygame.image.load("images/goblinw/Walkl2.png").convert_alpha()
        goblinwl4=pygame.image.load("images/goblinw/Walkl3.png").convert_alpha()
    
        #goblin atakant cap a la dreta
        goblinar1=pygame.image.load("images/goblinw/Attack0.png").convert_alpha()
        goblinar2=pygame.image.load("images/goblinw/Attack1.png").convert_alpha()
        goblinar3=pygame.image.load("images/goblinw/Attack2.png").convert_alpha()
    
        #goblin atacant cap a leskerra
        goblinal1=pygame.image.load("images/goblinw/Attackl0.png").convert_alpha()
        goblinal2=pygame.image.load("images/goblinw/Attackl1.png").convert_alpha()
        goblinal3=pygame.image.load("images/goblinw/Attackl2.png").convert_alpha()
    
        #goblin atacant am magia cap a la dreta
        goblinamr=pygame.image.load("images/goblinw/Attackmr.png").convert_alpha()
    
        #goblin atacant am magia kap a leskerra
        goblinaml=pygame.image.load("images/goblinw/Attackml.png").convert_alpha()
    
        #goblin mort 1
        goblindr=pygame.image.load("images/goblinw/Dead0.png").convert_alpha()
    
        #goblin mort 2
        goblindl=pygame.image.load("images/goblinw/Dead1.png").convert_alpha()
    
        #goblin golpejat 1
        goblinhr=pygame.image.load("images/goblinw/Hurt0.png").convert_alpha()
    
        #goblin golpejat 2
        goblinhl=pygame.image.load("images/goblinw/Hurt1.png").convert_alpha()
    
        
        #bola de foc
        foc1=pygame.image.load("images/goblinw/foc.png").convert_alpha()
    
        #monstres
        
        #POP
        monstruoimage1=pygame.image.load("images/goblinw/monstruo2.png").convert_alpha()
        monstruoimage3=pygame.image.load("images/goblinw/monstruo2_3.png").convert_alpha()
        monstruoimage4=pygame.image.load("images/goblinw/monstruo2_4.png").convert_alpha()
        monstruoimage5=pygame.image.load("images/goblinw/monstruo2_5.png").convert_alpha()
        monstruoimage6=pygame.image.load("images/goblinw/monstruo2_6.png").convert_alpha()
    
        #GUERRER DAURAT
        monstruo2image1=pygame.image.load("images/goblinw/guerrero2.png").convert_alpha()
        monstruo2image2=pygame.image.load("images/goblinw/guerrero2_2.png").convert_alpha()
        monstruo2image3=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
        monstruo2image4=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
        monstruo2image5=pygame.image.load("images/goblinw/guerrero2_5.png").convert_alpha()
        monstruo2image6=pygame.image.load("images/goblinw/guerrero2_6.png").convert_alpha()
        monstruo2image7=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
        monstruo2image8=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
        monstruo2image9=pygame.image.load("images/goblinw/guerrero2_7.png").convert_alpha()
    
        #monstre 3 (sNakE)
        monstruo3image1=pygame.image.load("images/goblinw/guerrero3.png").convert_alpha()
        monstruo3image2=pygame.image.load("images/goblinw/guerrero3_2.png").convert_alpha()
        monstruo3image3=pygame.image.load("images/goblinw/guerrero3_3.png").convert_alpha()
        monstruo3image4=pygame.image.load("images/goblinw/guerrero3_4.png").convert_alpha()
        monstruo3image5=pygame.image.load("images/goblinw/guerrero3_5.png").convert_alpha()
        monstruo3image6=pygame.image.load("images/goblinw/guerrero3_6.png").convert_alpha()
        monstruo3image7=pygame.image.load("images/goblinw/guerrero3_7.png").convert_alpha()
        monstruo3image8=pygame.image.load("images/goblinw/guerrero3_8.png").convert_alpha()
        monstruo3image9=pygame.image.load("images/goblinw/guerrero3_9.png").convert_alpha()
        monstruo3image10=pygame.image.load("images/goblinw/guerrero3_9.png").convert_alpha()
        monstruo3image11=pygame.image.load("images/goblinw/guerrero3_9.png").convert_alpha()
    
        #imatges dels arbres
        tree1image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree2image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree3image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
    
        #imatges de las rokas
        rock1image=pygame.image.load("images/goblinw/roca.png").convert_alpha()
        rock2image=pygame.image.load("images/goblinw/roca2.png").convert_alpha()
    
        #imatge eskut
        escut_i=pygame.image.load("images/goblinw/escudo_m.png").convert_alpha()    
        
        #sprite del goblin
        sprite1=pygame.sprite.Sprite()
        sprite1.image=goblin1
        sprite1.rect=goblin1.get_rect()
        sprite1.rect.top=100
        sprite1.rect.left=50
    
        #sprite de leskut
        spritee=pygame.sprite.Sprite()
        spritee.image=escut_i
        spritee.rect=escut_i.get_rect()
        spritee.rect.top=sprite1.rect.top
        spritee.rect.left=sprite1.rect.left
    
        
    
        #sprite de la bola de foc
        spritefoc=pygame.sprite.Sprite()
        spritefoc.image=foc1
        spritefoc.rect=foc1.get_rect()
        spritefoc.rect.top=9999
        spritefoc.rect.left=9999
    
        #sprite de monstre pop 1
        spritemonstruo1=pygame.sprite.Sprite()
        spritemonstruo1.image=monstruoimage1
        spritemonstruo1.rect=monstruoimage1.get_rect()
        spritemonstruo1.rect.top=random.randrange(0,570)
        spritemonstruo1.rect.left=random.randrange(0,770)
    
        #sprite de monstre guerrer 2
        sger=pygame.sprite.Sprite()
        sger.image=monstruo2image1
        sger.rect=monstruo2image1.get_rect()
        sger.rect.top=random.randrange(0,570)
        sger.rect.left=random.randrange(0,770)
    
        #sprite del snake 3
        smonster=pygame.sprite.Sprite()
        smonster.image=monstruo3image1
        smonster.rect=monstruo3image1.get_rect()
        smonster.rect.top=random.randrange(0,570)
        smonster.rect.left=random.randrange(0,770)
    
        #sprites de las rokas
        #1
        sr1=pygame.sprite.Sprite()
        sr1.image=rock1image
        sr1.rect=rock1image.get_rect()
        sr1.rect.top=280
        sr1.rect.left=60
        #2
        sr2=pygame.sprite.Sprite()
        sr2.image=rock2image
        sr2.rect=rock2image.get_rect()
        sr2.rect.top=70
        sr2.rect.left=400
        #3
        sr3=pygame.sprite.Sprite()
        sr3.image=rock2image
        sr3.rect=rock2image.get_rect()
        sr3.rect.top=350
        sr3.rect.left=500
        
    
        #arbres k no utilitzu xd
        sa1=pygame.sprite.Sprite()
        sa1.image=tree1image
        sa1.rect=tree1image.get_rect()
        sa1.rect.top=280
        sa1.rect.left=60
    
        sa2=pygame.sprite.Sprite()
        sa2.image=tree1image
        sa2.rect=tree1image.get_rect()
        sa2.rect.top=95
        sa2.rect.left=372
    
        sa3=pygame.sprite.Sprite()
        sa3.image=tree1image
        sa3.rect=tree1image.get_rect()
        sa3.rect.top=350
        sa3.rect.left=677
    
        #r_a1=pygame.Rect(87,320,10,30)
        #r_a2=pygame.Rect(400,135,10,30)
        #r_a3=pygame.Rect(705,392,10,30)
        
    
        #fuentes
        fuente1=pygame.font.SysFont("Arial",16,True,False)
        fuentevidapj=pygame.font.SysFont("Arial",25,True,False)
        fuenteGO=pygame.font.SysFont("Arial",70,True,False)
    
        
    
        #colors:
        rojo=(255,0,0)
        azul=(0,0,255)
        verde=(0,255,0)
        blanco=(255,255,255)
        negro=(0,0,0)
    
        #textos constants
        textoGO=fuenteGO.render('GAME OVER',0,rojo)
        textoV=fuenteGO.render('NIVEL COMPLETADO',0,azul)
    
        #altres variables i contadors
        cont5=0
        cont4=0
        cont3=0
        cont1=0
        cont2=0
        cont6=0
        cont11=0
        cont12=0
        cont13=0
        cont15=0
        cont16=0
        cont17=0
        cont18=0
        cont19=0
        cont20=0
        cont21=0
        cont22=0
        contx=0
        cont23=0
        cont24=0
        cont25=0
        contG=0
        contE1=0
        contE2=0
        contE3=0
        contC1=0
        contC2=0
        contC3=0
        cont_escudo=0
        cont_terremoto=0
        #########
        var1=1
        var2=0
        var3=True  #<---variable per saber si el monstre esta viu
        var3_2=True #<---variable per saber si el monstre 2 esta viu
        var3_3=True #<---variable per saber si el monster 3 esta viu
        var4=0
        vr3=var3
        vr3_2=var3_2
        vr3_3=var3_3
        var7=0
        var8=False # variable k indica si san matat prous pops per finalitzar el nivell
        var8_2=False
        var8_3=False
        var9=False
        var_c1=True
        var_c2=True
        var_c3=True
        var_d2=1
        var_md=1#direccio guerrer drago
        var_escudo=False
        var_potion=False
        var_terremoto=False
    
        #variables per saber si sesta atacant o si sa tirat magia
        var_attack=False
        var_magia=False
    
        #vida monstres i pj
        hpmonstruo1=120
        hpmonstruo2=100
        hpmonstruo3=80
    
    
        #per llegir les pocions
        potionsreader=open('log\potions.txt')
        potionshp=int(potionsreader.readlines()[0])
        print 'potions hp: ', potionshp
        potionsreader.close()
        
        potionsreader=open('log\potions.txt')
        potionsmp=int(potionsreader.readlines()[1])
        print 'potions mp: ', potionsmp
        potionsreader.close()
    
    
    
        
    
    
    #escudo i atak terratremol
        tendareader=open('log/shop.txt')
        escudo=int(tendareader.readlines()[0])
        tendareader.close()
        print 'escudo', escudo
        
        tendareader=open('log/shop.txt')
        terremoto=int(tendareader.readlines()[1])
        tendareader.close()
        print 'terremoto', terremoto
        
    
    
    
    
    
        
    
    #per llegir el hp del pj:
        datosreader=open('log\datos.txt')
        hpdatos=int(datosreader.readlines()[0])
        print 'hp: ', hpdatos
        datosreader.close()
    
        hp_pj=hpdatos
        hpt_pj=hp_pj
    
        #variable del bucle principal
        salir=False
    
        #reloj
        reloj1=pygame.time.Clock()
    
        #grup de sprites de monstres
        grupo_m=pygame.sprite.Group(spritemonstruo1,sger,smonster)
    
    #per llegir el mp del pj:
    
        datosreader=open('log\datos.txt')
        mpdatos=int(datosreader.readlines()[1])
        print 'mp: ', mpdatos
        datosreader.close()
        
        #mp del pj
        mptpj=mpdatos
        mppj=mptpj
    
    ######
        #variable diners
        moneyreader=open('log\money.txt')
        money=int(moneyreader.readline())
        print 'dinero:', money
        moneyreader.close()
    
        money_t=str(money)
        moneywriter=open('log\money.txt','w')
        moneywriter.write(money_t)
        moneywriter.close()
    
        perdrediners=money
        
    
        sonido3.play()
    
    
        while salir != True:
            
            var_potion=False
    
            hp_pjant=hp_pj
    
            if hp_pj<=0 and var1==1:
                sprite1.image=goblindr
    
            if hp_pj<=0 and var1==2:
                sprite1.image=goblindl
                
    
            xant=sprite1.rect.left
            yant=sprite1.rect.top
    
            if hpmonstruo1<0:
                hpmonstruo1==0
            
            if hpmonstruo1==0:
                spritemonstruo1.image=monstruoimage3
    
    
    
            if hpmonstruo2<0:
                hpmonstruo2==0
            
            if hpmonstruo2==0:
                sger.image=monstruo2image9
    
                
    
            if hpmonstruo3<0:
                hpmonstruo3==0
            
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
                
    
            if hp_pj<0:
                hp_pj=0
                
    
    
            xmant1=smonster.rect.left
            ymant1=smonster.rect.top
            xmant2=sger.rect.left
            ymant2=sger.rect.top
            xmant3=spritemonstruo1.rect.left
            ymant3=spritemonstruo1.rect.top
    
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN and hp_pj>0:
    
                    if event.key==pygame.K_LEFT and sprite1.rect.left>0:
                        if cont1==0:
                            sprite1.image=goblinwl1
                        if cont1==1:
                            sprite1.image=goblinwl2
                        if cont1==2:
                            sprite1.image=goblinwl3
                        if cont1==3:
                            sprite1.image=goblinwl4
                        if cont1==4:
                            sprite1.image=goblinwl3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left-=6
                        cont1+=1
                        var1=2
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
                        
    
                    if event.key==pygame.K_RIGHT and sprite1.rect.left<775:
                        if cont1==0:
                            sprite1.image=goblinwr1
                        if cont1==1:
                            sprite1.image=goblinwr2
                        if cont1==2:
                            sprite1.image=goblinwr3
                        if cont1==3:
                            sprite1.image=goblinwr4
                        if cont1==4:
                            sprite1.image=goblinwr3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left+=6
                        cont1+=1
                        var1=1
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_UP and sprite1.rect.top>0:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
                            
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top-=6
                        cont1+=1
                        var4=1
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_DOWN and sprite1.rect.top<555:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top+=6
                        cont1+=1
                        var4=2
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_SPACE:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinar2
                            if cont1==1:
                                sprite1.image=goblinar1
                            if cont1==2:
                                sprite1.image=goblinar1
                            if cont1==3:
                                sprite1.image=goblinar2
                            if cont1==4:
                                sprite1.image=goblinar3
                            if cont1>=5:
                                cont1=0
                                sprite1.image=goblinar2
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinal2
                            if cont1==1:
                                sprite1.image=goblinal1
                            if cont1==2:
                                sprite1.image=goblinal2
                            if cont1==3:
                                sprite1.image=goblinal3
                            if cont1>=4:
                                cont1=0
                                sprite1.image=goblinal2
                                
                        cont1+=1
                        var_attack=True
                        if cont1%2==0:
                            sonidoespadaF.play()
    
                        
                            
    
                        
                    if event.key==pygame.K_m:
                        if cont2<=3:
                            if var1==1:
                                sprite1.image=goblinamr
                            if var1==2:
                                sprite1.image=goblinaml
                        if cont2==4:
                            if var1==1:
                                sprite1.image=goblin1
                            if var1==2:
                                sprite1.image=goblin2
                        if cont2==1 and mppj>=20:
                            var_magia=True
                        cont2+=1
    
    
                    if event.key==pygame.K_h and potionshp>0 and hp_pj>0:
                        if hp_pj<hpt_pj:
                            potionshp-=1
                            hp_pj+=random.randrange(15,20)
                            sopotion.play()
                            print 'potionshp: ', potionshp
                            var_potion=True
                            
                            if hp_pj>hpt_pj:
                                hp_pj=hpt_pj
    
                    if event.key==pygame.K_j and potionsmp>0 and hp_pj>0:
                        if mppj<mptpj:
                            potionsmp-=1
                            mppj+=random.randrange(10,20)
                            sopotion.play()
                            print 'potionsmp: ', potionsmp
                            
                            if mppj>mptpj:
                                mppj=mptpj
    
                    if event.key==pygame.K_n and escudo==1 and hp_pj>0 and mppj>=60:
                        mppj-=60
                        var_escudo=True
                        print 'escudo activado'
                    
                    if event.key==pygame.K_b and terremoto==1 and hp_pj>0 and mppj>=250 and var_terremoto==False:
                        mppj-=250
                        var_terremoto=True
                        print 'terremoto activado'
    
                    
    
                    if event.key==pygame.K_ESCAPE:
                        sonido3.stop()
                        menu1()
                            
                            
                    
                if event.type==pygame.KEYUP and hp_pj>0:
                    if var1==1:
                        sprite1.image=goblin1
                    if var1==2:
                        sprite1.image=goblin2
                        
                    var_attack=False
                    cont2=0
                    cont1=0
                    
    
            reloj1.tick(17)
            
            
            pantalla.blit(fondo,(0,0))
            
            if var_terremoto==True:
                if var3==True:
                    hpmonstruo1=0
                if var3_2==True:
                    hpmonstruo2=0
                if var3_3==True and var7==1:
                    hpmonstruo3=0
                s_terremoto.play()
                cont_terremoto+=1
                if cont_terremoto%2==0:
                    pantalla.blit(fondo,(random.randrange(0,5),random.randrange(0,5)))
                else:
                    pantalla.blit(fondo,(0,0))
            if cont_terremoto==10:
                var_terremoto=False
                cont_terremoto=0
    
            pantalla.blit(sprite1.image,sprite1.rect)
    
            
    
            if var3==True:
                pantalla.blit(spritemonstruo1.image,spritemonstruo1.rect)
    
    
            if var3_2==True:
                pantalla.blit(sger.image,sger.rect)
    
            
            
            #MOVIMENTS DEL MONSTRE 1 (pop)
                
            if var3==True and hpmonstruo1>0 and hp_pj>0:
                variable1=random.randrange(0,5)
    
    
                if variable1==0 or variable1==1:
                    if spritemonstruo1.rect.left<770 and sprite1.rect.left>spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left+=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage5
                if variable1==1 or variable1==2:
                    if spritemonstruo1.rect.top<570 and sprite1.rect.top>spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top+=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage1
                if variable1==2 or variable1==3:
                    if spritemonstruo1.rect.top>15 and sprite1.rect.top<spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top-=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage6
                if variable1==3 or variable1==0:
                    if spritemonstruo1.rect.left>15 and sprite1.rect.left<spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left-=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage4
    
            #MOVIMENTS DEL MONSTRE 2 (guerrer daurat)
                
            if var3_2==True and hpmonstruo2>0 and hp_pj>0:
                variable1_2=random.randrange(0,5)
    
    
                if variable1_2==0 or variable1_2==1:
                    if sger.rect.left<770 and sprite1.rect.left>sger.rect.left:
                        sger.rect.left+=random.randrange(0,10)
                        randomvar1=random.randrange(0,2)
                        if randomvar1==0:
                            sger.image=monstruo2image2
                        else:
                            sger.image=monstruo2image3
                        var_d2=1
                            
                if variable1_2==1 or variable1_2==2:
                    if sger.rect.top<570 and sprite1.rect.top>sger.rect.top:
                        sger.rect.top+=random.randrange(0,7)
                        randomvar1=random.randrange(0,2)
                        if var_d2==1:
                            if randomvar1==0:
                                sger.image=monstruo2image2
                            else:
                                sger.image=monstruo2image3
    
                        if var_d2==2:
                            if randomvar1==0:
                                sger.image=monstruo2image1
                            else:
                                sger.image=monstruo2image4
    
                            
                            
                if variable1_2==2 or variable1_2==3:
                    if sger.rect.top>15 and sprite1.rect.top<sger.rect.top:
                        sger.rect.top-=random.randrange(0,7)
                        randomvar1=random.randrange(0,2)
                        if var_d2==1:
                            if randomvar1==0:
                                sger.image=monstruo2image2
                            else:
                                sger.image=monstruo2image3
    
                        if var_d2==2:
                            if randomvar1==0:
                                sger.image=monstruo2image1
                            else:
                                sger.image=monstruo2image4
                        
                        
                            
                if variable1_2==3 or variable1_2==0:
                    if sger.rect.left>15 and sprite1.rect.left<sger.rect.left:
                        sger.rect.left-=random.randrange(0,10)
                        randomvar1=random.randrange(0,2)
                        if randomvar1==0:
                            sger.image=monstruo2image1
                        else:
                            sger.image=monstruo2image4
                        var_d2=2
    
            
                        
                        
            #"INVOCACIO" BOLA DE FOC
                        
            if var_magia==True and cont5==0 and mppj>20:
                #sprite de la bola de foc
                spritefoc=pygame.sprite.Sprite()
                spritefoc.image=foc1
                spritefoc.rect=foc1.get_rect()
                if var4==0:
                    spritefoc.rect.top=sprite1.rect.top+5
                if var4==1 or var4==2:
                    spritefoc.rect.left=sprite1.rect.left+5
    
                if var1==1 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left+20
                if var1==2 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left-20
                if var4==1:
                    spritefoc.rect.top=sprite1.rect.top-20
                if var4==2:
                    spritefoc.rect.top=sprite1.rect.top+20
    
                mppj-=20
                sonido2.play()
                cont5+=1
    
            #MOVIMENTS BOLA DE FOC
            if var_magia==True:
                pantalla.blit(spritefoc.image,spritefoc.rect)
                if cont3==0:
                    cont3+=1
                    if var1==1 and var4==0:
                        var2=1
                    if var1==2 and var4==0:
                        var2=2
                    if var4==1:
                        var2=3
                    if var4==2:
                        var2=4
    
                if cont3>0 and cont4<70:
                    if var2==1:
                        spritefoc.rect.left+=10
                    if var2==2:
                        spritefoc.rect.left-=10
                    if var2==3:
                        spritefoc.rect.top-=10
                    if var2==4:
                        spritefoc.rect.top+=10
                    cont4+=2
    
            if spritefoc.rect.left<0 or spritefoc.rect.left>800 or spritefoc.rect.top>600 or spritefoc.rect.top<0 or cont4>=70 or spritefoc.rect.colliderect(sr1.rect) or spritefoc.rect.colliderect(sr2.rect) or spritefoc.rect.colliderect(sr3.rect):
                var_magia=False
                
            if var_magia==False:
                cont3=0
                cont4=0
                cont5=0
                spritefoc.rect.top=99999
                spritefoc.rect.left=99999
    
    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
            var_attackconfirm_l=sprite1.rect.left-spritemonstruo1.rect.left
            var_attackconfirm_t=sprite1.rect.top-spritemonstruo1.rect.top
    
            var_attackconfirm_l_2=sprite1.rect.left-sger.rect.left
            var_attackconfirm_t_2=sprite1.rect.top-sger.rect.top
    
    #accions que infringeixen dany al monstre (pop)
            
            if var3==True:
                if spritefoc.rect.colliderect(spritemonstruo1) and hpmonstruo1>0:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(5,15)
                    if hpmonstruo1<0:
                        hpmonstruo1==0
            
                if var1==1 and var_attackconfirm_l>-20 and var_attackconfirm_l<10 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left+10,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
                if var1==2 and var_attackconfirm_l>-10 and var_attackconfirm_l<20 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left-10)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
    
    #accions que infringeixen dany al monstre (guerrer)
            
            if var3_2==True:
                if spritefoc.rect.colliderect(sger) and hpmonstruo2>0:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(1,4)
                    if hpmonstruo2<0:
                        hpmonstruo2==0
            
                if var1==1 and var_attackconfirm_l_2>-25 and var_attackconfirm_l_2<20 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left+10,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
                if var1==2 and var_attackconfirm_l_2>-20 and var_attackconfirm_l_2<25 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left-10)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
    
    
    #accions que infringeixen dany al pj (pop)
                        
            if var3==True and spritemonstruo1.rect.colliderect(sprite1.rect) and hpmonstruo1>0 and hp_pj>0:
                hp_pj-=random.randrange(0,2)
                sprite1.rect.left-=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo1<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
    
    #accions que infringeixen dany al pj (guerrer d)
                        
            if var3_2==True and sger.rect.colliderect(sprite1.rect) and hpmonstruo2>0 and hp_pj>0:
                hp_pj-=random.randrange(1,4)
                sprite1.rect.left+=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo2<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
            
    
    #axo serveix perk no senkalli el pj en matar el monstre
            #if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6<50 and hpmonstruo1==0:
             #   sprite1.rect.left+=10
                
            #if sprite1.rect.colliderect(sger.rect) and cont6<50 and hpmonstruo2==0:
             #   sprite1.rect.left+=10
            
    #vida dels monstres          
            if var3==True:       
                hpm1=str(str(hpmonstruo1)+'/120')
    
            if var3_2==True:
                hpm2=str(str(hpmonstruo2)+'/100')
    
    #per fer desaparexer el pop un kop mort:
            if hpmonstruo1<=0 and cont6<70:
                hpmonstruo1=0
                cont6+=1
                if cont6==70:
                    cont6=0
                    var3=False
                    spritemonstruo1.rect.top=9999
                    spritemonstruo1.rect.left=9999
    
    #per fer desaparexer el guerrer un kop mort:
            if hpmonstruo2<=0 and cont15<70:
                hpmonstruo2=0
                cont15+=1
                if cont15==70:
                    cont15=0
                    var3_2=False
                    sger.rect.top=9999
                    sger.rect.left=9999
    
    
    #imprimacio de la vida dels monstres
            #pop       
            if var3==True:
                textohp1=fuente1.render(hpm1,0,rojo)
                pantalla.blit(textohp1,(spritemonstruo1.rect.left-10,spritemonstruo1.rect.top-25))
    
            #guerrer
            if var3_2==True:
                textohp2=fuente1.render(hpm2,0,rojo)
                pantalla.blit(textohp2,(sger.rect.left-10,sger.rect.top-25))
    
    
    #sistema k fa k el pj no travessi el monstre
            if hpmonstruo1==0:
                if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6>10 and var_c1==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
            if hpmonstruo2==0:
                if sprite1.rect.colliderect(sger.rect) and cont6>10 and var_c2==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
    
    
            if var3==False and cont11==0:
                cont6=0
                cont11+=1
    
            if var3==False and cont12==0:
                cont6=0
                cont12+=1
    
            if hp_pj==0:
                cont13+=1
    
            if cont13==50:
                sonido3.stop()
                menu1()
    
            if hp_pj<=0:
                pantalla.blit(textoGO,(200,200))
                if cont13==1:
                    sonidodead.play()
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                elif cont13==20:
                    sonidodead.stop()
                
    
    #per saber si sa akabat el nivell:
            if var8==True and var8_2==True and var8_3==True:
                pantalla.blit(textoV,(115,200))
                cont16+=1
                var9=True
                if cont16==60:
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                    sonido3.stop()
                    menu1()
    
    
                
                
            
    ###############################################################################
    ###############################################################################
    
    
            if vr3==False or vr3_2==False:
                    var7=1
                #si el monstre esta viu la imatge simprimex en la pantalla
                    
            if var7==1:
                if var3_3==True:
                    pantalla.blit(smonster.image,smonster.rect)
    
                    #moviments
                        
                    if var3_3==True and hpmonstruo3>0 and hp_pj>0:
                        variable1_3=random.randrange(0,5)
    
                        
                        
                        if variable1_3==0 or variable1_3==1:
                            if smonster.rect.left<770 and sprite1.rect.left>smonster.rect.left:
                                smonster.rect.left+=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image1
                                if variable1_3==1:
                                    smonster.image=monstruo3image3
                                var_md=1
                        if variable1_3==1 or variable1_3==2:
                            if smonster.rect.top<570 and sprite1.rect.top>smonster.rect.top:
                                smonster.rect.top+=random.randrange(0,25)
                                if var_md==1:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image1
                                    if variable1_3==1:
                                        smonster.image=monstruo3image3
                                if var_md==2:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image2
                                    if variable1_3==1:
                                        smonster.image=monstruo3image4
                        if variable1_3==2 or variable1_3==3:
                            if smonster.rect.top>15 and sprite1.rect.top<smonster.rect.top:
                                smonster.rect.top-=random.randrange(0,25)
                                if var_md==1:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image1
                                    if variable1_3==1:
                                        smonster.image=monstruo3image3
                                if var_md==2:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image2
                                    if variable1_3==1:
                                        smonster.image=monstruo3image4
                                    
                        if variable1==3 or variable1_3==0:
                            if smonster.rect.left>15 and sprite1.rect.left<smonster.rect.left:
                                smonster.rect.left-=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image2
                                if variable1_3==3:
                                    smonster.image=monstruo3image4
                                var_md=2
    
            
    
    
    
                    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
                    var_attackconfirm_l_3=sprite1.rect.left-smonster.rect.left
                    var_attackconfirm_t_3=sprite1.rect.top-smonster.rect.top
    
                #accions que infringeixen dany al monstre (snake)
    
                    if var3_3==True:
                        if spritefoc.rect.colliderect(smonster) and hpmonstruo3>0:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(5,15)
                            if hpmonstruo3<0:
                                hpmonstruo3==0
    
                        if var1==1 and var_attackconfirm_l_3>-20 and var_attackconfirm_l_3<10 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left+10,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
                        if var1==2 and var_attackconfirm_l_3>-10 and var_attackconfirm_l_3<20 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left-10)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
    
    
                    #accions que infringeixen dany al pj (snake)
                                
                    if var3_3==True and smonster.rect.colliderect(sprite1.rect) and hpmonstruo3>0 and hp_pj>0:
                        hp_pj-=random.randrange(0,2)
                        sprite1.rect.left-=random.randrange(-5,5)
                        sprite1.rect.top+=random.randrange(-5,5)
    
                        if var1==1:
                            sprite1.image=goblinhr
                        if var1==2:
                            sprite1.image=goblinhl
    
                    if hpmonstruo3<0:
                        hpmonstruo3==0
    
    
                    hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    textohppj=fuente1.render(hppjt,0,verde)
                    pantalla.blit(textohppj,(5,5))
    
                    #t=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    #textohppj=fuente1.render(hppjt,0,verde)
                    #pantalla.blit(textohppj,(5,5))
    
    
                    #axo serveix perk no senkalli el pj en matar el monstre
                    #if sprite1.rect.colliderect(smonster.rect) and cont6<50 and hpmonstruo3==0:
                     #   sprite1.rect.left+=10
                        
    
                    #vida dels monstres          
                    if var3_3==True:       
                        hpm3=str(str(hpmonstruo3)+'/80')
    
                    #per fer desaparexer el snake un kop mort:
                    
                    if hpmonstruo3<=0 and cont17<70:
                        hpmonstruo3=0
                        cont17+=1
                        if cont17==70:
                            cont17=0
                            var3_3=False
                            smonster.rect.top=9999
                            smonster.rect.left=9999
    
    
                    #imprimacio de la vida dels monstres       
                    if var3_3==True:
                        textohp1=fuente1.render(hpm3,0,rojo)
                        pantalla.blit(textohp1,(smonster.rect.left-10,smonster.rect.top-25))
    
    
                    #sistema k fa k el pj no travessi el monstre
                    if hpmonstruo3==0:
                        if sprite1.rect.colliderect(smonster.rect) and cont6>10 and var_c3==True:
                            sprite1.rect.left=xant
                            sprite1.rect.top=yant
    
                    
    
    
    
    
                    if var3_3==False and cont11==0:
                        cont6=0
                        cont11+=1
    
                    if var3_3==False and cont12==0:
                        cont6=0
                        cont12+=1
    
    
    
            vr3=var3
            vr3_2=var3_2
            vr3_3=var3_3
    
            
    
    
    #si el pop esta mort i sa mort menys de 4 vegades torna a aparexer depen del resultat de f
            if vr3==False and cont19<3:
                    spritemonstruo1=pygame.sprite.Sprite()
                    spritemonstruo1.image=monstruoimage1
                    spritemonstruo1.rect=monstruoimage1.get_rect()
                    spritemonstruo1.rect.top=random.randrange(0,570)
                    spritemonstruo1.rect.left=random.randrange(0,770)
                    hpmonstruo1=120
                    cont6=0
                    var3=True
                    cont19+=1
                    cont23=0
            if cont19==3 and var3==False:
                var8=True
                
    #
            if vr3_2==False and cont20<2:
                    sger=pygame.sprite.Sprite()
                    sger.image=monstruo2image1
                    sger.rect=monstruo2image1.get_rect()
                    sger.rect.top=random.randrange(0,570)
                    sger.rect.left=random.randrange(0,770)
                    hpmonstruo2=100
                    cont6=0
                    var3_2=True
                    cont20+=1
                    cont24=0
            if cont20==2 and var3_2==False:
                var8_2=True
    
    
    
            if vr3_3==False and cont21<5:
                    smonster=pygame.sprite.Sprite()
                    smonster.image=monstruo3image1
                    smonster.rect=monstruo3image1.get_rect()
                    smonster.rect.top=random.randrange(0,570)
                    smonster.rect.left=random.randrange(0,770)
                    hpmonstruo3=80
                    cont6=0
                    var3_3=True
                    cont21+=1
                    cont25=0
            if cont21==5 and var3_3==False:
                var8_3=True
    
                
    ####AKI ANIRA LU MATEX K LU DEL POP AM ELS ALTRES 2 MONSTRES
    
    #per k es recargi el mp:
            cont18+=1
            if cont18%10==0 and mppj<mpdatos:
                mppj+=1
        
    #imprimacio del mp:
            mppjt=str('MP: '+str(mppj)+'/'+str(mptpj))
            textomppj=fuente1.render(mppjt,0,verde)
            pantalla.blit(textomppj,(700,5))
    
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
    
    #per guardar la kantitat de diners i desblokejar el seguen nivell si sa completat la misio
            if var9==True:
                money_t=str(money)
                moneywriter=open('log\money.txt','w')
                moneywriter.write(money_t)
                moneywriter.close()
            
                moneyreader=open('log\money.txt')
                money=int(moneyreader.readline())
                moneyreader.close()
    
                if mision==3:
                    misionwriter=open('log\misions.txt','w')
                    misionwriter.write('4')
                    misionwriter.close()
    
            
    
    #per sumar diners al matar els monstres:
            if cont23==0 and hpmonstruo1==0:
                cont23+=1
                money+=random.randrange(10,22)
                print 'dinero:', money
    
            if cont24==0 and hpmonstruo2==0:
                cont24+=1
                money+=random.randrange(26,40)
                print 'dinero:', money
    
            if cont25==0 and hpmonstruo3==0:
                cont25+=1
                money+=random.randrange(10,15)
                print 'dinero:', money
    
                
                
    
            if hp_pj==0:
                money=perdrediners
                
                if contx==0:
                    print 'dinero: ', money
                    contx+=1
    
            tttmoney=str('Dinero: '+str(money))
            textomoney=fuente1.render(tttmoney,0,verde)
            pantalla.blit(textomoney,(200,5))
    
            misionreader=open('log\misions.txt')
            mision=int(misionreader.readline())
            misionreader.close()
    
        
            if sprite1.rect.colliderect(sr1.rect) or sprite1.rect.colliderect(sr2.rect) or sprite1.rect.colliderect(sr3.rect):     
                sprite1.rect.left=xant
                sprite1.rect.top=yant
    
    #prk el pj no surti del mapa:
            if sprite1.rect.left<=0:
                sprite1.rect.left=0
            if sprite1.rect.top<=0:
                sprite1.rect.top=0
            if sprite1.rect.left>=780:
                sprite1.rect.left=780
            if sprite1.rect.top>=550:
                sprite1.rect.top=550
    
    #prk els monstres no chokin am les palmeras:
            if smonster.rect.colliderect(sr1.rect) or smonster.rect.colliderect(sr2.rect) or smonster.rect.colliderect(sr3.rect) and contG>0:
                smonster.rect.left=xmant1
                smonster.rect.top=ymant1
                contE3+=1
            else:
                contE3=0
            if sger.rect.colliderect(sr1.rect) or sger.rect.colliderect(sr2.rect) or sger.rect.colliderect(sr3.rect) and contG>0:
                sger.rect.left=xmant2
                sger.rect.top=ymant2
                contE2+=1
            else:
                contE2=0
            if spritemonstruo1.rect.colliderect(sr1.rect) or spritemonstruo1.rect.colliderect(sr2.rect) or spritemonstruo1.rect.colliderect(sr3.rect) and contG>0:
                spritemonstruo1.rect.left=xmant3
                spritemonstruo1.rect.top=ymant3
                contE1+=1
            else:
                contE1=0
    
            #imprimacio de las rokass
            pantalla.blit(sr1.image,sr1.rect)
            pantalla.blit(sr2.image,sr2.rect)
            pantalla.blit(sr3.image,sr3.rect)
    
            #imprimacio dels arbres
            #pantalla.blit(sa1.image,sa1.rect)
            #pantalla.blit(sa2.image,sa2.rect)
            #pantalla.blit(sa3.image,sa3.rect)
            
    
    #perk el pj no senkalli am els monstres:
            if hpmonstruo1==0 and sprite1.rect.colliderect(spritemonstruo1)==False:
                var_c1=True
            if hpmonstruo2==0 and sprite1.rect.colliderect(sger)==False:
                var_c2=True
            if hpmonstruo3==0 and sprite1.rect.colliderect(smonster)==False:
                var_c3=True
    
            if hpmonstruo1>0:
                var_c1=False
            if hpmonstruo2>0:
                var_c2=False
            if hpmonstruo3>0:
                var_c3=False
    
    #per si el monstre aparex sobre una roka k es mogi per no enkallarse
            #if contE1==2:
             #   smonster.rect.left+=10
            #if contE2==2:
             #   sger.rect.left+=10
            #if contE3==2:
             #   spritemonstruo1.rect.left+=10
    
    #perk kridin els monstres kuan morin:
            if hpmonstruo1==0 and contC1==0:
                sonidocrit1.play()
                contC1+=1
            if hpmonstruo1>0:
                contC1=0
    
            if hpmonstruo2==0 and contC2==0:
                sonidocrit2.play()
                contC2+=1
            if hpmonstruo2>0:
                contC2=0
    
            if hpmonstruo3==0 and contC3==0:
                sonidocrit3.play()
                contC3+=1
            if hpmonstruo3>0:
                contC3=0
    
    #per fer k el gerrer tingi la imatge de atacant:
            if hpmonstruo2>0 and sger.rect.colliderect(sprite1) and var_d2==1:
                if contG%2==0:
                    sger.image=monstruo2image5
    
            if hpmonstruo2>0 and sger.rect.colliderect(sprite1) and var_d2==2:
                if contG%2==0:
                    sger.image=monstruo2image6
    
            
            #textos pocions:
            potionhpt=str('Pociones HP: '+str(potionshp))
            potionmpt=str('Pociones MP: '+str(potionsmp))
            textohpp=fuente1.render(potionhpt,0,verde)
            textompp=fuente1.render(potionmpt,0,verde)
            pantalla.blit(textohpp,(350,5))
            pantalla.blit(textompp,(500,5))
    
    
            if var_escudo==True:
                spritee.rect.top=sprite1.rect.top-15
                spritee.rect.left=sprite1.rect.left-25
            else:
                spritee.rect.top=999999
                spritee.rect.left=999999
    
            if var_escudo==True:
                cont_escudo+=1
            if var_escudo==True and var_potion==False:
                hp_pj=hp_pjant
    
            if cont_escudo==100:
                var_escudo=False
                cont_escudo=0
    
            
            
    
            pantalla.blit(spritee.image,spritee.rect)
            
            #per fer k leskut giri :)
            if var_escudo==True:
                escut_i=pygame.transform.rotate(escut_i, 90)
                spritee.image=escut_i
    
            
            contG+=1
            
            pygame.display.update()
        pygame.quit()
    
    def guerra4():
        pygame.init()
        pygame.key.set_repeat(20)
        pantalla=pygame.display.set_mode((800,600))
        fondo=pygame.image.load("images/goblinw/fons4.png")
        pygame.display.set_caption('GOBLIN W.')
    
        #rectangles dels arbres
        r_a1=pygame.Rect(80,300,10,30)
        r_a2=pygame.Rect(400,200,10,30)
        r_a3=pygame.Rect(700,400,10,30)
    
        #pygame.draw.rect(pantalla,(0,0,0),r_a1)
        #pygame.draw.rect(pantalla,(0,0,0),r_a2)
        #pygame.draw.rect(pantalla,(0,0,0),r_a3)
    
    
        #SONS
        sonido1=pygame.mixer.Sound("sounds/goblinw/Blast.wav")
        sonido2=pygame.mixer.Sound("sounds/goblinw/explosion.wav")
        sonido3=pygame.mixer.Sound("sounds/goblinw/BSO5.wav")
        sonidodead=pygame.mixer.Sound("sounds/goblinw/deadpj.wav")
        sonidoespada=pygame.mixer.Sound("sounds/goblinw/Sspada.wav")
        sonidoespadaF=pygame.mixer.Sound("sounds/goblinw/SspadaF.wav")
        sonidocrit1=pygame.mixer.Sound("sounds/goblinw/crit1.wav")
        sonidocrit2=pygame.mixer.Sound("sounds/goblinw/crit2.wav")
        sonidocrit3=pygame.mixer.Sound("sounds/goblinw/crit3.wav")
        sonidorun=pygame.mixer.Sound("sounds/goblinw/run.wav")
        sopotion=pygame.mixer.Sound("sounds/goblinw/potion.wav")
        s_terremoto=pygame.mixer.Sound("sounds/goblinw/terremoto.wav")
        #sonidocrit3=pygame.mixer.Sound("sounds/goblinw/.wav")
    
        
        #goblin parat
        goblin1=pygame.image.load("images/goblinw/Idle0.png").convert_alpha()
        goblin2=pygame.image.load("images/goblinw/Idle1.png").convert_alpha()
    
        #goblin caminant cap a la dreta
        goblinwr1=pygame.image.load("images/goblinw/Walk0.png").convert_alpha()
        goblinwr2=pygame.image.load("images/goblinw/Walk1.png").convert_alpha()
        goblinwr3=pygame.image.load("images/goblinw/Walk2.png").convert_alpha()
        goblinwr4=pygame.image.load("images/goblinw/Walk3.png").convert_alpha()
    
        #goblin caminant cap a leskerra
        goblinwl1=pygame.image.load("images/goblinw/Walkl0.png").convert_alpha()
        goblinwl2=pygame.image.load("images/goblinw/Walkl1.png").convert_alpha()
        goblinwl3=pygame.image.load("images/goblinw/Walkl2.png").convert_alpha()
        goblinwl4=pygame.image.load("images/goblinw/Walkl3.png").convert_alpha()
    
        #goblin atakant cap a la dreta
        goblinar1=pygame.image.load("images/goblinw/Attack0.png").convert_alpha()
        goblinar2=pygame.image.load("images/goblinw/Attack1.png").convert_alpha()
        goblinar3=pygame.image.load("images/goblinw/Attack2.png").convert_alpha()
    
        #goblin atacant cap a leskerra
        goblinal1=pygame.image.load("images/goblinw/Attackl0.png").convert_alpha()
        goblinal2=pygame.image.load("images/goblinw/Attackl1.png").convert_alpha()
        goblinal3=pygame.image.load("images/goblinw/Attackl2.png").convert_alpha()
    
        #goblin atacant am magia cap a la dreta
        goblinamr=pygame.image.load("images/goblinw/Attackmr.png").convert_alpha()
    
        #goblin atacant am magia kap a leskerra
        goblinaml=pygame.image.load("images/goblinw/Attackml.png").convert_alpha()
    
        #goblin mort 1
        goblindr=pygame.image.load("images/goblinw/Dead0.png").convert_alpha()
    
        #goblin mort 2
        goblindl=pygame.image.load("images/goblinw/Dead1.png").convert_alpha()
    
        #goblin golpejat 1
        goblinhr=pygame.image.load("images/goblinw/Hurt0.png").convert_alpha()
    
        #goblin golpejat 2
        goblinhl=pygame.image.load("images/goblinw/Hurt1.png").convert_alpha()
    
        
        #bola de foc
        foc1=pygame.image.load("images/goblinw/foc.png").convert_alpha()
    
        #monstres
        
        #POP
        monstruoimage1=pygame.image.load("images/goblinw/monstruo2.png").convert_alpha()
        monstruoimage3=pygame.image.load("images/goblinw/monstruo2_3.png").convert_alpha()
        monstruoimage4=pygame.image.load("images/goblinw/monstruo2_4.png").convert_alpha()
        monstruoimage5=pygame.image.load("images/goblinw/monstruo2_5.png").convert_alpha()
        monstruoimage6=pygame.image.load("images/goblinw/monstruo2_6.png").convert_alpha()
    
        #GUERRER DAURAT
        monstruo2image1=pygame.image.load("images/goblinw/guerrero2.png").convert_alpha()
        monstruo2image2=pygame.image.load("images/goblinw/guerrero2_2.png").convert_alpha()
        monstruo2image3=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
        monstruo2image4=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
        monstruo2image5=pygame.image.load("images/goblinw/guerrero2_5.png").convert_alpha()
        monstruo2image6=pygame.image.load("images/goblinw/guerrero2_6.png").convert_alpha()
        monstruo2image7=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
        monstruo2image8=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
        monstruo2image9=pygame.image.load("images/goblinw/guerrero2_7.png").convert_alpha()
        
    
        #monstre 3 (sNakE)
        monstruo3image1=pygame.image.load("images/goblinw/guerrero3.png").convert_alpha()
        monstruo3image2=pygame.image.load("images/goblinw/guerrero3_2.png").convert_alpha()
        monstruo3image3=pygame.image.load("images/goblinw/guerrero3_3.png").convert_alpha()
        monstruo3image4=pygame.image.load("images/goblinw/guerrero3_4.png").convert_alpha()
        monstruo3image5=pygame.image.load("images/goblinw/guerrero3_5.png").convert_alpha()
        monstruo3image6=pygame.image.load("images/goblinw/guerrero3_6.png").convert_alpha()
        monstruo3image7=pygame.image.load("images/goblinw/guerrero3_7.png").convert_alpha()
        monstruo3image8=pygame.image.load("images/goblinw/guerrero3_8.png").convert_alpha()
        monstruo3image9=pygame.image.load("images/goblinw/guerrero3_9.png").convert_alpha()
        monstruo3image10=pygame.image.load("images/goblinw/guerrero3_9.png").convert_alpha()
        monstruo3image11=pygame.image.load("images/goblinw/guerrero3_9.png").convert_alpha()
    
        #imatges dels arbres
        tree1image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree2image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree3image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
    
        #imatges de las rokas
        rock1image=pygame.image.load("images/goblinw/roca.png").convert_alpha()
        rock2image=pygame.image.load("images/goblinw/roca2.png").convert_alpha()
    
    
        #imatge eskut
        escut_i=pygame.image.load("images/goblinw/escudo_m.png").convert_alpha()
    
            
        #sprite del goblin
        sprite1=pygame.sprite.Sprite()
        sprite1.image=goblin1
        sprite1.rect=goblin1.get_rect()
        sprite1.rect.top=100
        sprite1.rect.left=50
    
        #sprite de la bola de foc
        spritefoc=pygame.sprite.Sprite()
        spritefoc.image=foc1
        spritefoc.rect=foc1.get_rect()
        spritefoc.rect.top=9999
        spritefoc.rect.left=9999
    
        #sprite de monstre pop 1
        spritemonstruo1=pygame.sprite.Sprite()
        spritemonstruo1.image=monstruoimage1
        spritemonstruo1.rect=monstruoimage1.get_rect()
        spritemonstruo1.rect.top=random.randrange(0,570)
        spritemonstruo1.rect.left=random.randrange(0,770)
    
        #sprite de monstre guerrer 2
        sger=pygame.sprite.Sprite()
        sger.image=monstruo2image1
        sger.rect=monstruo2image1.get_rect()
        sger.rect.top=random.randrange(0,570)
        sger.rect.left=random.randrange(0,770)
    
        #sprite del snake 3
        smonster=pygame.sprite.Sprite()
        smonster.image=monstruo3image1
        smonster.rect=monstruo3image1.get_rect()
        smonster.rect.top=random.randrange(0,570)
        smonster.rect.left=random.randrange(0,770)
    
        #sprite de leskut
        spritee=pygame.sprite.Sprite()
        spritee.image=escut_i
        spritee.rect=escut_i.get_rect()
        spritee.rect.top=sprite1.rect.top
        spritee.rect.left=sprite1.rect.left
    
        #sprites de las rokas
        #1
        sr1=pygame.sprite.Sprite()
        sr1.image=rock1image
        sr1.rect=rock1image.get_rect()
        sr1.rect.top=280
        sr1.rect.left=60
        #2
        sr2=pygame.sprite.Sprite()
        sr2.image=rock2image
        sr2.rect=rock2image.get_rect()
        sr2.rect.top=70
        sr2.rect.left=400
        #3
        sr3=pygame.sprite.Sprite()
        sr3.image=rock2image
        sr3.rect=rock2image.get_rect()
        sr3.rect.top=350
        sr3.rect.left=500
        
    
        #arbres k no utilitzu xd
        sa1=pygame.sprite.Sprite()
        sa1.image=tree1image
        sa1.rect=tree1image.get_rect()
        sa1.rect.top=280
        sa1.rect.left=60
    
        sa2=pygame.sprite.Sprite()
        sa2.image=tree1image
        sa2.rect=tree1image.get_rect()
        sa2.rect.top=95
        sa2.rect.left=372
    
        sa3=pygame.sprite.Sprite()
        sa3.image=tree1image
        sa3.rect=tree1image.get_rect()
        sa3.rect.top=350
        sa3.rect.left=677
    
        #r_a1=pygame.Rect(87,320,10,30)
        #r_a2=pygame.Rect(400,135,10,30)
        #r_a3=pygame.Rect(705,392,10,30)
        
    
        #fuentes
        fuente1=pygame.font.SysFont("Arial",16,True,False)
        fuentevidapj=pygame.font.SysFont("Arial",25,True,False)
        fuenteGO=pygame.font.SysFont("Arial",70,True,False)
    
        
    
        #colors:
        rojo=(255,0,0)
        azul=(0,0,255)
        verde=(0,255,0)
        blanco=(255,255,255)
        negro=(0,0,0)
    
        #textos constants
        textoGO=fuenteGO.render('GAME OVER',0,rojo)
        textoV=fuenteGO.render('NIVEL COMPLETADO',0,azul)
    
        #altres variables i contadors
        cont5=0
        cont4=0
        cont3=0
        cont1=0
        cont2=0
        cont6=0
        cont11=0
        cont12=0
        cont13=0
        cont15=0
        cont16=0
        cont17=0
        cont18=0
        cont19=0
        cont20=0
        cont21=0
        cont22=0
        contx=0
        cont23=0
        cont24=0
        cont25=0
        contG=0
        contE1=0
        contE2=0
        contE3=0
        contC1=0
        contC2=0
        contC3=0
        cont_escudo=0
        cont_terremoto=0
        #########
        var1=1
        var2=0
        var3=True  #<---variable per saber si el monstre esta viu
        var3_2=True #<---variable per saber si el monstre 2 esta viu
        var3_3=True #<---variable per saber si el monster 3 esta viu
        var4=0
        vr3=var3
        vr3_2=var3_2
        vr3_3=var3_3
        var7=0
        var8=False # variable k indica si san matat prous pops per finalitzar el nivell
        var8_2=False
        var8_3=False
        var9=False
        var_c1=True
        var_c2=True
        var_c3=True
        var_d2=1
        var_md=1#direccio guerrer drago
        var_escudo=False
        var_potion=False
        var_terremoto=False
    
        #variables per saber si sesta atacant o si sa tirat magia
        var_attack=False
        var_magia=False
    
        #vida monstres i pj
        hpmonstruo1=100
        hpmonstruo2=100
        hpmonstruo3=50
    
    
        #per llegir les pocions
        potionsreader=open('log\potions.txt')
        potionshp=int(potionsreader.readlines()[0])
        print 'potions hp: ', potionshp
        potionsreader.close()
        
        potionsreader=open('log\potions.txt')
        potionsmp=int(potionsreader.readlines()[1])
        print 'potions mp: ', potionsmp
        potionsreader.close()
    
        
    
    #per llegir el hp del pj:
        datosreader=open('log\datos.txt')
        hpdatos=int(datosreader.readlines()[0])
        print 'hp: ', hpdatos
        datosreader.close()
    
        hp_pj=hpdatos
        hpt_pj=hp_pj
    
        #variable del bucle principal
        salir=False
    
        #reloj
        reloj1=pygame.time.Clock()
    
        #grup de sprites de monstres
        grupo_m=pygame.sprite.Group(spritemonstruo1,sger,smonster)
    
    
    
    
    
    
    
    #escudo i atak terratremol
        tendareader=open('log/shop.txt')
        escudo=int(tendareader.readlines()[0])
        tendareader.close()
        print 'escudo', escudo
        
        tendareader=open('log/shop.txt')
        terremoto=int(tendareader.readlines()[1])
        tendareader.close()
        print 'terremoto', terremoto
    
    
    
    
    
    
    
    #per llegir el mp del pj:
    
        datosreader=open('log\datos.txt')
        mpdatos=int(datosreader.readlines()[1])
        print 'mp: ', mpdatos
        datosreader.close()
        
        #mp del pj
        mptpj=mpdatos
        mppj=mptpj
    
    ######
        #variable diners
        moneyreader=open('log\money.txt')
        money=int(moneyreader.readline())
        print 'dinero:', money
        moneyreader.close()
    
        money_t=str(money)
        moneywriter=open('log\money.txt','w')
        moneywriter.write(money_t)
        moneywriter.close()
    
        perdrediners=money
        
    
        sonido3.play()
    
    
        while salir != True:
            if cont20==1:
                monstruo2image1=pygame.image.load("images/goblinw/guerrero1.png").convert_alpha()
                monstruo2image2=pygame.image.load("images/goblinw/guerrero1_2.png").convert_alpha()
                monstruo2image3=pygame.image.load("images/goblinw/guerrero1_4.png").convert_alpha()
                monstruo2image4=pygame.image.load("images/goblinw/guerrero1_3.png").convert_alpha()
                monstruo2image5=pygame.image.load("images/goblinw/guerrero1_5.png").convert_alpha()
                monstruo2image6=pygame.image.load("images/goblinw/guerrero1_6.png").convert_alpha()
                monstruo2image7=pygame.image.load("images/goblinw/guerrero1_3.png").convert_alpha()
                monstruo2image8=pygame.image.load("images/goblinw/guerrero1_4.png").convert_alpha()
                monstruo2image9=pygame.image.load("images/goblinw/guerrero1_9.png").convert_alpha()
            else:
                monstruo2image1=pygame.image.load("images/goblinw/guerrero2.png").convert_alpha()
                monstruo2image2=pygame.image.load("images/goblinw/guerrero2_2.png").convert_alpha()
                monstruo2image3=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
                monstruo2image4=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
                monstruo2image5=pygame.image.load("images/goblinw/guerrero2_5.png").convert_alpha()
                monstruo2image6=pygame.image.load("images/goblinw/guerrero2_6.png").convert_alpha()
                monstruo2image7=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
                monstruo2image8=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
                monstruo2image9=pygame.image.load("images/goblinw/guerrero2_7.png").convert_alpha()
            
            if cont19==0 or cont19==1:
                monstruoimage1=pygame.image.load("images/goblinw/monstruo1.png").convert_alpha()
                monstruoimage3=pygame.image.load("images/goblinw/monstruo1_3.png").convert_alpha()
                monstruoimage4=pygame.image.load("images/goblinw/monstruo1_4.png").convert_alpha()
                monstruoimage5=pygame.image.load("images/goblinw/monstruo1_5.png").convert_alpha()
                monstruoimage6=pygame.image.load("images/goblinw/monstruo1_6.png").convert_alpha()
                
            else:
                monstruoimage1=pygame.image.load("images/goblinw/monstruo2.png").convert_alpha()
                monstruoimage3=pygame.image.load("images/goblinw/monstruo2_3.png").convert_alpha()
                monstruoimage4=pygame.image.load("images/goblinw/monstruo2_4.png").convert_alpha()
                monstruoimage5=pygame.image.load("images/goblinw/monstruo2_5.png").convert_alpha()
                monstruoimage6=pygame.image.load("images/goblinw/monstruo2_6.png").convert_alpha()
                
                
        
                
            var_potion=False
            
            hp_pjant=hp_pj
    
            if hp_pj<=0 and var1==1:
                sprite1.image=goblindr
    
            if hp_pj<=0 and var1==2:
                sprite1.image=goblindl
                
    
            xant=sprite1.rect.left
            yant=sprite1.rect.top
    
            if hpmonstruo1<0:
                hpmonstruo1==0
            
            if hpmonstruo1==0:
                spritemonstruo1.image=monstruoimage3
    
    
    
            if hpmonstruo2<0:
                hpmonstruo2==0
            
            if hpmonstruo2==0:
                sger.image=monstruo2image9
    
                
    
            if hpmonstruo3<0:
                hpmonstruo3==0
            
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
                
    
            if hp_pj<0:
                hp_pj=0
                
    
    
            xmant1=smonster.rect.left
            ymant1=smonster.rect.top
            xmant2=sger.rect.left
            ymant2=sger.rect.top
            xmant3=spritemonstruo1.rect.left
            ymant3=spritemonstruo1.rect.top
    
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN and hp_pj>0:
    
                    if event.key==pygame.K_LEFT and sprite1.rect.left>0:
                        if cont1==0:
                            sprite1.image=goblinwl1
                        if cont1==1:
                            sprite1.image=goblinwl2
                        if cont1==2:
                            sprite1.image=goblinwl3
                        if cont1==3:
                            sprite1.image=goblinwl4
                        if cont1==4:
                            sprite1.image=goblinwl3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left-=6
                        cont1+=1
                        var1=2
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
                        
    
                    if event.key==pygame.K_RIGHT and sprite1.rect.left<775:
                        if cont1==0:
                            sprite1.image=goblinwr1
                        if cont1==1:
                            sprite1.image=goblinwr2
                        if cont1==2:
                            sprite1.image=goblinwr3
                        if cont1==3:
                            sprite1.image=goblinwr4
                        if cont1==4:
                            sprite1.image=goblinwr3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left+=6
                        cont1+=1
                        var1=1
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_UP and sprite1.rect.top>0:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
                            
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top-=6
                        cont1+=1
                        var4=1
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_DOWN and sprite1.rect.top<555:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top+=6
                        cont1+=1
                        var4=2
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_SPACE:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinar2
                            if cont1==1:
                                sprite1.image=goblinar1
                            if cont1==2:
                                sprite1.image=goblinar1
                            if cont1==3:
                                sprite1.image=goblinar2
                            if cont1==4:
                                sprite1.image=goblinar3
                            if cont1>=5:
                                cont1=0
                                sprite1.image=goblinar2
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinal2
                            if cont1==1:
                                sprite1.image=goblinal1
                            if cont1==2:
                                sprite1.image=goblinal2
                            if cont1==3:
                                sprite1.image=goblinal3
                            if cont1>=4:
                                cont1=0
                                sprite1.image=goblinal2
                                
                        cont1+=1
                        var_attack=True
                        if cont1%2==0:
                            sonidoespadaF.play()
    
                        
                            
    
                        
                    if event.key==pygame.K_m:
                        if cont2<=3:
                            if var1==1:
                                sprite1.image=goblinamr
                            if var1==2:
                                sprite1.image=goblinaml
                        if cont2==4:
                            if var1==1:
                                sprite1.image=goblin1
                            if var1==2:
                                sprite1.image=goblin2
                        if cont2==1 and mppj>=20:
                            var_magia=True
                        cont2+=1
    
    
                    if event.key==pygame.K_h and potionshp>0 and hp_pj>0:
                        if hp_pj<hpt_pj:
                            potionshp-=1
                            hp_pj+=random.randrange(15,20)
                            sopotion.play()
                            print 'potionshp: ', potionshp
                            var_potion=True
                            
                            if hp_pj>hpt_pj:
                                hp_pj=hpt_pj
    
                    if event.key==pygame.K_j and potionsmp>0 and hp_pj>0:
                        if mppj<mptpj:
                            potionsmp-=1
                            mppj+=random.randrange(10,20)
                            sopotion.play()
                            print 'potionsmp: ', potionsmp
                            
                            if mppj>mptpj:
                                mppj=mptpj
    
                    if event.key==pygame.K_n and escudo==1 and hp_pj>0 and mppj>=60:
                        mppj-=60
                        var_escudo=True
                        print 'escudo activado'
                    
                    if event.key==pygame.K_b and terremoto==1 and hp_pj>0 and mppj>=250 and var_terremoto==False:
                        mppj-=250
                        var_terremoto=True
                        print 'terremoto activado'
                        
                        
    
                    if event.key==pygame.K_ESCAPE:
                        sonido3.stop()
                        menu1()
                            
                            
                    
                if event.type==pygame.KEYUP and hp_pj>0:
                    if var1==1:
                        sprite1.image=goblin1
                    if var1==2:
                        sprite1.image=goblin2
                        
                    var_attack=False
                    cont2=0
                    cont1=0
                    
    
            reloj1.tick(17)
            
            
            pantalla.blit(fondo,(0,0))
            
            if var_terremoto==True:
                if var3==True:
                    hpmonstruo1=0
                if var3_2==True:
                    hpmonstruo2=0
                if var3_3==True and var7==1:
                    hpmonstruo3=0
                s_terremoto.play()
                cont_terremoto+=1
                if cont_terremoto%2==0:
                    pantalla.blit(fondo,(random.randrange(0,5),random.randrange(0,5)))
                else:
                    pantalla.blit(fondo,(0,0))
            if cont_terremoto==10:
                var_terremoto=False
                cont_terremoto=0
    
            pantalla.blit(sprite1.image,sprite1.rect)
    
            
    
            if var3==True:
                pantalla.blit(spritemonstruo1.image,spritemonstruo1.rect)
    
    
            if var3_2==True:
                pantalla.blit(sger.image,sger.rect)
    
            
            
            #MOVIMENTS DEL MONSTRE 1 (pop)
                
            if var3==True and hpmonstruo1>0 and hp_pj>0:
                variable1=random.randrange(0,5)
    
    
                if variable1==0 or variable1==1:
                    if spritemonstruo1.rect.left<770 and sprite1.rect.left>spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left+=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage5
                if variable1==1 or variable1==2:
                    if spritemonstruo1.rect.top<570 and sprite1.rect.top>spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top+=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage1
                if variable1==2 or variable1==3:
                    if spritemonstruo1.rect.top>15 and sprite1.rect.top<spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top-=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage6
                if variable1==3 or variable1==0:
                    if spritemonstruo1.rect.left>15 and sprite1.rect.left<spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left-=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage4
    
            #MOVIMENTS DEL MONSTRE 2 (guerrer daurat)
                
            if var3_2==True and hpmonstruo2>0 and hp_pj>0:
                variable1_2=random.randrange(0,5)
    
    
                if variable1_2==0 or variable1_2==1:
                    if sger.rect.left<770 and sprite1.rect.left>sger.rect.left:
                        sger.rect.left+=random.randrange(0,10)
                        randomvar1=random.randrange(0,2)
                        if randomvar1==0:
                            sger.image=monstruo2image2
                        else:
                            sger.image=monstruo2image3
                        var_d2=1
                            
                if variable1_2==1 or variable1_2==2:
                    if sger.rect.top<570 and sprite1.rect.top>sger.rect.top:
                        sger.rect.top+=random.randrange(0,7)
                        randomvar1=random.randrange(0,2)
                        if var_d2==1:
                            if randomvar1==0:
                                sger.image=monstruo2image2
                            else:
                                sger.image=monstruo2image3
    
                        if var_d2==2:
                            if randomvar1==0:
                                sger.image=monstruo2image1
                            else:
                                sger.image=monstruo2image4
    
                            
                            
                if variable1_2==2 or variable1_2==3:
                    if sger.rect.top>15 and sprite1.rect.top<sger.rect.top:
                        sger.rect.top-=random.randrange(0,7)
                        randomvar1=random.randrange(0,2)
                        if var_d2==1:
                            if randomvar1==0:
                                sger.image=monstruo2image2
                            else:
                                sger.image=monstruo2image3
    
                        if var_d2==2:
                            if randomvar1==0:
                                sger.image=monstruo2image1
                            else:
                                sger.image=monstruo2image4
                        
                        
                            
                if variable1_2==3 or variable1_2==0:
                    if sger.rect.left>15 and sprite1.rect.left<sger.rect.left:
                        sger.rect.left-=random.randrange(0,10)
                        randomvar1=random.randrange(0,2)
                        if randomvar1==0:
                            sger.image=monstruo2image1
                        else:
                            sger.image=monstruo2image4
                        var_d2=2
    
            
                        
                        
            #"INVOCACIO" BOLA DE FOC
                        
            if var_magia==True and cont5==0 and mppj>20:
                #sprite de la bola de foc
                spritefoc=pygame.sprite.Sprite()
                spritefoc.image=foc1
                spritefoc.rect=foc1.get_rect()
                if var4==0:
                    spritefoc.rect.top=sprite1.rect.top+5
                if var4==1 or var4==2:
                    spritefoc.rect.left=sprite1.rect.left+5
    
                if var1==1 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left+20
                if var1==2 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left-20
                if var4==1:
                    spritefoc.rect.top=sprite1.rect.top-20
                if var4==2:
                    spritefoc.rect.top=sprite1.rect.top+20
    
                mppj-=20
                sonido2.play()
                cont5+=1
    
            #MOVIMENTS BOLA DE FOC
            if var_magia==True:
                pantalla.blit(spritefoc.image,spritefoc.rect)
                if cont3==0:
                    cont3+=1
                    if var1==1 and var4==0:
                        var2=1
                    if var1==2 and var4==0:
                        var2=2
                    if var4==1:
                        var2=3
                    if var4==2:
                        var2=4
    
                if cont3>0 and cont4<70:
                    if var2==1:
                        spritefoc.rect.left+=10
                    if var2==2:
                        spritefoc.rect.left-=10
                    if var2==3:
                        spritefoc.rect.top-=10
                    if var2==4:
                        spritefoc.rect.top+=10
                    cont4+=2
    
            if spritefoc.rect.left<0 or spritefoc.rect.left>800 or spritefoc.rect.top>600 or spritefoc.rect.top<0 or cont4>=70 or spritefoc.rect.colliderect(sr1.rect) or spritefoc.rect.colliderect(sr2.rect) or spritefoc.rect.colliderect(sr3.rect):
                var_magia=False
                
            if var_magia==False:
                cont3=0
                cont4=0
                cont5=0
                spritefoc.rect.top=99999
                spritefoc.rect.left=99999
    
    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
            var_attackconfirm_l=sprite1.rect.left-spritemonstruo1.rect.left
            var_attackconfirm_t=sprite1.rect.top-spritemonstruo1.rect.top
    
            var_attackconfirm_l_2=sprite1.rect.left-sger.rect.left
            var_attackconfirm_t_2=sprite1.rect.top-sger.rect.top
    
    #accions que infringeixen dany al monstre (pop)
            
            if var3==True:
                if spritefoc.rect.colliderect(spritemonstruo1) and hpmonstruo1>0:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(5,15)
                    if hpmonstruo1<0:
                        hpmonstruo1==0
            
                if var1==1 and var_attackconfirm_l>-20 and var_attackconfirm_l<10 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left+10,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
                if var1==2 and var_attackconfirm_l>-10 and var_attackconfirm_l<20 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left-10)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
    
    #accions que infringeixen dany al monstre (guerrer)
            
            if var3_2==True:
                if spritefoc.rect.colliderect(sger) and hpmonstruo2>0:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(1,4)
                    if hpmonstruo2<0:
                        hpmonstruo2==0
            
                if var1==1 and var_attackconfirm_l_2>-25 and var_attackconfirm_l_2<20 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left+10,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
                if var1==2 and var_attackconfirm_l_2>-20 and var_attackconfirm_l_2<25 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left-10)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
    
    
    #accions que infringeixen dany al pj (pop)
                        
            if var3==True and spritemonstruo1.rect.colliderect(sprite1.rect) and hpmonstruo1>0 and hp_pj>0:
                hp_pj-=random.randrange(0,2)
                sprite1.rect.left-=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo1<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
    
    #accions que infringeixen dany al pj (guerrer d)
                        
            if var3_2==True and sger.rect.colliderect(sprite1.rect) and hpmonstruo2>0 and hp_pj>0:
                hp_pj-=random.randrange(1,4)
                sprite1.rect.left+=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo2<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
            
    
    #axo serveix perk no senkalli el pj en matar el monstre
            #if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6<50 and hpmonstruo1==0:
             #   sprite1.rect.left+=10
                
            #if sprite1.rect.colliderect(sger.rect) and cont6<50 and hpmonstruo2==0:
             #   sprite1.rect.left+=10
            
    #vida dels monstres          
            if var3==True:
                if cont19==0 or cont19==1:       
                    hpm1=str(str(hpmonstruo1)+'/100')
                else:       
                    hpm1=str(str(hpmonstruo1)+'/120')
                
    
            if var3_2==True:
                hpm2=str(str(hpmonstruo2)+'/100')
    
    #per fer desaparexer el pop un kop mort:
            if hpmonstruo1<=0 and cont6<70:
                hpmonstruo1=0
                cont6+=1
                if cont6==70:
                    cont6=0
                    var3=False
                    spritemonstruo1.rect.top=9999
                    spritemonstruo1.rect.left=9999
    
    #per fer desaparexer el guerrer un kop mort:
            if hpmonstruo2<=0 and cont15<70:
                hpmonstruo2=0
                cont15+=1
                if cont15==70:
                    cont15=0
                    var3_2=False
                    sger.rect.top=9999
                    sger.rect.left=9999
    
    
    #imprimacio de la vida dels monstres
            #pop       
            if var3==True:
                textohp1=fuente1.render(hpm1,0,rojo)
                pantalla.blit(textohp1,(spritemonstruo1.rect.left-10,spritemonstruo1.rect.top-25))
    
            #guerrer
            if var3_2==True:
                textohp2=fuente1.render(hpm2,0,rojo)
                pantalla.blit(textohp2,(sger.rect.left-10,sger.rect.top-25))
    
    
    #sistema k fa k el pj no travessi el monstre
            if hpmonstruo1==0:
                if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6>10 and var_c1==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
            if hpmonstruo2==0:
                if sprite1.rect.colliderect(sger.rect) and cont6>10 and var_c2==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
    
    
            if var3==False and cont11==0:
                cont6=0
                cont11+=1
    
            if var3==False and cont12==0:
                cont6=0
                cont12+=1
    
            if hp_pj==0:
                cont13+=1
    
            if cont13==50:
                sonido3.stop()
                menu1()
    
            if hp_pj<=0:
                pantalla.blit(textoGO,(200,200))
                if cont13==1:
                    sonidodead.play()
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                elif cont13==20:
                    sonidodead.stop()
                
    
    #per saber si sa akabat el nivell:
            if var8==True and var8_2==True and var8_3==True:
                pantalla.blit(textoV,(115,200))
                cont16+=1
                var9=True
                if cont16==60:
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                    sonido3.stop()
                    menu1()
    
    
                
                
            
    ###############################################################################
    ###############################################################################
    
    
            if vr3==False or vr3_2==False:
                    var7=1
                #si el monstre esta viu la imatge simprimex en la pantalla
                    
            if var7==1:
                if var3_3==True:
                    pantalla.blit(smonster.image,smonster.rect)
    
                    #moviments
                        
                    if var3_3==True and hpmonstruo3>0 and hp_pj>0:
                        variable1_3=random.randrange(0,5)
    
                        
                        
                        if variable1_3==0 or variable1_3==1:
                            if smonster.rect.left<770 and sprite1.rect.left>smonster.rect.left:
                                smonster.rect.left+=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image1
                                if variable1_3==1:
                                    smonster.image=monstruo3image3
                                var_md=1
                        if variable1_3==1 or variable1_3==2:
                            if smonster.rect.top<570 and sprite1.rect.top>smonster.rect.top:
                                smonster.rect.top+=random.randrange(0,25)
                                if var_md==1:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image1
                                    if variable1_3==1:
                                        smonster.image=monstruo3image3
                                if var_md==2:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image2
                                    if variable1_3==1:
                                        smonster.image=monstruo3image4
                        if variable1_3==2 or variable1_3==3:
                            if smonster.rect.top>15 and sprite1.rect.top<smonster.rect.top:
                                smonster.rect.top-=random.randrange(0,25)
                                if var_md==1:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image1
                                    if variable1_3==1:
                                        smonster.image=monstruo3image3
                                if var_md==2:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image2
                                    if variable1_3==1:
                                        smonster.image=monstruo3image4
                                    
                        if variable1==3 or variable1_3==0:
                            if smonster.rect.left>15 and sprite1.rect.left<smonster.rect.left:
                                smonster.rect.left-=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image2
                                if variable1_3==3:
                                    smonster.image=monstruo3image4
                                var_md=2
    
            
    
    
    
                    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
                    var_attackconfirm_l_3=sprite1.rect.left-smonster.rect.left
                    var_attackconfirm_t_3=sprite1.rect.top-smonster.rect.top
    
                #accions que infringeixen dany al monstre (snake)
    
                    if var3_3==True:
                        if spritefoc.rect.colliderect(smonster) and hpmonstruo3>0:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(5,15)
                            if hpmonstruo3<0:
                                hpmonstruo3==0
    
                        if var1==1 and var_attackconfirm_l_3>-20 and var_attackconfirm_l_3<10 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left+10,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
                        if var1==2 and var_attackconfirm_l_3>-10 and var_attackconfirm_l_3<20 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left-10)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
    
    
                    #accions que infringeixen dany al pj (snake)
                                
                    if var3_3==True and smonster.rect.colliderect(sprite1.rect) and hpmonstruo3>0 and hp_pj>0:
                        hp_pj-=random.randrange(0,2)
                        sprite1.rect.left-=random.randrange(-5,5)
                        sprite1.rect.top+=random.randrange(-5,5)
    
                        if var1==1:
                            sprite1.image=goblinhr
                        if var1==2:
                            sprite1.image=goblinhl
    
                    if hpmonstruo3<0:
                        hpmonstruo3==0
    
    
                    hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    textohppj=fuente1.render(hppjt,0,verde)
                    pantalla.blit(textohppj,(5,5))
    
                    #t=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    #textohppj=fuente1.render(hppjt,0,verde)
                    #pantalla.blit(textohppj,(5,5))
    
    
                    #axo serveix perk no senkalli el pj en matar el monstre
                    #if sprite1.rect.colliderect(smonster.rect) and cont6<50 and hpmonstruo3==0:
                     #   sprite1.rect.left+=10
                        
    
                    #vida dels monstres          
                    if var3_3==True:       
                        hpm3=str(str(hpmonstruo3)+'/50')
    
                    #per fer desaparexer el snake un kop mort:
                    
                    if hpmonstruo3<=0 and cont17<70:
                        hpmonstruo3=0
                        cont17+=1
                        if cont17==70:
                            cont17=0
                            var3_3=False
                            smonster.rect.top=9999
                            smonster.rect.left=9999
    
    
                    #imprimacio de la vida dels monstres       
                    if var3_3==True:
                        textohp1=fuente1.render(hpm3,0,rojo)
                        pantalla.blit(textohp1,(smonster.rect.left-10,smonster.rect.top-25))
    
    
                    #sistema k fa k el pj no travessi el monstre
                    if hpmonstruo3==0:
                        if sprite1.rect.colliderect(smonster.rect) and cont6>10 and var_c3==True:
                            sprite1.rect.left=xant
                            sprite1.rect.top=yant
    
                    
    
    
    
    
                    if var3_3==False and cont11==0:
                        cont6=0
                        cont11+=1
    
                    if var3_3==False and cont12==0:
                        cont6=0
                        cont12+=1
    
    
    
            vr3=var3
            vr3_2=var3_2
            vr3_3=var3_3
    
            
    
    
    #si el pop esta mort i sa mort menys de 4 vegades torna a aparexer depen del resultat de f
            if vr3==False and cont19<4:
                    spritemonstruo1=pygame.sprite.Sprite()
                    spritemonstruo1.image=monstruoimage1
                    spritemonstruo1.rect=monstruoimage1.get_rect()
                    spritemonstruo1.rect.top=random.randrange(0,570)
                    spritemonstruo1.rect.left=random.randrange(0,770)
                    if cont19==0 or cont19==1:
                        hpmonstruo1=100
                    else:
                        hpmonstruo1=120
                    cont6=0
                    var3=True
                    cont19+=1
                    cont23=0
            if cont19==4 and var3==False:
                var8=True
                
    #
            if vr3_2==False and cont20<2:
                    sger=pygame.sprite.Sprite()
                    sger.image=monstruo2image1
                    sger.rect=monstruo2image1.get_rect()
                    sger.rect.top=random.randrange(0,570)
                    sger.rect.left=random.randrange(0,770)
                    hpmonstruo2=100
                    cont6=0
                    var3_2=True
                    cont20+=1
                    cont24=0
            if cont20==2 and var3_2==False:
                var8_2=True
    
    
    
            if vr3_3==False and cont21<5:
                    smonster=pygame.sprite.Sprite()
                    smonster.image=monstruo3image1
                    smonster.rect=monstruo3image1.get_rect()
                    smonster.rect.top=random.randrange(0,570)
                    smonster.rect.left=random.randrange(0,770)
                    hpmonstruo3=50
                    cont6=0
                    var3_3=True
                    cont21+=1
                    cont25=0
            if cont21==5 and var3_3==False:
                var8_3=True
    
                
    ####AKI ANIRA LU MATEX K LU DEL POP AM ELS ALTRES 2 MONSTRES
    
    #per k es recargi el mp:
            cont18+=1
            if cont18%10==0 and mppj<mpdatos:
                mppj+=1
        
    #imprimacio del mp:
            mppjt=str('MP: '+str(mppj)+'/'+str(mptpj))
            textomppj=fuente1.render(mppjt,0,verde)
            pantalla.blit(textomppj,(700,5))
    
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
    
    #per guardar la kantitat de diners i desblokejar el seguen nivell si sa completat la misio
            if var9==True:
                money_t=str(money)
                moneywriter=open('log\money.txt','w')
                moneywriter.write(money_t)
                moneywriter.close()
            
                moneyreader=open('log\money.txt')
                money=int(moneyreader.readline())
                moneyreader.close()
    
                if mision==4:
                    misionwriter=open('log\misions.txt','w')
                    misionwriter.write('5')
                    misionwriter.close()
    
            
    
    #per sumar diners al matar els monstres:
            if cont23==0 and hpmonstruo1==0:
                cont23+=1
                money+=random.randrange(15,26)
                print 'dinero:', money
    
            if cont24==0 and hpmonstruo2==0:
                cont24+=1
                money+=random.randrange(35,45)
                print 'dinero:', money
    
            if cont25==0 and hpmonstruo3==0:
                cont25+=1
                money+=random.randrange(12,18)
                print 'dinero:', money
    
                
                
    
            if hp_pj==0:
                money=perdrediners
                
                if contx==0:
                    print 'dinero: ', money
                    contx+=1
    
            tttmoney=str('Dinero: '+str(money))
            textomoney=fuente1.render(tttmoney,0,verde)
            pantalla.blit(textomoney,(200,5))
    
            misionreader=open('log\misions.txt')
            mision=int(misionreader.readline())
            misionreader.close()
    
        
            if sprite1.rect.colliderect(sr1.rect) or sprite1.rect.colliderect(sr2.rect) or sprite1.rect.colliderect(sr3.rect):     
                sprite1.rect.left=xant
                sprite1.rect.top=yant
    
    #prk el pj no surti del mapa:
            if sprite1.rect.left<=0:
                sprite1.rect.left=0
            if sprite1.rect.top<=0:
                sprite1.rect.top=0
            if sprite1.rect.left>=780:
                sprite1.rect.left=780
            if sprite1.rect.top>=550:
                sprite1.rect.top=550
    
    #prk els monstres no chokin am les palmeras:
            if smonster.rect.colliderect(sr1.rect) or smonster.rect.colliderect(sr2.rect) or smonster.rect.colliderect(sr3.rect) and contG>0:
                smonster.rect.left=xmant1
                smonster.rect.top=ymant1
                contE3+=1
            else:
                contE3=0
            if sger.rect.colliderect(sr1.rect) or sger.rect.colliderect(sr2.rect) or sger.rect.colliderect(sr3.rect) and contG>0:
                sger.rect.left=xmant2
                sger.rect.top=ymant2
                contE2+=1
            else:
                contE2=0
            if spritemonstruo1.rect.colliderect(sr1.rect) or spritemonstruo1.rect.colliderect(sr2.rect) or spritemonstruo1.rect.colliderect(sr3.rect) and contG>0:
                spritemonstruo1.rect.left=xmant3
                spritemonstruo1.rect.top=ymant3
                contE1+=1
            else:
                contE1=0
    
            #imprimacio de las rokass
            pantalla.blit(sr1.image,sr1.rect)
            pantalla.blit(sr2.image,sr2.rect)
            pantalla.blit(sr3.image,sr3.rect)
    
            #imprimacio dels arbres
            #pantalla.blit(sa1.image,sa1.rect)
            #pantalla.blit(sa2.image,sa2.rect)
            #pantalla.blit(sa3.image,sa3.rect)
            
    
    #perk el pj no senkalli am els monstres:
            if hpmonstruo1==0 and sprite1.rect.colliderect(spritemonstruo1)==False:
                var_c1=True
            if hpmonstruo2==0 and sprite1.rect.colliderect(sger)==False:
                var_c2=True
            if hpmonstruo3==0 and sprite1.rect.colliderect(smonster)==False:
                var_c3=True
    
            if hpmonstruo1>0:
                var_c1=False
            if hpmonstruo2>0:
                var_c2=False
            if hpmonstruo3>0:
                var_c3=False
    
    #per si el monstre aparex sobre una roka k es mogi per no enkallarse
            #if contE1==2:
             #   smonster.rect.left+=10
            #if contE2==2:
             #   sger.rect.left+=10
            #if contE3==2:
             #   spritemonstruo1.rect.left+=10
    
    #perk kridin els monstres kuan morin:
            if hpmonstruo1==0 and contC1==0:
                sonidocrit1.play()
                contC1+=1
            if hpmonstruo1>0:
                contC1=0
    
            if hpmonstruo2==0 and contC2==0:
                sonidocrit2.play()
                contC2+=1
            if hpmonstruo2>0:
                contC2=0
    
            if hpmonstruo3==0 and contC3==0:
                sonidocrit3.play()
                contC3+=1
            if hpmonstruo3>0:
                contC3=0
    
    #per fer k el gerrer tingi la imatge de atacant:
            if hpmonstruo2>0 and sger.rect.colliderect(sprite1) and var_d2==1:
                if contG%2==0:
                    sger.image=monstruo2image5
    
            if hpmonstruo2>0 and sger.rect.colliderect(sprite1) and var_d2==2:
                if contG%2==0:
                    sger.image=monstruo2image6
    
            
            #textos pocions:
            potionhpt=str('Pociones HP: '+str(potionshp))
            potionmpt=str('Pociones MP: '+str(potionsmp))
            textohpp=fuente1.render(potionhpt,0,verde)
            textompp=fuente1.render(potionmpt,0,verde)
            pantalla.blit(textohpp,(350,5))
            pantalla.blit(textompp,(500,5))
    
    
            if var_escudo==True:
                spritee.rect.top=sprite1.rect.top-15
                spritee.rect.left=sprite1.rect.left-25
            else:
                spritee.rect.top=999999
                spritee.rect.left=999999
    
            if var_escudo==True:
                cont_escudo+=1
            if var_escudo==True and var_potion==False:
                hp_pj=hp_pjant
    
            if cont_escudo==100:
                var_escudo=False
                cont_escudo=0
    
            
            
    
            pantalla.blit(spritee.image,spritee.rect)
            
            #per fer k leskut giri :)
            if var_escudo==True:
                escut_i=pygame.transform.rotate(escut_i, 90)
                spritee.image=escut_i
            
            contG+=1
            
            pygame.display.update()
        pygame.quit()
    
    def guerra5():
        pygame.init()
        pygame.key.set_repeat(20)
        pantalla=pygame.display.set_mode((800,600))
        fondo=pygame.image.load("images/goblinw/fonsboss.png")
        pygame.display.set_caption('GOBLIN W.')
    
        #rectangles dels arbres
        r_a1=pygame.Rect(80,300,10,30)
        r_a2=pygame.Rect(400,200,10,30)
        r_a3=pygame.Rect(700,400,10,30)
    
        #pygame.draw.rect(pantalla,(0,0,0),r_a1)
        #pygame.draw.rect(pantalla,(0,0,0),r_a2)
        #pygame.draw.rect(pantalla,(0,0,0),r_a3)
    
    
        #SONS
        sonido1=pygame.mixer.Sound("sounds/goblinw/Blast.wav")
        sonido2=pygame.mixer.Sound("sounds/goblinw/explosion.wav")
        sonido3=pygame.mixer.Sound("sounds/goblinw/BSO3.wav")
        sonidodead=pygame.mixer.Sound("sounds/goblinw/deadpj.wav")
        sonidoespada=pygame.mixer.Sound("sounds/goblinw/Sspada.wav")
        sonidoespadaF=pygame.mixer.Sound("sounds/goblinw/SspadaF.wav")
        sonidocrit1=pygame.mixer.Sound("sounds/goblinw/critboss1.wav")
        sonidocrit2=pygame.mixer.Sound("sounds/goblinw/crit2.wav")
        sonidocrit3=pygame.mixer.Sound("sounds/goblinw/crit3.wav")
        sonidorun=pygame.mixer.Sound("sounds/goblinw/run.wav")
        sopotion=pygame.mixer.Sound("sounds/goblinw/potion.wav")
        s_terremoto=pygame.mixer.Sound("sounds/goblinw/terremoto.wav")
        s_cofre=pygame.mixer.Sound("sounds/goblinw/cofre1.wav")
        s2_cofre=pygame.mixer.Sound("sounds/goblinw/a_cofre.wav")
        s_sell=pygame.mixer.Sound("sounds/goblinw/sell.wav")
        #sonidocrit3=pygame.mixer.Sound("sounds/goblinw/.wav")
    
        
        #goblin parat
        goblin1=pygame.image.load("images/goblinw/Idle0.png").convert_alpha()
        goblin2=pygame.image.load("images/goblinw/Idle1.png").convert_alpha()
    
        #goblin caminant cap a la dreta
        goblinwr1=pygame.image.load("images/goblinw/Walk0.png").convert_alpha()
        goblinwr2=pygame.image.load("images/goblinw/Walk1.png").convert_alpha()
        goblinwr3=pygame.image.load("images/goblinw/Walk2.png").convert_alpha()
        goblinwr4=pygame.image.load("images/goblinw/Walk3.png").convert_alpha()
    
        #goblin caminant cap a leskerra
        goblinwl1=pygame.image.load("images/goblinw/Walkl0.png").convert_alpha()
        goblinwl2=pygame.image.load("images/goblinw/Walkl1.png").convert_alpha()
        goblinwl3=pygame.image.load("images/goblinw/Walkl2.png").convert_alpha()
        goblinwl4=pygame.image.load("images/goblinw/Walkl3.png").convert_alpha()
    
        #goblin atakant cap a la dreta
        goblinar1=pygame.image.load("images/goblinw/Attack0.png").convert_alpha()
        goblinar2=pygame.image.load("images/goblinw/Attack1.png").convert_alpha()
        goblinar3=pygame.image.load("images/goblinw/Attack2.png").convert_alpha()
    
        #goblin atacant cap a leskerra
        goblinal1=pygame.image.load("images/goblinw/Attackl0.png").convert_alpha()
        goblinal2=pygame.image.load("images/goblinw/Attackl1.png").convert_alpha()
        goblinal3=pygame.image.load("images/goblinw/Attackl2.png").convert_alpha()
    
        #goblin atacant am magia cap a la dreta
        goblinamr=pygame.image.load("images/goblinw/Attackmr.png").convert_alpha()
    
        #goblin atacant am magia kap a leskerra
        goblinaml=pygame.image.load("images/goblinw/Attackml.png").convert_alpha()
    
        #goblin mort 1
        goblindr=pygame.image.load("images/goblinw/Dead0.png").convert_alpha()
    
        #goblin mort 2
        goblindl=pygame.image.load("images/goblinw/Dead1.png").convert_alpha()
    
        #goblin golpejat 1
        goblinhr=pygame.image.load("images/goblinw/Hurt0.png").convert_alpha()
    
        #goblin golpejat 2
        goblinhl=pygame.image.load("images/goblinw/Hurt1.png").convert_alpha()
    
        
        #bola de foc
        foc1=pygame.image.load("images/goblinw/foc.png").convert_alpha()
    
        #monstres
        
        #POP
        monstruoimage1=pygame.image.load("images/goblinw/boss1_4.png").convert_alpha()
        monstruoimage3=pygame.image.load("images/goblinw/boss1_5.png").convert_alpha()
        monstruoimage4=pygame.image.load("images/goblinw/boss1_2.png").convert_alpha()
        monstruoimage5=pygame.image.load("images/goblinw/boss1_3.png").convert_alpha()
        monstruoimage6=pygame.image.load("images/goblinw/boss1.png").convert_alpha()
    
        
    
    
        #imatge eskut
        escut_i=pygame.image.load("images/goblinw/escudo_m.png").convert_alpha()
        
        #imatges cofre
        cofre_i=pygame.image.load("images/goblinw/cofre.png").convert_alpha()
        cofre_i2=pygame.image.load("images/goblinw/cofre2.png").convert_alpha()
        
        #imatges cofre
        pebrot1_i=pygame.image.load("images/goblinw/pebrot1.png").convert_alpha()
        pebrot2_i=pygame.image.load("images/goblinw/pebrot2.png").convert_alpha()
        pebrot3_i=pygame.image.load("images/goblinw/pebrot3.png").convert_alpha()
        pebrot4_i=pygame.image.load("images/goblinw/pebrot4.png").convert_alpha()
        pebrot5_i=pygame.image.load("images/goblinw/pebrot5.png").convert_alpha()
        
    
            
        #sprite del goblin
        sprite1=pygame.sprite.Sprite()
        sprite1.image=goblin1
        sprite1.rect=goblin1.get_rect()
        sprite1.rect.top=100
        sprite1.rect.left=50
    
        #sprite de la bola de foc
        spritefoc=pygame.sprite.Sprite()
        spritefoc.image=foc1
        spritefoc.rect=foc1.get_rect()
        spritefoc.rect.top=9999
        spritefoc.rect.left=9999
    
        #sprite de monstre pop 1
        spritemonstruo1=pygame.sprite.Sprite()
        spritemonstruo1.image=monstruoimage1
        spritemonstruo1.rect=monstruoimage1.get_rect()
        spritemonstruo1.rect.top=random.randrange(0,570)
        spritemonstruo1.rect.left=random.randrange(0,770)
    
    
    
        #sprite de leskut
        spritee=pygame.sprite.Sprite()
        spritee.image=escut_i
        spritee.rect=escut_i.get_rect()
        spritee.rect.top=sprite1.rect.top
        spritee.rect.left=sprite1.rect.left
        
        #sprite del cofre
        spritec=pygame.sprite.Sprite()
        spritec.image=cofre_i
        spritec.rect=cofre_i.get_rect()
        spritec.rect.top=300
        spritec.rect.left=350
        
        #sprite del pebrot
        spritep=pygame.sprite.Sprite()
        spritep.image=pebrot1_i
        spritep.rect=pebrot1_i.get_rect()
        spritep.rect.top=sprite1.rect.top
        spritep.rect.left=sprite1.rect.left
    
        
        
    
        #fuentes
        fuente1=pygame.font.SysFont("Arial",16,True,False)
        fuentevidapj=pygame.font.SysFont("Arial",25,True,False)
        fuenteGO=pygame.font.SysFont("Arial",70,True,False)
    
        
    
        #colors:
        rojo=(255,0,0)
        azul=(0,0,255)
        verde=(0,255,0)
        blanco=(255,255,255)
        negro=(0,0,0)
    
        #textos constants
        textoGO=fuenteGO.render('GAME OVER',0,rojo)
        textoV=fuenteGO.render('NIVEL COMPLETADO',0,azul)
    
        #altres variables i contadors
        cont5=0
        cont4=0
        cont3=0
        cont1=0
        cont2=0
        cont6=0
        cont11=0
        cont12=0
        cont13=0
        cont15=0
        cont16=0
        cont17=0
        cont18=0
        cont19=0
        cont20=0
        cont21=0
        cont22=0
        contx=0
        cont23=0
        cont24=0
        cont25=0
        contG=0
        contE1=0
        contE2=0
        contE3=0
        contC1=0
        contC2=0
        contC3=0
        cont_escudo=0
        cont_terremoto=0
        cont_boss=0
        cont_cofre=0
        #########
        var1=1
        var2=0
        var3=True  #<---variable per saber si el monstre esta viu
        var3_2=True #<---variable per saber si el monstre 2 esta viu
        var3_3=True #<---variable per saber si el monster 3 esta viu
        var4=0
        vr3=var3
        vr3_2=var3_2
        vr3_3=var3_3
        var7=0
        var8=False # variable k indica si san matat prous pops per finalitzar el nivell
        var8_2=False
        var8_3=False
        var9=False
        var_c1=True
        var_c2=True
        var_c3=True
        var_d2=1
        var_md=1#direccio guerrer drago
        var_escudo=False
        var_potion=False
        var_terremoto=False
        var_pebrot=True
        var_cofre=False
        var_cofre2=False
        
        k2=0
    
        #variables per saber si sesta atacant o si sa tirat magia
        var_attack=False
        var_magia=False
    
        #vida monstres i pj
        hpmonstruo1=2000
    
    
        #per llegir les pocions
        potionsreader=open('log\potions.txt')
        potionshp=int(potionsreader.readlines()[0])
        print 'potions hp: ', potionshp
        potionsreader.close()
        
        potionsreader=open('log\potions.txt')
        potionsmp=int(potionsreader.readlines()[1])
        print 'potions mp: ', potionsmp
        potionsreader.close()
    
        
    
    #per llegir el hp del pj:
        datosreader=open('log\datos.txt')
        hpdatos=int(datosreader.readlines()[0])
        print 'hp: ', hpdatos
        datosreader.close()
    
        hp_pj=hpdatos
        hpt_pj=hp_pj
    
        #variable del bucle principal
        salir=False
    
        #reloj
        reloj1=pygame.time.Clock()
    
    
    
    
    
    
    
    
    #escudo i atak terratremol
        tendareader=open('log/shop.txt')
        escudo=int(tendareader.readlines()[0])
        tendareader.close()
        print 'escudo', escudo
        
        tendareader=open('log/shop.txt')
        terremoto=int(tendareader.readlines()[1])
        tendareader.close()
        print 'terremoto', terremoto
    
    
    
    
    
    
    
    #per llegir el mp del pj:
    
        datosreader=open('log\datos.txt')
        mpdatos=int(datosreader.readlines()[1])
        print 'mp: ', mpdatos
        datosreader.close()
        
        #mp del pj
        mptpj=mpdatos
        mppj=mptpj
    
    ######
        #variable diners
        moneyreader=open('log\money.txt')
        money=int(moneyreader.readline())
        print 'dinero:', money
        moneyreader.close()
    
        money_t=str(money)
        moneywriter=open('log\money.txt','w')
        moneywriter.write(money_t)
        moneywriter.close()
    
        perdrediners=money
        
        xant=sprite1.rect.left
        yant=sprite1.rect.top
        
    
        sonido3.play()
    
    #######################################################################################################
        while salir != True:
                        
            var_potion=False
            
            hp_pjant=hp_pj
    
            if hp_pj<=0 and var1==1:
                sprite1.image=goblindr
    
            if hp_pj<=0 and var1==2:
                sprite1.image=goblindl
                
            if sprite1.rect.colliderect(spritemonstruo1.rect)==False:
                xant=sprite1.rect.left
                yant=sprite1.rect.top
    
            if hpmonstruo1<0:
                hpmonstruo1==0
            
            if hpmonstruo1==0:
                spritemonstruo1.image=monstruoimage3
    
    
    
            if hp_pj<0:
                hp_pj=0
                
    
    
            xmant3=spritemonstruo1.rect.left
            ymant3=spritemonstruo1.rect.top
            
    
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN and hp_pj>0:
    
                    if event.key==pygame.K_LEFT and sprite1.rect.left>0:
                        if cont1==0:
                            sprite1.image=goblinwl1
                        if cont1==1:
                            sprite1.image=goblinwl2
                        if cont1==2:
                            sprite1.image=goblinwl3
                        if cont1==3:
                            sprite1.image=goblinwl4
                        if cont1==4:
                            sprite1.image=goblinwl3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left-=6
                        cont1+=1
                        var1=2
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
                        
    
                    if event.key==pygame.K_RIGHT and sprite1.rect.left<775:
                        if cont1==0:
                            sprite1.image=goblinwr1
                        if cont1==1:
                            sprite1.image=goblinwr2
                        if cont1==2:
                            sprite1.image=goblinwr3
                        if cont1==3:
                            sprite1.image=goblinwr4
                        if cont1==4:
                            sprite1.image=goblinwr3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left+=6
                        cont1+=1
                        var1=1
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_UP and sprite1.rect.top>0:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
                            
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top-=6
                        cont1+=1
                        var4=1
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_DOWN and sprite1.rect.top<555:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top+=6
                        cont1+=1
                        var4=2
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_SPACE:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinar2
                            if cont1==1:
                                sprite1.image=goblinar1
                            if cont1==2:
                                sprite1.image=goblinar1
                            if cont1==3:
                                sprite1.image=goblinar2
                            if cont1==4:
                                sprite1.image=goblinar3
                            if cont1>=5:
                                cont1=0
                                sprite1.image=goblinar2
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinal2
                            if cont1==1:
                                sprite1.image=goblinal1
                            if cont1==2:
                                sprite1.image=goblinal2
                            if cont1==3:
                                sprite1.image=goblinal3
                            if cont1>=4:
                                cont1=0
                                sprite1.image=goblinal2
                                
                        cont1+=1
                        var_attack=True
                        if cont1%2==0:
                            sonidoespadaF.play()
    
                        
                            
    
                        
                    if event.key==pygame.K_m:
                        if cont2<=3:
                            if var1==1:
                                sprite1.image=goblinamr
                            if var1==2:
                                sprite1.image=goblinaml
                        if cont2==4:
                            if var1==1:
                                sprite1.image=goblin1
                            if var1==2:
                                sprite1.image=goblin2
                        if cont2==1 and mppj>=20:
                            var_magia=True
                        cont2+=1
    
    
                    if event.key==pygame.K_h and potionshp>0 and hp_pj>0:
                        if hp_pj<hpt_pj:
                            potionshp-=1
                            hp_pj+=random.randrange(15,20)
                            sopotion.play()
                            print 'potionshp: ', potionshp
                            var_potion=True
                            
                            if hp_pj>hpt_pj:
                                hp_pj=hpt_pj
    
                    if event.key==pygame.K_j and potionsmp>0 and hp_pj>0:
                        if mppj<mptpj:
                            potionsmp-=1
                            mppj+=random.randrange(10,20)
                            sopotion.play()
                            print 'potionsmp: ', potionsmp
                            
                            if mppj>mptpj:
                                mppj=mptpj
    
                    if event.key==pygame.K_n and escudo==1 and hp_pj>0 and mppj>=60:
                        mppj-=60
                        var_escudo=True
                        print 'escudo activado'
                    
                    if event.key==pygame.K_b and terremoto==1 and hp_pj>0 and mppj>=250 and var_terremoto==False:
                        mppj-=250
                        var_terremoto=True
                        print 'terremoto activado'
                    
                    #truko per matar al boss klikan (2,7,4) :)
                    if event.key==pygame.K_2:
                        k2=2
                    if event.key==pygame.K_4:
                        if k2==7:
                            k2=4
                        else:
                            k2=0
                    if event.key==pygame.K_7:
                        if k2==2:
                            k2=7
                        else:
                            k2=0
                    
                    
                    
                        
                        
    
                    if event.key==pygame.K_ESCAPE:
                        sonido3.stop()
                        menu1()
                            
                            
                    
                if event.type==pygame.KEYUP and hp_pj>0:
                    if var1==1:
                        sprite1.image=goblin1
                    if var1==2:
                        sprite1.image=goblin2
                        
                    var_attack=False
                    cont2=0
                    cont1=0
                    
                    
    
            reloj1.tick(17)
            
            
            
            
            pantalla.blit(fondo,(0,0))
            
            if var_terremoto==True:
                if var3==True:
                    hpmonstruo1-=35
                s_terremoto.play()
                cont_terremoto+=1
                if cont_terremoto%2==0:
                    pantalla.blit(fondo,(random.randrange(0,5),random.randrange(0,5)))
                else:
                    pantalla.blit(fondo,(0,0))
            if cont_terremoto==10:
                var_terremoto=False
                cont_terremoto=0
    
            pantalla.blit(sprite1.image,sprite1.rect)
    
            
            #imprimacio pebrot
            pantalla.blit(spritep.image,spritep.rect)
            
            if var3==True:
                pantalla.blit(spritemonstruo1.image,spritemonstruo1.rect)
    
    
    
            
            
            #MOVIMENTS DEL MONSTRE 1 (pop)
                
            if var3==True and hpmonstruo1>0 and hp_pj>0:
                
                if hpmonstruo1>750:
                    variable1=random.randrange(0,5)
        
        
                    if variable1==0 or variable1==1:
                        if spritemonstruo1.rect.left<770 and sprite1.rect.left>spritemonstruo1.rect.left:
                            spritemonstruo1.rect.left+=random.randrange(0,12)
                            spritemonstruo1.image=monstruoimage5
                    if variable1==1 or variable1==2:
                        if spritemonstruo1.rect.top<570 and sprite1.rect.top>spritemonstruo1.rect.top:
                            spritemonstruo1.rect.top+=random.randrange(0,12)
                            spritemonstruo1.image=monstruoimage1
                    if variable1==2 or variable1==3:
                        if spritemonstruo1.rect.top>15 and sprite1.rect.top<spritemonstruo1.rect.top:
                            spritemonstruo1.rect.top-=random.randrange(0,12)
                            spritemonstruo1.image=monstruoimage6
                    if variable1==3 or variable1==0:
                        if spritemonstruo1.rect.left>15 and sprite1.rect.left<spritemonstruo1.rect.left:
                            spritemonstruo1.rect.left-=random.randrange(0,12)
                            spritemonstruo1.image=monstruoimage4
                else:
                    variable1=random.randrange(0,5)
        
        
                    if variable1==0 or variable1==1:
                        if spritemonstruo1.rect.left<770 and sprite1.rect.left>spritemonstruo1.rect.left:
                            spritemonstruo1.rect.left+=random.randrange(0,15)
                            spritemonstruo1.image=monstruoimage5
                    if variable1==1 or variable1==2:
                        if spritemonstruo1.rect.top<570 and sprite1.rect.top>spritemonstruo1.rect.top:
                            spritemonstruo1.rect.top+=random.randrange(0,15)
                            spritemonstruo1.image=monstruoimage1
                    if variable1==2 or variable1==3:
                        if spritemonstruo1.rect.top>15 and sprite1.rect.top<spritemonstruo1.rect.top:
                            spritemonstruo1.rect.top-=random.randrange(0,15)
                            spritemonstruo1.image=monstruoimage6
                    if variable1==3 or variable1==0:
                        if spritemonstruo1.rect.left>15 and sprite1.rect.left<spritemonstruo1.rect.left:
                            spritemonstruo1.rect.left-=random.randrange(0,15)
                            spritemonstruo1.image=monstruoimage4
                        
                
            #Invocacio pebrot
            if contG%20==0 and hp_pj>0 and hpmonstruo1>0:
                spritep.rect.left=spritemonstruo1.rect.left+40
                spritep.rect.top=spritemonstruo1.rect.top+40
                dirp=random.randrange(0,4)
                var_pebrot=True
            
            #moviments pebrot
            if var_pebrot==True:
                if dirp==0:
                    spritep.image=pebrot2_i
                    spritep.rect.left+=10
                if dirp==1:
                    spritep.image=pebrot1_i
                    spritep.rect.left-=10
                if dirp==2:
                    spritep.image=pebrot4_i
                    spritep.rect.top+=10
                if dirp==3:
                    spritep.image=pebrot3_i
                    spritep.rect.top-=10
                
            
            
                
                
            
            
                        
                        
            #"INVOCACIO" BOLA DE FOC
                        
            if var_magia==True and cont5==0 and mppj>20:
                #sprite de la bola de foc
                spritefoc=pygame.sprite.Sprite()
                spritefoc.image=foc1
                spritefoc.rect=foc1.get_rect()
                if var4==0:
                    spritefoc.rect.top=sprite1.rect.top+5
                if var4==1 or var4==2:
                    spritefoc.rect.left=sprite1.rect.left+5
    
                if var1==1 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left+20
                if var1==2 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left-20
                if var4==1:
                    spritefoc.rect.top=sprite1.rect.top-20
                if var4==2:
                    spritefoc.rect.top=sprite1.rect.top+20
    
                mppj-=20
                sonido2.play()
                cont5+=1
    
            #MOVIMENTS BOLA DE FOC
            if var_magia==True:
                pantalla.blit(spritefoc.image,spritefoc.rect)
                if cont3==0:
                    cont3+=1
                    if var1==1 and var4==0:
                        var2=1
                    if var1==2 and var4==0:
                        var2=2
                    if var4==1:
                        var2=3
                    if var4==2:
                        var2=4
    
                if cont3>0 and cont4<70:
                    if var2==1:
                        spritefoc.rect.left+=10
                    if var2==2:
                        spritefoc.rect.left-=10
                    if var2==3:
                        spritefoc.rect.top-=10
                    if var2==4:
                        spritefoc.rect.top+=10
                    cont4+=2
    
            if spritefoc.rect.left<0 or spritefoc.rect.left>800 or spritefoc.rect.top>600 or spritefoc.rect.top<0 or cont4>=70:
                var_magia=False
                
            if var_magia==False:
                cont3=0
                cont4=0
                cont5=0
                spritefoc.rect.top=99999
                spritefoc.rect.left=99999
    
    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
            var_attackconfirm_l=sprite1.rect.left-spritemonstruo1.rect.left
            var_attackconfirm_t=sprite1.rect.top-spritemonstruo1.rect.top
    
    
    #accions que infringeixen dany al monstre (pop gegant)
            
            if var3==True:
                if spritefoc.rect.colliderect(spritemonstruo1) and hpmonstruo1>0:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(5,15)
                    if hpmonstruo1<0:
                        hpmonstruo1==0
            
                if var1==1 and var_attackconfirm_l>-35 and var_attackconfirm_l<110 and var_attackconfirm_t>-50 and var_attackconfirm_t<110 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left+10,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
                if var1==2 and var_attackconfirm_l>-35 and var_attackconfirm_l<110 and var_attackconfirm_t>-50 and var_attackconfirm_t<110 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left-10)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
    
    
    
    
    #accions que infringeixen dany al pj (pop)
                        
            if var3==True and spritemonstruo1.rect.colliderect(sprite1.rect) and hpmonstruo1>0 and hp_pj>0:
                spritemonstruo1.rect.left=xmant3
                spritemonstruo1.rect.top=ymant3
                hp_pj-=random.randrange(0,10)
                sprite1.rect.left-=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo1<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
    
    
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
            
    
            
    #vida dels monstres          
            if var3==True:  
                    hpm1=str(str(hpmonstruo1)+'/2000')
    
         
    
    #per fer desaparexer el pop un kop mort:
            if hpmonstruo1<=0 and cont6<70:
                hpmonstruo1=0
                cont6+=1
                if cont6==70:
                    cont6=0
                    var3=False
                    spritemonstruo1.rect.top=9999
                    spritemonstruo1.rect.left=9999
    
    
    
    
    #imprimacio de la vida dels monstres
            #pop       
            if var3==True:
                textohp1=fuente1.render(hpm1,0,rojo)
                pantalla.blit(textohp1,(spritemonstruo1.rect.left-10,spritemonstruo1.rect.top-25))
    
    
    
    
    #sistema k fa k el pj no travessi el monstre
            if hpmonstruo1==0:
                if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6>10 and var_c1==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
            if var3==False and cont11==0:
                cont6=0
                cont11+=1
    
            if var3==False and cont12==0:
                cont6=0
                cont12+=1
    
            if hp_pj==0:
                cont13+=1
    
            if cont13==50:
                sonido3.stop()
                menu1()
    
            if hp_pj<=0:
                pantalla.blit(textoGO,(200,200))
                if cont13==1:
                    sonidodead.play()
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                elif cont13==20:
                    sonidodead.stop()
                
    
    #per saber si sa akabat el nivell:
            if var8==True and hp_pj>0:
                if mision==5:
                    var_cofre2=True
                    sonido3.stop()
                
                if mision==5:
                    if var_cofre==True and cont_cofre>=10:
                        pantalla.blit(textoV,(115,200))
                        cont16+=1
                        var9=True
                        if cont16==60:
                            datoswriter=open('log/potions.txt','w')
                            datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                            datoswriter.close()
                            menu1()
                else:
                    pantalla.blit(textoV,(115,200))
                    cont16+=1
                    var9=True
                    if cont16==60:
                        datoswriter=open('log/potions.txt','w')
                        datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                        datoswriter.close()
                        sonido3.stop()
                        s_cofre.stop()
                        menu1()
                    
            
            
            if var_cofre==True:
                cont_cofre+=1
                
            if var_cofre2==True:
                s_cofre.play()
                pantalla.blit(spritec.image,spritec.rect)
                if sprite1.rect.colliderect(spritec.rect):
                    spritec.image=cofre_i2
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
                    var_cofre=True
                    if cont_cofre==0 and mision==5:
                        money+=1500
                        s_cofre.stop()
                        s2_cofre.play()
                        s_sell.play()
                        
                
    
    
    
            vr3=var3
    
            
    
    
            if var3==False:
                var8=True
    
    
    
    #per k es recargi el mp:
            cont18+=1
            if cont18%10==0 and mppj<mpdatos:
                mppj+=1
        
    #imprimacio del mp:
            mppjt=str('MP: '+str(mppj)+'/'+str(mptpj))
            textomppj=fuente1.render(mppjt,0,verde)
            pantalla.blit(textomppj,(700,5))
    
            
    
    
    #per guardar la kantitat de diners i desblokejar el seguen nivell si sa completat la misio
            if var9==True:
                money_t=str(money)
                moneywriter=open('log\money.txt','w')
                moneywriter.write(money_t)
                moneywriter.close()
            
                moneyreader=open('log\money.txt')
                money=int(moneyreader.readline())
                moneyreader.close()
    
                if mision==5:
                    misionwriter=open('log\misions.txt','w')
                    misionwriter.write('6')
                    misionwriter.close()
    
            
    
    #per sumar diners al matar els monstres:
            if cont23==0 and hpmonstruo1==0:
                cont23+=1
                money+=300
                print 'dinero:', money
    
    
    
                
                
    
            if hp_pj==0:
                money=perdrediners
                
                if contx==0:
                    print 'dinero: ', money
                    contx+=1
    
            tttmoney=str('Dinero: '+str(money))
            textomoney=fuente1.render(tttmoney,0,verde)
            pantalla.blit(textomoney,(200,5))
    
            misionreader=open('log\misions.txt')
            mision=int(misionreader.readline())
            misionreader.close()
    
        
    
    #prk el pj no surti del mapa:
            if sprite1.rect.left<=0:
                sprite1.rect.left=0
            if sprite1.rect.top<=0:
                sprite1.rect.top=0
            if sprite1.rect.left>=780:
                sprite1.rect.left=780
            if sprite1.rect.top>=550:
                sprite1.rect.top=550
    
    
    
    
            
            
    
    #perk el pj no senkalli am els monstres:
            if hpmonstruo1==0 and sprite1.rect.colliderect(spritemonstruo1)==False:
                var_c1=True
                
    
            if hpmonstruo1>0:
                var_c1=False
    
    
    #per si el monstre aparex sobre una roka k es mogi per no enkallarse
            if contE1==2:
                smonster.rect.left+=10
            
    
    #perk kridin els monstres kuan morin:
            if hpmonstruo1==0 and contC1==0:
                sonidocrit1.play()
                contC1+=1
            if hpmonstruo1>0:
                contC1=0
    
    
    
            
            #textos pocions:
            potionhpt=str('Pociones HP: '+str(potionshp))
            potionmpt=str('Pociones MP: '+str(potionsmp))
            textohpp=fuente1.render(potionhpt,0,verde)
            textompp=fuente1.render(potionmpt,0,verde)
            pantalla.blit(textohpp,(350,5))
            pantalla.blit(textompp,(500,5))
    
    
            if var_escudo==True:
                spritee.rect.top=sprite1.rect.top-15
                spritee.rect.left=sprite1.rect.left-25
            else:
                spritee.rect.top=999999
                spritee.rect.left=999999
    
            if var_escudo==True:
                cont_escudo+=1
            
    
            if cont_escudo==100:
                var_escudo=False
                cont_escudo=0
    
            
            if spritemonstruo1.rect.colliderect(sprite1.rect):
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
                    #spritemonstruo1.rect.left
            
            pantalla.blit(spritee.image,spritee.rect)
            
            #per fer k leskut giri :)
            if var_escudo==True:
                escut_i=pygame.transform.rotate(escut_i, 90)
                spritee.image=escut_i
            
            #dany del pebrot al pj:
            if sprite1.rect.colliderect(spritep.rect):
                spritep.image=pebrot5_i
                var_pebrot=False
                hp_pj-=25
        
        
            #per destruir pebrots (li e dafegir un so kuan chokin perk kedi millor
            if spritefoc.rect.colliderect(spritep.rect):
                spritep.rect.left=999999
            
            
            
            
            if var_escudo==True and var_potion==False:
                hp_pj=hp_pjant
            
            if k2==4:
                hpmonstruo1=0
            
                
            contG+=1
            
            pygame.display.update()
        pygame.quit()
           
    def guerra6():
        pygame.init()
        pygame.key.set_repeat(20)
        pantalla=pygame.display.set_mode((800,600))
        fondo=pygame.image.load("images/goblinw/fons5.png")
        pygame.display.set_caption('GOBLIN W.')
    
        #rectangles dels arbres
        r_a1=pygame.Rect(80,300,10,30)
        r_a2=pygame.Rect(400,200,10,30)
        r_a3=pygame.Rect(700,400,10,30)
    
        #pygame.draw.rect(pantalla,(0,0,0),r_a1)
        #pygame.draw.rect(pantalla,(0,0,0),r_a2)
        #pygame.draw.rect(pantalla,(0,0,0),r_a3)
    
    
        #SONS
        sonido1=pygame.mixer.Sound("sounds/goblinw/Blast.wav")
        sonido2=pygame.mixer.Sound("sounds/goblinw/explosion.wav")
        sonido3=pygame.mixer.Sound("sounds/goblinw/BSO6.wav")
        sonidodead=pygame.mixer.Sound("sounds/goblinw/deadpj.wav")
        sonidoespada=pygame.mixer.Sound("sounds/goblinw/Sspada.wav")
        sonidoespadaF=pygame.mixer.Sound("sounds/goblinw/SspadaF.wav")
        sonidocrit1=pygame.mixer.Sound("sounds/goblinw/crit1.wav")
        sonidocrit2=pygame.mixer.Sound("sounds/goblinw/crit2.wav")
        sonidocrit3=pygame.mixer.Sound("sounds/goblinw/crit3.wav")
        sonidorun=pygame.mixer.Sound("sounds/goblinw/run.wav")
        sopotion=pygame.mixer.Sound("sounds/goblinw/potion.wav")
        s_terremoto=pygame.mixer.Sound("sounds/goblinw/terremoto.wav")
        #sonidocrit3=pygame.mixer.Sound("sounds/goblinw/.wav")
        s_cremada = pygame.mixer.Sound("sounds/goblinw/cremada.wav")
    
        
        #goblin parat
        goblin1=pygame.image.load("images/goblinw/Idle0.png").convert_alpha()
        goblin2=pygame.image.load("images/goblinw/Idle1.png").convert_alpha()
    
        #goblin caminant cap a la dreta
        goblinwr1=pygame.image.load("images/goblinw/Walk0.png").convert_alpha()
        goblinwr2=pygame.image.load("images/goblinw/Walk1.png").convert_alpha()
        goblinwr3=pygame.image.load("images/goblinw/Walk2.png").convert_alpha()
        goblinwr4=pygame.image.load("images/goblinw/Walk3.png").convert_alpha()
    
        #goblin caminant cap a leskerra
        goblinwl1=pygame.image.load("images/goblinw/Walkl0.png").convert_alpha()
        goblinwl2=pygame.image.load("images/goblinw/Walkl1.png").convert_alpha()
        goblinwl3=pygame.image.load("images/goblinw/Walkl2.png").convert_alpha()
        goblinwl4=pygame.image.load("images/goblinw/Walkl3.png").convert_alpha()
    
        #goblin atakant cap a la dreta
        goblinar1=pygame.image.load("images/goblinw/Attack0.png").convert_alpha()
        goblinar2=pygame.image.load("images/goblinw/Attack1.png").convert_alpha()
        goblinar3=pygame.image.load("images/goblinw/Attack2.png").convert_alpha()
    
        #goblin atacant cap a leskerra
        goblinal1=pygame.image.load("images/goblinw/Attackl0.png").convert_alpha()
        goblinal2=pygame.image.load("images/goblinw/Attackl1.png").convert_alpha()
        goblinal3=pygame.image.load("images/goblinw/Attackl2.png").convert_alpha()
    
        #goblin atacant am magia cap a la dreta
        goblinamr=pygame.image.load("images/goblinw/Attackmr.png").convert_alpha()
    
        #goblin atacant am magia kap a leskerra
        goblinaml=pygame.image.load("images/goblinw/Attackml.png").convert_alpha()
    
        #goblin mort 1
        goblindr=pygame.image.load("images/goblinw/Dead0.png").convert_alpha()
    
        #goblin mort 2
        goblindl=pygame.image.load("images/goblinw/Dead1.png").convert_alpha()
    
        #goblin golpejat 1
        goblinhr=pygame.image.load("images/goblinw/Hurt0.png").convert_alpha()
    
        #goblin golpejat 2
        goblinhl=pygame.image.load("images/goblinw/Hurt1.png").convert_alpha()
    
        
        #bola de foc
        foc1=pygame.image.load("images/goblinw/foc.png").convert_alpha()
    
        #monstres
        
        #POP
        monstruoimage1=pygame.image.load("images/goblinw/monstruo2.png").convert_alpha()
        monstruoimage3=pygame.image.load("images/goblinw/monstruo2_3.png").convert_alpha()
        monstruoimage4=pygame.image.load("images/goblinw/monstruo2_4.png").convert_alpha()
        monstruoimage5=pygame.image.load("images/goblinw/monstruo2_5.png").convert_alpha()
        monstruoimage6=pygame.image.load("images/goblinw/monstruo2_6.png").convert_alpha()
    
        #GUERRER DAURAT
        monstruo2image1=pygame.image.load("images/goblinw/guerrero2.png").convert_alpha()
        monstruo2image2=pygame.image.load("images/goblinw/guerrero2_2.png").convert_alpha()
        monstruo2image3=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
        monstruo2image4=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
        monstruo2image5=pygame.image.load("images/goblinw/guerrero2_5.png").convert_alpha()
        monstruo2image6=pygame.image.load("images/goblinw/guerrero2_6.png").convert_alpha()
        monstruo2image7=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
        monstruo2image8=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
        monstruo2image9=pygame.image.load("images/goblinw/guerrero2_7.png").convert_alpha()
        
    
        #monstre 3 (sNakE)
        monstruo3image1=pygame.image.load("images/goblinw/guerrero3.png").convert_alpha()
        monstruo3image2=pygame.image.load("images/goblinw/guerrero3_2.png").convert_alpha()
        monstruo3image3=pygame.image.load("images/goblinw/guerrero3_3.png").convert_alpha()
        monstruo3image4=pygame.image.load("images/goblinw/guerrero3_4.png").convert_alpha()
        monstruo3image5=pygame.image.load("images/goblinw/guerrero3_5.png").convert_alpha()
        monstruo3image6=pygame.image.load("images/goblinw/guerrero3_6.png").convert_alpha()
        monstruo3image7=pygame.image.load("images/goblinw/guerrero3_7.png").convert_alpha()
        monstruo3image8=pygame.image.load("images/goblinw/guerrero3_8.png").convert_alpha()
        monstruo3image9=pygame.image.load("images/goblinw/guerrero3_9.png").convert_alpha()
        monstruo3image10=pygame.image.load("images/goblinw/guerrero3_9.png").convert_alpha()
        monstruo3image11=pygame.image.load("images/goblinw/guerrero3_9.png").convert_alpha()
    
        #imatges dels arbres
        tree1image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree2image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree3image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
    
        #imatges de las rokas
        rock1image=pygame.image.load("images/goblinw/lava.png").convert_alpha()
        rock2image=pygame.image.load("images/goblinw/lava2.png").convert_alpha()
    
    
        #imatge eskut
        escut_i=pygame.image.load("images/goblinw/escudo_m.png").convert_alpha()
    
            
        #sprite del goblin
        sprite1=pygame.sprite.Sprite()
        sprite1.image=goblin1
        sprite1.rect=goblin1.get_rect()
        sprite1.rect.top=100
        sprite1.rect.left=50
    
        #sprite de la bola de foc
        spritefoc=pygame.sprite.Sprite()
        spritefoc.image=foc1
        spritefoc.rect=foc1.get_rect()
        spritefoc.rect.top=9999
        spritefoc.rect.left=9999
    
        #sprite de monstre pop 1
        spritemonstruo1=pygame.sprite.Sprite()
        spritemonstruo1.image=monstruoimage1
        spritemonstruo1.rect=monstruoimage1.get_rect()
        spritemonstruo1.rect.top=random.randrange(0,570)
        spritemonstruo1.rect.left=random.randrange(0,770)
    
        #sprite de monstre guerrer 2
        sger=pygame.sprite.Sprite()
        sger.image=monstruo2image1
        sger.rect=monstruo2image1.get_rect()
        sger.rect.top=random.randrange(0,570)
        sger.rect.left=random.randrange(0,770)
    
        #sprite del snake 3
        smonster=pygame.sprite.Sprite()
        smonster.image=monstruo3image1
        smonster.rect=monstruo3image1.get_rect()
        smonster.rect.top=random.randrange(0,570)
        smonster.rect.left=random.randrange(0,770)
    
        #sprite de leskut
        spritee=pygame.sprite.Sprite()
        spritee.image=escut_i
        spritee.rect=escut_i.get_rect()
        spritee.rect.top=sprite1.rect.top
        spritee.rect.left=sprite1.rect.left
    
        #sprites de las rokas
        #1
        sr1=pygame.sprite.Sprite()
        sr1.image=rock1image
        sr1.rect=rock1image.get_rect()
        sr1.rect.top=280
        sr1.rect.left=60
        #2
        sr2=pygame.sprite.Sprite()
        sr2.image=rock2image
        sr2.rect=rock2image.get_rect()
        sr2.rect.top=70
        sr2.rect.left=400
        #3
        sr3=pygame.sprite.Sprite()
        sr3.image=rock2image
        sr3.rect=rock2image.get_rect()
        sr3.rect.top=350
        sr3.rect.left=500
        
    
        #arbres k no utilitzu xd
        sa1=pygame.sprite.Sprite()
        sa1.image=tree1image
        sa1.rect=tree1image.get_rect()
        sa1.rect.top=280
        sa1.rect.left=60
    
        sa2=pygame.sprite.Sprite()
        sa2.image=tree1image
        sa2.rect=tree1image.get_rect()
        sa2.rect.top=95
        sa2.rect.left=372
    
        sa3=pygame.sprite.Sprite()
        sa3.image=tree1image
        sa3.rect=tree1image.get_rect()
        sa3.rect.top=350
        sa3.rect.left=677
    
        #r_a1=pygame.Rect(87,320,10,30)
        #r_a2=pygame.Rect(400,135,10,30)
        #r_a3=pygame.Rect(705,392,10,30)
        
    
        #fuentes
        fuente1=pygame.font.SysFont("Arial",16,True,False)
        fuentevidapj=pygame.font.SysFont("Arial",25,True,False)
        fuenteGO=pygame.font.SysFont("Arial",70,True,False)
    
        
    
        #colors:
        rojo=(255,0,0)
        azul=(0,0,255)
        verde=(0,255,0)
        blanco=(255,255,255)
        negro=(0,0,0)
    
        #textos constants
        textoGO=fuenteGO.render('GAME OVER',0,rojo)
        textoV=fuenteGO.render('NIVEL COMPLETADO',0,azul)
    
        #altres variables i contadors
        cont5=0
        cont4=0
        cont3=0
        cont1=0
        cont2=0
        cont6=0
        cont11=0
        cont12=0
        cont13=0
        cont15=0
        cont16=0
        cont17=0
        cont18=0
        cont19=0
        cont20=0
        cont21=0
        cont22=0
        contx=0
        cont23=0
        cont24=0
        cont25=0
        contG=0
        contE1=0
        contE2=0
        contE3=0
        contC1=0
        contC2=0
        contC3=0
        cont_escudo=0
        cont_terremoto=0
        #########
        var1=1
        var2=0
        var3=True  #<---variable per saber si el monstre esta viu
        var3_2=True #<---variable per saber si el monstre 2 esta viu
        var3_3=True #<---variable per saber si el monster 3 esta viu
        var4=0
        vr3=var3
        vr3_2=var3_2
        vr3_3=var3_3
        var7=0
        var8=False # variable k indica si san matat prous pops per finalitzar el nivell
        var8_2=False
        var8_3=False
        var9=False
        var_c1=True
        var_c2=True
        var_c3=True
        var_d2=1
        var_md=1#direccio guerrer drago
        var_escudo=False
        var_potion=False
        var_terremoto=False
    
        #variables per saber si sesta atacant o si sa tirat magia
        var_attack=False
        var_magia=False
    
        #vida monstres i pj
        hpmonstruo1=100
        hpmonstruo2=100
        hpmonstruo3=50
    
    
        #per llegir les pocions
        potionsreader=open('log\potions.txt')
        potionshp=int(potionsreader.readlines()[0])
        print 'potions hp: ', potionshp
        potionsreader.close()
        
        potionsreader=open('log\potions.txt')
        potionsmp=int(potionsreader.readlines()[1])
        print 'potions mp: ', potionsmp
        potionsreader.close()
    
        
    
    #per llegir el hp del pj:
        datosreader=open('log\datos.txt')
        hpdatos=int(datosreader.readlines()[0])
        print 'hp: ', hpdatos
        datosreader.close()
    
        hp_pj=hpdatos
        hpt_pj=hp_pj
    
        #variable del bucle principal
        salir=False
    
        #reloj
        reloj1=pygame.time.Clock()
    
        #grup de sprites de monstres
        grupo_m=pygame.sprite.Group(spritemonstruo1,sger,smonster)
    
    
    
    
    
    
    
    #escudo i atak terratremol
        tendareader=open('log/shop.txt')
        escudo=int(tendareader.readlines()[0])
        tendareader.close()
        print 'escudo', escudo
        
        tendareader=open('log/shop.txt')
        terremoto=int(tendareader.readlines()[1])
        tendareader.close()
        print 'terremoto', terremoto
    
    
    
    
    
    
    
    #per llegir el mp del pj:
    
        datosreader=open('log\datos.txt')
        mpdatos=int(datosreader.readlines()[1])
        print 'mp: ', mpdatos
        datosreader.close()
        
        #mp del pj
        mptpj=mpdatos
        mppj=mptpj
    
    ######
        #variable diners
        moneyreader=open('log\money.txt')
        money=int(moneyreader.readline())
        print 'dinero:', money
        moneyreader.close()
    
        money_t=str(money)
        moneywriter=open('log\money.txt','w')
        moneywriter.write(money_t)
        moneywriter.close()
    
        perdrediners=money
        
    
        sonido3.play()
    
    
        while salir != True:
            
            
            
                
            
            
            
            if cont20==1:
                monstruo2image1=pygame.image.load("images/goblinw/guerrero2.png").convert_alpha()
                monstruo2image2=pygame.image.load("images/goblinw/guerrero2_2.png").convert_alpha()
                monstruo2image3=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
                monstruo2image4=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
                monstruo2image5=pygame.image.load("images/goblinw/guerrero2_5.png").convert_alpha()
                monstruo2image6=pygame.image.load("images/goblinw/guerrero2_6.png").convert_alpha()
                monstruo2image7=pygame.image.load("images/goblinw/guerrero2_3.png").convert_alpha()
                monstruo2image8=pygame.image.load("images/goblinw/guerrero2_4.png").convert_alpha()
                monstruo2image9=pygame.image.load("images/goblinw/guerrero2_7.png").convert_alpha()
            else:
                monstruo2image1=pygame.image.load("images/goblinw/guerrero4.png").convert_alpha()
                monstruo2image2=pygame.image.load("images/goblinw/guerrero4_2.png").convert_alpha()
                monstruo2image3=pygame.image.load("images/goblinw/guerrero4_4.png").convert_alpha()
                monstruo2image4=pygame.image.load("images/goblinw/guerrero4_3.png").convert_alpha()
                monstruo2image5=pygame.image.load("images/goblinw/guerrero4_5.png").convert_alpha()
                monstruo2image6=pygame.image.load("images/goblinw/guerrero4_6.png").convert_alpha()
                monstruo2image7=pygame.image.load("images/goblinw/guerrero4_3.png").convert_alpha()
                monstruo2image8=pygame.image.load("images/goblinw/guerrero4_4.png").convert_alpha()
                monstruo2image9=pygame.image.load("images/goblinw/guerrero4_7.png").convert_alpha()
                
                
            if cont19==0 or cont19==1:
                monstruoimage1=pygame.image.load("images/goblinw/monstruo1.png").convert_alpha()
                monstruoimage3=pygame.image.load("images/goblinw/monstruo1_3.png").convert_alpha()
                monstruoimage4=pygame.image.load("images/goblinw/monstruo1_4.png").convert_alpha()
                monstruoimage5=pygame.image.load("images/goblinw/monstruo1_5.png").convert_alpha()
                monstruoimage6=pygame.image.load("images/goblinw/monstruo1_6.png").convert_alpha()
                
            else:
                monstruoimage1=pygame.image.load("images/goblinw/monstruo2.png").convert_alpha()
                monstruoimage3=pygame.image.load("images/goblinw/monstruo2_3.png").convert_alpha()
                monstruoimage4=pygame.image.load("images/goblinw/monstruo2_4.png").convert_alpha()
                monstruoimage5=pygame.image.load("images/goblinw/monstruo2_5.png").convert_alpha()
                monstruoimage6=pygame.image.load("images/goblinw/monstruo2_6.png").convert_alpha()
                
                
        
                
            var_potion=False
            
            hp_pjant=hp_pj
    
            if hp_pj<=0 and var1==1:
                sprite1.image=goblindr
    
            if hp_pj<=0 and var1==2:
                sprite1.image=goblindl
                
    
            xant=sprite1.rect.left
            yant=sprite1.rect.top
    
            if hpmonstruo1<0:
                hpmonstruo1==0
            
            if hpmonstruo1==0:
                spritemonstruo1.image=monstruoimage3
    
    
    
            if hpmonstruo2<0:
                hpmonstruo2==0
            
            if hpmonstruo2==0:
                sger.image=monstruo2image9
    
                
    
            if hpmonstruo3<0:
                hpmonstruo3==0
            
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
                
    
            if hp_pj<0:
                hp_pj=0
                
    
    
            xmant1=smonster.rect.left
            ymant1=smonster.rect.top
            xmant2=sger.rect.left
            ymant2=sger.rect.top
            xmant3=spritemonstruo1.rect.left
            ymant3=spritemonstruo1.rect.top
    
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN and hp_pj>0:
    
                    if event.key==pygame.K_LEFT and sprite1.rect.left>0:
                        if cont1==0:
                            sprite1.image=goblinwl1
                        if cont1==1:
                            sprite1.image=goblinwl2
                        if cont1==2:
                            sprite1.image=goblinwl3
                        if cont1==3:
                            sprite1.image=goblinwl4
                        if cont1==4:
                            sprite1.image=goblinwl3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left-=6
                        cont1+=1
                        var1=2
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
                        
    
                    if event.key==pygame.K_RIGHT and sprite1.rect.left<775:
                        if cont1==0:
                            sprite1.image=goblinwr1
                        if cont1==1:
                            sprite1.image=goblinwr2
                        if cont1==2:
                            sprite1.image=goblinwr3
                        if cont1==3:
                            sprite1.image=goblinwr4
                        if cont1==4:
                            sprite1.image=goblinwr3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left+=6
                        cont1+=1
                        var1=1
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_UP and sprite1.rect.top>0:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
                            
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top-=6
                        cont1+=1
                        var4=1
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_DOWN and sprite1.rect.top<555:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top+=6
                        cont1+=1
                        var4=2
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_SPACE:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinar2
                            if cont1==1:
                                sprite1.image=goblinar1
                            if cont1==2:
                                sprite1.image=goblinar1
                            if cont1==3:
                                sprite1.image=goblinar2
                            if cont1==4:
                                sprite1.image=goblinar3
                            if cont1>=5:
                                cont1=0
                                sprite1.image=goblinar2
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinal2
                            if cont1==1:
                                sprite1.image=goblinal1
                            if cont1==2:
                                sprite1.image=goblinal2
                            if cont1==3:
                                sprite1.image=goblinal3
                            if cont1>=4:
                                cont1=0
                                sprite1.image=goblinal2
                                
                        cont1+=1
                        var_attack=True
                        if cont1%2==0:
                            sonidoespadaF.play()
    
                        
                            
    
                        
                    if event.key==pygame.K_m:
                        if cont2<=3:
                            if var1==1:
                                sprite1.image=goblinamr
                            if var1==2:
                                sprite1.image=goblinaml
                        if cont2==4:
                            if var1==1:
                                sprite1.image=goblin1
                            if var1==2:
                                sprite1.image=goblin2
                        if cont2==1 and mppj>=20:
                            var_magia=True
                        cont2+=1
    
    
                    if event.key==pygame.K_h and potionshp>0 and hp_pj>0:
                        if hp_pj<hpt_pj:
                            potionshp-=1
                            hp_pj+=random.randrange(15,20)
                            sopotion.play()
                            print 'potionshp: ', potionshp
                            var_potion=True
                            
                            if hp_pj>hpt_pj:
                                hp_pj=hpt_pj
    
                    if event.key==pygame.K_j and potionsmp>0 and hp_pj>0:
                        if mppj<mptpj:
                            potionsmp-=1
                            mppj+=random.randrange(10,20)
                            sopotion.play()
                            print 'potionsmp: ', potionsmp
                            
                            if mppj>mptpj:
                                mppj=mptpj
    
                    if event.key==pygame.K_n and escudo==1 and hp_pj>0 and mppj>=60:
                        mppj-=60
                        var_escudo=True
                        print 'escudo activado'
                    
                    if event.key==pygame.K_b and terremoto==1 and hp_pj>0 and mppj>=250 and var_terremoto==False:
                        mppj-=250
                        var_terremoto=True
                        print 'terremoto activado'
                        
                        
    
                    if event.key==pygame.K_ESCAPE:
                        sonido3.stop()
                        menu1()
                            
                            
                    
                if event.type==pygame.KEYUP and hp_pj>0:
                    if var1==1:
                        sprite1.image=goblin1
                    if var1==2:
                        sprite1.image=goblin2
                        
                    var_attack=False
                    cont2=0
                    cont1=0
                    
    
            reloj1.tick(17)
            
            
            pantalla.blit(fondo,(0,0))
            
            
            
            if var_terremoto==True:
                if var3==True:
                    hpmonstruo1=0
                if var3_2==True:
                    hpmonstruo2=0
                if var3_3==True and var7==1:
                    hpmonstruo3=0
                s_terremoto.play()
                cont_terremoto+=1
                if cont_terremoto%2==0:
                    pantalla.blit(fondo,(random.randrange(0,5),random.randrange(0,5)))
                else:
                    pantalla.blit(fondo,(0,0))
            if cont_terremoto==10:
                var_terremoto=False
                cont_terremoto=0
                
            #imprimacio de las rokass
            pantalla.blit(sr1.image,sr1.rect)
            pantalla.blit(sr2.image,sr2.rect)
            pantalla.blit(sr3.image,sr3.rect)
    
            pantalla.blit(sprite1.image,sprite1.rect)
    
            
    
            if var3==True:
                pantalla.blit(spritemonstruo1.image,spritemonstruo1.rect)
    
    
            if var3_2==True:
                pantalla.blit(sger.image,sger.rect)
    
            
            
            #MOVIMENTS DEL MONSTRE 1 (pop)
                
            if var3==True and hpmonstruo1>0 and hp_pj>0:
                variable1=random.randrange(0,5)
    
    
                if variable1==0 or variable1==1:
                    if spritemonstruo1.rect.left<770 and sprite1.rect.left>spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left+=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage5
                if variable1==1 or variable1==2:
                    if spritemonstruo1.rect.top<570 and sprite1.rect.top>spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top+=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage1
                if variable1==2 or variable1==3:
                    if spritemonstruo1.rect.top>15 and sprite1.rect.top<spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top-=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage6
                if variable1==3 or variable1==0:
                    if spritemonstruo1.rect.left>15 and sprite1.rect.left<spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left-=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage4
    
            #MOVIMENTS DEL MONSTRE 2 (guerrer daurat)
                
            if var3_2==True and hpmonstruo2>0 and hp_pj>0:
                variable1_2=random.randrange(0,5)
    
    
                if variable1_2==0 or variable1_2==1:
                    if sger.rect.left<770 and sprite1.rect.left>sger.rect.left:
                        sger.rect.left+=random.randrange(0,10)
                        randomvar1=random.randrange(0,2)
                        if randomvar1==0:
                            sger.image=monstruo2image2
                        else:
                            sger.image=monstruo2image3
                        var_d2=1
                            
                if variable1_2==1 or variable1_2==2:
                    if sger.rect.top<570 and sprite1.rect.top>sger.rect.top:
                        sger.rect.top+=random.randrange(0,7)
                        randomvar1=random.randrange(0,2)
                        if var_d2==1:
                            if randomvar1==0:
                                sger.image=monstruo2image2
                            else:
                                sger.image=monstruo2image3
    
                        if var_d2==2:
                            if randomvar1==0:
                                sger.image=monstruo2image1
                            else:
                                sger.image=monstruo2image4
    
                            
                            
                if variable1_2==2 or variable1_2==3:
                    if sger.rect.top>15 and sprite1.rect.top<sger.rect.top:
                        sger.rect.top-=random.randrange(0,7)
                        randomvar1=random.randrange(0,2)
                        if var_d2==1:
                            if randomvar1==0:
                                sger.image=monstruo2image2
                            else:
                                sger.image=monstruo2image3
    
                        if var_d2==2:
                            if randomvar1==0:
                                sger.image=monstruo2image1
                            else:
                                sger.image=monstruo2image4
                        
                        
                            
                if variable1_2==3 or variable1_2==0:
                    if sger.rect.left>15 and sprite1.rect.left<sger.rect.left:
                        sger.rect.left-=random.randrange(0,10)
                        randomvar1=random.randrange(0,2)
                        if randomvar1==0:
                            sger.image=monstruo2image1
                        else:
                            sger.image=monstruo2image4
                        var_d2=2
    
            
                        
                        
            #"INVOCACIO" BOLA DE FOC
                        
            if var_magia==True and cont5==0 and mppj>20:
                #sprite de la bola de foc
                spritefoc=pygame.sprite.Sprite()
                spritefoc.image=foc1
                spritefoc.rect=foc1.get_rect()
                if var4==0:
                    spritefoc.rect.top=sprite1.rect.top+5
                if var4==1 or var4==2:
                    spritefoc.rect.left=sprite1.rect.left+5
    
                if var1==1 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left+20
                if var1==2 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left-20
                if var4==1:
                    spritefoc.rect.top=sprite1.rect.top-20
                if var4==2:
                    spritefoc.rect.top=sprite1.rect.top+20
    
                mppj-=20
                sonido2.play()
                cont5+=1
    
            #MOVIMENTS BOLA DE FOC
            if var_magia==True:
                pantalla.blit(spritefoc.image,spritefoc.rect)
                if cont3==0:
                    cont3+=1
                    if var1==1 and var4==0:
                        var2=1
                    if var1==2 and var4==0:
                        var2=2
                    if var4==1:
                        var2=3
                    if var4==2:
                        var2=4
    
                if cont3>0 and cont4<70:
                    if var2==1:
                        spritefoc.rect.left+=10
                    if var2==2:
                        spritefoc.rect.left-=10
                    if var2==3:
                        spritefoc.rect.top-=10
                    if var2==4:
                        spritefoc.rect.top+=10
                    cont4+=2
    
            if spritefoc.rect.left<0 or spritefoc.rect.left>800 or spritefoc.rect.top>600 or spritefoc.rect.top<0 or cont4>=70 or spritefoc.rect.colliderect(sr1.rect) or spritefoc.rect.colliderect(sr2.rect) or spritefoc.rect.colliderect(sr3.rect):
                var_magia=False
                
            if var_magia==False:
                cont3=0
                cont4=0
                cont5=0
                spritefoc.rect.top=99999
                spritefoc.rect.left=99999
    
    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
            var_attackconfirm_l=sprite1.rect.left-spritemonstruo1.rect.left
            var_attackconfirm_t=sprite1.rect.top-spritemonstruo1.rect.top
    
            var_attackconfirm_l_2=sprite1.rect.left-sger.rect.left
            var_attackconfirm_t_2=sprite1.rect.top-sger.rect.top
    
    #accions que infringeixen dany al monstre (pop)
            
            if var3==True:
                if spritefoc.rect.colliderect(spritemonstruo1) and hpmonstruo1>0:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(5,15)
                    if hpmonstruo1<0:
                        hpmonstruo1==0
            
                if var1==1 and var_attackconfirm_l>-20 and var_attackconfirm_l<10 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left+10,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
                if var1==2 and var_attackconfirm_l>-10 and var_attackconfirm_l<20 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left-10)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
    
    #accions que infringeixen dany al monstre (guerrer)
            
            if var3_2==True:
                if spritefoc.rect.colliderect(sger) and hpmonstruo2>0:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(1,4)
                    if hpmonstruo2<0:
                        hpmonstruo2==0
            
                if var1==1 and var_attackconfirm_l_2>-25 and var_attackconfirm_l_2<20 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left+10,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
                if var1==2 and var_attackconfirm_l_2>-20 and var_attackconfirm_l_2<25 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left-10)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
    
    
    #accions que infringeixen dany al pj (pop)
                        
            if var3==True and spritemonstruo1.rect.colliderect(sprite1.rect) and hpmonstruo1>0 and hp_pj>0:
                hp_pj-=random.randrange(0,2)
                sprite1.rect.left-=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo1<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
    
    #accions que infringeixen dany al pj (guerrer d)
                        
            if var3_2==True and sger.rect.colliderect(sprite1.rect) and hpmonstruo2>0 and hp_pj>0:
                hp_pj-=random.randrange(1,4)
                sprite1.rect.left+=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo2<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
            
    
    #axo serveix perk no senkalli el pj en matar el monstre
            #if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6<50 and hpmonstruo1==0:
             #   sprite1.rect.left+=10
                
            #if sprite1.rect.colliderect(sger.rect) and cont6<50 and hpmonstruo2==0:
             #   sprite1.rect.left+=10
            
    #vida dels monstres          
            if var3==True:
                if cont19==0 or cont19==1:       
                    hpm1=str(str(hpmonstruo1)+'/100')
                else:       
                    hpm1=str(str(hpmonstruo1)+'/120')
                
    
            if var3_2==True:
                hpm2=str(str(hpmonstruo2)+'/100')
    
    #per fer desaparexer el pop un kop mort:
            if hpmonstruo1<=0 and cont6<70:
                hpmonstruo1=0
                cont6+=1
                if cont6==70:
                    cont6=0
                    var3=False
                    spritemonstruo1.rect.top=9999
                    spritemonstruo1.rect.left=9999
    
    #per fer desaparexer el guerrer un kop mort:
            if hpmonstruo2<=0 and cont15<70:
                hpmonstruo2=0
                cont15+=1
                if cont15==70:
                    cont15=0
                    var3_2=False
                    sger.rect.top=9999
                    sger.rect.left=9999
    
    
    #imprimacio de la vida dels monstres
            #pop       
            if var3==True:
                textohp1=fuente1.render(hpm1,0,rojo)
                pantalla.blit(textohp1,(spritemonstruo1.rect.left-10,spritemonstruo1.rect.top-25))
    
            #guerrer
            if var3_2==True:
                textohp2=fuente1.render(hpm2,0,rojo)
                pantalla.blit(textohp2,(sger.rect.left-10,sger.rect.top-25))
    
    
    #sistema k fa k el pj no travessi el monstre
            if hpmonstruo1==0:
                if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6>10 and var_c1==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
            if hpmonstruo2==0:
                if sprite1.rect.colliderect(sger.rect) and cont6>10 and var_c2==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
    
    
            if var3==False and cont11==0:
                cont6=0
                cont11+=1
    
            if var3==False and cont12==0:
                cont6=0
                cont12+=1
    
            if hp_pj==0:
                cont13+=1
    
            if cont13==50:
                sonido3.stop()
                menu1()
    
            if hp_pj<=0:
                pantalla.blit(textoGO,(200,200))
                if cont13==1:
                    sonidodead.play()
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                elif cont13==20:
                    sonidodead.stop()
                
    
    #per saber si sa akabat el nivell:
            if var8==True and var8_2==True and var8_3==True:
                pantalla.blit(textoV,(115,200))
                cont16+=1
                var9=True
                if cont16==60:
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                    sonido3.stop()
                    menu1()
    
    
                
                
            
    ###############################################################################
    ###############################################################################
    
    
            if vr3==False or vr3_2==False:
                    var7=1
                #si el monstre esta viu la imatge simprimex en la pantalla
                    
            if var7==1:
                if var3_3==True:
                    pantalla.blit(smonster.image,smonster.rect)
    
                    #moviments
                        
                    if var3_3==True and hpmonstruo3>0 and hp_pj>0:
                        variable1_3=random.randrange(0,5)
    
                        
                        
                        if variable1_3==0 or variable1_3==1:
                            if smonster.rect.left<770 and sprite1.rect.left>smonster.rect.left:
                                smonster.rect.left+=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image1
                                if variable1_3==1:
                                    smonster.image=monstruo3image3
                                var_md=1
                        if variable1_3==1 or variable1_3==2:
                            if smonster.rect.top<570 and sprite1.rect.top>smonster.rect.top:
                                smonster.rect.top+=random.randrange(0,25)
                                if var_md==1:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image1
                                    if variable1_3==1:
                                        smonster.image=monstruo3image3
                                if var_md==2:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image2
                                    if variable1_3==1:
                                        smonster.image=monstruo3image4
                        if variable1_3==2 or variable1_3==3:
                            if smonster.rect.top>15 and sprite1.rect.top<smonster.rect.top:
                                smonster.rect.top-=random.randrange(0,25)
                                if var_md==1:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image1
                                    if variable1_3==1:
                                        smonster.image=monstruo3image3
                                if var_md==2:
                                    if variable1_3==0:
                                        smonster.image=monstruo3image2
                                    if variable1_3==1:
                                        smonster.image=monstruo3image4
                                    
                        if variable1==3 or variable1_3==0:
                            if smonster.rect.left>15 and sprite1.rect.left<smonster.rect.left:
                                smonster.rect.left-=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image2
                                if variable1_3==3:
                                    smonster.image=monstruo3image4
                                var_md=2
    
            
    
    
    
                    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
                    var_attackconfirm_l_3=sprite1.rect.left-smonster.rect.left
                    var_attackconfirm_t_3=sprite1.rect.top-smonster.rect.top
    
                #accions que infringeixen dany al monstre (snake)
    
                    if var3_3==True:
                        if spritefoc.rect.colliderect(smonster) and hpmonstruo3>0:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(5,15)
                            if hpmonstruo3<0:
                                hpmonstruo3==0
    
                        if var1==1 and var_attackconfirm_l_3>-20 and var_attackconfirm_l_3<10 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left+10,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
                        if var1==2 and var_attackconfirm_l_3>-10 and var_attackconfirm_l_3<20 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left-10)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
    
    
                    #accions que infringeixen dany al pj (snake)
                                
                    if var3_3==True and smonster.rect.colliderect(sprite1.rect) and hpmonstruo3>0 and hp_pj>0:
                        hp_pj-=random.randrange(0,2)
                        sprite1.rect.left-=random.randrange(-5,5)
                        sprite1.rect.top+=random.randrange(-5,5)
    
                        if var1==1:
                            sprite1.image=goblinhr
                        if var1==2:
                            sprite1.image=goblinhl
    
                    if hpmonstruo3<0:
                        hpmonstruo3==0
    
    
                    hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    textohppj=fuente1.render(hppjt,0,verde)
                    pantalla.blit(textohppj,(5,5))
    
                    #t=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    #textohppj=fuente1.render(hppjt,0,verde)
                    #pantalla.blit(textohppj,(5,5))
    
    
                    #axo serveix perk no senkalli el pj en matar el monstre
                    #if sprite1.rect.colliderect(smonster.rect) and cont6<50 and hpmonstruo3==0:
                     #   sprite1.rect.left+=10
                        
    
                    #vida dels monstres          
                    if var3_3==True:       
                        hpm3=str(str(hpmonstruo3)+'/50')
    
                    #per fer desaparexer el snake un kop mort:
                    
                    if hpmonstruo3<=0 and cont17<70:
                        hpmonstruo3=0
                        cont17+=1
                        if cont17==70:
                            cont17=0
                            var3_3=False
                            smonster.rect.top=9999
                            smonster.rect.left=9999
    
    
                    #imprimacio de la vida dels monstres       
                    if var3_3==True:
                        textohp1=fuente1.render(hpm3,0,rojo)
                        pantalla.blit(textohp1,(smonster.rect.left-10,smonster.rect.top-25))
    
    
                    #sistema k fa k el pj no travessi el monstre
                    if hpmonstruo3==0:
                        if sprite1.rect.colliderect(smonster.rect) and cont6>10 and var_c3==True:
                            sprite1.rect.left=xant
                            sprite1.rect.top=yant
    
                    
    
    
    
    
                    if var3_3==False and cont11==0:
                        cont6=0
                        cont11+=1
    
                    if var3_3==False and cont12==0:
                        cont6=0
                        cont12+=1
    
    
    
            vr3=var3
            vr3_2=var3_2
            vr3_3=var3_3
    
            
    
    
    #si el pop esta mort i sa mort menys de 4 vegades torna a aparexer depen del resultat de f
            if vr3==False and cont19<4:
                    spritemonstruo1=pygame.sprite.Sprite()
                    spritemonstruo1.image=monstruoimage1
                    spritemonstruo1.rect=monstruoimage1.get_rect()
                    spritemonstruo1.rect.top=random.randrange(0,570)
                    spritemonstruo1.rect.left=random.randrange(0,770)
                    if cont19==0 or cont19==1:
                        hpmonstruo1=100
                    else:
                        hpmonstruo1=120
                    cont6=0
                    var3=True
                    cont19+=1
                    cont23=0
            if cont19==4 and var3==False:
                var8=True
                
    #
            if vr3_2==False and cont20<2:
                    sger=pygame.sprite.Sprite()
                    sger.image=monstruo2image1
                    sger.rect=monstruo2image1.get_rect()
                    sger.rect.top=random.randrange(0,570)
                    sger.rect.left=random.randrange(0,770)
                    hpmonstruo2=100
                    cont6=0
                    var3_2=True
                    cont20+=1
                    cont24=0
            if cont20==2 and var3_2==False:
                var8_2=True
    
    
    
            if vr3_3==False and cont21<5:
                    smonster=pygame.sprite.Sprite()
                    smonster.image=monstruo3image1
                    smonster.rect=monstruo3image1.get_rect()
                    smonster.rect.top=random.randrange(0,570)
                    smonster.rect.left=random.randrange(0,770)
                    hpmonstruo3=50
                    cont6=0
                    var3_3=True
                    cont21+=1
                    cont25=0
            if cont21==5 and var3_3==False:
                var8_3=True
    
                
    ####AKI ANIRA LU MATEX K LU DEL POP AM ELS ALTRES 2 MONSTRES
    
    #per k es recargi el mp:
            cont18+=1
            if cont18%10==0 and mppj<mpdatos:
                mppj+=1
        
    #imprimacio del mp:
            mppjt=str('MP: '+str(mppj)+'/'+str(mptpj))
            textomppj=fuente1.render(mppjt,0,verde)
            pantalla.blit(textomppj,(700,5))
    
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
    
    #per guardar la kantitat de diners i desblokejar el seguen nivell si sa completat la misio
            if var9==True:
                money_t=str(money)
                moneywriter=open('log\money.txt','w')
                moneywriter.write(money_t)
                moneywriter.close()
            
                moneyreader=open('log\money.txt')
                money=int(moneyreader.readline())
                moneyreader.close()
    
                if mision==6:
                    misionwriter=open('log\misions.txt','w')
                    misionwriter.write('7')
                    misionwriter.close()
    
            
    
    #per sumar diners al matar els monstres:
            if cont23==0 and hpmonstruo1==0:
                cont23+=1
                money+=random.randrange(15,26)
                print 'dinero:', money
    
            if cont24==0 and hpmonstruo2==0:
                cont24+=1
                money+=random.randrange(35,45)
                print 'dinero:', money
    
            if cont25==0 and hpmonstruo3==0:
                cont25+=1
                money+=random.randrange(12,18)
                print 'dinero:', money
    
                
                
    
            if hp_pj==0:
                money=perdrediners
                
                if contx==0:
                    print 'dinero: ', money
                    contx+=1
    
            tttmoney=str('Dinero: '+str(money))
            textomoney=fuente1.render(tttmoney,0,verde)
            pantalla.blit(textomoney,(200,5))
    
            misionreader=open('log\misions.txt')
            mision=int(misionreader.readline())
            misionreader.close()
    
        
            if sprite1.rect.colliderect(sr1.rect) or sprite1.rect.colliderect(sr2.rect) or sprite1.rect.colliderect(sr3.rect):     
                #sprite1.rect.left=xant
                #sprite1.rect.top=yant
                hp_pj -= 1
                s_cremada.play()
            #else:
                #s_cremada.stop()
    
    #prk el pj no surti del mapa:
            if sprite1.rect.left<=0:
                sprite1.rect.left=0
            if sprite1.rect.top<=0:
                sprite1.rect.top=0
            if sprite1.rect.left>=780:
                sprite1.rect.left=780
            if sprite1.rect.top>=550:
                sprite1.rect.top=550
    
    #prk els monstres no chokin am les palmeras:
            #if smonster.rect.colliderect(sr1.rect) or smonster.rect.colliderect(sr2.rect) or smonster.rect.colliderect(sr3.rect) and contG>0:
                #smonster.rect.left=xmant1
                #smonster.rect.top=ymant1
                #contE3+=1
            #else:
                #contE3=0
            #if sger.rect.colliderect(sr1.rect) or sger.rect.colliderect(sr2.rect) or sger.rect.colliderect(sr3.rect) and contG>0:
                #sger.rect.left=xmant2
                #sger.rect.top=ymant2
                #contE2+=1
            #else:
                #contE2=0
            #if spritemonstruo1.rect.colliderect(sr1.rect) or spritemonstruo1.rect.colliderect(sr2.rect) or spritemonstruo1.rect.colliderect(sr3.rect) and contG>0:
                #spritemonstruo1.rect.left=xmant3
                #spritemonstruo1.rect.top=ymant3
                #contE1+=1
            #else:
                #contE1=0
    
            
    
            #imprimacio dels arbres
            #pantalla.blit(sa1.image,sa1.rect)
            #pantalla.blit(sa2.image,sa2.rect)
            #pantalla.blit(sa3.image,sa3.rect)
            
    
    #perk el pj no senkalli am els monstres:
            if hpmonstruo1==0 and sprite1.rect.colliderect(spritemonstruo1)==False:
                var_c1=True
            if hpmonstruo2==0 and sprite1.rect.colliderect(sger)==False:
                var_c2=True
            if hpmonstruo3==0 and sprite1.rect.colliderect(smonster)==False:
                var_c3=True
    
            if hpmonstruo1>0:
                var_c1=False
            if hpmonstruo2>0:
                var_c2=False
            if hpmonstruo3>0:
                var_c3=False
    
    #per si el monstre aparex sobre una roka k es mogi per no enkallarse
            #if contE1==2:
       #         smonster.rect.left+=10
        #    if contE2==2:
         #       sger.rect.left+=10
        #    if contE3==2:
          #      spritemonstruo1.rect.left+=10
    
    #perk kridin els monstres kuan morin:
            if hpmonstruo1==0 and contC1==0:
                sonidocrit1.play()
                contC1+=1
            if hpmonstruo1>0:
                contC1=0
    
            if hpmonstruo2==0 and contC2==0:
                sonidocrit2.play()
                contC2+=1
            if hpmonstruo2>0:
                contC2=0
    
            if hpmonstruo3==0 and contC3==0:
                sonidocrit3.play()
                contC3+=1
            if hpmonstruo3>0:
                contC3=0
    
    #per fer k el gerrer tingi la imatge de atacant:
            if hpmonstruo2>0 and sger.rect.colliderect(sprite1) and var_d2==1:
                if contG%2==0:
                    sger.image=monstruo2image5
    
            if hpmonstruo2>0 and sger.rect.colliderect(sprite1) and var_d2==2:
                if contG%2==0:
                    sger.image=monstruo2image6
    
            
            #textos pocions:
            potionhpt=str('Pociones HP: '+str(potionshp))
            potionmpt=str('Pociones MP: '+str(potionsmp))
            textohpp=fuente1.render(potionhpt,0,verde)
            textompp=fuente1.render(potionmpt,0,verde)
            pantalla.blit(textohpp,(350,5))
            pantalla.blit(textompp,(500,5))
    
    
            if var_escudo==True:
                spritee.rect.top=sprite1.rect.top-15
                spritee.rect.left=sprite1.rect.left-25
            else:
                spritee.rect.top=999999
                spritee.rect.left=999999
    
            if var_escudo==True:
                cont_escudo+=1
            if var_escudo==True and var_potion==False:
                hp_pj=hp_pjant
    
            if cont_escudo==100:
                var_escudo=False
                cont_escudo=0
    
            
            
    
            pantalla.blit(spritee.image,spritee.rect)
            
            #per fer k leskut giri :)
            if var_escudo==True:
                escut_i=pygame.transform.rotate(escut_i, 90)
                spritee.image=escut_i
            
            contG+=1
            
            if contG%10==0:
                rock1image=pygame.image.load("images/goblinw/lava.png").convert_alpha()
                rock2image=pygame.image.load("images/goblinw/lava2.png").convert_alpha()
            elif contG%6==0:
                rock1image=pygame.image.load("images/goblinw/lava2.png").convert_alpha()
                rock2image=pygame.image.load("images/goblinw/lava3.png").convert_alpha()
            else:
                rock1image=pygame.image.load("images/goblinw/lava3.png").convert_alpha()
                rock2image=pygame.image.load("images/goblinw/lava.png").convert_alpha()
                
                
            sr1.image=rock1image
            sr2.image=rock2image
            sr3.image=rock1image
            
            pygame.display.update()
        pygame.quit()
        #8938
    
    def guerra7():
        #SA DE ARREGLAR EL 7!!!
        pygame.init()
        pygame.key.set_repeat(20)
        pantalla=pygame.display.set_mode((800,600))
        fondo=pygame.image.load("images/goblinw/fonsgel.png")
        icono=pygame.image.load("images/goblinw/icon.png")
        pygame.display.set_caption('GOBLIN W.')
        pygame.display.set_icon(icono)
    
        #rectangles dels arbres
        #r_a1=pygame.Rect(80,300,10,30)
        #r_a2=pygame.Rect(400,200,10,30)
        #r_a3=pygame.Rect(700,400,10,30)
    
        #pygame.draw.rect(pantalla,(0,0,0),r_a1)
        #pygame.draw.rect(pantalla,(0,0,0),r_a2)
        #pygame.draw.rect(pantalla,(0,0,0),r_a3)
    
    
        #SONS
        sonido1=pygame.mixer.Sound("sounds/goblinw/Blast.wav")
        sonido2=pygame.mixer.Sound("sounds/goblinw/explosion.wav")
        sonido3=pygame.mixer.Sound("sounds/goblinw/BSO1.wav")
        sonidodead=pygame.mixer.Sound("sounds/goblinw/deadpj.wav")
        sonidoespada=pygame.mixer.Sound("sounds/goblinw/Sspada.wav")
        sonidoespadaF=pygame.mixer.Sound("sounds/goblinw/SspadaF.wav")
        sonidocrit1=pygame.mixer.Sound("sounds/goblinw/crit1.wav")
        sonidocrit2=pygame.mixer.Sound("sounds/goblinw/crit2.wav")
        sonidocrit3=pygame.mixer.Sound("sounds/goblinw/crit3.wav")
        sonidorun=pygame.mixer.Sound("sounds/goblinw/run.wav")
        sopotion=pygame.mixer.Sound("sounds/goblinw/potion.wav")
        s_terremoto=pygame.mixer.Sound("sounds/goblinw/terremoto.wav")
        #sonidocrit3=pygame.mixer.Sound("sounds/goblinw/.wav")
    
        
        #goblin parat
        goblin1=pygame.image.load("images/goblinw/Idle0.png").convert_alpha()
        goblin2=pygame.image.load("images/goblinw/Idle1.png").convert_alpha()
    
        #goblin caminant cap a la dreta
        goblinwr1=pygame.image.load("images/goblinw/Walk0.png").convert_alpha()
        goblinwr2=pygame.image.load("images/goblinw/Walk1.png").convert_alpha()
        goblinwr3=pygame.image.load("images/goblinw/Walk2.png").convert_alpha()
        goblinwr4=pygame.image.load("images/goblinw/Walk3.png").convert_alpha()
    
        #goblin caminant cap a leskerra
        goblinwl1=pygame.image.load("images/goblinw/Walkl0.png").convert_alpha()
        goblinwl2=pygame.image.load("images/goblinw/Walkl1.png").convert_alpha()
        goblinwl3=pygame.image.load("images/goblinw/Walkl2.png").convert_alpha()
        goblinwl4=pygame.image.load("images/goblinw/Walkl3.png").convert_alpha()
    
        #goblin atakant cap a la dreta
        goblinar1=pygame.image.load("images/goblinw/Attack0.png").convert_alpha()
        goblinar2=pygame.image.load("images/goblinw/Attack1.png").convert_alpha()
        goblinar3=pygame.image.load("images/goblinw/Attack2.png").convert_alpha()
    
        #goblin atacant cap a leskerra
        goblinal1=pygame.image.load("images/goblinw/Attackl0.png").convert_alpha()
        goblinal2=pygame.image.load("images/goblinw/Attackl1.png").convert_alpha()
        goblinal3=pygame.image.load("images/goblinw/Attackl2.png").convert_alpha()
    
        #goblin atacant am magia cap a la dreta
        goblinamr=pygame.image.load("images/goblinw/Attackmr.png").convert_alpha()
    
        #goblin atacant am magia kap a leskerra
        goblinaml=pygame.image.load("images/goblinw/Attackml.png").convert_alpha()
    
        #goblin mort 1
        goblindr=pygame.image.load("images/goblinw/Dead0.png").convert_alpha()
    
        #goblin mort 2
        goblindl=pygame.image.load("images/goblinw/Dead1.png").convert_alpha()
    
        #goblin golpejat 1
        goblinhr=pygame.image.load("images/goblinw/Hurt0.png").convert_alpha()
    
        #goblin golpejat 2
        goblinhl=pygame.image.load("images/goblinw/Hurt1.png").convert_alpha()
    
        
        #bola de foc
        foc1=pygame.image.load("images/goblinw/foc.png").convert_alpha()
    
        #monstres
        
        #POP
        monstruoimage1=pygame.image.load("images/goblinw/monstruo2.png").convert_alpha()
        monstruoimage3=pygame.image.load("images/goblinw/monstruo2_3.png").convert_alpha()
        monstruoimage4=pygame.image.load("images/goblinw/monstruo2_4.png").convert_alpha()
        monstruoimage5=pygame.image.load("images/goblinw/monstruo2_5.png").convert_alpha()
        monstruoimage6=pygame.image.load("images/goblinw/monstruo2_6.png").convert_alpha()
    
        #GUERRER DAURAT
        monstruo2image1=pygame.image.load("images/goblinw/guerrero9.png").convert_alpha()
        monstruo2image2=pygame.image.load("images/goblinw/guerrero9_2.png").convert_alpha()
        monstruo2image3=pygame.image.load("images/goblinw/guerrero9_3.png").convert_alpha()
        monstruo2image4=pygame.image.load("images/goblinw/guerrero9_4.png").convert_alpha()
        monstruo2image5=pygame.image.load("images/goblinw/guerrero9_5.png").convert_alpha()
        monstruo2image6=pygame.image.load("images/goblinw/guerrero9_6.png").convert_alpha()
        monstruo2image7=pygame.image.load("images/goblinw/guerrero9_7.png").convert_alpha()
        monstruo2image8=pygame.image.load("images/goblinw/guerrero9_8.png").convert_alpha()
        monstruo2image9=pygame.image.load("images/goblinw/guerrero9_9.png").convert_alpha()
    
        #monstre 3 (sNakE)
        monstruo3image1=pygame.image.load("images/goblinw/snake2.png").convert_alpha()
        monstruo3image2=pygame.image.load("images/goblinw/snake2_2.png").convert_alpha()
        monstruo3image3=pygame.image.load("images/goblinw/snake2.png").convert_alpha()
        monstruo3image4=pygame.image.load("images/goblinw/snake2_2.png").convert_alpha()
        monstruo3image5=pygame.image.load("images/goblinw/snake2.png").convert_alpha()
        monstruo3image6=pygame.image.load("images/goblinw/snake2_2.png").convert_alpha()
        monstruo3image7=pygame.image.load("images/goblinw/snake2.png").convert_alpha()
        monstruo3image8=pygame.image.load("images/goblinw/snake2_3.png").convert_alpha()
        monstruo3image9=pygame.image.load("images/goblinw/snake2_4.png").convert_alpha()
        monstruo3image10=pygame.image.load("images/goblinw/snake2_5.png").convert_alpha()
        monstruo3image11=pygame.image.load("images/goblinw/snake.png").convert_alpha()
    
        #imatges dels arbres
        tree1image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree2image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree3image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
    
    
        #imatge eskut
        escut_i=pygame.image.load("images/goblinw/escudo_m.png").convert_alpha()
        
        
        
        #sprite del goblin
        sprite1=pygame.sprite.Sprite()
        sprite1.image=goblin1
        sprite1.rect=goblin1.get_rect()
        sprite1.rect.top=100
        sprite1.rect.left=50
    
        #sprite de la bola de foc
        spritefoc=pygame.sprite.Sprite()
        spritefoc.image=foc1
        spritefoc.rect=foc1.get_rect()
        spritefoc.rect.top=9999
        spritefoc.rect.left=9999
    
        #sprite de monstre pop 1
        spritemonstruo1=pygame.sprite.Sprite()
        spritemonstruo1.image=monstruoimage1
        spritemonstruo1.rect=monstruoimage1.get_rect()
        spritemonstruo1.rect.top=random.randrange(0,570)
        spritemonstruo1.rect.left=random.randrange(0,770)
    
        #sprite de monstre guerrer 2
        sger=pygame.sprite.Sprite()
        sger.image=monstruo2image1
        sger.rect=monstruo2image1.get_rect()
        sger.rect.top=random.randrange(0,570)
        sger.rect.left=random.randrange(0,770)
    
        #sprite del snake 3
        smonster=pygame.sprite.Sprite()
        smonster.image=monstruo3image1
        smonster.rect=monstruo3image1.get_rect()
        smonster.rect.top=random.randrange(0,570)
        smonster.rect.left=random.randrange(0,770)
    
        #sprite de leskut
        spritee=pygame.sprite.Sprite()
        spritee.image=escut_i
        spritee.rect=escut_i.get_rect()
        spritee.rect.top=sprite1.rect.top
        spritee.rect.left=sprite1.rect.left
    
        #sprites dels arbres
    
        #arbre 1 ########################################################
        #sa1=pygame.sprite.Sprite()
        #sa1.image=tree1image
        #sa1.rect=tree1image.get_rect()
        #sa1.rect.top=280
        #sa1.rect.left=60
    
        #sa2=pygame.sprite.Sprite()
        #sa2.image=tree1image
    #   sa2.rect=tree1image.get_rect()
        #sa2.rect.top=95
        #sa2.rect.left=372
    
        #sa3=pygame.sprite.Sprite()
        #sa3.image=tree1image
        #sa3.rect=tree1image.get_rect()
        #sa3.rect.top=350
        #sa3.rect.left=677
    
        #r_a1=pygame.Rect(87,320,10,30)
        #r_a2=pygame.Rect(400,135,10,30)
        #r_a3=pygame.Rect(705,392,10,30)
        
    
        #fuentes
        fuente1=pygame.font.SysFont("Arial",16,True,False)
        fuentevidapj=pygame.font.SysFont("Arial",25,True,False)
        fuenteGO=pygame.font.SysFont("Arial",70,True,False)
    
        
    
        #colors:
        rojo=(255,0,0)
        azul=(0,0,255)
        verde=(0,255,0)
        blanco=(255,255,255)
        negro=(0,0,0)
    
        #textos constants
        textoGO=fuenteGO.render('GAME OVER',0,rojo)
        textoV=fuenteGO.render('NIVEL COMPLETADO',0,azul)
        
    
        #altres variables i contadors
        cont5=0
        cont4=0
        cont3=0
        cont1=0
        cont2=0
        cont6=0
        cont11=0
        cont12=0
        cont13=0
        cont15=0
        cont16=0
        cont17=0
        cont18=0
        cont19=0
        cont20=0
        cont21=0
        cont22=0
        contx=0
        cont23=0
        cont24=0
        cont25=0
        contG=0
        contE1=0
        contE2=0
        contE3=0
        contC1=0
        contC2=0
        contC3=0
        cont_escudo=0
        cont_terremoto=0
        #########
        var1=1
        var2=0
        var3=True  #<---variable per saber si el monstre esta viu
        var3_2=True #<---variable per saber si el monstre 2 esta viu
        var3_3=False #<---variable per saber si el monster 3 esta viu
        var4=0
        vr3=var3
        vr3_2=var3_2
        vr3_3=var3_3
        var7=0
        var8=False # variable k indica si san matat prous pops per finalitzar el nivell
        var8_2=False
        var8_3=False
        var9=False
        var_c1=True
        var_c2=True
        var_c3=True
        var_escudo=False
        var_potion=False
        var_terremoto=False
    
        #variables per saber si sesta atacant o si sa tirat magia
        var_attack=False
        var_magia=False
    
        #vida monstres i pj
        hpmonstruo1=100
        hpmonstruo2=100
        hpmonstruo3=50
    
        #per llegir les pocions
        potionsreader=open('log\potions.txt')
        potionshp=int(potionsreader.readlines()[0])
        print 'potions hp: ', potionshp
        potionsreader.close()
        
        potionsreader=open('log\potions.txt')
        potionsmp=int(potionsreader.readlines()[1])
        print 'potions mp: ', potionsmp
        potionsreader.close()
    
    
    
    
    
    
    
    #escudo i atak terratremol
        tendareader=open('log/shop.txt')
        escudo=int(tendareader.readlines()[0])
        tendareader.close()
        print 'escudo', escudo
        
        tendareader=open('log/shop.txt')
        terremoto=int(tendareader.readlines()[1])
        tendareader.close()
        print 'terremoto', terremoto
        
    
    
    
    
        
    
    #per llegir el hp del pj:
        datosreader=open('log\datos.txt')
        hpdatos=int(datosreader.readlines()[0])
        print 'hp: ', hpdatos
        datosreader.close()
    
        hp_pj=hpdatos
        hpt_pj=hp_pj
    
        #variable del bucle principal
        salir=False
    
        #reloj
        reloj1=pygame.time.Clock()
    
        #grup de sprites de monstres
        grupo_m=pygame.sprite.Group(spritemonstruo1,sger,smonster)
    
        #mp del pj
    
        #per llegir el mp del pj:
    
        datosreader=open('log\datos.txt')
        mpdatos=int(datosreader.readlines()[1])
        print 'mp: ', mpdatos
        datosreader.close()
        
        mptpj=mpdatos
        mppj=mptpj
    
        #variable diners
        moneyreader=open('log\money.txt')
        money=int(moneyreader.readline())
        print 'dinero:', money
        moneyreader.close()
    
        money_t=str(money)
        moneywriter=open('log\money.txt','w')
        moneywriter.write(money_t)
        moneywriter.close()
    
        perdrediners=money
        
    
        sonido3.play()
    
    
        while salir != True:
            
            
            var_potion=False
    
            hp_pjant=hp_pj
    
            if hp_pj<=0 and var1==1:
                sprite1.image=goblindr
    
            if hp_pj<=0 and var1==2:
                sprite1.image=goblindl
                
    
            xant=sprite1.rect.left
            yant=sprite1.rect.top
    
            if hpmonstruo1<0:
                hpmonstruo1==0
            
            if hpmonstruo1==0:
                spritemonstruo1.image=monstruoimage3
    
    
    
            if hpmonstruo2<0:
                hpmonstruo2==0
            
            if hpmonstruo2==0:
                sger.image=monstruo2image9
    
                
    
            if hpmonstruo3<0:
                hpmonstruo3==0
            
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
                
    
            if hp_pj<0:
                hp_pj=0
                
    
    
            xmant1=smonster.rect.left
            ymant1=smonster.rect.top
            xmant2=sger.rect.left
            ymant2=sger.rect.top
            xmant3=spritemonstruo1.rect.left
            ymant3=spritemonstruo1.rect.top
    
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN and hp_pj>0:
    
                    if event.key==pygame.K_LEFT and sprite1.rect.left>0:
                        if cont1==0:
                            sprite1.image=goblinwl1
                        if cont1==1:
                            sprite1.image=goblinwl2
                        if cont1==2:
                            sprite1.image=goblinwl3
                        if cont1==3:
                            sprite1.image=goblinwl4
                        if cont1==4:
                            sprite1.image=goblinwl3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left-=6
                        cont1+=1
                        var1=2
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
                        
    
                    if event.key==pygame.K_RIGHT and sprite1.rect.left<775:
                        if cont1==0:
                            sprite1.image=goblinwr1
                        if cont1==1:
                            sprite1.image=goblinwr2
                        if cont1==2:
                            sprite1.image=goblinwr3
                        if cont1==3:
                            sprite1.image=goblinwr4
                        if cont1==4:
                            sprite1.image=goblinwr3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left+=6
                        cont1+=1
                        var1=1
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_UP and sprite1.rect.top>0:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
                            
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top-=6
                        cont1+=1
                        var4=1
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_DOWN and sprite1.rect.top<555:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top+=6
                        cont1+=1
                        var4=2
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_SPACE:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinar2
                            if cont1==1:
                                sprite1.image=goblinar1
                            if cont1==2:
                                sprite1.image=goblinar1
                            if cont1==3:
                                sprite1.image=goblinar2
                            if cont1==4:
                                sprite1.image=goblinar3
                            if cont1>=5:
                                cont1=0
                                sprite1.image=goblinar2
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinal2
                            if cont1==1:
                                sprite1.image=goblinal1
                            if cont1==2:
                                sprite1.image=goblinal2
                            if cont1==3:
                                sprite1.image=goblinal3
                            if cont1>=4:
                                cont1=0
                                sprite1.image=goblinal2
                                
                        cont1+=1
                        var_attack=True
                        if cont1%2==0:
                            sonidoespadaF.play()
    
                        
                            
    
                        
                    if event.key==pygame.K_m:
                        if cont2<=3:
                            if var1==1:
                                sprite1.image=goblinamr
                            if var1==2:
                                sprite1.image=goblinaml
                        if cont2==4:
                            if var1==1:
                                sprite1.image=goblin1
                            if var1==2:
                                sprite1.image=goblin2
                        if cont2==1 and mppj>=20:
                            var_magia=True
                        cont2+=1
    
                    if event.key==pygame.K_h and potionshp>0 and hp_pj>0:
                        if hp_pj<hpt_pj:
                            potionshp-=1
                            hp_pj+=random.randrange(15,20)
                            var_potion=True
                            
                            sopotion.play()
                            print 'potionshp: ', potionshp
                            if hp_pj>hpt_pj:
                                hp_pj=hpt_pj
    
                    if event.key==pygame.K_j and potionsmp>0 and hp_pj>0:
                        if mppj<mptpj:
                            potionsmp-=1
                            mppj+=random.randrange(10,20)
                            sopotion.play()
                            print 'potionsmp: ', potionsmp
                            
                            if mppj>mptpj:
                                mppj=mptpj
    
                    if event.key==pygame.K_n and escudo==1 and hp_pj>0 and mppj>=60:
                        mppj-=60
                        var_escudo=True
                        print 'escudo activado'
                    
                    if event.key==pygame.K_b and terremoto==1 and hp_pj>0 and mppj>=250 and var_terremoto==False:
                        mppj-=250
                        var_terremoto=True
                        print 'terremoto activado'
    
                    
    
                    if event.key==pygame.K_ESCAPE:
                        sonido3.stop()
                        menu1()
                            
                            
                    
                if event.type==pygame.KEYUP and hp_pj>0:
                    if var1==1:
                        sprite1.image=goblin1
                    if var1==2:
                        sprite1.image=goblin2
                        
                    var_attack=False
                    cont2=0
                    cont1=0
                    
    
            reloj1.tick(17)
            
            
            pantalla.blit(fondo,(0,0))
            if var_terremoto==True:
                if var3==True:
                    hpmonstruo1=0
                if var3_2==True:
                    hpmonstruo2=0
                if var3_3==True and var7==1:
                    hpmonstruo3=0
                s_terremoto.play()
                cont_terremoto+=1
                if cont_terremoto%2==0:
                    pantalla.blit(fondo,(random.randrange(0,5),random.randrange(0,5)))
                else:
                    pantalla.blit(fondo,(0,0))
            if cont_terremoto==10:
                var_terremoto=False
                cont_terremoto=0
    
            pantalla.blit(sprite1.image,sprite1.rect)
    
            
    
            if var3==True:
                pantalla.blit(spritemonstruo1.image,spritemonstruo1.rect)
    
    
            if var3_2==True:
                pantalla.blit(sger.image,sger.rect)
    
            
            
            #MOVIMENTS DEL MONSTRE 1 (pop)
                
            if var3==True and hpmonstruo1>0 and hp_pj>0:
                variable1=random.randrange(0,5)
    
    
                if variable1==0 or variable1==1:
                    if spritemonstruo1.rect.left<770 and sprite1.rect.left>spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left+=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage5
                if variable1==1 or variable1==2:
                    if spritemonstruo1.rect.top<570 and sprite1.rect.top>spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top+=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage1
                if variable1==2 or variable1==3:
                    if spritemonstruo1.rect.top>15 and sprite1.rect.top<spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top-=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage6
                if variable1==3 or variable1==0:
                    if spritemonstruo1.rect.left>15 and sprite1.rect.left<spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left-=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage4
    
            #MOVIMENTS DEL MONSTRE 2 (guerrer daurat)
                
            if var3_2==True and hpmonstruo2>0 and hp_pj>0:
                variable1_2=random.randrange(0,5)
    
    
                if variable1_2==0 or variable1_2==1:
                    if sger.rect.left<770 and sprite1.rect.left>sger.rect.left:
                        sger.rect.left+=random.randrange(0,10)
                        sger.image=monstruo2image2
                if variable1_2==1 or variable1_2==2:
                    if sger.rect.top<570 and sprite1.rect.top>sger.rect.top:
                        sger.rect.top+=random.randrange(0,7)
                        sger.image=monstruo2image1
                if variable1_2==2 or variable1_2==3:
                    if sger.rect.top>15 and sprite1.rect.top<sger.rect.top:
                        sger.rect.top-=random.randrange(0,7)
                        sger.image=monstruo2image6
                if variable1_2==3 or variable1_2==0:
                    if sger.rect.left>15 and sprite1.rect.left<sger.rect.left:
                        sger.rect.left-=random.randrange(0,10)
                        sger.image=monstruo2image1
    
            
                        
                        
            #"INVOCACIO" BOLA DE FOC
                        
            if var_magia==True and cont5==0 and mppj>20:
                #sprite de la bola de foc
                spritefoc=pygame.sprite.Sprite()
                spritefoc.image=foc1
                spritefoc.rect=foc1.get_rect()
                if var4==0:
                    spritefoc.rect.top=sprite1.rect.top+5
                if var4==1 or var4==2:
                    spritefoc.rect.left=sprite1.rect.left+5
    
                if var1==1 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left+20
                if var1==2 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left-20
                if var4==1:
                    spritefoc.rect.top=sprite1.rect.top-20
                if var4==2:
                    spritefoc.rect.top=sprite1.rect.top+20
    
                mppj-=20
                sonido2.play()
                cont5+=1
    
            #MOVIMENTS BOLA DE FOC
            if var_magia==True:
                pantalla.blit(spritefoc.image,spritefoc.rect)
                if cont3==0:
                    cont3+=1
                    if var1==1 and var4==0:
                        var2=1
                    if var1==2 and var4==0:
                        var2=2
                    if var4==1:
                        var2=3
                    if var4==2:
                        var2=4
    
                if cont3>0 and cont4<70:
                    if var2==1:
                        spritefoc.rect.left+=10
                    if var2==2:
                        spritefoc.rect.left-=10
                    if var2==3:
                        spritefoc.rect.top-=10
                    if var2==4:
                        spritefoc.rect.top+=10
                    cont4+=2
    
            if spritefoc.rect.left<0 or spritefoc.rect.left>800 or cont4>=70:
                var_magia=False
                
            if var_magia==False:
                cont3=0
                cont4=0
                cont5=0
                spritefoc.rect.top=99999
                spritefoc.rect.left=99999
    
    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
            var_attackconfirm_l=sprite1.rect.left-spritemonstruo1.rect.left
            var_attackconfirm_t=sprite1.rect.top-spritemonstruo1.rect.top
    
            var_attackconfirm_l_2=sprite1.rect.left-sger.rect.left
            var_attackconfirm_t_2=sprite1.rect.top-sger.rect.top
    
    #accions que infringeixen dany al monstre (pop)
            
            if var3==True:
                if spritefoc.rect.colliderect(spritemonstruo1) and hpmonstruo1>0:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(5,15)
                    if hpmonstruo1<0:
                        hpmonstruo1==0
            
                if var1==1 and var_attackconfirm_l>-20 and var_attackconfirm_l<10 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left+10,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
                if var1==2 and var_attackconfirm_l>-10 and var_attackconfirm_l<20 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left-10)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
    
    #accions que infringeixen dany al monstre (guerrer)
            
            if var3_2==True:
                if spritefoc.rect.colliderect(sger) and hpmonstruo2>0:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(1,4)
                    if hpmonstruo2<0:
                        hpmonstruo2==0
            
                if var1==1 and var_attackconfirm_l_2>-25 and var_attackconfirm_l_2<20 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left+10,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
                if var1==2 and var_attackconfirm_l_2>-20 and var_attackconfirm_l_2<25 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left-10)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
    
    
    #accions que infringeixen dany al pj (pop)
                        
            if var3==True and spritemonstruo1.rect.colliderect(sprite1.rect) and hpmonstruo1>0 and hp_pj>0:
                hp_pj-=random.randrange(0,2)
                sprite1.rect.left-=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo1<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
    
    #accions que infringeixen dany al pj (guerrer d)
                        
            if var3_2==True and sger.rect.colliderect(sprite1.rect) and hpmonstruo2>0 and hp_pj>0:
                hp_pj-=random.randrange(1,4)
                sprite1.rect.left+=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo2<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
            
    
    #axo serveix perk no senkalli el pj en matar el monstre
            #if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6<50 and hpmonstruo1==0:
             #   sprite1.rect.left+=10
                
            #if sprite1.rect.colliderect(sger.rect) and cont6<50 and hpmonstruo2==0:
             #   sprite1.rect.left+=10
            
    #vida dels monstres          
            if var3==True:       
                hpm1=str(str(hpmonstruo1)+'/100')
    
            if var3_2==True:
                hpm2=str(str(hpmonstruo2)+'/100')
    
    #per fer desaparexer el pop un kop mort:
            if hpmonstruo1<=0 and cont6<70:
                hpmonstruo1=0
                cont6+=1
                if cont6==70:
                    cont6=0
                    var3=False
                    spritemonstruo1.rect.top=9999
                    spritemonstruo1.rect.left=9999
    
    #per fer desaparexer el guerrer un kop mort:
            if hpmonstruo2<=0 and cont15<70:
                hpmonstruo2=0
                cont15+=1
                if cont15==70:
                    cont15=0
                    var3_2=False
                    sger.rect.top=9999
                    sger.rect.left=9999
    
    
    #imprimacio de la vida dels monstres
            #pop       
            if var3==True:
                textohp1=fuente1.render(hpm1,0,rojo)
                pantalla.blit(textohp1,(spritemonstruo1.rect.left-10,spritemonstruo1.rect.top-25))
    
            #guerrer
            if var3_2==True:
                textohp2=fuente1.render(hpm2,0,rojo)
                pantalla.blit(textohp2,(sger.rect.left-10,sger.rect.top-25))
    
    
    #sistema k fa k el pj no travessi el monstre
            if hpmonstruo1==0:
                if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6>10 and var_c1==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
            if hpmonstruo2==0:
                if sprite1.rect.colliderect(sger.rect) and cont6>10 and var_c2==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
    
    
            if var3==False and cont11==0:
                cont6=0
                cont11+=1
    
            if var3==False and cont12==0:
                cont6=0
                cont12+=1
    
            if hp_pj==0:
                cont13+=1
    
            if cont13==50:
                sonido3.stop()
                menu1()
    
            if hp_pj<=0:
                pantalla.blit(textoGO,(200,200))
                if cont13==1:
                    sonidodead.play()
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                elif cont13==20:
                    sonidodead.stop()
                
    
    #per saber si sa akabat el nivell:
            if var8==True and var8_2==True and var8_3==True:
                pantalla.blit(textoV,(115,200))
                cont16+=1
                var9=True
                if cont16==60:
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                    sonido3.stop()
                    menu1()
    
    
                
                
            
    ###############################################################################
    ###############################################################################
    
    
            if vr3==False or vr3_2==False:
                    var7=1
                #si el monstre esta viu la imatge simprimex en la pantalla
                    
            if var7==1:
                if var3_3==True:
                    pantalla.blit(smonster.image,smonster.rect)
                    
    
                    #moviments
                        
                    if var3_3==True and hpmonstruo3>0 and hp_pj>0:
                        variable1_3=random.randrange(0,5)
    
                        
                        
                        if variable1_3==0 or variable1_3==1:
                            if smonster.rect.left<770 and sprite1.rect.left>smonster.rect.left:
                                smonster.rect.left+=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image5
                                if variable1_3==1:
                                    smonster.image=monstruo3image8
                        if variable1_3==1 or variable1_3==2:
                            if smonster.rect.top<570 and sprite1.rect.top>smonster.rect.top:
                                smonster.rect.top+=random.randrange(0,25)
                                if variable1_3==0:
                                    smonster.image=monstruo3image5
                                if variable1_3==1:
                                    smonster.image=monstruo3image8
                        if variable1_3==2 or variable1_3==3:
                            if smonster.rect.top>15 and sprite1.rect.top<smonster.rect.top:
                                smonster.rect.top-=random.randrange(0,25)
                                if variable1_3==0:
                                    smonster.image=monstruo3image4
                                if variable1_3==1:
                                    smonster.image=monstruo3image9
                        if variable1==3 or variable1_3==0:
                            if smonster.rect.left>15 and sprite1.rect.left<smonster.rect.left:
                                smonster.rect.left-=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image4
                                if variable1_3==3:
                                    smonster.image=monstruo3image9
    
            
    
    
    
                    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
                    var_attackconfirm_l_3=sprite1.rect.left-smonster.rect.left
                    var_attackconfirm_t_3=sprite1.rect.top-smonster.rect.top
    
                #accions que infringeixen dany al monstre (snake)
    
                    if var3_3==True:
                        if spritefoc.rect.colliderect(smonster) and hpmonstruo3>0:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(5,15)
                            if hpmonstruo3<0:
                                hpmonstruo3==0
    
                        if var1==1 and var_attackconfirm_l_3>-20 and var_attackconfirm_l_3<10 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left+10,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
                        if var1==2 and var_attackconfirm_l_3>-10 and var_attackconfirm_l_3<20 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left-10)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
    
    
                    #accions que infringeixen dany al pj (snake)
                                
                    if var3_3==True and smonster.rect.colliderect(sprite1.rect) and hpmonstruo3>0 and hp_pj>0:
                        hp_pj-=random.randrange(0,2)
                        sprite1.rect.left-=random.randrange(-5,5)
                        sprite1.rect.top+=random.randrange(-5,5)
    
                        if var1==1:
                            sprite1.image=goblinhr
                        if var1==2:
                            sprite1.image=goblinhl
    
                    if hpmonstruo3<0:
                        hpmonstruo3==0
    
    
                    hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    textohppj=fuente1.render(hppjt,0,verde)
                    pantalla.blit(textohppj,(5,5))
    
    
                    #axo serveix perk no senkalli el pj en matar el monstre
                    #if sprite1.rect.colliderect(smonster.rect) and cont6<50 and hpmonstruo3==0:
                     #   sprite1.rect.left+=10
                        
    
                    #vida dels monstres          
                    if var3_3==True:       
                        hpm3=str(str(hpmonstruo3)+'/50')
    
                    #per fer desaparexer el snake un kop mort:
                    
                    if hpmonstruo3<=0 and cont17<70:
                        hpmonstruo3=0
                        cont17+=1
                        if cont17==70:
                            cont17=0
                            var3_3=False
                            smonster.rect.top=9999
                            smonster.rect.left=9999
    
    
                    #imprimacio de la vida dels monstres       
                    if var3_3==True:
                        textohp1=fuente1.render(hpm3,0,rojo)
                        pantalla.blit(textohp1,(smonster.rect.left-10,smonster.rect.top-25))
    
    
                    #sistema k fa k el pj no travessi el monstre
                    if hpmonstruo3==0:
                        if sprite1.rect.colliderect(smonster.rect) and cont6>10 and var_c3==True:
                            sprite1.rect.left=xant
                            sprite1.rect.top=yant
    
                    
    
    
    
    
                    if var3_3==False and cont11==0:
                        cont6=0
                        cont11+=1
    
                    if var3_3==False and cont12==0:
                        cont6=0
                        cont12+=1
    
    
    
            vr3=var3
            vr3_2=var3_2
            vr3_3=var3_3
    
            
    
    
    #si el pop esta mort i sa mort menys de 4 vegades torna a aparexer depen del resultat de f
            if vr3==False and cont19<4:
                f=1
                if f==1:
                    spritemonstruo1=pygame.sprite.Sprite()
                    spritemonstruo1.image=monstruoimage1
                    spritemonstruo1.rect=monstruoimage1.get_rect()
                    spritemonstruo1.rect.top=random.randrange(0,570)
                    spritemonstruo1.rect.left=random.randrange(0,770)
                    hpmonstruo1=100
                    cont6=0
                    var3=True
                    cont19+=1
                    cont23=0
            if cont19==4 and var3==False:
                var8=True
                
    #
            if vr3_2==False and cont20<4:
                f2=1
                if f2==1:
                    sger=pygame.sprite.Sprite()
                    sger.image=monstruo2image1
                    sger.rect=monstruo2image1.get_rect()
                    sger.rect.top=random.randrange(0,570)
                    sger.rect.left=random.randrange(0,770)
                    hpmonstruo2=100
                    cont6=0
                    var3_2=True
                    cont20+=1
                    cont24=0
            if cont20==4 and var3_2==False:
                var8_2=True
    
    
    
            if vr3_3==False and cont21<6:
                f3=1
                if f3==1:
                    smonster=pygame.sprite.Sprite()
                    smonster.image=monstruo3image1
                    smonster.rect=monstruo3image1.get_rect()
                    smonster.rect.top=random.randrange(0,570)
                    smonster.rect.left=random.randrange(0,770)
                    hpmonstruo3=50
                    cont6=0
                    var3_3=True
                    cont21+=1
                    cont25=0
            if cont21==6 and var3_3==False:
                var8_3=True
    
                
    ####AKI ANIRA LU MATEX K LU DEL POP AM ELS ALTRES 2 MONSTRES
    
    #per k es recargi el mp:
            cont18+=1
            if cont18%10==0 and mppj<mpdatos:
                mppj+=1
        
    #imprimacio del mp:
            mppjt=str('MP: '+str(mppj)+'/'+str(mptpj))
            textomppj=fuente1.render(mppjt,0,verde)
            pantalla.blit(textomppj,(700,5))
    
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
    
    #per guardar la kantitat de diners i desblokejar el seguen nivell si sa completat la misio
            if var9==True:
                money_t=str(money)
                moneywriter=open('log\money.txt','w')
                moneywriter.write(money_t)
                moneywriter.close()
            
                moneyreader=open('log\money.txt')
                money=int(moneyreader.readline())
                moneyreader.close()
    
                if mision==7:
                    misionwriter=open('log\misions.txt','w')
                    misionwriter.write('8')
                    misionwriter.close()
    
            
    
    #per sumar diners al matar els monstres:
            if cont23==0 and hpmonstruo1==0:
                cont23+=1
                money+=random.randrange(15,27)
                print 'dinero:', money
    
            if cont24==0 and hpmonstruo2==0:
                cont24+=1
                money+=random.randrange(36,46)
                print 'dinero:', money
    
            if cont25==0 and hpmonstruo3==0:
                cont25+=1
                money+=random.randrange(14,19)
                print 'dinero:', money
    
                
                
    
            if hp_pj==0:
                money=perdrediners
                
                if contx==0:
                    print 'dinero: ', money
                    contx+=1
    
            tttmoney=str('Dinero: '+str(money))
            textomoney=fuente1.render(tttmoney,0,verde)
            pantalla.blit(textomoney,(200,5))
    
            misionreader=open('log\misions.txt')
            mision=int(misionreader.readline())
            misionreader.close()
    
        
            #if sprite1.rect.colliderect(r_a1) or sprite1.rect.colliderect(r_a2) or sprite1.rect.colliderect(r_a3):     
             #   sprite1.rect.left=xant
              #  sprite1.rect.top=yant
    
    #prk el pj no surti del mapa:
            if sprite1.rect.left<=0:
                sprite1.rect.left=0
            if sprite1.rect.top<=0:
                sprite1.rect.top=0
            if sprite1.rect.left>=780:
                sprite1.rect.left=780
            if sprite1.rect.top>=550:
                sprite1.rect.top=550
    
    #prk els monstres no chokin am les palmeras:
            #if smonster.rect.colliderect(r_a1) or smonster.rect.colliderect(r_a2) or smonster.rect.colliderect(r_a3):
             #   smonster.rect.left=xmant1
              #  smonster.rect.top=ymant1
               # contE3+=1
            #else:
             #   contE3=0
            #if sger.rect.colliderect(r_a1) or sger.rect.colliderect(r_a2) or sger.rect.colliderect(r_a3):
            #    sger.rect.left=xmant2
             #   sger.rect.top=ymant2
             #   contE2+=1
            #else:
           #     contE2=0
            #if spritemonstruo1.rect.colliderect(r_a1) or spritemonstruo1.rect.colliderect(r_a2) or spritemonstruo1.rect.colliderect(r_a3):
             #   spritemonstruo1.rect.left=xmant3
              #  spritemonstruo1.rect.top=ymant3
               # contE1+=1
            #else:
             #   contE1=0
    
            #imprimacio dels arbres
            #pantalla.blit(sa1.image,sa1.rect)
            #pantalla.blit(sa2.image,sa2.rect)
            #pantalla.blit(sa3.image,sa3.rect)
    
    #perk el pj no senkalli am els monstres:
            if hpmonstruo1==0 and sprite1.rect.colliderect(spritemonstruo1)==False:
                var_c1=True
            if hpmonstruo2==0 and sprite1.rect.colliderect(sger)==False:
                var_c2=True
            if hpmonstruo3==0 and sprite1.rect.colliderect(smonster)==False:
                var_c3=True
    
            if hpmonstruo1>0:
                var_c1=False
            if hpmonstruo2>0:
                var_c2=False
            if hpmonstruo3>0:
                var_c3=False
    
    #per si el monstre aparex sobre un arbre k es mogi per no enkallarse
            #X
    
    #perk kridin els monstres kuan morin:
            if hpmonstruo1==0 and contC1==0:
                sonidocrit1.play()
                contC1+=1
            if hpmonstruo1>0:
                contC1=0
    
            if hpmonstruo2==0 and contC2==0:
                sonidocrit2.play()
                contC2+=1
            if hpmonstruo2>0:
                contC2=0
    
            if hpmonstruo3==0 and contC3==0:
                sonidocrit3.play()
                contC3+=1
            if hpmonstruo3>0:
                contC3=0
    
            #textos pocions:
            potionhpt=str('Pociones HP: '+str(potionshp))
            potionmpt=str('Pociones MP: '+str(potionsmp))
            textohpp=fuente1.render(potionhpt,0,verde)
            textompp=fuente1.render(potionmpt,0,verde)
            pantalla.blit(textohpp,(350,5))
            pantalla.blit(textompp,(500,5))
    
    
            if var_escudo==True:
                spritee.rect.top=sprite1.rect.top-15
                spritee.rect.left=sprite1.rect.left-25
            else:
                spritee.rect.top=999999
                spritee.rect.left=999999
    
            if var_escudo==True:
                cont_escudo+=1
                
            if var_escudo==True and var_potion==False:
                hp_pj=hp_pjant
    
            if cont_escudo==100:
                var_escudo=False
                cont_escudo=0
            
            
                
    
            
            
    
            pantalla.blit(spritee.image,spritee.rect)
            
            #per fer k leskut giri :)
            if var_escudo==True:
                escut_i=pygame.transform.rotate(escut_i, 90)
                spritee.image=escut_i
    
            contG+=1
            
            pygame.display.update()
        pygame.quit()
    
    def guerra8():
        #SA DE ARREGLAR EL 7!!!
        pygame.init()
        pygame.key.set_repeat(20)
        pantalla=pygame.display.set_mode((800,600))
        fondo=pygame.image.load("images/goblinw/fonsgel.png")
        icono=pygame.image.load("images/goblinw/icon.png")
        pygame.display.set_caption('GOBLIN W.')
        pygame.display.set_icon(icono)
    
        #rectangles dels arbres
        #r_a1=pygame.Rect(80,300,10,30)
        #r_a2=pygame.Rect(400,200,10,30)
        #r_a3=pygame.Rect(700,400,10,30)
    
        #pygame.draw.rect(pantalla,(0,0,0),r_a1)
        #pygame.draw.rect(pantalla,(0,0,0),r_a2)
        #pygame.draw.rect(pantalla,(0,0,0),r_a3)
    
    
        #SONS
        sonido1=pygame.mixer.Sound("sounds/goblinw/Blast.wav")
        sonido2=pygame.mixer.Sound("sounds/goblinw/explosion.wav")
        sonido3=pygame.mixer.Sound("sounds/goblinw/BSO1.wav")
        sonidodead=pygame.mixer.Sound("sounds/goblinw/deadpj.wav")
        sonidoespada=pygame.mixer.Sound("sounds/goblinw/Sspada.wav")
        sonidoespadaF=pygame.mixer.Sound("sounds/goblinw/SspadaF.wav")
        sonidocrit1=pygame.mixer.Sound("sounds/goblinw/crit1.wav")
        sonidocrit2=pygame.mixer.Sound("sounds/goblinw/crit2.wav")
        sonidocrit3=pygame.mixer.Sound("sounds/goblinw/crit3.wav")
        sonidorun=pygame.mixer.Sound("sounds/goblinw/run.wav")
        sopotion=pygame.mixer.Sound("sounds/goblinw/potion.wav")
        s_terremoto=pygame.mixer.Sound("sounds/goblinw/terremoto.wav")
        #sonidocrit3=pygame.mixer.Sound("sounds/goblinw/.wav")
    
        
        #goblin parat
        goblin1=pygame.image.load("images/goblinw/Idle0.png").convert_alpha()
        goblin2=pygame.image.load("images/goblinw/Idle1.png").convert_alpha()
    
        #goblin caminant cap a la dreta
        goblinwr1=pygame.image.load("images/goblinw/Walk0.png").convert_alpha()
        goblinwr2=pygame.image.load("images/goblinw/Walk1.png").convert_alpha()
        goblinwr3=pygame.image.load("images/goblinw/Walk2.png").convert_alpha()
        goblinwr4=pygame.image.load("images/goblinw/Walk3.png").convert_alpha()
    
        #goblin caminant cap a leskerra
        goblinwl1=pygame.image.load("images/goblinw/Walkl0.png").convert_alpha()
        goblinwl2=pygame.image.load("images/goblinw/Walkl1.png").convert_alpha()
        goblinwl3=pygame.image.load("images/goblinw/Walkl2.png").convert_alpha()
        goblinwl4=pygame.image.load("images/goblinw/Walkl3.png").convert_alpha()
    
        #goblin atakant cap a la dreta
        goblinar1=pygame.image.load("images/goblinw/Attack0.png").convert_alpha()
        goblinar2=pygame.image.load("images/goblinw/Attack1.png").convert_alpha()
        goblinar3=pygame.image.load("images/goblinw/Attack2.png").convert_alpha()
    
        #goblin atacant cap a leskerra
        goblinal1=pygame.image.load("images/goblinw/Attackl0.png").convert_alpha()
        goblinal2=pygame.image.load("images/goblinw/Attackl1.png").convert_alpha()
        goblinal3=pygame.image.load("images/goblinw/Attackl2.png").convert_alpha()
    
        #goblin atacant am magia cap a la dreta
        goblinamr=pygame.image.load("images/goblinw/Attackmr.png").convert_alpha()
    
        #goblin atacant am magia kap a leskerra
        goblinaml=pygame.image.load("images/goblinw/Attackml.png").convert_alpha()
    
        #goblin mort 1
        goblindr=pygame.image.load("images/goblinw/Dead0.png").convert_alpha()
    
        #goblin mort 2
        goblindl=pygame.image.load("images/goblinw/Dead1.png").convert_alpha()
    
        #goblin golpejat 1
        goblinhr=pygame.image.load("images/goblinw/Hurt0.png").convert_alpha()
    
        #goblin golpejat 2
        goblinhl=pygame.image.load("images/goblinw/Hurt1.png").convert_alpha()
    
        
        #bola de foc
        foc1=pygame.image.load("images/goblinw/foc.png").convert_alpha()
    
        #monstres
        
        #POP
        monstruoimage1=pygame.image.load("images/goblinw/monstruo2.png").convert_alpha()
        monstruoimage3=pygame.image.load("images/goblinw/monstruo2_3.png").convert_alpha()
        monstruoimage4=pygame.image.load("images/goblinw/monstruo2_4.png").convert_alpha()
        monstruoimage5=pygame.image.load("images/goblinw/monstruo2_5.png").convert_alpha()
        monstruoimage6=pygame.image.load("images/goblinw/monstruo2_6.png").convert_alpha()
    
        #GUERRER DAURAT
        monstruo2image1=pygame.image.load("images/goblinw/guerrero9.png").convert_alpha()
        monstruo2image2=pygame.image.load("images/goblinw/guerrero9_2.png").convert_alpha()
        monstruo2image3=pygame.image.load("images/goblinw/guerrero9_3.png").convert_alpha()
        monstruo2image4=pygame.image.load("images/goblinw/guerrero9_4.png").convert_alpha()
        monstruo2image5=pygame.image.load("images/goblinw/guerrero9_5.png").convert_alpha()
        monstruo2image6=pygame.image.load("images/goblinw/guerrero9_6.png").convert_alpha()
        monstruo2image7=pygame.image.load("images/goblinw/guerrero9_7.png").convert_alpha()
        monstruo2image8=pygame.image.load("images/goblinw/guerrero9_8.png").convert_alpha()
        monstruo2image9=pygame.image.load("images/goblinw/guerrero9_9.png").convert_alpha()
    
        #monstre 3 (sNakE)
        monstruo3image1=pygame.image.load("images/goblinw/snake2.png").convert_alpha()
        monstruo3image2=pygame.image.load("images/goblinw/snake2_2.png").convert_alpha()
        monstruo3image3=pygame.image.load("images/goblinw/snake2.png").convert_alpha()
        monstruo3image4=pygame.image.load("images/goblinw/snake2_2.png").convert_alpha()
        monstruo3image5=pygame.image.load("images/goblinw/snake2.png").convert_alpha()
        monstruo3image6=pygame.image.load("images/goblinw/snake2_2.png").convert_alpha()
        monstruo3image7=pygame.image.load("images/goblinw/snake2.png").convert_alpha()
        monstruo3image8=pygame.image.load("images/goblinw/snake2_3.png").convert_alpha()
        monstruo3image9=pygame.image.load("images/goblinw/snake2_4.png").convert_alpha()
        monstruo3image10=pygame.image.load("images/goblinw/snake2_5.png").convert_alpha()
        monstruo3image11=pygame.image.load("images/goblinw/snake.png").convert_alpha()
    
        #imatges dels arbres
        tree1image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree2image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
        tree3image=pygame.image.load("images/goblinw/tree1.png").convert_alpha()
    
    
        #imatge eskut
        escut_i=pygame.image.load("images/goblinw/escudo_m.png").convert_alpha()
        
        
        
        #sprite del goblin
        sprite1=pygame.sprite.Sprite()
        sprite1.image=goblin1
        sprite1.rect=goblin1.get_rect()
        sprite1.rect.top=100
        sprite1.rect.left=50
    
        #sprite de la bola de foc
        spritefoc=pygame.sprite.Sprite()
        spritefoc.image=foc1
        spritefoc.rect=foc1.get_rect()
        spritefoc.rect.top=9999
        spritefoc.rect.left=9999
    
        #sprite de monstre pop 1
        spritemonstruo1=pygame.sprite.Sprite()
        spritemonstruo1.image=monstruoimage1
        spritemonstruo1.rect=monstruoimage1.get_rect()
        spritemonstruo1.rect.top=random.randrange(0,570)
        spritemonstruo1.rect.left=random.randrange(0,770)
    
        #sprite de monstre guerrer 2
        sger=pygame.sprite.Sprite()
        sger.image=monstruo2image1
        sger.rect=monstruo2image1.get_rect()
        sger.rect.top=random.randrange(0,570)
        sger.rect.left=random.randrange(0,770)
    
        #sprite del snake 3
        smonster=pygame.sprite.Sprite()
        smonster.image=monstruo3image1
        smonster.rect=monstruo3image1.get_rect()
        smonster.rect.top=random.randrange(0,570)
        smonster.rect.left=random.randrange(0,770)
    
        #sprite de leskut
        spritee=pygame.sprite.Sprite()
        spritee.image=escut_i
        spritee.rect=escut_i.get_rect()
        spritee.rect.top=sprite1.rect.top
        spritee.rect.left=sprite1.rect.left
    
        #sprites dels arbres
    
        #arbre 1 ########################################################
        #sa1=pygame.sprite.Sprite()
        #sa1.image=tree1image
        #sa1.rect=tree1image.get_rect()
        #sa1.rect.top=280
        #sa1.rect.left=60
    
        #sa2=pygame.sprite.Sprite()
        #sa2.image=tree1image
    #   sa2.rect=tree1image.get_rect()
        #sa2.rect.top=95
        #sa2.rect.left=372
    
        #sa3=pygame.sprite.Sprite()
        #sa3.image=tree1image
        #sa3.rect=tree1image.get_rect()
        #sa3.rect.top=350
        #sa3.rect.left=677
    
        #r_a1=pygame.Rect(87,320,10,30)
        #r_a2=pygame.Rect(400,135,10,30)
        #r_a3=pygame.Rect(705,392,10,30)
        
    
        #fuentes
        fuente1=pygame.font.SysFont("Arial",16,True,False)
        fuentevidapj=pygame.font.SysFont("Arial",25,True,False)
        fuenteGO=pygame.font.SysFont("Arial",70,True,False)
    
        
    
        #colors:
        rojo=(255,0,0)
        azul=(0,0,255)
        verde=(0,255,0)
        blanco=(255,255,255)
        negro=(0,0,0)
    
        #textos constants
        textoGO=fuenteGO.render('GAME OVER',0,rojo)
        textoV=fuenteGO.render('NIVEL COMPLETADO',0,azul)
        
    
        #altres variables i contadors
        cont5=0
        cont4=0
        cont3=0
        cont1=0
        cont2=0
        cont6=0
        cont11=0
        cont12=0
        cont13=0
        cont15=0
        cont16=0
        cont17=0
        cont18=0
        cont19=0
        cont20=0
        cont21=0
        cont22=0
        contx=0
        cont23=0
        cont24=0
        cont25=0
        contG=0
        contE1=0
        contE2=0
        contE3=0
        contC1=0
        contC2=0
        contC3=0
        cont_escudo=0
        cont_terremoto=0
        #########
        var1=1
        var2=0
        var3=True  #<---variable per saber si el monstre esta viu
        var3_2=True #<---variable per saber si el monstre 2 esta viu
        var3_3=False #<---variable per saber si el monster 3 esta viu
        var4=0
        vr3=var3
        vr3_2=var3_2
        vr3_3=var3_3
        var7=0
        var8=False # variable k indica si san matat prous pops per finalitzar el nivell
        var8_2=False
        var8_3=False
        var9=False
        var_c1=True
        var_c2=True
        var_c3=True
        var_escudo=False
        var_potion=False
        var_terremoto=False
    
        #variables per saber si sesta atacant o si sa tirat magia
        var_attack=False
        var_magia=False
    
        #vida monstres i pj
        hpmonstruo1=100
        hpmonstruo2=100
        hpmonstruo3=50
    
        #per llegir les pocions
        potionsreader=open('log\potions.txt')
        potionshp=int(potionsreader.readlines()[0])
        print 'potions hp: ', potionshp
        potionsreader.close()
        
        potionsreader=open('log\potions.txt')
        potionsmp=int(potionsreader.readlines()[1])
        print 'potions mp: ', potionsmp
        potionsreader.close()
    
    
    
    
    
    
    
    #escudo i atak terratremol
        tendareader=open('log/shop.txt')
        escudo=int(tendareader.readlines()[0])
        tendareader.close()
        print 'escudo', escudo
        
        tendareader=open('log/shop.txt')
        terremoto=int(tendareader.readlines()[1])
        tendareader.close()
        print 'terremoto', terremoto
        
    
    
    
    
        
    
    #per llegir el hp del pj:
        datosreader=open('log\datos.txt')
        hpdatos=int(datosreader.readlines()[0])
        print 'hp: ', hpdatos
        datosreader.close()
    
        hp_pj=hpdatos
        hpt_pj=hp_pj
    
        #variable del bucle principal
        salir=False
    
        #reloj
        reloj1=pygame.time.Clock()
    
        #grup de sprites de monstres
        grupo_m=pygame.sprite.Group(spritemonstruo1,sger,smonster)
    
        #mp del pj
    
        #per llegir el mp del pj:
    
        datosreader=open('log\datos.txt')
        mpdatos=int(datosreader.readlines()[1])
        print 'mp: ', mpdatos
        datosreader.close()
        
        mptpj=mpdatos
        mppj=mptpj
    
        #variable diners
        moneyreader=open('log\money.txt')
        money=int(moneyreader.readline())
        print 'dinero:', money
        moneyreader.close()
    
        money_t=str(money)
        moneywriter=open('log\money.txt','w')
        moneywriter.write(money_t)
        moneywriter.close()
    
        perdrediners=money
        
    
        sonido3.play()
    
    
        while salir != True:
            
            
            var_potion=False
    
            hp_pjant=hp_pj
    
            if hp_pj<=0 and var1==1:
                sprite1.image=goblindr
    
            if hp_pj<=0 and var1==2:
                sprite1.image=goblindl
                
    
            xant=sprite1.rect.left
            yant=sprite1.rect.top
    
            if hpmonstruo1<0:
                hpmonstruo1==0
            
            if hpmonstruo1==0:
                spritemonstruo1.image=monstruoimage3
    
    
    
            if hpmonstruo2<0:
                hpmonstruo2==0
            
            if hpmonstruo2==0:
                sger.image=monstruo2image9
    
                
    
            if hpmonstruo3<0:
                hpmonstruo3==0
            
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
                
    
            if hp_pj<0:
                hp_pj=0
                
    
    
            xmant1=smonster.rect.left
            ymant1=smonster.rect.top
            xmant2=sger.rect.left
            ymant2=sger.rect.top
            xmant3=spritemonstruo1.rect.left
            ymant3=spritemonstruo1.rect.top
    
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
                if event.type==pygame.KEYDOWN and hp_pj>0:
    
                    if event.key==pygame.K_LEFT and sprite1.rect.left>0:
                        if cont1==0:
                            sprite1.image=goblinwl1
                        if cont1==1:
                            sprite1.image=goblinwl2
                        if cont1==2:
                            sprite1.image=goblinwl3
                        if cont1==3:
                            sprite1.image=goblinwl4
                        if cont1==4:
                            sprite1.image=goblinwl3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left-=6
                        cont1+=1
                        var1=2
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
                        
    
                    if event.key==pygame.K_RIGHT and sprite1.rect.left<775:
                        if cont1==0:
                            sprite1.image=goblinwr1
                        if cont1==1:
                            sprite1.image=goblinwr2
                        if cont1==2:
                            sprite1.image=goblinwr3
                        if cont1==3:
                            sprite1.image=goblinwr4
                        if cont1==4:
                            sprite1.image=goblinwr3
                        if cont1>=4:
                            cont1=0
                        sprite1.rect.left+=6
                        cont1+=1
                        var1=1
                        var4=0
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_UP and sprite1.rect.top>0:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
                            
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top-=6
                        cont1+=1
                        var4=1
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_DOWN and sprite1.rect.top<555:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinwr1
                            if cont1==1:
                                sprite1.image=goblinwr2
                            if cont1==2:
                                sprite1.image=goblinwr3
                            if cont1==3:
                                sprite1.image=goblinwr4
                            if cont1==4:
                                sprite1.image=goblinwr3
                            if cont1>=4:
                                cont1=0
    
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinwl1
                            if cont1==1:
                                sprite1.image=goblinwl2
                            if cont1==2:
                                sprite1.image=goblinwl3
                            if cont1==3:
                                sprite1.image=goblinwl4
                            if cont1==4:
                                sprite1.image=goblinwl3
                            if cont1>=4:
                                cont1=0
                            
                        sprite1.rect.top+=6
                        cont1+=1
                        var4=2
                        if cont18%3==0:
                            sonidorun.play()
    
                    if event.key==pygame.K_SPACE:
                        if var1==1:
                            if cont1==0:
                                sprite1.image=goblinar2
                            if cont1==1:
                                sprite1.image=goblinar1
                            if cont1==2:
                                sprite1.image=goblinar1
                            if cont1==3:
                                sprite1.image=goblinar2
                            if cont1==4:
                                sprite1.image=goblinar3
                            if cont1>=5:
                                cont1=0
                                sprite1.image=goblinar2
                        if var1==2:
                            if cont1==0:
                                sprite1.image=goblinal2
                            if cont1==1:
                                sprite1.image=goblinal1
                            if cont1==2:
                                sprite1.image=goblinal2
                            if cont1==3:
                                sprite1.image=goblinal3
                            if cont1>=4:
                                cont1=0
                                sprite1.image=goblinal2
                                
                        cont1+=1
                        var_attack=True
                        if cont1%2==0:
                            sonidoespadaF.play()
    
                        
                            
    
                        
                    if event.key==pygame.K_m:
                        if cont2<=3:
                            if var1==1:
                                sprite1.image=goblinamr
                            if var1==2:
                                sprite1.image=goblinaml
                        if cont2==4:
                            if var1==1:
                                sprite1.image=goblin1
                            if var1==2:
                                sprite1.image=goblin2
                        if cont2==1 and mppj>=20:
                            var_magia=True
                        cont2+=1
    
                    if event.key==pygame.K_h and potionshp>0 and hp_pj>0:
                        if hp_pj<hpt_pj:
                            potionshp-=1
                            hp_pj+=random.randrange(15,20)
                            var_potion=True
                            
                            sopotion.play()
                            print 'potionshp: ', potionshp
                            if hp_pj>hpt_pj:
                                hp_pj=hpt_pj
    
                    if event.key==pygame.K_j and potionsmp>0 and hp_pj>0:
                        if mppj<mptpj:
                            potionsmp-=1
                            mppj+=random.randrange(10,20)
                            sopotion.play()
                            print 'potionsmp: ', potionsmp
                            
                            if mppj>mptpj:
                                mppj=mptpj
    
                    if event.key==pygame.K_n and escudo==1 and hp_pj>0 and mppj>=60:
                        mppj-=60
                        var_escudo=True
                        print 'escudo activado'
                    
                    if event.key==pygame.K_b and terremoto==1 and hp_pj>0 and mppj>=250 and var_terremoto==False:
                        mppj-=250
                        var_terremoto=True
                        print 'terremoto activado'
    
                    
    
                    if event.key==pygame.K_ESCAPE:
                        sonido3.stop()
                        menu1()
                            
                            
                    
                if event.type==pygame.KEYUP and hp_pj>0:
                    if var1==1:
                        sprite1.image=goblin1
                    if var1==2:
                        sprite1.image=goblin2
                        
                    var_attack=False
                    cont2=0
                    cont1=0
                    
    
            reloj1.tick(17)
            
            
            pantalla.blit(fondo,(0,0))
            if var_terremoto==True:
                if var3==True:
                    hpmonstruo1=0
                if var3_2==True:
                    hpmonstruo2=0
                if var3_3==True and var7==1:
                    hpmonstruo3=0
                s_terremoto.play()
                cont_terremoto+=1
                if cont_terremoto%2==0:
                    pantalla.blit(fondo,(random.randrange(0,5),random.randrange(0,5)))
                else:
                    pantalla.blit(fondo,(0,0))
            if cont_terremoto==10:
                var_terremoto=False
                cont_terremoto=0
    
            pantalla.blit(sprite1.image,sprite1.rect)
    
            
    
            if var3==True:
                pantalla.blit(spritemonstruo1.image,spritemonstruo1.rect)
    
    
            if var3_2==True:
                pantalla.blit(sger.image,sger.rect)
    
            
            
            #MOVIMENTS DEL MONSTRE 1 (pop)
                
            if var3==True and hpmonstruo1>0 and hp_pj>0:
                variable1=random.randrange(0,5)
    
    
                if variable1==0 or variable1==1:
                    if spritemonstruo1.rect.left<770 and sprite1.rect.left>spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left+=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage5
                if variable1==1 or variable1==2:
                    if spritemonstruo1.rect.top<570 and sprite1.rect.top>spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top+=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage1
                if variable1==2 or variable1==3:
                    if spritemonstruo1.rect.top>15 and sprite1.rect.top<spritemonstruo1.rect.top:
                        spritemonstruo1.rect.top-=random.randrange(0,15)
                        spritemonstruo1.image=monstruoimage6
                if variable1==3 or variable1==0:
                    if spritemonstruo1.rect.left>15 and sprite1.rect.left<spritemonstruo1.rect.left:
                        spritemonstruo1.rect.left-=random.randrange(0,20)
                        spritemonstruo1.image=monstruoimage4
    
            #MOVIMENTS DEL MONSTRE 2 (guerrer daurat)
                
            if var3_2==True and hpmonstruo2>0 and hp_pj>0:
                variable1_2=random.randrange(0,5)
    
    
                if variable1_2==0 or variable1_2==1:
                    if sger.rect.left<770 and sprite1.rect.left>sger.rect.left:
                        sger.rect.left+=random.randrange(0,10)
                        sger.image=monstruo2image2
                if variable1_2==1 or variable1_2==2:
                    if sger.rect.top<570 and sprite1.rect.top>sger.rect.top:
                        sger.rect.top+=random.randrange(0,7)
                        sger.image=monstruo2image1
                if variable1_2==2 or variable1_2==3:
                    if sger.rect.top>15 and sprite1.rect.top<sger.rect.top:
                        sger.rect.top-=random.randrange(0,7)
                        sger.image=monstruo2image6
                if variable1_2==3 or variable1_2==0:
                    if sger.rect.left>15 and sprite1.rect.left<sger.rect.left:
                        sger.rect.left-=random.randrange(0,10)
                        sger.image=monstruo2image1
    
            
                        
                        
            #"INVOCACIO" BOLA DE FOC
                        
            if var_magia==True and cont5==0 and mppj>20:
                #sprite de la bola de foc
                spritefoc=pygame.sprite.Sprite()
                spritefoc.image=foc1
                spritefoc.rect=foc1.get_rect()
                if var4==0:
                    spritefoc.rect.top=sprite1.rect.top+5
                if var4==1 or var4==2:
                    spritefoc.rect.left=sprite1.rect.left+5
    
                if var1==1 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left+20
                if var1==2 and var4==0:
                    spritefoc.rect.left=sprite1.rect.left-20
                if var4==1:
                    spritefoc.rect.top=sprite1.rect.top-20
                if var4==2:
                    spritefoc.rect.top=sprite1.rect.top+20
    
                mppj-=20
                sonido2.play()
                cont5+=1
    
            #MOVIMENTS BOLA DE FOC
            if var_magia==True:
                pantalla.blit(spritefoc.image,spritefoc.rect)
                if cont3==0:
                    cont3+=1
                    if var1==1 and var4==0:
                        var2=1
                    if var1==2 and var4==0:
                        var2=2
                    if var4==1:
                        var2=3
                    if var4==2:
                        var2=4
    
                if cont3>0 and cont4<70:
                    if var2==1:
                        spritefoc.rect.left+=10
                    if var2==2:
                        spritefoc.rect.left-=10
                    if var2==3:
                        spritefoc.rect.top-=10
                    if var2==4:
                        spritefoc.rect.top+=10
                    cont4+=2
    
            if spritefoc.rect.left<0 or spritefoc.rect.left>800 or cont4>=70:
                var_magia=False
                
            if var_magia==False:
                cont3=0
                cont4=0
                cont5=0
                spritefoc.rect.top=99999
                spritefoc.rect.left=99999
    
    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
            var_attackconfirm_l=sprite1.rect.left-spritemonstruo1.rect.left
            var_attackconfirm_t=sprite1.rect.top-spritemonstruo1.rect.top
    
            var_attackconfirm_l_2=sprite1.rect.left-sger.rect.left
            var_attackconfirm_t_2=sprite1.rect.top-sger.rect.top
    
    #accions que infringeixen dany al monstre (pop)
            
            if var3==True:
                if spritefoc.rect.colliderect(spritemonstruo1) and hpmonstruo1>0:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(5,15)
                    if hpmonstruo1<0:
                        hpmonstruo1==0
            
                if var1==1 and var_attackconfirm_l>-20 and var_attackconfirm_l<10 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left+10,spritemonstruo1.rect.left+30)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
                if var1==2 and var_attackconfirm_l>-10 and var_attackconfirm_l<20 and var_attackconfirm_t>-20 and var_attackconfirm_t<20 and hpmonstruo1>0 and var_attack==True:
                    spritemonstruo1.rect.top=random.randrange(spritemonstruo1.rect.top-30,spritemonstruo1.rect.top+30)
                    spritemonstruo1.rect.left=random.randrange(spritemonstruo1.rect.left-30,spritemonstruo1.rect.left-10)
                    hpmonstruo1-=random.randrange(15,25)
                    sonidoespada.play()
                    if hpmonstruo1<0:
                        hpmonstruo1=0
    
    
    #accions que infringeixen dany al monstre (guerrer)
            
            if var3_2==True:
                if spritefoc.rect.colliderect(sger) and hpmonstruo2>0:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(1,4)
                    if hpmonstruo2<0:
                        hpmonstruo2==0
            
                if var1==1 and var_attackconfirm_l_2>-25 and var_attackconfirm_l_2<20 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left+10,sger.rect.left+30)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
                if var1==2 and var_attackconfirm_l_2>-20 and var_attackconfirm_l_2<25 and var_attackconfirm_t_2>-25 and var_attackconfirm_t_2<25 and hpmonstruo2>0 and var_attack==True:
                    sger.rect.top=random.randrange(sger.rect.top-30,sger.rect.top+30)
                    sger.rect.left=random.randrange(sger.rect.left-30,sger.rect.left-10)
                    hpmonstruo2-=random.randrange(5,15)
                    sonidoespada.play()
                    if hpmonstruo2<0:
                        hpmonstruo2=0
    
    
    
    #accions que infringeixen dany al pj (pop)
                        
            if var3==True and spritemonstruo1.rect.colliderect(sprite1.rect) and hpmonstruo1>0 and hp_pj>0:
                hp_pj-=random.randrange(0,2)
                sprite1.rect.left-=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo1<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
    
    #accions que infringeixen dany al pj (guerrer d)
                        
            if var3_2==True and sger.rect.colliderect(sprite1.rect) and hpmonstruo2>0 and hp_pj>0:
                hp_pj-=random.randrange(1,4)
                sprite1.rect.left+=random.randrange(-5,5)
                sprite1.rect.top+=random.randrange(-5,5)
    
                if var1==1:
                    sprite1.image=goblinhr
                if var1==2:
                    sprite1.image=goblinhl
    
            if hpmonstruo2<0:
                hpmonstruo1==0
    
    
            hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
            textohppj=fuente1.render(hppjt,0,verde)
            pantalla.blit(textohppj,(5,5))
    
            
    
    #axo serveix perk no senkalli el pj en matar el monstre
            #if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6<50 and hpmonstruo1==0:
             #   sprite1.rect.left+=10
                
            #if sprite1.rect.colliderect(sger.rect) and cont6<50 and hpmonstruo2==0:
             #   sprite1.rect.left+=10
            
    #vida dels monstres          
            if var3==True:       
                hpm1=str(str(hpmonstruo1)+'/100')
    
            if var3_2==True:
                hpm2=str(str(hpmonstruo2)+'/100')
    
    #per fer desaparexer el pop un kop mort:
            if hpmonstruo1<=0 and cont6<70:
                hpmonstruo1=0
                cont6+=1
                if cont6==70:
                    cont6=0
                    var3=False
                    spritemonstruo1.rect.top=9999
                    spritemonstruo1.rect.left=9999
    
    #per fer desaparexer el guerrer un kop mort:
            if hpmonstruo2<=0 and cont15<70:
                hpmonstruo2=0
                cont15+=1
                if cont15==70:
                    cont15=0
                    var3_2=False
                    sger.rect.top=9999
                    sger.rect.left=9999
    
    
    #imprimacio de la vida dels monstres
            #pop       
            if var3==True:
                textohp1=fuente1.render(hpm1,0,rojo)
                pantalla.blit(textohp1,(spritemonstruo1.rect.left-10,spritemonstruo1.rect.top-25))
    
            #guerrer
            if var3_2==True:
                textohp2=fuente1.render(hpm2,0,rojo)
                pantalla.blit(textohp2,(sger.rect.left-10,sger.rect.top-25))
    
    
    #sistema k fa k el pj no travessi el monstre
            if hpmonstruo1==0:
                if sprite1.rect.colliderect(spritemonstruo1.rect) and cont6>10 and var_c1==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
            if hpmonstruo2==0:
                if sprite1.rect.colliderect(sger.rect) and cont6>10 and var_c2==True:
                    sprite1.rect.left=xant
                    sprite1.rect.top=yant
    
    
    
            if var3==False and cont11==0:
                cont6=0
                cont11+=1
    
            if var3==False and cont12==0:
                cont6=0
                cont12+=1
    
            if hp_pj==0:
                cont13+=1
    
            if cont13==50:
                sonido3.stop()
                menu1()
    
            if hp_pj<=0:
                pantalla.blit(textoGO,(200,200))
                if cont13==1:
                    sonidodead.play()
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                elif cont13==20:
                    sonidodead.stop()
                
    
    #per saber si sa akabat el nivell:
            if var8==True and var8_2==True and var8_3==True:
                pantalla.blit(textoV,(115,200))
                cont16+=1
                var9=True
                if cont16==60:
                    datoswriter=open('log/potions.txt','w')
                    datoswriter.write(str(potionshp)+'\n'+str(potionsmp))
                    datoswriter.close()
                    sonido3.stop()
                    menu1()
    
    
                
                
            
    ###############################################################################
    ###############################################################################
    
    
            if vr3==False or vr3_2==False:
                    var7=1
                #si el monstre esta viu la imatge simprimex en la pantalla
                    
            if var7==1:
                if var3_3==True:
                    pantalla.blit(smonster.image,smonster.rect)
                    
    
                    #moviments
                        
                    if var3_3==True and hpmonstruo3>0 and hp_pj>0:
                        variable1_3=random.randrange(0,5)
    
                        
                        
                        if variable1_3==0 or variable1_3==1:
                            if smonster.rect.left<770 and sprite1.rect.left>smonster.rect.left:
                                smonster.rect.left+=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image5
                                if variable1_3==1:
                                    smonster.image=monstruo3image8
                        if variable1_3==1 or variable1_3==2:
                            if smonster.rect.top<570 and sprite1.rect.top>smonster.rect.top:
                                smonster.rect.top+=random.randrange(0,25)
                                if variable1_3==0:
                                    smonster.image=monstruo3image5
                                if variable1_3==1:
                                    smonster.image=monstruo3image8
                        if variable1_3==2 or variable1_3==3:
                            if smonster.rect.top>15 and sprite1.rect.top<smonster.rect.top:
                                smonster.rect.top-=random.randrange(0,25)
                                if variable1_3==0:
                                    smonster.image=monstruo3image4
                                if variable1_3==1:
                                    smonster.image=monstruo3image9
                        if variable1==3 or variable1_3==0:
                            if smonster.rect.left>15 and sprite1.rect.left<smonster.rect.left:
                                smonster.rect.left-=random.randrange(0,30)
                                if variable1_3==0:
                                    smonster.image=monstruo3image4
                                if variable1_3==3:
                                    smonster.image=monstruo3image9
    
            
    
    
    
                    #variable que defineix si el personatge golpeja el monstre segons la distancia a la que estiguin
                    var_attackconfirm_l_3=sprite1.rect.left-smonster.rect.left
                    var_attackconfirm_t_3=sprite1.rect.top-smonster.rect.top
    
                #accions que infringeixen dany al monstre (snake)
    
                    if var3_3==True:
                        if spritefoc.rect.colliderect(smonster) and hpmonstruo3>0:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(5,15)
                            if hpmonstruo3<0:
                                hpmonstruo3==0
    
                        if var1==1 and var_attackconfirm_l_3>-20 and var_attackconfirm_l_3<10 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left+10,smonster.rect.left+30)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
                        if var1==2 and var_attackconfirm_l_3>-10 and var_attackconfirm_l_3<20 and var_attackconfirm_t_3>-20 and var_attackconfirm_t_3<20 and hpmonstruo3>0 and var_attack==True:
                            smonster.rect.top=random.randrange(smonster.rect.top-30,smonster.rect.top+30)
                            smonster.rect.left=random.randrange(smonster.rect.left-30,smonster.rect.left-10)
                            hpmonstruo3-=random.randrange(15,25)
                            sonidoespada.play()
                            if hpmonstruo3<0:
                                hpmonstruo3=0
    
    
    
                    #accions que infringeixen dany al pj (snake)
                                
                    if var3_3==True and smonster.rect.colliderect(sprite1.rect) and hpmonstruo3>0 and hp_pj>0:
                        hp_pj-=random.randrange(0,2)
                        sprite1.rect.left-=random.randrange(-5,5)
                        sprite1.rect.top+=random.randrange(-5,5)
    
                        if var1==1:
                            sprite1.image=goblinhr
                        if var1==2:
                            sprite1.image=goblinhl
    
                    if hpmonstruo3<0:
                        hpmonstruo3==0
    
    
                    hppjt=str('HP: '+str(hp_pj)+'/'+str(hpt_pj))
                    textohppj=fuente1.render(hppjt,0,verde)
                    pantalla.blit(textohppj,(5,5))
    
    
                    #axo serveix perk no senkalli el pj en matar el monstre
                    #if sprite1.rect.colliderect(smonster.rect) and cont6<50 and hpmonstruo3==0:
                     #   sprite1.rect.left+=10
                        
    
                    #vida dels monstres          
                    if var3_3==True:       
                        hpm3=str(str(hpmonstruo3)+'/50')
    
                    #per fer desaparexer el snake un kop mort:
                    
                    if hpmonstruo3<=0 and cont17<70:
                        hpmonstruo3=0
                        cont17+=1
                        if cont17==70:
                            cont17=0
                            var3_3=False
                            smonster.rect.top=9999
                            smonster.rect.left=9999
    
    
                    #imprimacio de la vida dels monstres       
                    if var3_3==True:
                        textohp1=fuente1.render(hpm3,0,rojo)
                        pantalla.blit(textohp1,(smonster.rect.left-10,smonster.rect.top-25))
    
    
                    #sistema k fa k el pj no travessi el monstre
                    if hpmonstruo3==0:
                        if sprite1.rect.colliderect(smonster.rect) and cont6>10 and var_c3==True:
                            sprite1.rect.left=xant
                            sprite1.rect.top=yant
    
                    
    
    
    
    
                    if var3_3==False and cont11==0:
                        cont6=0
                        cont11+=1
    
                    if var3_3==False and cont12==0:
                        cont6=0
                        cont12+=1
    
    
    
            vr3=var3
            vr3_2=var3_2
            vr3_3=var3_3
    
            
    
    
    #si el pop esta mort i sa mort menys de 4 vegades torna a aparexer depen del resultat de f
            if vr3==False and cont19<4:
                f=1
                if f==1:
                    spritemonstruo1=pygame.sprite.Sprite()
                    spritemonstruo1.image=monstruoimage1
                    spritemonstruo1.rect=monstruoimage1.get_rect()
                    spritemonstruo1.rect.top=random.randrange(0,570)
                    spritemonstruo1.rect.left=random.randrange(0,770)
                    hpmonstruo1=100
                    cont6=0
                    var3=True
                    cont19+=1
                    cont23=0
            if cont19==4 and var3==False:
                var8=True
                
    #
            if vr3_2==False and cont20<4:
                f2=1
                if f2==1:
                    sger=pygame.sprite.Sprite()
                    sger.image=monstruo2image1
                    sger.rect=monstruo2image1.get_rect()
                    sger.rect.top=random.randrange(0,570)
                    sger.rect.left=random.randrange(0,770)
                    hpmonstruo2=100
                    cont6=0
                    var3_2=True
                    cont20+=1
                    cont24=0
            if cont20==4 and var3_2==False:
                var8_2=True
    
    
    
            if vr3_3==False and cont21<6:
                f3=1
                if f3==1:
                    smonster=pygame.sprite.Sprite()
                    smonster.image=monstruo3image1
                    smonster.rect=monstruo3image1.get_rect()
                    smonster.rect.top=random.randrange(0,570)
                    smonster.rect.left=random.randrange(0,770)
                    hpmonstruo3=50
                    cont6=0
                    var3_3=True
                    cont21+=1
                    cont25=0
            if cont21==6 and var3_3==False:
                var8_3=True
    
                
    ####AKI ANIRA LU MATEX K LU DEL POP AM ELS ALTRES 2 MONSTRES
    
    #per k es recargi el mp:
            cont18+=1
            if cont18%10==0 and mppj<mpdatos:
                mppj+=1
        
    #imprimacio del mp:
            mppjt=str('MP: '+str(mppj)+'/'+str(mptpj))
            textomppj=fuente1.render(mppjt,0,verde)
            pantalla.blit(textomppj,(700,5))
    
            if hpmonstruo3==0:
                smonster.image=monstruo3image10
    
    
    #per guardar la kantitat de diners i desblokejar el seguen nivell si sa completat la misio
            if var9==True:
                money_t=str(money)
                moneywriter=open('log\money.txt','w')
                moneywriter.write(money_t)
                moneywriter.close()
            
                moneyreader=open('log\money.txt')
                money=int(moneyreader.readline())
                moneyreader.close()
    
                if mision==7:
                    misionwriter=open('log\misions.txt','w')
                    misionwriter.write('8')
                    misionwriter.close()
    
            
    
    #per sumar diners al matar els monstres:
            if cont23==0 and hpmonstruo1==0:
                cont23+=1
                money+=random.randrange(15,27)
                print 'dinero:', money
    
            if cont24==0 and hpmonstruo2==0:
                cont24+=1
                money+=random.randrange(36,46)
                print 'dinero:', money
    
            if cont25==0 and hpmonstruo3==0:
                cont25+=1
                money+=random.randrange(14,19)
                print 'dinero:', money
    
                
                
    
            if hp_pj==0:
                money=perdrediners
                
                if contx==0:
                    print 'dinero: ', money
                    contx+=1
    
            tttmoney=str('Dinero: '+str(money))
            textomoney=fuente1.render(tttmoney,0,verde)
            pantalla.blit(textomoney,(200,5))
    
            misionreader=open('log\misions.txt')
            mision=int(misionreader.readline())
            misionreader.close()
    
        
            #if sprite1.rect.colliderect(r_a1) or sprite1.rect.colliderect(r_a2) or sprite1.rect.colliderect(r_a3):     
             #   sprite1.rect.left=xant
              #  sprite1.rect.top=yant
    
    #prk el pj no surti del mapa:
            if sprite1.rect.left<=0:
                sprite1.rect.left=0
            if sprite1.rect.top<=0:
                sprite1.rect.top=0
            if sprite1.rect.left>=780:
                sprite1.rect.left=780
            if sprite1.rect.top>=550:
                sprite1.rect.top=550
    
    #prk els monstres no chokin am les palmeras:
            #if smonster.rect.colliderect(r_a1) or smonster.rect.colliderect(r_a2) or smonster.rect.colliderect(r_a3):
             #   smonster.rect.left=xmant1
              #  smonster.rect.top=ymant1
               # contE3+=1
            #else:
             #   contE3=0
            #if sger.rect.colliderect(r_a1) or sger.rect.colliderect(r_a2) or sger.rect.colliderect(r_a3):
            #    sger.rect.left=xmant2
             #   sger.rect.top=ymant2
             #   contE2+=1
            #else:
           #     contE2=0
            #if spritemonstruo1.rect.colliderect(r_a1) or spritemonstruo1.rect.colliderect(r_a2) or spritemonstruo1.rect.colliderect(r_a3):
             #   spritemonstruo1.rect.left=xmant3
              #  spritemonstruo1.rect.top=ymant3
               # contE1+=1
            #else:
             #   contE1=0
    
            #imprimacio dels arbres
            #pantalla.blit(sa1.image,sa1.rect)
            #pantalla.blit(sa2.image,sa2.rect)
            #pantalla.blit(sa3.image,sa3.rect)
    
    #perk el pj no senkalli am els monstres:
            if hpmonstruo1==0 and sprite1.rect.colliderect(spritemonstruo1)==False:
                var_c1=True
            if hpmonstruo2==0 and sprite1.rect.colliderect(sger)==False:
                var_c2=True
            if hpmonstruo3==0 and sprite1.rect.colliderect(smonster)==False:
                var_c3=True
    
            if hpmonstruo1>0:
                var_c1=False
            if hpmonstruo2>0:
                var_c2=False
            if hpmonstruo3>0:
                var_c3=False
    
    #per si el monstre aparex sobre un arbre k es mogi per no enkallarse
            #X
    
    #perk kridin els monstres kuan morin:
            if hpmonstruo1==0 and contC1==0:
                sonidocrit1.play()
                contC1+=1
            if hpmonstruo1>0:
                contC1=0
    
            if hpmonstruo2==0 and contC2==0:
                sonidocrit2.play()
                contC2+=1
            if hpmonstruo2>0:
                contC2=0
    
            if hpmonstruo3==0 and contC3==0:
                sonidocrit3.play()
                contC3+=1
            if hpmonstruo3>0:
                contC3=0
    
            #textos pocions:
            potionhpt=str('Pociones HP: '+str(potionshp))
            potionmpt=str('Pociones MP: '+str(potionsmp))
            textohpp=fuente1.render(potionhpt,0,verde)
            textompp=fuente1.render(potionmpt,0,verde)
            pantalla.blit(textohpp,(350,5))
            pantalla.blit(textompp,(500,5))
    
    
            if var_escudo==True:
                spritee.rect.top=sprite1.rect.top-15
                spritee.rect.left=sprite1.rect.left-25
            else:
                spritee.rect.top=999999
                spritee.rect.left=999999
    
            if var_escudo==True:
                cont_escudo+=1
                
            if var_escudo==True and var_potion==False:
                hp_pj=hp_pjant
    
            if cont_escudo==100:
                var_escudo=False
                cont_escudo=0
            
            
                
    
            
            
    
            pantalla.blit(spritee.image,spritee.rect)
            
            #per fer k leskut giri :)
            if var_escudo==True:
                escut_i=pygame.transform.rotate(escut_i, 90)
                spritee.image=escut_i
    
            contG+=1
            
            pygame.display.update()
        pygame.quit()
    
    
    menu1()
    pygame.quit()

except:
    print "hubo un error al cargar una superficie"




