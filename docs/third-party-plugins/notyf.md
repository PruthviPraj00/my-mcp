---
title: "Notyf (Toasts)"
description: "Transform Your User Experience with Seamlessly Integrated and Customizable Toast Notifications, Tailored for Modern Web Applications."
bg_image: "svg/third-party-plugins/notyf.svg"
components: 5
menu:
  main:
    parent: "third party plugins"

previous: Full Calendar
previousLink: third-party-plugins/fullcalendar/

next: Rating
nextLink: third-party-plugins/rating/

pageJS:
  - "/js/pages/notyf.js"

vendorJS:
  - "/vendor/notyf/notyf.js"

vendorCSS:
  - "/vendor/notyf/notyf.css"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://carlosroso.com/notyf/" target="_blank" class="link link-primary font-semibold">Notyf JS</a> with FlyonUI.

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical w-full mb-12 ps-0">
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        1
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Installation</div>
      <p>Install <code>notyf</code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm install notyf{{< /code-highlight >}}
    </div>
    <hr class="rounded-none border-transparent !w-0.5" />
  </li>

  <!-- Include Third-Party JS and CSS -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Include Notyf JavaScript and CSS</div>
      <p>Add the following CSS and JavaScript to your page:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<head>
  <link rel="stylesheet" href="../path/to/notyf/notyf.css" />
</head>
<body>
  <script src="../path/to/notyf/notyf.js"></script>
</body>{{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> A CDN link will not work here because we need to customize the default Vendor CSS to align with FlyonUI's design.
      </p>
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Tailwind Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        3
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Update Tailwind Configuration</div>
      <p>Update your <code>tailwind.css</code> file to incorporate the path for the FlyonUI Notyf override CSS.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="css" >}}
@import "flyonui/src/vendor/notyf.css";
{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Notyf Initialization & Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        4
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Initialize Notyf</div>
      <p>Add the initialization JavaScript code for Notyf after including the Notyf JS library. Set up an event listener on any element to trigger the Notyf instance. Ensure this Notyf JS file is monitored by TailwindCSS, as described in step 3.</p>
      <p>For more options and detailed configurations, refer to the Notyf JS <a href="https://github.com/caroso1222/notyf?tab=readme-ov-file#notyf" class="link link-primary inline-flex items-center gap-1" target="_blank">documentation <span class="icon-[tabler--external-link]"></span></a>.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}// Notyf instance
const notyf = new Notyf();
// Trigger Notyf on button click
document.getElementById('trigger-btn').addEventListener('click', function () {
  notyf.success('This is a primary notification!');
});{{< /code-highlight >}}
    </div>
  </li>
</ul>

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default notyf -->

{{< headname level="3" >}} Default notyf {{< /headname >}}

Use the example below for default notification, initialized with the JS code provided below.

{{< code jsCode="true" >}}
<button class="btn btn-primary" id="notyf-default-example">Default notyf</button>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const notyfDefault = new Notyf()

    document.getElementById('notyf-default-example').addEventListener('click', function () {
     notyfDefault.success('This is primary notification!')
    })
  })
</script>

{{< /code >}}

<!-- Custom notyf -->

{{< headname level="3" >}} Custom notyf {{< /headname >}}

Use the example below for custom notification, initialized with the JS code provided below.

{{< code jsCode="true" >}}
<button class="btn btn-primary" id="notyf-custom-example">Custom notyf</button>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const notyfCustom = new Notyf({
      duration: 3000,
      position: {
        x: 'right',
        y: 'top'
      },
      types: [
        {
          type: 'primary',
          background: 'var(--color-primary)',
          icon: { className: 'icon-[tabler--circle-check] !text-primary', tagName: 'i' },
          text: '',
          color: 'white'
        }
      ]
    })

    document.getElementById('notyf-custom-example').addEventListener('click', function () {
      notyfCustom.open({
        type: 'primary',
        message: 'This is primary notification!',
        duration: 3000,
        ripple: true,
        dismissible: true
      })
    })
  })
</script>

{{< /code >}}

<!-------------------- Advance options -------------------->

{{< headname level="2" >}} Advance options {{< /headname >}}

<!-- Notyf generator -->

{{< headname level="3" >}} Notyf generator {{< /headname >}}

Use the `Notyf generator` below to create custom notifications according to your requirements for position, type, behavior, message, and duration.

{{< code jsCode="true" addClass="justify-center" >}}

