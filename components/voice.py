"""
Voice Input — browser microphone capture via Streamlit's st.audio_input.

Uses SpeechRecognition with Google's free Web Speech API backend.
Requires: speechrecognition (pip install SpeechRecognition)

Usage:
    from components.voice import transcribe_audio
    transcript = transcribe_audio(audio_bytes)   # returns str or None
"""

import io
from typing import Optional


def transcribe_audio(audio_bytes: bytes) -> Optional[str]:
    """
    Convert raw audio bytes (WAV/WebM from st.audio_input) to text.

    Returns:
        Transcribed string on success, None on failure or silence.
    """
    try:
        import speech_recognition as sr

        r = sr.Recognizer()
        # st.audio_input returns bytes; wrap in BytesIO for AudioFile
        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
            audio_data = r.record(source)

        text = r.recognize_google(audio_data, language="en-IN")
        return text.strip() if text else None

    except Exception:
        # Covers: UnknownValueError (silence/noise), RequestError (no internet),
        # ImportError (package missing), and format errors.
        return None
