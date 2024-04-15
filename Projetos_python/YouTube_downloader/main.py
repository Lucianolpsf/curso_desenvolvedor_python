'''
Programador: Alex Machado Ribeiro
Programa: YouTube downloader
Objetivo: baixar um vídeo do youtube.
'''

# NOTE: precisa instalar o pacote pytube: pip install pytube

from pytube import YouTube
from pytube.cli import on_progress # barra de progresso

# função para baixar o vídeo do youtube
def salvar_video(link_do_video):
    # mensagem de espera
    print('Baixando vídeo...')

    # NOTE: após a mensagem de baixando o vídeo, o progresso irá demorar um pouco para aparecer. Paciência...

    # captura o caminho do vídeo do youtube e exibe a barra de progresso
    yt = YouTube(link_do_video, on_progress_callback=on_progress)

    # pega a maior resolução possível
    video_stream = yt.streams.get_highest_resolution()

    # baixa o vídeo no diretório do projeto
    video_stream.download()

    # mensagem final a ser exibida
    return '\nDownload completo!'

# entra no loop
while True:
    # informa o link do vídeo
    link_do_video = input('Informe o link do YouTube para baixar ou aperte Enter para encerrar o progarma: ')

    # verifica se o usuário informou a url do vídeo
    if link_do_video != '':
        # executa função de baixar o vídeo
        print(salvar_video(link_do_video))
        continue
    else:
        # encerra o programa
        print('Programa encerrado!')
        break