import logging

from flask import Flask, jsonify, render_template, request
from transformers import AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

checkpoint = "/model"
device = "cpu"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    prompt = (
        f"<|im_start|>system\nYou are a helpful and very knowledgeable AI assistant named Llem.\n"
        f"Try to answer in no more than 3 sentences.\n"
        f"Do not hallucinate.<|im_end|>\n"
        f"<|im_start|>user\n{user_input}<|im_end|>\n"
    )

    logger.info("Prompt: %s", prompt)

    encoded = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    inputs = encoded["input_ids"].to(device)
    attention_mask = encoded["attention_mask"].to(device)

    outputs = model.generate(
        inputs,
        attention_mask=attention_mask,
        max_new_tokens=100,
        do_sample=True,
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.split("assistant\n")[-1].strip()

    logger.info("Response: %s", response)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
