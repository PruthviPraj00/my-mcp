---
title: "Set up FlyonUI with Laravel using Tailwind CSS"
description: "Integrate FlyonUI with Laravel and Tailwind CSS to create a responsive, modern interface and streamline your project's design."
bg_image: "https://cdn.flyonui.com/fy-assets/icons/laravel-icon.png"

previous: Framework guides
previousLink: getting-started/framework-guides/
---

<div>
  <div class="flex gap-2">
    <div><img src="https://cdn.flyonui.com/fy-assets/icons/laravel-icon.png" alt="laravel logo" class="h-auto w-14 mt-2" /></div>
    <div>
      <h2 class="text-base-content mb-3 text-lg font-semibold mt-2">
        Quick
        <span class="text-red-600">Laravel</span>
        setup
      </h2>
      <p class="text-base-conte/80 text-base">
        <a href="https://laravel.com/" class="link link-animated link-primary" target="_blank">Laravel</a> is most popular PHP web application framework with expressive, elegant syntax. If you haven't set up Tailwind CSS yet, check out
        <a class="link link-animated" target="_blank" href="https://tailwindcss.com/docs/guides/laravel">
          Laravel Tailwind CSS
        </a>
        installation guides.
      </p>
    </div>
  </div>

> Use this GitHub <a href="https://github.com/themeselection/flyonui-tailwindcss-laravel-livewire-starter-kit" class="link link-primary" target="_blank">repository</a> for a pre-configured **FlyonUI Laravel Livewire Starter Kit**.

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
        <p>Add the FlyonUI JavaScript in your app entry point <code>app.js</code></p>
        {{< code-highlight addClass="mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}// index.js
import "flyonui/flyonui"{{< /code-highlight >}}
<p><strong>Note:</strong> If you want to include specific js component </p>

{{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}
import "../node_modules/flyonui/dist/accordion.js" // Import particular component JS
{{< /code-highlight >}}
  </div>
      <hr class="!w-0.5 rounded-none border-transparent" />
    </li>
    <!--  -->
    <li class="mt-0 mb-0 ps-0">
      <div class="timeline-middle mb-2">
        <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
          4
        </span>
      </div>
      <div class="timeline-end m-0 mb-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Loading your scripts</div>
        <p>Once your Vite entry points are configured, simply reference them using the <code>@vite()</code> Blade directive in the <code>head</code> tag of your application's main template.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="php" >}}<!doctype html>
<head>
    {{-- ... --}}
    @vite('resources/css/app.css')
    @vite('resources/js/app.js')
</head>
{{< /code-highlight >}}
</div>
<hr class="!w-0.5 rounded-none border-transparent" />
</li>

  </ul>
</div>

<h2 class="text-lg font-medium mb-1">Icons</h2>
For icons setup you can refer {{< link link="customization/icons/" addClass="link link-primary" >}}Icons{{< /link >}} page.
