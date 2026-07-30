import datetime

# Cria o conteúdo básico do seu XML de EPG
conteudo_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<tv generator-info-name="AutomacaoEPGGlobo">

  <channel id="GloboSP">
    <display-name lang="pt">TV Globo São Paulo</display-name>
  </channel>

  <programme start="{datetime.datetime.now().strftime('%Y%m%d')}000000 -0300" stop="{datetime.datetime.now().strftime('%Y%m%d')}235959 -0300" channel="GloboSP">
    <title lang="pt">Programação Automatizada Globo</title>
    <desc lang="pt">Gerado automaticamente pelo robô do GitHub.</desc>
  </programme>

</tv>
"""

# Salva esse texto dentro do arquivo globo.xml
with open("globo.xml", "w", encoding="utf-8") as f:
    f.write(conteudo_xml)

print("Arquivo globo.xml gerado com sucesso!")
