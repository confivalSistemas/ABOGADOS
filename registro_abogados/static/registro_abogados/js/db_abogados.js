function mostrarPestana(n) {
    var pestanas = document.getElementsByClassName("pestana");
    var cabecera = document.getElementsByClassName("cabecera");
    for (i = 0; i < pestanas.length; i++) {
        if (pestanas[i].className.includes("pestana-activa")) {
            pestanas[i].className = pestanas[i].className.replace("pestana-activa", ""); //replace: reemplazar texto por otro
            cabecera[i].className = cabecera[i].className.replace("cabecera-activa", "");
            break;
        }
    } //todo el ciclo for elimina todas las clases activas de todas las pestañas
    pestanas[n].className += " pestana-activa"; //concatenar texto al texto que estaba
    cabecera[n].className += " cabecera-activa"; //estas 2 lineas permite activar la pestaña que se quiere activar
}