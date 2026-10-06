console.log("Script Loaded");

const button =
document.getElementById("theme-btn");

if(localStorage.getItem("theme")=="dark"){
    document.body.classList.add("dark");
}

button.onclick=function(){
    document.body.classList.toggle("dark");

    if(document.body.classList.contains("dark")){
        localStorage.setItem("theme","dark");
    }
    else{
        localStorage.setItem("theme","light");
    }
}

const box=document.getElementById("delete-box");

box.style.display="flex";
box.style.display="none";

let deleteLink="";
function openDelete(link){
    deleteLink=link;
    box.style.display="flex";
    return false;
}

const yes=document.getElementById("yes-delete");

const no=document.getElementById("no-delete");

no.onclick=function(){
    box.style.display="none";
}

yes.onclick=function(){
    window.location.href=deleteLink;
}

document.body.addEventListener("click",function(){
    console.log("یه جا کلیک شد");
});

console.log("اخر فایل");

const titles=document.querySelectorAll("h3");
console.log(titles);

const title=document.getElementById("title");
console.log(title);

document.addEventListener("DOMContentLoaded", function(){
    const box = document.getElementById("delete-box");
    document.addEventListener("keydown",
    function(event){
        if(event.key === "Escape"){
            box.style.display = "none";
        }
    });

    const title = document.getElementById("title");
    const changeBtn = document.getElementById("change-title");
    changeBtn.addEventListener("click",function(){
        console.log("دکمه تغییر عنوان کلیک شد");
        if(title.innerText === "📒 دفترچه یادداشت من"){
            title.innerText = "JavaScript وارد شد😎";
            title.classList.add("title-special");
        }
        else{
            title.innerText = "📒 دفترچه یادداشت من";
            title.classList.remove("title-special");
        }
    });

});

document.addEventListener("keydown",
    function(event){
        console.log("یک دکمه از کیبرد زده شد", event.key);
    }
);

document.addEventListener("keydown",
    function(event){
        console.log(event);
    }
);

const searchInput = document.getElementById("search-input");
document.addEventListener("keydown",
    function(event){
        if(event.ctrlKey && event.key === "k"){
            event.preventDefault();
            searchInput.focus();
        }
    }
);

searchInput.addEventListener("input",
    function(){
        console.log(searchInput.value);
    }
);


if(searchInput){
searchInput.addEventListener("input",
    function(){
        console.log("کاربر تایپ کرد:", searchInput.value);
        console.log("تعداد حروف:", searchInput.value.length);
        if(searchInput.value === ""){
            console.log("جستجو خالی است");}
        else{
            console.log("در حال جستجو برای:", searchInput.value);
        }   
    }
);
}

document.addEventListener("keydown",
    function(event){
        console.log("کلید:",event.key);
        console.log("Ctrl:",event.ctrlKey);
        console.log("Shift:",event.shiftKey);
        console.log("Alt:",event.altKey);
    }
);

document.addEventListener("click",
    function(event){
        console.log("عنصر:",
            event.target);
        console.log("نوع:",
            event.target.tagName);
    }
);

let clickCount = 0;
document.addEventListener("click",
    function(event){
        clickCount = clickCount + 1;
        console.log("شماره کلیک :", clickCount);
        console.log("عنصر کلیک شده:", event.target);
        console.log("نوع عنصر:", event.target.tagName);
    }
);

document.addEventListener("DOMContentLoaded", function(){

    console.log("HTML کامل آماده شد");

    const clickButton =
    document.getElementById("click-counter-btn");
    const clickCounter =
    document.getElementById("click-counter");

    console.log("دکمه:", clickButton);
    console.log("شمارنده:", clickCounter);

    let count = 0;

    clickButton.addEventListener("click",
        function(){
            count = count + 1;
            clickCounter.innerText = "تعداد کلیک: " + count;
            if(count === 10){
                clickCounter.innerText = "هـــورا یه 10 کلیک رسیدی 😂😂";
            }
        }
    );
});


const testTitle = document.getElementById("title");
console.log("عنوان پیدا شد:", testTitle);



// ============================
// new dars Delegation
// ============================

const testBox = document.getElementById("js-test-box");
testBox.addEventListener("click", function(event){
    if(event.target.tagName === "BUTTON"){
        return;
    }
    const action = event.target.dataset.action;
    if(action === "favorite"){
        event.target.classList.toggle("active");
    }
    if(action === "done"){
        event.target.classList.toggle("active");
    }
    if(action === "delete"){
        event.target.remove();
    }
});

// ============================
// LocalStorage
// ============================

const storageName = document.getElementById("storage-name");
const storageSaveBtn = document.getElementById("storage-save-btn");
const storageLoadBtn = document.getElementById("storage-load-btn");
const storageDeleteBtn = document.getElementById("storage-delete-btn");
const storageResult = document.getElementById("storage-result");

storageSaveBtn.addEventListener("click", function(){
    const name = storageName.value;
    localStorage.setItem("name", name);
    storageResult.innerText = "اسم ذخیره شد.";
});

storageLoadBtn.addEventListener("click", function(){
    const savedName = localStorage.getItem("name");
    storageResult.innerText = "اسم ذخیره شده:" + savedName;
});

storageDeleteBtn.addEventListener("click", function(){
    localStorage.removeItem("name");
    storageResult.innerText = "اسم پاک شد:" ;
});

//====================
// test
//====================

const saveUserBtn = document.getElementById("save-user-btn");
const loadUserBtn = document.getElementById("load-user-btn");
const userResult = document.getElementById("user-result");

saveUserBtn.addEventListener("click", function(){
    const user = {
        name: "Bahram",
        age: 28,
        language: "Python + JavaScript"
    };
    const userText = JSON.stringify(user);
    localStorage.setItem("user", userText);
    userResult.innerText = "اطلاعات کاربر ذخیره شد.";
});

loadUserBtn.addEventListener("click", function(){
    const savedUser = localStorage.getItem("user");
    const user = JSON.parse(savedUser);
    userResult.innerText = 
        "سلام" + user.name +
        " | سن: " + user.age;
});


// =================
// animation
//==================

function showNotification(message, type = "success") {
    const notification = document.createElement("div");
    notification.innerText = message;
notification.classList.add("notification");
    notification.classList.add(type);
document.body.appendChild(notification);
    setTimeout(() => {
        notification.classList.add("hide");
        setTimeout(() => {
            notification.remove();
        }, 500);
    }, 3000);
}

const notificationButton = document.getElementById("test-notification");

if (notificationButton) {
    notificationButton.addEventListener("click", () => {
        showNotification("آفرین جاواااا داره کار میکنه.");
        showNotification("نوت ذخیزه شد.", "success");
        showNotification("مشکلی پیش آمد.", "error");
        showNotification("مواظب باش.", "warning");
    });
}



// =================
// game
//==================



// =================================
// 🎮 GAME - TARGET
// =================================
