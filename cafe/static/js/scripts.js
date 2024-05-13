




// Script for making the Quantity button and inputs work in the product details page
  const count_up_btn = document.getElementById("button-addon2"); // accessing the + button
  const count_dwn_btn = document.getElementById("button-addon1"); // accessing the - button
  let q_value = document.getElementById("q_value"); //  accessing the input box

//   The following line adds an event listener on the buttons to run an anonymous function which
// adds or subtracts from the quantity value of product when 
  count_up_btn.addEventListener('click', ()=>{ q_value.value = parseInt(q_value.value) + 1; });
  count_dwn_btn.addEventListener('click', counting_down);

  function counting_down(){
    if (parseInt(q_value.value) > 0) {
    q_value.value = parseInt(q_value.value) - 1;
    }
  }
