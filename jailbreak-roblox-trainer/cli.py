import argparse
from .trainer import JailbreakTrainer
from .config import Config

def main():
    parser = argparse.ArgumentParser(description="Jailbreak Roblox Trainer")
    parser.add_argument("--interval", type=float, default=1.0, help="Action interval in seconds")
    parser.add_argument("--auto-arrest", action="store_true", help="Enable auto-arrest")
    parser.add_argument("--auto-escape", action="store_true", help="Enable auto-escape")

    args = parser.parse_args()
    config = Config(
        interval=args.interval,
        auto_arrest=args.auto_arrest,
        auto_escape=args.auto_escape
    )

    trainer = JailbreakTrainer(config)
    trainer.start()

if __name__ == "__main__":
    main()