📘 Sprint 24 — Início da Fase 7: APIs e Automação
🎯 Objetivo

Iniciar a Fase 7 do roadmap, aprendendo o conceito de API, autenticação, variáveis de ambiente seguras, e navegação em JSON aninhado — usando primeiro uma API pública simples, depois uma API de futebol real (API Futebol), incluindo a resolução de um problema real de configuração de plano.

🌐 Conceito de API e biblioteca requests
import requests

resposta = requests.get("https://countries.dev/alpha/BR")

print(resposta.status_code)
print(resposta.json())

requests.get(url) faz um pedido HTTP do tipo GET (buscar informação, sem alterar nada no servidor) — o mesmo tipo de pedido que um navegador faz ao visitar um site. resposta.status_code informa se o pedido deu certo (200 = sucesso; outros códigos como 404 e 401 têm significados padronizados). resposta.json() converte a resposta (formato JSON, parecido com dicionário) em estrutura que o Python já manipula nativamente.

Analogia (Excel): uma API é como um "Power Query buscando dados de uma fonte externa", só que especificado em código em vez de configurado visualmente.

📌 Navegação em JSON aninhado

APIs reais frequentemente devolvem estruturas aninhadas (dicionários dentro de dicionários, dentro de listas). Prática de navegação:

dados["currencies"][0]["code"]

Ao explorar uma API de futebol real, foi necessário navegar por várias camadas (dados["partidas"]["fase-unica"]["1a-rodada"][0]) até chegar às partidas de fato — cada camada intermediária representando fase, rodada, etc. type() foi usado como ferramenta de diagnóstico para identificar se uma variável era lista ou dicionário antes de tentar acessá-la, evitando tentativa e erro.

🔐 Autenticação com API Key e variáveis de ambiente

APIs que exigem chave usam autenticação via header:

headers = {
    "Authorization": f"Bearer {chave_api}"
}

resposta = requests.get(url, headers=headers)

Bearer é uma palavra-chave padrão do protocolo de autenticação (não específica dessa API).

Boa prática de segurança — nunca escrever a chave diretamente no código:

1. Criar um arquivo .env na raiz do projeto (arquivo de texto puro, nome sem prefixo, só a extensão), contendo: API_FUTEBOL_KEY=sua_chave_aqui
2. Adicionar .env ao .gitignore, garantindo que nunca seja commitado
3. Instalar python-dotenv (pip install python-dotenv) e carregar a chave em código:
import os
from dotenv import load_dotenv

load_dotenv()
chave_api = os.getenv("API_FUTEBOL_KEY")

Justificativa: se uma chave vazar (por exemplo, publicada sem querer num repositório público), qualquer pessoa pode usá-la, consumindo a cota do titular ou acessando dados indevidamente.

📌 Requisições — o que contam e por que há limite

Cada chamada requests.get(...) consome 1 requisição da cota do plano. Planos gratuitos de APIs de futebol tipicamente oferecem entre 100 requisições/dia (plano gratuito da API Futebol, restrito ao Brasileirão Série B) até limites maiores em planos pagos. O limite existe porque cada requisição gera processamento real do lado do servidor, com custo de infraestrutura para o provedor.

⚠️ Ambiente de Teste vs. Produção

APIs comerciais frequentemente oferecem uma chave de teste (prefixo test_), que devolve sempre os mesmos dados de exemplo fictícios, independente dos parâmetros enviados na requisição — usada para validar a integração sem consumir dados reais ou cota de produção. Identificado na prática: uma requisição para a partida 23346 devolveu, com a chave de teste, um exemplo fixo (partida 27650, jogo fictício futuro), confirmando esse comportamento. A chave de produção (prefixo live_) devolve dados reais, mas está sujeita ao plano contratado.

⚠️ Erro resolvido: plano não ativado

Ao gerar uma chave de produção diretamente (sem completar o fluxo de checkout de plano — que envolve múltiplas etapas: Plano, Campeonatos, Requisições, Adicionais, Revisão), a API retornou 401 mesmo em endpoints que deveriam ser abertos (ex: listagem geral de campeonatos). Causa identificada: o plano não estava de fato ativo na conta, apesar da chave existir. Resolvido completando o fluxo de ativação do Plano Free (restrito ao Campeonato Brasileiro Série B, campeonato_id 14) até o final.

📊 Estrutura de dados de uma API de futebol real

Explorada a estrutura completa de uma partida (endpoint /v1/partidas/{id}), muito mais rica que o CSV histórico usado no Athena até aqui: estatisticas (posse de bola, passes, finalizações, desarmes por time), escalacoes (titulares, reservas, técnico, posição), gols (autor, minuto exato, pênalti/gol contra), substituicoes e cartoes detalhados por jogador e minuto. Identificado como recurso relevante para ideias futuras de análise de jogador individual (ex: desarmes de um jogador específico).

💬 Curiosidade discutida: como uma API de futebol obtém seus dados

Coleta por analistas humanos assistindo aos jogos ao vivo, digitando eventos em tempo real; parcerias oficiais com ligas/clubes; tecnologia de rastreamento (câmeras/sensores) em ligas de elite para métricas avançadas (ex: xG); tudo armazenado em banco de dados e disponibilizado via API — mesma lógica de banco.py do Athena (Sprint 23), em escala maior. Modelo de negócio: fornecedor de dados cobra do desenvolvedor (ex: casas de aposta como o Packball mencionado pelo usuário), que cobra do usuário final.

📌 Decisão de escopo

Definido não criar ainda um api.py dedicado (paralelo ao banco.py) para encapsular as chamadas à API Futebol — decisão adiada para quando o dashboard final (Fase 10) precisar de fato consumir dados atualizados, evitando estrutura sem uso imediato.

📝 Esclarecimento importante sobre custo e escopo do projeto

O núcleo do Athena (análise histórica do Brasileirão Série A, 2003-2024) não depende da API e permanece gratuito — o CSV já foi baixado e processado integralmente. A necessidade de pagar por acesso a API só se aplicaria a dados ao vivo/atualizados, ou a dados detalhados de ligas menos populares (ex: análise individual de um jogador de liga dinamarquesa, ideia registrada anteriormente). Alternativa sem custo de API para esse tipo de análise: sites como FBref publicam estatísticas detalhadas por jogador gratuitamente na própria página, acessíveis via web scraping (técnica de extração de dados direto do HTML) — abordagem mais avançada, cabível também na Fase 7, a ser explorada quando fizer sentido.

📝 Anotações da Athena

Esta sprint cobriu o ciclo completo de trabalho com APIs: desde uma chamada simples sem autenticação, passando por autenticação com chave, gerenciamento seguro de credenciais, navegação em estruturas de dados profundamente aninhadas, até a resolução de um problema real de configuração de conta (plano não ativado). Também ficou estabelecido um entendimento importante sobre a relação entre custo e escopo do projeto: o valor histórico do Athena já está garantido e gratuito, e expansões futuras (dados ao vivo, ligas específicas) têm tanto caminhos pagos quanto gratuitos (scraping) a serem avaliados conforme a necessidade real aparecer.
