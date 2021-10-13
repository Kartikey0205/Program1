//Project 1: Age in Days
function ageindays(){
    var birthyear=prompt('what year where u born my friend?');
    var ageindays=(2020-birthyear)*365;
    var h1=document.createElement('h2');
    var textanswer=document.createTextNode('Your age in days is  '+" "+ageindays);
    h1.appendChild(textanswer);
    document.getElementById('flexbox').appendChild(h1);
    h1.setAttribute('id','resettext')
    }
    
    
    function reset(){
        document.getElementById('resettext').remove();
    
    }