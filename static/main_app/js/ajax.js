// const button = document.getElementById('but');
// const h_ = document.getElementById('h1_');


   function sendRequestSql(method,url,data){
    return new Promise((resolve,reject)=>{
        xhr = new XMLHttpRequest()
        xhr.open(method, url)
        xhr.setRequestHeader('X-CSRFToken',document.cookie.split('csrftoken=')[1].split(';')[0])
        xhr.responseType = 'json';
        xhr.onload = ()=>{
            if (xhr.status>=400){
                reject('<h3>Сервер не может обработать данный запрос</h3>')
            }else{

            }
        }
        xhr.onerror = ()=>{
            reject('<h3>Сервер не может обработать данный запрос</h3>')
        }
        xhr.send(data)
    })
}





// $('#form2').click(function () {
//     console.log('ff')
//     let requestURL_custom = 'go/'
//     let data = '<h1>ggggggg</h1>'
//     sendRequestSql('GET',requestURL_custom,data).then(result=>{
//                         console.log(result)
//
//                     })
// })


$('li a').click(function (e) {
    e.stopPropagation()
})