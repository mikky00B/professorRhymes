// script.js
document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll("[data-filter]");
    const galleryItems = document.querySelectorAll(".gallery-item");
  
    buttons.forEach(button => {
      button.addEventListener("click", () => {
        const filter = button.getAttribute("data-filter");
  
        galleryItems.forEach(item => {
          if (filter === "all" || item.getAttribute("data-event") === filter) {
            item.style.display = "block";
          } else {
            item.style.display = "none";
          }
        });
      });
    });
  });

document.addEventListener("DOMContentLoaded", () => {
    const lightbox = document.getElementById("lightbox");
    const lightboxImg = document.getElementById("lightbox-img");
    const closeBtn = document.querySelector(".lightbox .close");
    const galleryItems = document.querySelectorAll(".gallery-item img");
  
    // Open lightbox when an image is clicked
    galleryItems.forEach(item => {
      item.addEventListener("click", () => {
        lightbox.style.display = "flex";
        lightboxImg.src = item.src; // Use the clicked image's source
      });
    });
  
    // Close lightbox when the close button is clicked
    closeBtn.addEventListener("click", () => {
      lightbox.style.display = "none";
    });
  
    // Close lightbox when clicking outside the image
    lightbox.addEventListener("click", (e) => {
      if (e.target === lightbox) {
        lightbox.style.display = "none";
      }
    });
  });
  