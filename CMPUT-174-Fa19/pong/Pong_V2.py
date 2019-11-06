# Pong V2
# This version of Pong will have the ball being able to collide with the front of the paddles, be able to update the score and end the game

import pygame


screen_width = 500
screen_height = 400

# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((screen_width, screen_height))
   # set the title of the display window
   pygame.display.set_caption('Pong')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 


# User-defined classes

class Game():
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game

      #properties of the game, including screen colour, FPS, and closing fucntion
      self.surface = surface
      self.bg_color = pygame.Color('black')
      
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      self.leftp_score = 0
      self.rightp_score =0
      self.max_score = 11
      
      # colour of balls, and "time" limit for game
      self.ball = Ball('white', 5, [250, 200], [3, 1], self.surface)
      self.paddle_Right = pygame.Rect(400, 175, 10, 50)
      self.paddle_Left = pygame.Rect(80, 175, 10, 50)
      self.max_frames = 150
      self.frame_counter = 0
      

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.
      # until player clicks close box
      while not self.close_clicked:  
         self.handle_events(self.ball, self.paddle_Right, self.paddle_Left)
         self.draw()
         self.decide_continue(self.leftp_score, self.rightp_score)
         if self.continue_game:
            self.update()
            self.update_scores()
            
         self.game_Clock.tick(self.FPS)

   def handle_events(self, ball, pRight, pLeft):
      # Handle each user event by changing the game state appropriately.

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked == True
            pygame.quit()
            quit()
      
      if ball.velocity[0] < 0 and pLeft.collidepoint(ball.center[0]-ball.radius, ball.center[1]):
         ball.velocity[0] = -ball.velocity[0]
      if ball.velocity[0] > 0 and pRight.collidepoint(ball.center[0]+ball.radius, ball.center[1]):
         ball.velocity[0] = -ball.velocity[0]    
      

   def draw(self):
      # Draw all game objects.
      self.surface.fill(self.bg_color) # clear the display surface first
      self.ball.draw()
      pygame.draw.rect(self.surface, pygame.Color('white'), self.paddle_Right)
      pygame.draw.rect(self.surface, pygame.Color('white'), self.paddle_Left)
      self.draw_score_left()
      self.draw_score_right()
      
      pygame.display.update() # make the updated surface appear on the 
   
   def draw_score_left(self):
      score_string = str(self.rightp_score)
      score_font = pygame.font.SysFont('',70)
      score_color = pygame.Color('white')
      score_display = score_font.render(score_string, True, score_color)
      self.surface.blit(score_display, (10,0)) 
   
   def draw_score_right(self):
      score_string = str(self.leftp_score)
      score_font = pygame.font.SysFont('',70)
      score_color = pygame.Color('white')
      score_display = score_font.render(score_string, True, score_color)
      self.surface.blit(score_display, (450,0))   
   
      
   def update(self):
      # Update the game objects for the next frame.      
      self.ball.move()
      self.frame_counter = self.frame_counter + 1
      
   def update_scores(self):
      if self.ball.center[0] < self.ball.radius:
         self.leftp_score = self.leftp_score + 1
      if self.ball.center[0] + self.ball.radius > 500:
         self.rightp_score = self.rightp_score + 1
         
   def decide_continue(self, scoreL, scoreR):
      # Check and remember if the game should continue      
      if scoreL == 11 or scoreR == 11:
         pygame.quit()
         
class Ball:
   # An object in this class represents a Ball that moves 
   
   def __init__(self, Ball_color, Ball_radius, Ball_center, Ball_velocity, surface):
      
      # Initialize a Ball.
      # - self is the Ball to initialize
      # - color is the pygame.Color of the Ball
      # - center is a list containing the x and y int
      #   coords of the center of the Ball
      # - radius is the int pixel radius of the Ball
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(Ball_color)
      self.radius = Ball_radius
      self.center = Ball_center
      self.velocity = Ball_velocity
      self.surface = surface
      
   def move(self):
      # Change the location of the Ball by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Ball
      
      for i in range (0,len(self.center)):
         self.center[i] += self.velocity[i]
      if self.center[0] <= 0 + self.radius or self.center[0] >= screen_width - self.radius:
         self.velocity[0] = -self.velocity[0]
      if self.center[1] >= screen_height - self.radius or self.center[1] <= self.radius:
         self.velocity[1] = -self.velocity[1]      
      
      print(self.velocity)
   
   def draw(self):
      # Draw the Ball on the surface
      # - self is the Ball
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
   
main()
