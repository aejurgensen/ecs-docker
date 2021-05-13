import capitals
import random
from flask import Flask, request

app = Flask(__name__)

def get_random_state():
    random_selection = random.choice(capitals.get_all_abbrevations())
    return capitals.get_state_info(random_selection)

# expects search string to match for a state/territory name using the key
# 'search' (e.g. localhost:5000/?search=California)
@app.route('/')
def get_state():
    search = request.args.get('search')

    if search is None:
        info = get_random_state()
    else:
        info = capitals.get_safe_state_info(search)

    return info


# expects search string to match for a state/territory name using the key
# 'search' (e.g. localhost:5000/prettified?search=California)
@app.route('/prettified')
def prettified_get_state():
    search = request.args.get('search')

    if search is None:
        info = get_random_state()
    else:
        info = capitals.get_safe_state_info(search)

    info_str = info["name"] + "<br/>"
    info_str += "capital: " + info["capital"] + "<br/>"
    info_str += "statehood: " + info["statehood"] + "<br/>"
    info_str += "timezones: " + info["timezones"]
    return info_str


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
