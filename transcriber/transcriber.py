"""Classe responsável pela transcrição de um áudio"""

from openai import OpenAI
from transcriber.semantic_time import SemanticTime

class Transcriber:
    def __init__(self, api_key):
        self.client = OpenAI(api_key = api_key)
        self.semanticTime = SemanticTime()
    

    def TakeTranscription(self, audio_file):
        """Recebe a transcrição via Whisper da OpenAi

        Args:
            audio_file: Path do arquivo de áudio que deseja transcrever.

        Returns:
            A Transcrição verbosa do áudio (confira a API da OpenAI para mais informações).
        """

        audio = open(audio_file, "rb")
        transcript = self.client.audio.transcriptions.create(
        file=audio,
        model="whisper-1",
        response_format="verbose_json",
        timestamp_granularities=["segment"]
        )

        return transcript


    def MakeSegment(self, segment, offset=0):
        """Recebe um segmento de áudio transcrito e formata o tempo semânticamente

        Args:
            segment: Segmento verboso de uma transcrição de áudio via Whisper.
            offset: Um argumento opcional para aumentar o valor do inicio (padrão: 0).

        Returns:
            A Transcrição com tempo semântico do áudio.
        """

        text = segment['text']
        time = self.semanticTime.format_timestamp(segment['start'], offset)

        return {'time': time, 'text': text}
    

    def MakeTranscription(self, transcript, filename, offset=0):
        """Cria a transcrição com base na quantidade de texto gerado.

        Args:
            transcript: Transcrição verbosa do áudio.
            filename: Nome do arquivo de saída.
            offset: Um argumento opcional para aumentar o valor do inicio (padrão: 0).

        Returns:
            Cria um arquivo de texto com a transcrição e retorna uma lista de segmentos semânticos da transcrição.
        """

        transcription = []
        for segment in transcript.segments:
            transcription.append(self.MakeSegment(segment, offset=offset))

        with open(filename, "w") as output:
            for line in transcription:
                output.write(str(line) + "\n")

        return transcription