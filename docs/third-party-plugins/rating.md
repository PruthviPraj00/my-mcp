---
title: "Rating"
description: "The Ratings Component uses stars or symbols to visually represent user evaluations, providing a quick and intuitive way to display feedback and quality."
bg_image: "svg/third-party-plugins/rating.svg"
components: 5
menu:
  main:
    parent: "third party plugins"

previous: Notyf (Toasts)
previousLink: third-party-plugins/notyf/

next: Wave Effect
nextLink: third-party-plugins/wave-effect/

pageJS:
  - "/js/pages/rating.js"

vendorJS:
  - "/vendor/raty/raty.js"

vendorCSS:
  - "/vendor/raty/raty.css"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://github.com/wbotelhos/raty" target="_blank" class="link link-primary font-semibold">Raty JS</a> with FlyonUI.

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
      <p>Install <code>raty-js</code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm install raty-js{{< /code-highlight >}}
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
      <div class="text-base-content mb-3 font-semibold">Include Raty JavaScript and CSS</div>
      <p>Include the following CSS and JS files in your page:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<head>
  <link rel="stylesheet" href="../path/to/raty-js/src/raty.css" />
</head>
<body>
  <script src="../path/to/raty-js/build/raty.js"></script>
</body>{{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> A CDN link will not work here as customization of the default Vendor CSS is required to align with FlyonUI's design.
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
      <p>Update your <code>tailwind.css</code> file to incorporate the path for the FlyonUI RatyJS override CSS.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="css" >}}@import "flyonui/src/vendor/raty.css";{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Raty Initialization & Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        4
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Initialize Raty</div>
      <p>Add the Raty initialization JavaScript code below the Raty JS library inclusion. Set up the Raty instance to target elements using its <code>id</code> or <code>data-raty</code> attribute. Ensure this Raty JS file is in a location where TailwindCSS can monitor it, as specified in step 3.</p>
      <p>For more options and detailed configurations, refer to the Raty JS <a href="https://github.com/wbotelhos/raty/blob/main/README.md" class="link link-primary inline-flex items-center gap-1" target="_blank">documentation <span class="icon-[tabler--external-link]"></span></a>.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}const target = new Raty(document.querySelector('[data-raty]'), // or #Id
  {
    path: 'path/to/star-images/',
  });
target.init();{{< /code-highlight >}}
    </div>
  </li>
</ul>

<!-- Class Table -->

{{< class-table >}}
raty-jump | modifier | Applies a jump animation to the clicked star.
{{< /class-table >}}

<!-------------------- Basic usage -------------------->

{{< headname level="2" >}} Basic usage {{< /headname >}}

<!-- With images -->

{{< headname level="3" >}} With images {{< /headname >}}

The following example demonstrates the usage of a star-based rating system with the raty-js library using images, initialized with the below provided JavaScript code. Set the `path` to the location where the images are stored in your project, or to the node modules if they are stored there.

{{< code jsCode="true" >}}

<div class="flex" id="raty-with-image"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingImage = new Raty(document.querySelector('#raty-with-image'), {
    path: '/images/' // path/to/images(directory)
  })

  ratingImage.init()
})
</script>

{{< /code >}}

<!-- With fonts -->

{{< headname level="3" >}} With fonts {{< /headname >}}

The following example demonstrates the usage of a star-based rating system with the raty-js library using fonts, initialized with the below provided JavaScript code. Set the `path` to the location where the fonts are stored in your project, or to the node modules if they are stored there.

{{< code jsCode="true" >}}

<div class="flex" id="raty-with-font"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingFont = new Raty(document.querySelector('#raty-with-font'), {
    path: '/fonts/', // path/to/fonts(directory)
    starType: 'i'
  })
  ratingFont.init()
})
</script>

{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Read only (static) -->

{{< headname level="3" >}} Read only (static) {{< /headname >}}

The following example demonstrates the usage of a star-based read only (static) rating system, initialized with the below provided JavaScript code.

{{< code jsCode="true" >}}

<div class="flex" id="raty-read-only"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingReadOnly = new Raty(document.querySelector('#raty-read-only'), {
    path: '/images/',
    score: 3,
    readOnly: true
  })
  ratingReadOnly.init()
})
</script>

