from rtmbot import RtmBot
from rtmbot.core import Plugin

import secret
import chatlogic


    # if "똥글" in data["text"]:
    #     self.outputs.append([data["channel"], "세계최강귀요미가 맞다."])
    # elif "주사위" == data["text"]:
    #     die = str(random.randint(1, 6))
    #     self.outputs.append([data["channel"], die])
    # elif "채원" in data["text"]:
    #     self.outputs.append([data["channel"], "바보ㅡ3ㅡ"])
    # else:
    #     pass


class HelloPlugin(Plugin):
    def process_message(self, data):
        reply = answer(data["text"])
        if reply is not None:
            self.outputs.append([data["channel"],reply])



config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
