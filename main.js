/* ╔══════════════════════════════════╗ */
/* ║         LOADING ANIMATION        ║ */
/* ╚══════════════════════════════════╝ */

const loadingTextElement = document.getElementById("periods");
let dotCount = 0;
const maxDots = 3;

/**
 * Adds dots to end of text
 */
function animateDots() {
    dotCount = (dotCount % (maxDots + 1)); 
    let dots = '';
    for (let i = 0; i < dotCount; i++) {
      dots += '.';
    }
    if (loadingTextElement) {
    loadingTextElement.textContent = "angel clarke" + dots;
    }
    dotCount++;
}

setInterval(animateDots, 500);

/* ╔══════════════════════════════════╗ */
/* ║        HOMEPAGE SLIDESHOW        ║ */
/* ╚══════════════════════════════════╝ */
document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".heroslideshow .slide");
  const totalSlides = slides.length;

  console.log("Found slides:", totalSlides);

  if (totalSlides === 0) return; // nothing to do if no slides

  let currentIndex = 0;
  let timerId = null;

  function showSlide(index) {
    // keep index in range 0..totalSlides-1
    currentIndex = (index + totalSlides) % totalSlides;

    slides.forEach((slide, i) => {
      slide.classList.toggle("active", i === currentIndex);
    });
  }

  function nextSlide() {
    showSlide(currentIndex + 1);
  }

  // initial state
  showSlide(0);

  // auto-advance every 7 seconds
  timerId = setInterval(nextSlide, 7000);
});


/* ╔══════════════════════════════════╗ */
/* ║         CAROUSEL LOGIC           ║ */
/* ╚══════════════════════════════════╝ */

const carouseltrack = document.querySelector(".carouseltrack");
const nextbutton = document.getElementById("nextbutton");
const backbutton = document.getElementById("backbutton");

if (carouseltrack && nextbutton && backbutton) {
  const carouselwindow = document.querySelector(".carousel");
  const cards = Array.from(document.querySelectorAll(".carouselitem"));
  let index = 0;

  function getCarouselSpecs() {
    const cardwidth = cards[0].getBoundingClientRect().width; // Keeps track of active decimal widths
    const gap = 27;
    const step = cardwidth + gap;

    // Use clientWidth to fetch inner structural width minus scrollbars
    const visibleWidth = carouselwindow.clientWidth;
    
    // Add gap adjustments to get clean integer divisions for desktop multi-columns
    const visibleCount = Math.max(1, Math.floor((visibleWidth + gap) / step));

    // Caps your slide index safely based on what is currently displayed on screen
    const maxIndex = Math.max(0, cards.length - visibleCount);
    return { step, maxIndex };
  }

  /**
   * Function: Updates the carousel for when you scroll past it
   */
  function updateCarousel() {
    const { step } = getCarouselSpecs();
    carouseltrack.style.transform = `translateX(-${index * step}px)`;
  }

  backbutton.addEventListener("click", () => {
    const { maxIndex } = getCarouselSpecs();
    if (index == 0) {
      index = maxIndex;
    } else {
      index -= 1;
    }
    updateCarousel();
  })

  nextbutton.addEventListener("click", () => {
    const { maxIndex } = getCarouselSpecs();
    if (index < maxIndex) {
      index++;
    } else {
      index = 0;
    }
    updateCarousel();
  })

  window.addEventListener("load", updateCarousel);
  window.addEventListener("resize", () => {
    const { maxIndex } = getCarouselSpecs();
    if (index > maxIndex) index = maxIndex;
    updateCarousel();
  });
}

/* ╔══════════════════════════════════╗ */
/* ║          DOWN ARROW              ║ */
/* ╚══════════════════════════════════╝ */

const downArrow = document.getElementById("downArrow");
const nextSection = document.querySelector(".aboutmehomepage");
if (downArrow && nextSection) {
  downArrow.addEventListener("click", () => {
    window.scrollTo({
      top: nextSection.offsetTop - 80,
      behavior: "smooth"
    });
    
  })
}

/* ╔══════════════════════════════════╗ */
/* ║       SUBMIT BUTTON              ║ */
/* ╚══════════════════════════════════╝ */

const contactform = document.querySelector(".contact-form");
const popup = document.getElementById("popup");
const closepopupbutton = document.getElementById("closepopup")
if (contactform) {
    contactform.addEventListener("submit", (event) => {
    event.preventDefault();
    popup.classList.add("show");
    const formData = new FormData(contactform);

    formData.append("form-name", "contact");

    if (window.grecaptcha) {
      const recaptchaResponse = window.grecaptcha.getResponse();
      formData.append("g-recaptcha-response", recaptchaResponse);
    }

    // Send data to Netlify via AJAX
    fetch("/", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(formData).toString(),
    })
      .then((response) => {
        if (response.ok) {
          popup.classList.add("show"); // Display your popup
          contactform.reset();         // Clear the form fields
        } else {
          console.error("Netlify server submission failed");
        }
      })
      .catch((error) => console.error("Network error:", error));
  })
}

if (closepopupbutton) {
  closepopupbutton.addEventListener("click", () => {
    popup.classList.remove("show");
  })
}

/* ╔══════════════════════════════════╗ */
/* ║    TRANSPARENCY ON SCROLL        ║ */
/* ╚══════════════════════════════════╝ */

