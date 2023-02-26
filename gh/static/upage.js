let searchbtn = document.getElementById("searchbtn");
searchbtn.onclick = function() {
  let username=document.getElementById("search").value;
  redirect(username);
}