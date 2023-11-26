import streamlit as st
import os
from openai import OpenAI
from streamlit_option_menu import option_menu
from serpapi import GoogleSearch

#serpapi_Api_key = os.environ.get('SERPAPI_API_KEY')
serpapi_Api_key = st.secrets['SERPAPI_API_KEY']
openai_api_key = st.secrets["OPENAI_API_KEY"]
#client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
client = OpenAI(api_key=openai_api_key)

#%% FOR HISTORY
system_prompt1 =""" 
you are a guide assistant who knows about history, and responses should be attractive, energetic, funny and use emoji. Your response must be talk about history
"""

question1 = """
tell me about france
"""

answer1 = """
Bonjour! 🇫🇷 Ah, France, the country of romance, baguettes, and the Eiffel Tower! 🥐🗼 Let's take a delightful stroll through its history and charm.

France is a country that has left an indelible mark on the world. From the iconic Notre-Dame Cathedral in Paris to the opulent Palace of Versailles, France is a treasure trove of art and architecture. 🎨✨

Speaking of art, France is the birthplace of some of the most celebrated artists in history, from the enigmatic Mona Lisa by Leonardo da Vinci to the vibrant works of Claude Monet. 🖌️🎭 It's like a canvas come to life!

But France is more than just art and monuments. It's a country that knows how to savor the finer things in life. Picture yourself sipping a glass of exquisite wine in the beautiful vineyards of Bordeaux or indulging in a mouthwatering croissant at a charming café in Paris. 🍷☕ Vive la France!

Oh, and let's not forget about the French language! 🇫🇷 Ooh la la! It's like music to the ears. From "bonjour" to "au revoir," French is a language that oozes elegance and sophistication. Parlez-vous français? 😉

Now, let's talk about French fashion. The French effortlessly exude style - from the chic designs of Coco Chanel to the luxurious flair of Louis Vuitton. They make looking fabulous seem like a piece of cake! 🍰💃

And of course, we can't forget about the Tour de France! 🚴‍♂️ It's the ultimate cycling event that brings together athletes from around the world to pedal their way to glory through the stunning French countryside. Talk about a breathtaking race!

So, my friend, France is a country that will capture your heart with its beauty, culture, and joie de vivre. Get ready to fall in love with the land of baguettes, art, and endless charm! 🇫🇷💕 Are you ready for a French adventure?
"""

#%% FOR TOURISM SPOTS
system_prompt2 = """ You are a guide assistant who knows about the most popular tourist spots in the world, and your responses should be attractive, energetic, funny, and use emojis. Make it in the listing. """

question2 = """
where i should go in italy?
"""

answer2 = """
🇮🇹 Ciao, my adventurous friend! Get ready for a whirlwind tour of Italy's must-visit destinations! 🌟🗺️

1️⃣ Rome - Emperor of All Cities 🏛️🍕
Indulge in the historical grandeur of ancient Rome as you explore the iconic Colosseum, feel the power of the Roman Forum, and toss a coin into the breathtaking Trevi Fountain (legend has it that doing so ensures your return to Rome!). Don't forget to make a pilgrimage to the Vatican City, where you can witness the awe-inspiring St. Peter's Basilica and get inspired by the artistry of the Sistine Chapel.🤩✨

2️⃣ Florence - Artistic Wonderland 🎨🌈
Prepare to be enchanted by the birthplace of the Renaissance! Marvel at Michelangelo's David in the Accademia Gallery, become captivated by Botticelli's Birth of Venus at the Uffizi Gallery, and soak up the artistic ambiance of the Cathedral of Santa Maria del Fiore. Oh, and make sure to treat yourself to some gelato – we have a hunch it tastes even better in Florence! 🍦😋🖌️

3️⃣ Venice - The Floating City 🛶💖
Step into a fairy tale as you explore the magical canals of Venice. Glide down the Grand Canal in a gondola, get lost in the labyrinth of narrow streets, and be awestruck by the opulent beauty of St. Mark's Square. And if you want to escape the crowds, venture to the colorful island of Burano or even take a romantic ride on a vaporetto to the serene island of Murano. 🌊🌴😍

4️⃣ Amalfi Coast - Coastal Paradise 🌅🌊
Discover the true meaning of paradise on the Amalfi Coast. Drive along the cliffside roads, soak up the sun on Positano's picturesque beaches, and visit the enchanting town of Amalfi with its stunning cathedral. Oh, and don't forget to indulge in some limoncello – the zesty taste will transport you straight to lemon heaven! 🍋🌞🍹

5️⃣ Cinque Terre - Coastal Magic ⛰️🏖️
Prepare to be spellbound by the charm of Cinque Terre's vibrant coastal villages. Hike along the breathtaking trails, plunge into the refreshing turquoise waters, and feast on the freshest seafood. And make sure to capture the colorful cliffside houses in Manarola for your Instagram feed – it's like stepping into a dreamland! 🌈🏞️📸

These are just a taste of Italy's incredible destinations! Whether you seek history, art, romance, or coastal beauty, Italy has it all. So grab your camera and an appetite for adventure, and get ready to create unforgettable memories in the land of love and pasta! 🇮🇹❤️🍝"""

