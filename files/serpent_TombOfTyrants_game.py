from serpent.game import Game

from .api.api import TombOfTyrantsAPI

from serpent.utilities import Singleton


class SerpentTombOfTyrantsGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Tomb of Tyrants"

        kwargs["app_id"] = "340360"
        kwargs["app_args"] = None

        super().__init__(**kwargs)

        self.api_class = TombOfTyrantsAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "TOMB_OF_TYRANTS_LOGO_MENU": (15, 28, 206, 449),
            "RESTART_YES": (253, 816, 274, 857),
            "RESTART_NO": (278, 822, 300, 853),

            "NB_DAYS_STATE_GAME": (16, 30, 76, 89)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "MENU": {
                "extract": {
                    "gradient_size": 10,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 5,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
