import os
import subprocess
import sys
from pathlib import Path

def check_ffmpeg():
    """Verifica se o FFmpeg está instalado"""
    try:
        subprocess.run(['ffmpeg', '-version'], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL, 
                      check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_video_files(directory):
    """Busca todos os arquivos de vídeo no diretório"""
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.3gp'}
    video_files = []
    
    for file_path in Path(directory).iterdir():
        if file_path.is_file() and file_path.suffix.lower() in video_extensions:
            video_files.append(file_path)
    
    return video_files

def change_video_speed(input_file, output_file, speed_factor):
    """Altera a velocidade do vídeo usando FFmpeg"""
    try:
        # Comando FFmpeg para alterar velocidade (vídeo e áudio)
        cmd = [
            'ffmpeg',
            '-i', str(input_file),
            '-filter_complex', f'[0:v]setpts={1/speed_factor}*PTS[v];[0:a]atempo={speed_factor}[a]',
            '-map', '[v]',
            '-map', '[a]',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-y',  # Sobrescrever arquivo se existir
            str(output_file)
        ]
        
        print(f"Processando: {input_file.name}...")
        
        # Executa o comando
        result = subprocess.run(cmd, 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE, 
                              text=True)
        
        if result.returncode == 0:
            print(f"✓ Concluído: {output_file.name}")
            return True
        else:
            print(f"✗ Erro ao processar {input_file.name}: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Erro inesperado ao processar {input_file.name}: {str(e)}")
        return False

def main():
    print("=== CONVERSOR DE VELOCIDADE DE VÍDEOS ===\n")
    
    # Verifica se o FFmpeg está instalado
    if not check_ffmpeg():
        print("❌ ERRO: FFmpeg não encontrado!")
        print("Por favor, instale o FFmpeg:")
        print("- Windows: https://ffmpeg.org/download.html")
        print("- Mac: brew install ffmpeg")
        print("- Linux: sudo apt install ffmpeg")
        return
    
    # Solicita o diretório dos vídeos
    while True:
        directory = input("Digite o caminho da pasta com os vídeos (ou Enter para pasta atual): ").strip()
        
        if not directory:
            directory = "."
        
        if os.path.exists(directory) and os.path.isdir(directory):
            break
        else:
            print("❌ Diretório não encontrado! Tente novamente.")
    
    # Busca vídeos no diretório
    video_files = get_video_files(directory)
    
    if not video_files:
        print("❌ Nenhum arquivo de vídeo encontrado no diretório!")
        print("Formatos suportados: .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .m4v, .3gp")
        return
    
    print(f"📹 Encontrados {len(video_files)} vídeo(s):")
    for video in video_files:
        print(f"  • {video.name}")
    
    # Solicita a velocidade desejada
    while True:
        try:
            speed_input = input("\nDigite a velocidade desejada (ex: 2.0, 1.5, 0.5): ").strip()
            speed_factor = float(speed_input)
            
            if speed_factor <= 0:
                print("❌ A velocidade deve ser maior que 0!")
                continue
            
            if speed_factor > 100:
                print("❌ Velocidade muito alta! Use um valor menor que 100.")
                continue
                
            break
            
        except ValueError:
            print("❌ Digite um número válido (ex: 2.0, 1.5, 0.5)")
    
    # Pergunta se quer sobrescrever ou criar novos arquivos
    print(f"\n📁 Opções de saída:")
    print("1. Sobrescrever arquivos originais")
    print("2. Criar novos arquivos (adiciona '_speed{velocidade}x' no nome)")
    
    while True:
        choice = input("Escolha (1 ou 2): ").strip()
        if choice in ['1', '2']:
            break
        print("❌ Digite 1 ou 2")
    
    overwrite = (choice == '1')
    
    # Confirmação
    action = "sobrescrever" if overwrite else "criar novos arquivos para"
    print(f"\n⚠️  Você vai {action} {len(video_files)} vídeo(s) com velocidade {speed_factor}x")
    confirm = input("Continuar? (s/N): ").strip().lower()
    
    if confirm not in ['s', 'sim', 'y', 'yes']:
        print("❌ Operação cancelada.")
        return
    
    # Processa os vídeos
    print(f"\n🚀 Iniciando conversão para {speed_factor}x...\n")
    
    success_count = 0
    failed_files = []
    
    for video_file in video_files:
        if overwrite:
            # Cria arquivo temporário e depois substitui
            temp_output = video_file.with_suffix('.temp' + video_file.suffix)
            output_file = video_file
        else:
            # Cria novo arquivo com sufixo
            speed_suffix = f"_speed{speed_factor}x"
            output_file = video_file.with_stem(video_file.stem + speed_suffix)
        
        # Processa o vídeo
        temp_file = temp_output if overwrite else output_file
        
        if change_video_speed(video_file, temp_file, speed_factor):
            if overwrite:
                # Move o arquivo temporário para substituir o original
                try:
                    temp_file.replace(output_file)
                    success_count += 1
                except Exception as e:
                    print(f"✗ Erro ao substituir {video_file.name}: {str(e)}")
                    failed_files.append(video_file.name)
                    if temp_file.exists():
                        temp_file.unlink()  # Remove arquivo temporário
            else:
                success_count += 1
        else:
            failed_files.append(video_file.name)
            # Remove arquivo temporário se houver erro
            if overwrite and temp_file.exists():
                temp_file.unlink()
    
    # Relatório final
    print(f"\n{'='*50}")
    print(f"📊 RELATÓRIO FINAL:")
    print(f"✅ Sucessos: {success_count}/{len(video_files)}")
    
    if failed_files:
        print(f"❌ Falhas: {len(failed_files)}")
        print("Arquivos com erro:")
        for file in failed_files:
            print(f"  • {file}")
    
    if success_count > 0:
        print(f"🎉 Conversão concluída! Velocidade alterada para {speed_factor}x")
    
    print(f"{'='*50}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {str(e)}")
    
    input("\nPressione Enter para sair...")
