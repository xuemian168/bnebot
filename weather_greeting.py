import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime, timedelta
import pytz
import os
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

def get_brisbane_weather():
    API_KEY = os.getenv('APIKEY')
    if not API_KEY:
        print("错误：未在.env文件中找到APIKEY")
        return None
        
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q=Brisbane&days=2&aqi=no"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # 获取明天的预报数据
        tomorrow_forecast = data['forecast']['forecastday'][1]['day']
        
        return {
            'list': [{
                'main': {
                    'temp_min': tomorrow_forecast['mintemp_c'],
                    'temp_max': tomorrow_forecast['maxtemp_c']
                },
                'pop': tomorrow_forecast['daily_chance_of_rain'] / 100
            }]
        }
        
    except Exception as e:
        print(f"获取天气数据时出错: {e}")
        return None

def get_sunset_time():
    brisbane_tz = pytz.timezone('Australia/Brisbane')
    current_time = datetime.now(brisbane_tz)
    
    # 这里需要使用另一个API调来获取准确的日落时间
    # 为简化示例，这里使用固定时间
    return "17:52"

def generate_random_greeting():
    greetings = [
        "祝大家有个美好的一天~",
        "愿你有一天充满阳光~",
        "今天也要开开心心哦~",
        "祝大家心想事成~",
        "愿每一天都精彩纷呈~",
        "愿你的梦想都能实现~",
        "祝你天天开心快乐~",
        "愿你前程似锦~",
        "祝你学业进步~",
        "愿你遇见最美好的自己~",
        "祝你前行的路上有温暖的阳光~",
        "愿你的生活甜甜蜜蜜~",
        "祝你平安喜乐，万事胜意~",
        "愿你所求皆所愿~",
        "祝你前程似锦，未来可期~",
        "愿你遇见更好的自己~",
        "祝你梦想成真~",
        "愿你的笑容比阳光更灿烂~",
        "祝你每天都元气满满~",
        "愿你所有的期待都能成真~"
    ]
    
    emojis = ["🌻", "🫧", "🍦", "🍾", "✨", "🌈", "🎉", "🌸", "🍀", "💫", 
              "🌺", "🎨", "🌙", "⭐", "🌹", "🍭", "🎵", "🌞", "🦋", "🎊",
              "🍀", "🌈", "💝", "💫", "🌟", "🎀", "💐", "🌼", "🎭", "💕"]
    
    greeting = random.choice(greetings)
    emoji_count = random.randint(2, 5)  # 增加了可能出现的表情数量
    selected_emojis = ''.join(random.sample(emojis, emoji_count))
    
    return f"{greeting}{selected_emojis}"

def generate_weather_message():
    weather_data = get_brisbane_weather()
    if not weather_data:
        return "无法获取天气数据"
    
    brisbane_tz = pytz.timezone('Australia/Brisbane')
    tomorrow = datetime.now(brisbane_tz).date() + timedelta(days=1)
    
    # 获取明天的温度范围
    temp_min = round(weather_data['list'][0]['main']['temp_min'])
    temp_max = round(weather_data['list'][0]['main']['temp_max'])
    
    # 获取降水概率
    rain_prob = int(weather_data['list'][0]['pop'] * 100)
    
    # 生成三个不同的消息示例
    messages = []
    for _ in range(3):
        message = f"""🥳学霸们晚上好！
💡每日晚间天气预报来啦~！
布里斯班明天{tomorrow.month}月{tomorrow.day}日，{['周一', '周二', '周三', '周四', '周五', '周六', '周日'][tomorrow.weekday()]}，气温{temp_min}-{temp_max}度，{rain_prob}%概率有雨。
📍日落时间：{get_sunset_time()}
{"记得带个伞哦！" if rain_prob > 30 else ""}
{generate_random_greeting()}"""
        messages.append(message)
    
    # 用分隔线连接三个消息
    return "\n\n-------------------\n\n".join(messages)

if __name__ == "__main__":
    print(generate_weather_message())