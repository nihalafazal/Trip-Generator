import os
import csv
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")


def load_prompt_template():
    with open("prompts/travel_prompt.txt", "r") as f:
        return f.read()


def load_destinations():
    destinations = []
    with open("dataset/destinations.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            destinations.append(row)
    return destinations


def find_matching_destinations(dest_type, budget, destinations):
    matches = [
        d for d in destinations
        if d["type"].lower() == dest_type.lower()
        and int(d["avg_budget"]) <= int(budget)
    ]
    return matches[:3] if matches else destinations[:3]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    budget = data.get("budget", "1000")
    days = data.get("days", "3")
    dest_type = data.get("destination_type", "beach")

    destinations = load_destinations()
    matching = find_matching_destinations(dest_type, budget, destinations)
    dest_names = ", ".join([d["destination"] for d in matching]) if matching else dest_type

    prompt_template = load_prompt_template()
    prompt = prompt_template.format(
        budget=budget,
        days=days,
        destination_type=dest_type,
        suggested_destinations=dest_names
    )

    try:
        response = model.generate_content(prompt)
        result_text = response.text

        # Parse sections from response
        sections = {
            "suggestion": "",
            "itinerary": "",
            "packing": "",
            "image_idea": ""
        }

        lines = result_text.split("\n")
        current_section = None

        for line in lines:
            line_lower = line.lower()
            if "trip suggestion" in line_lower or "## suggestion" in line_lower:
                current_section = "suggestion"
            elif "itinerary" in line_lower:
                current_section = "itinerary"
            elif "packing" in line_lower:
                current_section = "packing"
            elif "image" in line_lower:
                current_section = "image_idea"
            elif current_section:
                sections[current_section] += line + "\n"

        # Fallback: if parsing fails, put everything in suggestion
        if not any(sections.values()):
            sections["suggestion"] = result_text

        return jsonify({"success": True, "data": sections, "raw": result_text})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
