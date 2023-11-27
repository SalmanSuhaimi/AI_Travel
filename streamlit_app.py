import streamlit as st
import os
from openai import OpenAI
from streamlit_option_menu import option_menu
import requests

serpapi_Api_key = st.secrets["SERPAPI_API_KEY"]
openai_api_key = st.secrets["OPENAI_API_KEY"]
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

#%% for travel planner

system_prompt4 = """ You are a virtual guide and assistant. You are a travel planner, and your responses should be attractive and use emojis. Listing what itinerary suggestions to do.  Make sure it is in English."""

question4 = """
I want to go Barcelona for 7 days. Type of travel is backpacking and type of attraction is natural attraction. Transportation is none
"""

answer4 = """
🌞 Barcelona Backpacking Adventure 🎒

Day 1: 🏨 Check-in at your hostel and explore Barcelona's vibrant streets. Start with a visit to Park Güell, a stunning natural attraction designed by Gaudí. Don't forget to take lots of #selfies! 📸

Day 2: 🍊 Head to Mount Montjuïc for breathtaking views of the city and the sea. Walk or take the cable car to the top and enjoy a picnic surrounded by nature. 🌳

Day 3: 🐟 Visit Barceloneta Beach and soak up the sun. Take a dip in the Mediterranean Sea and try some delicious seafood at the beachfront restaurants. 🏖️

Day 4: ⛰️ Explore the natural beauty of Montserrat Mountain. Take a train and cable car to this iconic destination, known for its stunning rock formations and the Benedictine monastery. 🚂

Day 5: 🌴 Wander through the scenic Park de la Ciutadella, Barcelona's central park. Rent a rowboat to explore the lake or relax in the shade of the palm trees. 🚣‍♀️

Day 6: 🌺 Enjoy Tibidabo Mountain, offering panoramic views of the city. Visit the amusement park, take a hike, or have a picnic at one of the highest points in Barcelona. 🎡

Day 7: 🌊 Take a day trip to the beautiful Costa Brava coastline. Explore hidden coves, swim in crystal-clear water, and relax on picturesque beaches. 🏝️

Don't forget to try local cuisine and immerse yourself in Barcelona's vibrant culture! Enjoy your backpacking adventure! 💃🌍🎒🌞🌴🍊🐟⛰️🌺🌊✨😎"""

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
def planner_ai(msg):
    planner_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
                    {
            
                        "role":"system",
                        "content": system_prompt4
                    },
                    {
                        "role": "user",
                        "content": question4
                    },
                    {
                        "role":"assistant",       
                        "content": answer4
                    },
                    {
                        "role": "user",
                        "content": f'{msg}'
                    }
        ],
        max_tokens = 1000,
    
        temperature = 1.0
    )

    planner = planner_response.choices[0].message.content
    #print(story)
    return planner

#%%
def image_ai(msg):
    cover_response = client.images.generate(
    model="dall-e-3",
    prompt=msg,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = cover_response.data[0].url
    # print(image_url) 
    #display(Image(url=image_url))
    return image_url

def design_ai(msg):
    design_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{
                        "role":"system",
                        "content": """
                        Based on the place/country given.
                        You will generate a detailed image prompt for the place/country. 
                        Image prompt should include relevent style and color, style of the picture should look realistic"""
                    },
                    {
                        "role":"user",
                        "content":f'{msg}'
                    }
        ],
        max_tokens = 1000,
        temperature = 1.0
    )

    design_prompt = design_response.choices[0].message.content
    #print(design_prompt)
    return design_prompt

#%%
# main function to chain everything

def combine_ai(user_prompt):
    plan = planner_ai(user_prompt)
    design = design_ai(plan)
    image = image_ai(design)
    
    st.image(image, caption="Generated Image", use_column_width=True)
    st.write("Story:", plan)
