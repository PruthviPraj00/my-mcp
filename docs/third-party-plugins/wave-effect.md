---
title: "Wave Effect"
description: "Add smooth wave effects to your components with Nodewave for better interaction."
bg_image: "svg/third-party-plugins/wave-effect.svg"
components: 5
menu:
  main:
    parent: "third party plugins"

previous: Rating
previousLink: third-party-plugins/rating/

next: WYSIWYG Editor
nextLink: third-party-plugins/editor/

pageJS:
  - "/js/helper/wave-helper.js"

vendorJS:
  - "vendor/node-waves/waves.js"

vendorCSS:
  - "vendor/node-waves/waves.css"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://fians.github.io/Waves/" target="_blank" class="link link-primary font-semibold">Waves</a> with FlyonUI.

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
      <p>Install <code>waves</code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm install node-waves{{< /code-highlight >}}
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
      <div class="text-base-content mb-3 font-semibold">Include Waves JavaScript and CSS</div>
      <p>Add the following CSS and JavaScript to your page:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<head>
  <link rel="stylesheet" type="text/css" href="/path/to/waves.min.css" />
</head>
<body>
  <script type="text/javascript" src="../path/to/waves.min.js"></script>
</body>{{< /code-highlight >}}
<p class="!mt-4">
        <strong>Note:</strong> A CDN link won't work here because we need to modify the default Vendor CSS to fit FlyonUI's design.
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
     <p>Update your <code>tailwind.css</code> file to incorporate the path for the FlyonUI Waves override CSS.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="css" >}}@import "flyonui/src/vendor/waves.css";{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Waves Initialization & Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        4
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Initialize Waves</div>
      <p>Add the initialization JavaScript code for Waves after including the Waves JS library. Set up an event listener on any element to trigger the Waves instance. Ensure this Waves JS file is monitored by TailwindCSS, as described in step 3.</p>
      <p>For more options and detailed configurations, refer to the Waves <a href="https://github.com/fians/Waves?tab=readme-ov-file#waves" class="link link-primary inline-flex items-center gap-1" target="_blank">documentation <span class="icon-[tabler--external-link]"></span></a>.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}// Waves Initialization
Waves.init()
Waves.attach('.waves'){{< /code-highlight >}}
    </div>
  </li>
</ul>

<!-- Class table -->

{{< class-table >}}
waves| component | Base class for the waves.
waves-light | color | Waves with `white' color.
waves-primary | color | Waves with 'primary' color.
waves-secondary | color | Waves with 'secondary' color.
waves-accent | color | Waves with 'accent' color.
waves-info | color | Waves with 'info' color.
waves-success | color | Waves with 'success' color.
waves-warning | color | Waves with 'warning' color.
waves-error | color | Waves with 'error' color.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Use the `waves` class to implement the default ripple effect.

{{< code >}}

<button class="btn btn-outline waves">Default</button>
{{< /code >}}

<!-------------------- Color -------------------->

{{< headname level="2" >}} Color {{< /headname >}}

<!-- Semantic colors -->

{{< headname level="3" >}} Semantic colors {{< /headname >}}

Combine the `waves` class with `waves-{semantic color}` to implement colored wave effects.

{{< code >}}
<button class="btn btn-soft waves">Default</button>
<button class="btn btn-soft btn-primary waves waves-primary"><span class="waves-ripple"></span>Primary</button>
<button class="btn btn-soft btn-secondary waves waves-secondary">Secondary</button>
<button class="btn btn-soft btn-accent waves waves-accent">Accent</button>
<button class="btn btn-soft btn-info waves waves-info">Info</button>
<button class="btn btn-soft btn-success waves waves-success">Success </button>
<button class="btn btn-soft btn-warning waves waves-warning">Warning</button>
<button class="btn btn-soft btn-error waves waves-error">Error</button>
{{< /code >}}

<!-- Custom colors -->

{{< headname level="3" >}} Custom colors {{< /headname >}}

To customize the ripple color, apply the `waves` class alongside the `--wave-color` CSS variable.

{{< code >}}

<!-- Solid -->
<button class="btn waves [--btn-color:#1877F2] text-white [--wave-color:#ffffff5e]">
  <span class="icon-[tabler--brand-facebook] size-4.5 shrink-0"></span> Facebook <span class="waves-ripple"></span>
</button>

<button class="btn waves btn-soft [--btn-color:#1da1f2] [--btn-fg:#1da1f2] [--wave-color:#4a87d766]">
  <span class="icon-[tabler--brand-x] size-4.5 shrink-0"></span> Twitter
</button>

<button class="btn waves btn-outline [--btn-color:#0a66c2] [--btn-fg:#0a66c2] [--wave-color:#0a66c250]">
  <span class="icon-[tabler--brand-linkedin] size-4.5 shrink-0"></span> LinkedIn
</button>

{{< /code >}}

<!-------------------- Illustration -------------------->

{{< headname level="2" >}} Illustration {{< /headname >}}

<!-- Buttons -->

{{< headname level="3" >}} Buttons {{< /headname >}}

Example of wave effect applied to buttons.

{{< code >}}

<button class="btn btn-primary waves waves-light">Default</button>
<button class="btn btn-primary btn-soft waves waves-primary">Default</button>
<button class="btn btn-primary btn-outline waves waves-primary">Default</button>
<button class="btn btn-primary btn-text waves waves-primary">Default</button>
<button class="btn btn-primary btn-gradient waves waves-light">Default</button>
{{< /code >}}

<!-- Icons -->

{{< headname level="3" >}} Icons {{< /headname >}}

Example of wave effect applied to icon buttons.

{{< code >}}

<button class="btn btn-square waves waves-light btn-primary" aria-label="Icon Button">
  <span class="icon-[tabler--star] size-4.5"></span>
</button>
<button class="btn btn-square waves waves-primary btn-soft btn-primary" aria-label="Soft Icon Button">
  <span class="icon-[tabler--star] size-4.5"></span>
</button>
<button class="btn btn-square waves waves-primary btn-outline btn-primary" aria-label="Outline Icon Button">
  <span class="icon-[tabler--star] size-4.5"></span>
</button>
<button class="btn btn-square waves waves-primary btn-text btn-primary" aria-label="Outline Icon Button">
  <span class="icon-[tabler--star] size-4.5"></span>
</button>
<button class="btn btn-square waves waves-light btn-gradient btn-primary" aria-label="Gradient Icon Button">
  <span class="icon-[tabler--star] size-4.5"></span>
</button>

{{< /code >}}

<!-- Card -->

{{< headname level="3" >}} Card {{< /headname >}}

Example of wave effect applied to card.

{{< code >}}

<div class="card waves waves-primary sm:max-w-sm">
  <div class="card-body">
    <h5 class="card-title mb-2.5">Welcome to Our Service</h5>
    <p>
      Discover the features and benefits that our service offers. Enhance your experience with our user-friendly
      platform designed to meet all your needs.
    </p>
  </div>
</div>
{{< /code >}}

<!-- Image -->

{{< headname level="3" >}} Image {{< /headname >}}

Example of wave effect applied to images.

{{< code >}}

<div class="waves waves-info">
  <img src="https://cdn.flyonui.com/fy-assets/components/card/image-5.png" alt="flower image" />
</div>
{{< /code >}}
