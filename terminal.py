from prompt_toolkit import PromptSession
from commands import list_dir, change_dir, make_dir, remove, pwd, system_info

def main():
    session = PromptSession()
    print("🚀 Welcome to CodeMate Terminal (Python-based) 🚀")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = session.prompt("codemate> ").strip().split()
            if not user_input:
                continue

            cmd = user_input[0]
            args = user_input[1:]

            if cmd == "exit":
                print("Goodbye 👋")
                break
            elif cmd == "ls":
                print(list_dir())
            elif cmd == "cd":
                print(change_dir(args[0]) if args else "Usage: cd <directory>")
            elif cmd == "mkdir":
                print(make_dir(args[0]) if args else "Usage: mkdir <dirname>")
            elif cmd == "rm":
                print(remove(args[0]) if args else "Usage: rm <path>")
            elif cmd == "pwd":
                print(pwd())
            elif cmd == "sysinfo":
                print(system_info())
            else:
                print(f"Unknown command: {cmd}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
