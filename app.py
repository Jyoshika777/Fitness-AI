from flask import Flask, render_template, request
from fitness_agent import fitness_agent

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    plan = None
    score = None
    attempts = None
    error = None

    if request.method == "POST":

        try:

            initial_state = {
                "age": request.form["age"],
                "height": request.form["height"],
                "weight": request.form["weight"],
                "goal": request.form["goal"],
                "experience": request.form["experience"],
                "days": request.form["days"],
                "duration": request.form["duration"],
                "equipment": request.form["equipment"],
                "preferences": request.form["preferences"],
                "plan": "",
                "score": 0,
                "attempts": 0,
                "feedback": ""
            }

            result = fitness_agent.invoke(
                initial_state
            )

            plan = result["plan"]
            score = result["score"]
            attempts = result["attempts"]

        except Exception as e:

            error = str(e)

    return render_template(
        "index.html",
        plan=plan,
        score=score,
        attempts=attempts,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)