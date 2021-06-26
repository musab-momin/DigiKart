let cart_icon = document.getElementById('cart_count')
function add_to_cart(pid, pname, price)
{
    // toast message section
    // var x = document.getElementById("snackbar");
    // x.className = "show";
    // setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);



    let cart = localStorage.getItem('cart');
    if(cart==null)
    {
        let products = []
        let product = {productId: pid, productName: pname, productQuantity: 1, productPrice: price}
        products.push(product)
        localStorage.setItem("cart", JSON.stringify(products));
        cart_icon.innerHTML = '('+products.length+')';
        console.log('fist time product added....!')
    }
    else
    {
        let p_cart = JSON.parse(cart);
        let old_product = p_cart.find((item) => item.productId == pid)
        if(old_product)
        {
            //increasing only quantity
            old_product.productQuantity = old_product.productQuantity+1
            p_cart.map((item)=>{
                if(item.productId==old_product.productId)
                {
                    item.productQuantity = old_product.productQuantity
                }
            });
            localStorage.setItem('cart', JSON.stringify(p_cart));
            cart_icon.innerHTML = '('+p_cart.length+')';
            console.log('product quantity is increased !')
        }
        else
        {
            //create new product
            let product = {productId: pid, productName: pname, productQuantity: 1, productPrice: price}
            p_cart.push(product)
            localStorage.setItem('cart', JSON.stringify(p_cart));
            cart_icon.innerHTML = '('+p_cart.length+')';
            console.log('product is added...!')


        }
    }
}

// add_to_cart("redmi", 7999)