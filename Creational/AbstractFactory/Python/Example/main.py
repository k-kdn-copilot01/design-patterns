from windows_factory import WindowsFactory
from mac_factory import MacFactory
from client import Application

def main():
    print("Using Windows Factory:")
    win_app = Application(WindowsFactory())
    win_app.render()

    print("\nUsing Mac Factory:")
    mac_app = Application(MacFactory())
    mac_app.render()

if __name__ == "__main__":
    main()
