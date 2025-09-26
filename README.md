# 🚀 Projetos Python - Utilitários de Mídia

Uma coleção de scripts Python para organização e processamento de arquivos multimídia.

## 📋 Projetos Incluídos

### 1. 📁 Organizador de Arquivos - Pollyana Valentine
### 2. 🎬 Conversor de Velocidade de Vídeos

---

## 📁 Organizador de Arquivos - Pollyana Valentine

Um script Python para organizar automaticamente imagens e vídeos em diretórios específicos baseado em regras predefinidas.

### 🎯 Funcionalidades

O script percorre todas as pastas dentro do diretório principal e aplica as seguintes regras:

- **📸 Apenas imagens na pasta**: Move todas as imagens para o diretório `imagens`
- **🎬 1 imagem + 1 vídeo**: Move o vídeo para o diretório `vídeos`
- **❌ Outros casos**: Ignora a pasta (não move nenhum arquivo)

### 📂 Estrutura de Diretórios

```
C:\Users\baker\OneDrive\Desktop\HOT\pollyana_vallentine\
├── pollyana_vallentine\          # Diretório origem (com subpastas)
│   ├── pasta1\                   # Contém arquivos a serem organizados
│   ├── pasta2\
│   └── ...
├── imagens\                      # Destino das imagens
└── vídeos\                       # Destino dos vídeos
```

---

## 🎬 Conversor de Velocidade de Vídeos

Script completo para alterar a velocidade de vídeos, disponível em **3 versões** diferentes.

### 🖥️ Versão Desktop (Python)

**Arquivo:** `video_speed_converter.py`

#### **Funcionalidades:**
- ✅ **Processamento em lote**: Converte múltiplos vídeos automaticamente
- ✅ **Interface interativa**: Menu intuitivo com emojis
- ✅ **Análise detalhada**: Mostra informações dos vídeos (duração, tamanho, resolução)
- ✅ **Múltiplas opções de saída**: Sobrescrever, novos arquivos ou pasta específica
- ✅ **Relatório completo**: Estatísticas de processamento e erros

#### **Instalação:**
```bash
# Instalar dependências
pip install moviepy

# Para usar FFmpeg diretamente (versão alternativa)
# Windows: Baixar em https://ffmpeg.org/download.html
# Mac: brew install ffmpeg
# Linux: sudo apt install ffmpeg
```

#### **Uso:**
```bash
python video_speed_converter.py
```

### 📱 Versão Mobile (Python - Termux/Pythonista)

**Arquivo:** `mobile_video_converter.py`

#### **Para Android (Termux - Gratuito):**
1. Instale **Termux** da Play Store
2. Execute os comandos:
```bash
pkg update && pkg upgrade
pkg install python ffmpeg
pip install moviepy
```
3. Execute: `python mobile_video_converter.py`

#### **Para iPhone (Pythonista - $10):**
1. Compre **Pythonista** na App Store
2. Dentro do app: `pip install moviepy`
3. Execute o script no Pythonista

#### **Recursos Mobile:**
- 📱 **Interface otimizada** para terminal mobile
- ⚡ **Configurações otimizadas** para economia de bateria
- 🔧 **Detecção automática** de dispositivo móvel
- 📊 **Relatórios detalhados** mesmo no celular

### 🌐 Versão Web (HTML/JavaScript)

**Arquivo:** `mobile_web_converter.html`

#### **Funcionalidades:**
- 🌐 **Funciona no navegador** (sem instalação)
- 📱 **Design responsivo** para celular
- 🎯 **Preview em tempo real** da velocidade
- 📤 **Hospedagem no GitHub Pages**

#### **Limitações:**
- ⚠️ **Apenas preview** no celular (processamento limitado)
- 💻 **Para conversão real**: use as versões Python

#### **Como hospedar no GitHub Pages:**
1. Crie um repositório público no GitHub
2. Adicione o arquivo `mobile_web_converter.html` como `index.html`
3. Ative GitHub Pages nas configurações
4. Acesse: `https://seuusuario.github.io/nome-repositorio/`

---

## 🔧 Requisitos Gerais

### **Organizador de Arquivos:**
- Python 3.6 ou superior
- Bibliotecas padrão: `os`, `shutil`, `pathlib`

### **Conversor de Vídeos:**
- Python 3.6 ou superior
- **MoviePy**: `pip install moviepy`
- **FFmpeg** (instalado automaticamente com MoviePy)

---

## 📋 Formatos Suportados

### 🖼️ Imagens
- `.jpg`, `.jpeg`, `.png`, `.gif`
- `.bmp`, `.tiff`, `.webp`

### 🎥 Vídeos  
- `.mp4`, `.avi`, `.mov`, `.mkv`
- `.wmv`, `.flv`, `.webm`, `.m4v`, `.3gp`

---

## 🚀 Exemplos de Uso

### **Organizador de Arquivos:**
```bash
python file_organizer_script.py
```

