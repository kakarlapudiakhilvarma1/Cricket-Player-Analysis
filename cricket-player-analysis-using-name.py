import streamlit as st
import requests
import json
from PIL import Image
from io import BytesIO

# ... (keep the fetch_player_data function as is)
def fetch_player_data(api_key, player_name):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""
    Provide detailed information about the cricket player {player_name}. Include the following:
    - Full Name
    - Date of Birth
    - Country Represented
    - Playing Role (e.g., Batsman, Bowler, All-rounder, Wicket-keeper)
    - Batting Style (right-handed or left-handed)
    - Bowling Style (if applicable)
    - Career Data:
        - Matches played (Test, ODI, T20I)
        - Runs scored
        - Batting average
        - Wickets taken (if applicable)
        - Bowling average (if applicable)
        - Notable achievements
    - Debut Information:
        - Test debut (date and opponent)
        - ODI debut (date and opponent)
        - T20I debut (date and opponent)
    - A brief description of their playing style, impact on the game, and any records held

    Format the response as a JSON object with the following structure:
    {{
        "name": "",
        "dob": "",
        "country": "",
        "playing_role": "",
        "batting_style": "",
        "bowling_style": "",
        "career_data": {{
            "matches": {{"test": 0, "odi": 0, "t20i": 0}},
            "runs": {{"test": 0, "odi": 0, "t20i": 0}},
            "batting_average": {{"test": 0.0, "odi": 0.0, "t20i": 0.0}},
            "wickets": {{"test": 0, "odi": 0, "t20i": 0}},
            "bowling_average": {{"test": 0.0, "odi": 0.0, "t20i": 0.0}},
            "achievements": []
        }},
        "debut": {{
            "test": {{"date": "", "opponent": ""}},
            "odi": {{"date": "", "opponent": ""}},
            "t20i": {{"date": "", "opponent": ""}}
        }},
        "description": ""
    }}
    """

    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 1500
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        content = response.json()['choices'][0]['message']['content']
        return json.loads(content)
    except requests.RequestException as e:
        st.error(f"Error fetching data: {str(e)}")
        return None
    except json.JSONDecodeError:
        st.error("Error parsing the response from GROQ API")
        return None
    except KeyError:
        st.error("Unexpected response format from GROQ API")
        return None

def fetch_player_image(player_name):
    # This is a placeholder. In a real app, you'd implement an image search or use a sports API
    return f"https://via.placeholder.com/150x150.png?text={player_name}"

st.set_page_config(page_title="Cricket Player Info", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.8rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
    }
    .stTextInput > div > div > input {
        font-size: 1.2rem;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    .stButton > button {
        width: 100%;
        font-size: 1.2rem;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        background-color: #FF4B4B;
        color: white;
    }
    .stExpander {
        border: 1px solid #ddd;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #43A047;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Cricket Player Information</h1>", unsafe_allow_html=True)

# Main input area
col1, col2, col3 = st.columns([1,2,1])
with col2:
    player_name = st.text_input("Enter player name", key="player_name")
    search_button = st.button("Search", key="search_button", type="primary")

# Sidebar for API key
st.sidebar.header("API Configuration")
groq_api_key = st.sidebar.text_input("Enter your GROQ API key", type="password")

# Main UI
if search_button and player_name and groq_api_key:
    with st.spinner("Fetching player data..."):
        player_data = fetch_player_data(groq_api_key, player_name)

    if player_data:
        st.markdown(f"<h2 class='section-header'>{player_data['name']}</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])

        with col1:
            player_image_url = fetch_player_image(player_data['name'])
            st.image(player_image_url, caption=player_data["name"], width=150)

        with col2:
            with st.expander("Personal Information", expanded=True):
                st.write(f"**Date of Birth:** {player_data['dob']}")
                st.write(f"**Country:** {player_data['country']}")
                st.write(f"**Playing Role:** {player_data['playing_role']}")
                st.write(f"**Batting Style:** {player_data['batting_style']}")
                if player_data['bowling_style']:
                    st.write(f"**Bowling Style:** {player_data['bowling_style']}")

        # ... (keep the rest of the expanders as they are)

        with st.expander("Career Statistics", expanded=True):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write("**Test Matches**")
                st.write(f"Matches: {player_data['career_data']['matches']['test']}")
                st.write(f"Runs: {player_data['career_data']['runs']['test']}")
                st.write(f"Average: {player_data['career_data']['batting_average']['test']:.2f}")
                if player_data['career_data']['wickets']['test'] > 0:
                    st.write(f"Wickets: {player_data['career_data']['wickets']['test']}")
                    st.write(f"Bowling Avg: {player_data['career_data']['bowling_average']['test']:.2f}")

            with col2:
                st.write("**ODI Matches**")
                st.write(f"Matches: {player_data['career_data']['matches']['odi']}")
                st.write(f"Runs: {player_data['career_data']['runs']['odi']}")
                st.write(f"Average: {player_data['career_data']['batting_average']['odi']:.2f}")
                if player_data['career_data']['wickets']['odi'] > 0:
                    st.write(f"Wickets: {player_data['career_data']['wickets']['odi']}")
                    st.write(f"Bowling Avg: {player_data['career_data']['bowling_average']['odi']:.2f}")

            with col3:
                st.write("**T20I Matches**")
                st.write(f"Matches: {player_data['career_data']['matches']['t20i']}")
                st.write(f"Runs: {player_data['career_data']['runs']['t20i']}")
                st.write(f"Average: {player_data['career_data']['batting_average']['t20i']:.2f}")
                if player_data['career_data']['wickets']['t20i'] > 0:
                    st.write(f"Wickets: {player_data['career_data']['wickets']['t20i']}")
                    st.write(f"Bowling Avg: {player_data['career_data']['bowling_average']['t20i']:.2f}")

        with st.expander("Debut Information", expanded=True):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write("**Test Debut**")
                st.write(f"Date: {player_data['debut']['test']['date']}")
                st.write(f"Opponent: {player_data['debut']['test']['opponent']}")

            with col2:
                st.write("**ODI Debut**")
                st.write(f"Date: {player_data['debut']['odi']['date']}")
                st.write(f"Opponent: {player_data['debut']['odi']['opponent']}")

            with col3:
                st.write("**T20I Debut**")
                st.write(f"Date: {player_data['debut']['t20i']['date']}")
                st.write(f"Opponent: {player_data['debut']['t20i']['opponent']}")

        with st.expander("Notable Achievements", expanded=True):
            for achievement in player_data['career_data']['achievements']:
                st.write(f"• {achievement}")

        with st.expander("Player Description", expanded=True):
            st.write(player_data['description'])

else:
    st.info("Enter a player name and click 'Search' to fetch player information.")

st.sidebar.markdown("---")
st.sidebar.info("This app uses the GROQ API to fetch cricket player information. Please ensure you have a valid API key.")