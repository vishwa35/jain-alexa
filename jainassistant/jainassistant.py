import logging
from random import randint
from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement, context, audio, current_stream

app = Flask(__name__)
ask = Ask(app, "/")
logger = logging.getLogger()
logging.getLogger('flask_ask').setLevel(logging.INFO)


@ask.launch
def launch():
  return greet()

@ask.intent('JJIntent')
def greet():
  speech = "Jai Jinendra. Would you like to hear a quote?"
  return question(speech)

@ask.intent('QuoteIntent')
def quote():
  quotes = list_quotes()
  speech = quotes[randint(0, 43)]
  return statement(speech)

@ask.intent('AMAZON.HelpIntent')
def help():
  speech = "Say \"Tell me a quote\" to hear a quote or \"Jai Jinendra\" for a greeting. What would you like me to do?"
  return question(speech)

@ask.session_ended
def session_ended():
  return "{}", 200

def list_quotes():
  with open('quotes.txt', 'r') as f:
    quotes = f.readlines()
  return quotes


if __name__ == '__main__':
  app.run(debug=True)
