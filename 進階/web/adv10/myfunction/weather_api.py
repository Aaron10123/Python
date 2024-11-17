import requests
import openai
import discord


class WeatherAPI:
    def __init__(self, api_key, units="metric", lang="zh-tw"):
        self.api_key = api_key
        self.units = units
        self.lang = lang
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast?"
        self.icon_base_url = "https://openweathermap.org/img/wn/"

    def get_weather_info(self, city_name):
        send_url = f"{self.base_url}appid={self.api_key}&q={city_name}&units={self.units}&lang={self.lang}"
        response = requests.get(send_url)
        return response.json()

    def get_forecast(self, city_name):
        send_url = f"{self.forecast_url}q={city_name}&appid={self.api_key}&units={self.units}&lang={self.lang}"
        response = requests.get(send_url)
        response.raise_for_status()
        return response.json()

    def get_icon_url(self, icon_code):
        return f"{self.icon_base_url}{icon_code}@2x.png"

    def get_icon(self, icon_code):
        icon_url = self.get_icon_url(icon_code)
        response = requests.get(icon_url)
        if response.status_code == 200:
            return response.content
        else:
            return None

    async def create_weather_embed(self, city, weather_info):
        """建立天氣資訊的 discord embed"""
        unit_symbol = "°C" if self.units == "metric" else "°F"
        if "weather" in weather_info and "main" in weather_info:
            current_temperature = weather_info["main"]["temp"]
            weather_description = weather_info["weather"][0]["description"]
            icon_code = weather_info["weather"][0]["icon"]
            icon_url = self.get_icon_url(icon_code)
            embed = discord.Embed(
                title=f"{city}的天氣",
                description=f"描述: {weather_description}",
                color=0x1E90FF,
            )
            embed.set_thumbnail(url=icon_url)
            embed.add_field(
                name="溫度", value=f"{current_temperature}{unit_symbol}", inline=False
            )
            return embed
        return None

    async def create_forecast_embed(self, city, forecast_info):
        """建立天氣預報的 discord embed列表"""
        unit_symbol = "°C" if self.units == "metric" else "°F"
        embeds = []

        if "list" in forecast_info:
            forecast_list = forecast_info["list"][:10]

            for forecast in forecast_list:
                dt_text = forecast["dt_txt"]
                temp = forecast["main"]["temp"]
                descripiton = forecast["weather"][0]["description"]
                icon_code = forecast["weather"][0]["icon"]
                icon_url = self.get_icon_url(icon_code)
                embed = discord.Embed(
                    title=f"{city}的天氣預報 - {dt_text}",
                    description=f"描述: {descripiton}",
                    color=0x1E90FF,
                )
                embed.set_thumbnail(url=icon_url)
                embed.add_field(name="溫度", value=f"{temp}{unit_symbol}", inline=False)
                embeds.append(embed)

        return embeds

    async def analyze_weather(self, city_name, forecast_date, openai_client: openai):
        """分析天氣預報數據並提供建議"""
        try:
            response = openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "你是一個天氣預報分析器，請根據天氣預報數據來回答以下問題：",
                    },
                    {
                        "role": "user",
                        "content": f"我想知道{city_name}的天氣情況，請根據以下天氣資訊回答我:\n{forecast_date}",
                    },
                ],
                temperature=0.2,
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"發生錯誤：{str(e)}")
