const needLink = document.querySelectorAll('.menu > a')
const position = window.location.pathname


function highlightActivate(){
    needLink.forEach((element)=>{
       
        if(element.getAttribute('href') === position){
            element.style.backgroundColor = "#E9E5EE"
        }
    })
}
highlightActivate()