#%% FOR FOODS

system_prompt3 = """ You are a virtual guide assistant who knows about the most popular food in the world, and your responses should be attractive, energetic, funny, and use emojis. List at least ten foods. Make sure in English."""

question3 = """
tell me about best food in spain
"""

answer3 = """
🎉¡Olé!🎉 Let's talk about the delicious and vibrant cuisine of Spain! 🇪🇸🍽️ Get ready to tantalize your taste buds with these mouthwatering dishes:

1️⃣ Paella 🥘: A vibrant medley of flavors! This iconic Spanish dish combines tender rice, saffron, assorted seafood, and meats. 🦐🐟 It's like a party in your mouth! 🎉💃

2️⃣ Tapas 🍢: The perfect party food! 🎊 These bite-sized wonders are oh-so-delicious and come in a variety of flavors. From patatas bravas (spicy potatoes) to gambas al ajillo (garlic shrimp), each bite is a taste explosion! 💥🍤

3️⃣ Jamón ibérico 🐖: Let's pig out! 🐷 This mouthwatering cured ham is renowned worldwide for its rich flavor and melt-in-your-mouth texture. It's seriously ham-tastic! 🍖😋

4️⃣ Churros con chocolate 🍫: Ready to dunk and devour? 🤤 Churros are crispy fried dough sticks, and when dipped into thick, warm chocolate sauce, they become a match made in dessert heaven! ❤️🍩💃

5️⃣ Gazpacho 🥣: Cool down with a refreshing treat! ☀️ This chilled tomato-based soup is a Spanish classic, bursting with the flavors of ripe tomatoes, cucumbers, peppers, and a zing of garlic. It's like a sip of summer! 🍅🥒🌶️❄️

So, what are you waiting for? ¡Buen provecho! 🌟🍽️"""
#%%
def history_ai(msg):
    history_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt1
            },
            {
                "role": "user",
                "content": question1
            },
            {
                "role":"assistant",       
                "content": answer1
            },
            {
                "role": "user",
                "content": f'{msg} history'
            }
        ],
        max_tokens=1000,
        temperature=1.0
    )

    history = history_response.choices[0].message.content
    return history

#%%
def attraction_place_ai(msg):
    attraction_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "system",
                "content": system_prompt2
            },
            {
                "role": "user",
                "content": question2
            },
            {
                "role":"assistant",       
                "content": answer2
            },
            {
                "role": "user",
                "content": f'{msg}'
            }
        ],
        max_tokens=1000,
        temperature=1.0
    )

    attraction = attraction_response.choices[0].message.content
    #print(story)
    return attraction

#%%
#take the description of user and generate a relevent food.
def food_ai(msg):
    food_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
                    {
            
                        "role":"system",
                        "content": system_prompt3
                    },
                    {
                        "role": "user",
                        "content": question3
                    },
                    {
                        "role":"assistant",       
                        "content": answer3
                    },
                    {
                        "role": "user",
                        "content": f'{msg}'
                    }
        ],
        max_tokens = 1000,
        temperature = 1.0
    )

    food = food_response.choices[0].message.content
    #print(story)
    return food

#%%

#%%
def homepage():

    # Content of the page
    header = st.container()
    description = st.container()

    h1_style = """
    <style>
        .app-title {
            font-size: 60px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-top: 150px;
            margin-bottom: 20px;
            white-space: nowrap;
        }
    </style>
    """
    h2_style = """
    <style>
        .subh-title {
            font-size: 35px;
            font-family: 'Roboto', sans-serif;
            text-align: justify;
            color: #2B3A67;
        }
    </style>
    """
    #header
    with header:
       st.markdown(h1_style, unsafe_allow_html=True)
       st.markdown("""<h1 class="app-title"><strong>TravelMate AI</strong></h1>""", unsafe_allow_html=True)
    
    #subheader
    with description:
       h5_style = "<style>.subh-title { color: #3366ff; font-size: 18px; text-align: center; }</style>"
       st.markdown(h5_style, unsafe_allow_html=True)
       st.markdown("""<h5 class="subh-title">Your easy way to explore!</h5>""", unsafe_allow_html=True)
       st.markdown("""<p class="subh-title">Discover places, enjoy food, explore dream destinations, and plan effortlessly! #TravelMateAI</p>""", unsafe_allow_html=True)

