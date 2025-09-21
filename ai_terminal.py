import os
import requests
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from commands import list_dir, change_dir, make_dir, remove, pwd, system_info

# -------------------------------
# Configuration for Ollama local AI
# -------------------------------
OLLAMA_URL = "http://localhost:11434/api/chat"  # Local Ollama API
MODEL_NAME = "llama3"

def ask_ollama(prompt: str) -> str:
    """Send natural language command to Ollama LLaMA3 and get the interpreted command."""
    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(OLLAMA_URL, json=data, stream=False)
        if response.status_code == 200:
            return response.json()["message"]["content"].strip()
        else:
            return f"AI Error: {response.text}"
    except Exception as e:
        return f"AI connection error: {e}"

# -------------------------------
# Autocomplete for terminal commands
# -------------------------------
commands_list = ["ls", "cd", "mkdir", "rm", "pwd", "sysinfo", "exit", "ai"]
command_completer = WordCompleter(commands_list, ignore_case=True)

# -------------------------------
# Execute standard commands
# -------------------------------
def execute_command(cmd, args):
    if cmd == "ls":
        return list_dir()
    elif cmd == "cd":
        return change_dir(args[0]) if args else "Usage: cd <directory>"
    elif cmd == "mkdir":
        return make_dir(args[0]) if args else "Usage: mkdir <dirname>"
    elif cmd == "rm":
        return remove(args[0]) if args else "Usage: rm <path>"
    elif cmd == "pwd":
        return pwd()
    elif cmd == "sysinfo":
        return system_info()
    else:
        return f"Unknown command: {cmd}"

# -------------------------------
# Main terminal loop
# -------------------------------
def main():
    session = PromptSession(
        history=FileHistory(".cmd_history"),
        completer=command_completer
    )

    print("🚀 Welcome to AI CodeMate Terminal 🚀")
    print("Type 'exit' to quit. Use 'ai' for natural language commands.\n")

    while True:
        try:
            user_input = session.prompt("codemate> ").strip().split()
            if not user_input:
                continue

            cmd = user_input[0]
            args = user_input[1:]

            if cmd.lower() == "exit":
                print("Goodbye 👋")
                break
            elif cmd.lower() == "ai":
                if not args:
                    print("Usage: ai <your natural language request>")
                    continue
                nl_request = " ".join(args)
                interpreted = ask_ollama(nl_request)
                print(f"🤖 AI interpreted: {interpreted}")
                parts = interpreted.split()
                print(execute_command(parts[0], parts[1:]))
            else:
                print(execute_command(cmd, args))

        except KeyboardInterrupt:
            print("\nInterrupted. Type 'exit' to quit.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
