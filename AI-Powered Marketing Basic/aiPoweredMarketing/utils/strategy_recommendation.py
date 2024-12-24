import openai


def generate_strategy(campaign_metrics):
    prompt = f"Based on these campaign metrics: {campaign_metrics}, suggest strategies to improve marketing performance"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

