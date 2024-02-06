function ajax(src, callback){
    fetch(src).then(function (response){
        return response.json();
    }).then(function (result){callback(result)});
}


function render(data){
    var list = document.createElement('div');
    list.id='list'
    list.innerHTML=';'

    var text = ''
    var product
    var sum = 0

    for(var i=0; i<data.length;i++){
        product=data[i];
        text+='<div class = product><strong> [' +product.name +']</strong>: $' + product.price.toLocaleString()+ '<br/>' + product.description + '<hr/></div>';
        sum+=product.price;
    }
    text += '<div class = total><strong>Total: </strong>$' +sum.toLocaleString()+'</div>';
    list.innerHTML=text;
    document.body.appendChild(list)

}
ajax("https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
function(response){ render(response);


}); // you should get product information in JSON format and render data in the page