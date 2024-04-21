# Cria transcrições semânticas baseadas nas transcrições do Whisper da OpenAi
from transcriber.transcriber import Transcriber
from formater.semantic_transcribes import SemanticTranscribes

# Key da api da OpenAi
api_key = ""
# nome do áudio de entrada (mp3, wav, aac ...)
audio_file = "audio.mp3"
# nome do arquivo de saída
output = "transcription.txt"

# inicializa o Transcriber
transcriber = Transcriber(api_key=api_key)

# Gera a transcrição pelo Whisper da OpenAi
print("Gerando transcrição...")
transcription = transcriber.TakeTranscription(audio_file)
#print(transcription)
print("Transcrição criada!")

# Cria um arquivo .txt com a transcrição obtida
print("Formatando Transcrição...")
formated_transcription = transcriber.MakeTranscription(transcription, output)
print("Transcrição formatada!")

# Opcional - Deixa a transcrição semântica no formato -> [hh:mm:ss] texto
print("Criando semântica...")
SemanticTranscribes(output).MakeSemantic()
print("Semântica criada!")