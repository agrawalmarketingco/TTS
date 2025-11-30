from flask import Flask, render_template, request, jsonify, send_file ,Response,send_from_directory
import asyncio
import uuid
import os
from app import tts_generate


app = Flask(__name__)
@app.route('/service-worker.js')
def service_worker():
    return send_from_directory('static', 'service-worker.js')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/extract")
def extract():
    return render_template("extract.html")
    
@app.route("/conversion" , methods=["POST"])
async def conversion():
    text = request.form["text"]
    voice = request.form["voice"]
    
    if not text or not voice:
        return jsonify({"error":"Text and voice are required for conversion. Check if anything is missing and then try again"}),400
    
    if voice not in ["en-IN-PrabhatNeural", "en-IN-NeerjaNeural", "en-IN-NeerjaExpressiveNeural"]:
        return jsonify({"error": "Invalid voice selected."}), 400
    
    try:
        audio_buffer = await tts_generate(text, voice)
        
        return Response(
            audio_buffer,
            mimetype="audio/mpeg",  # MP3 format
            status=200
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)