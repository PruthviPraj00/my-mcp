---
title: "Set up FlyonUI with SolidJS using Tailwind CSS"
description: "Integrate FlyonUI with SolidJS and Tailwind CSS to create a modern, responsive UI, simplifying your development workflow with ease."
bg_image: "https://cdn.flyonui.com/fy-assets/icons/solidjs-icon.png"

previous: Framework guides
previousLink: getting-started/framework-guides/
---

{{< callout "info" >}}

<h2 class="text-lg font-medium mb-1">Installation</h2>
Please note that the plugin has been tested with the latest version of the framework (v1.9.5). The framework was installed using the standard <code>`npm create vite@latest project-name -- --template solid`</code> command.
If you are using your own project structure, be mindful of file paths!
{{< /callout >}}

<div>
  <div class="flex gap-2">
    <div><img src="https://cdn.flyonui.com/fy-assets/icons/solidjs-icon.png" alt="SolidJS logo" class="h-auto w-14 mt-2" /></div>
    <div>
      <h2 class="text-base-content mb-3 text-lg font-semibold mt-2">
        Quick
        <span class="text-sky-700">SolidJS</span>
        setup
      </h2>
      <p class="text-base-conte/80 text-base">
        A tool for building simple, performant, and reactive user interfaces. If you haven't set up Tailwind CSS yet, check out
        <a class="link link-primary link-animated" target="_blank" href="https://tailwindcss.com/docs/guides/solidjs">
          SolidJS Tailwind CSS
        </a>
        installation guides.
      </p>
      <div class="tooltip">
        <a href="https://github.com/themeselection/flyonui-solidjs-integration" target="_blank" type="button" class="tooltip-toggle btn-sm btn btn-outline" aria-label="Tooltip">
          <span class="icon-[tabler--bolt-filled] text-sky-700"></span>
          FlyonUI + SolidJS
        </a>
        <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
          <span class="tooltip-body">Check out the starterkit</span>
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
    <!-- Add FlyonUI plugin -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Add FlyonUI plugin</div>
      <p>
        Include FlyonUI plugin in your <code>index.css</code> file.
      </p>
      {{< code-highlight addClass="mt-2" lang="css" >}}
// index.css
@import "tailwindcss";
@plugin "flyonui";
@import "flyonui/variants.css";
@source "./node_modules/flyonui/flyonui.js"; // Add only if node_modules is gitignored

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
// index.css
@source "./node_modules/flyonui/dist/accordion.js" // Specific JS component
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
      {{< code-highlight addClass="mt-2" lang="react" >}}// global.d.ts
import { IStaticMethods } from "flyonui/flyonui.js";

declare global {
  interface Window {
    // Optional third-party libraries
    _;
    $: typeof import("jquery");
    jQuery: typeof import("jquery");
    DataTable;
    Dropzone;

    HSStaticMethods: IStaticMethods;
  }
}

export {};
{{< /code-highlight >}}
  <p><strong>Note:</strong> If you want to include specific js component </p>

  {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}
// global.d.ts
import { HSAccordion } from "flyonui/flyonui.js";

declare global {
  interface Window {
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
        <p>Add the FlyonUI JavaScript in your app entry point <code>root_directory/src/index.tsx</code></p>
        {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}import { render } from 'solid-js/web';

import 'flyonui/flyonui';
import App from './App';


const root = document.getElementById('root');

render(() => (
  <Router>
    <App />
  </Router>
), root!);

{{< /code-highlight >}}
</div>
<hr class="!w-0.5 rounded-none border-transparent" />
</li>
<!-- Add a reinitialization helper -->
<li class="mt-0 mb-0 ps-0">
<div class="timeline-middle mb-2">
<span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
4
</span>
</div>
<div class="timeline-end m-0 mb-0 w-full rounded-lg p-4">
<div class="text-base-content mb-3 font-semibold">Add a reinitialization helper</div>
<p>Add code to reinitialize the components each time the app is mounted or when the page changes in <code>root_directory/src/App.tsx</code>.</p>
{{< code-highlight addClass="mt-2" lang="js" >}}import { useLocation } from '@solidjs/router';
import { createEffect, createSignal } from 'solid-js';
import { render } from 'solid-js/web';

...

async function loadFlyonUI() {
  return import('flyonui/flyonui.js');
}

...

const App = () => {
  const location = useLocation();
  const [_, setLoc] = createSignal(location.pathname);

  createEffect(() => {
    const initFlyonUI = async () => {
      await loadFlyonUI();
    };

    initFlyonUI();
  });

  createEffect(() => {
    setLoc(location.pathname);

    setTimeout(() => {
      if (
        window.HSStaticMethods &&
        typeof window.HSStaticMethods.autoInit === 'function'
      ) {
        window.HSStaticMethods.autoInit();
      }
    }, 100);
  });

  return (
    ...
  );
};

export default App;
{{< /code-highlight >}}
<p><strong>Note:</strong> If you want to include specific js component </p>

{{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}
...

async function loadFlyonUI() {
  return import('flyonui/dist/accordion.js');
}

...

const App = () => {
  const location = useLocation();
  const [_, setLoc] = createSignal(location.pathname);

  createEffect(() => {
    const initFlyonUI = async () => {
      await loadFlyonUI();
    };

    initFlyonUI();
  });

  createEffect(() => {
    setLoc(location.pathname);

    setTimeout(() => {
      if (
        window.HSAccordion &&
        typeof window.HSAccordion.autoInit === 'function'
      ) {
        window.HSAccordion.autoInit();
      }
    }, 100);
  });

  return (
    ...
  );
};

export default App;
{{< /code-highlight >}}
</div>
</li>

  </ul>
</div>

<h2 class="text-lg font-medium mb-1">Icons</h2>
For icons setup you can refer {{< link link="customization/icons/" addClass="link link-primary" >}}Icons{{< /link >}} page.
