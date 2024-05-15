from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get('prompt')
    
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="b64_json"
        )
        image_data = response['data'][0]['b64_json']
        return jsonify({'image': image_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
