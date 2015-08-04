# -*- encoding: utf8 -*-
import xmltodict
import urllib
import StringIO, csv, json

def get_politician_presence(politician_id, date_from, date_to):
    url_handler = urllib.urlopen('http://www.camara.gov.br/SitCamaraWS/sessoesreunioes.asmx/'
                                 'ListarPresencasParlamentar?'
                                 'dataIni=%s&dataFim=%s&numMatriculaParlamentar=%s' % (date_from,
                                                                                       date_to,
                                                                                       politician_id))

    politician_raw_data = url_handler.read()
    politician_raw_data = politician_raw_data.replace('\\x', '\\u00')  #Fixing encoding issues
    url_handler.close()

    politician_presence =  xmltodict.parse(politician_raw_data)
    politician_presence = politician_presence['parlamentar']

    politician_presence_formatted = {
        'nome': politician_presence['nomeParlamentar'],
        'partido': politician_presence['siglaPartido'],
        'presenca': []
    }

    for presenca in politician_presence['diasDeSessoes2']['dia']:
        evento = {
            'data': presenca['data'],
            'is_presente': True if presenca['frequencianoDia'] == u'Presença' else False,
            'frequencia_no_dia': presenca['frequencianoDia'],
            'justificativa': presenca['justificativa'],
            'qtde_sessoes': presenca['qtdeSessoes']
        }
        politician_presence_formatted['presenca'].append(evento)

    return politician_presence_formatted

def process_csv_presence(csv_writter, politician):

    for evento in politician['presenca']:
        fields = [
            politician['nome'],
            politician['partido'],
            evento['data'],
            'SIM' if evento['is_presente'] == True else 'NAO',
            evento['frequencia_no_dia'],
            evento['justificativa'] if evento['justificativa'] else '',
            int(evento['qtde_sessoes'])
        ]

        csv_writter.writerow([unicode(s).encode("iso-8859-1") for s in fields])



if __name__ == '__main__':

    print "OPS Crawler - Deputados presença"

    report_date_from='01/02/2015'
    report_date_to='31/07/2015'

    file_handler = open('presenca.csv', 'w')
    cw = csv.writer(file_handler, quotechar='"', quoting=csv.QUOTE_ALL, dialect=csv.excel)

    with open('deputados.xml','r') as raw_file:
        xml_file = (raw_file.read()).replace('\\x', '\\u00')  #Encoding stuff

    if xml_file:
        parsed_file = xmltodict.parse(xml_file, process_namespaces=True)

        deputados = parsed_file['deputados']['deputado']
        size_deputados = len(deputados)

        treated_politicians = []
        for index, deputado in enumerate(deputados):
            print "Baixando [%(index)s de %(total)s] - %(nome)s" % {'index': index+1,
                                                                    'total': size_deputados,
                                                                    'nome': deputado['nome']}

            process_csv_presence(csv_writter=cw, politician=get_politician_presence(
                politician_id=deputado['matricula'], date_from=report_date_from, date_to=report_date_to))

            print "OK"

        print file_handler.close()
        print 'Finalizado!'
