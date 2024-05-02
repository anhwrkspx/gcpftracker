from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import utils as utils


app = Flask(__name__)

@app.route("/")
def index():
    user_link = request.args.get('user_link')
    num_badges = None
    skill_badges = None
    base_badges = None
    error_message = None
    badge_data=[0,0,0]
    tier=""
    if user_link:
        badge_data = utils.get_badge_statistics(utils.get_badge_info(user_link))
        num_badges=badge_data[0]
        skill_badges=badge_data[1]
        base_badges= badge_data[2]
        tier=utils.categorize_tier(badge_data)
        if any([not num for num in [num_badges, skill_badges, base_badges]]):
            error_message = "Unable to find badge."

    return render_template('index.html', user_link=user_link, num_badges=num_badges, skill_badges=skill_badges, base_badges=base_badges, tier=tier, error_message=error_message)

@app.route("/home")
def home():
    return render_template("templates/index.html")

if __name__ == '__main__':
    app.run(debug=True)