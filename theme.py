
# custom_css = """
# <style>
#     /* Animated background */
#     @keyframes gradientAnimation {
#         0% { background-position: 0% 50%; }
#         50% { background-position: 100% 50%; }
#         100% { background-position: 0% 50%; }
#     }

#     body {
#         background: linear-gradient(-45deg, #1a1a2e, #3a0ca3, #7209b7, #ff477e);
#         background-size: 300% 300%;
#         animation: gradientAnimation 15s ease infinite;
#         color: #e0e0e0;
#         font-family: 'Arial', sans-serif;
#     }
    
#     /* Main container */
#     .stApp {
#         padding: 20px;
#         border-radius: 12px;
#         backdrop-filter: blur(10px);
#     }

#     /* Title */
#     .stTitle {
#         color: #e0e0e0;
#         font-size: 32px;
#         font-weight: bold;
#         text-align: center;
#         text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.2);
#     }

#     /* Input fields inside a 3D shadow box */
#     .stSelectbox, .stTextInput, .stNumberInput {
        
#         background-color: rgba(34, 34, 59, 0.9);
#         color: #ffffff;
#         border-radius: 12px;
#         padding: 12px;
#         box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);
#         border: 1px solid rgba(255, 255, 255, 0.2);
#         transition: all 0.3s ease-in-out;
#     }

#     .stSelectbox:hover, .stTextInput:hover, .stNumberInput:hover {
#         box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.5);
#     }

#   /* Increase font size of selectbox labels */
#     .stSelectbox label {
#         font-size: 30px;
#     }


  
#     /* Output Messages */
#     .stSuccess {
#         background-color: #0f5132;
#         color: #d1e7dd;
#         border-radius: 10px;
#         padding: 12px;
#         margin-top: 10px;
#         box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
#     }

#     .stError {
#         background-color: #842029;
#         color: #f8d7da;
#         border-radius: 10px;
#         padding: 12px;
#         margin-top: 10px;
#         box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
#     }
# </style>
# """

#PREVIOUS CSS

custom_css = """
<style>
    /* Apply background animation to the whole page */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #1a1a2e, #3a0ca3, #7209b7, #ff477e);
        background-size: 300% 300%;
        animation: gradientAnimation 15s ease infinite;
        color: #e0e0e0;
        font-family: 'Poppins', sans-serif;
    }

    /* Define gradient animation */
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

     /* Floating robot animation */
    @keyframes floatRobot {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }

    /* Floating robot image */
    .floating-robot {
        position: fixed;
        bottom: 50px;
        right: 50px;
        width: 120px;
        height: auto;
        animation: floatRobot 3s ease-in-out infinite;
        opacity: 0.8;
        z-index: 999;
    }

    /* Styling for main container */
    div[data-testid="stAppViewContainer"] > div {
        padding: 20px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
    }

    /* Center the main container and apply a glassmorphism effect */
    div[data-testid="stAppViewContainer"] > div {
        padding: 20px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
    }

    /* Title Styling */
    h1 {
        font-size: 7rem !important;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        text-shadow: 2px 2px 8px rgba(255, 255, 255, 0.3);
    }
 /* Input fields inside a 3D shadow box */
        div[data-baseweb="select"], div[data-baseweb="input"] {
            background-color: rgba(34, 34, 59, 0.9) !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            padding: 10px !important;
            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            transition: all 0.3s ease-in-out !important;
            font-size: 18px !important;
        }
/* Targeting the label inside the select box container */
    div[data-testid="stSelectbox"] label {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #ffffff !important;
    }
    

  /* Buttons */
    .stButton > button {
        background-color: #e27602;
        color: black;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
        font-size: 20px;
    }

    .stButton > button:hover {
        background-color: #eee9f27;
        transform: scale(1.05);
        box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.5);
        color: black !important;
    }

/* Prevent Text Color Change on Click */
    .stButton > button:active,
    .stButton > button:focus {
        color: black !important;
        background-color: #d96e00 !important; /* Slightly darker orange for click effect */
        outline: none !important;
        box-shadow: inset 2px 2px 6px rgba(0, 0, 0, 0.4);
    }


    /* Success & Error Messages */
    .stSuccess, .stError {
        border-radius: 10px;
        padding: 12px;
        margin-top: 10px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
        font-size: 18px;
        font-weight: bold;
    }

    .stSuccess {
        background-color: #0f5132;
        color: #d1e7dd;
    }

    .stError {
        background-color: #842029;
        color: #f8d7da;
    }
</style>



<img src= "https://cdn-icons-png.flaticon.com/512/4712/4712139.png" class="floating-robot" />
"""
