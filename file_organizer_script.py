import os
import shutil
from pathlib import Path

def organizar_arquivos():
    # Diretórios
    diretorio_origem = r"C:\Users\baker\OneDrive\Desktop\HOT\pollyana_vallentine\pollyana_vallentine"
    dir_imagens = r"C:\Users\baker\OneDrive\Desktop\HOT\pollyana_vallentine\imagens"
    dir_videos = r"C:\Users\baker\OneDrive\Desktop\HOT\pollyana_vallentine\vídeos"
    
    # Extensões de arquivos
    extensoes_imagem = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    extensoes_video = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v'}
    
    # Criar diretórios de destino se não existirem
    os.makedirs(dir_imagens, exist_ok=True)
    os.makedirs(dir_videos, exist_ok=True)
    
    # Contadores para relatório
    imagens_movidas = 0
    videos_movidos = 0
    pastas_processadas = 0
    
    print(f"Iniciando organização dos arquivos...")
    print(f"Diretório origem: {diretorio_origem}")
    print(f"Diretório imagens: {dir_imagens}")
    print(f"Diretório vídeos: {dir_videos}")
    print("-" * 60)
    
    # Percorrer todas as pastas no diretório origem
    for item in os.listdir(diretorio_origem):
        caminho_pasta = os.path.join(diretorio_origem, item)
        
        # Verificar se é um diretório
        if os.path.isdir(caminho_pasta):
            pastas_processadas += 1
            print(f"Processando pasta: {item}")
            
            # Listar arquivos na pasta
            arquivos = os.listdir(caminho_pasta)
            
            # Separar imagens e vídeos
            imagens = []
            videos = []
            
            for arquivo in arquivos:
                extensao = Path(arquivo).suffix.lower()
                if extensao in extensoes_imagem:
                    imagens.append(arquivo)
                elif extensao in extensoes_video:
                    videos.append(arquivo)
            
            print(f"  Encontrados: {len(imagens)} imagem(ns), {len(videos)} vídeo(s)")
            
            # Aplicar regras de movimentação
            if len(imagens) >= 1 and len(videos) == 0:
                # Caso 1: Apenas imagem(ns) - mover todas as imagens
                for imagem in imagens:
                    origem = os.path.join(caminho_pasta, imagem)
                    destino = os.path.join(dir_imagens, imagem)
                    
                    # Verificar se já existe arquivo com mesmo nome
                    contador = 1
                    nome_base, extensao = os.path.splitext(imagem)
                    while os.path.exists(destino):
                        novo_nome = f"{nome_base}_{contador}{extensao}"
                        destino = os.path.join(dir_imagens, novo_nome)
                        contador += 1
                    
                    shutil.move(origem, destino)
                    imagens_movidas += 1
                    print(f"  ✓ Imagem movida: {os.path.basename(destino)}")
                
            elif len(imagens) == 1 and len(videos) == 1:
                # Caso 2: 1 imagem e 1 vídeo - mover vídeo
                video = videos[0]
                origem = os.path.join(caminho_pasta, video)
                destino = os.path.join(dir_videos, video)
                
                # Verificar se já existe arquivo com mesmo nome
                contador = 1
                nome_base, extensao = os.path.splitext(video)
                while os.path.exists(destino):
                    novo_nome = f"{nome_base}_{contador}{extensao}"
                    destino = os.path.join(dir_videos, novo_nome)
                    contador += 1
                
                shutil.move(origem, destino)
                videos_movidos += 1
                print(f"  ✓ Vídeo movido: {os.path.basename(destino)}")
                
            else:
                # Outros casos - não fazer nada
                print(f"  → Pasta ignorada (não atende aos critérios)")
            
            print()
    
    # Relatório final
    print("=" * 60)
    print("RELATÓRIO FINAL:")
    print(f"Pastas processadas: {pastas_processadas}")
    print(f"Imagens movidas: {imagens_movidas}")
    print(f"Vídeos movidos: {videos_movidos}")
    print("Organização concluída!")

if __name__ == "__main__":
    try:
        organizar_arquivos()
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        input("Pressione Enter para sair...")
