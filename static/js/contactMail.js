function sendMail(contactForm) {
    /* variables from EmailJS account */
    var service_id = "gmail";
    var template_id = "template_bos_up";

    /* Sending template from EmailJS */
    try {
        emailjs.send(service_id, template_id, {
            "from_name": contactForm.name.value,
            "from_email": contactForm.email.value,
            "message": contactForm.message.value,
            "subject": contactForm.subject.value
        });
        $("#name, #email, #message, #subject").val("");
            alert("Thank you for your message!");
        return true;
    
    /* Error catching */
    } catch (error) {
        $("#name, #email, #message, #subject").val("");
            alert(error);
        return false;
    }
}