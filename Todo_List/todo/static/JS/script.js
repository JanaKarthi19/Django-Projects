
const showPass = document.getElementById("show_pass")
const passInput = document.getElementById("log_pass")

showPass.addEventListener("change", function(){
    passInput.type = this.checked ? "text" : "password"
})

const reShowPass = document.getElementById("re_show_pass")
const rePassInput = document.getElementById("re_log_pass")

reShowPass.addEventListener("change", function(){
    rePassInput.type = this.checked ? "text" : "password"
})