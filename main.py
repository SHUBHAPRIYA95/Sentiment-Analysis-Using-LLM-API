import openai
import gradio as gr

openai.api_key = "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"

def analyze_sentiment(conversation):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=1,
        temperature=0.0,
        n=1,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    sentiment = response.choices[0].message.content.strip().lower()
    return sentiment

def sentiment_analysis_api(text):
    conversation = [
        {"role": "system", "content": "You are a helpful and kind AI Assistant."},
        {"role": "user", "content": text}
    ]
    sentiment = analyze_sentiment(conversation)
    return sentiment.capitalize()

iface = iface = gr.Interface(fn=sentiment_analysis_api, inputs="text", outputs=gr.outputs.Textbox(label="Sentiment"),
                     title="Sentiment Analysis API",
                     description="Analyze the sentiment of a given text",
                     theme="compact")



iface.launch(share=True)