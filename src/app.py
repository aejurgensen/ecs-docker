import time
import os
import capitals
import random
from flask import Flask

app = Flask(__name__)


@app.route('/')
def random_state():
  random_selection = random.choice(capitals.get_all_abbrevations())
  return capitals.get_state_info(random_selection)
  #ENV = os.getenv('ENV')
  #return f'Hello {ENV}!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
