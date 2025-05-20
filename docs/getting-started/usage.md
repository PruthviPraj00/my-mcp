---
title: "Usage"
description: "Master FlyonUI with component and modifier classes for easy customization and dynamic UI updates."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "getting-started"
    weight: 4

previous: Quick start
previousLink: getting-started/quick-start/

next: Javascript
nextLink: getting-started/javascript/
---

<!-------------------- Add component classes to your HTML -------------------->

{{< headsingle addClass="!mt-px" level="2" >}} Add component classes to your HTML {{< /headsingle >}}

After installing FlyonUI, you use its component classes, such as `btn` and `card`, to your HTML elements effortlessly.

<ol class="list-inside list-decimal ps-0">
  <li class="mb-2">Instead of manually constructing a button with multiple utility classes:</li>
</ol>

```html
<button
  class="inline-block cursor-pointer rounded-md bg-blue-500 px-4 py-3 
  text-center text-sm font-semibold uppercase text-white transition
  duration-200 ease-in-out hover:bg-blue-600">
  Button
</button>
```

<button class="inline-block cursor-pointer rounded-md bg-blue-500 px-4 py-3 text-center text-sm font-semibold uppercase text-white transition duration-200 ease-in-out hover:bg-blue-600 mt-4">Button</button>

<ol start="2" class="list-inside list-decimal ps-0">
  <li class="mb-2">You can simply use a FlyonUI component class:</li>
</ol>

```html
<button class="btn">Button</button>
```

<button class="btn mt-4">Button</button>

<ol start="3" class="list-inside list-decimal ps-0">
  <li class="mb-2">Further customization is easy using {{< link link="components/button/" addClass="link link-primary" >}}FlyonUI utility classes{{< /link >}}:</li>
</ol>

```html
<button class="btn btn-primary">Button</button>
```

<button class="btn btn-primary mt-4">Button</button>

<ol start="4" class="list-inside list-decimal ps-0">
  <li class="mb-2">For even more flexibility, combine FlyonUI with <a href="https://tailwindcss.com/docs/border-radius" class="link link-primary" target="_blank">Tailwind CSS utilities</a>:</li>
</ol>

```html
<button class="btn rounded-full">Button</button>
```

<button class="btn rounded-full mt-4">Button</button>

{{< headsingle level="2" >}} Using Modifier Classes for JS Components {{< /headsingle >}}

FlyonUI also provides modifier classes that allow dynamic component changes based on specific events.

<!-- Example -->

{{< headsingle level="4" >}} Example {{< /headsingle >}}

In this example, the `collapse-open:` modifier changes the button's text and rotates the icon when the collapsible section opens or closes.


```html 
<button type="button" class="collapse-toggle btn btn-primary" id="basic-collapse" aria-expanded="false" aria-controls="basic-collapse-heading" data-collapse="#basic-collapse-heading" >
  <span class="collapse-open:hidden">Collapsed</span>
  <span class="collapse-open:block hidden">Collapse</span>
  <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 transition-rotate size-4 duration-300"></span>
</button>
<div id="basic-collapse-heading" class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="basic-collapse" >
  <div class="border-base-content/25 mt-3 rounded-md border p-3">
    <p class="text-base-content/80">
      The collapsible body remains hidden until the collapse plugin adds specific classes. These control appearance and
      manage visibility through transitions.
    </p>
  </div>
</div>
```

<button type="button" class="collapse-toggle btn btn-primary mt-4" id="basic-collapse" aria-expanded="false" aria-controls="basic-collapse-heading" data-collapse="#basic-collapse-heading" >
  <span class="collapse-open:hidden">Collapsed</span>
  <span class="collapse-open:block hidden">Collapse</span>
  <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 transition-rotate size-4 duration-300"></span>
</button>
<div id="basic-collapse-heading" class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="basic-collapse" >
  <div class="border-base-content/25 mt-3 rounded-md border p-3">
    <p class="text-base-content/80 mb-0">
      The collapsible body remains hidden until the collapse plugin adds specific classes. These control appearance and manage visibility through transitions.
    </p>
  </div>
</div>

<p class="not-prose my-4">This example shows how modifier classes adjust components dynamically based on user interaction.</p>
