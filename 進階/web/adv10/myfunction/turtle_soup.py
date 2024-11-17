import openai
import json
import random
import os
import sys


class TurtleSoupGame:
    def __init__(self, openai_client: openai):
        self.openai_client = openai_client
        self.games = {}
        self.questions = []

    def load_questions(self):
        """從JSON檔案載入題目"""
        try:
            os.chdir(sys.path[0])
            json_path = "turtle_soup.json"
            with open(json_path, "r", encoding="utf-8") as f:
                self.questions = json.load(f)
        except Exception as e:
            print(f"載入題目失敗：{e}")
            self.questions = [
                {
                    "question": "一名女孩夜裡聽到滴水聲，伸手確認被狗舔後安心睡去。隔天發現狗的屍體被吊在天花板上。發生了什麼事？",
                    "answer": "強盜闖入女孩家並殺了狗，將狗屍吊在天花板上。女孩聽到的滴水聲是狗屍血滴聲，強盜假裝狗舔她的手安撫她，以免她發現異常",
                    "solved": False,
                },
            ]

    def start_game(self, channel_id):
        """開始新遊戲"""
        if channel_id in self.games:
            return False, "正在遊戲中，請勿重複開始"

        self.load_questions()
        selected_question = random.choice(self.questions).copy()
        self.games[channel_id] = {
            "game_date": selected_question,
            "history": [],
        }
        return True, self.games[channel_id]["game_date"]["question"]

    def end_game(self, channel_id):
        """結束遊戲"""
        if channel_id in self.games:
            self.games.pop(channel_id)
            return True
        return False

    async def process_answer(self, channel_id, user_input):
        """處理用戶的回應"""
        if channel_id not in self.games:
            return None, "沒有進行中的遊戲"
        game_date = self.games[channel_id]
        history = game_date.setdefault("history", [])
        history.append({"role": "user", "content": user_input})
        messages = (
            [
                {
                    "role": "user",
                    "content": f"""你是一個海龜湯遊戲的主持人,
                         根據以下的謎題回答玩家的提問。你的回應只能是「是」、「不是」、「無可奉告」、「恭喜答對!」,
                         並盡可能簡短,當玩家要求提示的時候,你可以提供"關鍵字"當作提示。
                         謎題:{game_date["game_date"]["question"]}解答:{game_date["game_date"]["answer"]}""",
                }
            ]
            + history
        )
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.5,
            )
            answer = response.choices[0].message.content
            if answer == "恭喜答對!":
                game_date["game_date"]["solved"] = True
                self.end_game(channel_id)
                return True, answer
            else:
                history.append({"role": "assistant", "content": answer})
                return False, answer
        except Exception as e:
            return None, f"除理回答時發生錯誤：{str(e)}"

    def is_active_game(self, channel_id):
        """檢查頻道是否正在遊戲中"""
        return channel_id in self.games
