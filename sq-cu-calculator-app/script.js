function square_of_num(){
    const num = document.getElementById("num").value;
    const res = document.getElementById("res");
    if (num.trim() == ""){
        alert("Number is empty !!!");
        res.innerHTML = `<u>This text will be replaced with answer after clicking any button</u>`;
    }
    else{
        const final = parseInt(num) * parseInt(num);
        res.innerHTML = `Square of <strong>${num}</strong> is <strong>${final}</strong>.`;
    }
}
function cube_of_num(){
    const num = document.getElementById("num").value;
    const res = document.getElementById("res");
    if (num.trim() == ""){
        alert("Number is empty !!!");
        res.innerHTML = `<u>This text will be replaced with answer after clicking any button</u>`;
    }
    else{
        const final = parseInt(num) * parseInt(num) * parseInt(num);
        res.innerHTML = `Cube of <strong>${num}</strong> is <strong>${final}</strong>.`;
    }
}