# Stonk Analyzer

Stonk Analyzer is a web-based application that provides in-depth technical analysis and AI-powered insights for publicly traded stocks. Users can quickly search for any stock symbol and receive a detailed breakdown of key technical indicators, an interactive chart, and an AI-generated investment analysis.

## Features

-   **Technical Indicator Analysis**: Get real-time values for the top five technical indicators:
    -   Simple Moving Average (SMA)
    -   Exponential Moving Average (EMA)
    -   Moving Average Convergence Divergence (MACD)
    -   Relative Strength Index (RSI)
    -   Bollinger Bands (BBANDS)
-   **AI-Powered Insights**: An AI-driven analysis of the technical indicators provides a detailed breakdown of each indicator's significance, along with short-term and long-term investment outlooks.
-   **Interactive Charts**: A dynamic TradingView chart is displayed for each searched stock, allowing for further personal analysis.
-   **Timeframe Selection**: Users can select different timeframes (from 3 days to 1 year) to tailor the analysis to their needs.
-   **Indicator Explanations**: A dedicated page provides clear explanations for each of the technical indicators used in the analysis.
-   **Password Protected**: The application is secured with a simple password protection layer.

## Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

-   Python 3.x
-   An API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
-   An API key from [OpenAI](https://platform.openai.com/api-keys)

### Steps

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/StonkAnalyzer.git
    cd StonkAnalyzer
    ```

2.  **Create and activate a virtual environment:**
    It is highly recommended to use a virtual environment to manage project dependencies.

    -   **Create the environment:**
        ```sh
        python -m venv venv
        ```
    -   **Activate the environment:**
        -   On Windows:
            ```sh
            .\\venv\\Scripts\\activate
            ```
        -   On macOS and Linux:
            ```sh
            source venv/bin/activate
            ```

3.  **Create a configuration file:**
    Create a file named `config.py` in the root directory and add your API keys, a secret key for session management, and a password for the application.

    ```python
    # config.py
    ALPHA_VANTAGE_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
    SECRET_KEY = "your_super_secret_key"
    PASSWORD = "your_password"
    ```

4.  **Install dependencies:**
    Ensure your virtual environment is activated, then run:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1.  **Activate your virtual environment (if not already active):**
    -   On Windows:
        ```sh
        .\\venv\\Scripts\\activate
        ```
    -   On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

2.  **Run the application:**
    ```sh
    flask run
    ```
    Or, if the `flask` command is not available directly:
    ```sh
    python -m flask run
    ```

3.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000/`.

4.  **Login:**
    You will be prompted to enter the password you set in the `config.py` file.

5.  **Analyze a stock:**
    -   Enter a stock symbol (e.g., AAPL, GOOGL) into the search bar.
    -   Select your desired timeframe from the dropdown menu.
    -   Click the "Search" button.

The application will then display the technical analysis, AI insights, and the TradingView chart for the selected stock.

---
_**Note:** This application is for educational purposes only and should not be considered financial advice._ 