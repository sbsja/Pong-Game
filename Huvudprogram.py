import pygame, sys, random

def boll_rörelse(boll_dx, boll_dy):
    # Rörelse för karaktärerna
    boll.x += boll_dx
    boll.y += boll_dy
    
    if boll.top <= 0 or boll.bottom >= HEIGHT:
        boll_dy *= -1 
    if boll.left <= 0 or boll.right >= WIDTH:
        boll.center = (WIDTH/2, HEIGHT/2)
        boll_dx *= random.choice((1, -1))
        boll_dy *= random.choice((1, -1))
        
    if boll.colliderect(spelare) or boll.colliderect(motståndare):
        boll_dx *= -1
        
    return boll_dx, boll_dy

def spelare_rörelse():
    spelare.y += spelare_hastighet
    if spelare.top <= 0:
        spelare.top = 0
    if spelare.bottom >= HEIGHT:
        spelare.bottom = HEIGHT

def motståndare_rörelse():
    motståndare.y += motståndare_hastighet
    if motståndare.top <= 0:
        motståndare.top = 0
    if motståndare.bottom >= HEIGHT:
        motståndare.bottom = HEIGHT

def Knapp_tryck(spelare_hastighet, motståndare_hastighet):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            spelare_hastighet += 7
        if event.key == pygame.K_UP:
            spelare_hastighet -= 7
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            spelare_hastighet -= 7
        if event.key == pygame.K_UP:
            spelare_hastighet += 7
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            motståndare_hastighet += 7
        if event.key == pygame.K_w:
            motståndare_hastighet -= 7
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_s:
            motståndare_hastighet -= 7
        if event.key == pygame.K_w:
            motståndare_hastighet += 7
            
    return spelare_hastighet, motståndare_hastighet

def Rita_fönster():
    #RITAR IN FIGURERNA
    FÖNSTER.fill("Grey12")
    pygame.draw.rect(FÖNSTER, WHITE, spelare)
    pygame.draw.rect(FÖNSTER, WHITE, motståndare)
    pygame.draw.ellipse(FÖNSTER, WHITE, boll)
    pygame.draw.aaline(FÖNSTER, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT))
            
    pygame.display.flip()
    klocka.tick(60)



pygame.init()
klocka = pygame.time.Clock()

WIDTH, HEIGHT = 1280, 720
FÖNSTER = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")


boll = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30)
spelare = pygame.Rect(WIDTH - 30, HEIGHT/2 - 70, 10, 140)
motståndare = pygame.Rect(20, HEIGHT/2 -70, 10, 140)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

boll_dx = 10
boll_dy = 10
spelare_hastighet = 0
motståndare_hastighet = 0

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        spelare_hastighet, motståndare_hastighet = Knapp_tryck(spelare_hastighet, motståndare_hastighet)        
        
    boll_dx, boll_dy = boll_rörelse(boll_dx, boll_dy)
    spelare_rörelse()
    motståndare_rörelse()
    Rita_fönster()
