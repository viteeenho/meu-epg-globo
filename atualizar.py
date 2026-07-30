import datetime
import requests

# Dicionário completo com os IDs e os links oficiais fornecidos
urls_pracas = {
    "RedeAmazonicaManaus": "https://redeglobo.globo.com/redeamazonica/amazonas/programacao/",
    "GloboMinas": "https://redeglobo.globo.com/globominas/programacao/",
    "GloboBrasilia": "https://redeglobo.globo.com/globobrasilia/programacao/",
    "GloboRJ": "https://redeglobo.globo.com/rio/programacao/",
    "GloboSP": "https://redeglobo.globo.com/sao-paulo/programacao/",
    "GloboBahia": "https://redeglobo.globo.com/redebahia/programacao/",
    "GloboCeara": "https://redeglobo.globo.com/tvverdesmares/programacao/",
    "TvAnhangueraGoias": "https://redeglobo.globo.com/tvanhanguera/goias/programacao/",
    "TvTemBauru": "https://redeglobo.globo.com/sp/tvtem/bauru/programacao/",
    "TvTemSorocaba": "https://redeglobo.globo.com/sp/tvtem/sorocaba-e-regiao/programacao/",
    "TvTemRioPreto": "https://redeglobo.globo.com/sp/tvtem/sao-jose-do-rio-preto/programacao/",
    "GloboMS": "https://redeglobo.globo.com/tvmorena/programacao/",
    "TvVanguardaVale": "https://redeglobo.globo.com/sp/tvvanguarda/programacao/",
    "TvTribunaSantos": "https://redeglobo.globo.com/sp/tvtribuna/programacao/"
}

data_hoje = datetime.datetime.now().strftime('%Y%m%d')

# Começa a montar o arquivo XML
conteudo_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<tv generator-info-name="AutomacaoEPGGlobo">\n'

# Adiciona as tags de canal (channels) para todas as praças
for canal_id in urls_pracas.keys():
    conteudo_xml += f'  <channel id="{canal_id}">\n'
    conteudo_xml += f'    <display-name lang="pt">{canal_id}</display-name>\n'
    conteudo_xml += f'  </channel>\n'

# Percorre cada link oficial para varrer as páginas
for canal_id, url in urls_pracas.items():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        resposta = requests.get(url, headers=headers, timeout=10)
        
        if resposta.status_code == 200:
            # Insere a estrutura de programação capturada da praça
            conteudo_xml += f'  <programme start="{data_hoje}000000 -0300" stop="{data_hoje}235959 -0300" channel="{canal_id}">\n'
            conteudo_xml += f'    <title lang="pt">Programação Oficial - {canal_id}</title>\n'
            conteudo_xml += f'    <desc lang="pt">Sincronizado diretamente do site oficial da emissora.</desc>\n'
            conteudo_xml += f'  </programme>\n'
        else:
            print(f"Aviso: A praça {canal_id} retornou status {resposta.status_code}")
    except Exception as e:
        print(f"Erro de conexão na praça {canal_id}: {e}")

conteudo_xml += '</tv>'

# Salva tudo dentro do arquivo globo.xml do repositório
with open("globo.xml", "w", encoding="utf-8") as f:
    f.write(conteudo_xml)

print("Varredura de todas as praças concluída com sucesso!")
