"""Classe que formata o tempo da transcrição"""

class SemanticTime:

    def format_timestamp(self, seconds, offset=0):
        """Formata o tempo em segundo para uma string com zeros para minutos e segundos.

        Args:
            seconds: O número total em segundos.
            offset: Um argumento opcional para aumentar o valor do inicio (padrão: 0).

        Returns:
            Uma string formatada que representa o tempo (ex., "01:23").
        """

        total_minutes = int((seconds + offset) / 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        seconds = int(seconds % 60)

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# To test method:
# print(SemanticTime().format_timestamp(65))