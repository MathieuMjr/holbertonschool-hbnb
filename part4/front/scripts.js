/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  const loggin = document.querySelector('#login-form')
  const errorText = document.querySelector('#error-text')
  // repère l'élément loggin sur la page
  if (loggin) {
    // s'il est présent(login.html, mais pas sur index par ex)
    // écoute le submit du formulaire associé
    // s'il est réalisé, construit un payload et envoi les info
    // en requête post au endpoint de mon API
    loggin.addEventListener('submit', (event) => {
      event.preventDefault(); // évite le refresh de la page ?
      const payload = {
        'email': document.querySelector('input[name=email]').value,
        'password': document.querySelector('input[name=password]').value
      }
      fetch('http://localhost:5000/api/v1/auth/login', {
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
          "Content-Type": "application/json"
        }
      })
      // on va vérifier la réponse de l'API
      .then(response => {
        // si retour 4xx ou 5xx, génère une erreur
        // a récupérer dans .catch
        if (!response.ok) {
          return response.json().then(error => {
            if (response.status === 401){
              throw new Error(error.message || "Invalid credentials")
            }
            else if (response.status === 500){
              throw new Error(error.message || "Internal server error")
            }
            else {
              throw new Error(error.message || "Error")
            }  
          })
        }
        return response.json()
      })
      .then(data => {
        errorText.textContent = "";
        document.cookie = "token=" + data.access_token + "; path=/; samesite=strict"; 
        // ajouter "secure" plus tard
        window.location.href = 'index.html';
      }
      )
      .catch(error => {
        console.error("Error:", error);
        errorText.textContent = error.message;
      });
    });
  }
});

