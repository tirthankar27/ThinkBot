import ollama
import random
import gradio as gr

def llama_chatbot(message, history):
    return ollama.generate(model='llama3.2:latest', prompt=message)['response']

gr.ChatInterface(llama_chatbot).launch()