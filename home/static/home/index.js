function changeNav(media_query) {
    if (media_query.matches) {
        let x = document.querySelector('.right-side');
        x.style.display = "flex";
    } else {
        let x = document.querySelector('.right-side');
        let y = document.querySelector('.icon')
        x.style.display = "none";
        y.style.display = "block";
    }
}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.icon').onclick = ()=> {
        let x = document.querySelector('.right-side');
        if (x.style.display === "block") {
            x.style.display = "none";
        } else {
            x.style.display = "block";
        }
    }

    media_query = window.matchMedia("(min-width: 640px)");
    changeNav(media_query);
    media_query.addListener(changeNav);

});
