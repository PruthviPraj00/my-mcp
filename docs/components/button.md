---
title: "Button"
description: "Browse and customize beautiful Tailwind CSS buttons in various styles and states, from active to disabled, allowing users to take actions or make choices."
bg_image: "svg/components/button.svg"
components: 20
isLanding: true
menu:
  main:
    parent: "components"

previous: Badge
previousLink: components/badge/

next: Card
nextLink: components/card/

pageJS:
  - "/js/helper/wave-helper.js"

vendorJS:
  - "vendor/node-waves/waves.js"

vendorCSS:
  - "vendor/node-waves/waves.css"
---

<!-- Class table -->

{{< class-table >}}
btn| component | Base class for the button component.
btn-soft | style | Soft colored button.
btn-outline | style | Transparent button with colored border.
btn-gradient | style | Gradient button
btn-primary | color | Button with 'primary' color.
btn-secondary | color | Button with 'secondary' color.
btn-accent | color | Button with 'accent' color.
btn-info | color | Button with 'info' color.
btn-success | color | Button with 'success' color.
btn-warning | color | Button with 'warning' color.
btn-error | color | Button with 'error' color.
btn-active | state | Force button to show active state.
btn-disabled | state | Force button to show disabled state.
btn-xs | size | Button with extra small size.
btn-sm | size | Button with small size.
btn-md | size | Button with medium(Default) size.
btn-lg | size | Button with large size.
btn-xl | size | Button with extra large size.
glass | modifier | Button with a glass effect.
btn-wide | modifier | Wide button (max-w-64).
btn-block | modifier | Full width button.
btn-circle | modifier | Circle button with a 1:1 ratio.
btn-square | modifier | Square button with a 1:1 ratio.
{{< /class-table >}}

<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!-- Solid buttons -->

{{< headname level="3" >}} Solid buttons {{< /headname >}}

The standard format for button is component class `btn`, accompanied by modifier class `btn-{semantic-color}`.

{{< code >}}
<button class="btn">Default</button>
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-accent">Accent</button>
<button class="btn btn-info">Info</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-warning">Warning</button>
<button class="btn btn-error">Error</button>
{{< /code >}}

<!-- Soft buttons -->

{{< headname level="3" >}} Soft buttons {{< /headname >}}

Add modifier class `btn-soft` for soft colored buttons.

{{< code >}}
<button class="btn btn-soft">Default</button>
<button class="btn btn-soft btn-primary">Primary</button>
<button class="btn btn-soft btn-secondary">Secondary</button>
<button class="btn btn-soft btn-accent">Accent</button>
<button class="btn btn-soft btn-info">Info</button>
<button class="btn btn-soft btn-success">Success</button>
<button class="btn btn-soft btn-warning">Warning</button>
<button class="btn btn-soft btn-error">Error</button>
{{< /code >}}

<!-- Outline buttons -->

{{< headname level="3" >}} Outline buttons {{< /headname >}}

Add modifier class `btn-outline` for outline colored buttons.

{{< code >}}
<button class="btn btn-outline">Default</button>
<button class="btn btn-outline btn-primary">Primary</button>
<button class="btn btn-outline btn-secondary">Secondary</button>
<button class="btn btn-outline btn-accent">Accent</button>
<button class="btn btn-outline btn-info">Info</button>
<button class="btn btn-outline btn-success">Success</button>
<button class="btn btn-outline btn-warning">Warning</button>
<button class="btn btn-outline btn-error">Error</button>
{{< /code >}}


<!-- Text buttons -->

{{< headname level="3" >}} Text buttons {{< /headname >}}

Add modifier class `btn-text` for text colored buttons.

{{< code >}}
<button class="btn btn-text">Default</button>
<button class="btn btn-text btn-primary">Primary</button>
<button class="btn btn-text btn-secondary">Secondary</button>
<button class="btn btn-text btn-accent">Accent</button>
<button class="btn btn-text btn-info">Info</button>
<button class="btn btn-text btn-success">Success</button>
<button class="btn btn-text btn-warning">Warning</button>
<button class="btn btn-text btn-error">Error</button>
{{< /code >}}