<div class="card mt-6 max-w-lg max-sm:w-64">
  <form id="notificationForm">
    <div class="card-body">
      <!-- Message -->
      <div>
        <label class="label-text" for="notyf-value"> Message </label>
        <input id="notyf-value" type="text" placeholder="Notification message" class="input" autofocus />
      </div>
      <!-- Number -->
      <div>
        <label class="label-text" for="notyf-number"> Duration </label>
        <input id="notyf-number" type="number" placeholder="1000 (Milliseconds)" class="input" min="1000" />
      </div>
      <!-- position - X -->
      <div class="flex flex-col">
        <h6 class="text-sm text-base-content mb-1">Position - X</h6>
        <div class="flex flex-wrap gap-3">
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-x" class="radio radio-primary" id="positionXLeft" value="left" checked />
            <label class="label-text text-base" for="positionXLeft"> Left </label>
          </div>
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-x" class="radio radio-primary" id="positionXcenter" value="center" />
            <label class="label-text text-base" for="positionXcenter"> Center </label>
          </div>
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-x" class="radio radio-primary" id="positionXright" value="right" />
            <label class="label-text text-base" for="positionXright"> Right </label>
          </div>
        </div>
      </div>
      <!-- position - Y -->
      <div class="flex flex-col">
        <h6 class="text-sm text-base-content mb-1">Position - Y</h6>
        <div class="flex flex-wrap gap-3">
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-y" class="radio radio-primary" id="positionYtop" value="top" checked />
            <label class="label-text text-base" for="positionYtop"> Top </label>
          </div>
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-y" class="radio radio-primary" id="positionYcenter" value="center" />
            <label class="label-text text-base" for="positionYcenter"> Center </label>
          </div>
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-y" class="radio radio-primary" id="positionYbottom" value="bottom" />
            <label class="label-text text-base" for="positionYbottom"> Bottom </label>
          </div>
        </div>
      </div>
      <!-- Behavior -->
      <div class="flex flex-col">
        <h6 class="text-sm text-base-content mb-1">Behavior</h6>
        <div class="flex flex-col gap-2 sm:flex-row sm:gap-4">
          <div class="flex items-center gap-1">
            <input id="notyf-ripple" type="checkbox" class="checkbox checkbox-primary" checked />
            <label class="label-text text-base" for="notyf-ripple"> With Ripple effect </label>
          </div>
          <div class="flex items-center gap-1">
            <input id="notyf-dismiss" type="checkbox" class="checkbox checkbox-primary"/>
            <label class="label-text text-base" for="notyf-dismiss"> Dismissible </label>
          </div>
        </div>
      </div>
      <!-- Type -->
      <div class="flex flex-col">
        <h6 class="text-sm text-base-content mb-1">Type</h6>
        <div class="flex flex-col gap-2 sm:flex-row sm:gap-4">
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-type" class="radio radio-primary" id="typeSuccess" value="success" checked />
            <label class="label-text text-base" for="typeSuccess"> Success </label>
          </div>
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-type" class="radio radio-primary" id="typeInfo" value="info" />
            <label class="label-text text-base" for="typeInfo"> Info </label>
          </div>
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-type" class="radio radio-primary" id="typeWarning" value="warning" />
            <label class="label-text text-base" for="typeWarning"> Warning </label>
          </div>
          <div class="flex items-center gap-1">
            <input type="radio" name="radio-type" class="radio radio-primary" id="typeError" value="error" />
            <label class="label-text text-base" for="typeError"> Error </label>
          </div>
        </div>
      </div>
      <button id="notyf-submit" type="submit" class="btn btn-primary">Show Notification</button>
    </div>
  </form>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const notyf = new Notyf({
      duration: 3000,
      position: {
        x: 'right',
        y: 'top'
      },
      types: [
        {
          // Added Info and Warning type 
          type: 'info',
          background: 'var(--color-info)',
          icon: { className: 'icon-[tabler--info-circle] !text-info', tagName: 'i' },
          text: '',
          color: 'white'
        },
        {
          type: 'warning',
          background: 'var(--color-warning)',
          icon: { className: 'icon-[tabler--alert-triangle] !text-warning', tagName: 'i' },
          text: '',
          color: 'white'
        }
      ]
    })

    document.getElementById('notificationForm').addEventListener('submit', function (event) {
      event.preventDefault()

      // Get values from the form
      let message = document.getElementById('notyf-value').value || 'This is a notification!'
      let duration = parseInt(document.getElementById('notyf-number').value) || 3000 // Default duration to 3000 if not specified
      let positionX = document.querySelector('input[name="radio-x"]:checked').value
      let positionY = document.querySelector('input[name="radio-y"]:checked').value
      let ripple = document.getElementById('notyf-ripple').checked
      let dismissible = document.getElementById('notyf-dismiss').checked
      let type = document.querySelector('input[name="radio-type"]:checked').value

      // Update Notyf instance with dynamic position
      notyf.options.duration = duration
      notyf.options.position = {
        x: positionX,
        y: positionY
      }

      // Show the toast notification
      notyf.open({
        type: type,
        message: message,
        duration: duration,
        ripple: ripple,
        dismissible: dismissible
      })
    })
  })
</script>

{{< /code >}}
