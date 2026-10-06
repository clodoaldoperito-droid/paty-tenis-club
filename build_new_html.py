import os

html_code = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PATY TÊNIS CLUB | Clube de Assinatura Oficial</title>
  <meta name="description" content="Monte sua lista com no mínimo 12 tênis do catálogo e receba 4 modelos originais por ano no seu endereço por apenas 12x de R$ 99,90.">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="style.css">
</head>
<body class="dark-theme">
  <div class="glow-sphere glow-cyan"></div>
  <div class="glow-sphere glow-gold"></div>

  <!-- Announcement Bar -->
  <div class="announcement-bar">
    <div class="container flex-center-between">
      <span class="badge-live">● ASSINATURA ANUAL OFICIAL</span>
      <span class="announcement-text">Escolha no mínimo 12 modelos e receba 4 tênis no ano por 12x de R$ 99,90</span>
      <a href="#planos" class="announcement-link">Ver Termos e Assinar &rarr;</a>
    </div>
  </div>

  <!-- Header -->
  <header class="site-header">
    <div class="container nav-container">
      <a href="#" class="logo">
        <span class="logo-brand">PATY TÊNIS</span>
        <span class="logo-club">CLUB</span>
        <span class="tag-vip">OFICIAL</span>
      </a>

      <nav class="nav-links">
        <a href="#como-funciona">Regras do Clube</a>
        <a href="#box">O Box</a>
        <a href="#catalogo">Catálogo e Escolha</a>
        <a href="#planos">Assinatura</a>
        <a href="#termos">Termos e Aceite</a>
        <a href="#faq">Dúvidas</a>
      </nav>

      <div class="nav-actions">
        <a href="#planos" class="btn btn-primary btn-glow">
          <span>Entrar no Clube</span>
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section" id="inicio">
    <div class="container hero-grid">
      <div class="hero-content">
        <div class="hero-badge">
          <span class="pill-pulse"></span>
          <span>SNEAKERS ORIGINAIS POR ASSINATURA</span>
        </div>
        
        <h1 class="hero-title">
          RECEBA 4 TÊNIS POR ANO POR APENAS <span class="text-gradient-cyan">12x DE R$ 99,90</span>.
        </h1>
        
        <p class="hero-subtitle">
          Você escolhe no mínimo <strong>12 modelos favoritos</strong> em nosso catálogo oficial e nós enviamos <strong>4 pares ao longo do ano</strong> direto para o seu endereço, de acordo com o estoque. Entrega programada e garantida.
        </p>

        <div class="hero-cta-group">
          <a href="#catalogo" class="btn btn-primary btn-lg btn-glow">
            <span>Montar Minha Lista de 12 Tênis</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
          <a href="#como-funciona" class="btn btn-outline btn-lg">
            <span>Entenda as Regras</span>
          </a>
        </div>

        <div class="hero-stats-row">
          <div class="stat-box">
            <span class="stat-num">4 Pares</span>
            <span class="stat-label">Entregues no Ano</span>
          </div>
          <div class="stat-separator"></div>
          <div class="stat-box">
            <span class="stat-num">Mín. 12</span>
            <span class="stat-label">Modelos que Você Escolhe</span>
          </div>
          <div class="stat-separator"></div>
          <div class="stat-box">
            <span class="stat-num">35 ao 45</span>
            <span class="stat-label">Grade Completa</span>
          </div>
        </div>
      </div>

      <!-- Container Interativo com Tênis do Catálogo que Desmonta no Hover -->
      <div class="hero-visual">
        <div class="hero-card-interactive" id="heroInteractiveSneaker">
          <div class="floating-badge badge-top-right">
            <span class="dot-green"></span> MODELO DO CATÁLOGO OFICIAL
          </div>
          
          <div class="sneaker-layers-wrapper">
            <img src="assets/sneaker-assembled.jpg" alt="Tênis do Catálogo Paty Tênis" class="sneaker-layer sneaker-assembled">
            <img src="assets/exploded-view.jpg" alt="Tênis Desmontado em Camadas" class="sneaker-layer sneaker-dismantled">
            
            <div class="dismantled-tags-overlay">
              <span class="part-tag tag-laces">Cadarços e Língua</span>
              <span class="part-tag tag-upper">Cabedal em Couro</span>
              <span class="part-tag tag-insole">Palmilha Anatômica</span>
              <span class="part-tag tag-shank">Carbon Shank</span>
              <span class="part-tag tag-air">Câmara de Ar</span>
              <span class="part-tag tag-outsole">Solado de Borracha</span>
            </div>
          </div>

          <div class="hover-instruction-badge" id="hoverBadge">
            <span class="hover-icon">👆</span>
            <span class="hover-text" id="hoverText">PASSE O MOUSE PARA DESMONTAR O TÊNIS</span>
          </div>

          <div class="floating-hud badge-bottom-left">
            <div class="hud-header">STATUS DO PRODUTO</div>
            <div class="hud-row"><span>Catálogo:</span> <strong>Disponível na Seleção</strong></div>
            <div class="hud-row"><span>Estrutura:</span> <strong id="hudStructure">Original Montado</strong></div>
            <div class="hud-row"><span>Envio:</span> <strong>Integrado ao Plano Anual</strong></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Regras Claras do Clube (Passo a Passo de Seleção e Envio) -->
  <section class="timeline-section" id="como-funciona">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag">REGRAS DE FUNCIONAMENTO</div>
        <h2 class="section-title">COMO FUNCIONA A <span class="text-gradient-cyan">SELEÇÃO E ENTREGA</span></h2>
        <p class="section-description">
          Transparência completa para você receber exatamente os modelos que combinam com seu estilo.
        </p>
      </div>

      <div class="rules-grid">
        <div class="rule-box glass-panel">
          <div class="rule-icon-box">📋</div>
          <h3>1. Você Escolhe no Mínimo 12 Modelos</h3>
          <p>Ao assinar o clube, você monta sua lista de preferências selecionando <strong>no mínimo 12 tênis</strong> do nosso catálogo oficial que você mais gosta.</p>
        </div>

        <div class="rule-box glass-panel">
          <div class="rule-icon-box">👟</div>
          <h3>2. Enviamos 4 Modelos da Sua Lista</h3>
          <p>Nossa equipe garante o envio de <strong>4 modelos contidos na sua lista de 12</strong> ao longo do ano, selecionados de acordo com a disponibilidade do nosso estoque.</p>
        </div>

        <div class="rule-box glass-panel">
          <div class="rule-icon-box">🛡️</div>
          <h3>3. Garantia de Fabricação</h3>
          <p>Somente será enviado um modelo fora da sua lista caso algum tênis escolhido tenha <strong>saído de linha ou sido descontinuado pelo fabricante</strong>. Nesse caso, enviaremos um modelo similar de mesmo padrão.</p>
        </div>

        <div class="rule-box glass-panel">
          <div class="rule-icon-box">📦</div>
          <h3>4. Cronograma Trimestral (3 em 3 Meses)</h3>
          <p>Você investe 12 parcelas de R$ 99,90. Na compensação de <strong>cada 3 parcelas quitadas</strong> (3ª, 6ª, 9ª e 12ª parcela), um novo tênis é despachado para a sua casa.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Unboxing Section -->
  <section class="unboxing-section" id="box">
    <div class="container">
      <div class="unboxing-grid">
        <div class="unboxing-visual">
          <div class="unboxing-glow-box">
            <img src="assets/club-box.jpg" alt="Paty Tênis Club Box do Mês" class="unboxing-img">
          </div>
        </div>

        <div class="unboxing-info">
          <div class="section-tag text-gold">EXPERIÊNCIA COMPLETA</div>
          <h2 class="section-title">O QUE VEM NO SEU <span class="text-gradient-gold">BOX TRIMESTRAL</span></h2>
          <p class="unboxing-p">
            A cada remessa trimestral, você recebe uma embalagem exclusiva contendo:
          </p>

          <div class="box-perks-list">
            <div class="box-perk-item">
              <div class="perk-icon-gold">👟</div>
              <div>
                <h4>Tênis Original Selecionado da Sua Lista</h4>
                <p>Um dos modelos da sua lista de 12 favoritos, no seu tamanho exato e inspecionado.</p>
              </div>
            </div>

            <div class="box-perk-item">
              <div class="perk-icon-gold">💳</div>
              <div>
                <h4>Cartão Black VIP de Membro</h4>
                <p>Identificação oficial de assinante e benefícios exclusivos em toda a rede Paty Tênis.</p>
              </div>
            </div>

            <div class="box-perk-item">
              <div class="perk-icon-gold">✨</div>
              <div>
                <h4>Kit de Limpeza e Cuidados Sneaker</h4>
                <p>Mantenha seus pares limpos e conservados com produtos especializados.</p>
              </div>
            </div>

            <div class="box-perk-item">
              <div class="perk-icon-gold">🎁</div>
              <div>
                <h4>Pack Colecionável de Brindes</h4>
                <p>Meias especiais, adesivos metalizados e acessórios do universo sneakerhead.</p>
              </div>
            </div>
          </div>

          <div class="unboxing-cta-row">
            <a href="#catalogo" class="btn btn-gold btn-lg btn-glow">Montar Minha Lista Agora &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Catalog (Monte sua Lista de 12 Tênis) -->
  <section class="catalog-section" id="catalogo">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag">MONTE SUA WISHLIST</div>
        <h2 class="section-title">CATÁLOGO OFICIAL: <span class="text-gradient-cyan">ESCOLHA SEUS 12 FAVORITOS</span></h2>
        <p class="section-description">
          Clique nos tênis para adicionar à sua lista de preferências. Você precisa escolher <strong>no mínimo 12 modelos</strong> para compor o seu plano anual.
        </p>

        <!-- Floating Wishlist Counter -->
        <div class="wishlist-status-card glass-panel" id="wishlistStatusCard">
          <div class="wishlist-status-info">
            <span class="wishlist-counter-label">SUA LISTA DE PREFERÊNCIAS:</span>
            <div class="wishlist-counter-badge">
              <strong id="selectedCount">0</strong> / 12 modelos selecionados (mínimo)
            </div>
          </div>
          <div class="wishlist-status-msg" id="wishlistMsg">
            Selecione pelo menos 12 modelos abaixo para habilitar o envio.
          </div>
        </div>

        <div class="catalog-filter-bar">
          <button class="filter-btn active" data-filter="all">Todos (18)</button>
          <button class="filter-btn" data-filter="ADIDAS">Adidas</button>
          <button class="filter-btn" data-filter="NIKE">Nike</button>
          <button class="filter-btn" data-filter="Corrida">Corrida e Treino</button>
          <button class="filter-btn" data-filter="Streets">Casual e Street</button>
        </div>
      </div>

      <div class="catalog-grid" id="catalogGrid"></div>

      <div class="catalog-footer-note">
        <p>💡 <em>A numeração do seu calçado é confirmada individualmente por WhatsApp antes de cada um dos 4 despachos no ano.</em></p>
      </div>
    </div>
  </section>

  <!-- Pricing Section & Termos Contratuais com Aceite Obrigatório -->
  <section class="pricing-section" id="planos">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag text-gold">ASSINATURA ANUAL</div>
        <h2 class="section-title">PLANO PATY TÊNIS CLUB <span class="text-gradient-gold">ANUAL</span></h2>
        <p class="section-description">
          4 pares de tênis originais entregues ao longo de 12 meses na sua casa.
        </p>
      </div>

      <div class="pricing-wrapper-centered">
        <div class="pricing-card glass-panel featured-tier">
          <div class="featured-ribbon">PLANO ANUAL COM ENTREGA PROGRAMADA</div>
          
          <div class="card-tier-badge badge-glow">ADESÃO AO CLUBE</div>
          <h3 class="tier-name">12x de R$ 99,90 / mês</h3>
          <p class="tier-desc">Receba 4 tênis originais no ano (1 tênis enviado a cada 3 parcelas mensais quitadas).</p>
          
          <div class="price-block">
            <span class="currency">12 parcelas de</span>
            <span class="amount">R$ 99,90</span>
            <span class="period">/mês</span>
          </div>
          <span class="price-sub">✓ 4 envios garantidos baseados na sua lista de 12 modelos</span>

          <ul class="tier-features">
            <li>✔ <strong>04 Tênis Originais por ano</strong> (1 entregue no 3º, 6º, 9º e 12º mês)</li>
            <li>✔ <strong>Garantia de Escolha:</strong> enviados exclusivamente dentre os 12 selecionados por você</li>
            <li>✔ <strong>Garantia de Linha:</strong> outro modelo só será enviado se algum escolhido for descontinuado pelo fabricante</li>
            <li>✔ Box trimestral acompanhado de kit de limpeza e brindes</li>
            <li>✔ Pagamento seguro gerenciado pela <strong>Kiwify Pagamentos</strong></li>
          </ul>

          <!-- Box de Termos, Condições e Política de Não-Reembolso -->
          <div class="contract-terms-box" id="termos">
            <h4>📜 TERMOS DE ADESÃO E REGRAS DO CLUBE</h4>
            <div class="terms-scroll-area">
              <p><strong>1. SELEÇÃO DE MODELOS:</strong> O assinante deve selecionar no mínimo 12 modelos em sua lista no catálogo oficial. A Paty Tênis enviará 4 modelos constantes nessa lista, conforme a disponibilidade do estoque da loja.</p>
              <p><strong>2. SAÍDA DE LINHA:</strong> Caso algum dos modelos selecionados pelo cliente tenha saído de linha ou sido descontinuado pelo fabricante oficial, a empresa enviará outro modelo de mesma qualidade e categoria equivalente.</p>
              <p><strong>3. CRONOGRAMA DE EXPEDIÇÃO:</strong> A expedição de cada par de calçados ocorre na compensação da 3ª, 6ª, 9ª e 12ª parcelas mensais devidamente quitadas.</p>
              <p><strong>4. POLÍTICA DE DESISTÊNCIA E NÃO-REEMBOLSO:</strong> Fica expressamente acordado que, em caso de cancelamento, inadimplência ou desistência da assinatura antes da conclusão do ciclo trimestral de envio, <strong>os valores já pagos pelo cliente NÃO SERÃO DEVOLVIDOS</strong>. As quantias pagas serão integralmente retidas para cobrir custos de reserva, compras programadas junto aos fornecedores, estocagem, custos operacionais e cobertura de prejuízos decorrentes da quebra antecipada do plano.</p>
              <p><strong>5. FRETE E TRIBUTOS:</strong> Os custos de frete/remessa e eventuais impostos locais incidentes sobre a entrega não estão inclusos na parcela de R$ 99,90 e serão cobrados à parte no momento de cada envio.</p>
            </div>

            <!-- Checkbox de Aceite Obrigatório -->
            <label class="terms-accept-label">
              <input type="checkbox" id="termsCheckbox" class="terms-checkbox">
              <span class="terms-checkbox-custom"></span>
              <span class="terms-text">
                Li, compreendo e <strong>CONCORDO</strong> com as regras de seleção de 12 modelos, o cronograma trimestral e a <strong>política de não devolução de valores em caso de desistência</strong>.
              </span>
            </label>
          </div>

          <!-- Botão de Assinatura via Kiwify -->
          <button id="btnSubscribeKiwify" class="btn btn-primary btn-glow btn-block btn-lg" disabled>
            <span>Assinar Plano Anual na Kiwify</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>

          <p class="terms-warning-hint" id="termsHint">
            ⚠️ <em>Marque a caixa de aceite dos termos acima para prosseguir para o pagamento seguro.</em>
          </p>

          <div class="security-banner">
            <span>🔒 Pagamento Seguro e Criptografado via Kiwify Pagamentos</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="faq-section" id="faq">
    <div class="container faq-container">
      <div class="section-header text-center">
        <div class="section-tag">DÚVIDAS FREQUENTES</div>
        <h2 class="section-title">PERGUNTAS <span class="text-gradient-cyan">FREQUENTES</span></h2>
      </div>

      <div class="faq-accordion">
        <div class="faq-item active">
          <button class="faq-question">
            <span>Como funciona a escolha dos 12 modelos?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Você navega pelo nosso catálogo oficial e escolhe no mínimo 12 modelos que você mais gosta. Ao longo do ano, nós enviaremos 4 modelos escolhidos exclusivamente dessa sua lista de 12, de acordo com o nosso estoque.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>E se um modelo da minha lista tiver saído de linha?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Somente enviaremos um modelo fora da sua lista caso o modelo que você escolheu tenha sido descontinuado ou saído de linha pelo fabricante oficial (Nike ou Adidas). Nesse caso, enviaremos um modelo similar equivalente do mesmo padrão.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Se eu cancelar ou parar de pagar, recebo o dinheiro de volta?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Não. Conforme previsto no termo de adesão, os valores pagos não são reembolsados em caso de cancelamento ou desistência. Eles são utilizados para cobrir os custos de reserva, compras programadas com fornecedores, estocagem, custos operacionais e prejuízos causados pela desistência.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Quando recebo cada um dos 4 tênis?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>A entrega é trimestral: você recebe o 1º tênis na confirmação da 3ª parcela, o 2º tênis na 6ª parcela, o 3º tênis na 9ª parcela e o 4º tênis na 12ª parcela quitada.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>O frete e os impostos estão inclusos na parcela de R$ 99,90?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Não. A parcela de R$ 99,90 cobre a assinatura dos calçados e o box do clube. Custos de frete/remessa e eventuais impostos são calculados à parte na ocasião de cada despacho para o seu CEP.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Os tênis são 100% originais?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Sim, 100% autênticos e inspecionados. Trabalhamos exclusivamente com modelos oficiais com garantia total de procedência e grade do 35 ao 45.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand-col">
        <div class="logo">
          <span class="logo-brand">PATY TÊNIS</span>
          <span class="logo-club">CLUB</span>
        </div>
        <p class="footer-text">
          O clube de assinatura oficial de tênis da Paty Tênis. Escolha seus 12 favoritos e receba 4 pares originais ao longo do ano.
        </p>
        <p class="footer-copy">&copy; 2026 PATY TÊNIS CLUB. Todos os direitos reservados. CNPJ 03.809.446/0001-50.</p>
      </div>

      <div class="footer-col">
        <h4>Navegação</h4>
        <ul>
          <li><a href="#como-funciona">Regras do Clube</a></li>
          <li><a href="#box">O Box</a></li>
          <li><a href="#catalogo">Catálogo de Escolha</a></li>
          <li><a href="#planos">Assinatura</a></li>
          <li><a href="#termos">Termos e Condições</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Atendimento</h4>
        <ul>
          <li><a href="https://wa.me/5519999999999" target="_blank">WhatsApp de Atendimento</a></li>
          <li><a href="#faq">Dúvidas Frequentes</a></li>
          <li><a href="#termos">Política de Desistência</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Pagamento Homologado</h4>
        <div class="security-badges">
          <span class="sec-badge">🔒 Kiwify Pagamentos</span>
          <span class="sec-badge">⚡ Pix Instantâneo</span>
          <span class="sec-badge">💳 Cartão em 12x</span>
        </div>
      </div>
    </div>
  </footer>

  <script src="app.js"></script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("index.html updated successfully with 12-shoe wishlist, no prices, and terms checkbox!")
