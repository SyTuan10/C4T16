var deleteBtns = document.getElementsByClassName('delete_btn')
for(var i=0; i<deleteBtns.length; i++){
    var deleteBtn = deleteBtns[i];
    deleteBtn.addEventListener('click', function(e){
        var btn = e.target;
        var div = btn.parentNode;
        div.remove();
    })
}