// console.log("Hello World")
const forloopnumber = document.getElementById('forloop-number')
var k = forloopnumber.textContent.length
var str = forloopnumber.textContent.substring(15,k-1)
var b = parseInt(str)+1
var i;
setInterval(()=>{
for(i = 1; i<b;i++){
    var n = i.toString();
    var eventBox= document.getElementById('event-box'.concat(n))

    var countDownBox = document.getElementById('countdown-box'.concat(n))
    var eventDate = Date.parse(eventBox.textContent)

    
    var days = document.getElementById('days'.concat(n)).textContent


    var now = new Date().getTime()
    var newDate = eventDate + parseInt(days)*1000*60*60*24
    var diff = newDate - now

    

    var d = Math.floor(newDate/(1000*60*60*24) - (now/(1000*60*60*24))) 
    var h = Math.floor((newDate/(1000*60*60) - (now/(1000*60*60)))%24)
    var m = Math.floor((newDate/(1000*60) - (now/(1000*60)))%60)
    var s = Math.floor((newDate/(1000) - (now/(1000)))%60)

    if(diff>0){
        countDownBox.innerHTML = d + " days, " + h + " hours, " + m + " minutes, " + s + " seconds"
    }else{
        countDownBox.innerHTML = "Deposit due!!"
    }
}
},1000)
