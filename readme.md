# Brisbane 天气预报机器人

一个自动获取布里斯班天气信息并生成友好消息的 Python 脚本。

## 功能特点

- 🌤 自动获取布里斯班明天的天气预报
- 🌡 显示最高温和最低温
- 🌧 显示降水概率
- 🌅 显示日落时间
- 💝 随机生成温馨的祝福语
- 🎨 自动添加随机表情符号
- 🕒 基于布里斯班时区的时间显示

## 技术实现

- 使用 WeatherAPI 获取天气数据
- 使用 pytz 处理时区问题
- 支持多种随机祝福语和表情组合

## 配置要求

### 依赖包
```bash
pip install -r requirements.txt
```

### 环境变量
```bash
APIKEY=your_weather_api_key
```