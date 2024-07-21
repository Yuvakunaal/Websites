var cells = ['','','','','','','','',''];
turn = "X";
function clearboard(){
    cells = ['','','','','','','','',''];
    turn = "X";
    loadboard();
}

function loadboard(){
    for(let i=0;i<9;i++){
        const box_id = "box"+(i+1);
        const box_tag = document.getElementById(box_id);
        box_tag.innerHTML = cells[i];
    }
    document.getElementById('turn').innerHTML = turn;
}

function play(event){
    const box_id = event.target.id;
    const box_index = parseInt(box_id[box_id.length-1])-1;
    if (cells[box_index] != ''){
        return;
    }
    cells[box_index] = turn;
    if(turn == "X"){
        turn = "O";
    }
    else{
        turn = "X";
    }
    loadboard();

}