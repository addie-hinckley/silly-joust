import pygame, sys, player, platform1, random


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 400))
    fps = pygame.time.Clock()
    pygame.display.set_caption("siLlY jOUsT")
    player1_score = 0
    player2_score = 0

    text_font = pygame.font.Font("Fonts/Pixeltype.ttf", 50)

    sky_surface = pygame.image.load("Graphics/Backgrounds/bg_shroom.png")
    text_surface = text_font.render("siLlY jOUsT", False, "#000000AB")
    text_box = text_surface.get_rect(midtop = (400, 30))

    #platforms
    platforms = pygame.sprite.Group()
    platforms.add(platform1.Platform1((300, 255), (200, 10), "#1B6305FF"))
    platforms.add(platform1.Platform1((300, 80), (200, 10), "#1B6305FF"))
    platforms.add(platform1.Platform1((0, 155), (200, 10), "#1B6305FF"))
    platforms.add(platform1.Platform1((600, 155), (200, 10), "#1B6305FF"))

    player1_surface = pygame.image.load("Graphics/Enemies/1flyFly1.png")

    player1 = pygame.sprite.GroupSingle()
    player1.add(player.Player(1, player1_surface, (200, 200), 3))


    player2_surface = pygame.image.load("Graphics/Enemies/2flyFly1.png")

    player2 = pygame.sprite.GroupSingle()
    player2.add(player.Player(2, player2_surface, (500, 200), 3))



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
                    player1.sprite.is_looking_right = True
                    

                if event.key == pygame.K_a:
                    player1.sprite.is_moving_left = True
                    player1.sprite.is_looking_right = False
                
                if event.key == pygame.K_w:
                    player1.sprite.player_jump()

                    # player 2
                if event.key == pygame.K_RIGHT:
                    player2.sprite.is_moving_right = True
                    player2.sprite.is_looking_right = True

                if event.key == pygame.K_LEFT:
                    player2.sprite.is_moving_left = True
                    player2.sprite.is_looking_right = False
                
                if event.key == pygame.K_UP:
                    player2.sprite.player_jump()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player1.sprite.is_moving_right = False

                if event.key == pygame.K_a:
                    player1.sprite.is_moving_left = False

                if event.key == pygame.K_RIGHT:
                    player2.sprite.is_moving_right = False

                if event.key == pygame.K_LEFT:
                    player2.sprite.is_moving_left = False
                    
            #Move the player
        if player1.sprite.is_moving_right: player1.sprite.move_right()
        if player1.sprite.is_moving_left: player1.sprite.move_left()


#------------------------------------------------GRAVITY----------------

        player1.sprite.apply_gravity()

        if player1.sprite.rect.bottom >= 330:
            player1.sprite.rect.bottom = 330
        
        #left
        if player1.sprite.rect.left <= 0:
            player1.sprite.rect.left = 0
        #Right
        if player1.sprite.rect.right >= 800:
            player1.sprite.rect.right = 800
        #top
        if player1.sprite.rect.top <= 0:
            player1.sprite.rect.top = 0


        player2.sprite.apply_gravity()

        if player2.sprite.rect.bottom >= 330:
            player2.sprite.rect.bottom = 330

        #left
        if player2.sprite.rect.left <= 0:
            player2.sprite.rect.left = 0
        #Right
        if player2.sprite.rect.right >= 800:
            player2.sprite.rect.right = 800
        #top
        if player2.sprite.rect.top <= 0:
            player2.sprite.rect.top = 0


#-----------------------------------------------colliding and platforms-----------------

        platforms_collide = pygame.sprite.spritecollideany(player1.sprite, platforms)
        if (platforms_collide):

            if player1.sprite.rect.right < platforms_collide.rect.left + 2:
                player1.sprite.rect.right = platforms_collide.rect.left

            if player1.sprite.rect.left > platforms_collide.rect.right - 2:
                player1.sprite.rect.left = platforms_collide.rect.right

            if player1.sprite.rect.centery > platforms_collide.rect.centery:
                player1.sprite.rect.top = platforms_collide.rect.bottom

            elif player1.sprite.rect.centery < platforms_collide.rect.centery:
                player1.sprite.rect.bottom = platforms_collide.rect.top
            

        #player 2            
        if player2.sprite.is_moving_right: player2.sprite.move_right()
        if player2.sprite.is_moving_left: player2.sprite.move_left()

