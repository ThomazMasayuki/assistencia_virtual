# Assistente Virtual por Voz com PLN — Python

## Visão Geral

Este projeto implementa um **assistente virtual por voz** desenvolvido em Python, capaz de interpretar comandos falados, processá-los utilizando técnicas de **Processamento de Linguagem Natural (PLN)** e executar ações automatizadas no sistema.

A solução foi projetada com foco em arquitetura modular, permitindo expansão de funcionalidades, integração com APIs externas e adaptação para diferentes cenários de automação e interação homem-máquina.

---

## Objetivo

Construir um sistema interativo que permita comunicação natural com o usuário por meio de voz, contemplando:

* Conversão de fala em texto *(Speech-to-Text)*
* Conversão de texto em fala *(Text-to-Speech)*
* Interpretação semântica de comandos
* Execução automatizada de tarefas

---

## Funcionalidades Implementadas

### Interação por Voz

* Captura de áudio em tempo real
* Reconhecimento de fala
* Respostas audíveis geradas dinamicamente

### Interpretação de Linguagem Natural

* Identificação de intenções do usuário
* Extração de palavras-chave
* Classificação de comandos

### Automação de Ações

O assistente pode executar comandos como:

* Abrir páginas web (Google, YouTube etc.)
* Pesquisar informações
* Consultar conteúdos via API
* Enviar e-mails personalizados
* Executar rotinas automatizadas
* Encerrar execução por comando de voz

---

## Tecnologias Utilizadas

* **Python 3**
* **SpeechRecognition** → reconhecimento de voz
* **PyAudio** → captura de áudio
* **pyttsx3** → síntese de fala
* **Wikipedia API** → consulta de informações
* **Webbrowser** → automações web

---

## Arquitetura do Sistema

O projeto foi estruturado em módulos independentes:

1. **Entrada de Voz** → captação e conversão STT
2. **Processamento NLP** → interpretação do comando
3. **Motor de Decisão** → identificação da ação
4. **Executor de Tarefas** → execução da rotina
5. **Resposta** → geração de áudio TTS

---

## Conceitos Aplicados

* Processamento de Linguagem Natural
* Reconhecimento de fala
* Síntese de voz
* Automação de tarefas
* Sistemas interativos
* Interfaces naturais
* Arquitetura modular

---

## Possibilidades de Expansão

O sistema foi projetado para permitir evolução futura, como:

* Integração com APIs externas
* Comandos personalizados
* Aprendizado contínuo de intenções
* Integração com IoT
* Deploy como serviço local ou remoto

---

## Conclusão

Este projeto demonstra, de forma prática, a aplicação de técnicas de PLN, reconhecimento de voz e automação para construção de interfaces naturais entre humanos e computadores. A implementação evidencia domínio de conceitos de inteligência artificial aplicada, engenharia de software e integração de serviços, consolidando uma base sólida para desenvolvimento de assistentes virtuais mais avançados.