<!-- Gradient buttons -->

{{< headname level="3" >}} Gradient buttons {{< /headname >}}

Add modifier class `btn-gradient` for gradient colored buttons.

{{< code >}}
<button class="btn btn-gradient">Default</button>
<button class="btn btn-gradient btn-primary">Primary</button>
<button class="btn btn-gradient btn-secondary">Secondary</button>
<button class="btn btn-gradient btn-accent">Accent</button>
<button class="btn btn-gradient btn-info">Info</button>
<button class="btn btn-gradient btn-success">Success</button>
<button class="btn btn-gradient btn-warning">Warning</button>
<button class="btn btn-gradient btn-error">Error</button>
{{< /code >}}

<!-- Wave effect button -->

{{< headname level="3" >}} Wave effect button {{< /headname >}}

Add modifier class `waves` for wave effect in buttons.

{{< callout "info" >}}
Refer {{< link link="third-party-plugins/wave-effect/" addClass="link link-primary" >}}Wave Effect{{< /link >}} plugin for more details.

{{< /callout >}}

{{< code >}}
<button class="btn btn-primary waves waves-light">Primary</button>
<button class="btn btn-soft btn-primary waves waves-primary">Primary</button>
<button class="btn btn-outline btn-primary waves waves-primary">Primary</button>
<button class="btn btn-text btn-primary waves waves-primary">Primary</button>
<button class="btn btn-gradient btn-primary waves waves-light">Primary</button>
{{< /code >}}

<!-------------------- Shapes -------------------->

{{< headname level="2" >}} Shapes {{< /headname >}}

<!-- Pilled buttons -->

{{< headname level="3" >}} Pilled buttons {{< /headname >}}

Use the `rounded-full` utility class to make buttons circular. The default shape of the button but can be altered by using TailwindCSS <a href="https://tailwindcss.com/docs/border-radius" target="_blank" class="link link-primary">Border Radius</a> utility classes.

{{< code >}}
<button class="btn btn-primary rounded-full">Primary</button>
<button class="btn btn-soft btn-primary rounded-full">Primary</button>
<button class="btn btn-outline btn-primary rounded-full">Primary</button>
<button class="btn btn-gradient btn-primary rounded-full">Primary</button>
{{< /code >}}

<!-- Rounded buttons -->

{{< headname level="3" >}} Rounded buttons {{< /headname >}}

This is the default shape of button.

{{< code >}}
<button class="btn btn-primary">Primary</button>
<button class="btn btn-soft btn-primary">Primary</button>
<button class="btn btn-outline btn-primary">Primary</button>
<button class="btn btn-gradient btn-primary">Primary</button>
{{< /code >}}

<!-------------------- State -------------------->

{{< headname level="2" >}} States {{< /headname >}}

<!-- States variants -->

{{< headname level="3" >}} States variants {{< /headname >}}

Use the `btn-active` class to force the button to show the active state and the `btn-disabled` class to force the button to show the disabled state.

Use state classes with any button variants.

{{< code >}}
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary btn-active">Active</button>
<button class="btn btn-primary btn-disabled">Disabled</button>
{{< /code >}}

<!-------------------- Size -------------------->

{{< headname level="2" >}} Size {{< /headname >}}

<!-- Size variants -->

{{< headname level="3" >}} Size variants {{< /headname >}}

Add responsive class `btn-{size}` where `{size} = xs|sm|md|lg|xl` for button of different sizes.

{{< callout "info" >}}
For medium size button, use component class `btn`.
{{< /callout >}}

{{< code addClass="items-center">}}
<button class="btn btn-primary btn-xs">Tiny</button>
<button class="btn btn-primary btn-sm">Small</button>
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary btn-xl">Extra Large</button>
{{< /code >}}

<!-- Wide button -->

{{< headname level="3" >}} Wide button {{< /headname >}}

To create a wide button, add the `btn-wide` class which provides additional horizontal padding.

{{< code >}}
<button class="btn btn-primary btn-wide">Wide</button>
{{< /code >}}

<!-- Block button -->

