import os

# Append or rewrite styles for rules, wishlist, and contract terms
with open("style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

terms_and_wishlist_css = """
/* Rules Grid */
.rules-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.rule-box {
  padding: 20px 16px;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--border-subtle);
  transition: transform 0.2s, border-color 0.2s;
}

.rule-box:hover {
  transform: translateY(-3px);
  border-color: rgba(0, 240, 255, 0.3);
}

.rule-icon-box {
  font-size: 24px;
  margin-bottom: 10px;
}

.rule-box h3 {
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 8px;
  line-height: 1.3;
}

.rule-box p {
  font-size: 12.5px;
  color: var(--text-muted);
  line-height: 1.5;
}

/* Wishlist Status Card */
.wishlist-status-card {
  max-width: 680px;
  margin: 18px auto 0;
  padding: 16px 20px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  align-items: center;
  text-align: center;
  border: 1px solid rgba(0, 240, 255, 0.3);
  background: rgba(14, 18, 28, 0.85);
  box-shadow: 0 10px 25px rgba(0,0,0,0.5);
  transition: all 0.3s;
}

.wishlist-status-card.ready {
  border-color: rgba(0, 255, 157, 0.5);
  box-shadow: 0 0 25px rgba(0, 255, 157, 0.2);
}

.wishlist-status-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.wishlist-counter-label {
  font-size: 11px;
  font-weight: 800;
  color: var(--accent-cyan);
  letter-spacing: 0.08em;
}

.wishlist-counter-badge {
  font-size: 13px;
  font-weight: 700;
  color: #fff;
}

.wishlist-counter-badge strong {
  font-size: 18px;
  font-family: var(--font-display);
  color: var(--accent-cyan);
}

.wishlist-status-card.ready .wishlist-counter-badge strong {
  color: var(--accent-green);
}

.wishlist-status-msg {
  font-size: 12px;
  color: var(--text-muted);
}

/* Card Selection State */
.sneaker-card.selected {
  border-color: rgba(0, 255, 157, 0.5);
  box-shadow: 0 10px 25px rgba(0,0,0,0.6), 0 0 20px rgba(0, 255, 157, 0.15);
}

.btn-card-select.selected {
  background: rgba(0, 255, 157, 0.2);
  color: var(--accent-green);
  border-color: rgba(0, 255, 157, 0.5);
}

/* Contract Terms & Acceptance */
.contract-terms-box {
  background: rgba(10, 13, 20, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-md);
  padding: 18px;
  margin: 20px 0 16px;
  text-align: left;
}

.contract-terms-box h4 {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: var(--accent-gold);
  margin-bottom: 10px;
}

.terms-scroll-area {
  max-height: 130px;
  overflow-y: auto;
  padding-right: 8px;
  margin-bottom: 14px;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 10px;
}

.terms-scroll-area p {
  font-size: 11px;
  color: var(--text-muted);
  line-height: 1.5;
  margin-bottom: 8px;
}

.terms-scroll-area strong {
  color: #f1f5f9;
}

.terms-accept-label {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}

.terms-checkbox {
  width: 18px;
  height: 18px;
  accent-color: var(--accent-cyan);
  cursor: pointer;
  margin-top: 2px;
  flex-shrink: 0;
}

.terms-text {
  font-size: 12px;
  color: #f8fafc;
  line-height: 1.4;
}

.terms-warning-hint {
  text-align: center;
  font-size: 11px;
  color: #fbbf24;
  margin-top: 10px;
  transition: opacity 0.2s;
}

button:disabled {
  opacity: 0.45;
  cursor: not-allowed;
  filter: grayscale(0.8);
  box-shadow: none !important;
}

@media (max-width: 1024px) {
  .rules-grid { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 768px) {
  .rules-grid { grid-template-columns: 1fr; }
}
"""

if ".rules-grid" not in css_content:
    with open("style.css", "a", encoding="utf-8") as f:
        f.write("\n" + terms_and_wishlist_css)
    print("style.css updated with terms and wishlist styles.")
else:
    print("style.css already has rules-grid.")
