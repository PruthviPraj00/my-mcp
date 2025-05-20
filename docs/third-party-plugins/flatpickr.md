---
title: "Flatpickr (Datepicker)"
description: "Flatpickr is a lightweight JavaScript library for easy date and time picking, offering sleek design and extensive customization options for web applications."
bg_image: "svg/third-party-plugins/flatpickr.svg"
components: 5
menu:
  main:
    parent: "third party plugins"

previous: File upload
previousLink: third-party-plugins/file-upload/

next: Form Validation
nextLink: third-party-plugins/form-validation/

pageJS:
  - "/js/pages/flatpickr.js"

vendorJS:
  - "vendor/flatpickr/flatpickr.js"
  - "vendor/flatpickr/ru.js"

vendorCSS:
  - "vendor/flatpickr/flatpickr.css"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the steps to seamlessly integrate <a href="https://flatpickr.js.org/" target="_blank" class="link link-primary">Flatpickr</a> JS into your project.

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical mb-12 w-full ps-0">
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        1
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Installation</div>
      <p> Install <code>flatpickr</code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm i flatpickr{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>
  
  <!-- Include JS and CSS -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Include Flatpickr JavaScript and CSS</div>
      <p>Include the necessary CSS and JavaScript files in the following locations:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<head>
  <link rel="stylesheet" href="../path/to/flatpickr/dist/flatpickr.css" />
</head>
<body>
  <script src="../path/to/flatpickr/flatpickr.js"></script>
</body>
{{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong>  A CDN link won't work here because we need to modify the default Vendor CSS to fit FlyonUI's design.
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
      <p>Update your <code>tailwind.css</code> file to incorporate the path for the FlyonUI Flatpickr override CSS.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="css" >}}@import "flyonui/src/vendor/flatpickr.css";{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>
  
  <!-- Basic Usage -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        4
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Basic Usage</div>
      <p>The following are valid ways to create a Flatpickr instance:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="js" >}}// If using Flatpickr in a framework, it's recommended to pass the element directly
flatpickr(element, {});

// Alternatively, selectors are supported
flatpickr("#myID", {});

// Create multiple instances
flatpickr(".anotherSelector");
{{< /code-highlight >}}

</div>

  </li>
</ul>

<!-------------------- Basic examples -------------------->

{{< headname level="2" >}} Basic examples {{< /headname >}}

<!-- Date picker -->

{{< headname level="3" >}} Date picker {{< /headname >}}

Basic date picker example.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="YYYY-MM-DD" id="flatpickr-date" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Basic
    flatpickr('#flatpickr-date', {
      monthSelectorType: 'static'
    })
  })
</script>

{{< /code >}}

<!-- Time picker -->

{{< headname level="3" >}} Time picker {{< /headname >}}

Basic time picker example.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="HH:MM" id="flatpickr-time" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Time
    flatpickr('#flatpickr-time', {
      enableTime: true,
      noCalendar: true,
      dateFormat: 'H:i'
    })
  })
</script>

{{< /code >}}

<!-------------------- Types -------------------->

{{< headname level="2" >}} Types {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Default datepicker.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="YYYY-MM-DD" id="flatpickr-default" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Default Type
    flatpickr('#flatpickr-default', {
      monthSelectorType: 'static'
    })
  })
</script>

{{< /code >}}

<!-- Floating -->

{{< headname level="3" >}} Floating {{< /headname >}}

Floating label example.

{{< code addClass="!block" jsCode="true" >}}

<div class="input-floating max-w-sm">
  <input type="text" placeholder="YYYY-MM-DD" class="input" id="flatpickr-floating" />
  <label class="input-floating-label" for="flatpickr-floating">Date</label>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // floating Type
    flatpickr('#flatpickr-floating', {
      monthSelectorType: 'static'
    })
  })
</script>

{{< /code >}}

<!-------------------- Validation states -------------------->

{{< headname level="2" >}} Validation states {{< /headname >}}

<!-- Success state -->

{{< headname level="3" >}} Success state {{< /headname >}}

Success state can be show using `is-valid` class.

{{< code addClass="flex-col gap-6" jsCode="true" >}}
<div class="max-w-sm">
  <label class="label-text" for="flatpickrStateSuccess">Date</label>
  <input type="text" placeholder="YYYY-MM-DD" class="input is-valid flatpickr-success" id="flatpickrStateSuccess" />
  <span class="helper-text">Helper text</span>
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="YYYY-MM-DD" class="input is-valid flatpickr-success" id="flatpickrFloatingStateSuccess" />
  <label class="input-floating-label" for="flatpickrFloatingStateSuccess">Date</label>
  <span class="helper-text ps-3">Helper text</span>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Success Date Picker
    flatpickr('.flatpickr-success', {
      monthSelectorType: 'static'
    })
  })
