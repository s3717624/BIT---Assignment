function raise(div) {
    if (div.className.match(/(?:^|\s)cell(?!\S)/)) {
        div.className = "cellraised";
    }
    else {
        div.className = "cell";
    }
}

function hide() {
    var cells = document.getElementsByClassName('cell'), i;
    for (i = 0; i < cells.length; i += 1) {
        cells[i].style.display = 'none';
    }
}

function show() {
    var cells = document.getElementsByClassName('cell'), i;
    for (i = 0; i < cells.length; i += 1) {
        cells[i].style.display = '';
    }
}

function finish() {
    hide();
    var cells = document.getElementsByClassName("cellraised"), i;
    for (var i = cells.length-1; i >= 0; i--) {
        var x = cells[i].getBoundingClientRect();
        if (x.left >= 97 && x.left < 300) {
            cells[i].style.left = "97px";
        }
        else if (x.left >= 300 && x.left < 503) {
            cells[i].style.left = "300px";
        }
        else if (x.left >= 503 && x.left < 706) {
            cells[i].style.left = "503px";
        }
        else if (x.left >= 706 && x.left < 909) {
            cells[i].style.left = "706px";
        }
        else {
            cells[i].style.left = "909px";
        }
    }

    var cells = document.getElementsByClassName("cellraised"), i;
    for(var i = cells.length-1; i >= 0; i--) {
        cells[i].className = 'cellfinish';
    }

    var code = document.getElementsByClassName("code"), i;
    var k = 0;
    for(var i = code.length-1; i >= 0; i--) {
        var cells = document.getElementsByClassName("cellfinish"), j;
        for(var j = cells.length-1; j >= 0; j--) {
            if ((cells[j].style.background).includes(code[i].innerHTML)) {
                k++;
                j = 0;
            }
        }
    }
    if (k < code.length) {
        var screen = document.getElementById("screennormal");
        var popup = document.getElementById("popupnone");
        screen.id = "screenpopup";
        popup.id = "popup";
    }
}

function closePopup() {
    var screen = document.getElementById("screenpopup");
    var popup = document.getElementById("popup");
    screen.id = "screennormal";
    popup.id = "popupnone";
}
