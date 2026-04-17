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

    // Hero Section Logic: Static Grid (No JS Required)


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
                if (window.innerWidth <= 1024) return 2;
                return 4;
            };

            const updateTrackPosition = () => {
                const cards = track.querySelectorAll('.carousel-card');
                if (cards.length === 0) return;

                const gap = 24;
                const visibleCards = getVisibleCards();
                const containerWidth = track.parentElement.offsetWidth;
                const cardWidth = (containerWidth - (visibleCards - 1) * gap) / visibleCards;

                cards.forEach(card => {
                    card.style.flex = `0 0 ${cardWidth}px`;
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
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Close all others for a cleaner accordion effect
            faqItems.forEach(i => i.classList.remove('active'));

            // Toggle current if it wasn't active
            if (!isActive) {
                item.classList.add('active');
            }
        });
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

    // Recommendations Carousel Logic (Vous aimerez aussi)
    const recCarousel = document.querySelector('.recommendations-section');
    if (recCarousel) {
        const grid = document.getElementById('rec-grid');
        const prevBtn = document.getElementById('rec-prev');
        const nextBtn = document.getElementById('rec-next');
        
        if (grid && prevBtn && nextBtn) {
            const cards = grid.querySelectorAll('.rec-card');
            const dotsContainer = document.getElementById('rec-dots');
            let currentIdx = 0;

            const getVisibleCards = () => {
                if (window.innerWidth <= 600) return 2;
                if (window.innerWidth <= 1024) return 3;
                return 4;
            };

            const updateCarousel = () => {
                const visibleCards = getVisibleCards();
                const gap = 24; // Match CSS gap
                const containerWidth = grid.parentElement.offsetWidth;
                const cardWidth = (containerWidth - (visibleCards - 1) * gap) / visibleCards;

                cards.forEach(card => {
                    card.style.flex = `0 0 ${cardWidth}px`;
                });

                const maxIdx = Math.max(0, cards.length - visibleCards);
                if (currentIdx > maxIdx) currentIdx = maxIdx;

                const moveX = currentIdx * (cardWidth + gap);
                grid.style.transform = `translateX(-${moveX}px)`;

                // Update dots
                if (dotsContainer) {
                    const dots = dotsContainer.querySelectorAll('.gallery-dot');
                    dots.forEach((dot, idx) => {
                        dot.classList.toggle('active', idx === currentIdx);
                    });
                }
            };

            // Initialize dots
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
            
            // Initial call
            initDots();
            setTimeout(updateCarousel, 100);
        }
    }

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

        minHandle.addEventListener('mousedown', (e) => onStart(e, 'min'));
        maxHandle.addEventListener('mousedown', (e) => onStart(e, 'max'));
        minHandle.addEventListener('touchstart', (e) => onStart(e, 'min'), { passive: false });
        maxHandle.addEventListener('touchstart', (e) => onStart(e, 'max'), { passive: false });

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
});
