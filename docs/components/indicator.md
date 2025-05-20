---
title: "Indicator"
components: 4
description: "Indicators precisely position elements at the corners of other elements, improving visual alignment in user interfaces."
bg_image: "svg/components/indicator.svg"
menu:
  main:
    parent: "components"

previous: Diff
previousLink: components/diff/

next: List group
nextLink: components/list-group/
---

<!-- Class table -->

{{< class-table >}}
indicator | component | Container element.
indicator-item| part | Will be placed on the corner of sibling.
indicator-start| placement | Align horizontally to the start.
indicator-center| placement | Align horizontally to the center.
indicator-end| placement | Align horizontally to the end (default).
indicator-top| placement | Align vertically to top (default).
indicator-middle| placement | Align vertically to middle.
indicator-bottom| placement | Align vertically to bottom.
{{< /class-table >}}

<!-------------------- Basic -------------------->

{{< headname level="2" >}} Basic {{< /headname >}}

<!-- Indicator -->

{{< headname level="3" >}} Indicator {{< /headname >}}

The `indicator` component acts as a container for indicators, with the `indicator-item` class offering default positioning. Tailwind utility classes enable control over size, background color, and roundness of the indicators.

{{< code >}}

<div class="indicator">
  <span class="indicator-item bg-primary size-3 rounded-full"></span>
  <div class="bg-primary/10 border-primary grid place-items-center rounded-md border p-3">
    <span class="icon-[tabler--bell] text-primary size-5"></span>
  </div>
</div>
{{< /code >}}

<!-- Status as indicator -->

{{< headname level="3" >}} Status as indicator {{< /headname >}}

Use `status` for status style indicator.

{{< code >}}

<div class="indicator">
  <span class="indicator-item status status-primary status-lg"></span>
  <div class="bg-primary/10 border-primary grid place-items-center rounded-md border p-3">
    <span class="icon-[tabler--bell] text-primary size-5"></span>
  </div>
</div>
{{< /code >}}

<!-- Badge as indicator -->

{{< headname level="3" >}} Badge as indicator {{< /headname >}}

Use `badge` for badge style indicator.

{{< code >}}

<div class="indicator">
  <span class="indicator-item badge badge-primary">+999</span>
  <div class="bg-primary/10 border-primary grid place-items-center rounded-md border p-3">
    <span class="icon-[tabler--bell] text-primary size-5"></span>
  </div>
</div>
{{< /code >}}

<!-- Pill badge as indicator -->

{{< headname level="3" >}} Pill badge as indicator {{< /headname >}}

Using the `rounded-full` class with `badge` creates a pill-shaped badge as an indicator.

{{< code >}}

<div class="indicator">
  <span class="indicator-item badge badge-primary rounded-full">+999</span>
  <div class="bg-primary/10 border-primary grid place-items-center rounded-md border p-3">
    <span class="icon-[tabler--bell] text-primary size-5"></span>
  </div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Indicator on avatar -->

{{< headname level="3" >}} Indicator on avatar {{< /headname >}}

Avatar with an indicator badge denoting the user's status.

{{< callout "info" >}}
Note! : This indicator are different form the {{< link link="components/avatar/#status" addClass="link link-primary" >}}Avatar Status{{< /link >}}.
{{< /callout >}}

{{< code >}}

<div class="avatar indicator me-8">
  <span class="indicator-item badge badge-primary">typing…</span>
  <div class="size-16 rounded-md">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png" alt="avatar" />
  </div>
</div>

<div class="avatar indicator">
  <span class="indicator-item bg-primary size-3 rounded-full"></span>
  <div class="size-16 rounded-md">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png" alt="avatar" />
  </div>
</div>

<div class="avatar indicator">
  <span class="indicator-item status status-primary status-lg"></span>
  <div class="size-16 rounded-md">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png" alt="avatar" />
  </div>
</div>
{{< /code >}}

<!-- Indicator on input -->

{{< headname level="3" >}} Indicator on input {{< /headname >}}

Input field with a prominent indicator badge denoting a required entry.

{{< code >}}

<div class="indicator">
  <span class="indicator-item badge badge-primary">Required</span>
  <input type="text" placeholder="Your email address" class="input" />
</div>
{{< /code >}}

<!-- Button indicator -->

{{< headname level="3" >}} Button indicator {{< /headname >}}

Button indicator provides a visual cue for interacting with content or actions within a container.

{{< code >}}

<div class="indicator mt-4">
  <div class="indicator-item indicator-top">
    <button class="btn btn-error btn-circle btn-sm" aria-label="Close Button Indicator">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="card">
    <div class="card-body">
      <h2 class="card-title">Card Title</h2>
      <p>Rerum reiciendis beatae tenetur excepturi</p>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Animation -------------------->

{{< headname level="2" >}} Animation {{< /headname >}}

<!-- Ping animation -->

{{< headname level="3" >}} Ping animation {{< /headname >}}

Include the `animate-ping` utility to enable an element to scale and fade, resembling a radar ping or water ripple effect, which is beneficial for features like notification badges.

{{< code  >}}