{{< headname level="3" >}} Block button {{< /headname >}}

To create a wide button, add the `btn-block` class which occupies the full width of the parent container.

{{< code >}}
<button class="btn btn-primary btn-block">Block</button>
{{< /code >}}

<!-- Responsive button -->

{{< headname level="3" >}} Responsive button {{< /headname >}}

This button will have different sizes on different browser viewpoints.

{{< code >}}
<button class="btn btn-primary btn-sm md:btn-md lg:btn-lg">Responsive</button>
{{< /code >}}

<!-------------------- Icons -------------------->

{{< headname level="2" >}} Icon buttons {{< /headname >}}

<!-- Icon at start/end -->

{{< headname level="3" >}} Icon at start/end {{< /headname >}}

Use any icons at start/end the button.

{{< code >}}

<div class="flex w-full flex-wrap gap-2">
  <button class="btn btn-primary"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span> Primary </button>
  <button class="btn btn-soft btn-primary"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span> Primary </button>
  <button class="btn btn-outline btn-primary"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span> Primary </button>
  <button class="btn btn-gradient btn-primary"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span> Primary </button>
</div>

<div class="flex w-full flex-wrap gap-2">
  <button class="btn btn-primary"> Primary <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
  <button class="btn btn-soft btn-primary"> Primary <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
  <button class="btn btn-outline btn-primary"> Primary <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
  <button class="btn btn-gradient btn-primary"> Primary <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
</div>
{{< /code >}}

<!-- Icon only -->

{{< headname level="3" >}} Icon only {{< /headname >}}

Use `btn-square` or `btn-circle` to create circle/square button with a 1:1 ratio.

{{< code >}}
<button class="btn btn-square btn-primary" aria-label="Icon Button"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
<button class="btn btn-square btn-soft btn-primary" aria-label="Soft Icon Button"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
<button class="btn btn-square btn-outline btn-primary" aria-label="Outline Icon Button"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
<button class="btn btn-square btn-gradient btn-primary" aria-label="Gradient Icon Button"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
<button class="btn btn-circle btn-primary" aria-label="Circle Icon Button"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
<button class="btn btn-circle btn-soft btn-primary" aria-label="Circle Soft Icon Button"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
<button class="btn btn-circle btn-outline btn-primary" aria-label="Circle Outline Icon Button"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
<button class="btn btn-circle btn-gradient btn-primary" aria-label="Circle Gradient Icon Button"> <span class="icon-[tabler--star] size-4.5 shrink-0"></span></button>
{{< /code >}}

<!-- Input tags -->

{{< headname level="2" >}} Input tags {{< /headname >}}

<!-- Buttons with input tags -->

{{< headname level="3" >}} Buttons with input tags {{< /headname >}}

You can use `btn` class on `<button>`, `<input>`, `<a>`, etc...

{{< code >}}
<a role="button" class="btn">Link</a>
<button type="submit" class="btn">Button</button>
<input type="button" value="Input" class="btn" />
<input type="submit" value="Submit" class="btn" />
<input type="radio" aria-label="Radio" class="btn" />
<input type="checkbox" aria-label="Checkbox" class="btn" />
<input type="reset" value="Reset" class="btn" />
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Social buttons -->

{{< headname level="3" >}} Social buttons {{< /headname >}}

Use the following sample code to build custom Social, Payment, and other types of buttons. This example also demonstrates how to create a custom button using two variables: `--btn-color` and `--btn-fg`.

{{< code >}}

<!-- Solid -->
<div class="flex w-full flex-wrap gap-2">
  <button class="btn [--btn-color:#1877F2] text-white" >
    <span class="icon-[tabler--brand-facebook] size-4.5 shrink-0"></span> Facebook
  </button>
  <button class="btn [--btn-color:#000] text-white" >
    <span class="icon-[tabler--brand-x] size-4.5 shrink-0"></span> Twitter
  </button>
  <button class="btn [--btn-color:#0a66c2] text-white" >
    <span class="icon-[tabler--brand-linkedin] size-4.5 shrink-0"></span> LinkedIn
  </button>
  <button class="btn [--btn-color:#2b3137] text-white" >
    <span class="icon-[tabler--brand-github] size-4.5 shrink-0"></span> Github
  </button>
