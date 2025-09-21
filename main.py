# main.py
import terminal.py
import ai_terminal.py

def choose_terminal():
    choice = input("Choose terminal: 1=Basic, 2=AI: ").strip()
    if choice == "1":
        terminal.main()
    elif choice == "2":
        ai_terminal.main()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    choose_terminal()
