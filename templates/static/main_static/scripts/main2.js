function tranlated_text_code(){
    let text_code = document.getElementById('text_code').value.trim();

    let csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    let dataAddCep = new FormData()

    dataAddCep.append('text_code', text_code)

    fetch("/decrypt_text_code", {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: dataAddCep

    }).then(function(result){
        return result.json()
    }).then(function(dataAddCep){
        loading()
        setTimeout(function() {
            container_text_result = document.getElementById('container_text_result')
            container_text_result.style.display = 'flex';

            textarea = document.getElementById('text_result');
            textarea.value = ' ';
            textarea.value = dataAddCep['text_tranlated']['code']
            console.log(dataAddCep['text_tranlated']);


            // Criar um único elemento de áudio
            var audioElement = new Audio();

            // Adiciona ouvintes de evento aos botões
            document.getElementById('btnIniciarReproducao').addEventListener('click', function() {
                reproduzirSequencialmente(dataAddCep['text_tranlated']['list_files'], audioElement);
            });

            document.getElementById('btnPausarReproducao').addEventListener('click', function() {
                pausarReproducao(audioElement);
            });
            
           
        }, 3000);
        
        
        
        
    
    })
}






// function reproduzirSequencialmente(caminhos) {
//     var audioAtual = 0;
//     var audioElement = new Audio();

//     function tocarProximoAudio() {
//         if (audioAtual < caminhos.length) {
//             audioElement.src = caminhos[audioAtual];
//             audioElement.play();
//             audioElement.addEventListener('ended', avancarAudio);
//         }
//     }

//     function avancarAudio() {
//         audioAtual++;
//         tocarProximoAudio();
//     }

//     tocarProximoAudio(); // Inicia a reprodução do primeiro áudio

    
// }

function reproduzirSequencialmente(caminhos, audioElement) {
    var audioAtual = 0;

    function tocarProximoAudio() {
        if (audioAtual < caminhos.length) {
            audioElement.src = caminhos[audioAtual];
            audioElement.play();
            audioElement.addEventListener('ended', avancarAudio);
        }
    }

    function avancarAudio() {
        audioAtual++;
        tocarProximoAudio();
    }

    tocarProximoAudio(); // Inicia a reprodução do primeiro áudio
}

function pausarReproducao(audioElement) {
    audioElement.pause();
}

function loading(){

    sectio_page = document.getElementById('container_full_page')

    loader = document.getElementById('loader');
    loader.style.display = 'inline-block';
    sectio_page.style.display = 'flex';

    // Aguardar 3 segundos antes de remover o loader
    setTimeout(function() {
        loader.style.display = 'none';
        sectio_page.style.display = 'none';
    }, 3000);
}


function translatedFile(){
    
}


