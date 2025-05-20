---
title: "Join (Group Items)"
components: 16
description: "Join acts as a container for grouping items like buttons and inputs, applying border radius to the first and last items for horizontal or vertical lists."
bg_image: "svg/form-elements/join.svg"
menu:
  main:
    parent: "forms"

previous: Input
previousLink: forms/input/

next: Radio
nextLink: forms/radio/
---

<!-- Class table -->

{{< class-table >}}
join|component|Container for grouping multiple items
join-item|part|Item inside join. Can be a button, input, etc.
join-vertical|direction|Show items vertically  
join-horizontal|direction|Show items vertically  
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic join elements example.

{{< code >}}

<div class="join">
  <button class="btn btn-soft btn-primary join-item">Button</button>
  <button class="btn btn-soft btn-primary join-item">Button</button>
  <button class="btn btn-soft btn-primary join-item">Button</button>
</div>
{{< /code >}}

<!-- Icons -->

{{< headname level="3" >}} Icons {{< /headname >}}

Basic join elements example using icons.

{{< code >}}

<div class="join">
  <button class="btn btn-soft btn-primary btn-square join-item" aria-label="join"><span class="icon-[tabler--star]"></span></button>
  <button class="btn btn-soft btn-primary btn-square join-item" aria-label="join"><span class="icon-[tabler--star]"></span></button>
  <button class="btn btn-soft btn-primary btn-square join-item" aria-label="join"><span class="icon-[tabler--star]"></span></button>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Vertical -->

{{< headname level="3" >}} Vertical {{< /headname >}}

Group items vertically.

{{< code >}}

<div class="join join-vertical drop-shadow-sm">
  <button class="btn btn-soft btn-primary join-item">Button</button>
  <button class="btn btn-soft btn-primary join-item">Button</button>
  <button class="btn btn-soft btn-primary join-item">Button</button>
</div>
{{< /code >}}

<!-- Responsive -->

{{< headname level="3" >}} Responsive {{< /headname >}}

it's vertical on small screen and horizontal on large screen.

{{< code >}}

<div class="join max-sm:join-vertical">
  <button class="btn btn-soft btn-primary join-item">Button</button>
  <button class="btn btn-soft btn-primary join-item">Button</button>
  <button class="btn btn-soft btn-primary join-item">Button</button>
</div>
{{< /code >}}

<!-- Multiple elements -->

{{< headname level="3" >}} Multiple elements {{< /headname >}}

Basic join example illustrating the integration of multiple elements.

{{< code addClass="flex-col" >}}

<div class="join max-w-sm">
  <input class="input join-item" placeholder="Search" />
  <select class="select join-item" aria-label="select">
    <option disabled selected>Filter</option>
    <option>Sci-fi</option>
    <option>Drama</option>
    <option>Action</option>
  </select>
  <button class="btn btn-soft btn-primary join-item">Search</button>
</div>
{{< /code >}}

<!-- Pill shape -->

{{< headname level="3" >}} Pill shape {{< /headname >}}

The default shape of the join can be altered by using TailwindCSS <a href="https://tailwindcss.com/docs/border-radius" target="_blank" class="link link-primary">Border Radius</a> utility classes.

{{< code >}}

<div class="join">
  <input class="input join-item rounded-s-full" placeholder="Email" />
  <button class="btn btn-soft btn-primary join-item rounded-e-full">Subscribe</button>
</div>
{{< /code >}}

<!-- Dropdown with input -->

{{< headname level="3" >}} Dropdown with input {{< /headname >}}

You can also join `input` and `dropdown`.

{{< callout "info" >}}
To learn more about dropdowns, refer to the {{< link link="overlays/dropdown/" addClass="link link-primary" >}}Dropdown{{< /link >}} documentation.
{{< /callout >}}

{{< code >}}

<div class="join">
  <input class="input join-item shrink" placeholder="Email" />
  <div class="dropdown relative inline-flex max-sm:[--placement:bottom-end]">
    <button id="dropdown-input" type="button" class="dropdown-toggle btn btn-soft btn-primary join-item" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
      <span class="hidden sm:block">Dropdown</span>
      <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
    </button>
    <ul class="dropdown-menu dropdown-open:opacity-100 hidden" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-input">
      <li><a class="dropdown-item" href="#">Subscribe</a></li>
      <li><a class="dropdown-item" href="#">Verify</a></li>
    </ul>
  </div>
</div>
{{< /code >}}
