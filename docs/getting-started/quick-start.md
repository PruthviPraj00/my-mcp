---
title: "Quick Start"
description: "Quickly get started with FlyonUI and unleash its powerful features in just minutes."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "getting-started"
    weight: 2

previous: Introduction
previousLink: getting-started/introduction/

next: Upgrade Guide
nextLink: getting-started/upgrade/
---

FlyonUI brings together the beauty of **semantic classes** and the interactive **headless JavaScript plugins**, offering you a powerful toolkit to build stunning, interactive user interfaces with ease.

<!-------------------- Getting Started -------------------->

{{< headsingle level="2" >}} Getting Started {{< /headsingle >}}

This guide will walk you through getting started with FlyonUI. You’ll learn how to set it up, customize it, keep it updated, and integrate it into your project!

Make sure that you have <a href="https://nodejs.org/en/" class="link link-primary" target="_blank">Node.js</a> and <a href="https://tailwindcss.com/" class="link link-primary" target="_blank">Tailwind CSS</a> installed.

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical w-full ps-0 mb-0">
  
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        1
      </span>
    </div>
    <div class="timeline-end mb-0 ms-1 w-full rounded-lg p-4 pt-1">
      <div class="text-base-content mb-3 font-semibold">Install FlyonUI</div>
      <p>To start, add FlyonUI as a dependency to your project by running the following command:</p>
      {{< code-highlight addClass="!mb-0 mt-3" lang="bash" >}}npm install flyonui{{< /code-highlight >}}
      <p class="not-prose mt-4">This will install FlyonUI and make it available for use in your project.</p>
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Configure Tailwind -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 ms-1 w-full rounded-lg p-4 pt-1">
      <div class="text-base-content mb-3 font-semibold">Add flyonui to app.css:</div>
      <p>
        Next, configure main CSS to use FlyonUI.
      </p>
      {{< code-highlight addClass="!mb-0 mt-3" lang="css" >}}
@import "tailwindcss";
@plugin "flyonui";
@import "./node_modules/flyonui/variants.css"; /* Require only if you want to use FlyonUI JS component */

/* If you gitignored node_modules use below method */
@source "./node_modules/flyonui/dist/index.js"; /* Require only if you want to use FlyonUI JS component */
{{< /code-highlight >}}

<p class="not-prose mt-4">This ensures that FlyonUI's styling is applied correctly throughout your project.</p>

If you want to include specific js component:

{{< code-highlight addClass="!mb-0 mt-3" lang="css" >}}@source "./node_modules/flyonui/dist/accordion.js"; {{< /code-highlight >}}

</div>
<hr class="!w-0.5 rounded-none border-transparent" />

  </li>

  <!-- Tailwind Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
      3
      </span>
    </div>
    <div class="timeline-end mb-0 ms-1 w-full rounded-lg p-4 pt-1">
      <div class="text-base-content mb-3 font-semibold">Include FlyonUI JavaScript in HTML for JS components</div>
      <p>For enabling interactive components such as accordion, dropdown, modal etc... , include FlyonUI's JavaScript in your HTML file, just before the closing <code>&lt;/body&gt;</code> tag:</p>
        {{< code-highlight addClass="!mb-0 mt-3" lang="html" >}}<script src="../node_modules/flyonui/flyonui.js"></script>{{< /code-highlight >}}
      <p class="not-prose mt-4">For a single component, use the specific path:</p>
      {{< code-highlight addClass="!mb-0 mt-3" lang="html" >}}<script src="../node_modules/flyonui/dist/accordion.js"></script> {{< /code-highlight >}}</div>
  </li>
</ul>

<!-------------------- Setup Icons -------------------->

{{< headsingle level="2" >}} Setup Icons {{< /headsingle >}}

FlyonUI utilizes <a href="https://icon-sets.iconify.design/tabler/" class="link link-primary" target="_blank">Tabler icons</a>, which are available through <a href="https://iconify.design/" class="link link-primary" target="_blank">Iconify</a>.

For detailed installation instructions, refer to the official <a href="https://iconify.design/docs/usage/css/tailwind/tailwind4/" class="link link-primary" target="_blank">documentation</a>, or follow the steps below to set it up.

> You can refer {{< link link="customization/icons/" addClass="link link-primary" >}}Icons{{< /link >}} page for more info 

1. **Install the plugin**  
   Begin by adding `@iconify/tailwind4` as a dev dependency:
   {{< code-highlight addClass="!mb-0 mt-3" lang="bash" >}}npm i -D @iconify/tailwind4{{< /code-highlight >}}

2. **Add Tabler icons**  
   Install the Tabler icon set by running:
   {{< code-highlight addClass="!mb-0 mt-3" lang="bash" >}}npm i -D @iconify-json/tabler{{< /code-highlight >}}