<div class="indicator">
  <div class="indicator-item inline-grid *:[grid-area:1/1]">
    <div class="status status-error animate-ping"></div>
    <div class="status status-error"></div>
  </div>
  <button class="btn btn-secondary btn-outline btn-square" aria-label="Button Indicator"><span class="icon-[tabler--shopping-bag] size-5"></span></button>
</div>

<div class="indicator">
  <span class="indicator-item badge badge-error rounded-full">
    +99
    <span class="bg-error absolute size-full animate-ping rounded-full opacity-75"></span>
  </span>
  <button class="btn btn-secondary btn-outline">Notifications</button>
</div>
{{< /code >}}

<!-- Pulse animation -->

{{< headname level="3" >}} Pulse animation {{< /headname >}}

Apply the class `animation-pulse` to integrate this animated loading indicator for situations where content within a card is loading.

{{< code addClass="relative" >}}

<div class="bg-primary/10 flex size-32 items-center justify-center rounded-md border border-base-content/20">
  <div class="indicator">
    <span class="badge badge-primary animate-pulse rounded-full">loading...</span>
  </div>
</div>
{{< /code >}}

<!-------------------- Positions -------------------->

{{< headname level="2" >}} Positions {{< /headname >}}

<!-- Indicator -->

{{< headname level="3" >}} Indicator {{< /headname >}}

The Indicators can be positioned at.

{{< code >}}

<div class="indicator">
  <span class="indicator-item indicator-top indicator-start bg-primary size-3 rounded-full"></span>
  <span class="indicator-item indicator-top indicator-center bg-primary size-3 rounded-full"></span>
  <span class="indicator-item indicator-top indicator-end bg-primary size-3 rounded-full"></span>
  <span class="indicator-item indicator-middle indicator-start bg-primary size-3 rounded-full"></span>
  <span class="indicator-item indicator-middle indicator-center bg-primary size-3 rounded-full"></span>
  <span class="indicator-item indicator-middle indicator-end bg-primary size-3 rounded-full"></span>
  <span class="indicator-item indicator-bottom indicator-start bg-primary size-3 rounded-full"></span>
  <span class="indicator-item indicator-bottom indicator-center bg-primary size-3 rounded-full"></span>
  <span class="indicator-item indicator-bottom indicator-end bg-primary size-3 rounded-full"></span>
  <div class="bg-primary/10 border border-primary grid h-32 w-60 place-items-center rounded-md"></div>
</div>
{{< /code >}}

<!-- Badge indicator -->

{{< headname level="3" >}} Badge indicator {{< /headname >}}

The badge display can be positioned at.

{{< code >}}

<div class="indicator my-3 ms-14">
  <span class="indicator-item indicator-top indicator-start badge badge-primary max-sm:px-1">
    <span class="max-sm:hidden">top+start</span> <span class="sm:hidden">T-Start</span>
  </span>
  <span class="indicator-item indicator-top indicator-center badge badge-primary max-sm:px-1">
    <span class="max-sm:hidden">top+center</span> <span class="sm:hidden">T-center</span>
  </span>
  <span class="indicator-item indicator-top indicator-end badge badge-primary max-sm:px-1">
    <span class="max-sm:hidden">top+end</span> <span class="sm:hidden">T-end</span>
  </span>
  <span class="indicator-item indicator-middle indicator-start badge badge-primary max-sm:px-1">
    <span class="max-sm:hidden">middle+start</span> <span class="sm:hidden">M-start</span>
  </span>
  <span class="indicator-item indicator-middle indicator-center badge badge-primary max-sm:px-1">
    <span class="max-sm:hidden">middle+center</span> <span class="sm:hidden">M-center</span>
  </span>
  <span class="indicator-item indicator-middle indicator-end badge badge-primary max-sm:px-1">
    <span class="max-sm:hidden">middle+end</span> <span class="sm:hidden">M-end</span>
  </span>
  <span class="indicator-item indicator-bottom indicator-start badge badge-primary max-sm:px-1">
    <span class="max-sm:hidden">bottom+start</span> <span class="sm:hidden">B-Start</span>
  </span>
  <span class="indicator-item indicator-bottom indicator-center badge badge-primary max-sm:px-1">
    <span class="max-sm:hidden">bottom+center</span> <span class="sm:hidden">B-center</span>
  </span>
  <span class="indicator-item indicator-bottom indicator-end badge badge-primary max-sm:px-1">
    <span class="max-sm:hidden">bottom+end</span> <span class="sm:hidden">B-end</span>
  </span>
  <div class="bg-primary/10 border-primary grid h-32 w-60 place-items-center rounded-md border max-sm:w-40">content</div>
</div>

{{< /code >}}

<!-------------------- Responsive -------------------->

{{< headname level="2" >}} Responsive {{< /headname >}}

<!-- Position bassed on resolution -->

{{< headname level="3" >}} Position based on resolution {{< /headname >}}

Utilize responsive modifiers like `sm`, `md`, `lg` to adjust the indicator's position based on screen size.

{{< code >}}

<div class="indicator">
  <span class="indicator-item indicator-start sm:indicator-middle md:indicator-bottom lg:indicator-center xl:indicator-end status status-primary"></span>
  <div class="bg-primary/10 border-primary grid place-items-center rounded-md border p-3">
    <span class="icon-[tabler--bell] text-primary size-5"></span>
  </div>
</div>
{{< /code >}}
