from typing import TypedDict

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END


# ============================================================
# FITNESS STATE
# ============================================================

class FitnessState(TypedDict):
    age: str
    height: str
    weight: str
    goal: str
    experience: str
    days: str
    duration: str
    equipment: str
    preferences: str

    plan: str
    score: int
    attempts: int
    feedback: str


# ============================================================
# OLLAMA MODEL
# ============================================================

MODEL_NAME = "llama3.2:3b"

generator = ChatOllama(
    model=MODEL_NAME,
    temperature=0.5
)

evaluator = ChatOllama(
    model=MODEL_NAME,
    temperature=0
)


# ============================================================
# GENERATE FITNESS PLAN
# ============================================================

def generate_plan(state: FitnessState):

    prompt = f"""
Create a simple, safe and personalized fitness plan.

User details:
Age: {state["age"]}
Height: {state["height"]} cm
Weight: {state["weight"]} kg
Goal: {state["goal"]}
Experience: {state["experience"]}
Workout days per week: {state["days"]}
Workout duration: {state["duration"]} minutes
Equipment: {state["equipment"]}
Preferences: {state["preferences"]}

Create a practical weekly workout plan.

Include:

1. Weekly schedule
2. Exercises for each workout day
3. Sets and repetitions
4. Warm-up
5. Cool-down
6. Rest/recovery
7. Basic nutrition guidance
8. Progress tracking

Keep the answer concise and beginner-friendly.

Do not provide medical diagnosis, medication advice,
extreme diets, or dangerous exercises.

If the user has an injury or medical condition,
recommend consulting a qualified healthcare professional.
"""

    response = generator.invoke([
        HumanMessage(content=prompt)
    ])

    state["plan"] = response.content
    state["attempts"] = 1

    return state


# ============================================================
# EVALUATE PLAN
# ============================================================

def evaluate_plan(state: FitnessState):

    prompt = f"""
Evaluate the following fitness plan.

Give a score from 1 to 10 based on:

- Safety
- Personalization
- Exercise balance
- Realistic workload
- Recovery
- Goal alignment

Fitness plan:

{state["plan"]}

Return EXACTLY this format:

SCORE: 8
FEEDBACK: Short explanation of the score.
"""

    response = evaluator.invoke([
        HumanMessage(content=prompt)
    ])

    text = response.content.strip()

    score = 7
    feedback = "Plan evaluated successfully."

    for line in text.splitlines():

        line = line.strip()

        if line.upper().startswith("SCORE:"):

            try:
                score_text = line.split(":", 1)[1].strip()
                score = int(score_text.split()[0])

                # Keep score between 1 and 10
                score = max(1, min(10, score))

            except:
                score = 7

        elif line.upper().startswith("FEEDBACK:"):

            feedback = line.split(":", 1)[1].strip()

    state["score"] = score
    state["feedback"] = feedback

    return state


# ============================================================
# BUILD LANGGRAPH AGENT
# ============================================================

def build_fitness_agent():

    graph = StateGraph(FitnessState)

    # Add nodes
    graph.add_node("generate", generate_plan)
    graph.add_node("evaluate", evaluate_plan)

    # Start
    graph.set_entry_point("generate")

    # Generate → Evaluate
    graph.add_edge("generate", "evaluate")

    # Evaluate → Finish
    graph.add_edge("evaluate", END)

    return graph.compile()


# Create agent
fitness_agent = build_fitness_agent()


# ============================================================
# TERMINAL TEST
# ============================================================

if __name__ == "__main__":

    print("\n=================================")
    print(" PERSONALIZED FITNESS AI AGENT")
    print("=================================\n")

    age = input("Age: ")
    height = input("Height (cm): ")
    weight = input("Weight (kg): ")
    goal = input("Fitness goal: ")
    experience = input("Experience level: ")
    days = input("Workout days per week: ")
    duration = input("Workout duration (minutes): ")
    equipment = input("Equipment available: ")
    preferences = input("Workout preferences: ")

    initial_state = {
        "age": age,
        "height": height,
        "weight": weight,
        "goal": goal,
        "experience": experience,
        "days": days,
        "duration": duration,
        "equipment": equipment,
        "preferences": preferences,

        "plan": "",
        "score": 0,
        "attempts": 0,
        "feedback": ""
    }

    print("\nGenerating your fitness plan...")
    print("Please wait...\n")

    result = fitness_agent.invoke(initial_state)

    print("\n=================================")
    print(" YOUR FITNESS PLAN")
    print("=================================\n")

    print(result["plan"])

    print("\n=================================")
    print(" PLAN EVALUATION")
    print("=================================")

    print(f"\nPLAN SCORE: {result['score']} /10")
    print(f"FEEDBACK: {result['feedback']}")
    print(f"TOTAL ATTEMPTS: {result['attempts']}")

    print("\n=================================")
    print(" DONE")
    print("=================================\n")