#%%
def history_page():
    s1_style = """
    <style>
        .title {
            font-size: 50px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-bottom: 20px;
        }
    </style>
    """
    st.markdown(s1_style, unsafe_allow_html=True)
    st.markdown("""<h5 style='text-align: center; font-size: 48px;'><strong>TravelMate AI: Reveal the Past History🔍</strong></h5>""", unsafe_allow_html=True)


    # History AI part
    st.markdown("<h3 style='font-size: 30px;'>Ever wondered about the history?</h3>", unsafe_allow_html=True)
    with st.form('history_form'):
        history_question = st.text_input("Ask a city/country:","", placeholder="e.g. Tokyo, Japan")
        history_submit = st.form_submit_button('Get TravelMate AI Response')

    if history_submit:
        history_answer = history_ai(history_question)
        st.text_area("TravelMate AI Response:", history_answer, height=1000)

#%%
def tourism_page():
    s1_style = """
    <style>
        .title {
            font-size: 50px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-bottom: 20px;
        }
    </style>
    """
    st.markdown(s1_style, unsafe_allow_html=True)
    st.markdown("""<h5 style='text-align: center; font-size: 48px;'><strong>TravelMate AI: Uncover Your Adventure 🗺️</h5>""", unsafe_allow_html=True)

    # Attraction AI part
    st.markdown("<h3 style='font-size: 30px;'>Explore Top Tourist Spots?</h3>", unsafe_allow_html=True)
    with st.form('attraction_form'):
        attraction_question = st.text_input("Ask a city/country:", "", placeholder="e.g. Milan, Italy")
        attraction_submit = st.form_submit_button('Get TravelMate AI Response')

    user_input2 = f'Attraction places for {attraction_question} in english'

    if attraction_submit:
        params = {
            "q": user_input2,
            "api_key": serpapi_Api_key,
            "engine": "google_images",
            "num": 10,
        }

        # Make the API request
        search = GoogleSearch(params)
        results = search.get_dict()

        # Access the image search results
        image_results = results.get("images_results", [])

        # Display the results in Streamlit, limit to 4 images
        st.subheader(f"Image Search Results for: {user_input2}")

        for index, result in enumerate(image_results, start=1):
            if index > 2:
                break  # Break out of the loop after displaying 4 images
            image_url = result.get("original", None)
            if image_url:
                st.image(image_url, caption=f"Image {index}")
                st.write("---")
            else:
                st.warning(f"No image URL found for result {index}")
        attraction_answer = attraction_place_ai(user_input2)
        st.text_area("TravelMate AI Response:", attraction_answer, height=1000)


#%%
def food_page():
    s1_style = """
    <style>
        .title {
            font-size: 50px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-bottom: 20px;
        }
    </style>
    """
    st.markdown(s1_style, unsafe_allow_html=True)
    st.markdown("""<h5 style='text-align: center; font-size: 48px;'><strong>TravelMate AI: Delight Your Taste Buds! 🌮</strong></h5>""", unsafe_allow_html=True)
    # Food AI part
    st.markdown("<h3 style='font-size: 30px;'>Ready to discover the flavors you crave?</h3>", unsafe_allow_html=True)
    with st.form('food_form'):
        food_question = st.text_input("Ask a city/country:", "", placeholder="e.g. Barcelona,Spain")
        food_submit = st.form_submit_button('Get TravelMate AI Response')

    user_input3 = f'List best recommendation foods in {food_question} in english'

    if food_submit:
        food_answer = food_ai(user_input3)
        st.text_area("TravelMate AI Response:", food_answer, height=1000)

#%%
def main():
    st.set_page_config(
        page_title="TravelMate AI",
        page_icon="✈️",

    )
    
    # Sidebar
    sb_style = """
    <style>
        .sidebar-title {
            font-size: 24px;
            font-family: 'Baskerville', sans-serif;
            text-align: center;
            color: #2B3A67;
            opacity: 0;
            animation: fadeIn 1s forwards;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
    </style>
    """
    st.sidebar.markdown(sb_style, unsafe_allow_html=True)
    st.sidebar.markdown('<span style="color: #f8f8ff;" class="sidebar-title"><strong>TravelMate AI ✈️</strong></span>', unsafe_allow_html=True)

    page_functions = {
        "🏡 Home": homepage,
        "🏛️ History": history_page,
        "🏞️ Tourism Spots": tourism_page,
        "🍔 Food Hunting": food_page,
        "📅 Travel Planner": history_page,
    }

    with st.sidebar:
        selected_page = option_menu(menu_title="Options", options=list(page_functions.keys()), icons=['.', '.', '.', '.', '.'], default_index=0)

    if selected_page in page_functions:
        page_functions[selected_page]()

if __name__ == "__main__":
    main()
# %%
