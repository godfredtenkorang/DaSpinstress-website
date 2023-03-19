const form = document.getElementById('form');
const fullname = document.getElementById('fullname');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
const position = document.getElementById('position');
const location = document.getElementById('location');
const linkedin = document.getElementById('linkedin');
const choice1 = document.getElementById('choice1');
const resume = document.getElementById('resume');

form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});

const setError = (element, message) => {
    const inputControl = element.preventElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');
}

const setSuccess = element => {
    const inputControl = element.preventElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
}

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
    const fullnameValue = fullname.value.trim();
    const emailValue = email.value.trim();
    const phoneValue = phone.value.trim();
    const positionValue = position.value.trim();
    const locationValue = location.value.trim();
    const linkedinValue = linkedin.value.trim();
    const choice1Value = choice1.value.trim();
    const resumeValue = resume.value.trim();

    if(fullnameValue === '') {
        setError(fullname, 'Username is required');
    } else {
        setSuccess(fullname);
    }

    if(emailValue === '') {
        setError(email, 'Email is required');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Provide a valid email address');
    } else {
        setSuccess(email);
    }

    if(phoneValue === '') {
        setError(phone, 'Phone Number is required');
    } else {
        setSuccess(phone);
    }

    if(positionValue === '') {
        setError(position, 'Position applying for is required')
    } else {
        setSuccess(position);
    }

    if(locationValue === '') {
        setError(location, 'Location is required');
    } else {
        setSuccess(location);
    }

    if(linkedinValue === '') {
        setError(linkedin, 'Linkedin link is required')
    } else {
        setSuccess(linkedin);
    }

    if(choice1Value === '') {
        setError(choice1, 'Authorization is required')
    } else {
        setSuccess(choice1);
    }

    if(resumeValue === '') {
        setError(resume, 'Resume file is required')
    } else {
        setSuccess(resume);
    }
};