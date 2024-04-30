# Discord ChatGPT Bot 🤖

This repository contains the code for a simple Discord bot that uses OpenAI's GPT-3 model to respond to user queries.

## Features 🚀

- Connects to Discord using the discord.py library 📡.
- Responds to user commands prefixed with '!' 📣.
- Filters out non-alphanumeric characters from user queries 🗂.
- Sends user queries to the GPT-3 model and returns the response in the chat 💬.

## Installation 🔧

1. Install the required Python libraries by running: 📚
    
    ```Python
    pip install -r requirements.txt
    
    ```
    
2. Add your Discord token and OpenAI API Key to a .env file: 🔑
    
    ```Python
    DISCORD_TOKEN=your_discord_token
    OPENAI_API=your_openai_api_key
    
    ```
    

## Usage 🎮

1. Run the bot.py script: 🖥
    
    ```Python
    python bot.py
    
    ```
    
2. In Discord, use the '!gpt' command followed by your query: 💻
    
    ```Python
    !gpt your_query_here
    
    ```
    

## Dependencies 🧩

- discord.py
- python-dotenv
- openai

## Please Note
To obtain the OpenAI API key:

1. Sign up or log in to the OpenAI website.
2. Navigate to the API section in your account settings.
3. Generate a new API key and copy it.

To obtain a Discord token:

1. Go to the Discord Developer Portal and log in.
2. Click on "New Application" to create a new bot.
3. Go to the Bot settings, click on "Add Bot".
4. Under the "Token" section, click on "Copy" to copy your bot's token.
