// Initialiseer Swiper met automatische overgang
var swiper = new Swiper('.swiper-container', {
    slidesPerView: 1, // Toon één slide per keer
    spaceBetween: 0, // Geen ruimte tussen slides
    autoplay: {
        delay: 2500, // Tijd (in ms) tussen slides
        disableOnInteraction: false, // Blijf automatisch afspelen als de gebruiker interactie heeft
    },
    loop: true, // Herhaal de slides na de laatste
    effect: 'fade', // Gebruik fade-effect voor de overgang
});
