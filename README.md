# OPS LABS
## Capturador de presença nas seções

Script feito à pedido do Lucio para captura rápida da assiduidade dos políticos nas sessões. O objetivo é coletar de todos os politicos dado intervalo de tempo.

O script faz a chamada para o site coletando as presenças nas datas de acordo com a matrícula do político.

## Links Utilizados
* [http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/sessoesreunioes-2/listarpresencasparlamentar]() - Informações de como obter o dado
* [http://www.camara.gov.br/SitCamaraWS/sessoesreunioes.asmx/ListarPresencasParlamentar?dataIni=01/02/2015&dataFim=31/07/2015&numMatriculaParlamentar=125]() - Exemplo de dado de sessão

## Instalação
Esse script foi feito em Python 2.7. Também ele usa o virtualenv, pip e o wget (pra baixar o xml inicial, pra não ter que ficar baixando sempre)

Pra você fazê-lo funcionar faça o seguinte;

    $ virtualenv env;
    $ source env/bin/activate;
    $ pip install -r requirements.pip;


Para Baixar o arquivo que é utilizado no processo faça:

    $ curl http://www.camara.gov.br/SitCamaraWS/deputados.asmx/ObterDeputados > deputados.xml

Para executar o script basta fazer o seguinte:

    $ python fetcher.py