</script>

{{< /code >}}

<!-- Error state -->

{{< headname level="3" >}} Error state {{< /headname >}}

Error state can be show using `is-invalid` class.

{{< code addClass="flex-col gap-6" jsCode="true" >}}

<div class="max-w-sm">
  <label class="label-text" for="flatpickrStateError">Date</label>
  <input type="text" placeholder="John Doe" class="input is-invalid flatpickr-error" id="flatpickrStateError" />
  <span class="helper-text">Helper text</span>
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input is-invalid flatpickr-error" id="flatpickrFloatingStateError" />
  <label class="input-floating-label" for="flatpickrFloatingStateError">Date</label>
  <span class="helper-text ps-3">Helper text</span>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Error  Date Picker
    flatpickr('.flatpickr-error', {
      monthSelectorType: 'static'
    })
  })
</script>

{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- DateTime picker -->

{{< headname level="3" >}} DateTime picker {{< /headname >}}

Example showcasing a picker with both date and time selection.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="YYYY-MM-DD HH:MM" id="flatpickr-date-time" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Date Time
    flatpickr('#flatpickr-date-time', {
      enableTime: true,
      dateFormat: 'Y-m-d H:i'
    })
  })
</script>

{{< /code >}}

<!-- Multiple dates picker -->

{{< headname level="3" >}} Multiple dates picker {{< /headname >}}

Example demonstrating how to select multiple dates.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="YYYY-MM-DD, YYYY-MM-DD" id="flatpickr-multiple-date" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Multiple Date
    flatpickr('#flatpickr-multiple-date', {
      mode: 'multiple',
      dateFormat: 'Y-m-d'
    })
  })
</script>

{{< /code >}}

<!-- Range picker -->

{{< headname level="3" >}} Range picker {{< /headname >}}

Select range of date.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="YYYY-MM-DD to YYYY-MM-DD" id="flatpickr-range" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Range Date Picker
    flatpickr('#flatpickr-range', {
      mode: 'range'
    })
  })
</script>

{{< /code >}}

<!-- Human friendly -->

{{< headname level="3" >}} Human friendly {{< /headname >}}

Human Friendly date picker example.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="Month DD, YYYY" id="flatpickr-human-friendly" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Human Friendly
    flatpickr('#flatpickr-human-friendly', {
      altInput: true,
      altFormat: 'F j, Y',
      dateFormat: 'Y-m-d'
    })
  })
</script>

{{< /code >}}

<!-- Inline picker -->

{{< headname level="3" >}} Inline picker {{< /headname >}}

Basic inline picker example.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="YYYY-MM-DD" id="flatpickr-inline" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Inline Date Picker
    flatpickr('#flatpickr-inline', {
      inline: true,
      allowInput: false,
      monthSelectorType: 'static'
    })
  })
</script>

{{< /code >}}

<!-- Disabled dates -->

{{< headname level="3" >}} Disabled dates {{< /headname >}}

The example below demonstrates how to disable a specific date range.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="YYYY-MM-DD" id="flatpickr-disabled-range" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Disable Date Picker
    const fromDate = new Date(Date.now() - 3600 * 1000 * 48)
    const toDate = new Date(Date.now() + 3600 * 1000 * 48)
    flatpickr('#flatpickr-disabled-range', {
      dateFormat: 'Y-m-d',
      disable: [
        {
          from: fromDate.toISOString().split('T')[0],
          to: toDate.toISOString().split('T')[0]
        }
      ]
    })
  })
</script>

{{< /code >}}

<!-- Localization -->

{{< headname level="3" >}} Localization {{< /headname >}}

The date picker below has been localized to display months and days in Russian. For more information, please refer to the official documentation on <a href="https://flatpickr.js.org/localization/" target="_blank" class="link link-primary">localization</a>.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="YYYY-MM-DD" id="flatpickr-localization" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Localization
    flatpickr('#flatpickr-localization', {
      locale: 'ru'
    })
  })
</script>

{{< /code >}}

<!-- Display week numbers -->

{{< headname level="3" >}} Display week numbers {{< /headname >}}
Example displaying week number.

{{< code addClass="!block" jsCode="true" >}}

<input type="text" class="input max-w-sm" placeholder="YYYY-MM-DD" id="flatpickr-week-number" />

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Week Numbers
    flatpickr('#flatpickr-week-number', {
      weekNumbers: true,
      monthSelectorType: 'static'
    })
  })
</script>

{{< /code >}}
