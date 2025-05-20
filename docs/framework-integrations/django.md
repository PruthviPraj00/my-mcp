---
title: "Set up FlyonUI with Django using Tailwind CSS"
description: "Integrate FlyonUI with Django and Tailwind CSS to create a responsive, modern interface and streamline your project's design."
bg_image: "https://cdn.flyonui.com/fy-assets/icons/django-icon.png"

previous: Framework guides
previousLink: getting-started/framework-guides/
---

<div>
  <div class="flex gap-2">
    <div><img src="https://cdn.flyonui.com/fy-assets/icons/django-icon.png" alt="django logo" class="h-auto w-14 mt-2" /></div>
    <div>
      <h2 class="text-base-content mb-3 text-lg font-semibold mt-2">
        Quick
        <span class="text-emerald-800">Django</span>
        setup
      </h2>
      <p class="text-base-conte/80 text-base">
        <a href="https://www.djangoproject.com/" class="link link-animated link-primary" target="_blank">Django</a> is a progressive Python framework. If you haven't set up Tailwind CSS yet, refer to the
        <a class="link link-animated" target="_blank" href="https://www.freecodecamp.org/news/how-to-integrate-tailwind-with-django/">
          Django Tailwind CSS
        </a>
        installation guides.
      </p>
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
      <div class="timeline-end m-0 mb-0 w-full rounded-lg p-4">
        <div class="text-base-content mb-3 font-semibold">Add FlyonUI plugin</div>
        <p>Include FlyonUI plugin in your <code>static/main.css</code> file.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="css" >}}// main.css
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
        <div class="text-base-content mb-3 font-semibold">Copy the FlyonUI JavaScript</div>
        <p>Copy FlyonUI's JavaScript (node_modules/flyonui/flyonui.js) files to the <code>static/</code> folder.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}cp node_modules/flyonui/flyonui.js static/js/flyonui.js{{< /code-highlight >}}
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
        <div class="text-base-content mb-3 font-semibold">Add Js to you base.html</div>
        <p>Once you copied the js file to your static folder include it in base.html.</p>
        {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}<html lang="en">
  ...
  <body>
    ...
    <script src="{% static 'js/flyonui.js' %}"></script>
  </body>
</html>
{{< /code-highlight >}}

</div>
</li>
  </ul>
</div>

<h2 class="text-lg font-medium mb-1">Icons</h2>
For icons setup you can refer {{< link link="customization/icons/" addClass="link link-primary" >}}Icons{{< /link >}} page.
