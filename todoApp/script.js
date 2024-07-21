var todos = [];
function add_todo(){
    const todo_box = document.getElementById('todo');
    todos.push(todo_box.value);
    display();
}

function delete_todo(index){
    todos.splice(index,1);
    display();
}

function display(){
    let rows = '';
    let i = 1;
    for (let item of todos){
        rows += `
        <tr>
            <td>${i}</td>
            <td>${item}</td>
            <td><button class="btn btn-success" onclick="delete_todo(${i-1})">Delete</button></td>
        </tr>
        `;
        i++;
    }
    let table = `
    <table class="table">
        <tr>
            <th>SNO</th>
            <th>To-Do</th>
        </tr>
        ${rows}
    </table>
    `;
    const todo_list_tag = document.getElementById('todo-list');
    todo_list_tag.innerHTML = table;
    const todobox = document.getElementById('todo');
    todobox.value = '';
    todobox.focus();
}
