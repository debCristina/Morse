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
        console.log(dataAddCep['text_tranlated'])
        
        
    
    })
}