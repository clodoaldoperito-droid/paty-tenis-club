// PATY TENIS CLUB - INTERACTIVE SCRIPT

// 1. Data Dictionary for the 3D Exploded View Components
const specData = {
  laces: {
    title: "Cadar?os Tran?ados & L?ngua Ergon?mica",
    badge: "Ajuste & Firmeza",
    description: "Sistema de amarra??o de alta densidade com passadores refor?ados e l?ngua acolchoada com malha respir?vel para prevenir pontos de press?o no peito do p?.",
    val1: "100%",
    lbl1: "Ajuste Anat?mico",
    val2: "Zero",
    lbl2: "Pontos de Press?o"
  },
  upper: {
    title: "Cabedal em Couro Premium Perfurado",
    badge: "Durabilidade & Respira??o",
    description: "Confeccionado com couro leg?timo selecionado e micro-perfura??es a laser que garantem circula??o cont?nua de ar, mantendo os p?s sempre secos e confort?veis.",
    val1: "Grade A",
    lbl1: "Couro Leg?timo",
    val2: "360?",
    lbl2: "Ventila??o Cont?nua"
  },
  insole: {
    title: "Palmilha Ergon?mica Memory Foam",
    badge: "Conforto Ortop?dico",
    description: "Espuma viscoel?stica de densidade balanceada que se molda ? curvatura ?nica da sua pisada, eliminando o cansa?o mesmo ap?s longas horas de caminhada.",
    val1: "8mm",
    lbl1: "Espessura Memory",
    val2: "-42%",
    lbl2: "Impacto no Calcanhar"
  },
  shank: {
    title: "Placa Carbon Shank Antitor??o",
    badge: "Estabilidade Torsional",
    description: "Estrutura r?gida de fibra de carbono aeroespacial embutida no mediop?, impedindo tor??es articulares e garantindo firmeza em qualquer mudan?a brusca de dire??o.",
    val1: "Carbon",
    lbl1: "Fibra Aeroespacial",
    val2: "100%",
    lbl2: "Firmeza na Pisada"
  },
  air: {
    title: "C?mara de Ar Aether-Flow 720",
    badge: "Propuls?o & Absor??o",
    description: "C?psula transl?cida pressurizada com g?s inerte que absorve 99% da for?a do impacto e devolve como impulso el?stico na passada.",
    val1: "+35%",
    lbl1: "Retorno de Energia",
    val2: "Dual-Air",
    lbl2: "Absor??o Cont?nua"
  },
  outsole: {
    title: "Solado de Borracha Tracionada Ultra-Grip",
    badge: "Ader?ncia Urbana",
    description: "Composto de borracha vulcanizada com ranhuras geom?tricas projetadas para ader?ncia m?xima no asfalto, cal?adas molhadas ou piso de academia.",
    val1: "Ultra-Grip",
    lbl1: "Tra??o 360?",
    val2: "3x Mais",
    lbl2: "Resist?ncia ao Desgaste"
  }
};

// 2. Interactive Hotspot Setup
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

// 3. 3D Tilt Effect on Hero Card
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
    
    heroCard.style.transform = perspective(1000px) rotateX(deg) rotateY(deg) scale3d(1.02, 1.02, 1.02);
  });
  
  heroCard.addEventListener('mouseleave', () => {
    heroCard.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
  });
}

// 4. Catalog Models Data (Sincronizado com a Planilha de Estoque)
const catalogData = [
  { brand: "ADIDAS", model: "Samba", category: "Cl?ssicos / Streets / Academia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Superstar", category: "Cl?ssicos / Streets / Academia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Gazelle", category: "Cl?ssicos / Streets / Academia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Campus", category: "Cl?ssicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Forum", category: "Cl?ssicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Stan Smith", category: "Cl?ssicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Ozweego", category: "Cl?ssicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "NMD", category: "Cl?ssicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "ADIDAS", model: "Ultraboost", category: "Corrida / Treino / Conforto Extremo", sizes: "35 a 45", price: 290, type: "Corrida" },
  { brand: "ADIDAS", model: "Adizero", category: "Corrida / Treino / Alta Performance", sizes: "35 a 45", price: 290, type: "Corrida" },
  { brand: "ADIDAS", model: "Supernova", category: "Corrida / Treino / Conforto Di?rio", sizes: "35 a 45", price: 290, type: "Corrida" },
  { brand: "ADIDAS", model: "Adistar", category: "Corrida / Treino / Longas Dist?ncias", sizes: "35 a 45", price: 290, type: "Corrida" },
  { brand: "NIKE", model: "Air Force 1", category: "Cl?ssicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Dunk Low", category: "Cl?ssicos / Streets / Dia a dia", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Air Max 90", category: "AIR MAX / Streets / Estilo", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Air Max 95", category: "AIR MAX / Streets / Conforto", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Air Max 97", category: "AIR MAX / Streets / Futurista", sizes: "35 a 45", price: 290, type: "Streets" },
  { brand: "NIKE", model: "Pegasus", category: "Corrida / Treino / Amortecimento R?pido", sizes: "35 a 45", price: 290, type: "Corrida" }
];

const catalogGrid = document.getElementById('catalogGrid');

function renderCatalog(items) {
  if (!catalogGrid) return;
  catalogGrid.innerHTML = items.map(item => 
    <div class="sneaker-card">
      <div>
        <span class="card-brand-badge"></span>
        <h4 class="card-title"> </h4>
        <p class="card-category"></p>
        <div class="card-sizes">
          <span class="size-pill available">Grade </span>
          <span class="size-pill available">Dispon?vel no Box</span>
        </div>
      </div>
      <div class="card-footer">
        <div>
          <span class="card-price-ref">Valor avulso ref.</span>
          <div class="card-price-val">R$ ,00</div>
        </div>
        <a href="#planos" class="btn-card-select">Incluir no Box</a>
      </div>
    </div>
  ).join('');
}

// Initial render
renderCatalog(catalogData);

// 5. Filter Buttons Logic
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

// 6. FAQ Accordion Logic
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

console.log("Paty T?nis Club script initialized successfully.");