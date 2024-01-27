container = document.getElementById('centered');

textarea = document.getElementById('whoisInfo');

if (textarea) {
    container.style.height = '100%';

    let text = textarea.value;

    let lines = text.split('\n');

    for (let i = 0; i < lines.length; i++) {
        lines[i] = lines[i].trimStart();
    }

    let newText = lines.join('\n');

    textarea.value = newText;
}
else {
    container.style.height = 'auto';
}

let errorMessage = document.getElementById('error_notify');

setTimeout(() => {
    errorMessage.style.display = 'none';
}, 3000);