import os
from flask import Flask, render_template, jsonify, request
from alpha_vantage.techindicators import TechIndicators
import openai
from config import ALPHA_VANTAGE_API_KEY, OPENAI_API_KEY

app = Flask(__name__)

# Initialize APIs
ti = TechIndicators(key=ALPHA_VANTAGE_API_KEY, output_format='json')
openai.api_key = OPENAI_API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explanation')
def explanation():
    return render_template('explanation.html')

@app.route('/api/stock/<symbol>')
def get_stock_data(symbol):
    try:
        timeframe = request.args.get('timeframe', '1 month')

        timeframe_mapping = {
            '3 day': 3,
            '1 week': 7,
            '1 month': 20,
            '6 months': 120,
            '1 year': 250
        }
        time_period = timeframe_mapping.get(timeframe, 20)

        # Technical Analysis
        sma_data, _ = ti.get_sma(symbol=symbol, interval='daily', time_period=time_period, series_type='close')
        ema_data, _ = ti.get_ema(symbol=symbol, interval='daily', time_period=time_period, series_type='close')
        macd_data, _ = ti.get_macd(symbol=symbol, interval='daily', series_type='close')
        rsi_data, _ = ti.get_rsi(symbol=symbol, interval='daily', time_period=time_period, series_type='close')
        bbands_data, _ = ti.get_bbands(symbol=symbol, interval='daily', time_period=time_period, series_type='close')

        # Get the most recent values
        latest_sma_date = max(sma_data.keys())
        sma = sma_data[latest_sma_date]['SMA']

        latest_ema_date = max(ema_data.keys())
        ema = ema_data[latest_ema_date]['EMA']

        latest_macd_date = max(macd_data.keys())
        macd = macd_data[latest_macd_date]['MACD']

        latest_rsi_date = max(rsi_data.keys())
        rsi = rsi_data[latest_rsi_date]['RSI']

        latest_bbands_date = max(bbands_data.keys())
        bbands_upper = bbands_data[latest_bbands_date]['Real Upper Band']
        bbands_middle = bbands_data[latest_bbands_date]['Real Middle Band']
        bbands_lower = bbands_data[latest_bbands_date]['Real Lower Band']

        technical_analysis = {
            'SMA': f"{float(sma):.2f}",
            'EMA': f"{float(ema):.2f}",
            'MACD': f"{float(macd):.2f}",
            'RSI': f"{float(rsi):.2f}",
            'BBANDS': f"Upper: {float(bbands_upper):.2f}, Middle: {float(bbands_middle):.2f}, Lower: {float(bbands_lower):.2f}"
        }

        # AI Analysis (Commented out to save API tokens)
        # prompt = f"Provide a detailed investment analysis for {symbol} based on the following technical indicators. "
        # prompt += "Give a recommendation for both short-term (weeks) and long-term (months to years) investment strategies. "
        # prompt += "Explain the reasoning behind your recommendations.\\n\\n"
        # for key, value in technical_analysis.items():
        #     prompt += f"- {key}: {value}\\n"

        # response = openai.chat.completions.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "system", "content": "You are a financial analyst providing investment advice."},
        #         {"role": "user", "content": prompt}
        #     ],
        #     max_tokens=250,
        #     temperature=0.7,
        # )
        # ai_analysis = response.choices[0].message.content.strip()
        ai_analysis = "AI analysis is currently disabled."

        data = {
            'symbol': symbol,
            'technical_analysis': technical_analysis,
            'ai_analysis': ai_analysis,
            'timeframe': timeframe
        }
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True) 