import os
from flask import Flask, render_template, jsonify, request, session, redirect, url_for, flash
from alpha_vantage.techindicators import TechIndicators
import openai
from config import ALPHA_VANTAGE_API_KEY, OPENAI_API_KEY, SECRET_KEY, PASSWORD

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Initialize APIs
ti = TechIndicators(key=ALPHA_VANTAGE_API_KEY, output_format='json')
openai.api_key = OPENAI_API_KEY

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Wrong password!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/explanation')
def explanation():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('explanation.html')

@app.route('/api/stock/<symbol>')
def get_stock_data(symbol):
    if not session.get('logged_in'):
        return jsonify({'error': 'Not logged in'}), 401
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

        # AI Analysis
        technical_analysis_str = ""
        for key, value in technical_analysis.items():
            technical_analysis_str += f"- {key}: {value}\\n"

        prompt = f"""Analyze the investment potential of {symbol} based on the following technical indicators:
{technical_analysis_str}
Please structure your analysis with the following headers, using markdown bold (e.g., **Indicator Breakdown**):

**Indicator Breakdown:**
- **SMA:** Explain the significance of the current SMA value.
- **EMA:** Explain the significance of the current EMA value.
- **MACD:** Explain the significance of the current MACD value.
- **RSI:** Explain the significance of the current RSI value.
- **BBANDS:** Explain the significance of the current BBANDS value.

**Overall Analysis:**
**Short-Term Outlook (weeks):**
**Long-Term Outlook (months to years):**
"""

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial analyst providing investment advice. Format your response using markdown bold for headers as requested."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400,
            temperature=0.7,
        )
        ai_analysis = response.choices[0].message.content.strip()

        # Format for HTML
        parts = ai_analysis.split('**')
        for i in range(1, len(parts), 2):
            parts[i] = f'<strong>{parts[i]}</strong>'
        ai_analysis = "".join(parts)
        ai_analysis = ai_analysis.replace('\\n', '<br>').replace('\n', '<br>')

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