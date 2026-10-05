import os

# 1. Update style.css with compact spacing and hover dismantle classes
with open("style.css", "r", encoding="utf-8") as f:
    css_text = f.read()

# Append interactive hero styles
extra_css = """
/* Interactive Dismantle Sneaker on Hero */
.hero-card-interactive {
  position: relative;
  border-radius: 24px;
  background: linear-gradient(145deg, rgba(22, 27, 40, 0.8), rgba(11, 14, 20, 0.95));
  border: 1px solid rgba(0, 240, 255, 0.25);
  padding: 12px;
  box-shadow: 0 15px 35px rgba(0,0,0,0.6), 0 0 30px rgba(0, 240, 255, 0.12);
  cursor: pointer;
  overflow: hidden;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.hero-card-interactive:hover,
.hero-card-interactive.dismantled {
  border-color: var(--accent-cyan);
  box-shadow: 0 20px 45px rgba(0,0,0,0.7), 0 0 35px rgba(0, 240, 255, 0.25);
}

.sneaker-layers-wrapper {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  border-radius: 16px;
  overflow: hidden;
  background: #090b10;
}

.sneaker-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 0.45s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.sneaker-assembled {
  opacity: 1;
  transform: scale(1);
  z-index: 1;
}

.sneaker-dismantled {
  opacity: 0;
  transform: scale(0.96);
  z-index: 2;
}

/* Hover State / Dismantled State */
.hero-card-interactive:hover .sneaker-assembled,
.hero-card-interactive.dismantled .sneaker-assembled {
  opacity: 0;
  transform: scale(1.04);
}

.hero-card-interactive:hover .sneaker-dismantled,
.hero-card-interactive.dismantled .sneaker-dismantled {
  opacity: 1;
  transform: scale(1);
}

.dismantled-tags-overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.35s ease;
}

.hero-card-interactive:hover .dismantled-tags-overlay,
.hero-card-interactive.dismantled .dismantled-tags-overlay {
  opacity: 1;
}

.part-tag {
  position: absolute;
  background: rgba(11, 14, 20, 0.92);
  border: 1px solid var(--accent-cyan);
  color: #fff;
  font-size: 9px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.5);
}

.tag-laces { top: 12%; left: 32%; }
.tag-upper { top: 35%; left: 16%; }
.tag-insole { top: 48%; left: 45%; }
.tag-shank { top: 58%; left: 52%; }
.tag-air { top: 68%; left: 62%; border-color: #00ff9d; color: #00ff9d; }
.tag-outsole { bottom: 12%; left: 35%; }

.hover-instruction-badge {
  position: absolute;
  top: 18px;
  left: 18px;
  z-index: 5;
  background: rgba(7, 9, 14, 0.92);
  border: 1px solid var(--accent-cyan);
  padding: 5px 12px;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 10px;
  font-weight: 800;
  color: var(--accent-cyan);
  letter-spacing: 0.04em;
  transition: all 0.3s;
}

.hero-card-interactive:hover .hover-instruction-badge,
.hero-card-interactive.dismantled .hover-instruction-badge {
  background: rgba(0, 240, 255, 0.2);
  border-color: #fff;
  color: #fff;
}
"""

if ".hero-card-interactive" not in css_text:
    with open("style.css", "a", encoding="utf-8") as f:
        f.write("\n" + extra_css)
    print("style.css updated with hero hover styles.")
else:
    print("style.css already has hero hover styles.")

