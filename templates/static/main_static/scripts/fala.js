var dropArea = document.getElementById('drop-area');
var fileInput = document.getElementById('fileInput');
var resultadoTextarea = document.getElementById('resultado');

dropArea.addEventListener('dragover', function (e) {
  e.preventDefault();
  dropArea.style.borderColor = '#333';
});

dropArea.addEventListener('dragleave', function () {
  dropArea.style.borderColor = '#ccc';
});

dropArea.addEventListener('drop', function (e) {
  e.preventDefault();
  dropArea.style.borderColor = '#ccc';

  var file = e.dataTransfer.files[0];
  if (isFileTxt(file)) {
    readFile(file);
  } else {
    alert('Por favor, selecione um arquivo de texto (.txt).');
  }
});

fileInput.addEventListener('change', function () {
  var file = fileInput.files[0];
  if (isFileTxt(file)) {
    readFile(file);
  } else {
    alert('Por favor, selecione um arquivo de texto (.txt).');
  }
});

function isFileTxt(file) {
  return file && file.type === 'text/plain';
}

function readFile(file) {
  var reader = new FileReader();

  reader.onload = function (e) {
    var conteudo = e.target.result;
    resultadoTextarea.value = conteudo;
  };

  reader.readAsText(file);
}