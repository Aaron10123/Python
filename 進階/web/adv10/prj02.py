#######################模組#######################
import discord
import os
from dotenv import load_dotenv
from myfunction import WeatherAPI
import openai
from myfunction import TurtleSoupGame

#######################初始化#######################
load_dotenv()  # 載入環境變數

# 建立機器人,並設定ˋintentsˋ已接受訊息內容
intents = discord.Intents.default()
intents.message_content = True  # 接受訊息內容的intent

bot = discord.Client(intents=intents)  # 建立一個Discord客戶端
tree = discord.app_commands.CommandTree(bot)  # 建立一個指令樹,用於管理slash指令

weather_api = WeatherAPI(os.getenv("WEATHER_API_KEY"))

openai.api_key = os.getenv("OPENAI_API_KEY")
game_manager = TurtleSoupGame(openai)


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

    elif game_manager.is_active_game(channel_id):  # 檢查頻道已經在遊戲中
        user_input = message.content.strip()  # 去掉空白字元
        if user_input == "結束遊戲":  # 如果輸入結束遊戲
            game_manager.end_game(channel_id)  # 將遊戲狀態從字典中刪除
            await message.channel.send("遊戲結束！")
        else:  # 繼續與玩家互動
            solved, response = await game_manager.process_answer(channel_id, user_input)
            if solved:
                await message.channel.send("恭喜答對!")
            else:
                await message.channel.send(response)


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
    if not forecast:
        info = weather_api.get_weather_info(city_name)
        embed = await weather_api.create_weather_embed(city_name, info)
        if embed:
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"找不到**{city_name}**的天氣信息")
    else:
        info = weather_api.get_forecast(city_name)
        if "list" in info:
            if not ai:  # 不使用AI
                embeds = await weather_api.create_forecast_embed(city_name, info)
                if embeds:
                    await interaction.followup.send(embeds=embeds)
            else:
                try:
                    analysis = await weather_api.analyze_weather(
                        city_name, info, openai
                    )
                    await interaction.followup.send(
                        f"**{city_name}的天氣情況**\n{analysis}"
                    )
                except Exception as e:
                    await interaction.followup.send(f"發生錯誤：{e}")
        else:  # 使用AI
            await interaction.followup.send(f"找不到**{city_name}**的天氣預報")


@tree.command(name="turtle_soup", description="開始遊戲")
async def turtle_soup(interaction: discord.Interaction):
    success, message = game_manager.start_game(interaction.channel.id)
    if success:
        await interaction.response.send_message(
            f"""遊戲開始！
 題目：{message}
 請大家開始提問，輸入 結束遊戲 可結束遊戲。
 我的回應只會是「是」、「不是」或「無可奉告」。"""
        )
    else:
        await interaction.response.send_message(message, ephemeral=True)


def main():
    # 啟動機器人,讀取環境變數
    bot.run(os.getenv("DC_BOT_TOKEN"))


# 主程式
if __name__ == "__main__":
    main()  # 執行主程式
