# Twitch Chat Bot with GPT-4 API
This repository contains a Twitch chat bot that utilizes the GPT-4 API to emulate a chatter in a given channel. The bot has the ability to listen to the stream as well as grab screenshots from the stream. It is built using Python and relies on the pipenv package to manage dependencies and create a virtual environment.

## Requirements
Before cloning and running the project, make sure you have the following:
- Python 3.9 or higher 
- pipenv
- A valid Twitch API key
- A valid openAI API key

## Installation and Setup
To get started with this project, follow the steps below:

Clone the repository using the following command:
```git clone https://github.com/jthorn70/Twitch-GPT.git```

Navigate to the project directory:
```cd Twitch-GPT```

Install the required dependencies by running:
```pipenv install -r requirements.txt```


Rename conf.Example.py to conf.py and congifure the file with your personal settings

Easiest way to run is to run ```run.py```. This will create a new pipenv shell and run the bot and the script for listening to the stream audio in seperate windows.


Alternatively, you can just run the chat bot.
Activate the virtual environment:
```pipenv shell```


Start the bot by running:
``twitchGPT.py```
The bot should start running and connecting to the specified Twitch channel.

## Usage
Once the bot is up and running, it will listen to the Twitch channel and emulate a chatter using the GPT-4 API. It listens to the stream as well as the chat. 
There are a few commands you can use to configure the bot while it is running:
- ```-refreshing```: Toggles message memory saving. If off, memory is not cleared after every message.
- ```-wipe```: clears the entire log history
- ```-number```: this number decides when to send a message in chat automatically. Default is 12. the lower the value, the more often a message is automatically generated and sent.
- ```-ping```: checks to see if the bot is alive
- ```-g```: force generate a message

By Default the bot is configured to use the GPT-4 api endpoint. If you dont have access to the GPT-4 api, you can change it in the main file for now. 

## Contributions
Contributions to this project are welcome. If you find a bug or want to add a new feature, feel free to create a pull request.
