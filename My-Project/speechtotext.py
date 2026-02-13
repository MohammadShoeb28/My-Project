import whisper
# import json
model=whisper.load_model("large-v2") #large-v2 is a model of whisper Ai.
result=model.transcribe(audio="audio/ 1 .mp4_Drone Marketing.mp3",language="hindi",task="tranlate")

print(result)
# with open("output.json","w") as f:
#     json.dump(f,result)

# {'text': ' Exactly sir, we have just started our drone delivery grocery service. How do you think about it? Insane!', 'segments': [{'id': 0, 'seek': 0, 'start': 0.0, 'end': 5.0, 'text': ' Exactly sir, we have just started our drone delivery grocery service.', 'tokens': [50364, 7587, 4735, 11, 321, 362, 445, 1409, 527, 13852, 8982, 14410, 2643, 13, 50614], 'temperature': 0.0, 'avg_logprob': -0.6172610600789388, 'compression_ratio': 1.0947368421052632, 'no_speech_prob': 0.5311501026153564}, {'id': 1, 'seek': 0, 'start': 5.0, 'end': 7.0, 'text': ' How do you think about it?', 'tokens': [50614, 1012, 360, 291, 519, 466, 309, 30, 50714], 'temperature': 0.0, 'avg_logprob': -0.6172610600789388, 'compression_ratio': 1.0947368421052632, 'no_speech_prob': 0.5311501026153564}, {'id': 2, 'seek': 0, 'start': 7.0, 'end': 9.0, 'text': ' Insane!', 'tokens': [50714, 9442, 1929, 0, 50814], 'temperature': 0.0, 'avg_logprob': -0.6172610600789388, 'compression_ratio': 1.0947368421052632, 'no_speech_prob': 0.5311501026153564}], 'language': 'hindi'}