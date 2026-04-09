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

    // Shopping Cart logic
    let cartCount = 0;
    const cartBadge = document.querySelector('.cart-count');
    const addBtn = document.querySelector('.add-to-cart');

    if (addBtn) {
        addBtn.addEventListener('click', () => {
            cartCount++;
            cartBadge.textContent = cartCount;

            // Visual feedback
            addBtn.textContent = 'Ajouté !';
            addBtn.classList.add('added');

            // Animation for badge
            cartBadge.style.transform = 'scale(1.3)';

            setTimeout(() => {
                addBtn.textContent = 'Ajouter au panier';
                addBtn.classList.remove('added');
                cartBadge.style.transform = 'scale(1)';
            }, 2000);
        });
    }

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
            e.stopPropagation();
            cartCount++;
            if (cartBadge) {
                cartBadge.textContent = cartCount;
                cartBadge.style.transform = 'scale(1.3)';
                setTimeout(() => cartBadge.style.transform = 'scale(1)', 3000);
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
            const tagsRow = document.querySelector('.category-tags-row');

            if (isCollapsed) {
                // Expanding
                seoBody.classList.remove('collapsed');
                if (introPara) introPara.classList.add('expanded');
                viewMoreBtn.textContent = 'Voir moins';
                if (tagsRow) tagsRow.style.order = '4';

                // Move button container to the end of seoBody
                seoBody.appendChild(viewMoreContainer);
            } else {
                // Collapsing
                seoBody.classList.add('collapsed');
                if (introPara) introPara.classList.remove('expanded');
                viewMoreBtn.textContent = 'Voir plus';
                if (tagsRow) tagsRow.style.order = '2';

                // Move button container back to introductory section
                if (introLarge) introLarge.appendChild(viewMoreContainer);

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
    const minusBtn = document.querySelector('.qty-trigger.minus');
    const plusBtn = document.querySelector('.qty-trigger.plus');
    const qtyInput = document.getElementById('qty-input');

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
    const pdpAccordions = document.querySelectorAll('.pdp-accordion-v2 .accordion-item');
    pdpAccordions.forEach(item => {
        const header = item.querySelector('.accordion-header');
        header.addEventListener('click', () => {
            // Close others
            pdpAccordions.forEach(other => {
                if (other !== item) other.classList.remove('active');
            });
            item.classList.toggle('active');
        });
    });

    // Variant Selectors (Visual only)
    const swatchBtns = document.querySelectorAll('.swatch-btn');
    swatchBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            swatchBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });

    const sizeBtns = document.querySelectorAll('.size-btn');
    sizeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            sizeBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });

    // Testimonials Slider Logic
    const testimonialSlider = document.querySelector('.testimonials-slider');
    if (testimonialSlider) {
        const track = testimonialSlider.querySelector('.slider-track');
        const prevBtn = testimonialSlider.querySelector('.slider-arrow.prev');
        const nextBtn = testimonialSlider.querySelector('.slider-arrow.next');
        const cards = testimonialSlider.querySelectorAll('.review-card');

        if (track && prevBtn && nextBtn && cards.length > 0) {
            let currentIdx = 0;

            const getVisibleCards = () => {
                if (window.innerWidth <= 768) return 1;
                if (window.innerWidth <= 1100) return 2;
                return 3;
            };

            const getMaxIdx = () => Math.max(0, cards.length - getVisibleCards());

            // Add dots container
            const dotsContainer = document.createElement('div');
            dotsContainer.className = 'carousel-dots';
            testimonialSlider.appendChild(dotsContainer);

            const createDots = () => {
                dotsContainer.innerHTML = '';
                const totalDots = getMaxIdx() + 1;
                for (let i = 0; i < totalDots; i++) {
                    const dot = document.createElement('span');
                    dot.className = 'dot' + (i === currentIdx ? ' active' : '');
                    dot.onclick = () => {
                        currentIdx = i;
                        updateSlider();
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

            const updateSlider = () => {
                const visibleCards = getVisibleCards();
                const gap = 40; // 2.5rem
                const containerWidth = track.parentElement.offsetWidth;
                const cardWidth = (containerWidth - (visibleCards - 1) * gap) / visibleCards;

                cards.forEach(card => {
                    card.style.flex = `0 0 ${cardWidth}px`;
                });

                const maxIdx = getMaxIdx();
                if (currentIdx > maxIdx) currentIdx = maxIdx;

                const moveX = currentIdx * (cardWidth + gap);
                track.style.transform = `translateX(-${moveX}px)`;
                updateDots();
            };

            nextBtn.addEventListener('click', () => {
                const maxIdx = getMaxIdx();
                currentIdx = (currentIdx >= maxIdx) ? 0 : currentIdx + 1;
                updateSlider();
            });

            prevBtn.addEventListener('click', () => {
                const maxIdx = getMaxIdx();
                currentIdx = (currentIdx <= 0) ? maxIdx : currentIdx - 1;
                updateSlider();
            });

            window.addEventListener('resize', () => {
                createDots();
                updateSlider();
            });
            // Initial call
            createDots();
            setTimeout(updateSlider, 100);
        }
    }

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

    // Interactive Product Gallery (Hover to Swap + Autoplay)
    const mainImg = document.querySelector('.gallery-item.main-image img');
    const thumbItems = document.querySelectorAll('.thumbnails-row .gallery-item');
    let autoplayInterval;
    let currentThumbIdx = 0;

    if (mainImg && thumbItems.length > 0) {
        const dotsContainer = document.querySelector('.gallery-pagination');
        
        // Create dots dynamically
        thumbItems.forEach((_, idx) => {
            const dot = document.createElement('span');
            dot.className = 'gallery-dot';
            dot.addEventListener('click', () => {
                clearInterval(autoplayInterval);
                updateGallery(idx);
                // No automatic resumption on dot click to let user see their choice
                // but resume when they leave the gallery area (handled by other listeners)
            });
            if (dotsContainer) dotsContainer.appendChild(dot);
        });

        const dots = document.querySelectorAll('.gallery-dot');

        const updateGallery = (index) => {
            const thumbImg = thumbItems[index].querySelector('img');
            if (thumbImg) {
                mainImg.src = thumbImg.src;
                thumbItems.forEach(t => t.classList.remove('active'));
                thumbItems[index].classList.add('active');
                
                // Update dots
                dots.forEach(d => d.classList.remove('active'));
                if (dots[index]) dots[index].classList.add('active');
                
                currentThumbIdx = index;
            }
        };

        thumbItems.forEach((item, index) => {
            item.addEventListener('mouseenter', () => {
                clearInterval(autoplayInterval);
                updateGallery(index);
            });
            item.addEventListener('mouseleave', () => {
                startAutoplay();
            });
        });

        const startAutoplay = () => {
            clearInterval(autoplayInterval);
            autoplayInterval = setInterval(() => {
                currentThumbIdx = (currentThumbIdx + 1) % thumbItems.length;
                updateGallery(currentThumbIdx);
            }, 4500); // More relaxed transition (4.5s)
        };

        // Pause autoplay when hovering main image
        mainImg.parentElement.addEventListener('mouseenter', () => clearInterval(autoplayInterval));
        mainImg.parentElement.addEventListener('mouseleave', () => startAutoplay());

        // Initial setup
        updateGallery(0);
        startAutoplay();
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

            window.addEventListener('resize', updateCarousel);
            // Initial call
            setTimeout(updateCarousel, 100);
        }
    }

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

    // Cart Drawer Logic
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

    // Extend global Esc listener for cart
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeCartDrawer();
        }
    });
});
