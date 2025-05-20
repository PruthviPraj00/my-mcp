---
title: "Divider"
components: 6
description: "A divider is employed to separate content either vertically or horizontally."
bg_image: "svg/content/divider.svg"
menu:
  main:
    parent: "content"

previous: Blockquote
previousLink: blockquote/

next: Keyboard
nextLink: content/keyboard/
---

<!-- Class table -->

{{< class-table >}}
divider | component | Base class for divider components.
divider-dashed | style | Renders the divider line with a dashed pattern.
divider-dotted | style | Renders the divider line with a dotted pattern.
divider-neutral | color | Renders the divider line with a 'neutral' color.
divider-primary | color | Renders the divider line with a 'primary' color.
divider-secondary | color | Renders the divider line with a 'secondary' color.
divider-accent | color | Renders the divider line with an 'accent' color.
divider-success | color | Renders the divider line with a 'success' color.
divider-warning | color | Renders the divider line with a 'warning' color.
divider-info | color | Renders the divider line with an 'info' color.
divider-error | color | Renders the divider line with an 'error' color.
divider-end | placement | Aligns the divider text to the end.
divider-start | placement | Aligns the divider text to the start.
divider-vertical | direction | Positions elements vertically (default).
divider-horizontal | direction | Positions elements horizontally.
{{< /class-table >}}

<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!-- Vertical divider -->

{{< headname level="3" >}} Vertical divider {{< /headname >}}

Utilize the component class `divider` to create vertical content divisions. Apply the modifier class `divider-{semantic-color}` to specify different colors for the dividers.

{{< code addClass="gap-8">}}

<div class="divider"></div>
<div class="divider divider-neutral"></div>
<div class="divider divider-primary"></div>
<div class="divider divider-secondary"></div>
<div class="divider divider-accent"></div>
<div class="divider divider-info"></div>
<div class="divider divider-success"></div>
<div class="divider divider-warning"></div>
<div class="divider divider-error"></div>
{{< /code >}}

<!-- Horizontal divider -->

{{< headname level="3" >}} Horizontal divider {{< /headname >}}

Use the responsive class `divider-horizontal` with the component class `divider` to create horizontal content divisions.

{{< code >}}

<div class="flex h-60 flex-wrap gap-8">
  <div class="divider divider-horizontal"></div>
  <div class="divider divider-horizontal divider-neutral"></div>
  <div class="divider divider-horizontal divider-primary"></div>
  <div class="divider divider-horizontal divider-secondary"></div>
  <div class="divider divider-horizontal divider-accent"></div>
  <div class="divider divider-horizontal divider-info"></div>
  <div class="divider divider-horizontal divider-success"></div>
  <div class="divider divider-horizontal divider-warning"></div>
  <div class="divider divider-horizontal divider-error"></div>
</div>
{{< /code >}}

<!-- With content (horizontal) -->

{{< headname level="3" >}} With content (horizontal) {{< /headname >}}

Add text or icon within the divider markup to show it within the horizontal divider line.

{{< code >}}

<div class="flex h-60 flex-wrap gap-5">
  <div class="divider divider-horizontal">Text</div>
  <div class="divider divider-horizontal"><span class="flex items-center justify-center"><span class="icon-[tabler--sun] size-5"></span></span> </div>
</div>
{{< /code >}}

<!-- With content (vertical) -->

{{< headname level="3" >}} With content (vertical) {{< /headname >}}

Insert icons or text into the divider markup following the examples below to display them within the divider line.

{{< code addClass="gap-5">}}

<div class="divider">Text</div>
<div class="divider"><span class="flex items-center justify-center"><span class="icon-[tabler--crown] size-5"></span></span></div>
{{< /code >}}

<!-------------------- Styles -------------------->

