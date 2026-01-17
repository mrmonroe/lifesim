import time
from datetime import datetime

class Game:

    def __init__(self):
        self.game_state = {}
        self.start_time = None
        self.is_running = False
        self.game_title = "LifeSim"
        self.session_title = "Unnamed Session"
        self.hour= 0
        self.day = 0
        self.iteration_delay = 3  # seconds
        print(" ")
    
    
    def start_game(self):
        self.is_running = True
        self.start_time = datetime.now()
    
        print(f"Game '{self.game_title}' started at {self.start_time}.")
        self.initialize_game()
        self.game_loop()

    def initialize_game(self):
            pass

    def game_loop(self):
        while self.is_running:
            try:
              # Simulate time passing
                time.sleep(self.iteration_delay)
                self.hour += 1
                self.create()  # your blocking code here
            except ValueError:
                # handle only specific errors
                pass
            except KeyboardInterrupt:
                # handle the Ctrl+C specifically for cleanup
                self.is_running = False
                print("Interrupted by user, exiting gracefully...")
                
  
            

    
    def create(self):
        print("Creating game elements...")
        self.update()
        pass
    def update(self):
        print("Updating game state...")
        self.render()
        pass
    def render(self):
        print("Rendering game...")
        pass