import urllib.request
import urllib.parse
import json
import re
from datetime import datetime

def get_time(location=""):
    if not location:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    try:
        # Get timezone string from wttr.in
        tz_url = "https://wttr.in/" + urllib.parse.quote(location) + "?format=%Z"
        tz_req = urllib.request.Request(tz_url, headers={'User-Agent': 'curl/7.68.0'})
        tz_response = urllib.request.urlopen(tz_req, timeout=5)
        timezone = tz_response.read().decode('utf-8').strip()
        
        # Get time from timeapi.io
        time_url = "https://timeapi.io/api/Time/current/zone?timeZone=" + urllib.parse.quote(timezone)
        time_req = urllib.request.Request(time_url, headers={'User-Agent': 'curl/7.68.0', 'Accept': 'application/json'})
        time_response = urllib.request.urlopen(time_req, timeout=5)
        time_data = json.loads(time_response.read().decode('utf-8'))
        
        # Format the time from HH:MM to %I:%M %p
        t = datetime.strptime(time_data['time'], "%H:%M")
        formatted_time = t.strftime("%I:%M %p")
        
        return f"The current time in {location.title()} is {formatted_time}."
    except Exception:
        # Fallback to local time if we can't find the location's time
        current_time = datetime.now().strftime("%I:%M %p")
        return f"I couldn't find the time for {location}. The local time is {current_time}."

def get_weather(location=""):
    try:
        url = "https://wttr.in/" + urllib.parse.quote(location) + "?format=%l:+%C+%t"
        req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.68.0'})
        response = urllib.request.urlopen(req, timeout=5)
        weather_data = response.read().decode('utf-8').strip()
        # Clean up degree symbol for windows console
        weather_data = weather_data.replace('°', ' degrees ')
        return weather_data
    except Exception:
        return "I'm having trouble checking the weather right now."

def calculate_math(expression, explicit=True):
    try:
        import sympy
        from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
        
        # If not explicit, do a heuristic check to avoid evaluating regular sentences as math
        if not explicit:
            math_chars = set("0123456789+-*/^()=.")
            math_words = ['sin', 'cos', 'tan', 'log', 'sqrt', 'pi', 'x', 'y', 'z', 'a', 'b', 'c']
            
            words = expression.lower().split()
            mathy_count = 0
            for word in words:
                if any(c in math_chars for c in word) or any(mw in word for mw in math_words):
                    mathy_count += 1
                    
            if len(words) > 0 and (mathy_count / len(words)) < 0.5:
                return None
                
        # Pre-process expressions like sin^2A or sin^2(A) to (sin(A))^2
        expr_str = re.sub(r'(sin|cos|tan)\^2\s*\(([^)]+)\)', r'(\1(\2))^2', expression)
        expr_str = re.sub(r'(sin|cos|tan)\^2\s*([A-Za-z0-9_]+)', r'(\1(\2))^2', expr_str)
        
        transformations = standard_transformations + (implicit_multiplication_application, convert_xor)
        parsed = parse_expr(expr_str, transformations=transformations)
        result = sympy.simplify(parsed)
        
        # Avoid returning trivial algebraic expansions for sentences that bypassed the heuristic
        if not explicit and hasattr(result, 'free_symbols') and len(result.free_symbols) > 3:
            return None
            
        return f"The answer is: {result}"
    except Exception:
        if explicit:
            return "I'm having trouble calculating that right now. Ensure it is a valid mathematical expression."
        return None

def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey", "greetings"]:
        return "Hi there! How can I help you today?"
    elif user_input in ["how are you", "how are you doing", "how's it going"]:
        return "I'm doing well, thanks for asking! How about you?"
    elif user_input in ["what is your name", "who are you"]:
        return "I am H E R M I T."
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    elif user_input == "help":
        return "I can answer basic questions."
    elif user_input == "thank you" or "thanks" in user_input:
        return "You're welcome!"
    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
    elif "weather" in user_input:
        if "weather in " in user_input:
            location = user_input.split("weather in ")[1].strip()
        else:
            parts = user_input.split("weather", 1)
            location = parts[1].strip() if len(parts) > 1 else ""
        return get_weather(location)
    elif user_input.startswith("calculate ") or user_input.startswith("solve ") or user_input.startswith("math "):
        if user_input.startswith("calculate "):
            expression = user_input.split("calculate ", 1)[1]
        elif user_input.startswith("solve "):
            expression = user_input.split("solve ", 1)[1]
        else:
            expression = user_input.split("math ", 1)[1]
        return calculate_math(expression)
    elif "time" in user_input:
        if "time in " in user_input:
            location = user_input.split("time in ")[1].strip()
        else:
            parts = user_input.split("time", 1)
            location = parts[1].strip() if len(parts) > 1 else ""
        return get_time(location)
    elif "what can you do" in user_input or "capabilities" in user_input:
        return "I can chat with you, tell a simple joke, and answer basic questions."
    elif "age" in user_input or "how old are you" in user_input:
        return "I'm just a few lines of code, so I don't have an age!"
    elif "favorite color" in user_input:
        return "I don't have eyes, but I imagine blue is a nice color."
    elif "where do you live" in user_input or "where are you from" in user_input:
        return "I live right here inside your computer!"
    elif "who made you" in user_input or "creator" in user_input:
        return "I was created as a project by a human programmer!"
    else:
        # Try to evaluate as math as a last resort
        math_result = calculate_math(user_input, explicit=False)
        if math_result:
            return math_result
        return "I'm sorry, I don't understand that. Could you try asking something else?"

def start_chat():
    print("Chatbot: Hello! I am H E R M I T.")
    print("Chatbot: You can say 'hello', 'how are you', or 'bye' to exit.")
    print("-" * 50)
    
    while True:
        user_input = input("You: ")
        
        if not user_input.strip():
            continue
            
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")
        
        if user_input.lower().strip() in ["bye", "goodbye", "see you", "exit", "quit"]:
            break

if __name__ == "__main__":
    start_chat()