3. **Basic Usage**  
   To include the icons, add the following line to your CSS file:
   {{< code-highlight addClass="mt-3" lang="bash" >}}@plugin "@iconify/tailwind4";{{< /code-highlight >}}
   Then, to use an icon in your HTML, add a dynamic class selector for the desired icon. For example:
   {{< code-highlight addClass="!mb-0 mt-3" lang="html" >}}<span class="icon-[tabler--upload]"></span>{{< /code-highlight >}}

<!-- //TODO - Left to do  -->
<!-------------------- Why No CDN Support? -------------------->

{{< headsingle level="2" >}} Why No CDN Support? {{< /headsingle >}}

FlyonUI does not provide CDN support due to the way its styles and components are dynamically generated and integrated with JavaScript. The FlyonUI library relies on generating the required styles based on the specific javascript components being used, which makes it challenging to deliver a static version via CDN for development environments. This dynamic nature means that during development, FlyonUI needs to have access to the tools that generate these styles on-demand, making CDN integration complex and impractical in most cases.

Additionally, while CDNs are commonly used to host static resources like CSS and JS files, FlyonUI's requirement for dynamic style generation tailored to JavaScript-driven components limits this approach. We suggests that users can still use CDNs for production environments where the generated styles are finalized and static, but not during development .

<!-------------------- How do I import a single css component -------------------->

{{< headsingle level="2" >}} How do I import a single css component {{< /headsingle >}}

To import a single CSS component from a library, you can utilize the `include` configuration property. This allows you to selectively load only the components you need, reducing unnecessary styles and optimizing your project.

```php
@plugin "flyonui" {
  include: badge, dropdown, timeline;
}
```
</br>
In the example above, only the `badge`, `dropdown`, and `timeline` components from the FlyonUI library are included. All other components and styles are excluded from being imported, which can help keep your stylesheets more lightweight and efficient.

<!-------------------- How do I import a single JavaScript component? -------------------->


{{< headsingle level="2" >}} How do I import a single JavaScript component? {{< /headsingle >}}

To use a single JS component, let’s walk through the steps. In this example, we’ll focus on the accordion component.
> Please note that not all JavaScript components have variants. You can refer to the class table in the documentation to check if a component offers variant options.

**Step 1: Import the JavaScript for the component**

To enable the interactive accordion component, include the FlyonUI JavaScript file for the accordion just before the closing `</body>` tag. This file contains all the necessary JavaScript for accordion.

```html
<script src="../node_modules/flyonui/dist/accordion.js"></script>
```

</br>

**Step 2: Update main.css**

Add variants css for accordion and accordion.css.

```php
@plugin "flyonui" {
  include: accordion;
}
@import "./node_modules/flyonui/src/js/plugins/accordion/variants.css"

// If you gitignored node_modules use below method 
@source "./node_modules/flyonui/dist/accordion.js";
```

</br>

{{< callout "info" >}}
<span class="font-semibold">NOTE :</span> Following these steps helps reduce the size of the generated JS and CSS.
{{< /callout >}}

<!-- ### Integration via CDN -->

<!-- For a quicker setup, FlyonUI is also available via CDN.

#### Step 1: Include FlyonUI CSS via CDN

To include FlyonUI styles, add the following link tag inside the `<head>` of your HTML file:

```html
<link href="https://cdn.jsdelivr.net/npm/flyonui@/dist/flyonui.min.css" rel="stylesheet" />
```

#### Step 2: Include FlyonUI JavaScript via CDN

Similarly, before the closing `</body>` tag, add the FlyonUI JavaScript file:

```html
<script src="https://cdn.jsdelivr.net/npm/flyonui@/dist/flyonui.min.js"></script>
```

While this method is convenient, note that CDN files are not optimized for production as you cannot purge unused styles, which may lead to larger file sizes. -->

<!-------------------- Bundling FlyonUI with Webpack or Parcel -------------------->

{{< headsingle level="2" >}} Bundling FlyonUI with Webpack or Parcel {{< /headsingle >}}

To bundle FlyonUI into your project using a JavaScript bundler like Webpack or Parcel, follow these steps:

**Step 1: Import FlyonUI JavaScript**

In your main JavaScript file (e.g., `app-bundle.js`), import FlyonUI:

```js
import "flyonui/flyonui"
```

</br>

**Step 2: Include the JavaScript in HTML**

For a single component, import the specific component:

```js
import "flyonui/dist/accordion"
```

</br>

**Step 3: Include the JavaScript in HTML**

Finally, ensure your bundled JavaScript file is included in your HTML:

```html
<script src="../path-to/flyonui.js"></script>
```

<p class="not-prose my-5">For more details on FlyonUI's JavaScript capabilities, check out the a {{< link link="getting-started/javascript/" addClass="link link-primary" >}}JavaScript documentation{{< /link >}}.</p>