const topbar = document.getElementById("topbar");
if (topbar) {
  window.addEventListener("scroll", () => {
    if (window.scrollY > 80) {
      topbar.style.backgroundColor = "rgba(21, 22, 28, 0.9)";
      downArrow.style.opacity = 0;
    } else {
      topbar.style.backgroundColor = "rgba(21, 22, 28, 0.53)";
    }
  });
}

/* ╔══════════════════════════════════╗ */
/* ║            FUN FACT CARDS        ║ */
/* ╚══════════════════════════════════╝ */

const funfacts = [
  "I've beaten 10 escape rooms", 
  "I have over 2500 hours playing Rainbow Six Siege", 
  "I love travelling", 
  "I didn't start coding until I learned in university",
  "My best friend is a dog named Opal"];

const funfactcard = document.querySelectorAll(".funfactcard");

funfactcard.forEach((card, index) => {
  card.addEventListener("click", () => {
    const innerText = card.querySelector(".funfacttext")
    if (innerText) {
      innerText.textContent=funfacts[index];
      card.classList.toggle("flipped");
    }
  })
})

/* ╔══════════════════════════════════╗ */
/* ║         PROJECT FILTERING        ║ */
/* ╚══════════════════════════════════╝ */
const projectItems = document.querySelectorAll('.projectitem');
const filterInputs = document.querySelectorAll('input[type="checkbox"].checkboxes');
let filteredProjects = [];
if (projectItems.length && filterInputs.length) {
  // Listen for changes in the checked boxes
  filterInputs.forEach(input => {
      input.addEventListener('change', applyFilters);
  });

  /**
   * Gets an array of all the checked boxes on the filters
   * @param {*} groupName The group of filters to check from
   * @returns array of all checked boxes
   */
  function getCheckedValues(groupName) {
      return Array.from(
          document.querySelectorAll(`input[name="${groupName}"]:checked`)
      ).map(el => el.value.trim());
  }

  const sortingAlgo = document.getElementById("sortingalgo");
  if (sortingAlgo) {
    sortingAlgo.addEventListener("change", () => {
      sortProjects(sortingAlgo.value);
      showPage(1)
    })
  }

  /**
   * Go through every card and see if it matches the filters, then append to filteredProjects
   */
  function applyFilters() {
      const selectedLanguages = getCheckedValues('language');
      const selectedYears = getCheckedValues('year');
      const selectedKinds = getCheckedValues('kind');

      filteredProjects = [];
      projectItems.forEach(item => {

          const matchesLanguage = 
              selectedLanguages.length === 0 ||
              selectedLanguages.includes(item.dataset.language);

          const matchesYear =
              selectedYears.length === 0 ||
              selectedYears.includes(item.dataset.year);

          const matchesKind =
              selectedKinds.length === 0 ||
              selectedKinds.includes(item.dataset.kind);

          if (matchesLanguage && matchesYear && matchesKind) {
            filteredProjects.push(item);
          }});
      showPage(1);
  }

  function sortProjects(method) {
    filteredProjects = Array.from(filteredProjects);

    if (method == "newest") {
      filteredProjects.sort((a, b) => {
        return Number(b.dataset.year) - Number(a.dataset.year);
      })
    }

    if (method =="oldest") {
      filteredProjects.sort((a, b) => {
        return Number(a.dataset.year) - Number(b.dataset.year);
      })
    }

    if (method == "nameaz") { 
      filteredProjects.sort((a, b) => {
        const A = a.querySelector("h2").textContent.toLowerCase();
        const B = b.querySelector("h2").textContent.toLowerCase();
        return A.localeCompare(B);
      })
    }

    if (method == "nameza") {
      filteredProjects.sort((a, b) => {
        const A = a.querySelector("h2").textContent.toLowerCase();
        const B = b.querySelector("h2").textContent.toLowerCase();
        return B.localeCompare(A);
      })
    }
  }
  
  const projectsPerPage = 4;
  let currentPage = 0;

  /**
   * Shows items on the given page 
   * @param {*} pageNumber What page to display
   * @returns Nothing
   */
  function showPage(pageNumber){
    // Calculate total pages
    const totalPages = Math.ceil(filteredProjects.length / projectsPerPage) || 1;

    // Edge cases   
    currentPage = pageNumber;
    if (currentPage < 1) currentPage = 1;
    if (currentPage > totalPages) currentPage = totalPages;

    // hide all cards at first
    projectItems.forEach(item => {
      item.style.display = "none";
    });
    
    // Calculate indexes
    const startingIndex = (currentPage-1) * projectsPerPage;
    const endingIndex = startingIndex + projectsPerPage;

    // Set cards to display within the given indexes
    for (let i = startingIndex; i < endingIndex; i ++) {
      if (filteredProjects[i] != null) {
        filteredProjects[i].style.display = "flex";
      }
    }

    // Update display text
    const pageText = document.getElementById("displayText");
    if (pageText) {
      pageText.textContent = `Displaying page ${currentPage} of ${totalPages}...`;
      console.log("updated text to:", pageText.textContent);
    }
  }

  // Hook up previous and next buttons to show new page
  let previousButton = document.getElementById("previouspage");
  previousButton.addEventListener("click", () => {
    showPage(currentPage - 1);
  })

  let nextButton = document.getElementById("nextpage");
  nextButton.addEventListener("click", () => {
    showPage(currentPage + 1);
  })
  
  applyFilters();
}