{{< headname level="2" >}} Styles {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

The following example represents the default style for the divider line.

{{< code addClass="gap-0">}}

<div class="divider">Default</div>
{{< /code >}}

<!-- Dotted -->

{{< headname level="3" >}} Dotted {{< /headname >}}

Apply the modifier class `divider-dotted` to display the divider line in a dotted pattern.

{{< code addClass="gap-0">}}

<div class="divider divider-dotted">Dotted</div>
{{< /code >}}

<!-- Dashed -->

{{< headname level="3" >}} Dashed {{< /headname >}}

Apply the modifier class `divider-dashed` to display the divider line in a dashed pattern.

{{< code addClass="gap-0">}}

<div class="divider divider-dashed">Dashed</div>
{{< /code >}}

<!-- Custom thickness -->

{{< headname level="3" >}} Custom thickness {{< /headname >}}

Utilize the TailwindCSS <a href="https://tailwindcss.com/docs/hover-focus-and-other-states#before-and-after" target="_blank" class="link link-primary">state</a> classes `after:` and `before:` along with the border classes `border-e-*` for vertical dividers and `border-t-*` for horizontal dividers to customize their thickness.

{{< code addClass="gap-5">}}

<div class="divider after:border-t-2 before:border-t-2">Default</div>
<div class="divider divider-dotted after:border-t-4 before:border-t-4">Dotted</div>
<div class="divider divider-dashed after:border-t-8 before:border-t-8">Dashed</div>
{{< /code >}}

<!-- Content positions -->

{{< headname level="2" >}} Content positions {{< /headname >}}

<!-- Vertical divider content -->

{{< headname level="3" >}} Vertical divider content {{< /headname >}}

Use the responsive classes `divider-start` and `divider-end` to position content at the start and end positions, respectively. By default, the content is centered.

{{< code addClass="gap-5">}}

<div class="divider divider-start">Start</div>
<div class="divider">Center</div>
<div class="divider divider-end">End</div>
{{< /code >}}

<!-- Horizontal divider content -->

{{< headname level="3" >}} Horizontal divider content {{< /headname >}}

Use the responsive classes `divider-start` and `divider-end` to position content at the start and end positions in horizontal divider, respectively. By default, the content is centered.

{{< code >}}

<div class="flex h-60 gap-5">
  <div class="divider divider-start divider-horizontal">Start</div>
  <div class="divider divider-horizontal">Center</div>
  <div class="divider divider-end divider-horizontal">End</div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Responsive -->

{{< headname level="3" >}} Responsive {{< /headname >}}

The responsive dividers adapt according to breakpoints.

<!-- Horizontally -->

{{< headname level="4" >}} Horizontally {{< /headname >}}

Use TailwindCSS classes for <a href="https://tailwindcss.com/docs/responsive-design#targeting-a-breakpoint-range" target="_blank" class="link link-primary">responsive design</a>, such as `sm:`, `md:`, `lg:`, `xl:`, and `2xl:`, along with the responsive class `divider-horizontal`, to switch the divider alignment to horizontal at specific breakpoints.

{{< code >}}

<div class="flex w-full flex-col gap-5 lg:flex-row">
  <div class="shadow-base-300/20 bg-base-200 grid h-32 grow place-items-center shadow-sm"></div>
  <div class="divider lg:divider-horizontal">OR</div>
  <div class="shadow-base-300/20 bg-base-200 grid h-32 grow place-items-center shadow-sm"></div>
</div>
{{< /code >}}

<!-- Vertically -->

{{< headname level="4" >}} Vertically {{< /headname >}}

Utilize responsive breakpoint classes alongside the responsive class `divider-vertical` to adjust the divider alignment to vertical at specific breakpoints.

{{< code >}}

<div class="flex w-full gap-5 lg:flex-col">
  <div class="shadow-base-300/20 bg-base-200 grid h-32 grow place-items-center shadow-sm"></div>
  <div class="divider divider-horizontal lg:divider-vertical">OR</div>
  <div class="shadow-base-300/20 bg-base-200 grid h-32 grow place-items-center shadow-sm"></div>
</div>
{{< /code >}}

<!-- Buttons with divider -->

{{< headname level="3" >}} Buttons with divider {{< /headname >}}

Use the example below to implement buttons with a responsive horizontal divider.

{{< code >}}

<div class="flex w-fit flex-col gap-5 lg:flex-row">
  <div class="grid grow place-items-center">
    <button class="btn btn-soft [--btn-color:#1877F2] [--btn-fg:#1877F2]">
      <span class="icon-[tabler--brand-facebook]"></span>
      Sign in with Facebook
    </button>
  </div>
  <div class="divider lg:divider-horizontal"></div>
  <div class="grid grow place-items-center">
    <button class="btn btn-soft [--btn-color:#1da1f2] [--btn-fg:#1da1f2]">
      <span class="icon-[tabler--brand-x]"></span>
      Sign in with Twitter
    </button>
  </div>
</div>
{{< /code >}}

<!-- Buttons with vertical divider -->

{{< headname level="3" >}} Buttons with vertical divider {{< /headname >}}

Use the example below to implement buttons with a vertical divider.

{{< code >}}

<div class="flex w-fit flex-col gap-5">
  <div class="grid grow place-items-center">
    <button class="btn btn-soft [--btn-color:#1877F2] [--btn-fg:#1877F2]">
      <span class="icon-[tabler--brand-facebook]"></span>
      Sign in with Facebook
    </button>
  </div>
  <div class="divider divider-vertical"></div>
  <div class="grid grow place-items-center">
    <button class="btn btn-soft w-full [--btn-color:#1da1f2] [--btn-fg:#1da1f2]">
      <span class="icon-[tabler--brand-x]"></span>
      Sign in with Twitter
    </button>
  </div>
</div>
{{< /code >}}
