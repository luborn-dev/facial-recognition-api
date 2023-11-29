# API - Projeto Integrador VI

Este é um projeto acadêmico dedicado ao desenvolvimento de uma API em Python que tem como objetivo criar uma interface entre um usuário e um modelo de IA voltado para o Reconhecimento Facial.

O principal propósito desta API é oferecer suporte a aplicações web e móveis, permitindo a integração do reconhecimento facial como parte de suas funcionalidades. Esta documentação será atualizada à medida que o projeto avançar.

## Instalação

Instale todas as depêndencias necessárias

```bash
  cd <diretorio_do_projeto>

  pip install -r requirements.txt
```

## Rodando localmente

Crie uma pasta de uploads (opcional)

```bash
  mkdir uploads/
```

Inicie o servidor

- Opcional: Se desejar, mude a porta do servidor dentro do arquivo `init.sh`.

```bash
  sh init.sh
```

## Documentação da API

#### Processa a imagem enviada

```http
  POST /api/processar
```

| Parâmetro | Tipo   | Descrição                                  |
| :-------- | :----- | :----------------------------------------- |
| `imagem`  | `file` | **Obrigatório**: A imagem a ser processada |

A imagem deve ser enviada através de um objeto FormData.

Exemplo de uso em JavaScript:

```javascript
const formData = new FormData();
formData.append("file", selectedFile);
await fetch("<seu-endpoint>/api/processar", {
  method: "POST",
  body: formData,
});
```

#### Retorna o resultado da predição.

facial-recognition-api
├─ .gitignore
├─ README.md
├─ app
│ ├─ **init**.py
│ ├─ model
│ │ ├─ **init**.py
│ │ ├─ modelo_cnn_lucas100.h5
│ │ └─ modelo_cnn_lucas1000.h5
│ ├─ routers
│ │ ├─ **init**.py
│ │ └─ processar.py
│ └─ services
│ ├─ **init**.py
│ ├─ pre_processamento.py
│ └─ processar_modelo.py
├─ init.sh
├─ requirements.txt
└─ server.py
