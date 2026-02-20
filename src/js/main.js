
import '../assets/CP_Main_Catalogue.pdf';
import '../assets/CP_Mini_Catalogue.pdf';

const initPageTransitions = () => {

    if (!document.getElementById('page-loader')) {
        const loader = document.createElement('div');
        loader.id = 'page-loader';
        document.body.appendChild(loader);
    }

    const loader = document.getElementById('page-loader');


    document.addEventListener('click', (e) => {
        const link = e.target.closest('a');
        if (
            link &&
            link.href &&
            link.href.startsWith(window.location.origin) &&
            !link.getAttribute('target') &&
            !link.href.includes('#')
        ) {
            e.preventDefault();
            const targetUrl = link.href;


            loader.classList.add('animate');

            setTimeout(() => {
                window.location.href = targetUrl;
            }, 300);
        }
    });


    window.addEventListener('pageshow', (event) => {
        if (event.persisted && loader) {
            loader.classList.remove('animate');
        }
    });
};


const initIcons = () => {
    if (window.lucide) {
        window.lucide.createIcons();
    }
};


const initSwiper = () => {
    const swiperEl = document.querySelector(".mySwiper");
    if (swiperEl && window.Swiper) {
        new window.Swiper(".mySwiper", {
            slidesPerView: 1.1,
            spaceBetween: 20,
            loop: true,
            speed: 1000,
            autoplay: {
                delay: 4000,
                disableOnInteraction: false,
            },
            breakpoints: {
                640: {
                    slidesPerView: 1.2,
                    spaceBetween: 30,
                },
                1024: {
                    slidesPerView: 1.3,
                    spaceBetween: 30,
                }
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            grabCursor: true,
        });
    }
};


const initHeaderScroll = () => {
    window.addEventListener('scroll', () => {
        const header = document.querySelector('header');
        if (header) {
            if (window.scrollY > 50) {
                header.classList.add('py-2');
                header.classList.remove('py-4');
            } else {
                header.classList.add('py-4');
                header.classList.remove('py-2');
            }
        }
    });
};


const initMobileMenu = () => {
    const toggleBtn = document.getElementById('mobile-menu-toggle');
    const closeBtn = document.getElementById('mobile-menu-close');
    const menu = document.getElementById('mobile-menu');
    const menuLinks = document.querySelectorAll('#mobile-menu a');

    if (toggleBtn && menu) {
        toggleBtn.addEventListener('click', () => {
            menu.classList.remove('translate-x-full');
            document.body.style.overflow = 'hidden';
        });
    }

    if (closeBtn && menu) {
        closeBtn.addEventListener('click', () => {
            menu.classList.add('translate-x-full');
            document.body.style.overflow = '';
        });
    }


    menuLinks.forEach(link => {
        link.addEventListener('click', () => {
            menu.classList.add('translate-x-full');
            document.body.style.overflow = '';
        });
    });
};


if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        initPageTransitions();
        initIcons();
        initSwiper();
        initHeaderScroll();
        initMobileMenu();
    });
} else {
    initPageTransitions();
    initIcons();
    initSwiper();
    initHeaderScroll();
    initMobileMenu();
}


