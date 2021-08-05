/*

Script  : Subscribe Form
Version : 1.0
Author  : Surjith S M
URI     : http://themeforest.net/user/surjithctly

Copyright © All rights Reserved
Surjith S M / @surjithctly

*/

$(function() {

    "use strict";


    /* ================================================
   jQuery Validate - Reset Defaults
   ================================================ */

    $.validator.setDefaults({
        ignore: [],
        highlight: function(element) {
            $(element).closest('.form-group').addClass('has-error');
            $(element).addClass('form-control-danger');
            $(element).closest('form').addClass('form_error');
        },
        unhighlight: function(element) {
            $(element).closest('.form-group').removeClass('has-error');
            $(element).removeClass('form-control-danger');
            $(element).closest('form').removeClass('form_error');
        },
        errorElement: 'div',
        errorClass: 'help-block',
        errorPlacement: function(error, element) {
            if (element.parent('.input-group').length || element.parent('label').length) {
                // error.insertAfter(element.parent());
            } else {
                //  error.insertAfter(element);
            }
        }
    });

    /* 
    VALIDATE
    -------- */

    $("#subscribeform").submit(function(e) {
        e.preventDefault();
    }).validate({
        rules: {
            /* uncomment if Name is needed */
            /* 
            fname: "required",
            lname: "required", 
            */
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            /*
            fname: "Your first name please",
            lname: "Your last name please", 
            */
            email: "Please enter your email address"
        },
        submitHandler: function(form) {
            var $jssubscribebtn = $("#js-subscribe-btn");
            var $jssubscriberesult = $("#js-subscribe-result");
            var jssubscribebtnData = $jssubscribebtn.html();

            $jssubscribebtn.attr("disabled", true);

            /* 
             CHECK PAGE FOR REDIRECT (Thank you page)
             ---------------------------------------- */

            var redirect = $('#subscribeform').data('redirect');
            var noredirect = false;
            if (redirect == 'none' || redirect == "" || redirect == null) {
                noredirect = true;
            }
            $jssubscribebtn.html(jssubscribebtnData + ' <i class="fa fa-spinner fa-spin"></i>');

            /* 
             FETCH SUCCESS / ERROR MSG FROM HTML DATA-ATTR
             --------------------------------------------- */

            var success_msg = $jssubscriberesult.data('success-msg');
            var error_msg = $jssubscriberesult.data('error-msg');

            var dataString = $(form).serialize();

            /* 
             AJAX POST
             --------- */

            $.ajax({
                type: "POST",
                data: dataString,
                url: "php/subscribe.php",
                cache: false,
                success: function(d) {
                    $(".form-group").removeClass("has-success");
                    if (d == 'success') {
                        if (noredirect) {
                            $jssubscribebtn.html('Done <i class="fa fa-check"></i>');
                            setTimeout(function() {
                                $jssubscribebtn.html(jssubscribebtnData);
                            }, 3000);
                        } else {
                            window.location.href = redirect;
                        }
                    } else {
                        $jssubscribebtn.html('Error <i class="fa fa-times"></i>');
                        $(form).addClass('form_error');
                        setTimeout(function() {
                            $jssubscribebtn.html(jssubscribebtnData);
                        }, 3000);
                        if (window.console) {
                            console.log('PHP Error: ' + d);
                        }
                    }
                    $jssubscribebtn.attr("disabled", false);
                },
                error: function(d) {
                    $jssubscribebtn.html('Error <i class="fa fa-exclamation-triangle"></i>');
                    $(form).addClass('form_error');
                    setTimeout(function() {
                        $jssubscribebtn.html(jssubscribebtnData);
                    }, 3000);
                    $jssubscribebtn.attr("disabled", false);
                }
            });
            return false;

        }
    });

});