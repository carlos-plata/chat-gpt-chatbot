
# Voice-Chatbot | ChatGPT | Eleven Labs

## Overview

Welcome to the **Voice-Chatbot | ChatGPT | Eleven Labs**! This project integrates cutting-edge AI technologies to create a fully-functional chatbot that you can interact with using your voice. Built with **React** on the frontend and **FastAPI** on the backend, this chatbot leverages OpenAI's GPT-4 for natural language processing and Eleven Labs for text-to-speech, allowing seamless voice conversations with AI.

This project serves as a perfect example of how to combine state-of-the-art APIs with modern web technologies for building real-time, voice-powered applications.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [API Integration](#api-integration)
  - [OpenAI API](#openai-api)
  - [Eleven Labs API](#eleven-labs-api)

## Features

- **Voice-powered interaction**: Speak to the chatbot and hear it respond with synthesized voice.
- **AI-driven conversations**: Powered by OpenAI's GPT-4, the chatbot provides context-aware responses.
- **FastAPI backend**: A high-performance API framework that handles requests from the frontend.
- **Real-time communication**: Fast and responsive interactions between frontend and backend.
- **Text-to-speech synthesis**: Voice responses powered by Eleven Labs, delivering natural-sounding AI voices.
- **Beautiful UI**: Modern and responsive UI built with React and Tailwind CSS for an intuitive user experience.

## Tech Stack

### Backend:
- **Programming Language**: Python
- **Framework**: FastAPI
- **APIs**: 
  - [OpenAI GPT-4](https://openai.com)
  - [Eleven Labs Text-to-Speech](https://beta.elevenlabs.io)
  
### Frontend:
- **Programming Language**: JavaScript (ES6+)
- **Framework**: React
- **Styling**: Tailwind CSS

### Tools:
- **Node.js**: Used for frontend dependency management.
- **Python**: Powering the backend with FastAPI.

## Setup Instructions

### Prerequisites

Before setting up the project, make sure you have the following installed:

- **Node.js** (v16+)
- **Python** (v3.8+)
- **FastAPI** (You can install via `pip`)
- **Git** (for cloning the repository)
- **An OpenAI API key** (You need to sign up at [OpenAI](https://openai.com/))
- **An Eleven Labs API key** (You can get one at [Eleven Labs](https://beta.elevenlabs.io/))

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/carlos-plata/chat-gpt-chatbot.git
   cd chatgpt-gpt-chatbot/backend
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install backend dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the `backend` folder and add your API keys:
   ```
   OPENAI_API_KEY=your-openai-api-key
   ELEVEN_LABS_API_KEY=your-eleven-labs-api-key
   ```

5. **Run the FastAPI backend**:
   ```bash
   uvicorn main:app --reload
   ```
   Your backend should now be running at `http://127.0.0.1:8000`.

### Frontend Setup

1. **Navigate to the frontend folder**:
   ```bash
   cd ../frontend
   ```

2. **Install frontend dependencies**:
   ```bash
   npm install
   ```

3. **Run the React app**:
   ```bash
   npm start
   ```
   The React frontend should now be running at `http://localhost:3000`.

## Usage

1. Open the app in your browser by navigating to `http://localhost:3000`.
2. Click on the microphone button to speak to the chatbot.
3. The chatbot will process your input and reply with a voice response using Eleven Labs' text-to-speech engine.
4. Observe real-time interaction as the backend processes your queries using GPT-4 and returns intelligent responses.

## API Integration

### OpenAI API
The core functionality of this chatbot is powered by OpenAI's GPT-4 model. When a user speaks, the audio is converted to text, which is then sent to OpenAI's API for natural language processing. The GPT-4 model generates a response based on the input, which is then sent back to the frontend.

### Eleven Labs API
Eleven Labs' text-to-speech API converts the chatbot's textual response into synthesized speech. This allows users to interact with the chatbot through voice, making the interaction more dynamic.

Thank you for checking out this project! If you have any questions or suggestions, feel free to reach out.

Happy coding!
