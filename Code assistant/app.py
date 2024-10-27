import requests
import json
import gradio as gr

# Define the API endpoint and headers
url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json'
}

# Initialize history to store conversation context
history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "aristCode",
        "prompt": final_prompt,
        "temperature": 1,
        "sstream": True  # This indicates streaming is requested
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # Assuming your server sends multiple responses as text.
        # You would need to concatenate these into a final response.
        complete_response = ''
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                complete_response += data['response']

        return complete_response.strip()  # Clean up and return the complete response
    else:
        return f"Error: {response.text}"
# Create the Gradio interface
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your Prompt"),
    outputs="text",
    title="Code Assistant - AristCo",
    description="Ask any code-related questions and get responses from AristCo."
)

# Launch the interface
interface.launch()
