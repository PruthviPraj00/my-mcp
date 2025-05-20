---
title: "Setup FlyonUI with Svelte using Tailwind CSS."
description: "Configuring FlyonUI within a Svelte project while incorporating Tailwind CSS for enhanced styling."
bg_image: "https://cdn.flyonui.com/fy-assets/icons/svelte-icon.png"

previous: Framework guides
previousLink: getting-started/framework-guides/
---

{{< callout "info" >}}

<h2 class="text-lg font-medium mb-1">Installation</h2>
Please note that this plugin has been tested with the latest framework version (v5.0.5). It was installed using the standard <code>`npx sv create my-app`</code> command.<br/>
If you’re working with a custom project setup or a different framework version, be sure to check the file paths and features specific to your version!

{{< /callout >}}

<div>
  <div class="flex gap-2">
    <div><img src="https://cdn.flyonui.com/fy-assets/icons/svelte-icon.png" alt="svelte logo" class="h-auto w-14 mt-2" /></div>
    <div>
      <h2 class="text-base-content mb-3 text-lg font-semibold mt-2">
        Quick
        <span class="text-error">Svelte</span>
        setup
      </h2>
      <p class="text-base-conte/80 text-base">
        <a href="https://svelte.dev/" class="link link-animated link-primary" target="_blank">Svelte</a> is a powerful JavaScript framework designed for building fast, efficient web applications. If you haven't configured Tailwind CSS yet, refer to the <a class="link link-animated" target="_blank" href="https://tailwindcss.com/docs/guides/sveltekit">SvelteKit Tailwind</a> CSS installation guide.
      </p>
      <div class="tooltip">
        <a type="button" class="tooltip-toggle btn-sm btn btn-outline" href="https://github.com/themeselection/flyonui-svelte-integration" target="_blank" aria-label="Tooltip">
          <span class="icon-[tabler--bolt-filled] bg-error"></span>
          FlyonUI + Svelte
        </a>
        <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
          <span class="tooltip-body">Check out the staterkit</span>
        </span>
      </div>
    </div>
  </div>

  <ul class="timeline timeline-snap-icon timeline-compact timeline-vertical mb-12 w-full ps-0">
    <!-- Step 1: Installation -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          1
        </span>
      </div>
      <div class="timeline-end m-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Install FlyonUI</div>
        <p>
          To get started, install
          <code>flyonui</code>
          via npm.
        </p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm i flyonui{{< /code-highlight >}}
      </div>
      <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Step 2: Configure paths -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          2
        </span>
      </div>
      <div class="timeline-end m-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add FlyonUI plugin</div>
        <p>Include FlyonUI in your <code>projects_root_directory/src/app.css</code> file.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="css" >}}@import "tailwindcss";
@plugin "flyonui";
@import "flyonui/variants.css"; /* Required for Js components */

@source "../node_modules/flyonui/flyonui/index.js"; /* Required for Js components */

/* Import Third-party override css */
/* @import "flyonui/src/vendor/flatpickr.css"; */
/* @import "flyonui/src/vendor/notyf.css"; */
/* @import "flyonui/src/vendor/datatables.css"; */
/* @import "flyonui/src/vendor/editor.css"; */
/* @import "flyonui/src/vendor/fullcalendar.css"; */
/* @import "flyonui/src/vendor/raty.css"; */
/* @import "flyonui/src/vendor/waves.css"; */
/* @import "flyonui/src/vendor/apexcharts.css"; */

...{{< /code-highlight >}}
      </div>
      <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Step 3: Add FlyonUI JavaScript -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          3
        </span>
      </div>
      <div class="timeline-end m-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add type definitions for FlyonUI</div>
        <p>Add FlyonUI in <code>projects_root_directory/src/app.d.ts</code> file.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="rs" >}}import type { IStaticMethods } from "flyonui/flyonui";

declare global {
  interface Window {
    // Optional plugins
    _;
    $: typeof import("jquery");
    jQuery: typeof import("jquery");
    DataTable;
    Dropzone;

    // FlyonUI
    HSStaticMethods: IStaticMethods;
  }

  namespace App {
    ...
  }
}

export {};{{< /code-highlight >}}
      </div>
      <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Step 4: Reinitialize with vue-router -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          4
        </span>
      </div>
      <div class="timeline-end m-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add the FlyonUI JavaScript</div>
        <p>Add the FlyonUI JavaScript in your app entry point <code>projects_root_directory/src/lib/client/
init.ts</code> file.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="ts" >}}// Optional plugins
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
import("flyonui/flyonui");{{< /code-highlight >}}

<p>Add the FlyonUI Hook <code>projects_root_directory/src/
hooks.client.ts</code> file.</p>

{{< code-highlight addClass="!mb-0 mt-2" lang="ts" >}}import "./lib/client/init";{{< /code-highlight >}}
      </div>
      <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Step 5: Reinitialize without vue-router -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          5
        </span>
      </div>
      <div class="timeline-end m-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add a reinitialization helper</div>
        <p>Insert the code that reinitializes components whenever  to ensure that FlyonUI.js is reinitialized after any DOM updates and navigation events changes   in <code>projects_root_directory/src/routes/+layout.svelte</code>.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}<script>
  import { afterNavigate } from "$app/navigation";

  afterNavigate(() => {
    // Runs after navigating between pages
    HSStaticMethods.autoInit();
  });
</script>{{< /code-highlight >}}
</div>
</li>
  </ul>
</div>

<h2 class="text-lg font-medium mb-1">Icons</h2>
For icons setup you can refer {{< link link="customization/icons/" addClass="link link-primary" >}}Icons{{< /link >}} page.

<h2 class="text-lg font-medium mb-1">Hints and Tips</h2>

Passing parameters using data attributes. Observe how the object containing the parameters is wrapped in curly braces and how the slashes are properly escaped.

```svelte
<div class="max-w-sm">
  <select
    data-select={`{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\\"button\\" aria-expanded=\\"false\\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\\"flex justify-between items-center w-full\\"><span data-title></span><span class=\\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \\"></span></div>",
    "extraMarkup": "<span class=\\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \\"></span>"
    }`}
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>

```
