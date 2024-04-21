utilize o comando:
pip install -r requirements.txt
para instalar as bibliotecas necessárias

## 🌐 Sobre

Este projeto tem como finalidade utilizar a API da OpenAI "Whisper", para criar transcrições amigáveis, incluindo o tempo onde cada frase foi falada e um texto de alta qualidade.

## 📚 Conteúdos
- [🌐 Sobre](#-sobre)
- [🛠️ Recomendações do projeto](#-Recomendações-do-projeto)
- [💡 Utilização](#-utilização)
- [🚥 Status](#-status)
- [📄 Referências](#-referências)

## 🛠️ Recomendacoes do projeto

Este projeto utiliza:

```sh
Python3
OpenAI API
```

Certifique-se de ter todos os componentes instalados em sua máquina para testar a aplicação da maneira mais fluída possível, lembre-se de atualizar e construir as bibliotecas assim que fizer clone do repositório. As instruções de instalação e utilização serão informadas na seção [💡Utilização](#-utilização).

## 💡 Utilização
> [!Note]
<sup><strong>Está sendo implementada uma branch para utilização com o docker através de `docker compose -f "docker-compose.yml" up -d --build` mas ainda está em andamento!

1. Primeiro veja se você está com o Python3 instalado.

   - [Instalar Python3](https://www.python.org/downloads/)

2. Clone o repositório do GitHub:

```bash
git clone https://github.com/athoskenew/suTranscriber.git
```
3. Vá até o diretório do projeto:

```bash
cd suTranscriber
```
4. Instale o requirements.txt
```bash
pip install -r requirements.txt
```
5. Edite as seguintes linhas conforme o necessário
```python
# Key da api da OpenAi
api_key = "SUA_CHAVE_DA_OPENAI"
# nome do áudio de entrada (mp3, wav, aac ...)
audio_file = "CAMINHO_DO_ARQUIVO.mp3"
# nome do arquivo de saída
output = "transcription.txt"
```

## 🚥 Status

- [x] ~Arquitetura do projeto~
- [x] ~ADD Whisper~
- [x] ~ADD Transcriber~
- [x] ~ADD Formatador de transcrição~
- [ ] ADD Corte automático de áudio
- [ ] ADD Cenas do vídeo na transcrição
- [ ] ADD Outras ferramentas de transcrição

## 📄 Referências
[Whisper - OpenAI](https://openai.com/research/whisper)
