# 🤖 Trabalho - Robô Aspirador Reativo Simples

## 👥 Equipe
- Vitor Hugo Oliveira Paloco  

## 📌 Descrição

Este projeto consiste na implementação de um **robô aspirador reativo simples** em um ambiente linear representado por uma lista de 10 posições.

O ambiente pode conter:
- `"~"` → sujeira  
- `"R"` → robô  
- `" "` → espaço vazio  

O robô inicia em uma posição aleatória, enquanto a sujeira é distribuída aleatoriamente entre 2 e 6 posições do ambiente.

## ⚙️ Funcionamento

O robô segue a lógica de um **Agente Reativo Simples**, ou seja:

- Ele observa **apenas a posição atual**
- Se houver sujeira → **limpa**
- Caso contrário → **move-se aleatoriamente**:
  - Esquerda ou direita
  - Respeitando os limites do vetor

A cada ação:
- O estado do ambiente é exibido no terminal
- Há uma pausa de 1 segundo entre as ações

## ▶️ Execução

Para executar o projeto:

```bash
python nome_do_arquivo.py