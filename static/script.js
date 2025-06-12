document.addEventListener('DOMContentLoaded', () => {
    const searchBtn = document.getElementById('search-btn');
    const stockSearch = document.getElementById('stock-search');
    const stockDataContainer = document.getElementById('stock-data-container');

    searchBtn.addEventListener('click', () => {
        const symbol = stockSearch.value.toUpperCase();
        const timeframe = document.getElementById('timeframe-select').value;
        if (symbol) {
            console.log(`Fetching data for ${symbol} with timeframe ${timeframe}`);
            fetch(`/api/stock/${symbol}?timeframe=${encodeURIComponent(timeframe)}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Received data:', data);
                    displayStockData(data);
                    displayTradingViewChart(symbol, timeframe);
                })
                .catch(error => {
                    console.error('Error fetching stock data:', error);
                    stockDataContainer.innerHTML = `<p>Error fetching stock data: ${error.message}. Please check the console for more details.</p>`;
                });
        }
    });

    function displayStockData(data) {
        if (data.error) {
            stockDataContainer.innerHTML = `<p>${data.error}</p>`;
            return;
        }

        let html = `<h2>${data.symbol} - Analysis for ${data.timeframe}</h2>`;
        html += '<h3>Technical Analysis</h3>';
        html += '<ul>';
        for (const indicator in data.technical_analysis) {
            html += `<li><strong>${indicator}:</strong> ${data.technical_analysis[indicator]}</li>`;
        }
        html += '</ul>';
        html += '<h3>AI Analysis</h3>';
        html += `<p>${data.ai_analysis}</p>`;

        stockDataContainer.innerHTML = html;
    }

    function displayTradingViewChart(symbol, timeframe) {
        const chartContainer = document.getElementById('tradingview-chart-container');
        chartContainer.innerHTML = ''; // Clear previous chart

        let interval = 'D'; // Default to Daily
        if (timeframe === '6 months') {
            interval = 'W'; // Weekly
        } else if (timeframe === '1 year') {
            interval = 'M'; // Monthly
        } else if (timeframe === '3 day') {
            interval = '60'; // Hourly for very short term
        }

        new TradingView.widget({
            "width": "100%",
            "height": 400,
            "symbol": symbol,
            "interval": interval,
            "timezone": "Etc/UTC",
            "theme": "light",
            "style": "1",
            "locale": "en",
            "toolbar_bg": "#f1f3f6",
            "enable_publishing": false,
            "allow_symbol_change": true,
            "container_id": "tradingview-chart-container"
        });
    }
}); 