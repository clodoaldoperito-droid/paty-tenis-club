// PATY TENIS CLUB - SCRIPT OFICIAL

// 1. Catálogo Oficial com Fotos e Dados do Estoque
const catalogData = [
  { id: 1, brand: "ADIDAS", model: "Samba Classic", category: "Clássicos / Streets / Academia", sizes: "35 a 45", type: "Streets", image: "assets/samba-assembled.jpg" },
  { id: 2, brand: "ADIDAS", model: "Superstar", category: "Clássicos / Streets / Academia", sizes: "35 a 45", type: "Streets", image: "assets/samba-assembled.jpg" },
  { id: 3, brand: "ADIDAS", model: "Gazelle Retrô", category: "Clássicos / Streets / Academia", sizes: "35 a 45", type: "Streets", image: "assets/samba-assembled.jpg" },
  { id: 4, brand: "ADIDAS", model: "Campus", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", type: "Streets", image: "assets/samba-assembled.jpg" },
  { id: 5, brand: "ADIDAS", model: "Forum", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", type: "Streets", image: "assets/samba-assembled.jpg" },
  { id: 6, brand: "ADIDAS", model: "Stan Smith", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", type: "Streets", image: "assets/samba-assembled.jpg" },
  { id: 7, brand: "ADIDAS", model: "Ozweego", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", type: "Streets", image: "assets/samba-assembled.jpg" },
  { id: 8, brand: "ADIDAS", model: "NMD R1", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", type: "Streets", image: "assets/samba-assembled.jpg" },
  { id: 9, brand: "ADIDAS", model: "Ultraboost", category: "Corrida / Treino / Conforto Extremo", sizes: "35 a 45", type: "Corrida", image: "assets/boost-assembled.jpg" },
  { id: 10, brand: "ADIDAS", model: "Adizero Pro", category: "Corrida / Treino / Alta Performance", sizes: "35 a 45", type: "Corrida", image: "assets/boost-assembled.jpg" },
  { id: 11, brand: "ADIDAS", model: "Supernova", category: "Corrida / Treino / Conforto Diário", sizes: "35 a 45", type: "Corrida", image: "assets/boost-assembled.jpg" },
  { id: 12, brand: "ADIDAS", model: "Adistar", category: "Corrida / Treino / Longas Distâncias", sizes: "35 a 45", type: "Corrida", image: "assets/boost-assembled.jpg" },
  { id: 13, brand: "NIKE", model: "Air Force 1", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", type: "Streets", image: "assets/sneaker-assembled.jpg" },
  { id: 14, brand: "NIKE", model: "Dunk Low Panda", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", type: "Streets", image: "assets/dunk-assembled.jpg" },
  { id: 15, brand: "NIKE", model: "Air Max 90", category: "AIR MAX / Streets / Estilo", sizes: "35 a 45", type: "Streets", image: "assets/sneaker-assembled.jpg" },
  { id: 16, brand: "NIKE", model: "Air Max 95", category: "AIR MAX / Streets / Conforto", sizes: "35 a 45", type: "Streets", image: "assets/sneaker-assembled.jpg" },
  { id: 17, brand: "NIKE", model: "Air Max 97", category: "AIR MAX / Streets / Futurista", sizes: "35 a 45", type: "Streets", image: "assets/sneaker-assembled.jpg" },
  { id: 18, brand: "NIKE", model: "Pegasus Running", category: "Corrida / Treino / Amortecimento Rápido", sizes: "35 a 45", type: "Corrida", image: "assets/boost-assembled.jpg" }
];

let selectedWishlist = new Set();

const catalogGrid = document.getElementById('catalogGrid');
const selectedCountEl = document.getElementById('selectedCount');
const wishlistStatusCard = document.getElementById('wishlistStatusCard');
const wishlistMsg = document.getElementById('wishlistMsg');

function updateWishlistCounter() {
  const count = selectedWishlist.size;
  if (selectedCountEl) selectedCountEl.textContent = count;
  
  if (count >= 12) {
    if (wishlistStatusCard) wishlistStatusCard.classList.add('ready');
    if (wishlistMsg) {
      wishlistMsg.innerHTML = `<span style="color: var(--accent-green); font-weight: 700;">✓ Perfeito! Você selecionou ${count} modelos com fotos.</span> Seus 4 pares do ano sairão exclusivamente desta sua lista!`;
    }
  } else {
    if (wishlistStatusCard) wishlistStatusCard.classList.remove('ready');
    if (wishlistMsg) {
      const faltam = 12 - count;
      wishlistMsg.textContent = `Faltam ${faltam} modelo(s) para atingir o mínimo de 12 para o seu plano anual.`;
    }
  }
}

function renderCatalog(items) {
  if (!catalogGrid) return;
  catalogGrid.innerHTML = items.map(item => {
    const isSelected = selectedWishlist.has(item.id);
    return `
      <div class="sneaker-card ${isSelected ? 'selected' : ''}" id="card-${item.id}">
        <div class="sneaker-card-image">
          <img src="${item.image}" alt="${item.brand} ${item.model}" loading="lazy">
        </div>
        <div>
          <span class="card-brand-badge">${item.brand}</span>
          <h4 class="card-title">${item.brand} ${item.model}</h4>
          <p class="card-category">${item.category}</p>
          <div class="card-sizes">
            <span class="size-pill available">Grade ${item.sizes}</span>
            <span class="size-pill available">Em Estoque</span>
          </div>
        </div>
        <div class="card-footer">
          <div>
            <span class="card-price-ref">Plano Anual</span>
            <div class="card-price-val" style="font-size: 13px; color: var(--accent-cyan);">Incluso no Clube</div>
          </div>
          <button class="btn-card-select ${isSelected ? 'selected' : ''}" onclick="toggleWishlist(${item.id})">
            ${isSelected ? '✓ Na Minha Lista' : '+ Adicionar à Lista'}
          </button>
        </div>
      </div>
    `;
  }).join('');
}

window.toggleWishlist = function(id) {
  if (selectedWishlist.has(id)) {
    selectedWishlist.delete(id);
  } else {
    selectedWishlist.add(id);
  }
  updateWishlistCounter();
  
  const card = document.getElementById(`card-${id}`);
  if (card) {
    const btn = card.querySelector('.btn-card-select');
    if (selectedWishlist.has(id)) {
      card.classList.add('selected');
      if (btn) {
        btn.classList.add('selected');
        btn.textContent = '✓ Na Minha Lista';
      }
    } else {
      card.classList.remove('selected');
      if (btn) {
        btn.classList.remove('selected');
        btn.textContent = '+ Adicionar à Lista';
      }
    }
  }
};

renderCatalog(catalogData);
updateWishlistCounter();

// 2. Filtros de Categorias
const filterBtns = document.querySelectorAll('.filter-btn');
filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    
    const filter = btn.getAttribute('data-filter');
    if (filter === 'all') {
      renderCatalog(catalogData);
    } else if (filter === 'ADIDAS' || filter === 'NIKE') {
      const filtered = catalogData.filter(i => i.brand === filter);
      renderCatalog(filtered);
    } else {
      const filtered = catalogData.filter(i => i.type === filter || i.category.includes(filter));
      renderCatalog(filtered);
    }
  });
});

// 3. Carrossel de 3 Tênis no Hero com Efeito Desmontar no Hover
let currentSlideIndex = 0;
const slides = document.querySelectorAll('.carousel-slide');
const dots = document.querySelectorAll('.carousel-dot');
const carouselBadge = document.getElementById('carouselBadge');
const hudModel = document.getElementById('hudModel');
const hudStructure = document.getElementById('hudStructure');
const hudStyle = document.getElementById('hudStyle');
const hoverText = document.getElementById('hoverText');
const heroCard = document.getElementById('heroInteractiveSneaker');

function goToSlide(index) {
  slides.forEach((s, idx) => {
    s.classList.toggle('active', idx === index);
  });
  dots.forEach((d, idx) => {
    d.classList.toggle('active', idx === index);
  });
  currentSlideIndex = index;

  const activeSlide = slides[index];
  if (activeSlide) {
    if (carouselBadge) carouselBadge.innerHTML = `<span class="dot-green"></span> ${activeSlide.getAttribute('data-badge')}`;
    if (hudModel) hudModel.textContent = activeSlide.getAttribute('data-model');
    if (hudStyle) hudStyle.textContent = activeSlide.getAttribute('data-style');
    if (hudStructure) {
      hudStructure.textContent = heroCard && heroCard.classList.contains('dismantled') ? "Desmontado (Raio-X)" : "Original Montado";
    }
  }
}

// Rotação Automática do Carrossel a cada 4.5 segundos
let carouselTimer = setInterval(() => {
  let next = (currentSlideIndex + 1) % slides.length;
  goToSlide(next);
}, 4500);

function resetCarouselTimer() {
  clearInterval(carouselTimer);
  carouselTimer = setInterval(() => {
    let next = (currentSlideIndex + 1) % slides.length;
    goToSlide(next);
  }, 4500);
}

// Botões Próximo e Anterior
const prevBtn = document.getElementById('prevSlideBtn');
const nextBtn = document.getElementById('nextSlideBtn');

if (prevBtn) {
  prevBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    let prev = (currentSlideIndex - 1 + slides.length) % slides.length;
    goToSlide(prev);
    resetCarouselTimer();
  });
}

if (nextBtn) {
  nextBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    let next = (currentSlideIndex + 1) % slides.length;
    goToSlide(next);
    resetCarouselTimer();
  });
}

