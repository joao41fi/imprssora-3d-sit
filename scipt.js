function sartvidio(){
    navigator.mediaDevices.getUserMedia({video:true}).then(stream=>{


        const videoElement = document.querySelector("#video")
        videoElement.src0bject = stream
    }).catch(error=>{console.log(error)})

}
window.addEventListener("DOMContentLoaded", sartvidio)//seve para ver se tem algun evento observer 