</div>

<!-- Soft -->
<div class="flex w-full flex-wrap gap-2">
  <button class="btn btn-soft [--btn-color:#1877F2]">
    <span class="icon-[tabler--brand-facebook] size-4.5 shrink-0"></span> Facebook
  </button>
  <button class="btn btn-soft [--btn-color:#000]">
    <span class="icon-[tabler--brand-x] size-4.5 shrink-0"></span> Twitter
  </button>
  <button class="btn btn-soft [--btn-color:#0a66c2]">
    <span class="icon-[tabler--brand-linkedin] size-4.5 shrink-0"></span> LinkedIn
  </button>
  <button class="btn btn-soft [--btn-color:#2b3137]">
    <span class="icon-[tabler--brand-github] size-4.5 shrink-0"></span> Github
  </button>
</div>

<!-- Outline -->
<div class="flex w-full flex-wrap gap-2">
  <button class="btn btn-outline [--btn-color:#1877F2]">
    <span class="icon-[tabler--brand-facebook] size-4.5 shrink-0"></span> Facebook
  </button>
  <button class="btn btn-outline [--btn-color:#000]">
    <span class="icon-[tabler--brand-x] size-4.5 shrink-0"></span> Twitter
  </button>
  <button class="btn btn-outline [--btn-color:#0a66c2]">
    <span class="icon-[tabler--brand-linkedin] size-4.5 shrink-0"></span> LinkedIn
  </button>
  <button class="btn btn-outline [--btn-color:#2b3137]">
    <span class="icon-[tabler--brand-github] size-4.5 shrink-0"></span> Github
  </button>
</div>

<!-- Text -->
<div class="flex w-full flex-wrap gap-2">
  <button class="btn btn-text [--btn-color:#1877F2]">
    <span class="icon-[tabler--brand-facebook] size-4.5 shrink-0"></span> Facebook
  </button>
  <button class="btn btn-text [--btn-color:#000]">
    <span class="icon-[tabler--brand-x] size-4.5 shrink-0"></span> Twitter
  </button>
  <button class="btn btn-text [--btn-color:#0a66c2]">
    <span class="icon-[tabler--brand-linkedin] size-4.5 shrink-0"></span> LinkedIn
  </button>
  <button class="btn btn-text [--btn-color:#2b3137]">
    <span class="icon-[tabler--brand-github] size-4.5 shrink-0"></span> Github
  </button>
</div>

{{< /code >}}

Use `btn-square` or `btn-circle` to create circle/square buttons.

{{< code addClass="!inline-flex" >}}

<!-- Solid -->
<div class="flex w-full flex-wrap gap-2">
  <button class="btn btn-square  [--btn-color:#1877F2] text-white" aria-label="Facebook Icon Button" >
    <span class="icon-[tabler--brand-facebook] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-square  [--btn-color:#000] text-white" aria-label="X Icon Button" >
    <span class="icon-[tabler--brand-x] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-circle  [--btn-color:#0a66c2] text-white" aria-label="Linkedin Icon Button" >
    <span class="icon-[tabler--brand-linkedin] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-circle  [--btn-color:#2b3137] text-white" aria-label="Github Icon Button" >
    <span class="icon-[tabler--brand-github] size-4.5 shrink-0"></span>
  </button>
</div>

<!-- Soft -->
<div class="flex w-full flex-wrap gap-2">
  <button class="btn btn-square btn-soft [--btn-color:#1877F2]" aria-label="Facebook Soft Icon Button">
    <span class="icon-[tabler--brand-facebook] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-square btn-soft [--btn-color:#000]" aria-label="X Soft Icon Button">
    <span class="icon-[tabler--brand-x] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-circle btn-soft [--btn-color:#0a66c2]" aria-label="Linkedin Soft Icon Button">
    <span class="icon-[tabler--brand-linkedin] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-circle btn-soft [--btn-color:#2b3137]" aria-label="Github Soft Icon Button">
    <span class="icon-[tabler--brand-github] size-4.5 shrink-0"></span>
  </button>
