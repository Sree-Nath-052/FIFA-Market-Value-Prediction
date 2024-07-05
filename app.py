import streamlit as st
import pickle
import pandas as pd
from scipy.stats.mstats import winsorize

# Load the model from the pickle file
with open('market_value.pkl', 'rb') as file:
    model = pickle.load(file)

# Define a function for winsorization
def winsorize_series(series):
    return winsorize(series, limits=[0.01, 0.01])

# Define a function to handle user input and predictions
def user_input_features():
    title_html = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap');

    .title-container {
        text-align: center;
        margin: 20px 0;
    }

    .market-title {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 3.8em;
        color: #ff5733;
        text-align: center;
        display: inline-block;
        transition: font-size 0.3s ease-in-out;
    }

    .market-title:hover {
        font-size: 4em; /* Increase font size on hover */
    }

    .sub-title {
        font-family: 'Roboto Mono', monospace;
        font-size: 1.1em;
        color: #7f8c8d; /* Dimmed color */
        text-align: center;
        margin-top: -20px;
    }
    
    </style>
    <div class="title-container">
        <div class="market-title">FIFA Market Value Predictor</div>
        <div class="sub-title">Created by Sreenath</div>
    </div>
    """
    st.markdown(title_html, unsafe_allow_html=True)

    # Basic Information
    st.header("Basic Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.number_input('Age', min_value=0, max_value=100, value=25)
        Nationality = st.text_input('Nationality', 'England')
        Height_cm = st.number_input('Height (in cm)', min_value=0, max_value=300, value=180)
        Weight_kg = st.number_input('Weight (in kg)', min_value=0, max_value=200, value=75)
        Preferred_Foot = st.selectbox('Preferred Foot', ['Right', 'Left'])
    with col2:
        Overall = st.number_input('Overall', min_value=0, max_value=100, value=50)
        Potential = st.number_input('Potential', min_value=0, max_value=100, value=50)
        Club_Name = st.text_input('Club Name', 'Manchester United')
        Best_Position = st.selectbox('Best Position', ['ST', 'LW', 'LF', 'CF', 'RF', 'RW', 'CAM', 'LM', 'CM', 'RM', 'LWB', 'CDM', 'RWB', 'LB', 'CB', 'RB', 'GK'])
    with col3:
        Club_Position = st.selectbox('Club Position', ['ST', 'LW', 'LF', 'CF', 'RF', 'RW', 'CAM', 'LM', 'CM', 'RM', 'LWB', 'CDM', 'RWB', 'LB', 'CB', 'RB', 'GK'])
        Wage_Euro = st.number_input('Wage (in Euro)', min_value=0, max_value=1000000, value=50000)
        Release_Clause = st.number_input('Release Clause', min_value=0, max_value=1000000000, value=10000000)
        Attacking_Work_Rate = st.selectbox('Attacking Work Rate', ['Low', 'Medium', 'High'])
        Defensive_Work_Rate = st.selectbox('Defensive Work Rate', ['Low', 'Medium', 'High'])

    # Contract Information
    st.header("Contract Information")
    Joined_On = st.number_input('Joined On', min_value=2000, max_value=2050, value=2020)
    Contract_Until = st.number_input('Contract Until', min_value=2000, max_value=2050, value=2023)

    # Ratings
    st.header("Ratings")
    col1, col2, col3 = st.columns(3)
    with col1:
        Weak_Foot_Rating = st.slider('Weak Foot Rating', min_value=0, max_value=5, value=3)
        Skill_Moves = st.slider('Skill Moves', min_value=0, max_value=5, value=3)
        International_Reputation = st.slider('International Reputation', min_value=0, max_value=5, value=3)
    with col2:
        ST_Rating = st.slider('ST Rating', min_value=0, max_value=100, value=50)
        LW_Rating = st.slider('LW Rating', min_value=0, max_value=100, value=50)
        RW_Rating = st.slider('RW Rating', min_value=0, max_value=100, value=50)
    with col3:
        LF_Rating = st.slider('LF Rating', min_value=0, max_value=100, value=50)
        RF_Rating = st.slider('RF Rating', min_value=0, max_value=100, value=50)
        CF_Rating = st.slider('CF Rating', min_value=0, max_value=100, value=50)

    col1, col2, col3 = st.columns(3)
    with col1:
        CAM_Rating = st.slider('CAM Rating', min_value=0, max_value=100, value=50)
        LM_Rating = st.slider('LM Rating', min_value=0, max_value=100, value=50)
        CM_Rating = st.slider('CM Rating', min_value=0, max_value=100, value=50)
        RM_Rating = st.slider('RM Rating', min_value=0, max_value=100, value=50)
    with col2:
        LWB_Rating = st.slider('LWB Rating', min_value=0, max_value=100, value=50)
        CDM_Rating = st.slider('CDM Rating', min_value=0, max_value=100, value=50)
        RWB_Rating = st.slider('RWB Rating', min_value=0, max_value=100, value=50)
    with col3:
        CB_Rating = st.slider('CB Rating', min_value=0, max_value=100, value=50)
        LB_Rating = st.slider('LB Rating', min_value=0, max_value=100, value=50)
        RB_Rating = st.slider('RB Rating', min_value=0, max_value=100, value=50)
        GK_Rating = st.slider('GK Rating', min_value=0, max_value=100, value=50)

    # Skills
    st.header("Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        TotalStats = st.slider('Total Stats', min_value=1000, max_value=5000, value=2000)
        BaseStats = st.slider('Base Stats', min_value=0, max_value=1000, value=300)
        Pace_Total = st.slider('Pace Total', min_value=0, max_value=100, value=70)
        Shooting_Total = st.slider('Shooting Total', min_value=0, max_value=100, value=70)
        Passing_Total = st.slider('Passing Total', min_value=0, max_value=100, value=70)
    with col2:
        Dribbling_Total = st.slider('Dribbling Total', min_value=0, max_value=100, value=70)
        Defending_Total = st.slider('Defending Total', min_value=0, max_value=100, value=70)
        Physicality_Total = st.slider('Physicality Total', min_value=0, max_value=100, value=70)
        Crossing = st.slider('Crossing', min_value=0, max_value=100, value=50)
        Finishing = st.slider('Finishing', min_value=0, max_value=100, value=50)
    with col3:
        Heading_Accuracy = st.slider('Heading Accuracy', min_value=0, max_value=100, value=50)
        Short_Passing = st.slider('Short Passing', min_value=0, max_value=100, value=50)
        Volleys = st.slider('Volleys', min_value=0, max_value=100, value=50)
        Dribbling = st.slider('Dribbling', min_value=0, max_value=100, value=50)
        Curve = st.slider('Curve', min_value=0, max_value=100, value=50)

    col1, col2, col3 = st.columns(3)
    with col1:
        Freekick_Accuracy = st.slider('Freekick Accuracy', min_value=0, max_value=100, value=50)
        Long_Passing = st.slider('Long Passing', min_value=0, max_value=100, value=50)
        Ball_Control = st.slider('Ball Control', min_value=0, max_value=100, value=50)
        Acceleration = st.slider('Acceleration', min_value=0, max_value=100, value=70)
        Sprint_Speed = st.slider('Sprint Speed', min_value=0, max_value=100, value=70)
    with col2:
        Agility = st.slider('Agility', min_value=0, max_value=100, value=70)
        Reactions = st.slider('Reactions', min_value=0, max_value=100, value=70)
        Balance = st.slider('Balance', min_value=0, max_value=100, value=70)
        Shot_Power = st.slider('Shot Power', min_value=0, max_value=100, value=70)
        Jumping = st.slider('Jumping', min_value=0, max_value=100, value=70)
    with col3:
        Stamina = st.slider('Stamina', min_value=0, max_value=100, value=70)
        Strength = st.slider('Strength', min_value=0, max_value=100, value=70)
        Long_Shots = st.slider('Long Shots', min_value=0, max_value=100, value=70)
        Aggression = st.slider('Aggression', min_value=0, max_value=100, value=70)
        Goalkeeper_Diving = st.slider('Goalkeeper Diving', min_value=0, max_value=100, value=20)

    col1, col2, col3 = st.columns(3)
    with col1:
        Positioning = st.slider('Positioning', min_value=0, max_value=100, value=70)
        Vision = st.slider('Vision', min_value=0, max_value=100, value=70)
        Penalties = st.slider('Penalties', min_value=0, max_value=100, value=70)
        Composure = st.slider('Composure', min_value=0, max_value=100, value=70)
    with col2:
        Marking = st.slider('Marking', min_value=0, max_value=100, value=70)
        Standing_Tackle = st.slider('Standing Tackle', min_value=0, max_value=100, value=70)
        Sliding_Tackle = st.slider('Sliding Tackle', min_value=0, max_value=100, value=70)
        Interceptions = st.slider('Interceptions', min_value=0, max_value=100, value=70)
    with col3:
        Goalkeeper_Handling = st.slider('Goalkeeper Handling', min_value=0, max_value=100, value=20)
        Goalkeeper_Kicking = st.slider('Goalkeeper Kicking', min_value=0, max_value=100, value=20)
        Goalkeeper_Positioning = st.slider('Goalkeeper Positioning', min_value=0, max_value=100, value=20)
        Goalkeeper_Reflexes = st.slider('Goalkeeper Reflexes', min_value=0, max_value=100, value=20)

    data = {
        'Overall': Overall, 'Potential': Potential, 'Best Position': Best_Position,
        'Nationality': Nationality, 'Age': Age, 'Height(in cm)': Height_cm,
        'Weight(in kg)': Weight_kg, 'TotalStats': TotalStats, 'BaseStats': BaseStats,
        'Club Name': Club_Name, 'Wage(in Euro)': Wage_Euro, 'Release Clause': Release_Clause,
        'Club Position': Club_Position, 'Contract Until': Contract_Until, 'Joined On': Joined_On,
        'Preferred Foot': Preferred_Foot, 'Weak Foot Rating': Weak_Foot_Rating,
        'Skill Moves': Skill_Moves, 'International Reputation': International_Reputation,
        'Attacking Work Rate': Attacking_Work_Rate, 'Defensive Work Rate': Defensive_Work_Rate,
        'Pace Total': Pace_Total, 'Shooting Total': Shooting_Total, 'Passing Total': Passing_Total,
        'Dribbling Total': Dribbling_Total, 'Defending Total': Defending_Total,
        'Physicality Total': Physicality_Total, 'ST Rating': ST_Rating, 'LW Rating': LW_Rating,
        'LF Rating': LF_Rating, 'CF Rating': CF_Rating, 'RF Rating': RF_Rating, 'RW Rating': RW_Rating,
        'CAM Rating': CAM_Rating, 'LM Rating': LM_Rating, 'CM Rating': CM_Rating, 'RM Rating': RM_Rating,
        'LWB Rating': LWB_Rating, 'CDM Rating': CDM_Rating, 'RWB Rating': RWB_Rating, 'LB Rating': LB_Rating,
        'CB Rating': CB_Rating, 'RB Rating': RB_Rating, 'GK Rating': GK_Rating,
        'Crossing': Crossing, 'Finishing': Finishing, 'Heading Accuracy': Heading_Accuracy,
        'Short Passing': Short_Passing, 'Volleys': Volleys, 'Dribbling': Dribbling, 'Curve': Curve,
        'Freekick Accuracy': Freekick_Accuracy, 'Long Passing': Long_Passing, 'Ball Control': Ball_Control,
        'Acceleration': Acceleration, 'Sprint Speed': Sprint_Speed, 'Agility': Agility, 'Reactions': Reactions,
        'Balance': Balance, 'Shot Power': Shot_Power, 'Jumping': Jumping, 'Stamina': Stamina,
        'Strength': Strength, 'Long Shots': Long_Shots, 'Aggression': Aggression, 'Interceptions': Interceptions,
        'Positioning': Positioning, 'Vision': Vision, 'Penalties': Penalties, 'Composure': Composure,
        'Marking': Marking, 'Standing Tackle': Standing_Tackle, 'Sliding Tackle': Sliding_Tackle,
        'Goalkeeper Diving': Goalkeeper_Diving, 'Goalkeeper Handling': Goalkeeper_Handling,
        'Goalkeeper Kicking': Goalkeeper_Kicking, 'Goalkeeper Positioning': Goalkeeper_Positioning,
        'Goalkeeper Reflexes': Goalkeeper_Reflexes
    }

    features = pd.DataFrame(data, index=[0])
    return features

# User input
input_df = user_input_features()

# Handle the same preprocessing steps applied to the training data

# Get dummies for categorical variables
categorical_columns = ['Best Position', 'Nationality', 'Club Name', 'Club Position', 'Preferred Foot', 'Attacking Work Rate', 'Defensive Work Rate']
input_df = pd.get_dummies(input_df, columns=categorical_columns)

# Add missing columns with default value 0
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0

# Ensure columns are in the same order as training data
input_df = input_df[model.feature_names_in_]

# Winsorize the data
input_df = input_df.apply(winsorize_series, axis=0)

# Prediction
prediction = model.predict(input_df)
st.subheader('Prediction')
st.write(f"The expected market value of the player is:")

import time
with st.spinner('Calculating...'):
    time.sleep(2)
st.success(f"**€{prediction[0]:,.2f}**")