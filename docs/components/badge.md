---
title: "Badge"
components: 4
description: "Badges serve to communicate the status of particular data to the user."
bg_image: "svg/components/badge.svg"
menu:
  main:
    parent: "components"

previous: Avatar
previousLink: components/avatar/

next: Button
nextLink: components/button/
---

<!-- Class table -->

{{< class-table >}}
badge| component | Base class for the badge component.
badge-soft | style | Soft colored badge.
badge-outline | style | Transparent badge with colored border.
badge-primary | color | Badge with 'primary' color.
badge-secondary | color | Badge with 'secondary' color.
badge-accent | color | Badge with 'accent' color.
badge-info | color | Badge with 'info' color.
badge-success | color | Badge with 'success' color.
badge-warning | color | Badge with 'warning' color.
badge-error | color | Badge with 'error' color.
badge-xs | size | Badge with extra small size.
badge-sm | size | Badge with small size.
badge-md | size | Badge with medium(default) size.
badge-lg | size | Badge with large size.
badge-xl | size | Badge with extra-large size.
{{< /class-table >}}

<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!-- Solid badges -->

{{< headname level="3" >}} Solid badges {{< /headname >}}

The standard format for badge is component class `badge`, accompanied by modifier class `badge-{semantic-color}`.

{{< code >}}
<span class="badge">Default</span>
<span class="badge badge-primary">Primary</span>
<span class="badge badge-secondary">Secondary</span>
<span class="badge badge-accent">Accent</span>
<span class="badge badge-info">Info</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-warning">Warning</span>
<span class="badge badge-error">Error</span>
{{< /code >}}

<!-- Soft badges -->

{{< headname level="3" >}} Soft badges {{< /headname >}}

Add modifier class `badge-soft` for soft colored badges.

{{< code >}}
<span class="badge badge-soft">Default</span>
<span class="badge badge-soft badge-primary">Primary</span>
<span class="badge badge-soft badge-secondary">Secondary</span>
<span class="badge badge-soft badge-accent">Accent</span>
<span class="badge badge-soft badge-info">Info</span>
<span class="badge badge-soft badge-success">Success</span>
<span class="badge badge-soft badge-warning">Warning</span>
<span class="badge badge-soft badge-error">Error</span>
{{< /code >}}

<!-- Outline badges -->

{{< headname level="3" >}} Outline badges {{< /headname >}}

Add modifier class `badge-outline` for outline badges.

{{< code >}}
<span class="badge badge-outline">Default</span>
<span class="badge badge-outline badge-primary">Primary</span>
<span class="badge badge-outline badge-secondary">Secondary</span>
<span class="badge badge-outline badge-accent">Accent</span>
<span class="badge badge-outline badge-info">Info</span>
<span class="badge badge-outline badge-success">Success</span>
<span class="badge badge-outline badge-warning">Warning</span>
<span class="badge badge-outline badge-error">Error</span>
{{< /code >}}

<!-------------------- Shapes -------------------->

{{< headname level="2" >}} Shapes {{< /headname >}}

<!-- Pill badges -->

{{< headname level="3" >}} Pill badges {{< /headname >}}

Use the `rounded-full` utility class to make badges pilled. The default shape of the badges but can be altered by using
TailwindCSS <a href="https://tailwindcss.com/docs/border-radius" target="_blank" class="link link-primary">Border Radius</a> utility classes.

{{< code >}}
<span class="badge badge-primary rounded-full">Primary</span>
<span class="badge badge-soft badge-primary rounded-full">Primary</span>
<span class="badge badge-outline badge-primary rounded-full">Primary</span>
{{< /code >}}

<!-- Rounded badges -->

{{< headname level="3" >}} Rounded badges {{< /headname >}}

This is the Default shape of the badge.

{{< code >}}
<span class="badge badge-primary">Primary</span>
<span class="badge badge-soft badge-primary">Primary</span>
<span class="badge badge-outline badge-primary">Primary</span>
{{< /code >}}

<!-------------------- Sizes -------------------->

{{< headname level="2" >}} Sizes {{< /headname >}}

<!-- Size variants -->

{{< headname level="3" >}} Size variants {{< /headname >}}

Add responsive class `badge-{size}` where `{size} = xs|sm|md|lg|xl` for badges of different sizes.

{{< code addClass="items-center">}}
<span class="badge badge-primary badge-xs">1</span>
<span class="badge badge-primary badge-sm">2</span>
<span class="badge badge-primary">3</span>
<span class="badge badge-primary badge-lg">4</span>
<span class="badge badge-primary badge-xl">5</span>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Badge links -->

{{< headname level="3" >}} Badge links {{< /headname >}}

Use badges in anchor tags for clickable badge links.

{{< code >}}
<a href="#"><span class="badge badge-primary">Primary</span></a>
<a href="#"><span class="badge badge-secondary">Secondary</span></a>
<a href="#"><span class="badge badge-success">Success</span></a>
<a href="#"><span class="badge badge-error">Error</span></a>
<a href="#"><span class="badge badge-warning">Warning</span></a>
<a href="#"><span class="badge badge-info">Info</span></a>
{{< /code >}}