</div>

<!-- Outline -->
<div class="flex w-full flex-wrap gap-2">
  <button class="btn btn-square btn-outline [--btn-color:#1877F2]" aria-label="Facebook Outline Icon Button">
    <span class="icon-[tabler--brand-facebook] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-square btn-outline [--btn-color:#000]" aria-label="X Outline Icon Button">
    <span class="icon-[tabler--brand-x] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-circle btn-outline [--btn-color:#0a66c2]" aria-label="Linkedin Outline Icon Button">
    <span class="icon-[tabler--brand-linkedin] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-circle btn-outline [--btn-color:#2b3137]" aria-label="Github Outline Icon Button">
    <span class="icon-[tabler--brand-github] size-4.5 shrink-0"></span>
  </button>
</div>

<!-- Text -->
<div class="flex w-full flex-wrap gap-2">
  <button class="btn btn-square btn-text [--btn-color:#1877F2]" aria-label="Facebook Outline Icon Button">
    <span class="icon-[tabler--brand-facebook] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-square btn-text [--btn-color:#1da1f2]" aria-label="X Outline Icon Button">
    <span class="icon-[tabler--brand-x] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-circle btn-text [--btn-color:#0a66c2]" aria-label="Linkedin Outline Icon Button">
    <span class="icon-[tabler--brand-linkedin] size-4.5 shrink-0"></span>
  </button>
  <button class="btn btn-circle btn-text [--btn-color:#2b3137]" aria-label="Github Outline Icon Button">
    <span class="icon-[tabler--brand-github] size-4.5 shrink-0"></span>
  </button>
</div>

{{< /code >}}

<!-- Loading buttons -->

{{< headname level="3" >}} Loading buttons {{< /headname >}}

Use loading component to add a loader to the button.

{{< callout "info" >}}
Refer {{< link link="components/loading/" addClass="link link-primary" >}}Loading Element{{< /link >}} plugin for more details.
{{< /callout >}}

{{< code >}}
<button class="btn btn-square btn-primary" aria-label="Loading Button">
<span class="loading loading-spinner"></span>
</button>

<button class="btn btn-primary">
  <span class="loading loading-spinner"></span>
  loading
</button>
{{< /code >}}

<!-- Glass button -->

{{< headname level="3" >}} Glass button {{< /headname >}}

Use class `glass` to create a button with glass effect.

{{< code addClass="bg-[url('https://cdn.flyonui.com/fy-assets/components/card/image-1.png')] bg-cover" >}}
<button class="btn glass">Glass button</button>
{{< /code >}}


<!-- Dashed buttons -->

{{< headname level="3" >}} Dashed buttons {{< /headname >}}

You can achieve this style by combining the `border-dashed` utility class with the `btn-outline` modifier class.

{{< code >}}
<button class="btn btn-outline border-dashed">Default</button>
<button class="btn btn-outline border-dashed btn-primary">Primary</button>
<button class="btn btn-outline border-dashed btn-secondary">Secondary</button>
<button class="btn btn-outline border-dashed btn-accent">Accent</button>
<button class="btn btn-outline border-dashed btn-info">Info</button>
<button class="btn btn-outline border-dashed btn-success">Success</button>
<button class="btn btn-outline border-dashed btn-warning">Warning</button>
<button class="btn btn-outline border-dashed btn-error">Error</button>
{{< /code >}}

<!-- Button group -->

{{< headname level="3" >}} Button group {{< /headname >}}

Group a series of buttons together on a single line or stack them in a vertical/horizontal column

{{< callout "info" false >}}
Refer the {{< link link="forms/join/" addClass="link link-primary" >}}Join{{< /link >}} component documentation for creating a group of buttons.
{{< /callout >}}

{{< code >}}

<div class="join">
  <button class="btn btn-soft btn-primary join-item">Button</button>
  <button class="btn btn-soft btn-primary join-item">Button</button>
  <button class="btn btn-soft btn-primary join-item">Button</button>
</div>
{{< /code >}}
