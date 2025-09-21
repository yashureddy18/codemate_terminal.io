# 📘 CodeMate AI Terminal Assignment

## Overview
This project implements a **Python-based AI-enhanced command terminal** for the CodeMate Hackathon.  

It combines:

- Standard terminal commands: `ls`, `cd`, `mkdir`, `rm`, `pwd`, `sysinfo`  
- **AI natural language commands** via **Ollama LLaMA3**  
- Command history and autocomplete using `prompt_toolkit`  
- Fully compatible with **CodeMate Build** and **CodeMate Extension**  

This is a **single-file implementation (`main.py`)**, so all functionality is in one place for simplicity.

---

## Folder Structure
codemate_assignment/
│── main.py # Entry point with AI and terminal commands
│── .cmd_history # Command history (auto-generated)
│── README.md # This file

---

## Features

### 1. Basic Commands
| Command   | Description                           |
|-----------|---------------------------------------|
| `ls`      | List files and directories            |
| `cd`      | Change directory                      |
| `mkdir`   | Create a new directory                |
| `rm`      | Delete file or directory              |
| `pwd`     | Show current working directory        |
| `sysinfo` | Show CPU and memory usage             |
| `exit`    | Quit the terminal                     |

### 2. AI Commands
Use the `ai` command to type natural language requests:
ai create a folder called test
ai show CPU and memory usage
ai delete test
The AI interprets your instructions and executes the corresponding terminal commands automatically.

### 3. Command History & Autocomplete

Navigate history with up/down arrows

Auto-complete commands using Tab
Setup Instructions

Install Python dependencies:
py -m pip install prompt_toolkit requests psutil

Run Ollama LLaMA3 locally:
ollama run llama3

Run the terminal:
py main.py

#Use exit to quit or ai <natural language request> for AI commands.
