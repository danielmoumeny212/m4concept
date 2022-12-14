const navToggler = document.querySelector("#menu-btn");

const nav = document.querySelector(".navbar");
const pathname = location.pathname.includes('offers/') ? location.pathname : ''; 

navToggler.addEventListener("click", () => {
  navToggler.classList.toggle("active");
  nav.classList.toggle("active");
});

window.addEventListener("scroll", () => {
  navToggler.classList.remove("active");
  nav.classList.remove("active");

  let maxHeight = window.document.body.scrollHeight - window.innerHeight;
  let percentage = (window.scrollY / maxHeight) * 100;

  document.querySelector(".scroll-indicator").style.width = percentage + "%";
});

async function submitForm(formInput, csrftoken) {
  const request = await fetch(window.location.href, {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin",
    body: new FormData(formInput),
  });
  return await request.json();
}


const handleFormSubmission = (form, callback) => {
  form.addEventListener("submit", callback);
};
const selectCommonHtmlElements = () => {
  const form = document.querySelector("form");
  const textAction = document.querySelector(".text-action");
  const nodeInputs = document.querySelectorAll("input");
  const loading = document.querySelector(".load");
  const inputsW = Array.from(nodeInputs);
  const [csrf, ...inputs] = inputsW;
  return {
    form,
    textAction,
    csrf,
    loading,
  };
};


const initLoading = (loading, textAction) => {
  loading.style.display = "block";
  textAction.classList.remove("success");
  textAction.classList.remove("error");
}
const errorLoading = (loading, textAction , response) => {
  textAction.classList.remove("success");
  loading.style.display = "none";
  textAction.classList.add("error");
  textAction.textContent = response.message;
}

const successLoading = (loading, textAction , response) => {
  textAction.classList.remove("error");
  loading.style.display = "none";
  textAction.classList.add("success");
  textAction.textContent = response.message;
}


const contactPageScript = () => {
  const { form, textAction, loading, csrf} =
  selectCommonHtmlElements();
  handleFormSubmission(form,  async (e) => {
    e.preventDefault();
    
    let csrftoken = csrf.value;
    initLoading(loading, textAction); 
    const response = await submitForm(form, csrftoken);
    if (response.status !== "success") {
       errorLoading(loading, textAction, response)
      return;
  }
    successLoading(loading, textAction, response)
    form.reset();
  });

};
const applyingScript = () => {
  const { form, textAction, loading, csrf} =
  selectCommonHtmlElements();
  
  handleFormSubmission(form,  async (e) => {
    e.preventDefault();
    let csrftoken = csrf.value;
    initLoading(loading, textAction); 
    const response = await submitForm(form, csrftoken);
    if (response.status !== "success") {
       errorLoading(loading, textAction, response)
      return;
  }
    successLoading(loading, textAction, response)
    form.reset();
  });

}
const homeScript = () => {
  const swiper = new Swiper(".partners-slider", {
    loop: true,
    autoplay: {
      delay: 3000,
    },
    spaceBetween: 10,
    grapCursor: true,

    centeredSlides: true,
    breakpoints: {
      0: {
        sliderPerView: 1,
      },
      760: {
        sliderPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      991: {
        slidesPerView: 3,
      },
    },
  });
};

switch (location.pathname) {
  case "/":
    homeScript();
    break;
  case "/contact-us":
    contactPageScript();
    break;
  case pathname:
    applyingScript();
    break;
  default:
    
}
