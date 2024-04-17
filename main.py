import cv2
from datetime import datetime

# Inicializar a captura de vídeo da primeira câmera disponível
cap = cv2.VideoCapture(0)

# Verificar se a captura foi aberta com sucesso
if not cap.isOpened():
    print("Erro: Não foi possível abrir a câmera.")
    exit()

# Obter as configurações de captura de vídeo (largura e altura do quadro)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Definir o codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Obter a data e hora do início da gravação
start_time = datetime.now().strftime("%d-%m-%Y %Hh-%Mm")

# Criar o objeto VideoWriter com o nome do arquivo contendo a data e hora do início da gravação
out = cv2.VideoWriter(f'{start_time}.avi', fourcc, 20.0, (frame_width, frame_height))

# Loop de captura e gravação de vídeo
while True:
    ret, frame = cap.read()

    # Verificar se o quadro foi lido corretamente
    if not ret:
        print("Erro: Não foi possível capturar o quadro.")
        break

    # Inverter a imagem horizontalmente
    frame = cv2.flip(frame, 1)

    # Obter a data e hora atual
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Adicionar a data e hora como uma sobreposição no quadro
    cv2.putText(frame, current_time, (frame_width - 200, frame_height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    # Gravar o quadro no arquivo de vídeo
    out.write(frame)

    # Exibir o quadro na janela
    cv2.imshow('Camera', frame)

    # Verificar pressionamento da tecla 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os objetos de captura e gravação de vídeo
cap.release()
out.release()

# Fechar todas as janelas
cv2.destroyAllWindows()
