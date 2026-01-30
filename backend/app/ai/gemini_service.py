def explain(score):
    if score > 70:
        return "Strong match with required skills."
    elif score > 40:
        return "Partial match. Some skills missing."
    return "Low match with job requirements."
