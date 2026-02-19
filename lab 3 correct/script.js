const input = document.getElementById("taskInput"); 
const addBtn = document.getElementById("addBtn"); 
const taskList = document.getElementById("taskList"); 
addBtn.addEventListener("click", addTask); 
function addTask() { 
  const text = input.value.trim(); 
  if (text != ''){
  const li = document.createElement("li"); 
  const checkbox = document.createElement("input"); 
  checkbox.type = "checkbox"; 
  const span = document.createElement("span"); 
  span.textContent = text; 
  span.className = "task"; 
  const deleteBtn = document.createElement("button"); 
  deleteBtn.textContent = "Delete"; 
  deleteBtn.className = "delete-btn"; 
  checkbox.addEventListener("change", function() { 
    if (checkbox.checked) { 
      span.classList.add("done"); 
    } 
    else { 
      span.classList.remove("done"); 
    } 
  }); 
    deleteBtn.addEventListener("click", function() { 
      taskList.removeChild(li); }); 
    li.appendChild(checkbox); 
    li.appendChild(span); 
    li.appendChild(deleteBtn); 
    taskList.appendChild(li); 
  }
  
  
}