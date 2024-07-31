let currentIndex = 0;

function showSlide(index) {
    const slides = document.querySelector('.carousel-inner');
    const totalSlides = document.querySelectorAll('.carousel-item').length;

    if (index >= totalSlides) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = totalSlides - 1;
    } else {
        currentIndex = index;
    }

    slides.style.transform = `translateX(-${currentIndex * 100}%)`;
}

function moveSlide(step) {
    showSlide(currentIndex + step);
}

// Inicializa o carrossel com a primeira imagem
showSlide(currentIndex);
