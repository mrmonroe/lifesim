# lifesim
A python life simulator. From scratch

## Create a life simulator much like pol using python for ability to use it's data science platform.

## Roadmap
- ### Phase 1
  - Create MVP Architecture
  - Stub classes
  - Get basic functionality for system working, game loop, person, resource, state and environment objects
    - code structure
    - game loop
    - person factory
    - resource factory
    - environment factory
    - state object
    - update list

## MVP Requirements
- ### Actions
  - Maximum Comfort is the goal
  - Game loop os 1 second
  - 3 seconds = 1 day
  - Create food and water resources and eat and drink to increase comfort
  - Water and food available immediately
  - If person eats food one iteration, it is not available the next iteration
  - Water is available all the time but has low hunger value
  - Create environment with attributes like temperature, wind, weather, inside, outside, bed, entertainment
  - Environment conditions will determine the falling of comfort every second.
  - One single state object
  - data driven start state by yaml or json
  - 
  - Ability to save a file of the entire game state and
    
- ### Classes
  - Factories
    - ResourceFactory
    - PersonFactory
    - EnvironmentFactory
    - GameManager
    - ObjectManager
    - StateManager
  
 -   
- ### State
  - 
