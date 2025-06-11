# SafeCross Vision - Gestos

Este projeto utiliza visão computacional para detectar gestos de mãos em vídeo, com o objetivo de identificar sinais de parada, alerta, emergência e direção, facilitando a comunicação visual em ambientes de risco ou baixa luminosidade.

## Funcionalidades

- **Detecção de gestos de mão** em tempo real usando MediaPipe.
- **Reconhecimento dos seguintes gestos:**
  - **Mão aberta:** Exibe alerta "1 OPEN HAND - PARE!"
  - **Punho fechado:** Exibe alerta "FIST - ALERTA DESATIVADO"
  - **Duas mãos para cima:** Exibe alerta "2 HANDS UP - EMERGENCIA DETECTADA!"
  - **Apontando:** Exibe alerta "GESTO DE DIRECAO"
- **Exibição dos alertas** diretamente sobre o vídeo, com cores diferentes para cada situação.
- **Desenho dos pontos e conexões das mãos** detectadas no vídeo.
- **Execução em tela cheia** para melhor visualização.
- **Compatível com vídeos gravados** (exemplo: `samples/dark_environment_test.mp4`).

## Como rodar

1. **Pré-requisitos:**
   - Python 3.7 ou superior
   - Instale as dependências:
     ```
     pip install r- requirements.txt
     ```
3. **Executando o programa:**
- No terminal, navegue até a pasta do projeto:
  ```
  cd "c:\Users\{User}\...\GS - IOT"
  ```
- Execute o script principal:
  ```
  python [main.py](http://_vscodecontentref_/2)
  ```

4. **Funcionamento:**
- O programa abrirá o vídeo `samples/dark_environment_test.mp4` em tela cheia.
- Os gestos das mãos serão detectados e os alertas correspondentes aparecerão sobre o vídeo.
- Para sair, pressione `ESC`.

## Observações

- Para usar outro vídeo, altere o caminho em `main.py` na linha:
  ```python
  cap = cv2.VideoCapture("samples/dark_environment_test.mp4")
  ```
- Para usar a webcam, troque para:
    ```python
    cap = cv2.VideoCapture(0)
    ```
