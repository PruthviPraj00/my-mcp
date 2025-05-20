---
title: "Set up FlyonUI with 11ty using Tailwind CSS"
description: "Integrate FlyonUI with 11ty and Tailwind CSS to build a modern, responsive UI, streamlining your development process with ease."
bg_image: "https://cdn.flyonui.com/fy-assets/icons/11ty-icon.png"

previous: Framework guides
previousLink: getting-started/framework-guides/
---

{{< callout "info" >}}

<h2 class="text-lg font-medium mb-1">Installation</h2>
Please note that the plugin has been tested with the latest version of the framework (v3.0.0).
{{< /callout >}}

<div>
  <div class="flex gap-2">
    <div><img src="https://cdn.flyonui.com/fy-assets/icons/11ty-icon.png" alt="11ty logo" class="h-auto w-14 mt-2" /></div>
    <div>
      <h2 class="text-base-content mb-3 text-lg font-semibold mt-2">
        Quick 11ty setup
      </h2>
      <p class="text-base-conte/80 text-base">
        <a href="https://www.11ty.dev/" class="link link-animated link-primary" target="_blank">11ty</a> is a simple and versatile static site generator written in JavaScript that transforms templates and data into HTML pages. If you haven't set up Tailwind CSS yet, check out
        <a class="link link-animated" target="_blank" href="https://themeselection.com/how-to-integrate-tailwind-with-11ty/">
          11ty Tailwind CSS
        </a>
        installation guides.
      </p>
      <div class="tooltip">
        <a href="https://github.com/themeselection/flyonui-11ty-integration" target="_blank" type="button" class="tooltip-toggle btn-sm btn btn-outline" aria-label="Tooltip">
          <span class="icon-[tabler--bolt-filled]"></span>
          FlyonUI + 11ty
        </a>
        <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
          <span class="tooltip-body">Checkout the Starter Kit</span>
        </span>
      </div>
    </div>
  </div>

  <ul class="timeline timeline-snap-icon timeline-compact timeline-vertical mb-12 w-full ps-0">
    <!-- Installation -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          1
        </span>
      </div>
      <div class="timeline-end m-0 mb-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Install FlyonUI</div>
        <p>
          Install
          <code>flyonui</code>
          via npm.
        </p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm i flyonui{{< /code-highlight >}}
      </div>
      <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Configure FlyonUI JavaScript paths -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          2
        </span>
      </div>
      <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
        <div class="text-base-content mb-3 font-semibold">Add FlyonUI plugin</div>
        <p>
          Include FlyonUI plugin in your <code>main.css</code> file.
        </p>
        {{< code-highlight addClass="mt-2" lang="css" >}}
@import "tailwindcss";
@plugin "flyonui";
@import "flyonui/variants.css";
@source "../node_modules/flyonui/flyonui.js"; // Add only if node_modules is gitignored

/* Import Third-party override css */
/* @import "flyonui/src/vendor/flatpickr.css"; */
/* @import "flyonui/src/vendor/notyf.css"; */
/* @import "flyonui/src/vendor/datatables.css"; */
/* @import "flyonui/src/vendor/editor.css"; */
/* @import "flyonui/src/vendor/fullcalendar.css"; */
/* @import "flyonui/src/vendor/raty.css"; */
/* @import "flyonui/src/vendor/waves.css"; */
/* @import "flyonui/src/vendor/apexcharts.css"; */
        {{< /code-highlight >}}
  </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Update `eleventy.config.mjs` to copy FlyonUI Javascript -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          3
        </span>
      </div>
      <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
        <div class="text-base-content mb-3 font-semibold">Update `eleventy.config.mjs` to copy FlyonUI Javascript</div>
        <p>
          Copy FlyonUI Javascript.
        </p>
        {{< code-highlight addClass="mt-2" lang="js" >}}export default function (eleventyConfig) {
  // Copy flyonUI JS
  eleventyConfig.addPassthroughCopy({
    "node_modules/flyonui/flyonui.js": "vendor/flyonui/flyonui.js"
  });

  ...
}
  {{< /code-highlight >}}
  </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Add the FlyonUI JavaScript -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          3
        </span>
      </div>
      <div class="timeline-end m-0 mb-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add the FlyonUI JavaScript</div>
        <p>Include FlyonUI JavaScript to the <code>root_directory/src/layouts/default.njk</code> file.</p>
        {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="html" >}}---
title: My Blog
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="/styles/index.css">
  </head>
  <body class="prose">
    {{ content | safe }}

  <!-- FlyonUI JS -->
  <script src="/vendor/flyonui/flyonui.js"></script>  
  </body>
</html>
  {{< /code-highlight >}}
</div>
</li>

  </ul>
</div>

<h2 class="text-lg font-medium mb-1">Icons</h2>
For icons setup you can refer {{< link link="customization/icons/" addClass="link link-primary" >}}Icons{{< /link >}} page.
