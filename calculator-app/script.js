var first='',second='',operator='';
function calculate(val){
    if (val == "+" || val == "-" || val == "*" || val == "/"){
        operator = val;
    }
    else if (val == "="){
        let ifirst = parseInt(first),isecond = parseInt(second);
        switch(operator){
            case "+":
                first = ifirst + isecond;
                break;
            case "-":
                first = ifirst - isecond;
                break;
            case "*":
                first = ifirst * isecond;
                break;
            case "/":
                first = parseInt(ifirst / isecond);
                break;
        }
        second = '';
        operator = '';
    }
    else if (val == "C"){
        first = '';
        second = '';
        operator = '';
    }
    else{
        if (operator == ''){
            first += val;
        }
        else{
            second += val;
        }
    }
    const answer_box = document.getElementById('answer_box');
    const result = first + ' ' + operator + ' ' + second;
    answer_box.value = result.trim();
}