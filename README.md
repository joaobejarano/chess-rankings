# Chess Rankings

This project collects and analyzes data from classical chess players using the Lichess API. The project includes methods to fetch the rating history of the last 30 days of the top players and generate CSV reports.

## Main Solution
### Prerequisites

Before running the project, make sure you have installed:

- Python 3.7 or higher
- pip to manage Python packages

### Step by Step Configuration

1. Clone the Repository:

    Clone the repository to the local machine using the command:

    ```bash
    git clone https://github.com/seu-usuario/chess-rankings.git
    ```

2. Create and Activate the Virtual Environment:

    In the project root directory, create a virtual environment to manage dependencies:

    ```bash
    # Linux/MacOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    venv\Scripts\activate
    ```

    Make sure the virtual environment is activated (you should see (venv) at the top of the terminal prompt).

3. Install Dependencies:

    Install all required libraries and dependencies listed in requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```
4. PYTHONPATH Configuration:

    Make sure the src directory is in your PYTHONPATH to ensure modules are recognized correctly.

    ```bash
    # Linux/MacOS
    export PYTHONPATH=$(pwd)/src

    # Windows
    set PYTHONPATH=%cd%\src
    ```

5. Run the Main Script:

    After setting up the environment, run the main.py script to generate the CSV report:

    ```bash
    # Linux/MacOS e Windows
    python src/chess/main.py
    ```

    This will fetch the data of the top 50 classical chess players and save the rating history in a CSV file inside the output/ folder.


## Alternative Solution

This project is an evolution of the original chess data analysis system, previously developed in a simple format and executed locally. The new version has been restructured using FastAPI to improve scalability, organization and facilitate the consumption of data in a centralized and optimized way. The original project implemented the data search and processing functionalities using local methods and scripts executed directly. The new architecture with FastAPI allows these functionalities to be exposed as an API with accessible and standardized endpoints.

### Features

This API has three main endpoints that replicate the functionality of the original project:

1. List the Top 50 Classical Chess Players:

- Endpoint: `/top_50_classical_players`
- Method: GET
- Returns a list of the usernames of the top 50 classical chess players.

2. Get the Rating History of the Top 1 Player:

- Endpoint: `/last_30_day_rating_for_top_player`
- Method: GET
- Returns the rating history of the last 30 days for the player at the top of the classical chess rankings.

3. Generate a CSV File with the History of the Top 50 Players:

- Endpoint: `/rating_csv_for_top_50_classical_players`
- Method: POST
- Generates a CSV file containing the rating history of the last 30 days of the top 50 classical chess players and saves it in the output/ directory.

### Prerequisites

Before running the project, make sure you have installed:

- Python 3.7 or higher
- pip to manage Python packages

### Step by Step Configuration

1. Clone the Repository:

    Clone the repository to the local machine using the command:

    ```bash
    git clone https://github.com/seu-usuario/chess-rankings.git
    ```

2. Create and Activate the Virtual Environment:

    In the project root directory, create a virtual environment to manage dependencies:

    ```bash
    # Linux/MacOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    venv\Scripts\activate
    ```

    Make sure the virtual environment is activated (you should see (venv) at the top of the terminal prompt).

3. Install Dependencies:

    Install all required libraries and dependencies listed in requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```
4. Execute the Project:

    ```bash
    uvicorn src.chess.main:app --reload
    ```
    This will start the FastAPI server at http://127.0.0.1:8000.

