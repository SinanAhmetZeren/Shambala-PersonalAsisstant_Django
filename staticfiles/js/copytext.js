function myFunction() {
    /* Get the text field */
    var copyText = document.getElementById("myInput");
  
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
    /* Copy the text inside the text field */
    document.execCommand("copy");
  
    /* Alert the copied text */
    alert("Copied the text: " + copyText.value);
  }


/*function copyToClipboard(element) {
    var $temp = $("<input>");
    alert("Copied to clipboard: " + $(element).text());

    $("body").append($temp);
    $temp.val($(element).text()).select();

    document.execCommand("copy");
    $temp.remove();

}*/

function copyToClipboard(element) {
    var $temp = $("<input>");
    alert("Copied to clipboard: " + $(element).text());

    $("body").append($temp);
    $temp.val($(element).text()).select();

    document.execCommand("copy");
    $temp.remove();

}