# p2 collision
        platforms_collide = pygame.sprite.spritecollideany(player2.sprite, platforms)
        if (platforms_collide):

            if player2.sprite.rect.right < platforms_collide.rect.left + 2:
                player2.sprite.rect.right = platforms_collide.rect.left

            elif player2.sprite.rect.left > platforms_collide.rect.right - 2:
                player2.sprite.rect.left = platforms_collide.rect.right

            elif player2.sprite.rect.centery > platforms_collide.rect.centery:
                player2.sprite.rect.top = platforms_collide.rect.bottom

            elif player2.sprite.rect.centery < platforms_collide.rect.centery:
                player2.sprite.rect.bottom = platforms_collide.rect.top

        #player collisions
        if pygame.sprite.spritecollide(player1.sprite, player2, False):
            #if both players are facing right
            if player1.sprite.is_looking_right and player2.sprite.is_looking_right:
                if player1.sprite.rect.x < player2.sprite.rect.x and player1.sprite.rect.right < player2.sprite.rect.left + 3:
                    print("kill player 2R")
                    player2.sprite.kill_self()
                    player1_score += 1
                elif player2.sprite.rect.x < player1.sprite.rect.x and player2.sprite.rect.right < player1.sprite.rect.left + 3:
                    print("kill player 1R")
                    player1.sprite.kill_self()
                    player2_score += 1

            #if both players are facing left
            if  not player1.sprite.is_looking_right and not player2.sprite.is_looking_right:
                if player1.sprite.rect.x < player2.sprite.rect.x and player1.sprite.rect.left < player2.sprite.rect.right - 3:
                    print("kill player 1L")
                    player1.sprite.kill_self()
                    player2_score += 1
                elif player2.sprite.rect.x < player1.sprite.rect.x and player2.sprite.rect.left < player1.sprite.rect.right - 3:
                    print("kill player 2L")
                    player2.sprite.kill_self()
                    player1_score += 1
            
            #if one falls ontop
            if player1.sprite.rect.y < player2.sprite.rect.y and player1.sprite.rect.bottom < player2.sprite.rect.top + 3:
                print("kill player 2T")
                player2.sprite.kill_self()
                player1_score += 1
            elif player2.sprite.rect.y < player1.sprite.rect.y and player2.sprite.rect.bottom < player1.sprite.rect.top + 3:
                print("kill player 1T")
                player1.sprite.kill_self()
                player2_score += 1
            
            #bumping into each other
            if player1.sprite.is_looking_right and  not player2.sprite.is_looking_right and player1.sprite.rect.y - player2.sprite.rect.y < 5 and player1.sprite.rect.y - player2.sprite.rect.y > -5:
                player1.sprite.rect.x -= 10
                player2.sprite.rect.x += 10

            #bumping into each other
            if player2.sprite.is_looking_right and  not player1.sprite.is_looking_right and player2.sprite.rect.y - player1.sprite.rect.y < 5 and player2.sprite.rect.y - player1.sprite.rect.y > -5:
                player2.sprite.rect.x -= 10
                player1.sprite.rect.x += 10

            
#SPRITE DIRECTION
        if not player1.sprite.is_looking_right:
            player1.sprite.image = player1_surface
        else:
            player1.sprite.image = pygame.transform.flip(player1_surface, True, False)

        if not player2.sprite.is_looking_right:
            player2.sprite.image = player2_surface
        else:
            player2.sprite.image = pygame.transform.flip(player2_surface, True, False)


        text_surface = text_font.render(f"P1: {player1_score}   --    siLlY jOUsT    --   P2: {player2_score}", False, "#173109AB")
        text_box = text_surface.get_rect(midtop = (400, 35))


        #draw things onto screen     POSITIVE Y GOES DOWN IN THIS CASE
        screen.blit(sky_surface, (0,0))
        screen.blit(text_surface, text_box)
        screen.blit(ground_surface, (0, 330))


        player1.draw(screen)
        player2.draw(screen)

        platforms.draw(screen)

        pygame.display.update()

        fps.tick(60)



if __name__ == "__main__":
    main()
