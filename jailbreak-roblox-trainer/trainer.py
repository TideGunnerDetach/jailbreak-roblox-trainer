import pyautogui
import time
from .config import Config

class JailbreakTrainer:
    def __init__(self, config: Config):
        self.config = config
        self.running = False

    def start(self):
        self.running = True
        print("Jailbreak Trainer started. Press Ctrl+C to stop.")
        try:
            while self.running:
                self._execute_actions()
                time.sleep(self.config.interval)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.running = False
        print("Jailbreak Trainer stopped.")

    def _execute_actions(self):
        if self.config.auto_arrest:
            self._arrest_player()
        if self.config.auto_escape:
            self._escape_jail()

    def _arrest_player(self):
        pyautogui.press('e')
        time.sleep(0.1)
        pyautogui.click(button='left')

    def _escape_jail(self):
        pyautogui.keyDown('w')
        time.sleep(0.5)
        pyautogui.keyUp('w')