#%%
@st.cache_data
def serpapi_image_search(query, num_results=5):
    
    # Define SerpAPI parameters
    params = {
        "api_key": serpapi_Api_key,
        "engine": "google_images",
        "q": query,
        "google_domain": "google.com",
        "hl": "en",
        "gl": "us",
        "device": "desktop",
    }

    # Make the SerpAPI request
    response = requests.get("https://serpapi.com/search.json", params=params).json()

    # Debugging: Display the entire SerpAPI response
    # st.write("SerpAPI Response:", response)

    # Check if image results are present in the response
    if "images_results" in response:
        # Extract image results from the response
        all_image_results = [result["original"] for result in response["images_results"]]

        # Limit the results to the specified number
        image_results = all_image_results[:num_results]

        # Debugging: Display the image results
        # st.write("Image Results:", image_results)

        return image_results
    else:
        st.warning("No relevant images found.")
        return []

#%%

    # Replace this URL with the raw URL of your hosted image on GitHub
background_image_url = "https://raw.githubusercontent.com/SalmanSuhaimi/AI_Travel/main/bg.png"
#%%

def homepage():
# Set the page configuration with the background image
    
    header = st.container()
    description = st.container()

    github_gif_url = "https://raw.githubusercontent.com/SalmanSuhaimi/AI_Travel/main/giphy.gif"

    h1_style = """
    <style>
        .app-title {
            font-size: 60px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-top: 50px;
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
       h5_style = "<style>.subh-title { color: #000000; font-size: 22px; text-align: center; }</style>"
       st.markdown(h5_style, unsafe_allow_html=True)
       st.markdown("""<h5 class="subh-title">Your easy way to explore!</h5>""", unsafe_allow_html=True)
       st.markdown("""<p class="subh-title">Travel Planner | Tourism Spots | Food Hunting | History </p>""", unsafe_allow_html=True)

#%%
travel = ['Adventure','Backpacking','Business','Educational','Eco-Tourism','Family','Group','Leisure','Luxury','Solo','Volunteer']
att = ['Natural','Botanical Gardens','Cultural','Design','Entertainment','Fashion','Holiday','Music','Religious','Scenic','Science','Sports','Urban','Vintage']
#%%
def planner_page():
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
    st.markdown("""<h5 style='text-align: center; font-size: 48px;'><strong>TravelMate AI: Plan Your Next Getaway📝</strong></h5>""", unsafe_allow_html=True)
    # Planner AI part
    st.markdown("<h3 style='font-size: 30px;'>Ready to imagine your plan?</h3>", unsafe_allow_html=True)
    with st.form('planner_form'):
        destination = st.text_input("Destination:", "", placeholder="e.g. Delhi,India")
        
        col1, col2 = st.columns(2)
        with col1:
            days = st.number_input("Days:", 1)

            type_travel = st.multiselect("Type of Travel:", travel, placeholder="You can select multiple")
            
            if type_travel == []:
                type_travel = ",".join(travel)
            else:
                type_travel = ",".join(type_travel)

        with col2:
            type_transportation = st.text_input("Transportation:", "", placeholder="e.g. Airplane")
            att_travel = st.selectbox("Type of Attraction:", att, index=0)
            

            planner_submit = st.form_submit_button('Get TravelMate AI Response')

    user_input4 = f'i want to go {destination} for {days} days. The type of travel is {type_travel}. The type of transportation is {type_transportation}. The type of attraction is {att_travel}.'

    if planner_submit:
        planner_answer = f"TravelMate AI Response: {combine_ai(user_input4)}"

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
        attraction_question = st.text_input("Ask a place/city/country:", "", placeholder="e.g. Milan, Italy")
        attraction_submit = st.form_submit_button('Get TravelMate AI Response')

    user_input2 = f'Attraction places for {attraction_question} in english'

    if attraction_submit:
    # Call the serpapi_image_search function
        image_results = serpapi_image_search(user_input2, num_results=2)

    # Display the image search results
        st.subheader(f"Image Search Results for: {user_input2}")

        for index, image_url in enumerate(image_results, start=1):
            st.image(image_url, caption=f"Image {index}")
            st.write("---")

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
        "📅 Travel Planner": planner_page,
        "🏞️ Tourism Spots": tourism_page,
        "🍔 Food Hunting": food_page,
        "🏛️ History": history_page,
    }

    with st.sidebar:
        selected_page = option_menu(menu_title="Options", options=list(page_functions.keys()), icons=['.', '.', '.', '.', '.'], default_index=0)

    if selected_page in page_functions:
        page_functions[selected_page]()

if __name__ == "__main__":
    main()
