# AI-enhanced Agents using DeepSeek LLM
from core.tts import speak_text
from core.stt import listen_to_user
from core.llm import deepseek_call
from Agents.prompts import *


def greet_agent(state):
    user_name = state.get("user_name", "friend")
    language = state.get("language", "English")
    conversation = []

    # Initial Greeting
    greet_prompt_inst = greet_prompt(user_name, language)
    greeting = deepseek_call(greet_prompt_inst)
    print(greeting)
    speak_text(greeting)
    response = listen_to_user()
    print("*"*100)
    print(response)
    print("*"*100)
    conversation.append({"agent": "greet", "ai": greeting, "user": response})

    # Mood extraction and follow-up
    state["user_mood"] = response.lower()

    # Second turn: empathetic follow-up based on mood
    follow_up_inst = follow_up_prompt(user_name, response, language)
    follow_up = deepseek_call(follow_up_inst)
    print(follow_up)
    speak_text(follow_up)
    user_reply = listen_to_user()
    print("*"*100)
    print(user_reply)
    print("*"*100)
    conversation.append({"agent": "greet", "ai": follow_up, "user": user_reply})

    # Third turn: offer to begin session
    while True:
        check_inst = check_prompt(user_name, user_reply, language)
        check_in = deepseek_call(check_inst)
        print(check_in)
        speak_text(check_in)
        final_reply = listen_to_user()
        print("*"*100)
        print(final_reply)
        print("*"*100)
        conversation.append({"agent": "greet", "ai": check_in, "user": final_reply})

        if any(x in final_reply.lower() for x in ["start", "ready", "yes", "go ahead"]):
            speak_text("Great! Let’s begin our session.")
            break
        elif any(x in final_reply.lower() for x in ["not yet", "wait", "no", "give me a moment"]):
            speak_text("Take your time. I'm here when you're ready.")
        else:
            speak_text("Thanks for sharing. Let me know when you're ready.")

    state["conversation"].extend(conversation)
    return state


def intro_agent(state):
    language = state.get("language", "English")
    intro = deepseek_call(intro_prompt(language))
    speak_text(intro)
    state["techniques"] = ["Box Breathing", "4-7-8 Breathing", "Alternate Nostril Breathing"]
    state["conversation"].append({"agent": "intro", "ai": intro})
    return state


def breathing_agent(state, index):
    language = state.get("language", "English")
    technique = state["techniques"][index]
    breath_prompt_inst = breathing_prompt(technique, language)
    instructions = deepseek_call(breath_prompt_inst)
    speak_text(f"Let's begin with {technique}.")
    speak_text(instructions)
    state[f"breath_{index+1}"] = "completed"
    state["conversation"].append({"agent": f"breath_{index+1}", "ai": instructions, "user": "completed"})
    return state


def reflection_agent(state):
    language = state.get("language", "English")
    speak_text("How are you feeling now after the breathing exercises?")
    response = listen_to_user()
    prompt = reflection_prompt(response, language)
    reflection_reply = deepseek_call(prompt)
    speak_text(reflection_reply)
    state["reflection"] = response
    state["conversation"].append({"agent": "reflection", "user": response, "ai": reflection_reply})
    return state


def scoring_agent(state):
    language = state.get("language", "English")
    user_inputs = [entry["user"] for entry in state["conversation"] if entry.get("user")]
    session_summary = " ".join(user_inputs)
    prompt = scoring_prompt(session_summary, language)
    response = deepseek_call(prompt)

    try:
        score = float(response.strip().split()[0])
    except:
        score = 0.5  # fallback

    state["improvement_score"] = score
    state["conversation"].append({"agent": "scoring", "ai": prompt, "score": score})
    return state


def goodbye_agent(state):
    language = state.get("language", "English")
    farewell = deepseek_call(goodbye_prompt(language))
    speak_text(farewell)
    state["conversation"].append({"agent": "goodbye", "ai": farewell})
    return state
