import pygame, random

pygame.init()

pantalla = pygame.display.set_mode ((500, 500))

fuente = pygame.font.Font(None, 30)

fuente_titulo = pygame.font.Font(None, 50)

fps = pygame.time.Clock()


def food():
    return [random.randint(0, 49) * 10, random.randint(0, 49) * 10]

def pantalla_inicio():
    pantalla.fill((0, 0, 0))
    
    titulo = fuente_titulo.render("El Gusanito Juan", True, (255, 255, 255))
    pantalla.blit(titulo, (110, 150))
    
    boton_rect = pygame.Rect(200, 300, 100, 50)
    pygame.draw.rect(pantalla, (0, 255, 0), boton_rect)
    
    texto_boton = fuente.render("Iniciar", True, (0, 0, 0))
    pantalla.blit(texto_boton, (220, 315))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(event.pos):
                    return  # Regresa a la función main para iniciar el juego

def game_over(puntaje):
    pantalla.fill((0, 0, 0))
    
    texto_game_over = fuente.render("Pinche Manco", True, (255, 0, 0))
    pantalla.blit(texto_game_over, (200, 200))
    
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto_puntaje, (210, 240))
    
    boton_rect = pygame.Rect(200, 300, 100, 50)
    pygame.draw.rect(pantalla, (0, 255, 0), boton_rect)
    
    texto_boton = fuente.render("Reiniciar", True, (0, 0, 0))
    pantalla.blit(texto_boton, (210, 310))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(event.pos):
                    return True  # Reinicia el juego

def main():

    while True:
        pantalla_inicio()  # Muestra la pantalla de inicio antes de comenzar el juego

        snake_pos = [100, 50]
        snake_body = [[100, 50],[90,50],[80,50]]
        direccion = "RIGHT"
        run = True
        food_pos = food()
        puntaje = 0 

        while run: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        direccion = "RIGHT"
                    if event.key == pygame.K_a:
                        direccion = "LEFT"
                    if event.key == pygame.K_w:
                        direccion = "UP"
                    if event.key == pygame.K_s:
                        direccion = "DOWN"
            if direccion == "RIGHT":
                snake_pos[0] += 10
            if direccion == "LEFT":
                snake_pos[0] -= 10
            if direccion == "UP":
                snake_pos[1] -= 10
            if direccion == "DOWN":
                snake_pos[1] += 10

            snake_body.insert(0, list(snake_pos))
            if snake_pos == food_pos:
                food_pos = food()
                puntaje += 1
                print(puntaje)
            else:
                snake_body.pop()



            pantalla.fill((0, 128, 0))


            for pos in snake_body:
                pygame.draw.rect(pantalla,(255, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
            
            pygame.draw.rect(pantalla,(255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
            texto = fuente.render(str(puntaje), 0, (255, 255, 255))
            pantalla.blit(texto,(450,20))

            if puntaje < 10:
                fps.tick(10)
            elif puntaje >= 10:
                fps.tick(20)

            if snake_pos[0] < 0 or snake_pos[0] >= 500 or snake_pos[1] < 0 or snake_pos[1] >= 500:
                run = False
                print("pinche manco")

            if snake_pos in snake_body[1:]:
                run = False
                print("pinche manco")

    
            pygame.display.flip()

            if not run:
                if game_over(puntaje):
                    main()  # Reinicia el juego
            

main ()

pygame.quit()
