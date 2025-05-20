# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

---

# 🌾 PROJETO FASE 6 – O COMEÇO DA REDE NEURAL - FarmTech Solutions

## Nome do projeto
Fase 6 - Cap 1 - FarmTech, Despertar da rede neural

## Nome do grupo
Grupo 31

## 👨‍🎓 Integrantes:
- [Ana Beatriz Duarte Domingues](https://www.linkedin.com/in/)
- [Junior Rodrigues da Silva](https://www.linkedin.com/in/jrsilva051/)
- [Carlos Emilio Castillo Estrada](https://www.linkedin.com/in/)

## 👩‍🏫 Professores:
### Tutor(a)
- [Lucas Gomes Moreira](https://www.linkedin.com/company/inova-fusca)
### Coordenador(a)
- [André Godoi Chiovato](https://www.linkedin.com/company/inova-fusca)

---

## 📚 Estrutura de Pastas

```
bash
FarmTech_Vision/
├── assets/
│   ├── logo-fiap.png/
├── data/
│   ├── train/
│   │    ├── arquivos de texto...
│   │    └── imagens...
│   ├── val/
│   │    ├── arquivos de texto...
│   │    └── imagens...
│   └── test/
│   │    ├── arquivos de texto...
│   │    └── imagens...
│   └── data.yaml
├── JuniorSilva559451_fase6.ipynb
├── JuniorSilva559451_fase6_entrega2.ipynb
├── LinkApresentacao.txt
└── README.md
```

---
## ✅ Entrega 1
### 📝 Descrição

O projeto desenvolvido simula a implantação de um sistema de visão computacional utilizando YOLOv5, para a identificação de dois tipos de objetos distintos: **alface** e **maçã**.

O objetivo é demonstrar ao cliente da FarmTech Solutions o funcionamento, a acurácia e o potencial da tecnologia de visão computacional aplicada.

- Foram utilizadas 80 imagens divididas igualmente entre os dois objetos.
- As imagens foram rotuladas usando a plataforma Make Sense IA.
- A divisão dos dados foi feita em 32 imagens para treino, 4 para validação e 4 para teste por classe.
- As imagens e os arquivos de texto utilizados no treinamento foram salvos no Google Drive.
- Três treinos foram realizados com quantidades diferentes de épocas (30, 45 e 60), analisando os impactos nos resultados.


#### 📌 Acesse o Notebook no Google Colab:  
[📖 Abrir no Google Colab](https://colab.research.google.com/github/Jr-RS/fase6_cap1_FarmTech/blob/main/JuniorSilva559451_fase6.ipynb)


### 🎥 Vídeo Demonstrativo
- O vídeo demonstrativo da entrega 1 do projeto está disponível no YouTube:
[Assista aqui](https://youtu.be/kiQd7i4DL4E) 

---

---
## ✅ Entrega 2
### 📝 Descrição

Nesta segunda etapa, realizamos uma comparação entre diferentes abordagens de visão computacional para o problema de identificação de objetos (alface e maçã), visando encontrar a solução mais adequada para o cliente FarmTech Solutions.

Foram aplicadas as seguintes estratégias:
- **YOLO Customizada**: Utilizando o modelo treinado na Entrega 1, adaptado ao nosso conjunto de dados.
- **YOLO Padrão (pré-treinada no COCO)**: Aplicação do modelo YOLOv5s pré-treinado, sem ajustes específicos para a base da FarmTech.
- **CNN Desenvolvida do Zero**: Construção de uma rede convolucional simples para classificar as imagens em duas categorias.

Cada abordagem foi avaliada considerando:
- Facilidade de uso e integração;
- Precisão do modelo;
- Tempo de treinamento;
- Tempo de inferência.

Foi constatado que a **YOLO customizada** apresentou o melhor equilíbrio entre precisão, velocidade e aplicabilidade ao cenário da FarmTech Solutions.

#### 📌 Acesse o Notebook da Entrega 2 no Google Colab:
[📖 Abrir no Google Colab](https://colab.research.google.com/github/Jr-RS/fase6_cap1_FarmTech/blob/main/JuniorSilva559451_fase6_entrega2.ipynb)

---

## 📚 Histórico de Lançamentos

* 0.1.0 - 24/04/2025
    * Primeira versão do projeto de deep learning com yolo.

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
