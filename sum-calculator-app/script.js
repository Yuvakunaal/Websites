function sum_of_two_nums(){
    const first = document.getElementById("num1").value;
    const second = document.getElementById("num2").value;
    const res = document.getElementById("res");
    if (first.trim()=="" && second.trim()==""){
        alert("Both numbers are empty !!!");
        res.innerHTML = `This text will be replaced with answer after clicking the button`;
    }
    else if (first.trim() == ""){
        alert("Number - 1 is empty !!!");
        res.innerHTML = `This text will be replaced with answer after clicking the button`;
    }
    else if (second.trim() == ""){
        alert("Number - 2 is empty !!!");
        res.innerHTML = `This text will be replaced with answer after clicking the button`;
    }
    else{
        const final = parseInt(first) + parseInt(second);
        res.innerHTML = `Sum of <strong>${first}</strong> and <strong>${second}</strong> is <strong>${final}</strong>`;
    }
}