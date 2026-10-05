import os

html_code = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PATY TÊNIS CLUB | Clube de Assinatura Oficial</title>
  <meta name="description" content="Receba 4 tênis originais por ano no conforto da sua casa por apenas 12x de R$ 99,90. O clube de assinatura oficial da Paty Tênis.">
  
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
      <span class="badge-live">● VAGAS ABERTAS PARA O LOTE ANUAL</span>
      <span class="announcement-text">Receba 4 Tênis originais por ano por apenas 12x de R$ 99,90 | Grade do 35 ao 45</span>
      <a href="#planos" class="announcement-link">Quero Minha Vaga &rarr;</a>
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
        <a href="#como-funciona">Como Funciona</a>
        <a href="#box">O Box</a>
        <a href="#catalogo">Catálogo</a>
        <a href="#planos">Planos</a>
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

  <!-- Hero Section com Tênis do Catálogo que Desmonta ao Passar o Mouse -->
  <section class="hero-section" id="inicio">
    <div class="container hero-grid">
      <div class="hero-content">
        <div class="hero-badge">
          <span class="pill-pulse"></span>
          <span>CLUBE EXCLUSIVO DE ASSINATURA</span>
        </div>
        
        <h1 class="hero-title">
          4 TÊNIS ORIGINAIS POR ANO POR APENAS <span class="text-gradient-cyan">12x DE R$ 99,90</span>.
        </h1>
        
        <p class="hero-subtitle">
          Renove sua coleção a cada 3 meses com os modelos mais cobiçados da Nike e Adidas (valor avulso de R$ 320,00 por par). Sem filas, sem preços abusivos e com entrega programada.
        </p>

        <div class="hero-cta-group">
          <a href="#planos" class="btn btn-primary btn-lg btn-glow">
            <span>Garantir Meu Plano</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
          <a href="#catalogo" class="btn btn-outline btn-lg">
            <span>Ver Catálogo Completo</span>
          </a>
        </div>

        <div class="hero-stats-row">
          <div class="stat-box">
            <span class="stat-num">4 Pares</span>
            <span class="stat-label">Entregues no Ano</span>
          </div>
          <div class="stat-separator"></div>
          <div class="stat-box">
            <span class="stat-num">18 Modelos</span>
            <span class="stat-label">No Catálogo Ativo</span>
          </div>
          <div class="stat-separator"></div>
          <div class="stat-box">
            <span class="stat-num">35 ao 45</span>
            <span class="stat-label">Grade Completa</span>
          </div>
        </div>
      </div>

      <!-- Container Interativo: Tênis Montado que Desmonta no Hover -->
      <div class="hero-visual">
        <div class="hero-card-interactive" id="heroInteractiveSneaker">
          <div class="floating-badge badge-top-right">
            <span class="dot-green"></span> NIKE AIR SERIES // CATÁLOGO OFICIAL
          </div>
          
          <div class="sneaker-layers-wrapper">
            <!-- Imagem 1: Tênis Montado (Padrão) -->
            <img src="assets/sneaker-assembled.jpg" alt="Tênis Nike Air do Catálogo Paty Tênis" class="sneaker-layer sneaker-assembled">
            
            <!-- Imagem 2: Tênis Desmontado (Revelado no Hover) -->
            <img src="assets/exploded-view.jpg" alt="Tênis Desmontado em Camadas" class="sneaker-layer sneaker-dismantled">
            
            <!-- Tags flutuantes que surgem no hover quando desmontado -->
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
            <div class="hud-row"><span>Modelo:</span> <strong>Nike Air Series</strong></div>
            <div class="hud-row"><span>Estrutura:</span> <strong id="hudStructure">Original Montado</strong></div>
            <div class="hud-row"><span>Valor no Estoque:</span> <strong>R$ 320,00</strong></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Como Funciona o Ciclo de Entrega (12 parcelas / 4 tênis) -->
  <section class="timeline-section" id="como-funciona">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag">ENTREGA PROGRAMADA</div>
        <h2 class="section-title">COMO FUNCIONA O <span class="text-gradient-cyan">SEU PLANO</span></h2>
        <p class="section-description">
          Você paga uma mensalidade de R$ 99,90 e, a cada 3 parcelas quitadas, recebe um tênis original de R$ 320,00 na sua residência.
        </p>
      </div>

      <div class="timeline-grid">
        <div class="timeline-card glass-panel">
          <div class="timeline-step">1º TRIMESTRE</div>
          <h4>Meses 1, 2 e 3</h4>
          <p>Você paga a 1ª, 2ª e 3ª parcela. Na compensação da <strong>3ª parcela</strong>, despachamos o seu <strong>1º Tênis</strong>.</p>
          <span class="timeline-tag">📦 1º Tênis Enviado</span>
        </div>

        <div class="timeline-card glass-panel">
          <div class="timeline-step">2º TRIMESTRE</div>
          <h4>Meses 4, 5 e 6</h4>
          <p>Você paga a 4ª, 5ª e 6ª parcela. Na compensação da <strong>6ª parcela</strong>, despachamos o seu <strong>2º Tênis</strong>.</p>
          <span class="timeline-tag">📦 2º Tênis Enviado</span>
        </div>

        <div class="timeline-card glass-panel">
          <div class="timeline-step">3º TRIMESTRE</div>
          <h4>Meses 7, 8 e 9</h4>
          <p>Você paga a 7ª, 8ª e 9ª parcela. Na compensação da <strong>9ª parcela</strong>, despachamos o seu <strong>3º Tênis</strong>.</p>
          <span class="timeline-tag">📦 3º Tênis Enviado</span>
        </div>

        <div class="timeline-card glass-panel">
          <div class="timeline-step">4º TRIMESTRE</div>
          <h4>Meses 10, 11 e 12</h4>
          <p>Você paga a 10ª, 11ª e 12ª parcela. Na compensação da <strong>12ª parcela</strong>, despachamos o seu <strong>4º Tênis</strong>.</p>
          <span class="timeline-tag">📦 4º Tênis Enviado</span>
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
            A cada remessa, você recebe uma caixa personalizada contendo:
          </p>

          <div class="box-perks-list">
            <div class="box-perk-item">
              <div class="perk-icon-gold">👟</div>
              <div>
                <h4>Tênis Original Selecionado (Ref. R$ 320,00)</h4>
                <p>Modelo escolhido por você ou curadoria especial no seu tamanho exato.</p>
              </div>
            </div>

            <div class="box-perk-item">
              <div class="perk-icon-gold">💳</div>
              <div>
                <h4>Cartão Black VIP de Membro</h4>
                <p>Acesso antecipado a reposições raras e descontos exclusivos na rede.</p>
              </div>
            </div>

            <div class="box-perk-item">
              <div class="perk-icon-gold">✨</div>
              <div>
                <h4>Kit de Limpeza e Cuidados Sneaker</h4>
                <p>Mantenha seus pares limpos e impermeabilizados com produtos profissionais.</p>
              </div>
            </div>

            <div class="box-perk-item">
              <div class="perk-icon-gold">🎁</div>
              <div>
                <h4>Pack Colecionável de Brindes</h4>
                <p>Meias especiais, adesivos metalizados e acessórios de colecionador.</p>
              </div>
            </div>
          </div>

          <div class="unboxing-cta-row">
            <a href="#planos" class="btn btn-gold btn-lg btn-glow">Garantir Minha Vaga &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Realtime Catalog -->
  <section class="catalog-section" id="catalogo">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag">MODELOS DISPONÍVEIS</div>
        <h2 class="section-title">CATÁLOGO EM <span class="text-gradient-cyan">ESTOQUE</span></h2>
        <p class="section-description">
          Todos os modelos abaixo estão contemplados no seu plano de assinatura (valor avulso de R$ 320,00 cada).
        </p>

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
        <p>💡 <em>A confirmação milimétrica do tamanho é feita com nossa equipe antes de cada remessa trimestral.</em></p>
      </div>
    </div>
  </section>

  <!-- Pricing Section -->
  <section class="pricing-section" id="planos">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag text-gold">PLANO OFICIAL DE ASSINATURA</div>
        <h2 class="section-title">INVESTIMENTO INTELIGENTE EM <span class="text-gradient-gold">SNEAKERS</span></h2>
        <p class="section-description">
          Sem contratos abusivos. Você recebe 4 tênis originais ao longo do ano com parcelas leves no seu cartão.
        </p>
      </div>

      <div class="pricing-wrapper-centered">
        <div class="pricing-card glass-panel featured-tier">
          <div class="featured-ribbon">PLANO ANUAL RECOMENDADO</div>
          
          <div class="card-tier-badge badge-glow">CLUBE PATY TÊNIS ANUAL</div>
          <h3 class="tier-name">Plano 4 Tênis por Ano</h3>
          <p class="tier-desc">Receba 1 tênis novo original (valor avulso de R$ 320,00) a cada 3 parcelas mensais quitadas.</p>
          
          <div class="price-block">
            <span class="currency">12x de R$</span>
            <span class="amount">99,90</span>
            <span class="period">/mês</span>
          </div>
          <span class="price-sub">✓ 4 tênis no valor total de R$ 1.280,00 por apenas 12x de R$ 99,90</span>

          <div class="shipping-notice">
            <span>⚠️ <strong>Atenção:</strong> Custos de frete/remessa e tributos locais não estão inclusos na parcela de R$ 99,90 e são calculados no momento do envio de cada par.</span>
          </div>

          <ul class="tier-features">
            <li>✔ <strong>04 Tênis Originais por ano</strong> (1 par entregue a cada 3 meses pagos)</li>
            <li>✔ <strong>Valor individual de referência:</strong> R$ 320,00 por calçado</li>
            <li>✔ <strong>1º Tênis:</strong> enviado na compensação da 3ª parcela</li>
            <li>✔ <strong>2º Tênis:</strong> enviado na compensação da 6ª parcela</li>
            <li>✔ <strong>3º Tênis:</strong> enviado na compensação da 9ª parcela</li>
            <li>✔ <strong>4º Tênis:</strong> enviado na compensação da 12ª parcela</li>
            <li>✔ Box especial acompanhado de kit de limpeza e brindes</li>
            <li>✔ Pagamento seguro e transparente gerenciado pela <strong>Kiwify</strong></li>
          </ul>

          <a href="https://pay.kiwify.com.br/" target="_blank" class="btn btn-primary btn-glow btn-block btn-lg">
            <span>Assinar Agora com Kiwify</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>

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
        <h2 class="section-title">TUDO EXPLICADO COM <span class="text-gradient-cyan">CLAREZA</span></h2>
      </div>

      <div class="faq-accordion">
        <div class="faq-item active">
          <button class="faq-question">
            <span>Quando recebo o meu primeiro tênis?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>O primeiro tênis é despachado após a confirmação da <strong>3ª parcela de R$ 99,90</strong>. O segundo tênis é enviado na 6ª parcela, o terceiro na 9ª parcela e o quarto na 12ª parcela, totalizando 4 pares originais ao longo do ano.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Qual é o valor de mercado de cada tênis entregue?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Cada tênis do catálogo tem valor de referência de <strong>R$ 320,00</strong>. Comprando 4 tênis avulsos você gastaria R$ 1.280,00, além de não ter os brindes exclusivos e a comodidade do clube.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>O frete e os impostos estão inclusos na parcela de R$ 99,90?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Não. O valor da parcela de R$ 99,90 cobre a aquisição programada dos calçados e a experiência do clube. Os valores de remessa/frete para o seu CEP e eventuais taxas/impostos são calculados e informados separadamente na ocasião do despacho de cada par.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Os tênis são originais?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Sim, 100% autênticos e inspecionados. Trabalhamos exclusivamente com marcas consagradas (Nike e Adidas) com garantia total de procedência e grade de numeração do 35 ao 45.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>E se a numeração não servir no meu pé?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Você tem garantia de troca de numeração! Antes de cada despacho, nossa equipe confirma milimetricamente o tamanho ideal com você pelo WhatsApp.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Qual é a plataforma de pagamento utilizada?</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Todas as cobranças são processadas com segurança máxima através da plataforma oficial <strong>Kiwify Pagamentos</strong>, podendo ser pagas via Cartão de Crédito ou Pix.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Final CTA Banner -->
  <section class="cta-banner-section">
    <div class="container">
      <div class="cta-banner-box glass-panel">
        <div class="cta-banner-content">
          <h2>GARANTA SUA VAGA NO CLUBE PATY TÊNIS</h2>
          <p>4 tênis originais por ano, entregues de 3 em 3 meses por apenas 12x de R$ 99,90.</p>
        </div>
        <div class="cta-banner-actions">
          <a href="#planos" class="btn btn-primary btn-lg btn-glow">Garantir Minha Vaga com Kiwify</a>
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
          O clube de assinatura oficial de tênis da Paty Tênis. Sneakers originais com entrega trimestral programada.
        </p>
        <p class="footer-copy">&copy; 2026 PATY TÊNIS CLUB. Todos os direitos reservados. CNPJ 03.809.446/0001-50.</p>
      </div>

      <div class="footer-col">
        <h4>Navegação</h4>
        <ul>
          <li><a href="#como-funciona">Como Funciona</a></li>
          <li><a href="#box">O Box</a></li>
          <li><a href="#catalogo">Catálogo</a></li>
          <li><a href="#planos">Planos</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Atendimento</h4>
        <ul>
          <li><a href="https://wa.me/5519999999999" target="_blank">WhatsApp de Atendimento</a></li>
          <li><a href="#faq">Dúvidas Frequentes</a></li>
          <li><a href="#">Política de Trocas</a></li>
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

print("Clean index.html updated successfully!")
