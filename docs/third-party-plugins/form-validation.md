---
title: "Form Validation"
components: 1
description: "Form validation ensures inputs meet criteria before submission, enhancing data accuracy by providing instant feedback and preventing invalid data processing."
bg_image: "svg/third-party-plugins/forms-validation.svg"
menu:
  main:
    parent: "third party plugins"

previous: Flatpickr
previousLink: third-party-plugins/flatpickr/

next: Full Calendar
nextLink: third-party-plugins/fullcalendar/

pageJS:
  - "/js/pages/form-validation.js"

vendorJS:
  - "vendor/flatpickr/flatpickr.js"

vendorCSS:
  - "vendor/flatpickr/flatpickr.css"
---

<!-- Class Table -->

{{< class-table >}}
success-message | component | Displays a valid message for JavaScript validation
error-message | component | Displays an invalid message for JavaScript validation
{{< /class-table >}}

<!-- Js validation -->

{{< headname level="3" >}} JS validation {{< /headname >}}

A fundamental form input with JavaScript validation.

To implement custom validation messages , add the `novalidate` boolean attribute to your `<form>` element. This will disable the browser's default validation feedback tooltips while still allowing access to the form validation APIs via JavaScript. Try submitting the form below; JavaScript will intercept the submit action and provide feedback. When you attempt to submit, you’ll see the `:invalid` and `:valid` styles.

{{< code jsCode="true" >}}

<div class="bg-base-100 w-full rounded-lg shadow-base-300/20 shadow-sm">
  <h5 class="bg-base-300/10 rounded-t-lg p-4 text-xl font-bold">JS Validation</h5>
  <div class="w-full p-4">
    <form class="needs-validation peer grid gap-y-4" novalidate>
      <!-- Account Details -->
      <div class="w-full">
        <h6 class="text-lg font-semibold">1. Account Details</h6>
        <hr class="mb-4 mt-2" />
      </div>
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <div>
          <label class="label-text" for="firstName">First Name </label>
          <input id="firstName" type="text" placeholder="John" class="input" required />
          <span class="error-message">Please enter your name.</span>
          <span class="success-message">Looks good!</span>
        </div>
        <div>
          <label class="label-text" for="lastName">Last Name</label>
          <input id="lastName" type="text" placeholder="Doe" class="input" required />
          <span class="error-message">Please enter your last name.</span>
          <span class="success-message">Looks good!</span>
        </div>
      </div>
      <!-- Email and password -->
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <div>
          <label class="label-text" for="userEmail">Email</label>
          <input id="userEmail" type="email" class="input" placeholder="john@gmail.com" aria-label="john@gmail.com" required="" />
          <span class="error-message">Please enter a valid email</span>
          <span class="success-message">Looks good!</span>
        </div>
        <div>
          <label class="label-text" for="userPassword">Password</label>
          <div class="input">
            <input id="userPassword" type="password" class="grow" placeholder="Enter password" required />
            <button type="button" data-toggle-password='{ "target": "#userPassword" }' class="my-auto ms-4 block cursor-pointer" >
              <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-4 shrink-0"></span>
              <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-4 shrink-0"></span>
            </button>
          </div>
          <span class="error-message">Please enter a valid password</span>
          <span class="success-message">Looks good!</span>
        </div>
      </div>
      <!-- Personal Info -->
      <div class="w-full">
        <h6 class="text-lg font-semibold">2. Personal Info</h6>
        <hr class="mb-4 mt-2" />
      </div>
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <div>
          <label class="label-text" for="userProfile">Profile Pic</label>
          <input id="userProfile" type="file" class="input" required />
          <span class="error-message">Please select the file</span>
          <span class="success-message">Looks good!</span>
        </div>
        <div>
          <label class="label-text" for="jsPickr">DOB</label>
          <input id="jsPickr" type="text" class="input" placeholder="YYYY-MM-DD" id="jsPickr" required />
          <span class="error-message">Please select your DOB</span>
          <span class="success-message">Looks good!</span>
        </div>
      </div>
      <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
        <div>
          <label class="label-text" for="userCountry">Pick your Country</label>
          <select class="select" id="userCountry" aria-label="Select Country" required>
            <option value="">Select Country</option>
            <option value="usa">USA</option>
            <option value="uk">UK</option>
            <option value="france">France</option>
            <option value="australia">Australia</option>
            <option value="spain">Spain</option>
          </select>
          <span class="error-message">Please select your country</span>
          <span class="success-message">Looks good!</span>
        </div>
        <div>
          <div class="label-text">Gender</div>
          <div class="flex items-center gap-2">
            <input type="radio" id="male" name="radio-0" class="radio radio-primary" required />
            <label class="label-text text-base" for="male">Male</label>
          </div>
          <div class="flex items-center gap-2">
            <input type="radio" id="female" name="radio-0" class="radio radio-primary" required />
            <label class="label-text text-base" for="female">Female</label>
          </div>
          <span class="error-message">Please select your Gender</span>
          <span class="success-message">Looks good!</span>
        </div>
      </div>
      <div class="w-full">
        <label class="label-text" for="userBio">Bio</label>
        <textarea class="textarea min-h-20 resize-none" id="userBio" placeholder="Hello!!!" required=""></textarea>
        <span class="error-message">Please write few words</span>
        <span class="success-message">Looks good!</span>
      </div>
      <div>
        <div class="flex items-center gap-3">
          <input type="checkbox" id="userSwitch" class="switch switch-primary" required />
          <label class="label-text text-base" for="userSwitch">Send me related emails</label>
        </div>
        <span class="error-message">Please select your preference</span>
        <span class="success-message">Looks good!</span>
      </div>
      <div>
        <div class="flex items-center gap-3">
          <input type="checkbox" class="checkbox checkbox-primary" id="userAgre" required />
          <label class="label-text text-base" for="userAgre">Agree to our terms and conditions</label>
        </div>
        <span class="error-message">Please confirm our T&C</span>
        <span class="success-message">Looks good!</span>
      </div>
      <!-- Submit button -->
     <div class="mt-4">
        <button type="submit" name="submitButton" class="btn btn-primary">Submit</button>
      </div>
    </form>
  </div>
</div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
   // Initialize flatpickr
  flatpickr('#jsPickr', {
    allowInput: true,
    monthSelectorType: 'static'
  })
     // Fetch all the forms we want to apply custom validation styles to
  const forms = document.querySelectorAll('.needs-validation')

// Loop over them and prevent submission if invalid

Array.from(forms).forEach(form => {

    form.addEventListener(
      'submit',
      event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
          // Find the first invalid input field and set focus to it
          const firstInvalidElement = form.querySelector(':invalid')
          if (firstInvalidElement) {
            firstInvalidElement.focus()
          }
        }form.classList.add('validate')
      },
      false
    )})
})
</script>

{{< /code >}}
