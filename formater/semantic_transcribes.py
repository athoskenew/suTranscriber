import ast

class SemanticTranscribes:
    def __init__(self, file):
        self.file = file
        with open(self.file, 'r') as transcription:
            self.lines = transcription.readlines()

    def FormatLines(self, line):
        """Transforma cada linha de uma transcrição para um formato amigável de leitura.

        Args:
            line: uma linha de um arquivo de texto transcrito.

        Returns:
            Uma nova linha formatada de forma semântica e amigável para leitura.
        """

        dict = ast.literal_eval(line)
        formatted_time = f"[{dict['time']}]"
        return f"{formatted_time} {dict['text']}"
    
    def MakeSemantic(self):
        """Percorre um arquivo de transcrição, linha a linha e formata criando semântica amigável para leitura.

        Returns:
            Um arquivo de transcrição com linha formatadas e estruturadas semânticamente.
        """

        with open(self.file, 'w') as output:
            for line in self.lines:
                output.write(self.FormatLines(line.strip()) + '\n')