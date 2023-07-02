# Sentiment-Analysis-Using-LLM-API
Setting up OpenAI API:

The OpenAI API key is set using openai.api_key to authenticate your API requests. Make sure to replace  with actual OpenAI API key.
analyze_sentiment function:

This function takes a conversation as input and performs sentiment analysis using the OpenAI GPT-3.5 Turbo model.
The conversation is passed to the openai.Completion.create method, which sends the conversation as a prompt to the model for sentiment analysis.
The engine parameter is set to "gpt-3.5-turbo" to use the GPT-3.5 Turbo model.
Other parameters such as max_tokens, temperature, n, stop, top_p, frequency_penalty, and presence_penalty control the behavior of the completion generation process.
The sentiment is extracted from the response and returned as the output.
sentiment_analysis_api function:

This function takes a text input and constructs a conversation by combining it with a system message and user message.
The system message sets the context for the conversation and informs the AI that it is an AI assistant.
The user message contains the text input provided by the user.
The conversation is passed to the analyze_sentiment function to perform sentiment analysis.
The sentiment is then capitalized and returned as the output.
Creating the Gradio Interface:

The iface object is created using gr.Interface to build the user interface for the sentiment analysis API.
The function sentiment_analysis_api is used as the processing function, which takes text input and returns the sentiment analysis result.
The input is defined as a gr.inputs.Textbox to accept text input from the user.
The output is defined as a gr.outputs.Textbox to display the sentiment analysis result.
The title, description, and theme of the interface are set accordingly.
Launching the Gradio Interface:

The iface.launch(share=True) command is used to launch the Gradio interface with the sentiment analysis API.
The share=True parameter allows sharing the interface using a publicly accessible URL.
When the code is executed, it sets up the sentiment analysis API using OpenAI's GPT-3.5 Turbo model and launches a Gradio interface where users can input text and get the sentiment analysis result in real-time.