**Saída esperada:**
```
Iniciando organização dos arquivos...
Processando pasta: exemplo_pasta
  → Movendo 5 imagem(ns)...
    ✓ Imagem movida: foto1.jpg
    ✓ Imagem movida: foto2.png
    
============================================================
RELATÓRIO FINAL:
Pastas processadas: 10
Imagens movidas: 25
Vídeos movidos: 8
Organização concluída!
```

### **Conversor de Vídeos:**
```bash
python video_speed_converter.py
```

**Saída esperada:**
```
🎬 CONVERSOR DE VELOCIDADE DE VÍDEOS
==========================================

📁 Digite caminho (Enter = pasta atual): 
📹 Encontrados 3 vídeos:
  1. video1.mp4 (50.2 MB) - 2m30s - 1920x1080
  2. video2.mp4 (25.1 MB) - 1m15s - 1280x720

⚡ Digite velocidade (ex: 2.0): 2.0
🚀 Iniciar conversão? (s/N): s

✅ Sucessos: 3/3 ⏱️ Tempo: 5m30s
🎉 Conversão concluída!
```

---

## ⚡ Recursos Avançados

### **Organizador:**
- ✅ **Criação automática** dos diretórios de destino
- ✅ **Prevenção de conflitos** - renomeia arquivos duplicados
- ✅ **Debug completo** - mostra todos os arquivos encontrados
- ✅ **Tratamento de erros** para operações seguras

### **Conversor:**
- ✅ **Interface multilíngue** (português)
- ✅ **Detecção automática** de formato e codec
- ✅ **Otimizações específicas** para mobile
- ✅ **Backup automático** (modo sobrescrita)
- ✅ **Velocidades sugeridas** com explicações

---

## 🔧 Personalização

### **Organizador - Alterar diretórios:**
```python
diretorio_origem = r"C:\seu\caminho\origem"
dir_imagens = r"C:\seu\caminho\imagens"
dir_videos = r"C:\seu\caminho\vídeos"
```

### **Organizador - Adicionar formatos:**
```python
extensoes_imagem = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'}
extensoes_video = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.3gp'}
```

### **Conversor - Velocidades personalizadas:**
```python
# Exemplos de velocidades comuns
VELOCIDADES_COMUNS = {
    0.25: "4x mais lento",
    0.5: "2x mais lento", 
    0.75: "1.3x mais lento",
    1.0: "Velocidade normal",
    1.25: "1.25x mais rápido",
    1.5: "1.5x mais rápido",
    2.0: "2x mais rápido",
    3.0: "3x mais rápido",
    4.0: "4x mais rápido"
}
```

---

## ⚠️ Avisos Importantes

### **Geral:**
- **Backup recomendado**: Faça backup dos arquivos antes da primeira execução
- **Operações destrutivas**: Scripts movem/alteram arquivos originais
- **Teste primeiro**: Execute com poucos arquivos para testar

### **Organizador:**
- **Arquivos duplicados**: São automaticamente renomeados
- **Operação de movimento**: Arquivos são movidos (não copiados)

### **Conversor:**
- **Processamento pesado**: Vídeos grandes podem demorar muito
- **Espaço em disco**: Conversões podem gerar arquivos maiores
- **Qualidade**: Use configurações adequadas para cada situação

---

## 🐛 Solução de Problemas

### **Erro: "MoviePy não encontrado"**
```bash
pip install --upgrade moviepy
```

### **Erro: "FFmpeg não encontrado"**
```bash
# Windows
# Baixe em: https://ffmpeg.org/download.html

# Mac
brew install ffmpeg

# Linux
sudo apt update && sudo apt install ffmpeg
```

### **Erro: "Permissão negada"**
- Execute como administrador/sudo
- Verifique se os arquivos não estão sendo usados por outros programas

### **Vídeo não processa no mobile**
- Use arquivos menores (< 100MB)
- Prefira formato MP4
- Verifique espaço em disco disponível

---

## 📊 Compatibilidade

| Sistema | Organizador | Conversor Desktop | Conversor Mobile |
|---------|-------------|-------------------|------------------|
| Windows 10/11 | ✅ | ✅ | ✅ (via Python) |
| macOS | ✅ | ✅ | ✅ (via Python) |
| Linux | ✅ | ✅ | ✅ (via Python) |
| Android | ❌ | ❌ | ✅ (via Termux) |
| iPhone | ❌ | ❌ | ✅ (via Pythonista) |

---

## 🎯 Roadmap

### **Futuras melhorias:**
- [ ] Interface gráfica (GUI) com tkinter
- [ ] Suporte a mais formatos de vídeo
- [ ] Conversão com preservação de qualidade avançada
- [ ] Modo de processamento em paralelo
- [ ] Integração com serviços de nuvem
- [ ] App mobile nativo

---

## 📝 Licença

Este projeto é de uso livre para fins pessoais e educacionais.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Submeter pull requests
- Compartilhar casos de uso

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a seção **Solução de Problemas**
2. Consulte a documentação dos scripts
3. Teste com arquivos menores primeiro

---

**Desenvolvido para organização e processamento eficiente de arquivos multimídia** 🎯

**Última atualização:** 2025 - Versão completa com suporte mobile