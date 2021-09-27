let btnHome = document.querySelector('.btnHome')
let idForm = document.getElementById('idForm').getAttribute("value")

if (idForm === '2') {
    btnHome.addEventListener('click', () => {
        window.location.href = '/';
    });
}