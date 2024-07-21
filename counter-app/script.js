var count = 0;
function inc(){
    const offset_box = document.getElementById('offset');
    count+= +offset_box.value;
    document.getElementById('counter').innerHTML = count;
}
function dec(){
    const offset_box = document.getElementById('offset');
    count-= +offset_box.value;
    if (count >= 0){
        document.getElementById('counter').innerHTML = count;
    }
    else{
        alert("Can't decrement 0 !!!")
    }
}