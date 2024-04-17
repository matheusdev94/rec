# Gravador de Vídeo com Carimbo de Data e Hora

Este é um script em Python para capturar vídeo da câmera e gravá-lo em um arquivo AVI com um carimbo de data e hora sobreposto em cada quadro.

## Pré-requisitos

Certifique-se de ter o OpenCV instalado:

```bash
pip install -r reuquirements.txt
```

## Utilização

Execute o script.
Pressione 'q' para parar a gravação e fechar a janela.

## Como funciona

Inicializa a captura de vídeo da primeira câmera disponível.
Define as configurações de captura de vídeo (largura e altura do quadro).
Cria um objeto VideoWriter para gravar o vídeo em um arquivo AVI.
Inicia um loop de captura e gravação de vídeo:
Captura um quadro da câmera.
Inverte o quadro horizontalmente.
Adiciona um carimbo de data e hora sobreposto no quadro.
Grava o quadro no arquivo de vídeo.
Exibe o quadro na janela.
Verifica se a tecla 'q' foi pressionada para sair do loop.
Libera os objetos de captura e gravação de vídeo.
Fecha todas as janelas.

## Autor

- [@matheusdev94](https://github.com/matheusdev94)
