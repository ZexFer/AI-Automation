from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import openai
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    """Respond to incoming phone calls with a simple AI response"""
    resp = VoiceResponse()
    resp.say("Hello, this is your AI receptionist. How can I help you today?", voice="alice")
    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
