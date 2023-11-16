let header=document.querySelector(".byrger");
let burger=document.querySelector(".burger");

burger.addEventListener("click",function(){
    if(header.style.display== 'none'){
      header.style.display = 'block'
    }
    else{
      header.style.display = 'none'
    }
})