import whisper

model = whisper.load_model("base")
result = model.transcribe("adv13/prj01/10.000.m4a")
print(result["text"])
