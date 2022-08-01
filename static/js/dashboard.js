const chevron = document.querySelectorAll('.bi-chevron-down')
const top_bar = document.querySelector('.bi-text-paragraph')
const con_hover = document.querySelector('.main-one-con')
const main_all_con = document.querySelector(' .xmain-consa')
const main_all_con2 = document.querySelectorAll('.main-lef')
const hiddenc = document.querySelectorAll('.hiddenc')
let ticks = 0
top_bar.addEventListener('click',()=>{
    main_all_con.classList.toggle('xmain-consa-madie')
    main_all_con2.forEach((e,value) => {
    e.classList.toggle('main-lefop')
    e.style.transition= "all .5s linear"
    
            
            hiddenc.forEach((ex,valuex) => {
                    ex.classList.remove('open-link')
                    ex.style.transition= "all .5s linear"
    
               
    
     
     
      
    });
    

});
    chevron.forEach((e,value) => {
    e.classList.toggle('main-lefop')
    e.style.transition= "all .5s linear"


});
})
con_hover.addEventListener('mouseover',()=>{
    main_all_con.classList.remove('xmain-consa-madie')
    main_all_con2.forEach((e,value) => {
    e.classList.remove('main-lefop')
    

});
// document.addEventListener("mouseover")
    chevron.forEach((e,value) => {
    e.classList.remove('main-lefop')
    e.style.transition= "all .5s linear"
    


});
})

let ff = true

chevron.forEach((e,value) => {
    
    e.addEventListener('click',()=>{
        
        hiddenc.forEach((ex,valuex) => {
            if (value == valuex ){
                ex.classList.toggle('open-link')
                ex.style.transition= "all .5s linear"

            }
            else{
                ex.classList.remove('open-link')
         
          ex.style.transition= "all .5s linear"

 
 
            }
        });
     })
});


  









  