{{< /code >}}

<!-- Custom icons -->

{{< headname level="3" >}} Custom icons {{< /headname >}}

The following example demonstrates the usage of a rating with the custom heart icons, initialized with the below provided JavaScript code.

{{< code jsCode="true" >}}

<div class="flex" id="raty-custom-icons"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingCustomIcons = new Raty(document.querySelector('#raty-custom-icons'), {
    starType: 'i',
    starOff: 'icon-[tabler--heart-filled] opacity-20 size-7 text-error',
    starOn: 'icon-[tabler--heart-filled] size-7 text-error'
  })
  ratingCustomIcons.init()
})
</script>

{{< /code >}}

<!-- With half stars -->

{{< headname level="3" >}} With half stars {{< /headname >}}

The following example demonstrates the usage of a rating with half stars, initialized with the below provided JavaScript code.

{{< code jsCode="true" >}}

<div class="flex" id="raty-with-half-stars"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingHalfStars = new Raty(document.querySelector('#raty-with-half-stars'), {
    path: '/images/',
    score: 2.5,
    half: true
  })
  ratingHalfStars.init()
})
</script>

{{< /code >}}

<!-- Custom sizes -->

{{< headname level="3" >}} Custom sizes {{< /headname >}}

Utilize `size-{number}` with `starOff` & `starOn` options for rating with custom sizes.

{{< code addClass="flex-col" jsCode="true" >}}

<div class="flex" id="raty-xs"></div>
<div class="flex" id="raty-sm"></div>
<div class="flex" id="raty-default"></div>
<div class="flex" id="raty-lg"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  // Small
  const ratingSmall = new Raty(document.querySelector('#raty-sm'), {
    starType: 'i',
    score: 1,
    starOff: 'icon-[tabler--star-filled] opacity-20 size-4',
    starOn: 'icon-[tabler--star-filled] size-4'
  })
  ratingSmall.init()

  // Default
  const ratingDefault = new Raty(document.querySelector('#raty-default'), {
    starType: 'i',
    score: 2,
    starOff: 'icon-[tabler--star-filled] opacity-20 size-7',
    starOn: 'icon-[tabler--star-filled] size-7'
  })
  ratingDefault.init()

  // Large
  const ratingLarge = new Raty(document.querySelector('#raty-lg'), {
    starType: 'i',
    score: 3,
    starOff: 'icon-[tabler--star-filled] opacity-20 size-10',
    starOn: 'icon-[tabler--star-filled] size-10'
  })
  ratingLarge.init()
})
</script>

{{< /code >}}

<!-- Custom colors -->

{{< headname level="3" >}} Custom colors {{< /headname >}}

Utilize `text-{color}` with `starOff` & `starOn` options for rating with custom colors.

{{< code addClass="flex-col" jsCode="true" >}}

<div class="flex" id="raty-primary"></div>
<div class="flex" id="raty-warning"></div>
<div class="flex" id="raty-error"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  // Primary
  const ratingPrimary = new Raty(document.querySelector('#raty-primary'), {
    starType: 'i',
    score: 1,
    starOff: 'icon-[tabler--star-filled] opacity-20 size-7 text-primary',
    starOn: 'icon-[tabler--star-filled] size-7 text-primary'
  })
  ratingPrimary.init()
  
  // Warning
  const ratingWarning = new Raty(document.querySelector('#raty-warning'), {
    starType: 'i',
    score: 2,
    starOff: 'icon-[tabler--star-filled] opacity-20 size-7 text-warning',
    starOn: 'icon-[tabler--star-filled] size-7 text-warning'
  })
  ratingWarning.init()

  // Error
  const ratingError = new Raty(document.querySelector('#raty-error'), {
    starType: 'i',
    score: 3,
    starOff: 'icon-[tabler--star-filled] opacity-20 size-7 text-error',
    starOn: 'icon-[tabler--star-filled] size-7 text-error'
  })
  ratingError.init()
})
</script>

{{< /code >}}

<!-- With hints -->

{{< headname level="3" >}} With hints {{< /headname >}}

The following example demonstrates the usage of a rating with hints, initialized with the below provided JavaScript code.

