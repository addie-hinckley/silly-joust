
import pygame, sys, player, platform1


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 400))
    fps = pygame.time.Clock()
    pygame.display.set_caption("siLlY jOUsT")

    text_font = pygame.font.Font("Fonts/Pixeltype.ttf", 50)

    sky_surface = pygame.image.load("Graphics/Backgrounds/bg_shroom.png")
    text_surface = text_font.render("siLlY jOUsT", False, "#000000AB")
    text_box = text_surface.get_rect(midtop = (400, 30))

    #platforms
    platforms = pygame.sprite.Group()
    platforms.add(platform1.Platform1((0, 328), (800, 2), "#1B6305FF"))
    platforms.add(platform1.Platform1((300, 255), (200, 10), "#1B6305FF"))
    platforms.add(platform1.Platform1((300, 80), (200, 10), "#1B6305FF"))
    platforms.add(platform1.Platform1((0, 155), (200, 10), "#1B6305FF"))
    platforms.add(platform1.Platform1((600, 155), (200, 10), "#1B6305FF"))

    player1_surface = pygame.image.load("Graphics/Enemies/1flyFly1.png")
    player1_surface = pygame.transform.flip(player1_surface, True, False)

    player1 = pygame.sprite.GroupSingle()
    player1.add(player.Player(1, player1_surface, (200, 200), 3))

    ground_surface = pygame.image.load("Graphics/ground2.png")

    # while loop is game logic and in the game
    while True:
        for event in pygame.event.get():

            # to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player1.sprite.is_moving_right = True

                if event.key == pygame.K_a:
                    player1.sprite.is_moving_left = True
                
                if event.key == pygame.K_w:
                    player1.sprite.player_jump()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player1.sprite.is_moving_right = False

                if event.key == pygame.K_a:
                    player1.sprite.is_moving_left = False
                    
            #Move the player
        if player1.sprite.is_moving_right: player1.sprite.move_right()
        if player1.sprite.is_moving_left: player1.sprite.move_left()


        player1.sprite.apply_gravity()

        if player1.sprite.rect.bottom >= 330:
            player1.sprite.rect.bottom = 330


        platforms_collide = pygame.sprite.spritecollideany(player1.sprite, platforms)
        if (platforms_collide):

            if player1.sprite.rect.centery > platforms_collide.rect.centery:
                player1.sprite.rect.top = platforms_collide.rect.bottom

            elif player1.sprite.rect.centery < platforms_collide.rect.centery:
                player1.sprite.rect.bottom = platforms_collide.rect.top
            
            



        #draw things onto screen     POSITIVE Y GOES DOWN IN THIS CASE
        screen.blit(sky_surface, (0,0))
        screen.blit(text_surface, text_box)
        screen.blit(ground_surface, (0, 330))


        player1.draw(screen)

        platforms.draw(screen)

        pygame.display.update()

        fps.tick(60)


if __name__ == "__main__":
    main()