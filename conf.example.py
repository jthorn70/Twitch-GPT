class Conf:
    # Hard conf dont change unless you know what you are doing
    server = 'irc.chat.twitch.tv'
    port = 6667

    # Bot account conf
    # Lowercase name
    nickname = "Your Bot's name"
    # oauth generate with https://twitchapps.com/tmi/
    token = "twitch oauth token"
    # openai API key
    openai_key = "openai key"

    # Lowercase channel to join.
    channel = "enter channel name here"

    # Add users to ignore, lowercase. add as many as you want.
    ignoredUsers = [
        "Enter",
        "Users",
        "who",
        "should",
        "be",
        "ignored",
        "here",
        "lowercase",
    ]

    # Add mods who can use commands, lowercase.
    mods = ['enter',
            'mods',
            'names',
            'here',
            'lowercase'
            ]

    CMD_TOGGLE = "-toggle"

    CMD_CLEAR = "-refreshing"
    CMD_WIPE = "-wipe"
    CMD_SET_NUMBER = "-number"
    CMD_ALIVE = "-ping"
    CMD_UNIQUE = "-unique"
    CMD_EXIT = "-exit"
    CMD_GEN = "-g"

    SELF_PREFIX = "Maintenance Message: "

    # Your Twitch name, lowercase.
    owner = "Your Twitch name, lowercase."

    # THESE ARE WORDS THE BOT SHOULD NEVER LEARN.
    # I FEEL DISGUSTING TYPING THEM.
    # BUT BY THIS LIST EXISTING THEY WILL NOT PERPETUATE.
    # Some are here to keep the bot from being political.

    # I didn't want to commit them to GitHub.
    # Add your own, case insensitive.
    blacklisted_words = ['enter', 'bad', 'words', 'here', 'case sensitive']