{{< code addClass="flex-col" jsCode="true" >}}

<div class="flex" id="raty-with-hints"></div>
<div class="h-6" data-hint></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingHints = new Raty(document.querySelector('#raty-with-hints'), {
    path: '/images/',
    hints: ['Terrible 😔', 'Unsatisfactory 😑', 'Average 😊', 'Nice 😁', 'Splendid 😍'],
    target: '[data-hint]',
    targetFormat: 'Your experience was: {score}'
  })
  ratingHints.init()
})
</script>

{{< /code >}}

<!-- Custom number of stars -->

{{< headname level="3" >}} Custom number of stars {{< /headname >}}

The following example demonstrates the usage of a rating with custom number of stars , initialized with the below provided JavaScript code.

{{< code jsCode="true" >}}

<div class="flex" id="raty-with-custom-number-of-stars"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingCustomStars = new Raty(document.querySelector('#raty-with-custom-number-of-stars'), {
    path: '/images/',
    number: 8
  })
  ratingCustomStars.init()
})
</script>

{{< /code >}}

<!-- With score -->

{{< headname level="3" >}} With score {{< /headname >}}

The following example demonstrates the usage of a rating with score(value) , initialized with the below provided JavaScript code.

{{< code jsCode="true" >}}

<div class="flex items-center justify-between gap-4">
  <div class="flex" id="raty-with-score"></div>
  <div class="border-base-content/25 rounded-field text-base-content flex size-8 items-center justify-center border border-2 font-semibold" id="raty-score" ></div>
</div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingWithScore = new Raty(document.querySelector('#raty-with-score'), {
    starType: 'i',
    score: 2,
    starOff: 'icon-[tabler--star-filled] opacity-20 size-7',
    starOn: 'icon-[tabler--star-filled] size-7 text-warning',
    starHalf: 'icon-[tabler--star-half-filled] size-7 text-warning',
    targetScore: '#raty-score',
    half: true,
    click: function (score, event) {
      document.querySelector('#raty-score').textContent = score
    }
  })
  ratingWithScore.init()

  // Initial score
  document.querySelector('#raty-score').textContent = ratingWithScore.score()
})
</script>

{{< /code >}}

<!-- With reset option -->

{{< headname level="3" >}} With reset option {{< /headname >}}

The following example demonstrates the usage of a rating with reset option, initialized with the below provided JavaScript code.

{{< code jsCode="true" >}}

<div class="flex" id="raty-with-reset"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingWithReset = new Raty(document.querySelector('#raty-with-reset'), {
    starType: 'i',
    score: 2,
    starOff: 'icon-[tabler--star-filled] opacity-20 size-7',
    starOn: 'icon-[tabler--star-filled] size-7 text-warning',
    cancelOff: 'cancel-off-png',
    cancelOn: 'cancel-on-png text-error',
    cancelButton: true,
    cancelHint: 'Reset rating!',
    cancelPlace: 'right'
  })
  ratingWithReset.init()
})
</script>

{{< /code >}}

<!-- With animation -->

{{< headname level="3" >}} With animation {{< /headname >}}

The following example demonstrates the usage of a rating with animation, initialized with the below provided JavaScript code.

{{< code jsCode="true" >}}

<div class="flex" id="raty-with-animation"></div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const ratingWithAnimation = new Raty(document.querySelector('#raty-with-animation'), {
    starType: 'i',
    starOff: 'icon-[tabler--star-filled] opacity-20 size-7',
    starOn: 'icon-[tabler--star-filled] size-7 text-warning',
    click: function (score, event, target) {
      // Add the animation class to the clicked star using requestAnimationFrame
      requestAnimationFrame(() => {
        target.target.classList.add('raty-jump')
      })
    }
  })
  ratingWithAnimation.init()
  
  // Add hover effect immediately after initialization
  const stars = document.querySelectorAll('#raty-with-animation i') // Adjust the selector if needed
  stars.forEach(star => {
    star.addEventListener('mouseover', () => {
      star.classList.add('raty-jump')
    })
    star.addEventListener('mouseout', () => {
      star.classList.remove('raty-jump')
    })
  })
})
</script>

{{< /code >}}
