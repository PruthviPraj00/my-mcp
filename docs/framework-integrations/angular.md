---
title: "Set up FlyonUI with Angular using Tailwind CSS"
description: "Integrate FlyonUI with Angular and Tailwind CSS to create a modern, responsive UI, streamlining your development process efficiently."
bg_image: "https://cdn.flyonui.com/fy-assets/icons/angular-icon.png"

previous: Framework guides
previousLink: getting-started/framework-guides/
---

{{< callout "info" >}}

<h2 class="text-lg font-medium mb-1">Installation</h2>
The plugin has been tested with the latest framework version (v19.2.4), installed via the standard <code>`ng new project-name`</code> command. Components were created using <code>`ng generate component component-name`</code>. If you're using a custom project structure, pay attention to file paths!
{{< /callout >}}

<div>
  <div class="flex gap-2">
    <div><img src="https://cdn.flyonui.com/fy-assets/icons/angular-icon.png" alt="Angular logo" class="h-auto w-14 mt-2" /></div>
    <div>
      <h2 class="text-base-content mb-3 text-lg font-semibold mt-2">
        Quick
        <span class="text-red-600">Angular</span>
        setup
      </h2>
      <p class="text-base-conte/80 text-base">
        <a href="https://angular.dev/" class="link link-animated link-primary" target="_blank">Angular</a> is a JavaScript framework for building dynamic web applications. If you haven't set up Tailwind CSS yet, check out
        <a class="link link-animated" target="_blank" href="https://tailwindcss.com/docs/guides/angular">
          Angular Tailwind CSS
        </a>
        installation guides.
      </p>
      <div class="tooltip">
        <a href="https://github.com/themeselection/flyonui-angular-integration" target="_blank" type="button" class="tooltip-toggle btn-sm btn btn-outline" aria-label="Tooltip">
          <span class="icon-[tabler--bolt-filled] text-red-600"></span>
          FlyonUI + Angular
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
        <p>Include FlyonUI JavaScript to the <code>root_directory/angular.json</code> file.</p>
        {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}{
  ...
  "projects": {
    "angular": {
      ...
      "architect": {
        "build": {
          ...
          "options": {
            ...
            "scripts": [
              // Optional third-party libraries
              "node_modules/jquery/dist/jquery.min.js",
              "node_modules/lodash/lodash.min.js",
              "node_modules/dropzone/dist/dropzone-min.js",
              "node_modules/nouislider/dist/nouislider.min.js",
              "node_modules/datatables.net/js/dataTables.min.js",

              // FlyonUI
              "node_modules/flyonui/flyonui.js"
            ],
            ...
          }
          ...
        }
        ...
      }
      ...
    }
    ...
  }
  ...
}{{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> If you want to include specific js component:
      </p>
      {{< code-highlight addClass="!mb-0 mt-3" lang="js" >}}"scripts": [
  "node_modules/flyonui/dist/accordion.js"  // Specific JS Component
],
      {{< /code-highlight >}}
      </div>
      <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!-- Add a reinitialization helper -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          5
        </span>
      </div>
      <div class="timeline-end m-0 mb-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add a reinitialization helper</div>
        <p>Add code that reinitializes the components every time the page is refreshed to your app. <code>root_directory/src/app/app.component.ts</code>.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="php" >}}...
import { Router, Event, NavigationEnd } from '@angular/router';

@Component({
  ...
})

export class AppComponent {
  constructor(private router: Router) {
    ...
  }

  ngOnInit() {
    this.router.events.subscribe((event: Event) => {
      if (event instanceof NavigationEnd) {
        setTimeout(() => {
          if (typeof window !== 'undefined' && window.HSStaticMethods) {
            window.HSStaticMethods.autoInit();
          }
        }, 100);
      }
    });
  }
}{{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> If you want to include specific js component
      </p>
      {{< code-highlight addClass="!mb-0 mt-3" lang="js" >}}if (event instanceof NavigationEnd) {
  setTimeout(() => {
    if (typeof window !== 'undefined' && window.HSAccordion) {
      window.HSAccordion.autoInit();   // Add particular component `autoInit()` method
    }
  }, 100);
}
{{< /code-highlight >}}

  </div>
    </li>
  </ul>
</div>


<h2 class="text-lg font-medium mb-1">Icons</h2>
For icons setup you can refer {{< link link="customization/icons/" addClass="link link-primary" >}}Icons{{< /link >}} page.
