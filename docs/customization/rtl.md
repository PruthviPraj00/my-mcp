---
title: "RTL"
description: "Learn how to setup and configure bidirectional text formats (RTL and LTR) in your project using native Tailwind CSS variants and the FlyonUI components."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "customization"
    weight: 7

previous: Utilities and Variables
previousLink: customization/utilities/

next: Theme Generator
nextLink: customization/theme-generator/
---

<!-------------------- RTL(right-to-left) -------------------->

{{< headsingle addClass="!mt-px" level="2" >}} RTL(right-to-left) {{< /headsingle >}}

RTL (right-to-left) is a text orientation used for languages such as Arabic, Hebrew, Persian, Urdu, and Yiddish, spoken by over 500 million people. It is also among the fastest-growing language groups online.

All FlyonUI components seamlessly support RTL by leveraging logical CSS properties and values, like using `ms-0` instead of `ml-0` and `pe-4` instead of `pr-4`. This functionality requires Tailwind CSS v3.3.0.

In this guide, you'll learn how to set up and configure bidirectional text formats (RTL and LTR) in your project using Tailwind CSS variants and FlyonUI components by modifying the `dir` attribute on the `<html>` element.

<!-- Setting up RTL  -->

{{< headname level="3" >}} Setting up RTL {{< /headname >}}

Before you begin, ensure you have the latest version of <a href="https://tailwindcss.com/docs/installation" target="_blank">Tailwind CSS</a> and {{< link link="getting-started/quick-start/" addClass="link link-primary" >}}FlyonUI{{< /link >}} installed.

To enable RTL support, add the `dir` attribute to the `<html>` tag in your `index.html` file:

```html
<html dir="rtl">
  <!-- your HTML markup -->
</html>
```

<br />

All FlyonUI components are fully compatible with RTL mode, utilizing Tailwind CSS's logical properties for easy adaptability. You can test this functionality by toggling between LTR and RTL modes using the RTL button below.

{{< code addClass="!block" >}}

<div class="accordion accordion-shadow *:accordion-item-active:shadow-md">
  <div class="accordion-item active" id="payment-arrow-right">
    <button class="accordion-toggle inline-flex items-center justify-between text-start" aria-controls="payment-arrow-right-collapse" aria-expanded="true">
      <div class="flex gap-4">
        <div class="avatar">
          <div class="size-12 rounded-md">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="avatar" />
          </div>
        </div>
        <div>
          <p class="mb-0.5">Richard Payne</p>
          <p class="text-sm text-base-content/50 font-normal">pwright@yahoo.com</p>
        </div>
      </div>
      <span class="icon-[tabler--chevron-left] accordion-item-active:-rotate-90 size-5 shrink-0 transition-transform duration-300 rtl:-rotate-180"></span>
    </button>
    <div id="payment-arrow-right-collapse" class="accordion-content w-full overflow-hidden transition-[height] duration-300" aria-labelledby="payment-arrow-right" role="region">
      <div class="px-5 pb-4">
        <p class="text-base-content/80 font-normal">
          Richard Payne is a remarkable individual known for his exceptional skills and expertise in various fields. With a strong background in technology and a passion for innovation, Richard has made significant contributions to the industry.
        </p>
      </div>
    </div>
  </div>
  
  <div class="accordion-item" id="delivery-arrow-right">
    <button class="accordion-toggle inline-flex items-center justify-between text-start" aria-controls="delivery-arrow-right-collapse" aria-expanded="false">
      <div class="flex gap-4">
        <div class="avatar">
          <div class="size-12 rounded-md">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-7.png" alt="avatar" />
          </div>
        </div>
        <div>
          <p class="mb-0.5">Jordan Stevenson</p>
          <p class="text-sm text-base-content/50 font-normal">wramirez@outlook.com</p>
        </div>
      </div>
      <span class="icon-[tabler--chevron-left] accordion-item-active:-rotate-90 size-5 shrink-0 transition-transform duration-300 rtl:-rotate-180"></span>
    </button>
    <div id="delivery-arrow-right-collapse" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="delivery-arrow-right" role="region">
      <div class="px-5 pb-4">
        <p class="text-base-content/80 font-normal">
          Jordan Stevenson is a talented individual with a passion for technology and innovation. Jordan has made significant contributions to various projects and has a deep understanding of programming languages and frameworks.
        </p>
      </div>
    </div>
  </div>

  <div class="accordion-item" id="cancel-arrow-right">
    <button class="accordion-toggle inline-flex items-center justify-between text-start" aria-controls="cancel-arrow-right-collapse" aria-expanded="false">
      <div class="flex gap-4">
        <div class="avatar">
          <div class="size-12 rounded-md">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png" alt="avatar" />
          </div>
        </div>
        <div>
          <p class="mb-0.5">Nicholas Tanner</p>
          <p class="text-sm text-base-content/50 font-normal">snguyen@icloud.com</p>
        </div>
      </div>
      <span class="icon-[tabler--chevron-left] accordion-item-active:-rotate-90 size-5 shrink-0 transition-transform duration-300 rtl:-rotate-180"></span>
    </button>
    <div id="cancel-arrow-right-collapse" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="cancel-arrow-right" role="region">
      <div class="px-5 pb-4">
        <p class="text-base-content/80 font-normal">
          Nicholas Tanner is a highly skilled individual with a strong passion for technology and innovation. Nicholas has made significant contributions to numerous projects and possesses a deep understanding of various programming languages and frameworks.
        </p>
      </div>
    </div>
  </div>
</div>

{{< /code >}}

<!-- Using RTL variants -->

{{< headname level="3" >}} Using RTL variants {{< /headname >}}

To implement RTL variants in your custom components, prepend `rtl:` to the relevant classes. For example, use `me-2.5` for horizontal spacing in LTR mode, and `rtl:mr-2.5` for the equivalent in RTL mode:

```html
<div class="me-2.5 rtl:mr-2.5">
  <!-- ... -->
</div>
```

<br />

We recommend using logical properties for margins, paddings, borders, and rounded corners to keep your HTML markup clean and reduce the number of utility classes—beneficial when working with Tailwind CSS.

<!-- UI components -->

{{< headname level="3" >}} UI components {{< /headname >}}

All FlyonUI components come with built-in RTL support. By setting the `dir` attribute to `rtl` on the `<html>` element, all examples in the documentation will render correctly. Explore the full range of UI components and examples in our official documentation.
