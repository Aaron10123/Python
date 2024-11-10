#######################模組#######################
import discord
import os
from dotenv import load_dotenv
from .myfunction import WeatherAPI
import openai

#######################初始化#######################
load_dotenv()  # 載入環境變數

# 建立機器人,並設定ˋintentsˋ已接受訊息內容
intents = discord.Intents.default()
intents.message_content = True  # 接受訊息內容的intent

bot = discord.Client(intents=intents)  # 建立一個Discord客戶端
tree = discord.app_commands.CommandTree(bot)  # 建立一個指令樹,用於管理slash指令

weather_api = WeatherAPI(os.getenv("WEATHER_API_KEY"))

openai.api_key = os.getenv("OPENAI_API_KEY")


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")  # 在機器人啟動後印出訊息
    await tree.sync()  # 同步指令至伺服器


@bot.event
async def on_message(message):
    channel_id = message.channel.id  # 获取頻道id

    if message.author == bot.user:  # 避免自己回覆自己
        return  # 結束函式
    if message.content == "hello":
        await message.channel.send("Hello!")

    elif channel_id in channel_games:  # 檢查頻道已經在遊戲中
        user_input = message.content.strip()  # 去掉空白字元
        if user_input == "結束遊戲":  # 如果輸入結束遊戲
            channel_games.pop(channel_id)  # 將遊戲狀態從字典中刪除
            await message.channel.send("遊戲結束！")
        else:  # 繼續與玩家互動
            game_date = channel_games[channel_id]["game_date"]  # 取得遊戲狀態
            if (
                "history" not in channel_games[channel_id]
            ):  # 如果沒有历史記錄,就加入历史記錄
                channel_games[channel_id]["history"] = []
            history = channel_games[channel_id]["history"]  # 縮短名稱
            history.append({"role": "user", "content": user_input})  # 加入历史記錄


# 以頻道為鍵key,遊戲狀態為value,這是一個全域變數,所有指令都可以存取
# 如果把字典當作全域變數,就不需要宣告global就可以直接修改字典裡的數值
channel_games = {}


#######################指令#######################
@tree.command(name="hello", description="回傳Hello!")
async def hello(interaction: discord.Interaction):
    """輸入hello即可回傳Hello!"""
    await interaction.response.send_message("Hello!")  # 回傳Hello!


# 天氣指令,可以選擇當前天氣或未來預報
@tree.command(name="weather", description="取得天氣資訊")
async def weather(
    interaction: discord.Interaction,
    city_name: str,
    forecast: bool = False,
    ai: bool = False,
):
    await interaction.response.defer()

    unit_symbol = "°C" if weather_api.units == "metric" else "°F"
    if not forecast:
        info = weather_api.get_weather_info(city_name)
        if "weather" in info and "main" in info:
            current_temperature = info["main"]["temp"]
            weather_description = info["weather"][0]["description"]
            icon_code = info["weather"][0]["icon"]
            icon_url = weather_api.get_icon_url(icon_code)
            embed = discord.Embed(
                title=f"{city_name}的當前天氣",
                description=f"溫度: {current_temperature}{unit_symbol}\n描述: {weather_description}",
                color=0x1E90FF,
            )
            embed.set_thumbnail(url=icon_url)
            embed.add_field(
                name="溫度", value=f"{current_temperature}{unit_symbol}", inline=False
            )
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send("查詢失敗")
    else:
        info = weather_api.get_forecast(city_name)
        if "list" in info:
            if not ai:
                forecast_list = info["list"][:10]
                embeds = []
                for forecast in forecast_list:
                    dt_text = forecast["dt_txt"]
                    temp = forecast["main"]["temp"]
                    descripiton = forecast["weather"][0]["description"]
                    icon_code = forecast["weather"][0]["icon"]
                    icon_url = weather_api.get_icon_url(icon_code)

                    embed = discord.Embed(
                        title=f"{city_name}的{dt_text}預報",
                        description=f"溫度: {temp}{unit_symbol}\n描述: {descripiton}",
                        color=0x1E90FF,
                    )
                    embed.set_thumbnail(url=icon_url)
                    embed.add_field(
                        name="溫度", value=f"{temp}{unit_symbol}", inline=False
                    )
                    embeds.append(embed)
                await interaction.followup.send(embeds=embeds)

            else:
                try:
                    response = openai.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {
                                "role": "system",
                                "content": "你是一個專業的氣象分析師，為使用者提供詳細的天氣資訊。",
                            },
                            {
                                "role": "user",
                                "content": f"我想知道{city_name}的天氣情況，請根據以下天氣資訊回答我:\n{info}",
                            },
                        ],
                        temperature=0.2,
                    )

                    analysis = response.choices[0].message.content
                    await interaction.followup.send(
                        f"**{city_name}的天氣情況**\n{analysis}"
                    )

                except Exception as e:
                    await interaction.followup.send(f"發生錯誤：{e}")
        else:
            await interaction.followup.send("查詢失敗")


@tree.command(name="turtle_soup", description="開始遊戲")
async def turtle_soup(interaction: discord.Interaction):
    channel_id = interaction.channel.id  # 获取頻道id
    if channel_id in channel_games:  # 檢查頻道已經在遊戲中
        await interaction.response.send_message(
            "正在遊戲中，請勿重複開始", ephemeral=True
        )

    else:  # 如果頻道沒有在遊戲中，就加入遊戲中
        channel_games[channel_id] = {
            "game_date": {
                "question": "一名女孩夜裡聽到滴水聲，伸手確認被狗舔後安心睡去。隔天發現狗的屍體被吊在天花板上。發生了什麼事？",
                "answer": "強盜闖入女孩家並殺了狗，將狗屍吊在天花板上。女孩聽到的滴水聲是狗屍血滴聲，強盜假裝狗舔她的手安撫她，以免她發現異常",
                "solved": False,
            },
            "history": [],
        }
        await interaction.response.send_message(
            f"""遊戲開始！
題目：{channel_games[channel_id]["game_date"]["question"]}
請大家開始提問，輸入 結束遊戲 可結束遊戲。
我的回應只會是「是」、「不是」或「無可奉告」。"""
        )


def main():
    # 啟動機器人,讀取環境變數
    bot.run(os.getenv("DC_BOT_TOKEN"))


# 主程式
if __name__ == "__main__":
    main()  # 執行主程式
