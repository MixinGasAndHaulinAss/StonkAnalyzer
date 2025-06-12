# StonkAnalyzer

StonkAnalyzer is a web application that provides real-time stock analysis using technical indicators and AI-powered insights. Users can search for a stock symbol and receive an analysis of the stock's potential for long and short-term investment.

## Features

*   **Real-time Stock Data**: Fetches up-to-date stock prices and technical indicators from the Alpha Vantage API.
*   **Technical Analysis**: Displays the top five key technical indicators:
    *   Simple Moving Average (SMA)
    *   Exponential Moving Average (EMA)
    *   Moving Average Convergence Divergence (MACD)
    *   Relative Strength Index (RSI)
    *   Bollinger Bands
*   **AI-Powered Insights**: Uses the OpenAI API to generate a detailed analysis for long and short-term investment strategies based on the technical indicators.
*   **Explanations Page**: A dedicated page explaining each technical indicator with visual aids.

## Technology Stack

*   **Backend**: Python, Flask
*   **Frontend**: HTML, CSS, JavaScript
*   **APIs**: Alpha Vantage API, OpenAI API

## Installation

Follow these steps to set up the project locally.

### Prerequisites

*   Python 3.x
*   An API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
*   An API key from [OpenAI](https://platform.openai.com/api-keys)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/StonkAnalyzer.git
    cd StonkAnalyzer
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    *   On Windows, activate it with:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux, activate it with:
        ```bash
        source venv/bin/activate
        ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys:**
    *   Create a file named `config.py` in the root directory.
    *   Add your API keys to this file as follows:

    ```python
    # config.py
    ALPHA_VANTAGE_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
    ```
    **Note:** The `config.py` file is included in the `.gitignore` file to prevent your API keys from being committed to version control.

## Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Open your web browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

3.  **Use the application:**
    *   Enter a stock symbol (e.g., `AAPL`, `GOOGL`) in the search bar and click "Get Analysis".
    *   The application will display the technical analysis and AI-generated insights.
    *   Use the navigation bar to visit the "Explanation" page to learn more about the technical indicators.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details. 