# LLEM

LLEM is a simple and self-contained web interface for interacting with a Large Language Model (LLM) that can generate text based on user input. This project provides a Flask-based web application that allows users to chat with a model, giving answers to questions or completing prompts. It can be used with any model that supports the Hugging Face Transformers library.

<br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/e653900c-57a7-49e4-b7ec-835852916452" width="700" height="auto"/>
  <br><br>
  <em>Demo of the interface.</em>
</div>
<br>

## Features

- A web interface to interact with a pre-trained Large Language Model.
- Simple prompt-based interactions where users can chat with the AI.
- Powered by the Hugging Face transformers library for model handling.

## Setup and Installation

You can run the application using Docker or manually. The manual setup has only been tested with Python 3.12.

### Download the Model

The `download_model.py` script downloads the pre-trained model from Hugging Face and saves it locally in the `model` directory. By default, it fetches the `SmolLM2-135M-Instruct` model.

Make sure the required dependencies are installed and then run the script:
```bash
python download_model.py
```

### Docker Setup

The easiest way to run the application is using Docker. This will handle all dependencies and environment setup.

1. Download the model as described above.
2. Build the image:
    ```bash
    docker compose build
    ```
3. Run the container:
    ```bash
    docker compose up
    ```

The app will be accessible at [http://localhost:5000](http://localhost:5000).

### Manual Setup

If you prefer to run the application manually, follow steps below.

1. Set up a Python virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2. Install the required dependencies:
    ```bash
    pip install -r app/requirements.txt
    ```
3. Start the Flask web server:
    ```bash
    python app/app.py
    ```

The app will be accessible at [http://localhost:5000](http://localhost:5000).

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for more information.

Backround image: [Inspiration Geometry](https://www.transparenttextures.com/).
