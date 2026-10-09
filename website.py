<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>SSP · Royal Earth Produce | Wholesale & Retail</title>
  <!-- Google Fonts: Cinzel (headings), Playfair Display (secondary headings), Plus Jakarta Sans (body) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 (free) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <style>
    /* ---------- RESET & BASE ---------- */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
    }

    body {
      background-color: #0A0F1D;
      color: #F8F9FA;
      font-family: 'Plus Jakarta Sans', sans-serif;
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* ---------- TYPOGRAPHY ---------- */
    h1, h2, h3, h4, .serif-lux {
      font-family: 'Cinzel', 'Playfair Display', serif;
      font-weight: 600;
      letter-spacing: 0.02em;
    }

    h2 {
      font-size: clamp(2rem, 5vw, 3.2rem);
      background: linear-gradient(135deg, #F3E5AB 0%, #D4AF37 40%, #E0A96D 80%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      display: inline-block;
    }

    .section-subtitle {
      font-size: 1rem;
      text-transform: uppercase;
      letter-spacing: 4px;
      color: #C5A059;
      font-weight: 400;
      margin-bottom: 0.75rem;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* ---------- COLORS & UTILITIES ---------- */
    .gold-text {
      color: #D4AF37;
    }
    .champagne-text {
      color: #F3E5AB;
    }
    .copper-text {
      color: #E0A96D;
    }
    .bg-navy {
      background-color: #0A0F1D;
    }
    .bg-obsidian {
      background-color: #121624;
    }
    .glass-panel {
      background: rgba(18, 22, 36, 0.65);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(212, 175, 55, 0.2);
      border-radius: 24px;
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(212, 175, 55, 0.1) inset;
    }

    /* Gold divider */
    .gold-divider {
      width: 100px;
      height: 2px;
      background: linear-gradient(90deg, transparent, #D4AF37, #E0A96D, #D4AF37, transparent);
      margin: 1.5rem auto;
    }

    .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 2rem;
    }

    /* ---------- BUTTONS ---------- */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      padding: 0.9rem 2.2rem;
      border-radius: 50px;
      font-weight: 600;
      font-size: 0.95rem;
      text-decoration: none;
      transition: all 0.3s cubic-bezier(0.2, 0.9, 0.4, 1);
      cursor: pointer;
      border: none;
      letter-spacing: 0.5px;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .btn-gold {
      background: linear-gradient(145deg, #D4AF37, #E0A96D);
      color: #0A0F1D;
      box-shadow: 0 8px 20px -6px rgba(212, 175, 55, 0.4);
      border: 1px solid rgba(243, 229, 171, 0.5);
    }

    .btn-gold:hover {
      background: linear-gradient(145deg, #E0A96D, #F3E5AB);
      box-shadow: 0 12px 28px -6px rgba(212, 175, 55, 0.7);
      transform: translateY(-3px);
    }

    .btn-outline-gold {
      background: transparent;
      border: 1.5px solid rgba(212, 175, 55, 0.7);
      color: #F3E5AB;
    }

    .btn-outline-gold:hover {
      background: rgba(212, 175, 55, 0.1);
      border-color: #F3E5AB;
      transform: translateY(-3px);
      box-shadow: 0 8px 20px -8px rgba(212, 175, 55, 0.5);
    }

    .btn-whatsapp {
      background: #25D366;
      color: #0A0F1D;
      border: 1px solid rgba(255, 255, 255, 0.3);
    }

    .btn-whatsapp:hover {
      background: #2ee077;
      transform: translateY(-3px);
      box-shadow: 0 10px 25px -5px rgba(37, 211, 102, 0.5);
    }

    /* ---------- HEADER / NAV ---------- */
    header {
      position: sticky;
      top: 0;
      z-index: 999;
      background: rgba(10, 15, 29, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(212, 175, 55, 0.25);
      padding: 0.9rem 0;
    }

    .nav-container {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .logo {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
    }

    .logo-icon {
      font-size: 2rem;
      color: #D4AF37;
      filter: drop-shadow(0 0 6px rgba(212, 175, 55, 0.7));
    }

    .logo-text {
      font-family: 'Cinzel', serif;
      font-weight: 700;
      font-size: 2rem;
      letter-spacing: 2px;
      background: linear-gradient(135deg, #F3E5AB, #D4AF37, #E0A96D);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      line-height: 1;
    }

    .logo-sub {
      font-size: 0.6rem;
      letter-spacing: 3px;
      color: #C5A059;
      text-transform: uppercase;
      font-weight: 400;
    }

    .nav-links {
      display: flex;
      gap: 2.2rem;
      align-items: center;
      list-style: none;
    }

    .nav-links a {
      color: #F8F9FA;
      text-decoration: none;
      font-weight: 400;
      font-size: 0.95rem;
      transition: color 0.2s;
      letter-spacing: 0.5px;
      position: relative;
    }

    .nav-links a::after {
      content: '';
      position: absolute;
      bottom: -6px;
      left: 0;
      width: 0;
      height: 1.5px;
      background: #D4AF37;
      transition: width 0.3s;
    }

    .nav-links a:hover {
      color: #D4AF37;
    }

    .nav-links a:hover::after {
      width: 100%;
    }

    .nav-actions {
      display: flex;
      gap: 1rem;
      align-items: center;
    }

    .mobile-menu-btn {
      display: none;
      font-size: 1.8rem;
      color: #D4AF37;
      background: none;
      border: none;
      cursor: pointer;
    }

    /* Mobile nav */
    .mobile-nav {
      display: none;
      flex-direction: column;
      background: rgba(10, 15, 29, 0.98);
      backdrop-filter: blur(20px);
      padding: 1.5rem 2rem;
      border-bottom: 1px solid rgba(212, 175, 55, 0.3);
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      z-index: 998;
    }

    .mobile-nav.active {
      display: flex;
    }

    .mobile-nav a {
      color: #F8F9FA;
      text-decoration: none;
      padding: 0.9rem 0;
      border-bottom: 1px solid rgba(212, 175, 55, 0.15);
      font-size: 1.1rem;
      transition: color 0.2s;
    }

    .mobile-nav a:hover {
      color: #D4AF37;
    }

    /* ---------- HERO ---------- */
    .hero {
      min-height: 90vh;
      display: flex;
      align-items: center;
      position: relative;
      overflow: hidden;
      padding: 4rem 0;
    }

    .hero::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at 70% 30%, rgba(212, 175, 55, 0.08) 0%, transparent 60%),
                  radial-gradient(circle at 20% 80%, rgba(224, 169, 109, 0.06) 0%, transparent 50%);
      pointer-events: none;
    }

    .hero-content {
      position: relative;
      z-index: 2;
      max-width: 750px;
    }

    .hero h1 {
      font-size: clamp(2.8rem, 6vw, 5rem);
      font-weight: 700;
      line-height: 1.15;
      margin-bottom: 1.5rem;
      background: linear-gradient(135deg, #F8F9FA 0%, #F3E5AB 45%, #D4AF37 70%, #E0A96D 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    .hero p {
      font-size: 1.2rem;
      color: #C5A059;
      margin-bottom: 2.5rem;
      max-width: 600px;
      font-weight: 300;
    }

    .hero-cta {
      display: flex;
      flex-wrap: wrap;
      gap: 1.2rem;
      margin-bottom: 4rem;
    }

    .stats-row {
      display: flex;
      flex-wrap: wrap;
      gap: 2.5rem;
      border-top: 1px solid rgba(212, 175, 55, 0.3);
      padding-top: 2rem;
    }

    .stat-item h3 {
      font-family: 'Cinzel', serif;
      font-size: 2rem;
      font-weight: 700;
      color: #D4AF37;
      margin-bottom: 0.2rem;
    }

    .stat-item p {
      font-size: 0.9rem;
      color: #C5A059;
      text-transform: uppercase;
      letter-spacing: 2px;
      margin: 0;
    }

    /* ---------- SECTION STYLING ---------- */
    section {
      padding: 5rem 0;
      position: relative;
    }

    .section-header {
      text-align: center;
      margin-bottom: 3.5rem;
    }

    /* ---------- PRODUCT TABS ---------- */
    .product-tabs {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 3rem;
    }

    .tab-btn {
      background: transparent;
      border: 1px solid rgba(212, 175, 55, 0.4);
      color: #C5A059;
      padding: 0.6rem 1.8rem;
      border-radius: 40px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 500;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.3s;
      letter-spacing: 0.5px;
    }

    .tab-btn.active, .tab-btn:hover {
      background: rgba(212, 175, 55, 0.15);
      border-color: #D4AF37;
      color: #F3E5AB;
      box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }

    /* ---------- PRODUCT CARDS ---------- */
    .products-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
    }

    .product-card {
      background: rgba(18, 22, 36, 0.75);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(212, 175, 55, 0.2);
      border-radius: 24px;
      overflow: hidden;
      transition: all 0.4s cubic-bezier(0.2, 0.9, 0.4, 1);
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .product-card:hover {
      transform: translateY(-8px) scale(1.01);
      border-color: rgba(212, 175, 55, 0.8);
      box-shadow: 0 25px 40px -15px rgba(212, 175, 55, 0.3), 0 0 0 1px rgba(212, 175, 55, 0.2);
    }

    .product-img {
      height: 220px;
      background-size: cover;
      background-position: center;
      position: relative;
      border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    }

    .product-badge {
      position: absolute;
      top: 1rem;
      left: 1rem;
      background: rgba(10, 15, 29, 0.8);
      backdrop-filter: blur(4px);
      padding: 0.4rem 1rem;
      border-radius: 30px;
      font-size: 0.75rem;
      font-weight: 600;
      color: #F3E5AB;
      border: 1px solid rgba(212, 175, 55, 0.6);
      letter-spacing: 1px;
    }

    .product-info {
      padding: 1.5rem;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .product-name {
      font-family: 'Cinzel', serif;
      font-size: 1.4rem;
      font-weight: 600;
      color: #F3E5AB;
      margin-bottom: 0.2rem;
    }

    .product-grade {
      font-size: 0.8rem;
      color: #D4AF37;
      text-transform: uppercase;
      letter-spacing: 1.5px;
    }

    .product-modes {
      display: flex;
      gap: 0.6rem;
      margin: 0.5rem 0;
      flex-wrap: wrap;
    }

    .mode-tag {
      background: rgba(212, 175, 55, 0.15);
      border: 1px solid rgba(212, 175, 55, 0.3);
      color: #C5A059;
      font-size: 0.7rem;
      padding: 0.25rem 0.8rem;
      border-radius: 20px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .product-card .btn {
      margin-top: auto;
      width: 100%;
      padding: 0.75rem;
      font-size: 0.85rem;
      gap: 0.5rem;
    }

    /* ---------- ADVANTAGE / COMPARISON ---------- */
    .advantage-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
      margin-top: 2rem;
    }

    .advantage-card {
      background: rgba(18, 22, 36, 0.6);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(212, 175, 55, 0.2);
      border-radius: 20px;
      padding: 2rem 1.5rem;
      text-align: center;
      transition: all 0.3s;
    }

    .advantage-card:hover {
      border-color: rgba(212, 175, 55, 0.6);
      transform: translateY(-5px);
      background: rgba(18, 22, 36, 0.9);
    }

    .advantage-card i {
      font-size: 2.5rem;
      color: #D4AF37;
      margin-bottom: 1.2rem;
    }

    .advantage-card h4 {
      font-family: 'Cinzel', serif;
      font-size: 1.2rem;
      color: #F3E5AB;
      margin-bottom: 0.8rem;
    }

    .advantage-card p {
      color: #C5A059;
      font-size: 0.95rem;
      font-weight: 300;
    }

    /* ---------- WHY SSP ---------- */
    .why-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 2rem;
    }

    .why-card {
      text-align: center;
      padding: 2rem 1rem;
      border-radius: 16px;
      transition: all 0.3s;
      border: 1px solid transparent;
    }

    .why-card:hover {
      background: rgba(212, 175, 55, 0.05);
      border-color: rgba(212, 175, 55, 0.3);
    }

    .why-card i {
      font-size: 2.2rem;
      color: #E0A96D;
      margin-bottom: 1rem;
    }

    .why-card h4 {
      font-family: 'Cinzel', serif;
      font-size: 1.1rem;
      color: #F3E5AB;
      margin-bottom: 0.5rem;
    }

    .why-card p {
      color: #C5A059;
      font-size: 0.9rem;
    }

    /* ---------- CALCULATOR ---------- */
    .calculator-panel {
      max-width: 800px;
      margin: 0 auto;
      padding: 2.5rem;
    }

    .calc-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }

    .calc-group {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .calc-group label {
      font-size: 0.85rem;
      color: #C5A059;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-weight: 500;
    }

    .calc-group select, .calc-group input {
      background: rgba(10, 15, 29, 0.8);
      border: 1px solid rgba(212, 175, 55, 0.3);
      border-radius: 12px;
      padding: 0.9rem 1.2rem;
      color: #F8F9FA;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 1rem;
      outline: none;
      transition: border 0.3s;
      width: 100%;
    }

    .calc-group select:focus, .calc-group input:focus {
      border-color: #D4AF37;
      box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.1);
    }

    .calc-group select option {
      background: #0A0F1D;
    }

    .calc-actions {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
      margin-top: 1rem;
    }

    /* ---------- CONTACT & FOOTER ---------- */
    .contact-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
    }

    .contact-form {
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
    }

    .contact-form input, .contact-form select, .contact-form textarea {
      background: rgba(10, 15, 29, 0.8);
      border: 1px solid rgba(212, 175, 55, 0.3);
      border-radius: 12px;
      padding: 1rem 1.2rem;
      color: #F8F9FA;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.95rem;
      outline: none;
      transition: border 0.3s;
    }

    .contact-form input:focus, .contact-form select:focus, .contact-form textarea:focus {
      border-color: #D4AF37;
    }

    .contact-form textarea {
      min-height: 120px;
      resize: vertical;
    }

    .contact-info {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      justify-content: center;
    }

    .info-item {
      display: flex;
      gap: 1.2rem;
      align-items: flex-start;
    }

    .info-item i {
      font-size: 1.5rem;
      color: #D4AF37;
      width: 40px;
      text-align: center;
    }

    .info-item h5 {
      font-family: 'Cinzel', serif;
      color: #F3E5AB;
      font-size: 1rem;
      margin-bottom: 0.2rem;
    }

    .info-item p {
      color: #C5A059;
      font-size: 0.9rem;
    }

    footer {
      background: #070B14;
      border-top: 1px solid rgba(212, 175, 55, 0.2);
      padding: 3rem 0 1.5rem;
      margin-top: 2rem;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1.5fr;
      gap: 2rem;
      margin-bottom: 2.5rem;
    }

    .footer-col h5 {
      font-family: 'Cinzel', serif;
      color: #D4AF37;
      font-size: 1.1rem;
      margin-bottom: 1.2rem;
      letter-spacing: 1px;
    }

    .footer-col a, .footer-col p {
      display: block;
      color: #C5A059;
      text-decoration: none;
      font-size: 0.9rem;
      margin-bottom: 0.6rem;
      transition: color 0.2s;
      font-weight: 300;
    }

    .footer-col a:hover {
      color: #F3E5AB;
    }

    .footer-bottom {
      border-top: 1px solid rgba(212, 175, 55, 0.15);
      padding-top: 1.5rem;
      text-align: center;
      color: #C5A059;
      font-size: 0.85rem;
    }

    /* ---------- WHATSAPP FLOATING BUTTON ---------- */
    .whatsapp-float {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: #25D366;
      color: #0A0F1D;
      width: 60px;
      height: 60px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2rem;
      box-shadow: 0 8px 25px rgba(37, 211, 102, 0.5);
      z-index: 1000;
      transition: all 0.3s;
      text-decoration: none;
      border: 2px solid rgba(255, 255, 255, 0.3);
    }

    .whatsapp-float:hover {
      transform: scale(1.1);
      box-shadow: 0 12px 30px rgba(37, 211, 102, 0.8);
      background: #2ee077;
    }

    /* ---------- RESPONSIVE ---------- */
    @media (max-width: 1024px) {
      .footer-grid {
        grid-template-columns: 1fr 1fr;
      }
      .contact-grid {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 768px) {
      .nav-links, .nav-actions .btn {
        display: none;
      }
      .mobile-menu-btn {
        display: block;
      }
      .hero h1 {
        font-size: 2.5rem;
      }
      .stats-row {
        gap: 1.5rem;
      }
      .calc-row {
        grid-template-columns: 1fr;
      }
      .footer-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
      }
      .container {
        padding: 0 1.5rem;
      }
      .whatsapp-float {
        width: 50px;
        height: 50px;
        font-size: 1.6rem;
        bottom: 1.5rem;
        right: 1.5rem;
      }
      .hero-cta {
        flex-direction: column;
        align-items: stretch;
      }
      .hero-cta .btn {
        width: 100%;
      }
    }

    @media (min-width: 1920px) {
      .container {
        max-width: 1600px;
      }
      html {
        font-size: 18px;
      }
    }
  </style>
</head>
<body>

<!-- ========== HEADER / NAVIGATION ========== -->
<header>
  <div class="container nav-container">
    <!-- Brand logo -->
    <a href="#" class="logo">
      <i class="fas fa-crown logo-icon"></i>
      <div>
        <div class="logo-text">SSP</div>
        <div class="logo-sub">Wholesale & Retail</div>
      </div>
    </a>

    <!-- Desktop navigation -->
    <ul class="nav-links">
      <li><a href="#home">Home</a></li>
      <li><a href="#products">Products</a></li>
      <li><a href="#wholesale">Wholesale Inquiry</a></li>
      <li><a href="#why">Why SSP</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>

    <!-- Desktop action button + hamburger -->
    <div class="nav-actions">
      <a href="#calculator" class="btn btn-gold" style="padding: 0.7rem 1.6rem; font-size: 0.85rem;">Get Wholesale Quote</a>
      <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Menu">
        <i class="fas fa-bars"></i>
      </button>
    </div>
  </div>

  <!-- Mobile navigation dropdown -->
  <div class="mobile-nav" id="mobileNav">
    <a href="#home">Home</a>
    <a href="#products">Products</a>
    <a href="#wholesale">Wholesale Inquiry</a>
    <a href="#why">Why SSP</a>
    <a href="#contact">Contact</a>
    <a href="#calculator" style="color:#D4AF37; font-weight:600;">Get Wholesale Quote</a>
  </div>
</header>

<main>
  <!-- ========== HERO SECTION ========== -->
  <section id="home" class="hero">
    <div class="container hero-content">
      <p class="section-subtitle" style="margin-bottom: 1rem;">Premium Royal Earth Produce</p>
      <h1>Elevating Nature’s Finest Yield to Royal Perfection</h1>
      <p>Wholesale scale, farm freshness, uncompromised quality — direct from the heart of India’s finest farms to your business. Trusted supply chain for onions, shallots, garlic, ginger, and potatoes.</p>
      <div class="hero-cta">
        <a href="#products" class="btn btn-gold"><i class="fas fa-leaf"></i> Explore Products</a>
        <a href="https://wa.me/919876543210?text=Hello%20SSP%2C%20I%20would%20like%20to%20make%20a%20direct%20wholesale%20inquiry." target="_blank" class="btn btn-outline-gold"><i class="fab fa-whatsapp"></i> Direct WhatsApp Inquiry</a>
      </div>
      <!-- Key stats counter -->
      <div class="stats-row">
        <div class="stat-item">
          <h3>50,000+</h3>
          <p>Tons Supplied</p>
        </div>
        <div class="stat-item">
          <h3>100%</h3>
          <p>Quality Inspected</p>
        </div>
        <div class="stat-item">
          <h3>10+</h3>
          <p>Years Trust</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========== PRODUCT SHOWCASE ========== -->
  <section id="products" class="bg-obsidian">
    <div class="container">
      <div class="section-header">
        <p class="section-subtitle">Our Royal Selection</p>
        <h2>Handpicked for Excellence</h2>
        <div class="gold-divider"></div>
        <p style="color: #C5A059; max-width: 700px; margin: 0 auto;">Grade-A produce available in wholesale bulk and retail select packs. Every lot is inspected for perfection.</p>
      </div>

      <!-- Filter tabs -->
      <div class="product-tabs" id="productTabs">
        <button class="tab-btn active" data-filter="all">All</button>
        <button class="tab-btn" data-filter="wholesale">Wholesale Bulk</button>
        <button class="tab-btn" data-filter="retail">Retail Select</button>
      </div>

      <!-- Product grid -->
      <div class="products-grid" id="productsGrid">
        <!-- Big Onion -->
        <div class="product-card" data-category="wholesale retail">
          <div class="product-img" style="background-image: url('https://images.unsplash.com/photo-1518977676601-b53f82aba655?q=80&w=800&auto=format&fit=crop');">
            <span class="product-badge">Grade A Export</span>
          </div>
          <div class="product-info">
            <h3 class="product-name">Big Onion</h3>
            <p class="product-grade">Grade-A Export & Domestic Quality</p>
            <div class="product-modes">
              <span class="mode-tag">Wholesale Bags</span>
              <span class="mode-tag">Retail Packs</span>
            </div>
            <button class="btn btn-gold enquire-btn" data-product="Big Onion">
              <i class="fab fa-whatsapp"></i> Enquire Price / Bulk Order
            </button>
          </div>
        </div>

        <!-- Small Onion / Shallots -->
        <div class="product-card" data-category="wholesale retail">
          <div class="product-img" style="background-image: url('https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?q=80&w=800&auto=format&fit=crop');">
            <span class="product-badge">Hand-picked</span>
          </div>
          <div class="product-info">
            <h3 class="product-name">Small Onion / Shallots</h3>
            <p class="product-grade">South Indian Premium Shallots</p>
            <div class="product-modes">
              <span class="mode-tag">Wholesale Bags</span>
              <span class="mode-tag">Retail Packs</span>
            </div>
            <button class="btn btn-gold enquire-btn" data-product="Small Onion / Shallots">
              <i class="fab fa-whatsapp"></i> Enquire Price / Bulk Order
            </button>
          </div>
        </div>

        <!-- Garlic -->
        <div class="product-card" data-category="wholesale retail">
          <div class="product-img" style="background-image: url('https://images.unsplash.com/photo-1615477550927-6ec6a5c6f6f6?q=80&w=800&auto=format&fit=crop');">
            <span class="product-badge">Bold Clove</span>
          </div>
          <div class="product-info">
            <h3 class="product-name">Garlic</h3>
            <p class="product-grade">Pearl Garlic & Elephant Garlic</p>
            <div class="product-modes">
              <span class="mode-tag">Wholesale Bags</span>
              <span class="mode-tag">Retail Packs</span>
            </div>
            <button class="btn btn-gold enquire-btn" data-product="Garlic">
              <i class="fab fa-whatsapp"></i> Enquire Price / Bulk Order
            </button>
          </div>
        </div>

        <!-- Ginger -->
        <div class="product-card" data-category="wholesale retail">
          <div class="product-img" style="background-image: url('https://images.unsplash.com/photo-1599940824399-b87987ceb72a?q=80&wite