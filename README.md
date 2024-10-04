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