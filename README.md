##Considerações importantes

Os arquivos de áudio usam 16 bits por amostra, e 8000 amostras por segundo.
Isso significa que cada amostra é um valor numérico entre -32768 até 32767.

Cada um desses valores indica a amplitude de uma determinada onda sonora capturada
naquele instante.

Explicando de maneira bem simplifica, análise de Fourier decompõe a onda original
numa somatória de senoides de frequências e amplitudes diferentes.

##Conversão dos wavs num formato adequado
Instale o ffmpeg (mac users: `brew install ffmpeg`).

Navegue até a pasta com os `.wav` e execute no terminal:
```bash
mkdir converted

for file in ./*
do
  ffmpeg -i "$file" converted/"$file"
done
```

##Bibliotecas necessárias
Obtenha o pip, e execute:
```
pip install numpy
pip install scipy
```

##Captura em janelas de 20ms
Se temos 8000 amostras por segundo, cada amostra é um passo de 1/8000 segundos.

Para capturar 20ms, precisamos de 0.02 / (1/8000) = 160 amostras por janela.

Cada intervalo de 20ms terá sua própria análise de fourier.


##Normalização
A conversão será feita da sequinte maneira:
```
Seja f um vetor onde cada índice representa uma frequência e cada valor representa
a magnitude daquela frequência medida em dbs de um amostra de 20ms

f_novo[x] = f[x] * 255 / 32767
```
