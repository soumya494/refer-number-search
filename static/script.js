document.getElementById("searchBtn").addEventListener("click", searchNumber);

document.getElementById("mobile").addEventListener("keypress", function(e){

if(e.key==="Enter"){

searchNumber();

}

});

async function searchNumber(){

const number=document.getElementById("mobile").value.trim();

if(number.length!=10){

alert("Enter Valid 10 Digit Number");

return;

}

document.getElementById("result").innerHTML="<div class='loading'>🔍 Searching...</div>";

const response=await fetch("/search",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

number:number

})

});

const data=await response.json();

if(data.found){

document.getElementById("result").innerHTML="<div class='success'>✅ FOUND</div>";

}else{

document.getElementById("result").innerHTML="<div class='error'>❌ NOT FOUND</div>";

}

document.getElementById("mobile").focus();
document.getElementById("mobile").select();

}