<!-- Dot style badges -->

{{< headname level="3" >}} Dot style badges {{< /headname >}}

Use badge with utility classes `height(h)`, `width(w)` or `size` & `p-0` for dot style badges.

{{< code >}}

<div class="flex items-center justify-center gap-1.5 text-base">
  <span class="badge size-2 p-0"></span>
  Default
</div>
<div class="flex items-center justify-center gap-1.5 text-base">
  <span class="badge badge-primary size-2 p-0"></span>
  Primary
</div>
<div class="flex items-center justify-center gap-1.5 text-base">
  <span class="badge badge-secondary size-2 p-0"></span>
  Secondary
</div>
<div class="flex items-center justify-center gap-1.5 text-base">
  <span class="badge badge-success size-2 p-0"></span>
  Success
</div>
<div class="flex items-center justify-center gap-1.5 text-base">
  <span class="badge badge-error size-2 p-0"></span>
  Error
</div>
<div class="flex items-center justify-center gap-1.5 text-base">
  <span class="badge badge-warning size-2 p-0"></span>
  Warning
</div>
<div class="flex items-center justify-center gap-1.5 text-base">
  <span class="badge badge-info size-2 p-0"></span>
  Info
</div>
{{< /code >}}

<!-- Dashed badges -->

{{< headname level="3" >}} Dashed badges {{< /headname >}}

You can achieve this style by combining the `border-dashed` utility class with the `badge-outline` modifier class.

{{< code >}}
<span class="badge badge-outline border-dashed">Default</span>
<span class="badge badge-outline border-dashed badge-primary">Primary</span>
<span class="badge badge-outline border-dashed badge-secondary">Secondary</span>
<span class="badge badge-outline border-dashed badge-accent">Accent</span>
<span class="badge badge-outline border-dashed badge-info">Info</span>
<span class="badge badge-outline border-dashed badge-success">Success</span>
<span class="badge badge-outline border-dashed badge-warning">Warning</span>
<span class="badge badge-outline border-dashed badge-error">Error</span>
{{< /code >}}


<!-- Badge with icons -->

{{< headname level="3" >}} Badge with icons {{< /headname >}}

Use `svg` or `icons` inside badges for icon badges.

<!-- Icon badges (rounded) -->

{{< headname level="4" >}} Icon badges (rounded) {{< /headname >}}

Add utility classes `size` & `p-0` for square icon badges.

{{< code >}}
<span class="badge size-6 p-0"> <span class="icon-[tabler--user]"></span></span>
<span class="badge badge-primary size-6 p-0"> <span class="icon-[tabler--star]"></span></span>
<span class="badge badge-secondary size-6 p-0"> <span class="icon-[tabler--sun]"></span></span>
<span class="badge badge-accent size-6 p-0"> <span class="icon-[tabler--moon]"></span></span>
<span class="badge badge-info size-6 p-0"> <span class="icon-[tabler--folder]"></span></span>
<span class="badge badge-success size-6 p-0"> <span class="icon-[tabler--check]"></span></span>
<span class="badge badge-warning size-6 p-0"> <span class="icon-[tabler--cloud]"></span></span>
<span class="badge badge-error size-6 p-0"> <span class="icon-[tabler--clock]"></span></span>
{{< /code >}}

<!-- Icon badges (circular) -->

{{< headname level="4" >}} Icon badges (circular) {{< /headname >}}

Add utility classes `rounded-full`, `size` & `p-0` for circular Icon badges.

{{< code >}}
<span class="badge size-6 rounded-full p-0"> <span class="icon-[tabler--user]"></span></span>
<span class="badge badge-primary size-6 rounded-full p-0"> <span class="icon-[tabler--star]"></span></span>
<span class="badge badge-secondary size-6 rounded-full p-0"> <span class="icon-[tabler--sun]"></span></span>
<span class="badge badge-accent size-6 rounded-full p-0"> <span class="icon-[tabler--moon]"></span></span>
<span class="badge badge-info size-6 rounded-full p-0"> <span class="icon-[tabler--folder]"></span></span>
<span class="badge badge-success size-6 rounded-full p-0"> <span class="icon-[tabler--check]"></span></span>
<span class="badge badge-warning size-6 rounded-full p-0"> <span class="icon-[tabler--cloud]"></span></span>
<span class="badge badge-error size-6 rounded-full p-0"> <span class="icon-[tabler--clock]"></span></span>
{{< /code >}}

<!-- Badge in a text -->

{{< headname level="3" >}} Badge in a text {{< /headname >}}

Badges used in text `inherit` the font size of the immediate parent element.

{{< code addClass="flex-col">}}

