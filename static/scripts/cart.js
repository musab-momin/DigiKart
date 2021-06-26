let xyz = document.getElementById('cart_count')
//console.log(xyz)
window.onload = ()=>
{
  cartLogic()
  //alert('This is wokringk,,,')

}

const cartLogic = ()=>
{
  let cart = {}
  if(localStorage.getItem('cart') == null)
  {
    cart = {}
  }
  else
  {
    cart = JSON.parse(localStorage.getItem('cart'))
    xyz.innerHTML = '('+Object.keys(cart).length+')';
  }

  $('.cartbtn').click(function()
  {
    // alert('this is woking...')
    let idstr = this.id.toString();
    if(cart[idstr] != undefined)
    {
      let quantity = cart[idstr][0] + 1;
      let name = document.getElementById('name'+idstr).innerHTML;
      let price = document.getElementById('price'+idstr).innerHTML;
      cart[idstr] = [quantity, name, price]
    }
    else
    {
      let quantity =  1;
      let name = document.getElementById('name'+idstr).innerHTML;
      let price = document.getElementById('price'+idstr).innerHTML;
      cart[idstr] = [quantity, name, price];
    }
    console.log(cart)
    localStorage.setItem('cart', JSON.stringify(cart));
    xyz.innerHTML = '('+Object.keys(cart).length+')';
    //console.log(cart_counter++);
  });
}



//console.log(cart)

// for(let i in cart)
// {
//   console.log(i)
// }
//checkout work




