// FUNCTIONS DEFINITIONS
// --- Function to fetch place ---------------------
async function fetchPlaces(token) {
  const response = await fetch('http://localhost:5000/api/v1/places/', {
    method: "GET",
    headers: {
      }
  });
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.message || 'An error occured while loading Places');
  }
  return await response.json();
}

// --- Login function ----------------------------------------------
async function login(payload) {
  const response = await fetch('http://localhost:5000/api/v1/auth/login', {
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
          "Content-Type": "application/json"
        }
  });
  if (!response.ok) {
    const error = await response.json();
    if (response.status === 401) {
      throw new Error(error.message || 'Invalid credentials')
    }
    else if (response.status === 500) {
      throw new Error(error.message || 'Internal server')
    }
    else {
      throw new Error(error.message || "Error")
    }
  }
  return await response.json();
}

// --- GET COOKIE BY NAME
function getCookie(name) {
// chope le cookie par nom, pour un token : mettre token
// le cookie est uen string avec des infos nom=valeur séparé par des ;
// on peut extraire l'info qu'on veut du cookie en donnant "nom" à 
// la fonction
  const cookie = document.cookie.split("; ");
  for (const element of cookie) {
    const [key, value] = element.split("=");
    if (key === name) return value;
  }
  return null;
}

//--- DISPLAY PLACES ----------------------------------------------
function displayPlaces(places) {
  const placeSection = document.querySelector('#places-list');
    places.forEach(place => {
      const placeCard = document.createElement('div');
      placeCard.classList.add('place-card');
      const placeImg = document.createElement('img');
      placeImg.src = "images/picture.jpg";
      placeImg.alt = 'picture of the place';
      placeImg.classList.add('index-place-image');
      placeCard.appendChild(placeImg);
      const placeTitle = document.createElement('h4');
      placeTitle.textContent = place.title;
      placeCard.appendChild(placeTitle);
      const placePrice = document.createElement('p');
      placePrice.textContent = place.price;
      placeCard.appendChild(placePrice);
      const placeDetails = document.createElement('a');
      placeDetails.classList.add('details-button');
      placeDetails.href='place.html'; //devra envoyer l'id de la place pour affichage spécifique
      placeDetails.textContent = 'View details'
      placeCard.appendChild(placeDetails);
      placeSection.appendChild(placeCard);
    });
}

// ------------------------------------------------------------------//
// --- SCRIPT -------------------------------------------------------//

document.addEventListener('DOMContentLoaded', async () => {
  // header include
  await fetch('header.html')
  .then(response => response.text())
  .then(html => {document.querySelector('header').innerHTML = html;});
  // footer include
  await fetch('footer.html')
  .then(r => r.text())
  .then(html => {document.querySelector('footer').innerHTML = html})

  //---CHECK IF LOGGED / LOG BUTTONS AND LINK
  const token = getCookie('token');
  if (token) {
    const loginNav = document.getElementById('login-link');
    loginNav.textContent = 'logout';
    const loginButton = document.querySelector('.login-button')
    loginButton.textContent = 'logout';
    loginButton.addEventListener('click', () => {
      document.cookie = "token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC; samesite=strict"; 
      loginButton.removeAttribute('href')
      window.location.href = 'index.html';
    })
    loginNav.addEventListener('click', () => {
      document.cookie = "token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC; samesite=strict"; 
      loginNav.removeAttribute('href');
      window.location.href = 'index.html';
    })
  }
  //---FETCH PLACES AND DISPLAY PLACES CARDS
  try {
  const places = await fetchPlaces(token);
  if (places) {
    const placeSection = document.querySelector('#places-list');
    displayPlaces(places);
    const filter = document.getElementById('price-filter')
  filter.addEventListener('change', (event) => {
    const maxPrice = event.target.value === 'all' ? Infinity : Number(event.target.value);
    placeSection.innerHTML = "";
    let filteredPlaces = places;
    filteredPlaces = places.filter(p => p.price <= maxPrice);
    displayPlaces(filteredPlaces);
  });
  }
  } catch (error) {
    console.error("Error: ", error)
  }

  //---LOGIN----------------------------------------------------------- 
  const loggin = document.querySelector('#login-form')
  const errorText = document.querySelector('#error-text')
  // repère l'élément loggin sur la page
  if (loggin) {
    // s'il est présent(login.html, mais pas sur index par ex)
    // écoute le submit du formulaire associé
    // s'il est réalisé, construit un payload et envoi les info
    // en requête post au endpoint de mon API
    loggin.addEventListener('submit', async (event) => {
      event.preventDefault(); // évite le refresh de la page ?
      const payload = {
        'email': document.querySelector('input[name=email]').value,
        'password': document.querySelector('input[name=password]').value
      }
      try {
        const data = await login(payload);
        errorText.textContent = "";
        document.cookie = "token=" + data.access_token + "; path=/; samesite=strict"; 
        // ajouter "secure" plus tard
        window.location.href = 'index.html';
        } catch (error) {
          errorText.textContent = error.message;
        }
    });
  }
});