# 2. Update app.js with R$ 320 prices and interactive hover handler
js_code = """// PATY TENIS CLUB - SCRIPT OFICIAL

// 1. Catálogo com valor oficial de R$ 320,00 por par
const catalogData = [
  { brand: "ADIDAS", model: "Samba", category: "Clássicos / Streets / Academia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "ADIDAS", model: "Superstar", category: "Clássicos / Streets / Academia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "ADIDAS", model: "Gazelle", category: "Clássicos / Streets / Academia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "ADIDAS", model: "Campus", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "ADIDAS", model: "Forum", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "ADIDAS", model: "Stan Smith", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "ADIDAS", model: "Ozweego", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "ADIDAS", model: "NMD", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "ADIDAS", model: "Ultraboost", category: "Corrida / Treino / Conforto Extremo", sizes: "35 a 45", price: 320, type: "Corrida" },
  { brand: "ADIDAS", model: "Adizero", category: "Corrida / Treino / Alta Performance", sizes: "35 a 45", price: 320, type: "Corrida" },
  { brand: "ADIDAS", model: "Supernova", category: "Corrida / Treino / Conforto Diário", sizes: "35 a 45", price: 320, type: "Corrida" },
  { brand: "ADIDAS", model: "Adistar", category: "Corrida / Treino / Longas Distâncias", sizes: "35 a 45", price: 320, type: "Corrida" },
  { brand: "NIKE", model: "Air Force 1", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "NIKE", model: "Dunk Low", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "NIKE", model: "Air Max 90", category: "AIR MAX / Streets / Estilo", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "NIKE", model: "Air Max 95", category: "AIR MAX / Streets / Conforto", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "NIKE", model: "Air Max 97", category: "AIR MAX / Streets / Futurista", sizes: "35 a 45", price: 320, type: "Streets" },
  { brand: "NIKE", model: "Pegasus", category: "Corrida / Treino / Amortecimento Rápido", sizes: "35 a 45", price: 320, type: "Corrida" }
];

const catalogGrid = document.getElementById('catalogGrid');

function renderCatalog(items) {
  if (!catalogGrid) return;
  catalogGrid.innerHTML = items.map(item => `
    <div class="sneaker-card">
      <div>
        <span class="card-brand-badge">${item.brand}</span>
        <h4 class="card-title">${item.brand} ${item.model}</h4>
        <p class="card-category">${item.category}</p>
        <div class="card-sizes">
          <span class="size-pill available">Grade ${item.sizes}</span>
          <span class="size-pill available">No Plano Anual</span>
        </div>
      </div>
      <div class="card-footer">
        <div>
          <span class="card-price-ref">Valor avulso ref.</span>
          <div class="card-price-val">R$ ${item.price},00</div>
        </div>
        <a href="#planos" class="btn-card-select">Assinar</a>
      </div>
    </div>
  `).join('');
}

renderCatalog(catalogData);

// 2. Filtros de Catálogo
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

// 3. Efeito Interativo no Tênis do Hero: Desmontar no Hover / Clique
const heroSneakerCard = document.getElementById('heroInteractiveSneaker');
const hoverText = document.getElementById('hoverText');
const hudStructure = document.getElementById('hudStructure');

if (heroSneakerCard) {
  // Mouse Enter
  heroSneakerCard.addEventListener('mouseenter', () => {
    if (hoverText) hoverText.textContent = "DESMONTADO // ANATOMIA REVELADA";
    if (hudStructure) {
      hudStructure.textContent = "Desmontado (Exploded)";
      hudStructure.style.color = "var(--accent-cyan)";
    }
  });

  // Mouse Leave
  heroSneakerCard.addEventListener('mouseleave', () => {
    heroSneakerCard.classList.remove('dismantled');
    if (hoverText) hoverText.textContent = "PASSE O MOUSE PARA DESMONTAR O TÊNIS";
    if (hudStructure) {
      hudStructure.textContent = "Original Montado";
      hudStructure.style.color = "#fff";
    }
  });

  // Click/Touch Toggle (para celular)
  heroSneakerCard.addEventListener('click', () => {
    const isDismantled = heroSneakerCard.classList.toggle('dismantled');
    if (hoverText) {
      hoverText.textContent = isDismantled ? "DESMONTADO // TOQUE PARA MONTAR" : "PASSE O MOUSE PARA DESMONTAR O TÊNIS";
    }
    if (hudStructure) {
      hudStructure.textContent = isDismantled ? "Desmontado (Exploded)" : "Original Montado";
      hudStructure.style.color = isDismantled ? "var(--accent-cyan)" : "#fff";
    }
  });
}

// 4. FAQ Accordion
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

console.log("Paty Tênis Club interativo carregado com sucesso.");
"""

with open("app.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Generated clean app.js successfully!")
