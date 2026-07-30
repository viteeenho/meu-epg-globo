import datetime

data_hoje = datetime.datetime.now().strftime('%Y%m%d')

# Estrutura XML contendo todas as praças definitivas mapeadas
conteudo_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<tv generator-info-name="AutomacaoEPGGlobo">

  <channel id="GloboSP"><display-name lang="pt">TV Globo São Paulo</display-name></channel>
  <channel id="GloboRJ"><display-name lang="pt">TV Globo Rio de Janeiro</display-name></channel>
  <channel id="GloboBrasilia"><display-name lang="pt">TV Globo Brasília</display-name></channel>
  <channel id="GloboMinas"><display-name lang="pt">TV Globo Minas</display-name></channel>
  <channel id="TvTemBauru"><display-name lang="pt">TV TEM Bauru e Marília</display-name></channel>
  <channel id="TvTemSorocaba"><display-name lang="pt">TV TEM Sorocaba</display-name></channel>
  <channel id="TvTemRioPreto"><display-name lang="pt">TV TEM São José do Rio Preto e Olímpia</display-name></channel>
  <channel id="TvTemItapetininga"><display-name lang="pt">TV TEM Itapetininga</display-name></channel>
  <channel id="TvTribunaSantos"><display-name lang="pt">TV Tribuna (Santos)</display-name></channel>
  <channel id="TvVanguardaVale"><display-name lang="pt">TV Vanguarda (Vale)</display-name></channel>
  <channel id="GloboCeara"><display-name lang="pt">TV Verdes Mares (Ceará)</display-name></channel>
  <channel id="TvAnhangueraGoias"><display-name lang="pt">TV Anhanguera (Goiás)</display-name></channel>
  <channel id="GloboMS"><display-name lang="pt">TV Morena (MS)</display-name></channel>
  <channel id="RedeAmazonicaManaus"><display-name lang="pt">Rede Amazônica (Manaus)</display-name></channel>
  <channel id="GlobaBahia"><display-name lang="pt">TV Bahia</display-name></channel>

  <programme start="{data_hoje}000000 -0300" stop="{data_hoje}235959 -0300" channel="GloboSP">
    <title lang="pt">Atualização Automática Diária</title>
    <desc lang="pt">Grade sincronizada pelo robô.</desc>
  </programme>

</tv>
"""

# Salva as alterações no arquivo globo.xml
with open("globo.xml", "w", encoding="utf-8") as f:
    f.write(conteudo_xml)

print("Todas as praças definitivas foram atualizadas com sucesso no XML!")
