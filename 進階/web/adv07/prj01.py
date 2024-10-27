#######################模組#######################
import discord
import os
from dotenv import load_dotenv
from myfunction.myfunction import WeatherAPI

#######################初始化#######################
load_dotenv()  # 載入環境變數

# 建立機器人,並設定ˋintentsˋ已接受訊息內容
intents = discord.Intents.default()
intents.message_content = True  # 接受訊息內容的intent

bot = discord.Client(intents=intents)  # 建立一個Discord客戶端
tree = discord.app_commands.CommandTree(bot)  # 建立一個指令樹,用於管理slash指令

weather_api = WeatherAPI(os.getenv("WEATHER_API_KEY"))


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")  # 在機器人啟動後印出訊息
    await tree.sync()  # 同步指令至伺服器


@bot.event
async def on_message(message):
    if message.author == bot.user:  # 避免自己回覆自己
        return  # 結束函式
    if message.content == "hello":
        await message.channel.send("Hello!")


#######################指令#######################
@tree.command(name="hello", description="回傳Hello!")
async def hello(interaction: discord.Interaction):
    """輸入hello即可回傳Hello!"""
    await interaction.response.send_message("Hello!")  # 回傳Hello!


# 天氣指令,可以選擇當前天氣或未來預報
@tree.command(name="weather", description="取得天氣資訊")
async def weather(
    interaction: discord.Interaction, city_name: str, forecast: bool = False
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
                embed.add_field(name="溫度", value=f"{temp}{unit_symbol}", inline=False)
                embeds.append(embed)
            await interaction.followup.send(embeds=embeds)
        else:
            await interaction.followup.send("查詢失敗")


def main():
    # 啟動機器人,讀取環境變數
    bot.run(os.getenv("DC_BOT_TOKEN"))


# 主程式
if __name__ == "__main__":
    main()  # 執行主程式
