# Próximo assignment da Dooolha.

Comunicação é algo necessário para o ser humano e para que esta seja efetiva são necessários um meio de comunicação, um protocolo e, claro, a mensagem.

Em software não é diferente, softwares precisam se comunicar para buscar / enviar informações. Um exemplo disso foi o primeiro assignment relacionado a obtenção de informações de previsão de tempo.

O meio de comunicação foi a internet, o protocolo HTTP (o mesmo utilizado quando você acessa qualquer página no browser) e a mensagem foi o forecast em JSON.

Para essa tarefa a ideia é **fazer mais uma iteração na biblioteca de contagem de palavras que vc fez**, mas a ideia agora é tornar isso disponível para pessoinhas de forma distribuida, ou seja, através de um serviço. Para tal, vamos fazer igual o openweather. Você já utilizou a biblioteca 'requests' para servir de cliente HTTP e pegar a informação do tempo, **agora a ideia é implementar o outro lado, o servidor para contagem de palavras.**

Existem várias bibliotecas/frameworks em python para esta finalidade e a ideia não é vc implementar o protocolo HTTP pq já ta pronto a ideia é implementar o serviço.

A proposta é ter uma URL:

`http://localhost:<porta>/contagem` em que você envia o texto e essa api retorna a lista de palavras e a contagem, portanto em termos de HTTP, seria:

```http
POST /contagem HTTP/1.1
Accept: application/json
Content-Type: application/json

{
	"texto": "<seu_texto_aqui>"
}
```

E a resposta é:

```json
{
	"word_count": {
		"palavra1": 3,
		"palavra2": 1
	}
}
```

A parte sobre HTTP deve ter parecido grego, mas é simples, tem uma introdução aqui:

- https://www.httpwatch.com/httpgallery/introduction/

Esse tipo de API é comunmente chamada de api **REST**, que nada mais é que uma api, ou seja, algo que as pessoas podem chamar para obter informações e está sobre HTTP.

Sobre os frameworks para desenvolver servidores, existe uma lista com alguns abaixo. Minha sugestão é utilizar um que seja pequeno (micro-framework) porque você não vai precisar de um monte de abstrações que por exemplo o Django (o mais conhecido) tem:

- https://stackify.com/python-frameworks/

Boa diversão!