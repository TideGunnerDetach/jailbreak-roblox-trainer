import unittest
from unittest.mock import patch, MagicMock
from jailbreak_roblox_trainer.trainer import JailbreakTrainer
from jailbreak_roblox_trainer.config import Config

class TestJailbreakTrainer(unittest.TestCase):
    def setUp(self):
        self.config = Config(interval=0.1, auto_arrest=True, auto_escape=False)
        self.trainer = JailbreakTrainer(self.config)

    @patch('pyautogui.press')
    @patch('pyautogui.click')
    def test_arrest_player(self, mock_click, mock_press):
        self.trainer._arrest_player()
        mock_press.assert_called_once_with('e')
        mock_click.assert_called_once_with(button='left')

    @patch('jailbreak_roblox_trainer.trainer.JailbreakTrainer._execute_actions')
    def test_start_stop(self, mock_execute):
        with patch('time.sleep', side_effect=KeyboardInterrupt):
            self.trainer.start()
        self.assertFalse(self.trainer.running)
        mock_execute.assert_called()