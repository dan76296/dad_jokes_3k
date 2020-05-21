import argparse
import sys
import logging

import requests
import pyfiglet
import termcolor
from random import choice

__author__ = "Dan Wooffitt"
__copyright__ = "Dan Wooffitt"
__license__ = "mit"

_logger = logging.getLogger(__name__)

def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")

class dad_joke_3k:

  def __init__(self):
    self.url = "https://icanhazdadjoke.com/search"
    self.u_input = None
    self.request = None
    self.total_jokes = None
    self.response = None

  def welcome_message(self):
    header = pyfiglet.figlet_format("Dad Joke 3000")
    header = termcolor.colored(header, color="green")
    print(header)
    print(f"All jokes are taken from: {self.url}")
    _logger.debug("Welcome message displayed")

  def user_input(self):
    print("Let me tell you a joke. Please choose a topic:")
    self.u_input = input('> ')
    return self.u_input

  def request_jokes(self):
    self.request = requests.get(self.url,
    headers={"Accept": "application/json"},
    params={"term": self.u_input}).json()
    
    self.total_jokes = self.request['total_jokes']
    self.results = self.request['results']
  
  def display_jokes(self):
    if self.total_jokes >= 1:
      if self.total_jokes > 1:
        print(f"I have found {self.total_jokes} jokes about '{self.u_input}'. Here's one for you.\n")
      elif self.total_jokes == 1:
        print(f"I have only found 1 joke about '{self.u_input}'. So here goes everything...\n")
    
      print(choice(self.results)['joke'])
      print('\n')

    else:
      print(f"I couldn't find any jokes about '{self.u_input}. Maybe it just isn't a funny topic.\n")
  
  def relapse(self):
    if self.total_jokes > 1:
      try:
        print(f"There are more where that came from though... Would you like to hear the full list? (Y/N)\n")
        self.response = input("> ")

        if (self.response == "Y") or (self.response == "y"):
          for result in self.results:
            print(result['joke'])
            print('\n')
          
          self.response = True

        elif (self.response == "N") or (self.response == "n"):
          print("Ffffffffine. Would you like to choose a different topic? (Y/N)\n")
          self.response = input("> ")

        else:
         print("Incorrect input. Please try again.")

      except:
        self.relapse()

    else:
      self.response = True
      main()
    
    if (self.response == "Y") or (self.response == "y") or (self.response == True):
      main()

dad = dad_joke_3k()

def main():
  if dad.response is None:
    setup_logging(2)
    _logger.debug("Starting dad_jokes_3000...")
    dad.welcome_message()

  dad.user_input()
  dad.request_jokes()
  dad.display_jokes()
  dad.relapse()


def run():
    main()


if __name__ == "__main__":
    run()
