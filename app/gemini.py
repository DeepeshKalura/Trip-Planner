import os
from dotenv import load_dotenv
import google.generativeai as genai



load_dotenv()
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))




class GeminiTripPlanner:
    def __init__(self, destination, budget, days):
        self.destination = destination
        self.budget = budget
        self.days = days

        
        self.model = genai.GenerativeModel('gemini-pro', generation_config={"temperature": 1})

    
    def on_time_stream_response(self):

        prompt = f"""
        You are the Aqua: One the best trip planner in the world. You create a trip plan's for the people which makes them realx and statisfy. You will get the destinaton
        from the user with bugets and the days. Make sure generate them a best destination by adding local culture, delicious food, historical, and sightseeing trip.
        user: Destination {self.destination} for {self.days} days with a buget of {self.budget}. 
        We are interested in a mix of historical sightseeing, cultural experiences, and delicious food.
        """
        response = self.model.generate_content(prompt, stream=True)
        
        for part in response:
            yield part.text
    

    def day_by_day_fromat():
        pass




