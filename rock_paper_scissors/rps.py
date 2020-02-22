#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  outcomes = []
  def inner_func(rounds, result =[]):
    if rounds == 0:
      outcomes.append(result)
      return

    for play in plays:
      inner_func(rounds-1, result + [play])
  inner_func(n, [])
  return outcomes



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')