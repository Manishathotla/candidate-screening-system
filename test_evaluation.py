from evaluation import evaluate_answer

question = """
Explain the difference between supervised
and unsupervised learning.
"""

answer = """
Supervised learning uses labeled data
for training and prediction.

Unsupervised learning uses unlabeled data
and is commonly used for clustering and
pattern discovery.
"""

result = evaluate_answer(
    question,
    answer
)

print(result)