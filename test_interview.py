from interview import generate_question

skills = [
    "Python",
    "Machine Learning",
    "TensorFlow"
]

question = generate_question(
    role="AI/ML Engineer",
    skills=skills
)

print("\nGenerated Question:\n")
print(question)