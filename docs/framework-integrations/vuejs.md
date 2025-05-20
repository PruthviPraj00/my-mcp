---
title: "Set up FlyonUI with Vuejs using Tailwind CSS"
description: "Integrate FlyonUI with Vuejs and Tailwind CSS to build a modern, responsive UI, streamlining your development process with ease."
bg_image: "https://cdn.flyonui.com/fy-assets/icons/vue-vite-icon.png"

previous: Framework guides
previousLink: getting-started/framework-guides/
---

{{< callout "info" >}}

<h2 class="text-lg font-medium mb-1">Installation</h2>
Please note that the plugin has been tested with the latest version of the framework (v3.5.13). The framework was installed using the standard <code>`npm create vue@latest`</code> command.
If you are using your own project structure, be mindful of file paths!
{{< /callout >}}

<div>
  <div class="flex gap-2">
    <div><img src="https://cdn.flyonui.com/fy-assets/icons/vue-vite-icon.png" alt="vue logo" class="h-auto w-14 mt-2" /></div>
    <div>
      <h2 class="text-base-content mb-3 text-lg font-semibold mt-2">
        Quick
        <span class="text-emerald-600">Vue.js</span>
        setup
      </h2>
      <p class="text-base-conte/80 text-base">
        <a href="https://vuejs.org/" class="link link-animated link-primary" target="_blank">Vue</a> is a progressive JavaScript framework for building modern web applications. If you haven't set up Tailwind CSS yet, check out
        <a class="link link-animated" target="_blank" href="https://tailwindcss.com/docs/guides/vite#vue">
          Vue Tailwind CSS
        </a>
        installation guides.
      </p>
      <div class="tooltip">
        <a href="https://github.com/themeselection/flyonui-vuejs-integration" target="_blank" type="button" class="tooltip-toggle btn-sm btn btn-outline" aria-label="Tooltip">
          <span class="icon-[tabler--bolt-filled] text-emerald-600"></span>
          FlyonUI + Vue
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

  <!-- Add type definitions for FlyonUI -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        3
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Add type definitions for FlyonUI</div>
      <p>
        Create the <code>global.d.ts</code> file in the project root directory.
      </p>
      {{< code-highlight addClass="mt-2" lang="react" >}}
import type { IStaticMethods } from "flyonui/flyonui";

declare global {
  interface Window {
    // Optional third-party libraries
    _;
    $: typeof import("jquery");
    jQuery: typeof import("jquery");
    DataTable;
    Dropzone;

    // FlyonUI
    HSStaticMethods: IStaticMethods;
  }
}

export {};
  {{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> If you want to include specific js component
      </p>
      {{< code-highlight addClass="mt-2" lang="react" >}}
import { HSAccordion } from "flyonui/flyonui";

declare global {
  interface Window {
    // Specific JS component
    HSAccordion: typeof HSAccordion;
  }
}

export {};
  {{< /code-highlight >}}
  </div>
  <hr class="!w-0.5 rounded-none border-transparent" />
  </li>
    <!-- Add the FlyonUI JavaScript -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          4
        </span>
      </div>
      <div class="timeline-end m-0 mb-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add the FlyonUI JavaScript</div>
        <p>Add the FlyonUI JavaScript in your app entry point <code>root_directory/src/main.ts|js</code></p>
        {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}...
// Optional third-party libraries
import $ from "jquery";
import _ from "lodash";
import noUiSlider from "nouislider";
import "datatables.net";
import "dropzone/dist/dropzone-min.js";

window._ = _;
window.$ = $;
window.jQuery = $;
window.DataTable = $.fn.dataTable;
window.noUiSlider = noUiSlider;

// FlyonUI
import "flyonui/flyonui";
...
app.mount("#app");
      {{< /code-highlight >}}
        <p class="!mt-4">
        <strong>Note:</strong> If you want to include specific js component
      </p>
      {{< code-highlight addClass="!mb-0 mt-3" lang="js" >}}...
import 'flyonui/dist/accordion';  // Import specific component JS
...
app.mount("#app");
  {{< /code-highlight >}}
      </div>
      <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Add a reinitialization helper (vue-router) -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          5
        </span>
      </div>
      <div class="timeline-end m-0 mb-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add a reinitialization helper (vue-router)</div>
        <p>Add code that reinitializes the components every time the page is refreshed to your "route" <code>root_directory/src/router/index.ts|js</code>.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="js" >}}import { createRouter, createWebHistory } from 'vue-router'
...

const router = createRouter({
  ...
});

router.afterEach(async (to, from, failure) => {
  if (!failure) setTimeout(() => window.HSStaticMethods.autoInit(), 100);
});

export default router;
            {{< /code-highlight >}}
            <p class="!mt-4">
              <strong>Note:</strong> If you want to include specific js component
            </p>
      {{< code-highlight addClass="!mb-0 mt-3" lang="js" >}}
router.afterEach(async (to, from, failure) => {
  if (!failure) setTimeout(() => window.HSAccordion.autoInit(), 100);
});{{< /code-highlight >}}
      </div>
      <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Add a reinitialization helper (without router) -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          6
        </span>
      </div>
      <div class="timeline-end m-0 mb-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add a reinitialization helper (without router)</div>
        <p>Add code that reinitializes the components every time when app is mounted <code>root_directory/src/App.vue</code></p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}<script setup>
  onMounted(() => {
    setTimeout(() => window.HSStaticMethods.autoInit(), 100)
  });
</script>

...{{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> If you want to include specific js component
      </p>
      {{< code-highlight addClass="!mb-0 mt-3" lang="html" >}}<script setup>
  onMounted(() => {
    setTimeout(() => window.HSAccordion.autoInit(), 100)
  });
</script>
    {{< /code-highlight >}}
      </div>
    </li>
  </ul>
</div>

<h2 class="text-lg font-medium mb-1">Icons</h2>
For icons setup you can refer {{< link link="customization/icons/" addClass="link link-primary" >}}Icons{{< /link >}} page.
