const holder_slide = document.querySelectorAll('.main-sec-2-childe')
const holder_slide_text = document.querySelectorAll('.main-sec-2-slide-text2')
const container = document.querySelectorAll('.main-slide-master')
let inital = 0
let ins = 0
function slodeaction() {
    holder_slide[0].classList.add('slide-show')
    inital++
    


holder_slide.forEach((e,value) => {
    if (value == inital ){
        e.classList.add('slide-show')

   
} else if(holder_slide.length == inital){
     inital = 0
    }
    else{
        e.classList.remove('slide-show');
     
        
    }
})

 
};
function slodeaction2() {
    holder_slide_text[0].classList.add('main-sec-2-slide-text-show')
    ins++


    holder_slide_text.forEach((ex,value2) => {
    if ( value2 == ins ){
        ex.classList.add('main-sec-2-slide-text-show')

   
} else if( holder_slide_text.length == ins){
    ins = 0
    }
    else{
        ex.classList.remove('main-sec-2-slide-text-show');
     
        
    }
})

 
}


setInterval(() => {
slodeaction();
slodeaction2();
}, 7000);



const   chevron_right= document.querySelector('.bi-chevron-right')
const chevron_left = document.querySelector('.bi-chevron-left')
const main_holider_peronves = document.querySelector('.main-holider-peronves')
const main_holider_peronves2 = document.querySelector('.main-holider-peronves2')
const slide_investores = document.querySelectorAll('.main-disv-invesy')
 let investor= slide_investores[0].clientWidth
 let normail = 1 


chevron_left.addEventListener('click',()=>{

    if (normail >= slide_investores.length ) {
        

        normail = 0
    } else {
        main_holider_peronves2.style.transform = `translateX(${- investor * normail }px)`
        
        main_holider_peronves2.style.transition = "all 2s" 
        normail++
    }
    clearInterval('clesx',1000)

    console.log(normail);
})

chevron_right.addEventListener('click',()=>{

    if (normail <= slide_investores.length | normail == slide_investores.length  ) {
        
      
        normail = 0
 
    } else {
        main_holider_peronves2.style.transform = `translateX(${ -investor * normail }px)`
        
        main_holider_peronves2.style.transition = "all 2s" 
        normail-- 
    }
        
        clearInterval('clesx')
        

    console.log(normail);
})





function investore() {



    if (normail == slide_investores.length) {
        

        normail = 0
    } else {
        main_holider_peronves2.style.transform = `translateX(${- investor * normail }px)`
        
        main_holider_peronves2.style.transition = "all 2s" 
        normail++
    }

    console.log(normail);
}

  let clesx = setInterval(() => {
testimon_slide()
    
    investore()
}, 9000);



const testimonail_con = document.querySelector('.main-textimonal')
const testimonail_child = document.querySelectorAll('.main-pserson-testi')
let test_chd = testimonail_child[0].clientWidth
let test_chd2 = testimonail_con.clientWidth 




let testi_inital = 1

function testimon_slide() {
    if (testi_inital >= testimonail_child.length -2) {
        testi_inital = 0
    }else if (test_chd2 <= test_chd){
        testimonail_con.style.transform = `translateX(${ test_chd - test_chd2  * testi_inital }px)`
        testi_inital++
alert('heelox')
    }
    
    else {
            testimonail_con.style.transform = `translateX(${-test_chd * testi_inital }px)`
        
        testimonail_con.style.transition = "all 2s" 
        testi_inital++
    }

}

const select_invest_con = document.querySelector('.main-output')


const inputamount = document.querySelector('.main-amount')
const submite = document.querySelector('.submite')
let returns = document.querySelector('.return')

inputamount.addEventListener('keyup',()=>{
if( select_invest_con.value === 'trial Plan'){
    if( Number(inputamount.value) >= 100){

        let resuitx = 6/100 * 50/1
       resuit =  Number(inputamount.value) * Number(resuitx)
       
           returns.value = resuit +' profit'
    }else{
        returns.value = ' The deposit input is less than the subscription plan amount .'

    }
}

else if(select_invest_con.value == 'brozen' ){
    if( Number(inputamount.value) >= 1000){
        

        let resuitx = 3.5/100 * 200/1
        resuit =  Number(inputamount.value) * Number(resuitx)
            
               resut = Math.floor(resuit)
            returns.value = '$'+ resut +' profit'
    }else{
        returns.value = ' The deposit input is less than the subscription plan amount .'

    }
}
else if(select_invest_con.value == 'sliver' ){
        if( Number(inputamount.value) >= 1000){

            let resuitx = 5/100 * 1000/1
            resuit =  Number(inputamount.value) * Number(resuitx)
                
                   resut = Math.floor(resuit)
                returns.value = '$'+ resut +' profit'
        }else{
            returns.value = ' The input is less than the amount.'

        }
}
else if(select_invest_con.value == 'gold' ){
    if( Number(inputamount.value) >= 10000){
        
        let resuitx = 5/100 * 10000/1
        resuit =  Number(inputamount.value) * Number(resuitx)
            
               resut = Math.floor(resuit)
            returns.value = '$'+ resut +' profit'
    }
    else{
        returns.value = ' The deposit input is less than the subscription plan amount .'

    }
}
})


const toggle_con = document.querySelector('.ul-sec-1-first')
const advert_con = document.querySelector('.advert')
const advert_romver = document.querySelector('.advert-romver')
const body = document.querySelector('body')
const toggle_click = document.querySelector('.bi-justify')
const anin = document.querySelector('.anin')

function loads() {
    anin.classList.add('aninhide')
    document.style.transition = 'all 3s  cubic-bezier(0.165, 0.84, 0.44, 1)'
    
}
setTimeout(() => {
    document.addEventListener('load',loads() )
    
}, 2000);


let normaillz = 0


advert_romver.addEventListener('click',()=>{
    advert_con.classList.remove('advertopen')

})
setInterval(() => {
    normaillz++
    if(normaillz == 22){

        advert_con.classList.toggle('advertopen')
        normaillz = 0
    }
    console.log(normaillz, 'hekooo');
}, 6000);
toggle_click.addEventListener('click',()=>{
    toggle_con.classList.toggle('ul-sec-1-first_show')
})



document.addEventListener('scroll',()=>{
    body.style.transition='all 2.5s '
})


