import json
from ..keyboard.button import ButtonConfig


class Config:

    def __init__(self):
        with open('/config.json') as _f:
            self.config = json.load(_f)

    def __getitem__(self, button_cfg: ButtonConfig) -> ButtonConfig:
        btn_name = "BTN_{:02d}".format(button_cfg.index)
        if btn_name not in self.config:
            return button_cfg
        config = self.config[btn_name]
        button_cfg.action = config['action']
        return button_cfg
