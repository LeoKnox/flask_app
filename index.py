from flask import Flask, render_template, request
from flask_sqlalchemy import request

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "projDB01.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAchemy(app)

class Character(db.Model):
    charName = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return"<Char: {}>".format(self.charName)

@app.route("/", methods=["GET","POST"])
def index():
    if request.form:
        print(request.form)
        char = Character(charName=request.form.get("charName"))
        db.session.add(charName)
        db.session.commit()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)