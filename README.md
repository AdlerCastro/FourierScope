# 🎧 Processamento de Sinais usando Fourier – Engenharia de Computação

Este projeto tem como objetivo aplicar conceitos de **Sinais e Sistemas**, utilizando ferramentas computacionais para analisar sinais no domínio do tempo e da frequência, com a aplicação prática da **Transformada de Fourier**, **projeto de filtros digitais** e **reconstrução de sinais filtrados**.

---

## 🎯 Objetivos do Projeto

- Aplicar a **Transformada de Fourier** na análise espectral de sinais reais.
- Projetar e aplicar filtros digitais: **Passa-Baixa**, **Passa-Banda** e **Passa-Alta**.
- Compreender o **teorema da amostragem de Nyquist-Shannon** e seus efeitos no espectro.
- Interpretar os sinais no domínio do tempo e da frequência, antes e após o processo de filtragem.
- Desenvolver habilidades com ferramentas computacionais em Python para o processamento digital de sinais (DSP).

---

## 📦 Estrutura do Projeto

```
/Projeto_Fourier/
│
├── audio.wav                  # Áudio original em formato .wav (mono)
├── processamento_fourier.py  # Script principal do projeto
├── saida_passa_baixa.wav     # Resultado após filtro Passa-Baixa
├── saida_passa_alta.wav      # Resultado após filtro Passa-Alta
├── saida_passa_banda.wav     # Resultado após filtro Passa-Banda
├── requirements.txt          # Dependências do projeto
└── README.md                 # Instruções detalhadas de execução e análise
```

---

## 🛠️ Tecnologias e Bibliotecas

- `Python 3.8+`
- `numpy`
- `scipy`
- `matplotlib`
- `librosa`
- `soundfile`

---

## 🚀 Como Executar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Adicione o arquivo de áudio

- Coloque um arquivo `.wav` **mono** na raiz do projeto com o nome `audio.wav`.
- O áudio será usado como base para todo o processamento.

### 3. Execute o script principal

```bash
python processamento_fourier.py
```

> O script irá:
> - Ler o áudio;
> - Plotar o sinal no tempo e no espectro de frequência;
> - Aplicar três filtros digitais (PB, PA, PBanda);
> - Plotar os resultados;
> - Exportar os sinais resultantes em arquivos `.wav`.

---

## 🧠 Lógica do Processamento

Para cada filtro, o seguinte pipeline é executado:

```
Sinal Original → Transformada de Fourier (FFT) → Aplicação do Filtro Digital 
→ Transformada Inversa de Fourier (IFFT) → Sinal Reconstruído
```

### 🧹 Filtros utilizados

| Tipo         | Frequências de Corte        | Objetivo                                                             |
|--------------|-----------------------------|----------------------------------------------------------------------|
| Passa-Baixa  | até 1000 Hz                 | Preserva graves e elimina agudos                                     |
| Passa-Alta   | a partir de 3000 Hz         | Preserva agudos e elimina componentes graves                         |
| Passa-Banda  | entre 1000 Hz e 3000 Hz     | Isola região média, útil para análise de fala e inteligibilidade     |

---

## 📊 Resultados Gerados

- Gráficos do sinal no **tempo** (amplitude vs. tempo);
- Gráficos do **espectro de frequência** (magnitude vs. Hz);
- Três arquivos `.wav` com os sinais processados:
  - `saida_passa_baixa.wav`
  - `saida_passa_alta.wav`
  - `saida_passa_banda.wav`

---

## 🧪 Análises Esperadas (para o relatório)

- Efeitos dos filtros no conteúdo do sinal (visualmente e sonoramente);
- Comparação dos espectros antes/depois;
- Relação com o teorema da amostragem;
- Implicações práticas em áudio: supressão de ruído, isolamento de frequências, etc.

---

## 📋 Requisitos de Entrega

Conforme solicitado pelo professor:

1. ✅ **Código-fonte** com comentários explicativos;
2. ✅ **Documento de execução** (este README.md);
3. ❌ **Documento com análise teórica e prática** (a ser entregue à parte);
4. ❌ **Vídeo explicativo** com execução e análise (a ser gravado com base neste script).

---

## ⚠️ Observações Finais

- O uso de IA foi aplicado **exclusivamente na estruturação do projeto e documentação técnica**, como forma de **aprimorar clareza e organização**.
- A filtragem foi implementada com base em **filtros Butterworth** de 5ª ordem usando `scipy.signal`.

---

## 👨‍🔬 Autores

Alunos: Adler Castro, Edgar Klewert, Luiz Neto
Engenharia de Computação – EC5MA
2º Bimestre
Data de Entrega: 09/06/2025