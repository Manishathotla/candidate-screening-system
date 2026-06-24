from rag import retrieve_context


def evaluate_answer(question, answer):

    if not question or not answer:
        return {
            "error": "question and answer required"
        }

    context = retrieve_context(question)

    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())

    matched = list(answer_words.intersection(context_words))

    score = min(len(matched) + 3, 10)

    return {
        "score": score,
        "matched_keywords": matched,
        "feedback": {
            "strengths": ["Answer provided"],
            "improvements": ["Add more technical depth"]
        }
    }