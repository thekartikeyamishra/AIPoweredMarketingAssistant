import openai

openai.api_key = "API Key Here"


def generate_content(prompt, content_type="social media:"):
    template = f"Create a {content_type} post for the this : {prompt}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=template,
        max_tokens=150
    )
    return response.choices[0].text.strip()
