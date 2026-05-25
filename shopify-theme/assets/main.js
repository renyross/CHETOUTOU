document.addEventListener('DOMContentLoaded', () => {
    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    const handleScroll = () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
            document.body.classList.add('is-scrolled');
        } else {
            navbar.classList.remove('scrolled');
            document.body.classList.remove('is-scrolled');
        }
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Check on load to prevent jumping on refresh

    // Mobile Menu Toggle
    const mobileToggle = document.getElementById('mobile-toggle');
    const menuCloseBtn = document.getElementById('menu-close-btn');
    const navMenu = document.getElementById('nav-menu');
    const megaMenuParents = document.querySelectorAll('.has-megamenu');

    const toggleMenu = () => {
        const isActive = navMenu.classList.toggle('active');
        mobileToggle.classList.toggle('active');
        document.body.style.overflow = isActive ? 'hidden' : 'auto';
    };

    if (mobileToggle) {
        mobileToggle.addEventListener('click', toggleMenu);
    }

    if (menuCloseBtn) {
        menuCloseBtn.addEventListener('click', toggleMenu);
    }

    // Mega Menu Toggle Logic (Desktop & Mobile)
    megaMenuParents.forEach(item => {
        const link = item.querySelector('.nav-link');
        // Dynamically inject a clickable link and a close button inside the accordion
        const megamenuGrid = item.querySelector('.megamenu-grid');
        if (megamenuGrid && link) {
            if (!megamenuGrid.querySelector('.mobile-collection-header')) {
                // Header container
                const headerContainer = document.createElement('div');
                headerContainer.className = 'mobile-collection-header';
                
                // Collection link
                const mobileLink = document.createElement('a');
                mobileLink.href = link.href;
                mobileLink.className = 'nav-link mobile-collection-link';
                const linkText = link.textContent.trim(); 
                mobileLink.innerHTML = `${linkText}`;
                
                // Close button (X)
                const closeBtn = document.createElement('button');
                closeBtn.className = 'inline-close-btn';
                closeBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>';
                closeBtn.setAttribute('aria-label', 'Fermer la liste');
                
                // Collapse the accordion when the X is clicked
                closeBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    item.classList.remove('active'); 
                });

                headerContainer.appendChild(mobileLink);
                headerContainer.appendChild(closeBtn);
                megamenuGrid.insertBefore(headerContainer, megamenuGrid.firstChild);
            }
        }

        link.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();

            const wasActive = item.classList.contains('active');

            // 1. Close all other menus first
            megaMenuParents.forEach(other => other.classList.remove('active'));

            // 2. Toggle current menu
            if (!wasActive) {
                item.classList.add('active');
            }
        });

        // Prevention: don't close if clicking INSIDE the megamenu content
        const megamenu = item.querySelector('.megamenu');
        if (megamenu) {
            megamenu.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        }
    });

    // Close all menus when clicking anywhere else
    document.addEventListener('click', () => {
        megaMenuParents.forEach(item => item.classList.remove('active'));
    });

    // Hero Carousel Logic
    const heroSlides = document.querySelectorAll('.carousel-slide');
    const heroDots = document.querySelectorAll('.nav-dot');
    const heroPrev = document.querySelector('.nav-arrow.prev');
    const heroNext = document.querySelector('.nav-arrow.next');
    let currentHeroSlide = 0;
    let heroInterval;

    const showHeroSlide = (index) => {
        heroSlides.forEach(slide => slide.classList.remove('active'));
        heroDots.forEach(dot => dot.classList.remove('active'));

        currentHeroSlide = (index + heroSlides.length) % heroSlides.length;
        heroSlides[currentHeroSlide].classList.add('active');
        heroDots[currentHeroSlide].classList.add('active');
        
        // Reset timer
        resetHeroTimer();
    };

    const nextHeroSlide = () => showHeroSlide(currentHeroSlide + 1);
    const prevHeroSlide = () => showHeroSlide(currentHeroSlide - 1);

    const resetHeroTimer = () => {
        clearInterval(heroInterval);
        heroInterval = setInterval(nextHeroSlide, 5000);
    };

    if (heroNext) heroNext.addEventListener('click', nextHeroSlide);
    if (heroPrev) heroPrev.addEventListener('click', prevHeroSlide);
    
    heroDots.forEach((dot, idx) => {
        dot.addEventListener('click', () => showHeroSlide(idx));
    });

    // Start auto-play
    resetHeroTimer();


    // Cart Drawer Logic (Moved up for hoisting)
    const cartBtn = document.getElementById('cart-btn');
    const cartDrawer = document.getElementById('cart-drawer');
    const cartOverlay = document.getElementById('cart-overlay');
    const closeCart = document.getElementById('close-cart');

    const openCart = () => {
        if (cartDrawer && cartOverlay) {
            cartDrawer.classList.add('active');
            cartOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    };

    const closeCartDrawer = () => {
        if (cartDrawer && cartOverlay) {
            cartDrawer.classList.remove('active');
            cartOverlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    };

    if (cartBtn) {
        cartBtn.addEventListener('click', (e) => {
            e.preventDefault();
            openCart();
        });
    }

    if (closeCart) {
        closeCart.addEventListener('click', closeCartDrawer);
    }

    if (cartOverlay) {
        cartOverlay.addEventListener('click', closeCartDrawer);
    }

    // Global Esc listener for both search and cart
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeCartDrawer();
            if (typeof closeSearchOverlay === 'function') closeSearchOverlay();
        }
    });
    // Category Carousel Scroll Logic
    const catPrev = document.getElementById('cat-prev');
    const catNext = document.getElementById('cat-next');
    const catCarousel = document.querySelector('.category-tags-row');

    if (catPrev && catNext && catCarousel) {
        catPrev.addEventListener('click', () => {
            catCarousel.scrollBy({ left: -300, behavior: 'smooth' });
        });

        catNext.addEventListener('click', () => {
            catCarousel.scrollBy({ left: 300, behavior: 'smooth' });
        });
    }

    // Shopping Cart logic (Refactored for dynamic behavior)
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let appliedDiscount = parseFloat(localStorage.getItem('appliedDiscount')) || 0;
    let appliedFreeShipping = localStorage.getItem('appliedFreeShipping') === 'true';
    const cartBadge = document.querySelector('.cart-count');
    const cartItemsContainer = document.querySelector('.cart-items-container');
    const cartEmptyState = document.querySelector('.cart-empty-state');
    const cartTotalAmount = document.getElementById('cart-total-amount');
    const promoInput = document.querySelector('.cart-promo-v3 input');
    const promoBtn = document.querySelector('.btn-promo-apply');

    const updateCartUI = () => {
        const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        if (cartBadge) {
            cartBadge.textContent = totalItems;
            cartBadge.style.display = totalItems > 0 ? 'flex' : 'none';
        }

        renderCart();
        localStorage.setItem('cart', JSON.stringify(cart));
        localStorage.setItem('appliedDiscount', appliedDiscount.toString());
        localStorage.setItem('appliedFreeShipping', appliedFreeShipping.toString());
    };

    const renderCart = () => {
        if (!cartItemsContainer) return;

        if (cart.length === 0) {
            cartItemsContainer.style.display = 'none';
            if (cartEmptyState) cartEmptyState.style.display = 'block';
            if (cartTotalAmount) cartTotalAmount.textContent = '0,00 €';
            return;
        }

        cartItemsContainer.style.display = 'block';
        if (cartEmptyState) cartEmptyState.style.display = 'none';

        cartItemsContainer.innerHTML = cart.map((item, index) => `
            <div class="cart-item-v3" data-index="${index}">
                <div class="cart-item-image">
                    <img src="${item.image}" alt="${item.name}">
                </div>
                <div class="cart-item-details">
                    <div class="cart-item-header">
                        <span class="cart-item-name">${item.name}</span>
                        <button class="remove-item-btn" data-index="${index}">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                <path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                            </svg>
                        </button>
                    </div>
                    ${item.variant ? `<span class="cart-item-variant">${item.variant}</span>` : ''}
                    <div class="cart-item-footer">
                        <span class="cart-item-price">${item.price.toFixed(2).replace('.', ',')} €</span>
                        <div class="cart-qty-selector">
                            <button class="qty-change minus" data-index="${index}">-</button>
                            <span class="qty-number">${item.quantity}</span>
                            <button class="qty-change plus" data-index="${index}">+</button>
                        </div>
                    </div>
                </div>
            </div>
        `).join('');

        const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        const discountAmount = subtotal * appliedDiscount;
        const total = subtotal - discountAmount;

        // Update Total Amount Display
        if (cartTotalAmount) {
            if (appliedDiscount > 0) {
                cartTotalAmount.innerHTML = `
                    <div class="cart-total-display">
                        <span class="cart-subtotal-original">${subtotal.toFixed(2).replace('.', ',')} €</span>
                        <span class="cart-total-final">${total.toFixed(2).replace('.', ',')} €</span>
                        <div class="cart-discount-badge">Remise ${Math.round(appliedDiscount * 100)}% appliquée</div>
                    </div>
                `;
            } else if (appliedFreeShipping) {
                cartTotalAmount.innerHTML = `
                    <div class="cart-total-display">
                        <span class="cart-total-final">${subtotal.toFixed(2).replace('.', ',')} €</span>
                        <div class="cart-discount-badge" style="background: var(--sage); color: #fff;">Livraison gratuite offerte (dès 60€)</div>
                    </div>
                `;
            } else {
                cartTotalAmount.textContent = `${subtotal.toFixed(2).replace('.', ',')} €`;
            }
        }

        // Add event listeners to new elements
        // Add event listeners to new elements
        cartItemsContainer.querySelectorAll('.qty-change').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const idx = parseInt(btn.dataset.index);
                const delta = btn.classList.contains('plus') ? 1 : -1;
                updateQuantity(idx, delta);
            });
        });

        cartItemsContainer.querySelectorAll('.remove-item-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const idx = parseInt(btn.dataset.index);
                removeFromCart(idx);
            });
        });
    };

    const addToCart = (product) => {
        const existingIdx = cart.findIndex(item => item.name === product.name && item.variant === product.variant);
        if (existingIdx > -1) {
            cart[existingIdx].quantity += (product.quantity || 1);
        } else {
            cart.push({ ...product, quantity: product.quantity || 1 });
        }
        updateCartUI();
        openCart(); // Automatically open drawer
    };
    window.addToCart = addToCart; // Expose globally for inline page scripts


    // Promo Code Handler
    if (promoBtn && promoInput) {
        promoBtn.addEventListener('click', () => {
            const code = promoInput.value.trim().toUpperCase();
            
            if (code === 'TOUTOU10') {
                appliedDiscount = 0;
                appliedFreeShipping = true;
                alert('Code TOUTOU10 appliqué ! (Livraison gratuite dès 60€ d\'achat)');
            } else if (code === 'ELYSIUM20') {
                appliedDiscount = 0.20;
                appliedFreeShipping = false;
                alert('Code VIP ELYSIUM20 appliqué ! (20% de remise)');
            } else if (code === '') {
                appliedDiscount = 0;
                appliedFreeShipping = false;
            } else {
                alert('Code de réduction invalide.');
                return;
            }
            
            promoInput.value = '';
            updateCartUI();
        });

        // Also allow Enter key
        promoInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') promoBtn.click();
        });
    }

    const updateQuantity = (index, delta) => {
        cart[index].quantity += delta;
        if (cart[index].quantity <= 0) {
            cart.splice(index, 1);
        }
        updateCartUI();
    };

    const removeFromCart = (index) => {
        cart.splice(index, 1);
        updateCartUI();
    };

    // Global Add to Cart Event for PDP pages
    const pDpAddBtn = document.querySelector('.add-to-cart');
    if (pDpAddBtn) {
        pDpAddBtn.addEventListener('click', () => {
            const productName = document.querySelector('h1.product-title, .product-info-column h1, h1')?.textContent.trim() || 'Produit';
            
            // Priority selectors for main product price
            const priceSelectors = [
                '.product-info-column .product-price-main',
                '.product-info-column .product-price-large',
                '.product-info-column .price-main',
                '.product-price-large',
                '.price-main',
                '.product-price',
                '.price'
            ];
            
            let productPrice = 0;
            for (const selector of priceSelectors) {
                const el = document.querySelector(selector);
                if (el && el.textContent.trim()) {
                    let text = el.textContent.trim();
                    // Remove currency symbols and non-numeric characters except comma and dot
                    let cleanText = text.replace(/[€$£\s]/g, '').replace(',', '.');
                    // Keep only digits and the first dot
                    let numericMatch = cleanText.match(/(\d+\.?\d*)/);
                    if (numericMatch) {
                        const value = parseFloat(numericMatch[0]);
                        if (!isNaN(value) && value > 0) {
                            productPrice = value;
                            break;
                        }
                    }
                }
            }
            
            const productImage = document.querySelector('.gallery-item.main-image img, .product-main-image img')?.src || '';
            const selectedColor = document.querySelector('.swatch-btn.active')?.title || document.querySelector('.preview-btn.active')?.title || '';
            const selectedSize = document.querySelector('.size-btn.active')?.textContent || document.querySelector('.size-btn-v2.active')?.textContent || '';
            const quantityInput = document.getElementById('qty-input-v4') || document.getElementById('qty-input');
            const quantity = parseInt(quantityInput?.value || 1);

            const variantParts = [];
            if (selectedColor) variantParts.push(`Couleur: ${selectedColor}`);
            if (selectedSize) variantParts.push(`Taille: ${selectedSize}`);
            const variant = variantParts.join(' / ');

            addToCart({
                name: productName,
                price: productPrice,
                image: productImage,
                variant: variant,
                quantity: quantity
            });

            // Feedback on button
            const originalText = pDpAddBtn.textContent;
            pDpAddBtn.textContent = 'Ajouté !';
            pDpAddBtn.classList.add('added');
            setTimeout(() => {
                pDpAddBtn.textContent = originalText;
                pDpAddBtn.classList.remove('added');
            }, 2000);
        });
    }

    // Initial load
    updateCartUI();

    // Upsell logic
    const upsellAddBtn = document.querySelector('.btn-upsell-add');
    if (upsellAddBtn) {
        upsellAddBtn.addEventListener('click', () => {
            const giftName = "Boite Cadeau Premium";
            const giftPrice = 0.00;
            const giftImage = "boite_cadeau_premium_1775850265598.png";
            
            addToCart({
                name: giftName,
                price: giftPrice,
                image: giftImage,
                variant: "Cadeau offert",
                quantity: 1
            });
            
            upsellAddBtn.textContent = 'Ajouté';
            upsellAddBtn.disabled = true;
            upsellAddBtn.style.opacity = '0.5';
        });
    }

    // Product Gallery Interactive Zoom + Scroll-to-Zoom
    const mainImages = document.querySelectorAll('.gallery-item.main-image');
    mainImages.forEach(container => {
        const img = container.querySelector('img');
        if (!img) return;

        let currentScale = 2; // Default zoom
        const minScale = 1.5;
        const maxScale = 4;

        container.addEventListener('mousemove', (e) => {
            const rect = container.getBoundingClientRect();
            const x = ((e.clientX - rect.left) / rect.width) * 100;
            const y = ((e.clientY - rect.top) / rect.height) * 100;
            img.style.transformOrigin = `${x}% ${y}%`;
            img.style.transform = `scale(${currentScale})`;
        });

        container.addEventListener('wheel', (e) => {
            e.preventDefault();
            // Scroll up to zoom in, down to zoom out
            const delta = e.deltaY > 0 ? -0.2 : 0.2;
            currentScale = Math.min(Math.max(currentScale + delta, minScale), maxScale);
            img.style.transform = `scale(${currentScale})`;
        }, { passive: false });

        container.addEventListener('mouseleave', () => {
            img.style.transformOrigin = 'center center';
            img.style.transform = 'scale(1)';
            currentScale = 2; // Reset for next hover
        });
    });

    // Scroll reveal effects
    const revealElements = document.querySelectorAll('.hero-content, .hero-image, .featured-product, .story-section');

    const revealOnScroll = () => {
        revealElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            const viewHeight = window.innerHeight;

            if (rect.top < viewHeight * 0.8) {
                el.classList.add('is-revealed');
            }
        });
    };

    // Initial styles for animations
    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
    });

    // Add revelation class in CSS (via JS injection or just manually in CSS later)
    const style = document.createElement('style');
    style.textContent = `
        .is-revealed {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
        .add-to-cart.added {
            background-color: var(--sage);
            border-color: var(--sage);
        }
    `;
    document.head.appendChild(style);

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Run once on load

    // Multi-Carousel Logic (refactored to support multiple instances)
    const carousels = document.querySelectorAll('.incontournables');
    carousels.forEach(container => {
        const track = container.querySelector('.carousel-track');
        const prevBtn = container.querySelector('.prev-btn');
        const nextBtn = container.querySelector('.next-btn');

        if (track && prevBtn && nextBtn) {
            let currentIdx = 0;

            const getVisibleCards = () => {
                if (window.innerWidth <= 600) return 2;
                if (window.innerWidth <= 1024) return 3;
                return 5;
            };

            const updateTrackPosition = () => {
                const cards = track.querySelectorAll('.carousel-card');
                if (cards.length === 0) return;

                const visibleCards = getVisibleCards();
                const containerWidth = track.parentElement.clientWidth;
                const computedStyle = window.getComputedStyle(track);
                const gap = parseFloat(computedStyle.gap) || 24;
                const cardWidth = Math.floor((containerWidth - (visibleCards - 1) * gap) / visibleCards) - 1;

                cards.forEach(card => {
                    card.style.flex = `0 0 ${cardWidth}px`;
                    card.style.width = `${cardWidth}px`;
                });

                const maxIdx = Math.max(0, cards.length - visibleCards);
                if (currentIdx > maxIdx) currentIdx = 0; // Loop or clamp
                if (currentIdx < 0) currentIdx = maxIdx;

                const moveX = currentIdx * (cardWidth + gap);
                track.style.transform = `translateX(-${moveX}px)`;

                updateDots();
            };

            // Carousel Dots Generation
            const dotsContainer = document.createElement('div');
            dotsContainer.className = 'carousel-dots';
            const cards = track.querySelectorAll('.carousel-card');

            const createDots = () => {
                dotsContainer.innerHTML = '';
                const cards = track.querySelectorAll('.carousel-card');
                const visibleCards = getVisibleCards();
                const totalDots = Math.max(0, cards.length - visibleCards + 1);

                for (let i = 0; i < totalDots; i++) {
                    const dot = document.createElement('span');
                    dot.className = 'dot' + (i === currentIdx ? ' active' : '');
                    dot.onclick = () => {
                        currentIdx = i;
                        updateTrackPosition();
                    };
                    dotsContainer.appendChild(dot);
                }
            };

            const updateDots = () => {
                const dots = dotsContainer.querySelectorAll('.dot');
                dots.forEach((dot, idx) => {
                    dot.classList.toggle('active', idx === currentIdx);
                });
            };

            container.querySelector('.carousel-container').appendChild(dotsContainer);
            createDots();
            window.addEventListener('resize', createDots);

            const nextSlide = () => {
                currentIdx++;
                updateTrackPosition();
            };

            const prevSlide = () => {
                currentIdx--;
                updateTrackPosition();
            };

            nextBtn.addEventListener('click', () => nextSlide());
            prevBtn.addEventListener('click', () => prevSlide());

            window.addEventListener('resize', updateTrackPosition);
            setTimeout(updateTrackPosition, 100);

            // Swipe support
            let touchStartX = 0;
            track.addEventListener('touchstart', (e) => touchStartX = e.changedTouches[0].screenX, { passive: true });
            track.addEventListener('touchend', (e) => {
                const touchEndX = e.changedTouches[0].screenX;
                if (touchStartX - touchEndX > 50) nextSlide();
                else if (touchEndX - touchStartX > 50) prevSlide();
            }, { passive: true });
        }
    });

    // Quick add buttons (global)
    const quickAddBtns = document.querySelectorAll('.quick-add');
    quickAddBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();

            const card = btn.closest('.carousel-card') || btn.closest('.product-card') || btn.closest('.rec-card');
            if (card) {
                const name = card.querySelector('h3')?.textContent || 'Produit';
                const priceText = card.querySelector('.price, .rec-price, .product-price-large')?.textContent || '0';
                
                // Robust price parsing
                let cleanText = priceText.replace(/[€$£\s]/g, '').replace(',', '.');
                let numericMatch = cleanText.match(/(\d+\.?\d*)/);
                const price = numericMatch ? parseFloat(numericMatch[0]) : 0;
                
                const image = card.querySelector('img')?.src || '';

                addToCart({
                    name: name,
                    price: price,
                    image: image,
                    quantity: 1
                });
            }

            const originalSvg = btn.innerHTML;
            btn.innerHTML = '✓';
            btn.style.backgroundColor = 'var(--sage)';
            setTimeout(() => {
                btn.innerHTML = originalSvg;
                btn.style.backgroundColor = '';
            }, 1000);
        });
    });

    // FAQ Accordion Logic
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');

                // Close all others
                faqItems.forEach(i => {
                    i.classList.remove('active');
                    const icon = i.querySelector('.faq-icon');
                    if (icon) icon.textContent = '+';
                });

                // Toggle current
                if (!isActive) {
                    item.classList.add('active');
                    const icon = item.querySelector('.faq-icon');
                    if (icon) icon.textContent = '−';
                }
            });
        }
    });

    const viewMoreBtn = id('view-more-btn');
    const seoBody = id('seo-body');
    const introPara = document.querySelector('.intro-large p');
    const viewMoreContainer = document.querySelector('.view-more-container');
    const introLarge = document.querySelector('.intro-large');

    if (viewMoreBtn && seoBody) {
        viewMoreBtn.addEventListener('click', () => {
            const isCollapsed = seoBody.classList.contains('collapsed');
            const catWrapper = document.querySelector('.category-carousel-wrapper');

            if (isCollapsed) {
                // Expanding
                seoBody.classList.remove('collapsed');
                if (introPara) introPara.classList.add('expanded');
                viewMoreBtn.textContent = 'Voir moins';
                
                // Hide filters when expanded
                if (catWrapper) {
                    catWrapper.style.display = 'none';
                }

                // Move button to the bottom of expanded text
                if (viewMoreContainer && seoBody) {
                    seoBody.appendChild(viewMoreContainer);
                }

            } else {
                // Collapsing
                seoBody.classList.add('collapsed');
                if (introPara) introPara.classList.remove('expanded');
                viewMoreBtn.textContent = 'Voir plus';
                
                // Show filters back when collapsed
                if (catWrapper) {
                    catWrapper.style.display = 'flex';
                }

                // Move button back to intro section
                if (viewMoreContainer && introLarge) {
                    introLarge.appendChild(viewMoreContainer);
                }

                // Scroll back to top of the section
                const sectionTop = document.querySelector('.seo-page-section');
                if (sectionTop) {
                    sectionTop.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    }

    function id(name) { return document.getElementById(name); }

    // Product Page Specific Logic
    // Quantity Selector
    const minusBtn = document.querySelector('.qty-trigger.minus, .qty-btn.minus');
    const plusBtn = document.querySelector('.qty-trigger.plus, .qty-btn.plus');
    const qtyInput = document.getElementById('qty-input-v4') || document.getElementById('qty-input');

    if (minusBtn && plusBtn && qtyInput) {
        minusBtn.addEventListener('click', () => {
            let val = parseInt(qtyInput.value);
            if (val > 1) qtyInput.value = val - 1;
        });
        plusBtn.addEventListener('click', () => {
            let val = parseInt(qtyInput.value);
            qtyInput.value = val + 1;
        });
    }

    // Product Accordions
    const pdpAccordions = document.querySelectorAll('.pdp-accordion-v2 .accordion-item, .pdp-accordion-v3 .accordion-item');
    pdpAccordions.forEach(item => {
        const header = item.querySelector('.accordion-header, .accordion-header-v3');
        header.addEventListener('click', () => {
            // Close others
            pdpAccordions.forEach(other => {
                if (other !== item) other.classList.remove('active');
            });
            item.classList.toggle('active');
        });
    });

    // Variant Selectors (Visual only)
    const swatchBtns = document.querySelectorAll('.swatch-btn, .preview-btn');
    swatchBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            swatchBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // Update selected value text if it exists
            const selectedVal = btn.closest('.variant-selector-v2')?.querySelector('.selected-val');
            if (selectedVal && btn.title) {
                selectedVal.textContent = btn.title;
            }
        });
    });

    const sizeBtns = document.querySelectorAll('.size-btn, .size-btn-v2');
    sizeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            sizeBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });

    // Review Modal Logic V3
    const reviewModal = document.getElementById('review-modal');
    const btnWriteReview = document.querySelector('.btn-write-review');
    const closeReviewModal = document.getElementById('close-review-modal');
    const closeReviewModalBtn = document.getElementById('close-review-modal-btn');
    const nextToStep2 = document.getElementById('next-to-step2');
    const backToStep1 = document.getElementById('back-to-step1');
    const submitReview = document.getElementById('submit-review');
    const modalSteps = document.querySelectorAll('.modal-step');
    const starBtnsV3 = document.querySelectorAll('.star-btn-v3');

    if (btnWriteReview && reviewModal) {
        btnWriteReview.addEventListener('click', () => {
            reviewModal.classList.add('active');
            modalSteps.forEach(s => s.classList.remove('active'));
            if (modalSteps.length > 0) modalSteps[0].classList.add('active');
            document.body.style.overflow = 'hidden';
        });

        const closeModal = () => {
            reviewModal.classList.remove('active');
            document.body.style.overflow = '';
        };

        [closeReviewModal, closeReviewModalBtn].forEach(el => {
            if (el) el.addEventListener('click', closeModal);
        });

        reviewModal.addEventListener('click', (e) => {
            if (e.target === reviewModal) closeModal();
        });

        if (nextToStep2) {
            nextToStep2.addEventListener('click', (e) => {
                const reviewContent = document.getElementById('review-text').value;
                if (!reviewContent) {
                    alert('Veuillez écrire votre avis.');
                    return;
                }
                modalSteps[0].classList.remove('active');
                modalSteps[1].classList.add('active');
            });
        }

        if (backToStep1) {
            backToStep1.addEventListener('click', (e) => {
                modalSteps[1].classList.remove('active');
                modalSteps[0].classList.add('active');
            });
        }

        starBtnsV3.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const rating = parseInt(btn.getAttribute('data-rating'));
                starBtnsV3.forEach(s => {
                    const sRating = parseInt(s.getAttribute('data-rating'));
                    if (sRating <= rating) {
                        s.classList.add('active');
                    } else {
                        s.classList.remove('active');
                    }
                });
            });
        });

        if (submitReview) {
            submitReview.addEventListener('click', (e) => {
                const email = document.getElementById('review-email').value;
                const name = document.getElementById('review-name').value;
                if (!email || !name) {
                    alert('Veuillez remplir tous les champs obligatoires.');
                    return;
                }
                alert('Merci pour votre avis ! Il sera publié après modération.');
                closeModal();
            });
        }
    }

    // Filter Dropdown Logic
    const filterTrigger = document.getElementById('filter-trigger');
    const filterDropdown = document.getElementById('filter-dropdown');
    const filterOptions = document.querySelectorAll('.filter-option-v3');
    const currentFilterSpan = document.getElementById('current-filter');

    if (filterTrigger && filterDropdown) {
        filterTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            filterDropdown.classList.toggle('active');
        });

        const sortReviews = (criteria) => {
            const list = document.querySelector('.reviews-list-v3');
            const items = Array.from(list.querySelectorAll('.review-item-v3'));

            items.forEach(item => {
                let shouldShow = false;

                switch (criteria) {
                    case 'Meilleures notes':
                        shouldShow = (item.dataset.rating === '5');
                        break;
                    case 'Notes les plus basses':
                        shouldShow = (parseInt(item.dataset.rating) < 5);
                        break;
                    case 'Plus récents':
                        shouldShow = true; // Show all for default
                        break;
                    case 'Plus utiles':
                        shouldShow = (parseInt(item.dataset.utility) > 10);
                        break;
                    case 'Uniquement les photos':
                    case 'Photos en premier':
                        shouldShow = (item.dataset.media === 'true');
                        break;
                    case 'Vidéos en premier':
                        shouldShow = true; // No videos in sample, so show all
                        break;
                    default:
                        shouldShow = true;
                }

                item.style.display = shouldShow ? 'block' : 'none';
            });
            
            // Re-sort current visible items by date if 'Plus récents' is selected (just in case)
            if (criteria === 'Plus récents') {
                items.sort((a, b) => new Date(b.dataset.date) - new Date(a.dataset.date))
                     .forEach(item => list.appendChild(item));
            }
        };

        filterOptions.forEach(option => {
            option.addEventListener('click', () => {
                const value = option.getAttribute('data-value');
                currentFilterSpan.textContent = value;

                filterOptions.forEach(opt => opt.classList.remove('active'));
                
                // Remove existing check icon from all siblings
                filterOptions.forEach(opt => {
                    const check = opt.querySelector('.check-icon');
                    if (check) check.remove();
                });

                option.classList.add('active');

                // Add check icon to selected option
                const checkSvg = `
                    <svg class="check-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4">
                        <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                `;
                option.insertAdjacentHTML('afterbegin', checkSvg);

                sortReviews(value);
                filterDropdown.classList.remove('active');
            });
        });

        document.addEventListener('click', () => {
            filterDropdown.classList.remove('active');
        });
    }

    // Mobile Filter Drawer Logic
    const mobileFilterBtn = id('mobile-filter-btn');
    const closeFiltersBtn = id('close-filters');
    const filterSidebar = id('collection-sidebar');
    const filterBackdrop = id('filter-backdrop');

    if (mobileFilterBtn && filterSidebar && filterBackdrop) {
        mobileFilterBtn.addEventListener('click', () => {
            filterSidebar.classList.add('active');
            filterBackdrop.classList.add('active');
            document.body.style.overflow = 'hidden';
        });

        const closeFilterDrawer = () => {
            filterSidebar.classList.remove('active');
            filterBackdrop.classList.remove('active');
            document.body.style.overflow = '';
        };

        if (closeFiltersBtn) {
            closeFiltersBtn.addEventListener('click', closeFilterDrawer);
        }

        filterBackdrop.addEventListener('click', closeFilterDrawer);
    }

    // Interactive Product Gallery (Hover to Swap + Sync Scroll)
    const mainImg = document.querySelector('.gallery-item.main-image img');
    const thumbRow = document.querySelector('.thumbnails-row');
    const thumbItems = document.querySelectorAll('.thumbnails-row .gallery-item');
    const dotsContainer = document.querySelector('.gallery-pagination');
    let currentThumbIdx = 0;

    if (mainImg && thumbItems.length > 0) {
        // --- 1. Gallery Navigation Logic ---
        const isDesktop = window.innerWidth > 1024;
        const mainPrev = document.querySelector('.main-arrow.prev');
        const mainNext = document.querySelector('.main-arrow.next');

        const scrollThumbnails = (index) => {
            if (!thumbRow || !isDesktop) return;
            const thumbViewport = document.querySelector('.thumbnails-viewport');
            // Use physical offsetHeight for precision, fallback to 660 only if viewport is missing
            const viewportHeight = thumbViewport ? thumbViewport.offsetHeight : 660;
            const thumbHeight = 80; /* Consistent with CSS */
            const gap = 10; /* Unified gap for perfect consistency */
            const step = thumbHeight + gap;
            
            // The total height the thumbnails row wants to be
            const totalContentHeight = (thumbItems.length * step) - gap;
            const maxScroll = Math.max(0, totalContentHeight - viewportHeight);
            
            let offset = index * step;
            
            // Adjust offset to ensure we don't show whitespace at the bottom
            if (offset > maxScroll) offset = maxScroll;
            
            thumbRow.style.transform = `translateY(-${offset}px)`;
        };

        // --- 2. Gallery Logic ---
        if (dotsContainer) dotsContainer.innerHTML = '';
        thumbItems.forEach((_, idx) => {
            const dot = document.createElement('span');
            dot.className = 'gallery-dot';
            dot.addEventListener('click', () => {
                updateGallery(idx);
            });
            if (dotsContainer) dotsContainer.appendChild(dot);
        });

        const dots = document.querySelectorAll('.gallery-dot');

        const updateGallery = (index) => {
            if (index < 0) index = thumbItems.length - 1;
            if (index >= thumbItems.length) index = 0;
            
            const thumbImg = thumbItems[index].querySelector('img');

            if (thumbImg) {
                mainImg.src = thumbImg.src;
                thumbItems.forEach(t => t.classList.remove('active'));
                thumbItems[index].classList.add('active');
                
                // Update dots
                dots.forEach(d => d.classList.remove('active'));
                if (dots[index]) dots[index].classList.add('active');
                
                // Sync scroll (Vertical)
                scrollThumbnails(index);
                
                currentThumbIdx = index;
            }
        };

        if (mainPrev) mainPrev.addEventListener('click', () => updateGallery(currentThumbIdx - 1));
        if (mainNext) mainNext.addEventListener('click', () => updateGallery(currentThumbIdx + 1));

        thumbItems.forEach((item, index) => {
            item.addEventListener('mouseenter', () => updateGallery(index));
            item.addEventListener('click', () => updateGallery(index));
        });

        // Initial setup
        // Initial setup with small delay to ensure layout is ready
        setTimeout(() => updateGallery(0), 100);
    }

    // Back to Top Logic
    const backToTopBtn = document.getElementById('back-to-top');

    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                backToTopBtn.classList.add('active');
            } else {
                backToTopBtn.classList.remove('active');
            }
        });

        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Generic Multi-Carousel Logic
    const productCarousels = document.querySelectorAll('.product-carousel');
    productCarousels.forEach((carousel, index) => {
        const grid = carousel.querySelector('.carousel-track');
        const prevBtn = carousel.querySelector('.prev-btn');
        const nextBtn = carousel.querySelector('.next-btn');
        const dotsContainer = carousel.querySelector('.carousel-dots');
        
        if (grid && prevBtn && nextBtn) {
            const cards = grid.querySelectorAll('.product-card-item, .rec-card');
            let currentIdx = 0;

            const getVisibleCards = () => {
                if (window.innerWidth <= 600) return 2;
                if (window.innerWidth <= 1024) return 3;
                return 6;
            };

            const updateCarousel = () => {
                const visibleCards = getVisibleCards();
                const containerWidth = grid.parentElement.clientWidth;
                const computedStyle = window.getComputedStyle(grid);
                const gap = parseFloat(computedStyle.gap) || 24;
                const cardWidth = Math.floor((containerWidth - (visibleCards - 1) * gap) / visibleCards) - 1;

                cards.forEach(card => {
                    card.style.flex = `0 0 ${cardWidth}px`;
                    card.style.width = `${cardWidth}px`;
                });

                const maxIdx = Math.max(0, cards.length - visibleCards);
                if (currentIdx > maxIdx) currentIdx = maxIdx;

                const moveX = currentIdx * (cardWidth + gap);
                grid.style.transform = `translateX(-${moveX}px)`;

                if (dotsContainer) {
                    const dots = dotsContainer.querySelectorAll('.gallery-dot');
                    dots.forEach((dot, idx) => {
                        dot.classList.toggle('active', idx === currentIdx);
                    });
                }
            };

            const initDots = () => {
                if (!dotsContainer) return;
                dotsContainer.innerHTML = '';
                const visibleCards = getVisibleCards();
                const totalDots = Math.max(0, cards.length - visibleCards + 1);
                
                for (let i = 0; i < totalDots; i++) {
                    const dot = document.createElement('span');
                    dot.className = 'gallery-dot';
                    dot.addEventListener('click', () => {
                        currentIdx = i;
                        updateCarousel();
                    });
                    dotsContainer.appendChild(dot);
                }
            };

            nextBtn.addEventListener('click', () => {
                const maxIdx = Math.max(0, cards.length - getVisibleCards());
                currentIdx = (currentIdx >= maxIdx) ? 0 : currentIdx + 1;
                updateCarousel();
            });

            prevBtn.addEventListener('click', () => {
                const maxIdx = Math.max(0, cards.length - getVisibleCards());
                currentIdx = (currentIdx <= 0) ? maxIdx : currentIdx - 1;
                updateCarousel();
            });

            window.addEventListener('resize', () => {
                initDots();
                updateCarousel();
            });
            
            initDots();
            setTimeout(updateCarousel, 100);
        }
    });

    // Sidebar Filter Accordions
    const filterHeaders = document.querySelectorAll('.filter-group-header');
    filterHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const group = header.parentElement;
            group.classList.toggle('active');
        });
    });

    // Dynamic Price Range Slider
    const initPriceSlider = () => {
        const sliderRoot = document.getElementById('price-slider-root');
        if (!sliderRoot) return;

        const minHandle = document.getElementById('price-min-handle');
        const maxHandle = document.getElementById('price-max-handle');
        const rangeTrack = document.getElementById('price-range-active');
        const minField = document.getElementById('price-min-field');
        const maxField = document.getElementById('price-max-field');

        let minLeft = 0;
        let maxLeft = 100;
        const maxPrice = 300;

        const updateSlider = () => {
            minHandle.style.left = `${minLeft}%`;
            maxHandle.style.left = `${maxLeft}%`;
            rangeTrack.style.left = `${minLeft}%`;
            rangeTrack.style.right = `${100 - maxLeft}%`;
            
            if (minField) minField.value = Math.round((minLeft / 100) * maxPrice);
            if (maxField) maxField.value = Math.round((maxLeft / 100) * maxPrice);
        };

        const onMouseMove = (e, handleType) => {
            const rect = sliderRoot.getBoundingClientRect();
            const clientX = e.clientX || (e.touches && e.touches[0].clientX);
            let percent = ((clientX - rect.left) / rect.width) * 100;
            percent = Math.max(0, Math.min(100, percent));

            if (handleType === 'min') {
                minLeft = Math.min(percent, maxLeft - 5);
            } else {
                maxLeft = Math.max(percent, minLeft + 5);
            }
            updateSlider();
        };

        const onStart = (e, handleType) => {
            e.preventDefault();
            const moveHandler = (moveEvent) => onMouseMove(moveEvent, handleType);
            const endHandler = () => {
                document.removeEventListener('mousemove', moveHandler);
                document.removeEventListener('mouseup', endHandler);
                document.removeEventListener('touchmove', moveHandler);
                document.removeEventListener('touchend', endHandler);
            };
            document.addEventListener('mousemove', moveHandler);
            document.addEventListener('mouseup', endHandler);
            document.addEventListener('touchmove', moveHandler, { passive: false });
            document.addEventListener('touchend', endHandler);
        };

        if (minHandle) {
            minHandle.addEventListener('mousedown', (e) => onStart(e, 'min'));
            minHandle.addEventListener('touchstart', (e) => onStart(e, 'min'), { passive: false });
        }
        if (maxHandle) {
            maxHandle.addEventListener('mousedown', (e) => onStart(e, 'max'));
            maxHandle.addEventListener('touchstart', (e) => onStart(e, 'max'), { passive: false });
        }

        // Sync inputs back to slider if typed manually
        if (minField && maxField) {
            [minField, maxField].forEach(field => {
                field.addEventListener('input', () => {
                    let val = parseInt(field.value) || 0;
                    if (field.id === 'price-min-field') {
                        minLeft = Math.min((val / maxPrice) * 100, maxLeft - 5);
                    } else {
                        maxLeft = Math.max((val / maxPrice) * 100, minLeft + 5);
                    }
                    updateSlider();
                });
            });
        }
    };

    initPriceSlider();

    // Search Overlay Logic
    const searchOverlay = document.getElementById('search-overlay');
    if (searchOverlay) {
        // Dynamically inject the search-results element if it doesn't exist in the DOM
        let searchResultsContainer = document.getElementById('search-results');
        if (!searchResultsContainer) {
            const container = searchOverlay.querySelector('.search-container');
            if (container) {
                searchResultsContainer = document.createElement('div');
                searchResultsContainer.id = 'search-results';
                searchResultsContainer.className = 'search-results';
                container.appendChild(searchResultsContainer);
            }
        }
    }

    const searchBtns = document.querySelectorAll('.search-btn');
    const closeSearch = document.getElementById('close-search');
    const searchInput = document.getElementById('search-input');

    const openSearch = () => {
        if (searchOverlay) {
            searchOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
            setTimeout(() => {
                if (searchInput) searchInput.focus();
            }, 500);
        }
    };

    const closeSearchOverlay = () => {
        if (searchOverlay) {
            searchOverlay.classList.remove('active');
            document.body.style.overflow = '';
            if (searchInput) searchInput.value = '';
            if (searchResults) {
                searchResults.innerHTML = '';
                searchResults.classList.remove('has-content');
            }
        }
    };

    searchBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            openSearch();
        });
    });

    if (closeSearch) {
        closeSearch.addEventListener('click', closeSearchOverlay);
    }

    if (searchOverlay) {
        searchOverlay.addEventListener('click', (e) => {
            if (e.target === searchOverlay) closeSearchOverlay();
        });
    }

    // --- Search Functionality ---
    const searchProducts = [
        { name: "Harnais Anti-Traction SteadyWalk", price: "49,00 €", image: "harnais_anti_traction_main_1775840455761.png", url: "harnais-anti-traction-chien.html" },
        { name: "Collier Cuir Heritage", price: "125,00 €", image: "collier_cuir_visual.png", url: "collier-cuir-chien.html" },
        { name: "Laisse Cuir Elegance", price: "45,00 €", image: "dog_leash_elegant_1775487863541.png", url: "laisse-chien.html" },
        { name: "Panier Orthopédique Velvet", price: "129,00 €", image: "panier_velvet_main.png", url: "panier-orthopedique-velvet.html" },
        { name: "Imperméable StormGuard", price: "65,00 €", image: "impermeable_stormguard_main.png", url: "produit-impermeable.html" },
        { name: "Manteau de Pluie Mist", price: "55,00 €", image: "dog_raincoat_mist_1775488107577.png", url: "produit-impermeable.html" },
        { name: "Sac de Transport Nomade", price: "89,00 €", image: "sac_transport_chien_main.png", url: "sac-transport-chien.html" },
        { name: "Coussin Anti-Stress Nuage", price: "59,00 €", image: "cat_coussin_antistress_visual.png", url: "coussin-anti-stress-chien.html" },
        { name: "Tapis Rafraîchissant Chill", price: "39,00 €", image: "cat_tapis_rafraichissant_visual.png", url: "tapis-rafraichissant-chien.html" },
        { name: "Pull en Laine Douce", price: "35,00 €", image: "pull_chien_main.png", url: "pull-sweat.html" }
    ];

    const searchResults = document.getElementById('search-results');

    if (searchInput && searchResults) {
        searchInput.addEventListener('input', () => {
            const query = searchInput.value.toLowerCase().trim();
            
            if (query.length < 2) {
                searchResults.innerHTML = '';
                searchResults.classList.remove('has-content');
                return;
            }

            const filtered = searchProducts.filter(p => 
                p.name.toLowerCase().includes(query)
            );

            if (filtered.length > 0) {
                searchResults.innerHTML = filtered.map(p => `
                    <a href="${p.url}" class="search-result-item">
                        <img src="${p.image}" alt="${p.name}" class="search-result-img">
                        <div class="search-result-info">
                            <h4>${p.name}</h4>
                            <span class="price">${p.price}</span>
                        </div>
                    </a>
                `).join('');
                searchResults.classList.add('has-content');
            } else {
                searchResults.innerHTML = '<div class="search-no-results">Aucun produit trouvé pour "' + query + '"</div>';
                searchResults.classList.add('has-content');
            }
        });
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && searchOverlay && searchOverlay.classList.contains('active')) {
            closeSearchOverlay();
        }
    });

    // Category Carousel Logic
    function initCategoryCarousel() {
        const wrapper = document.querySelector('.category-carousel-wrapper');
        if (!wrapper) return;

        const row = wrapper.querySelector('.category-tags-row');
        const prevBtn = wrapper.querySelector('.carousel-nav.prev');
        const nextBtn = wrapper.querySelector('.carousel-nav.next');

        if (!row || !prevBtn || !nextBtn) return;

        const scrollAmount = 300;

        nextBtn.addEventListener('click', () => {
            row.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        prevBtn.addEventListener('click', () => {
            row.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });
        
        const toggleButtons = () => {
            prevBtn.style.opacity = row.scrollLeft <= 5 ? '0' : '1';
            prevBtn.style.pointerEvents = row.scrollLeft <= 5 ? 'none' : 'auto';
            
            const maxScroll = row.scrollWidth - row.clientWidth;
            nextBtn.style.opacity = row.scrollLeft >= maxScroll - 5 ? '0' : '1';
            nextBtn.style.pointerEvents = row.scrollLeft >= maxScroll - 5 ? 'none' : 'auto';
        };

        row.addEventListener('scroll', toggleButtons);
        window.addEventListener('resize', toggleButtons);
        
        // Initial state
        setTimeout(toggleButtons, 100);
    }
    
    initCategoryCarousel();

    // --- Premium Hero Logic ---
    const voirPlusBtn = document.getElementById('voir-plus-toggle');
    const heroDesc = document.getElementById('hero-desc');
    if (voirPlusBtn && heroDesc) {
        voirPlusBtn.addEventListener('click', () => {
            const isExpanded = heroDesc.classList.toggle('expanded');
            voirPlusBtn.textContent = isExpanded ? 'Voir moins' : 'Voir plus';
        });
    }

    const visualTrack = document.getElementById('visual-track');
    const visualPrev = document.getElementById('visual-prev');
    const visualNext = document.getElementById('visual-next');

    if (visualTrack && visualPrev && visualNext) {
        const container = visualTrack.parentElement;
        const getScrollAmount = () => {
            const card = visualTrack.querySelector('.visual-card');
            if (!card) return 320;
            const cardWidth = card.getBoundingClientRect().width;
            const gap = parseFloat(getComputedStyle(visualTrack).gap) || 32;
            return cardWidth + gap;
        };

        visualNext.addEventListener('click', () => {
            container.scrollBy({ left: getScrollAmount(), behavior: 'smooth' });
        });
        visualPrev.addEventListener('click', () => {
            container.scrollBy({ left: -getScrollAmount(), behavior: 'smooth' });
        });
    }

    // Collection Sort Dropdown Logic
    const sortBtn = document.getElementById('sort-dropdown-btn');
    const sortMenu = document.getElementById('sort-menu');
    const sortOptionsList = document.querySelectorAll('.sort-option');
    const currentSortSpan = document.querySelector('.current-sort');

    if (sortBtn && sortMenu) {
        sortBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            sortBtn.parentElement.classList.toggle('active');
        });

        sortOptionsList.forEach(option => {
            option.addEventListener('click', () => {
                const sortText = option.textContent.trim();
                
                if (currentSortSpan) currentSortSpan.textContent = sortText;
                
                sortOptionsList.forEach(opt => opt.classList.remove('active'));
                option.classList.add('active');

                sortBtn.parentElement.classList.remove('active');
            });
        });

        document.addEventListener('click', () => {
            if (sortBtn.parentElement.classList.contains('active')) {
                sortBtn.parentElement.classList.remove('active');
            }
        });
    }

    // --- Quick View System (Luxe Industrial) ---
    
    // 1. Inject Modal Structure
    const qvModalHTML = `
        <div class="qv-modal-overlay" id="qv-modal">
            <div class="qv-modal-container">
                <button class="qv-close-btn" id="qv-close" aria-label="Fermer">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
                <div class="qv-modal-left">
                    <div class="qv-main-img-box">
                        <button class="qv-main-nav prev" id="qv-main-prev">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
                        </button>
                        <img src="" alt="" id="qv-main-img">
                        <button class="qv-main-nav next" id="qv-main-next">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
                        </button>
                    </div>
                    <div class="qv-thumb-wrapper">
                        <div class="qv-thumbnails" id="qv-thumbs">
                            <div class="qv-thumb active"><img src="" alt="" class="thumb-img-1"></div>
                            <div class="qv-thumb"><img src="" alt="" class="thumb-img-2"></div>
                            <div class="qv-thumb"><img src="" alt="" class="thumb-img-3"></div>
                            <div class="qv-thumb"><img src="" alt="" class="thumb-img-4"></div>
                            <div class="qv-thumb"><img src="" alt="" class="thumb-img-5"></div>
                        </div>
                    </div>
                </div>
                <div class="qv-modal-right">
                    <div class="qv-category">CHETOUTOU PREMIUM</div>
                    <h2 class="qv-title" id="qv-title-el">Nom du Produit</h2>
                    <div class="qv-rating">
                        <div class="qv-stars">★★★★★</div>
                        <div class="qv-reviews-count">4.9/5 (120 avis)</div>
                    </div>
                    <div class="qv-price" id="qv-price-el">0,00 €</div>
                    <div class="qv-shipping">✓ Livraison gratuite</div>
                    
                    <div class="qv-selector-group">
                        <span class="qv-label">Couleur: <span id="qv-color-val" style="font-weight: 500; color: #666;">Noir</span></span>
                        <div class="qv-swatches">
                            <div class="qv-swatch active" data-color="Noir"><img src="" alt="Noir" class="swatch-img-1"></div>
                            <div class="qv-swatch" data-color="Marron"><img src="" alt="Marron" class="swatch-img-2"></div>
                        </div>
                    </div>
                    
                    <div class="qv-label">Quantité</div>
                    <div class="qv-qty-box">
                        <button class="qv-qty-btn" id="qv-qty-minus" type="button">−</button>
                        <input type="number" value="1" min="1" class="qv-qty-input" id="qv-qty-input">
                        <button class="qv-qty-btn" id="qv-qty-plus" type="button">+</button>
                    </div>
                    
                    <button class="qv-add-btn" type="button">Ajouter au panier</button>
                    
                    <div class="qv-full-details" id="qv-link">
                        Afficher tous les détails 
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="7" y1="17" x2="17" y2="7"></line>
                            <polyline points="7 7 17 7 17 17"></polyline>
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', qvModalHTML);

    const qvModal = document.getElementById('qv-modal');
    const qvClose = document.getElementById('qv-close');
    const qvMainImg = document.getElementById('qv-main-img');
    const qvMainPrev = document.getElementById('qv-main-prev');
    const qvMainNext = document.getElementById('qv-main-next');
    const qvThumb4 = document.querySelector('.thumb-img-4');
    const qvThumb5 = document.querySelector('.thumb-img-5');
    const qvTitle = document.getElementById('qv-title-el');
    const qvPrice = document.getElementById('qv-price-el');
    const qvQtyInput = document.getElementById('qv-qty-input');
    const qvQtyPlus = document.getElementById('qv-qty-plus');
    const qvQtyMinus = document.getElementById('qv-qty-minus');
    const qvThumb1 = document.querySelector('.thumb-img-1');
    const qvThumb2 = document.querySelector('.thumb-img-2');
    const qvThumb3 = document.querySelector('.thumb-img-3');
    const qvSwatch1 = document.querySelector('.swatch-img-1');
    const qvSwatch2 = document.querySelector('.swatch-img-2');
    const qvColorVal = document.getElementById('qv-color-val');
    const qvSwatches = document.querySelectorAll('.qv-swatch');

    let currentQvIdx = 0;
    const qvImages = []; // We'll populate this on open

    // 2. Inject Buttons into Products
    function injectQuickViewButtons() {
        const products = document.querySelectorAll('.product-item');
        products.forEach(product => {
            const wrapper = product.querySelector('.product-img-wrapper');
            if (wrapper && !wrapper.querySelector('.quick-view-btn')) {
                const btn = document.createElement('button');
                btn.className = 'quick-view-btn';
                btn.type = 'button';
                btn.textContent = 'Aperçu rapide';
                wrapper.appendChild(btn);

                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    openQuickView(product);
                });
            }
        });
    }

    function openQuickView(product) {
        const title = product.querySelector('h3').textContent.trim();
        const price = product.querySelector('.product-price').textContent.trim();
        const img = product.querySelector('img').src;

        // Pool of varied images for demo
        const demoImages = [
            img,
            "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&q=80&w=400",
            "https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&q=80&w=400",
            "https://images.unsplash.com/photo-1534361960057-19889db9621e?auto=format&fit=crop&q=80&w=400",
            "https://images.unsplash.com/photo-1544568100-847a948585b9?auto=format&fit=crop&q=80&w=400"
        ];

        qvTitle.textContent = title;
        qvPrice.textContent = price;
        qvMainImg.src = img;
        
        qvThumb1.src = demoImages[0];
        qvThumb2.src = demoImages[1]; 
        qvThumb3.src = demoImages[2];
        qvThumb4.src = demoImages[3];
        qvThumb5.src = demoImages[4];
        
        qvSwatch1.src = demoImages[0];
        qvSwatch2.src = demoImages[1];
        
        qvQtyInput.value = 1;
        qvColorVal.textContent = "Noir";
        
        currentQvIdx = 0;

        // Function to update main image when clicking/navigating
        const updateDisplay = (idx) => {
            qvMainImg.style.opacity = '0';
            setTimeout(() => {
                qvMainImg.src = demoImages[idx];
                qvMainImg.style.opacity = '1';
                updateQvImage(idx);
            }, 150);
        };

        qvModal.classList.add('active');
        document.body.style.overflow = 'hidden';

        // Add specific listeners for this open session if needed or use global ones
        // But the global ones need access to demoImages. Let's make demoImages global-ish or attach to window.
        window.currentQvImages = demoImages;
    }

    const updateQvImage = (index) => {
        const thumbs = document.querySelectorAll('.qv-thumb');
        thumbs.forEach((t, i) => t.classList.toggle('active', i === index));
    };

    if (qvMainPrev) qvMainPrev.addEventListener('click', () => {
        currentQvIdx = (currentQvIdx > 0) ? currentQvIdx - 1 : 4;
        if (window.currentQvImages) {
            qvMainImg.src = window.currentQvImages[currentQvIdx];
            updateQvImage(currentQvIdx);
        }
    });

    if (qvMainNext) qvMainNext.addEventListener('click', () => {
        currentQvIdx = (currentQvIdx < 4) ? currentQvIdx + 1 : 0;
        if (window.currentQvImages) {
            qvMainImg.src = window.currentQvImages[currentQvIdx];
            updateQvImage(currentQvIdx);
        }
    });

    // Thumbnail Click Interaction
    document.addEventListener('click', (e) => {
        if (e.target.closest('.qv-thumb')) {
            const thumb = e.target.closest('.qv-thumb');
            const thumbs = Array.from(document.querySelectorAll('.qv-thumb'));
            const idx = thumbs.indexOf(thumb);
            if (idx !== -1 && window.currentQvImages) {
                currentQvIdx = idx;
                qvMainImg.src = window.currentQvImages[idx];
                updateQvImage(idx);
            }
        }
    });

    // Swatch Interaction
    qvSwatches.forEach(swatch => {
        swatch.addEventListener('click', () => {
            qvSwatches.forEach(s => s.classList.remove('active'));
            swatch.classList.add('active');
            const color = swatch.getAttribute('data-color');
            qvColorVal.textContent = color;
            // Optionally swap main image here if we had different images
        });
    });

    function closeQuickView() {
        qvModal.classList.remove('active');
        document.body.style.overflow = '';
    }

    if (qvClose) qvClose.addEventListener('click', closeQuickView);
    qvModal.addEventListener('click', (e) => { if (e.target === qvModal) closeQuickView(); });

    if (qvQtyPlus) qvQtyPlus.addEventListener('click', () => { qvQtyInput.value = parseInt(qvQtyInput.value) + 1; });
    if (qvQtyMinus) qvQtyMinus.addEventListener('click', () => { if (parseInt(qvQtyInput.value) > 1) qvQtyInput.value = parseInt(qvQtyInput.value) - 1; });

    injectQuickViewButtons();

    // Re-inject on dynamic content updates
    const qvObserver = new MutationObserver(injectQuickViewButtons);
    qvObserver.observe(document.body, { childList: true, subtree: true });

    // --- MAIN GALLERY CAROUSEL LOGIC ---
    const galleryCarousel = document.getElementById('main-gallery-carousel');
    if (galleryCarousel) {
        const images = Array.from(galleryCarousel.querySelectorAll('.variant-img'));
        const prevBtn = document.getElementById('variant-prev');
        const nextBtn = document.getElementById('variant-next');
        const swatchButtons = document.querySelectorAll('.color-previews .preview-btn');
        let currentIndex = 0;

        const updateSlide = (index) => {
            images.forEach((img, i) => {
                img.classList.toggle('active', i === index);
            });
            currentIndex = index;

            // Sync with swatches ONLY if the current slide is a variant (index 0, 1, 2)
            if (index < 3 && swatchButtons.length > index) {
                swatchButtons.forEach(b => b.classList.remove('active'));
                swatchButtons[index].classList.add('active');
                
                // Update text label
                const selectedVal = document.querySelector('.variant-selector-v2 .selected-val');
                if (selectedVal && swatchButtons[index].title) {
                    selectedVal.textContent = swatchButtons[index].title;
                }
            }
        };

        if (prevBtn) {
            prevBtn.addEventListener('click', (e) => {
                e.preventDefault();
                // Restrict arrows to cycle only through grid images (indices 3 to 8)
                let newIndex = currentIndex - 1;
                if (newIndex < 3 || newIndex >= 9) newIndex = 8; // Loop within [3...8]
                updateSlide(newIndex);
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', (e) => {
                e.preventDefault();
                // Restrict arrows to cycle only through grid images (indices 3 to 8)
                let newIndex = currentIndex + 1;
                if (newIndex >= 9 || newIndex < 3) newIndex = 3; // Loop within [3...8]
                updateSlide(newIndex);
            });
        }

        // Sync from swatches to carousel
        swatchButtons.forEach((btn, index) => {
            btn.addEventListener('click', () => {
                updateSlide(index);
            });
        });

        // --- NEW: Sync from Grid Images to Main Carousel ---
        const gridImages = document.querySelectorAll('.gallery-stacked-row .gallery-stacked-item img');
        gridImages.forEach((gridImg) => {
            gridImg.style.cursor = 'pointer';
            gridImg.addEventListener('click', () => {
                const src = gridImg.getAttribute('src');
                const targetIndex = images.findIndex(img => img.getAttribute('src') === src);
                
                if (targetIndex !== -1) {
                    updateSlide(targetIndex);
                    // Smooth scroll back to top carousel
                    galleryCarousel.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            });
        });

        // --- NEW: Interactive Zoom on Main Carousel ---
        galleryCarousel.addEventListener('mousemove', (e) => {
            const activeImg = galleryCarousel.querySelector('.variant-img.active');
            if (!activeImg) return;

            const rect = galleryCarousel.getBoundingClientRect();
            const x = ((e.clientX - rect.left) / rect.width) * 100;
            const y = ((e.clientY - rect.top) / rect.height) * 100;
            
            activeImg.style.transformOrigin = `${x}% ${y}%`;
            activeImg.style.transform = 'scale(2)';
            activeImg.style.cursor = 'zoom-in';
        });

        galleryCarousel.addEventListener('mouseleave', () => {
            const activeImg = galleryCarousel.querySelector('.variant-img.active');
            if (!activeImg) return;
            
            activeImg.style.transformOrigin = 'center center';
            activeImg.style.transform = 'scale(1)';
        });
    }
    // --- BLOG FILTERING LOGIC (V7) ---
    const blogFilters = document.querySelectorAll('.filter-item-v7');
    const blogArticles = document.querySelectorAll('.grid-card-v7, .featured-card-v7');

    if (blogFilters.length > 0 && blogArticles.length > 0) {
        blogFilters.forEach(filter => {
            filter.addEventListener('click', (e) => {
                e.preventDefault();
                
                const category = filter.getAttribute('data-category');
                
                // Update active state
                blogFilters.forEach(f => f.classList.remove('active'));
                filter.classList.add('active');
                
                // Filter articles
                blogArticles.forEach(article => {
                    const articleCat = article.getAttribute('data-category');
                    
                    if (category === 'all' || articleCat === category) {
                        article.style.display = 'grid'; // Grid cards are flex/grid, featured is grid
                        if (article.classList.contains('grid-card-v7')) {
                            article.style.display = 'flex'; // Restore flex for grid cards
                        }
                        // Use a small timeout for animation if needed, or just show/hide
                        article.style.opacity = '0';
                        setTimeout(() => {
                            article.style.opacity = '1';
                        }, 50);
                    } else {
                        article.style.display = 'none';
                    }
                });

                // Update section titles visibility
                const featuredSection = document.querySelector('.featured-section-v7');
                const featuredTitle = featuredSection?.querySelector('.blog-section-title');
                const visibleFeatured = Array.from(blogArticles).filter(a => a.classList.contains('featured-card-v7') && a.style.display !== 'none');
                
                if (featuredSection) {
                    featuredSection.style.display = (visibleFeatured.length > 0) ? 'block' : 'none';
                }
            });
        });
    }

    // --- PRODUCT V4 SPECIFIC LOGIC ---
    
    // Accordion V4 Toggle
    const accHeadersV4 = document.querySelectorAll('.acc-header-v4');
    accHeadersV4.forEach(header => {
        header.addEventListener('click', () => {
            const item = header.parentElement;
            const content = item.querySelector('.pdp-acc-content');
            const isActive = item.classList.contains('active');
            
            // Close all others in the same group
            const group = item.parentElement;
            group.querySelectorAll('.acc-item-v4').forEach(other => {
                other.classList.remove('active');
                const otherContent = other.querySelector('.pdp-acc-content');
                if (otherContent) {
                    otherContent.style.maxHeight = '0';
                    otherContent.style.paddingBottom = '0';
                }
            });
            
            if (!isActive) {
                item.classList.add('active');
                content.style.maxHeight = '500px';
                content.style.paddingBottom = '1.5rem';
            }
        });
    });

    // Swatch V4 Selection
    const swatchesV4 = document.querySelectorAll('.swatch-v4');
    swatchesV4.forEach(swatch => {
        swatch.addEventListener('click', () => {
            swatchesV4.forEach(s => s.classList.remove('active'));
            swatch.classList.add('active');
        });
    });

    // Quantity V4 Control
    const qtyBtnMinusV4 = document.querySelector('.qty-btn-v4.minus');
    const qtyBtnPlusV4 = document.querySelector('.qty-btn-v4.plus');
    const qtyInputV4 = document.getElementById('qty-input-v4');

    if (qtyBtnMinusV4 && qtyBtnPlusV4 && qtyInputV4) {
        qtyBtnMinusV4.addEventListener('click', () => {
            let val = parseInt(qtyInputV4.value) || 1;
            if (val > 1) qtyInputV4.value = val - 1;
        });
        qtyBtnPlusV4.addEventListener('click', () => {
            let val = parseInt(qtyInputV4.value) || 1;
            qtyInputV4.value = val + 1;
        });
    }

    // Injected Floating Assistance Widget
    const injectAssistanceWidget = () => {
        // Create style tag
        const style = document.createElement('style');
        style.innerHTML = `
            #assistance-floating-btn {
                position: fixed;
                bottom: 24px;
                left: 24px;
                background-color: #e69c1a;
                color: #fff;
                border: none;
                border-radius: 50px;
                padding: 12px 20px;
                font-size: 0.95rem;
                font-weight: 600;
                box-shadow: 0 4px 16px rgba(0,0,0,0.15);
                cursor: pointer;
                display: flex;
                align-items: center;
                gap: 8px;
                z-index: 9999;
                transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
            }
            #assistance-floating-btn:hover {
                background-color: #d18712;
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(0,0,0,0.22);
            }
            #assistance-floating-btn.active {
                width: 50px;
                height: 50px;
                padding: 0;
                justify-content: center;
                border-radius: 50%;
                background-color: #e69c1a;
            }
            #assistance-widget {
                position: fixed;
                bottom: 150px;
                left: 24px;
                width: 360px;
                max-width: calc(100vw - 48px);
                background: #fff;
                border-radius: 16px;
                box-shadow: 0 12px 36px rgba(0,0,0,0.15);
                z-index: 9998;
                overflow: hidden;
                display: none;
                flex-direction: column;
                font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
                border: 1px solid #e1e1e1;
                transform-origin: bottom left;
                animation: assistanceScaleUp 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
            }
            @keyframes assistanceScaleUp {
                from {
                    opacity: 0;
                    transform: scale(0.85) translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: scale(1) translateY(0);
                }
            }
            .assistance-header {
                background-color: #e69c1a;
                color: #fff;
                padding: 1.5rem;
                position: relative;
            }
            .assistance-header h3 {
                margin: 0 0 6px 0;
                font-size: 1.2rem;
                font-weight: 700;
                letter-spacing: -0.2px;
            }
            .assistance-header p {
                margin: 0;
                font-size: 0.85rem;
                line-height: 1.4;
                opacity: 0.95;
            }
            .assistance-body {
                display: flex;
                flex-direction: column;
                background: #fff;
            }
            .assistance-input-container {
                padding: 1.25rem;
                border-bottom: 1px solid #f0f0f0;
            }
            .assistance-input-wrapper {
                border: 1px solid #d9d9d9;
                border-radius: 8px;
                padding: 10px 40px 10px 12px;
                background: #fff;
                position: relative;
                transition: border-color 0.2s;
            }
            .assistance-input-wrapper:focus-within {
                border-color: #e69c1a;
            }
            .assistance-textarea {
                width: 100%;
                border: none;
                outline: none;
                resize: none;
                font-family: inherit;
                font-size: 0.9rem;
                color: #333;
                height: 48px;
                box-sizing: border-box;
                display: block;
            }
            .assistance-textarea::placeholder {
                color: #aaa;
            }
            .assistance-send-btn {
                position: absolute;
                bottom: 10px;
                right: 12px;
                background: none;
                border: none;
                color: #e69c1a;
                cursor: pointer;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: color 0.2s;
            }
            .assistance-send-btn:hover {
                color: #d18712;
            }
            .assistance-instant-title {
                text-align: center;
                font-size: 0.9rem;
                font-weight: 600;
                color: #111;
                margin: 1.25rem 0 0.75rem 0;
            }
            .assistance-instant-btn {
                width: calc(100% - 2.5rem);
                margin: 0 auto 1.5rem auto;
                padding: 12px 16px;
                background: #fff;
                border: 1px solid #e1e1e1;
                border-radius: 8px;
                font-size: 0.9rem;
                font-weight: 500;
                color: #333;
                cursor: pointer;
                transition: all 0.2s;
                text-align: left;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: 0 1px 2px rgba(0,0,0,0.02);
            }
            .assistance-instant-btn:hover {
                background: #fafafa;
                border-color: #ccc;
                transform: translateY(-1px);
            }
        `;
        document.head.appendChild(style);

        // Create floating button
        const btn = document.createElement('button');
        btn.id = 'assistance-floating-btn';
        btn.setAttribute('aria-label', 'Ouvrir l\'assistance');
        btn.innerHTML = `
            <svg id="assistance-chat-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                <circle cx="8" cy="10" r="1" fill="currentColor"></circle>
                <circle cx="12" cy="10" r="1" fill="currentColor"></circle>
                <circle cx="16" cy="10" r="1" fill="currentColor"></circle>
            </svg>
            <span id="assistance-btn-text">Assistance</span>
        `;
        document.body.appendChild(btn);

        // Create widget
        const widget = document.createElement('div');
        widget.id = 'assistance-widget';
        widget.innerHTML = `
            <div class="assistance-header">
                <h3>Chattez avec nous</h3>
                <p>👋 Bonjour, envoyez-nous un message si vous avez des questions. Nous serons ravis de vous aider !</p>
            </div>
            <div class="assistance-body">
                <div class="assistance-input-container">
                    <div class="assistance-input-wrapper">
                        <textarea class="assistance-textarea" placeholder="Écrire un message" aria-label="Écrire un message"></textarea>
                        <button class="assistance-send-btn" aria-label="Envoyer le message">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="22" y1="2" x2="11" y2="13"></line>
                                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                            </svg>
                        </button>
                    </div>
                </div>
                <div class="assistance-instant-title">Réponses instantanées</div>
                <button class="assistance-instant-btn" id="assistance-track-order-btn">
                    <span>Suivre ma commande</span>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                </button>
            </div>
        `;
        document.body.appendChild(widget);

        // Event listener for floating button
        let isOpen = false;
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            isOpen = !isOpen;
            if (isOpen) {
                widget.style.display = 'flex';
                btn.classList.add('active');
                btn.innerHTML = `
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                `;
            } else {
                widget.style.display = 'none';
                btn.classList.remove('active');
                btn.innerHTML = `
                    <svg id="assistance-chat-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                        <circle cx="8" cy="10" r="1" fill="currentColor"></circle>
                        <circle cx="12" cy="10" r="1" fill="currentColor"></circle>
                        <circle cx="16" cy="10" r="1" fill="currentColor"></circle>
                    </svg>
                    <span id="assistance-btn-text">Assistance</span>
                `;
            }
        });

        // Close when clicking outside the widget
        document.addEventListener('click', (e) => {
            if (isOpen && !widget.contains(e.target) && e.target !== btn) {
                isOpen = false;
                widget.style.display = 'none';
                btn.classList.remove('active');
                btn.innerHTML = `
                    <svg id="assistance-chat-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                        <circle cx="8" cy="10" r="1" fill="currentColor"></circle>
                        <circle cx="12" cy="10" r="1" fill="currentColor"></circle>
                        <circle cx="16" cy="10" r="1" fill="currentColor"></circle>
                    </svg>
                    <span id="assistance-btn-text">Assistance</span>
                `;
            }
        });

        // Prevent closing when clicking inside
        widget.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        // Redirect to suivre-commande.html when "Suivre ma commande" is clicked
        const trackBtn = document.getElementById('assistance-track-order-btn');
        if (trackBtn) {
            trackBtn.addEventListener('click', () => {
                window.location.href = 'suivre-commande.html';
            });
        }

        // Mock send message interaction
        const sendBtn = widget.querySelector('.assistance-send-btn');
        const textarea = widget.querySelector('.assistance-textarea');
        if (sendBtn && textarea) {
            const sendMessage = () => {
                const text = textarea.value.trim();
                if (text.length > 0) {
                    alert('Votre message a bien été envoyé ! Notre équipe vous répondra dans les plus brefs délais.');
                    textarea.value = '';
                }
            };
            sendBtn.addEventListener('click', sendMessage);
            textarea.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    sendMessage();
                }
            });
        }
    };

    injectAssistanceWidget();

    // Injected Floating Promo Widget (5€ Voucher)
    const injectPromoWidget = () => {
        // Create style tag
        const style = document.createElement('style');
        style.innerHTML = `
            #promo-floating-btn {
                position: fixed;
                bottom: 88px;
                left: 24px;
                width: 50px;
                height: 50px;
                background-color: #000;
                color: #fff;
                border: 3px solid #e69c1a;
                border-radius: 50%;
                box-shadow: 0 4px 16px rgba(0,0,0,0.2);
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 9999;
                transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                outline: 2px solid #fff;
                outline-offset: -5px;
            }
            #promo-floating-btn:hover {
                transform: scale(1.08);
                box-shadow: 0 6px 20px rgba(0,0,0,0.3);
                border-color: #e69c1a;
            }
            #promo-modal-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(0, 0, 0, 0.45);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                display: none;
                justify-content: center;
                align-items: center;
                z-index: 10000;
            }
            .promo-modal-card {
                background: #fff;
                width: 380px;
                max-width: calc(100vw - 32px);
                border-radius: 16px;
                padding: 2.25rem 2rem;
                box-shadow: 0 12px 48px rgba(0,0,0,0.2);
                position: relative;
                text-align: center;
                font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
                border: 1px solid #e1e1e1;
                transform-origin: center;
                animation: promoScaleUp 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
            }
            @keyframes promoScaleUp {
                from {
                    opacity: 0;
                    transform: scale(0.85) translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: scale(1) translateY(0);
                }
            }
            .promo-modal-close {
                position: absolute;
                top: -12px;
                right: -12px;
                width: 32px;
                height: 32px;
                border-radius: 50%;
                background: #333;
                color: #fff;
                border: 2px solid #fff;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 2px 8px rgba(0,0,0,0.15);
                transition: background 0.2s, transform 0.2s;
            }
            .promo-modal-close:hover {
                background: #000;
                transform: scale(1.05);
            }
            .promo-image {
                width: 140px;
                height: 140px;
                object-fit: cover;
                border-radius: 50%;
                margin: 0 auto 1.25rem auto;
                display: block;
                border: 3px solid #fdf6ec;
                box-shadow: 0 4px 12px rgba(230,156,26,0.15);
            }
            .promo-eyebrow {
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 1px;
                color: #888;
                font-weight: 600;
                margin-bottom: 6px;
            }
            .promo-title {
                font-size: 1.35rem;
                font-weight: 700;
                line-height: 1.3;
                color: #111;
                margin: 0 0 8px 0;
            }
            .promo-subtitle {
                font-size: 0.88rem;
                color: #666;
                margin: 0 0 1.5rem 0;
                line-height: 1.4;
            }
            .promo-form {
                display: flex;
                flex-direction: column;
                gap: 12px;
                width: 100%;
            }
            .promo-input {
                width: 100%;
                border: 1px solid #d9d9d9;
                border-radius: 8px;
                padding: 12px;
                font-size: 0.9rem;
                color: #333;
                background-color: #fcfdfe;
                box-sizing: border-box;
                font-family: inherit;
                transition: border-color 0.2s;
            }
            .promo-input:focus {
                border-color: #e69c1a;
                outline: none;
                background-color: #fff;
            }
            .promo-btn {
                width: 100%;
                background: #e69c1a;
                color: #000;
                border: none;
                border-radius: 8px;
                padding: 12px 0;
                font-size: 0.95rem;
                font-weight: 700;
                cursor: pointer;
                transition: background 0.2s, transform 0.1s;
                font-family: inherit;
            }
            .promo-btn:hover {
                background: #d18712;
            }
            .promo-btn:active {
                transform: scale(0.98);
            }
            .promo-decline {
                color: #777;
                font-size: 0.85rem;
                font-weight: 500;
                text-decoration: none;
                margin-top: 1rem;
                display: inline-block;
                cursor: pointer;
                transition: color 0.2s;
            }
            .promo-decline:hover {
                color: #333;
                text-decoration: underline;
            }
        `;
        document.head.appendChild(style);

        // Create floating button
        const btn = document.createElement('button');
        btn.id = 'promo-floating-btn';
        btn.setAttribute('aria-label', 'Voir l\'offre spéciale');
        btn.innerHTML = `
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#e69c1a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 12 20 22 4 22 4 12"></polyline>
                <rect x="2" y="7" width="20" height="5"></rect>
                <line x1="12" y1="22" x2="12" y2="7"></line>
                <path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path>
                <path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path>
            </svg>
        `;
        document.body.appendChild(btn);

        // Create overlay and modal
        const overlay = document.createElement('div');
        overlay.id = 'promo-modal-overlay';
        overlay.innerHTML = `
            <div class="promo-modal-card">
                <button class="promo-modal-close" aria-label="Fermer la fenêtre">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
                <div id="promo-modal-content-wrapper">
                    <img class="promo-image" src="gift_promo_popup.png" alt="Cadeau Chetoutou">
                    <div class="promo-eyebrow">Offre spéciale bon d'achat</div>
                    <h3 class="promo-title">Rejoignez-nous et bénéficiez de -10% sur votre première commande.</h3>
                    <p class="promo-subtitle">Inscrivez-vous pour bénéficier de l'offre !</p>
                    <form class="promo-form" id="promo-subscription-form">
                        <input type="email" class="promo-input" placeholder="votre@email.com" required>
                        <button type="submit" class="promo-btn">Recevoir mon code</button>
                    </form>
                    <a class="promo-decline">Non, merci</a>
                </div>
            </div>
        `;
        document.body.appendChild(overlay);

        // Open modal
        btn.addEventListener('click', () => {
            overlay.style.display = 'flex';
        });

        // Close functions
        const closeModal = () => {
            overlay.style.display = 'none';
        };

        overlay.querySelector('.promo-modal-close').addEventListener('click', closeModal);
        overlay.querySelector('.promo-decline').addEventListener('click', closeModal);
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) {
                closeModal();
            }
        });

        const card = overlay.querySelector('.promo-modal-card');
        card.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        // Form submission
        const form = overlay.querySelector('#promo-subscription-form');
        const contentWrapper = overlay.querySelector('#promo-modal-content-wrapper');
        if (form && contentWrapper) {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                const emailInput = form.querySelector('.promo-input');
                if (emailInput && emailInput.value.includes('@')) {
                    // Inject success screen
                    contentWrapper.innerHTML = `
                        <div class="promo-success-state" style="text-align: center; padding: 1rem 0;">
                            <div style="width: 60px; height: 60px; border-radius: 50%; background: #e69c1a; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 2rem; margin: 0 auto 1.25rem auto; box-shadow: 0 4px 12px rgba(230, 156, 26, 0.3);">✓</div>
                            <h3 style="font-size: 1.3rem; font-weight: 700; color: #111; margin-bottom: 0.5rem;">Félicitations !</h3>
                            <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.4;">Votre code promo de -10% est actif. Copiez le code ci-dessous et insérez-le lors de votre paiement :</p>
                            <div id="promo-code-text" style="background: #fdf6ec; border: 1px dashed #e69c1a; border-radius: 6px; padding: 12px; font-size: 1.2rem; font-weight: 700; color: #e69c1a; letter-spacing: 2px; margin-bottom: 1.5rem; user-select: all;">TOUTOU10</div>
                            <button class="promo-btn" id="promo-copy-btn" style="width: 100%; margin: 0 auto; padding: 12px; background: #e69c1a; color: #000; border: none; font-weight: 700; border-radius: 8px; cursor: pointer;">Copier le code</button>
                        </div>
                    `;
                    
                    // Copy button logic
                    const copyBtn = contentWrapper.querySelector('#promo-copy-btn');
                    if (copyBtn) {
                        copyBtn.addEventListener('click', () => {
                            navigator.clipboard.writeText('TOUTOU10').then(() => {
                                copyBtn.textContent = 'Code copié !';
                                copyBtn.style.background = '#27ae60';
                                copyBtn.style.color = '#fff';
                                setTimeout(() => {
                                    closeModal();
                                    // Reset content for next open
                                    setTimeout(() => {
                                        injectPromoWidgetReset();
                                    }, 400);
                                }, 1200);
                            });
                        });
                    }
                }
            });
        }

        // Helper to reset the form content on close
        const injectPromoWidgetReset = () => {
            contentWrapper.innerHTML = `
                <img class="promo-image" src="gift_promo_popup.png" alt="Cadeau Chetoutou">
                <div class="promo-eyebrow">Offre spéciale bon d'achat</div>
                <h3 class="promo-title">Rejoignez-nous et bénéficiez de -10% sur votre première commande.</h3>
                <p class="promo-subtitle">Inscrivez-vous pour bénéficier de l'offre !</p>
                <form class="promo-form" id="promo-subscription-form">
                    <input type="email" class="promo-input" placeholder="votre@email.com" required>
                    <button type="submit" class="promo-btn">Recevoir mon code</button>
                </form>
                <a class="promo-decline">Non, merci</a>
            `;
            // Reattach close/decline listeners
            contentWrapper.querySelector('.promo-decline').addEventListener('click', closeModal);
            const newForm = contentWrapper.querySelector('#promo-subscription-form');
            if (newForm) {
                newForm.addEventListener('submit', (e) => {
                    e.preventDefault();
                    const emailInput = newForm.querySelector('.promo-input');
                    if (emailInput && emailInput.value.includes('@')) {
                        contentWrapper.innerHTML = `
                            <div class="promo-success-state" style="text-align: center; padding: 1rem 0;">
                                <div style="width: 60px; height: 60px; border-radius: 50%; background: #e69c1a; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 2rem; margin: 0 auto 1.25rem auto; box-shadow: 0 4px 12px rgba(230, 156, 26, 0.3);">✓</div>
                                <h3 style="font-size: 1.3rem; font-weight: 700; color: #111; margin-bottom: 0.5rem;">Félicitations !</h3>
                                <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.4;">Votre code promo de -10% est actif. Copiez le code ci-dessous et insérez-le lors de votre paiement :</p>
                                <div id="promo-code-text" style="background: #fdf6ec; border: 1px dashed #e69c1a; border-radius: 6px; padding: 12px; font-size: 1.2rem; font-weight: 700; color: #e69c1a; letter-spacing: 2px; margin-bottom: 1.5rem; user-select: all;">TOUTOU10</div>
                                <button class="promo-btn" id="promo-copy-btn" style="width: 100%; margin: 0 auto; padding: 12px; background: #e69c1a; color: #000; border: none; font-weight: 700; border-radius: 8px; cursor: pointer;">Copier le code</button>
                            </div>
                        `;
                        const newCopyBtn = contentWrapper.querySelector('#promo-copy-btn');
                        if (newCopyBtn) {
                            newCopyBtn.addEventListener('click', () => {
                                navigator.clipboard.writeText('TOUTOU10').then(() => {
                                    newCopyBtn.textContent = 'Code copié !';
                                    newCopyBtn.style.background = '#27ae60';
                                    newCopyBtn.style.color = '#fff';
                                    setTimeout(() => {
                                        closeModal();
                                        setTimeout(() => {
                                            injectPromoWidgetReset();
                                        }, 400);
                                    }, 1200);
                                });
                            });
                        }
                    }
                });
            }
        };
    };

    injectPromoWidget();

    // Dynamically redirect account menu buttons (.profile-btn) to the new connexion page
    const profileBtns = document.querySelectorAll('.profile-btn');
    profileBtns.forEach(btn => {
        btn.setAttribute('href', 'connexion.html');
    });
});