// Cliques nos Dots
dots.forEach((dot, idx) => {
  dot.addEventListener('click', (e) => {
    e.stopPropagation();
    goToSlide(idx);
    resetCarouselTimer();
  });
});

// Interatividade Hover que Desmonta o Modelo Ativo (Pausa o carrossel durante a inspeção)
if (heroCard) {
  heroCard.addEventListener('mouseenter', () => {
    clearInterval(carouselTimer); // Pausa para permitir examinar o tênis
    if (hoverText) hoverText.textContent = "DESMONTADO // ANATOMIA REVELADA";
    if (hudStructure) {
      hudStructure.textContent = "Desmontado (Raio-X)";
      hudStructure.style.color = "var(--accent-cyan)";
    }
  });

  heroCard.addEventListener('mouseleave', () => {
    heroCard.classList.remove('dismantled');
    if (hoverText) hoverText.textContent = "PASSE O MOUSE PARA DESMONTAR O TÊNIS";
    if (hudStructure) {
      hudStructure.textContent = "Original Montado";
      hudStructure.style.color = "#fff";
    }
    resetCarouselTimer(); // Retoma o carrossel
  });

  heroCard.addEventListener('click', () => {
    const isDismantled = heroCard.classList.toggle('dismantled');
    if (hoverText) {
      hoverText.textContent = isDismantled ? "DESMONTADO // TOQUE PARA MONTAR" : "PASSE O MOUSE PARA DESMONTAR O TÊNIS";
    }
    if (hudStructure) {
      hudStructure.textContent = isDismantled ? "Desmontado (Raio-X)" : "Original Montado";
      hudStructure.style.color = isDismantled ? "var(--accent-cyan)" : "#fff";
    }
  });
}

