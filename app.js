// PATY TENIS CLUB - INTERACTIVE SCRIPT

const specData = {
  laces: {
    title: "Cadarços Trançados & Língua Ergonômica",
    badge: "Ajuste & Firmeza",
    description: "Sistema de amarração de alta densidade com passadores reforçados e língua acolchoada com malha respirável para prevenir pontos de pressão no peito do pé.",
    val1: "100%",
    lbl1: "Ajuste Anatômico",
    val2: "Zero",
    lbl2: "Pontos de Pressão"
  },
  upper: {
    title: "Cabedal em Couro Premium Perfurado",
    badge: "Durabilidade & Respiração",
    description: "Confeccionado com couro legítimo selecionado e micro-perfurações a laser que garantem circulação contínua de ar, mantendo os pés sempre secos e confortáveis.",
    val1: "Grade A",
    lbl1: "Couro Legítimo",
    val2: "360°",
    lbl2: "Ventilação Contínua"
  },
  insole: {
    title: "Palmilha Ergonômica Memory Foam",
    badge: "Conforto Ortopédico",
    description: "Espuma viscoelástica de densidade balanceada que se molda à curvatura única da sua pisada, eliminando o cansaço mesmo após longas horas de caminhada.",
    val1: "8mm",
    lbl1: "Espessura Memory",
    val2: "-42%",
    lbl2: "Impacto no Calcanhar"
  },
  shank: {
    title: "Placa Carbon Shank Antitorção",
    badge: "Estabilidade Torsional",
    description: "Estrutura rígida de fibra de carbono aeroespacial embutida no mediopé, impedindo torções articulares e garantindo firmeza em qualquer mudança brusca de direção.",
    val1: "Carbon",
    lbl1: "Fibra Aeroespacial",
    val2: "100%",
    lbl2: "Firmeza na Pisada"
  },
  air: {
    title: "Câmara de Ar Aether-Flow 720",
    badge: "Propulsão & Absorção",
    description: "Cápsula translúcida pressurizada com gás inerte que absorve 99% da força do impacto e devolve como impulso elástico na passada.",
    val1: "+35%",
    lbl1: "Retorno de Energia",
    val2: "Dual-Air",
    lbl2: "Absorção Contínua"
  },
  outsole: {
    title: "Solado de Borracha Tracionada Ultra-Grip",
    badge: "Aderência Urbana",
    description: "Composto de borracha vulcanizada com ranhuras geométricas projetadas para aderência máxima no asfalto, calçadas molhadas ou piso de academia.",
    val1: "Ultra-Grip",
    lbl1: "Tração 360°",
    val2: "3x Mais",
    lbl2: "Resistência ao Desgaste"
  }
};

const pins = document.querySelectorAll('.hotspot-pin');
const specTitle = document.getElementById('specTitle');
const specBadge = document.getElementById('specBadge');
const specDescription = document.getElementById('specDescription');
const specMetric1 = document.getElementById('specMetric1');
const specMetricLabel1 = document.getElementById('specMetricLabel1');
const specMetric2 = document.getElementById('specMetric2');
const specMetricLabel2 = document.getElementById('specMetricLabel2');

pins.forEach(pin => {
  pin.addEventListener('click', () => {
    pins.forEach(p => p.classList.remove('active'));
    pin.classList.add('active');
    
    const targetKey = pin.getAttribute('data-target');
    const data = specData[targetKey];
    if (data) {
      specTitle.textContent = data.title;
      specBadge.textContent = data.badge;
      specDescription.textContent = data.description;
      specMetric1.textContent = data.val1;
      specMetricLabel1.textContent = data.lbl1;
      specMetric2.textContent = data.val2;
      specMetricLabel2.textContent = data.lbl2;
    }
  });
});

const heroCard = document.getElementById('heroCard');
if (heroCard) {
  heroCard.addEventListener('mousemove', (e) => {
    const rect = heroCard.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    
    const rotateX = ((y - centerY) / centerY) * -12;
    const rotateY = ((x - centerX) / centerX) * 12;
    
    heroCard.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
  });
  
  heroCard.addEventListener('mouseleave', () => {
    heroCard.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
  });
}

const catalogData = [
  { brand: "ADIDAS", model: "Samba", category: "Clássicos / Streets / Academia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Superstar", category: "Clássicos / Streets / Academia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Gazelle", category: "Clássicos / Streets / Academia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Campus", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Forum", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Stan Smith", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Ozweego", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "NMD", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Ultraboost", category: "Corrida / Treino / Conforto Extremo", sizes: "35 a 45", price: 290, type: "Corrida" },
  { brand: "ADIDAS", model: "Adizero", category: "Corrida / Treino / Alta Performance", sizes: "35 a 45", price: 290, type: "Corrida" },
  { brand: "ADIDAS", model: "Supernova", category: "Corrida / Treino / Conforto Diário", sizes: "35 a 45", price: 290, type: "Corrida" },
  { brand: "ADIDAS", model: "Adistar", category: "Corrida / Treino / Longas Distâncias", sizes: "35 a 45", price: 290, type: "Corrida" },
  { brand: "NIKE", model: "Air Force 1", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Dunk Low", category: "Clássicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Air Max 90", category: "AIR MAX / Streets / Estilo", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Air Max 95", category: "AIR MAX / Streets / Conforto", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Air Max 97", category: "AIR MAX / Streets / Futurista", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Pegasus", category: "Corrida / Treino / Amortecimento Rápido", sizes: "35 a 45", price: 290, type: "Corrida" }
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
          <span class="size-pill available">Disponível no Box</span>
        </div>
      </div>
      <div class="card-footer">
        <div>
          <span class="card-price-ref">Valor avulso ref.</span>
          <div class="card-price-val">R$ ${item.price},00</div>
        </div>
        <a href="#planos" class="btn-card-select">Incluir no Box</a>
      </div>
    </div>
  `).join('');
}

renderCatalog(catalogData);

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
