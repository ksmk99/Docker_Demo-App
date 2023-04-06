
from flask import Flask
from transformers import pipeline, set_seed

app = Flask(__name__)


@app.route('/')
def hello_world():



    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    return generator("Hello, I'm a language model,", max_length=30, num_return_sequences=1)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')