<p class="text-xl"> Heading <span class="badge badge-outline badge-secondary badge-xl ms-1 rounded-full">NEW</span></p>
<p class="text-lg"> Heading <span class="badge badge-outline badge-secondary badge-lg ms-1 rounded-full">NEW</span></p>
<p class="text-base"> Heading <span class="badge badge-outline badge-secondary ms-1 rounded-full">NEW</span></p>
<p class="text-sm"> Heading <span class="badge badge-outline badge-secondary badge-sm ms-1 rounded-full">NEW</span></p>
<p class="text-xs"> Heading <span class="badge badge-outline badge-secondary badge-xs ms-1 rounded-full">NEW</span></p>
{{< /code >}}

<!-- Badge in a button -->

{{< headname level="3" >}} Badge in a button {{< /headname >}}

Add badges to buttons to display additional information in buttons.

{{< code >}}

<button class="btn btn-primary btn-soft">
  Inbox
  <span class="badge badge-primary badge-sm">+99</span>
</button>
<button class="btn btn-primary btn-soft">
  Send
  <span class="badge badge-primary size-6 p-0"><span class="icon-[tabler--send]"></span></span>
</button>

{{< /code >}}

<!-- Avatar badges -->

{{< headname level="3" >}} Avatar badges {{< /headname >}}

Use the `img` tag to display avatar badges with an image.

{{< code >}}

<span class="badge badge-primary badge-lg">
  <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="John" class="size-4.5 rounded-full"/>
  John
</span>
<span class="badge badge-soft badge-primary badge-lg">
  <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="Anna" class="size-4.5 rounded-full"/>
  Anna
</span>
<span class="badge badge-outline badge-primary badge-lg">
  <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-10.png" alt="Sophia" class="size-4.5 rounded-full"/>
  Sophia
</span>
{{< /code >}}

{{< requires-js >}}

<!-------------------- Dismissible Badges -------------------->

{{< headname level="2" >}} Dismissible badges {{< /headname >}}

<!-- Default chips -->

{{< headname level="3" >}} Default chips {{< /headname >}}

Dismissible badges are also referred as chips.

Include the `data-remove-element` attribute in the close button element and set its value to `#id` to specify the element to be removed. Customize the removal animation by incorporating the `removing:` modifier, as illustrated below.

{{< callout "info" >}}
Refer {{< link link="components/remove-element/" addClass="link link-primary" >}}Remove Element{{< /link >}} plugin for more details.
{{< /callout >}}

{{< code >}}

<span class="badge badge-primary badge-lg removing:translate-x-5 removing:opacity-0 transition duration-300 ease-in-out" id="badge-1" >
  Badge
  <button class="icon-[tabler--circle-x-filled] size-5 min-h-0 cursor-pointer px-0" data-remove-element="#badge-1" aria-label="Dismiss Button" ></button>
</span>

<span class="badge badge-soft badge-primary badge-lg removing:translate-x-5 removing:opacity-0 transition duration-300 ease-in-out" id="badge-2" >
  Badge
  <button class="icon-[tabler--circle-x-filled] size-5 min-h-0 cursor-pointer px-0" data-remove-element="#badge-2" aria-label="Dismiss Button" ></button>
</span>

<span class="badge badge-outline badge-primary badge-lg removing:translate-x-5 removing:opacity-0 transition duration-300 ease-in-out" id="badge-3" >
  Badge
  <button class="icon-[tabler--circle-x-filled] size-5 min-h-0 cursor-pointer px-0" data-remove-element="#badge-3" aria-label="Dismiss Button" ></button>
</span>
{{< /code >}}

<!-- Avatar chips -->

{{< headname level="3" >}} Avatar chips {{< /headname >}}

A simple example of dismissible avatar badges.

{{< code >}}
<span class="badge badge-primary badge-lg removing:translate-x-5 removing:opacity-0 transition duration-300 ease-in-out" id="badge-4" >
<img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="John" class="size-4.5 rounded-full" />
John
<button class="icon-[tabler--circle-x-filled] size-5 min-h-0 cursor-pointer px-0" data-remove-element="#badge-4" aria-label="Dismiss Button" ></button>
</span>

<span class="badge badge-soft badge-primary badge-lg removing:translate-x-5 removing:opacity-0 transition duration-300 ease-in-out" id="badge-5" >
  <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="Anna" class="size-4.5 rounded-full"/>
  Anna
  <button class="icon-[tabler--circle-x-filled] size-5 min-h-0 cursor-pointer px-0" data-remove-element="#badge-5" aria-label="Dismiss Button" ></button>
</span>

<span class="badge badge-outline badge-primary badge-lg removing:translate-x-5 removing:opacity-0 transition duration-300 ease-in-out" id="badge-6" >
  <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-10.png" alt="Sophia" class="size-4.5 rounded-full"/>
  Sophia
  <button class="icon-[tabler--circle-x-filled] size-5 min-h-0 cursor-pointer px-0" data-remove-element="#badge-6" aria-label="Dismiss Button" ></button>
</span>
{{< /code >}}
