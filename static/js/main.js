document.addEventListener('DOMContentLoaded', function() {
    const voteButtons = document.querySelectorAll('.vote-btn');

    voteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();

            const mediaId = this.dataset.id;
            const voteType = this.dataset.type;
            const url = `votes/vote/${mediaId}/`;

            const csrftoken = getCookie('csrftoken');

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrftoken,
                },
                body: `vote_type=${voteType}`
            })
            .then(response => {
                if (!response.ok) {
                    // Se o usuário não estiver logado, o servidor retornará um erro 403 (Forbidden)
                    if (response.status === 403) {
                         alert('Você precisa estar logado para votar!');
                         // Opcional: redirecionar para a página de login
                         // window.location.href = '/admin/login/';
                    }
                    throw new Error('A requisição falhou.');
                }
                return response.json();
            })
            .then(data => {
                // Encontre o card correspondente para atualizar os votos
                const card = this.closest('.card');
                const likeButton = card.querySelector('.text-like');
                const dislikeButton = card.querySelector('.text-dislike');
                
                likeButton.innerHTML = `<i class="bi bi-hand-thumbs-up-fill"></i> ${data.likes}`;
                dislikeButton.innerHTML = `<i class="bi bi-hand-thumbs-down-fill"></i> ${data.dislikes}`;
            })
            .catch(error => {
                console.error('Erro:', error);
            });
        });
    });

    // Função para pegar o token CSRF dos cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    } 
});