import pygame.font

class ScoreBoard():
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.ai_settings=ai_settings
        self.text_color=(139,69,19)
        self.font=pygame.font.SysFont("italic",40)
        self.prep_score()


    def prep_score(self):
        rounded_score=int(round(self.ai_settings.score,-1))
        score_str=("SCORE "+"{:,}".format(rounded_score))
        self.score_image=self.font.render(score_str,True,self.text_color)


        self.score_rect=self.score_image.get_rect()
        self.score_rect.left=self.screen_rect.left+20
        self.score_rect.top=20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)