document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-button');
    const dislikeButtons = document.querySelectorAll('.dislike-button');

    likeButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const postId = this.dataset.postId;
            toggleLike(postId, this);
        });
    });

    dislikeButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const postId = this.dataset.postId;
            toggleDislike(postId, this);
        });
    });

    function toggleLike(postId, button) {
        fetch(`/post/${postId}/like/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                button.innerHTML = `Like (${data.like_count})`;
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function toggleDislike(postId, button) {
        fetch(`/post/${postId}/dislike/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                button.innerHTML = `Dislike (${data.dislike_count})`;
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function getCSRFToken() {
        const cookies = document.cookie.split('; ');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].split('=');
            if (cookie[0] === 'csrftoken') {
                return decodeURIComponent(cookie[1]);
            }
        }
        return null;
    }
});
