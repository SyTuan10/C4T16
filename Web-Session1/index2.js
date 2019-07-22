// function startClick(){
//     console.log('Start Clicking');
// }

var btn = document.getElementById('btn');
btn.textContent = 'Stop';
btn.addEventListener('click' , function (e){
    console.log(e)
});

var searchBar = document.getElementById('search_bar');
searchBar.value = '';
searchBar.style.backgroundColor = 'black';
searchBar.style.color = 'white';


// var menu = document.getElementById('menu');
// menu.textContent = '';




deleteBtns = document.getElementsByClassName('delete_btn');
for(var i=0; i<deleteBtns.length; i++){
    var deleteBtn = deleteBtns[i];
    deleteBtn.addEventListener('click', function(e){
        var btn = e.target;
        var div = btn.parentNode;
        div.remove();
    })
}