$(document).ready(function(){
    var submitButton = $(':submit');
    var textInput = $('input[type = "text"]');
    var textArea = $('textarea');
    $('input[type != "submit"]').addClass('form-control');
    submitButton.addClass('btn btn-primary');
    submitButton.attr('disabled',true)
    $('input[type = "file"]').change(function (){
        var file = $('input[type = "file"]');
        var numberOfFiles =  file[0].files.length;
        if(isAllowed(numberOfFiles)){
            if(!isEmpty() && !isTextAreaEmpty()){
                submitButton.attr('disabled',false);
            }
        }else{
            submitButton.attr('disabled', true);
            var errorText = "<p class='text-danger'>At maximum 3 images are allowed!!</p>"
            $(this).after(errorText);
        }
        
    });
    textInput.change(()=>{
        lastCall();
    });
    textArea.change(()=>{
        lastCall();
    })
    function lastCall(){
        var file = $('input[type = "file"]');
        var numberOfFiles =  file[0].files.length;
        if(!isEmpty() && isAllowed(numberOfFiles) && !isTextAreaEmpty()){
            submitButton.attr('disabled',false);
        }else{
            submitButton.attr('disabled',true);
        }
    }
    function isEmpty(){
        if(textInput[0].value === ''&& textInput[1].value === ''){
            return true;
        }else if(textInput[0].value === ''&& textInput[1].value !== ''){
            return true;
        }else if(textInput[0].value !== ''&& textInput[1].value === ''){
            return true;
        }else{
            return false;
        }
    }
    function isAllowed(numberOfFiles){
        if(numberOfFiles > 0 && numberOfFiles < 4){
            return true;
        }else{
            return false;
        }
    }
    function isTextAreaEmpty(){
        if(textArea.val() === ""){
            return true;
        }else{
            return false;
        }
    }

});