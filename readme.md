# PotterBot

Introducing a magical Discord bot inspired by the enchanting world of Harry Potter! PotterBot is a Discord bot that brings the magic of the Harry Potter universe to your server. It provides an interactive game where users can immerse themselves in the wizarding world, casting spells, exploring Hogwarts, and even riding the Hogwarts Express.

## Table of Contents

- [Track and Contributors](#Track-and-Contributors)
- [Problem Statement](#Problem-Statement)
- [Goal](#Goal)
- [Features and How to run](#Features-and-How-to-run)
- [Tech Stack](#Tech-Stack)
- [Deployment](#Deployment)
- [Applications of your idea](#Applications-of-your-idea)
- [Further improvements](#Further-improvements)
- [Demo video](#Demo-video)


## Track and Contributors
***Track***: Discord-Arcade

***Contributors***:

- Vriddhi Agrawal (IMT2023611)
- Snehal Sharma (IMT2023572)
- Gathik Jindal (IMT2023089)

## Problem Statement
Making an arcade themed bot.
## Goal
To create a Discord bot that brings the magic of the Harry Potter universe to your server.
## Features and How to run

- Separate channels
  - When the bot is added to a server, it creates a separate category called 'Potterbot' with channels for different purposes.
- Introductory quests
  - Write the command `~revelio` on the 'general' channel in the Potterbot category of the server to start the introductory quests.
  - The introductory quests take you through:
    - Hogwarts Express
    - Sorting Hat Ceremony
    - Ollivanders - Wand Selection
    - Hogwarts Staircase
- Beyond Introduction
   - After you complete the introductory quests, you can explore the other channels offering various fun games and features:
      - ***Multiplayer features*** (Dueling Club): Go to the dueling-club channel and type ~duel and tag a player(seperated by a space) to challenge them to a duel.(`~duel @discordUsername`)
      - Forbidden Forest: Go to the forbidden-forest channel and type `~explore` to explore the forbidden forest. You will encounter enemies who will challenge you to a duel.
      - NEWTs: Go to the newts channel and type `~trivia` to take a NEWT exam. You will be asked a series of questions and your score will be calculated at the end.
      - Mini Games
          - Word Chain: Go to the mini-games channel and type `~wordChain` to start a word chain game.
          - Crossword: Go to the mini-games channel and type `~crossword` to start a crossword game.
          - Emoji Guess: Go to the mini-games channel and type `~emoGuess` to start an emoji guessing game.
- Data: The bot stores the user data and house data in a JSON file. When an existing user types a command, they don't have to do any authentication again as the bot automatically fetches their info based on their discord id.
- Stats: Users can use the following commands to check their stats:
  - `~myStats` to check their stats.
  - `~houseStats` to check their house info.
  - `~leaderboard` to check the house standings.
- Natural interactions: We have tried our best to take into account most situations that could occur during an interaction so that the user experience is smooth.(The hardest part considering that the user could message anything anywhere)

## Tech Stack

- Discord.py
- Python
- JSON
- GitHub

## Deployment(if done)

Up and running on a Discord server. The bot is currently deployed on a server and can be invited to any server using the following link:
[Invite PotterBot](https://discord.com/oauth2/authorize?client_id=1223251110777716738&permissions=8&scope=bothttps://discord.com/oauth2/authorize?client_id=1223251110777716738&permissions=8&scope=bot)

## Applications of your idea

Endless entertainment for Harry Potter fans on Discord servers. The bot can be used in Harry Potter themed servers to provide an interactive experience to the users. It can also be used in general servers to provide a fun and engaging experience to the users.

## Further improvements

Things that we could have added given more time:
- Open, choice based story mode.
- Shops: Although we have currency which can be used to buy keys in games, we have not implemented a shop where users can buy items.
- Implementing and integrating items like potions, brooms, etc.

## Demo video (youtube link)