// 4. Aceite dos Termos de Contrato e Habilitação do Botão Kiwify
const termsCheckbox = document.getElementById('termsCheckbox');
const btnSubscribeKiwify = document.getElementById('btnSubscribeKiwify');
const termsHint = document.getElementById('termsHint');

if (termsCheckbox && btnSubscribeKiwify) {
  termsCheckbox.addEventListener('change', (e) => {
    if (e.target.checked) {
      btnSubscribeKiwify.removeAttribute('disabled');
      btnSubscribeKiwify.classList.add('btn-glow');
      if (termsHint) {
        termsHint.innerHTML = `<span style="color: var(--accent-green);">✓ Termos aceitos. Você já pode prosseguir para o checkout seguro.</span>`;
      }
    } else {
      btnSubscribeKiwify.setAttribute('disabled', 'true');
      btnSubscribeKiwify.classList.remove('btn-glow');
      if (termsHint) {
        termsHint.innerHTML = `⚠️ <em>Marque a caixa de aceite dos termos acima para prosseguir para o pagamento seguro.</em>`;
      }
    }
  });

  btnSubscribeKiwify.addEventListener('click', () => {
    if (!termsCheckbox.checked) {
      alert("Por favor, leia e marque o aceite dos Termos de Adesão e da Política de Não-Reembolso para continuar.");
      return;
    }
    
    if (selectedWishlist.size < 12) {
      const confirmContinue = confirm(`Você selecionou ${selectedWishlist.size} de 12 modelos recomendados. Deseja prosseguir para o pagamento e completar sua lista depois no WhatsApp?`);
      if (!confirmContinue) {
        document.getElementById('catalogo').scrollIntoView({ behavior: 'smooth' });
        return;
      }
    }

    window.open("https://pay.kiwify.com.br/", "_blank");
  });
}

// 5. FAQ Accordion
const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach(item => {
  const question = item.querySelector('.faq-question');
  question.addEventListener('click', () => {
    const isActive = item.classList.contains('active');
    faqItems.forEach(i => i.classList.remove('active'));
    if (!isActive) {
      item.classList.add('active');
    }
  });
});

console.log("Paty Tênis Club - Carrossel de 3 modelos e fotos de catálogo ativos.");
