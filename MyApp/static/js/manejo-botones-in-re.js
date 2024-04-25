window.addEventListener('beforeunload', function(event) {
    logoutUser();
});

function logoutUser() {
    fetch("{% url 'logout' %}", {
        method: 'POST',
        credentials: 'same-origin', // Incluye las cookies en la solicitud
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    }).then(response => {
        if (response.ok) {
            console.log('Sesión cerrada exitosamente');
        } else {
            console.error('Error al cerrar sesión');
        }
    }).catch(error => {
        console.error('Error al cerrar sesión:', error);
    });
}
