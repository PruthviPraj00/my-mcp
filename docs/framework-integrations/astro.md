---
title: "Set up FlyonUI with Astro using Tailwind CSS"
description: "Integrate FlyonUI with Astro and Tailwind CSS to build a modern, responsive UI, optimizing your development process for efficiency."
bg_image: "https://cdn.flyonui.com/fy-assets/icons/astro-icon.png"

previous: Framework guides
previousLink: getting-started/framework-guides/
---

{{< callout "info" >}}

<h2 class="text-lg font-medium">Installation</h2>
Please note that the plugin has been tested with the latest version of the framework (v5.5.5). The framework was installed using the standard <code>`npm create astro@latest`</code> command. If you are using your own project structure, be mindful of file paths!
{{< /callout >}}

<div>
  <div class="flex gap-2">
    <div><img src="https://cdn.flyonui.com/fy-assets/icons/astro-icon.png" alt="Astro logo" class="h-auto w-14 mt-2" /></div>
    <div>
      <h2 class="text-base-content mb-3 text-lg font-semibold mt-2">
        Quick
        <span class="text-base-content text-orange-500">Astro</span>
        setup
      </h2>
      <p class="text-base-conte/80 text-base">
        <a href="https://astro.build/" class="link link-animated link-primary" target="_blank">Astro</a> is the all-in-one web framework designed for speed. If you haven't set up Tailwind CSS yet, check out
        <a class="link link-animated" target="_blank" href="https://tailwindcss.com/docs/guides/astro">
          Astro Tailwind CSS
        </a>
        installation guides.
      </p>
      <div class="tooltip">
        <a href="https://github.com/themeselection/flyonui-astro-integration" target="_blank" type="button" class="tooltip-toggle btn-sm btn btn-outline" aria-label="Tooltip">
          <span class="icon-[tabler--bolt-filled] text-orange-500"></span>
          FlyonUI + Astro
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
        <p><strong>Note:</strong> If you want to include specific js component </p>
        {{< callout "info" >}}
          <span class="font-semibold">Tip :</span> Using specific components helps minimize the size of the generated JavaScript and CSS.
        {{< /callout >}}
        {{< code-highlight addClass="!mb-0 mt-2" lang="css" >}}
@source "../node_modules/flyonui/dist/accordion.js" // Specific JS component
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
        <p>Include FlyonUI JavaScript to the <code>root_directory/src/layouts/Layout.astro</code> file.</p>
        {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="html" >}}---
import "../styles/global.css";
---

<!DOCTYPE html>
<html lang="en">
  ...
</html>

<!-- Optional plugins -->
<script is:inline src="../node_modules/jquery/dist/jquery.min.js"></script>
<script is:inline src="../node_modules/lodash/lodash.js"></script>
<script is:inline src="../node_modules/datatables.net/js/dataTables.min.js"></script>
<script is:inline src="../node_modules/dropzone/dist/dropzone-min.js"></script>
<script is:inline src="../node_modules/nouislider/dist/nouislider.min.js"></script>

<!-- FlyonUI -->
<script is:inline src="../node_modules/flyonui/flyonui.js"></script>

  {{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> If you want to include specific js component
      </p>
      {{< code-highlight addClass="!mb-0 mt-3" lang="html" >}}<script is:inline src="../node_modules/flyonui/dist/accordion.js"></script>    // Specific JS component
      {{< /code-highlight >}}

</div>
</li>

  </ul>
</div>

<h2 class="text-lg font-medium mb-1">Icons</h2>
For icons setup you can refer {{< link link="customization/icons/" addClass="link link-primary" >}}Icons{{< /link >}} page.
