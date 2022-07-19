import utils
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('list.html', candidates=utils.candidates)


@app.route("/candidate/<int:id>/")
def page_candidate(id):
    return render_template('card.html', candidate=utils.get_by_id(id))


@app.route("/search/<candidate_name>/")
def search_candidate(candidate_name):
    return render_template('search.html', candidates=utils.get_by_name(candidate_name), len=len(utils.get_by_name(candidate_name)))


@app.route("/skill/<skill_name>/")
def search_by_skill(skill_name):
    return render_template('skill.html', candidates=utils.get_by_skill(skill_name), skill=skill_name, len=len(utils.get_by_skill(skill_name)))


app.run()
