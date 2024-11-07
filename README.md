# 🏏 Cricket Player Information App

Welcome to the **Cricket Player Information App**! This app allows users to search for detailed cricket player statistics and personal information by entering a player's name. It fetches data from the **GROQ API**, which provides in-depth cricket player statistics such as career stats, debut information, notable achievements, and more. The app also displays the player's image and description. 🎉

## Features ✨

- **🔍 Search for cricket players**: Enter a player's name and click "Search" to fetch detailed player data.
- **👤 Player information**: Displays full name, date of birth, country, playing role, batting and bowling styles, and more.
- **📊 Career statistics**: Shows the player's career stats for Test, ODI, and T20I formats, including matches, runs, batting average, wickets, and bowling average.
- **🏅 Debut information**: Get details of the player's debut matches for Test, ODI, and T20I formats, including the date and opponent.
- **🏆 Achievements**: View the player's notable achievements in cricket.
- **📝 Player description**: A brief description of the player's playing style, impact, and records held.
- **🎨 Customizable UI**: The app features a responsive, user-friendly interface with a sidebar for API key configuration.

## Tech Stack 🛠️

- **Streamlit**: A Python framework for building web apps. 🌐
- **GROQ API**: Provides cricket player data via an API. 📡
- **Pillow**: For displaying player images. 🖼️
- **Requests**: To make HTTP requests to the GROQ API. 🌍
- **JSON**: For parsing and handling player data. 🧩

## Installation ⚙️

To run this app locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cricket-player-info.git
cd cricket-player-info
```

### 2. Install Dependencies
Make sure you have Python 3.7+ installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Get the API Key 🔑
- Register on the [GROQ API](https://groq.com) platform to obtain your API key.
- Store the API key in the app via the sidebar's input field when prompted.

### 4. Run the Streamlit App 🚀
Once the dependencies are installed and your API key is set, run the app using the following command:
```bash
streamlit run app.py
```

The app should now be running locally on [http://localhost:8501](http://localhost:8501).

## Usage 📱

- Enter a **cricket player's name** in the input field. 📝
- Click the **Search** button to fetch player data. 🔍
- The app will display the player's **profile**, **career statistics**, **debut information**, and **achievements**. 🏅
- You can explore different sections of the player's information using **expandable panels**. 📊

## Project Structure 🗂️

```plaintext
cricket-player-info/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── assets/
    └── (optional)          # Folder for storing assets (e.g., images, icons)
```

## Screenshots 📸

![Player Info](screenshots/player_info.png)
*Example of player information with stats, debut, and achievements.*

## Contributing 🤝

We welcome contributions! If you'd like to contribute to the project, please fork the repository, make your changes, and create a pull request. 🚀 

Please ensure that any code changes adhere to the style and structure used in the project. 🖋️

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙏

- The app uses the **GROQ API** to fetch cricket player data. 📡
- Thanks to **Streamlit** for providing an easy-to-use framework for building this app. 🌟

---

**Note**: Ensure that you have a valid GROQ API key before using the app. You can obtain the key by signing up for the GROQ API service. 🔑

---

Feel free to reach out via issues or PRs if you encounter any bugs or have any suggestions for improving the app! 🐞💡

---

Now, this `README.md` is not only informative but also engaging and visually appealing with the help of emojis! 😊
