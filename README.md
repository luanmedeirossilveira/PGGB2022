# PGGB2022
``` Trabalho Grau B - Unisinos 2022/2 ```

Luan Medeiros Silveira

CÓDIGO DO TRABALHO EM ```main.py```

Adicionando filtros com PYTHON - OpenCV

## Documentação
- [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)


## Filtros Utilizados

- Grayscale
- Binarização
- Binarização Dark
- Binarização Invert
- Blur 5x5
- Blur 15x15
- Gaussian 5x5
- Gaussian 15x15
- Median 5x5
- Median 15x15
- Bilateral 5x5
- Bilateral 15x15
- Canny 
- Sobel
- Laplacian
- Erosion
- Dilation
- Opening
- Closing
- Morphological Gradient
- Top Hat
- Black Hat

## Trabalho

Objetivo: Implementar um protótipo de aplicativo de edição de imagens (inspirado nos stories
do Instagram). Para tal, é necessário:

• Input:
[x] Permitir ao usuário escolher a foto para carregar (pode ser via console)
[x] Permitir fazer a captura de vídeo pela webcam

• Execução: dois tipos de operações serão possíveis:
[X] Colar stickers – a partir de uma base de no mínimo 5 stickers diferentes (sprites
com transparência), selecionar pela interface (clique do mouse) e posicioná-los
acima da foto (o posicionamento pode ser feito via mouse ou teclado)

[X] Aplicar filtro – a partir de uma base de no mínimo 10 efeitos diferentes,
selecionar pela interface (clique do mouse) e com isso a foto será alterada de
acordo com o filtro.

• Output: 
[X] salvar a foto alterada. No caso do vídeo, salvar um frame.

# Execução
  
  ``` python3 main.py stadium.jpg "False" ```

  ``` python3 main.py stadium.jpg "True" ```

  ``` python3 main.py "True" ```

  ``` python3 main.py "False" ```
