---
title: "Avatar"
description: "Avatars bring life to the interface, offering a small but vivid representation of individuals or businesses."
bg_image: "svg/components/avatar.svg"
components: 9
menu:
  main:
    parent: "components"

previous: Alert
previousLink: components/alert/

next: Badge
nextLink: components/badge/
---

<!-- Class table -->

{{< class-table >}}
avatar | component | Container element
avatar-group | component | Container for grouping multiple avatars
avatar-placeholder | part | To show some letters as avatar placeholder
pull-up | style | Add pull up animation when used with avatar group
avatar-online-top | modifier | Shows a green dot at top as online indicator
avatar-online-bottom | modifier | Shows a green dot at bottom as online indicator
avatar-away-top | modifier | Shows a warning dot at top as away indicator
avatar-away-bottom | modifier | Shows a warning dot at bottom as away indicator
avatar-busy-top | modifier | Shows an error dot at top as busy indicator
avatar-busy-bottom | modifier | Shows an error dot at bottom as busy indicator
avatar-offline-top | modifier | Shows a neutral dot at top as offline indicator
avatar-offline-bottom | modifier | Shows a neutral dot at bottom as offline indicator
{{< /class-table >}}

<!-------------------- Shape -------------------->

{{< headname level="2" >}} Shape {{< /headname >}}

<!-- Circular avatars -->

{{< headname level="3" >}} Circular avatars {{< /headname >}}

The `avatar` component class serves as a wrapper for the image, while the <a href="https://tailwindcss.com/docs/size" target="_blank" class="link link-primary">Size</a> and <a href="https://tailwindcss.com/docs/border-radius" target="_blank" class="link link-primary">Border Radius</a> utility classes can be utilized to adjust its dimensions and radius.

Use `rounded-full` utility class to make circular avatars.

{{< code addClass="items-center" >}}

<div class="avatar">
  <div class="size-6 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar">
  <div class="size-10 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar">
  <div class="size-14 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar">
  <div class="size-16 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>
{{< /code >}}

<!-- Rounded avatars -->

{{< headname level="3" >}} Rounded avatars {{< /headname >}}

Apply the `rounded-md` utility class to achieve rounded avatars.

{{< code addClass="items-center" >}}

<div class="avatar">
  <div class="size-6 rounded-md">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar">
  <div class="size-10 rounded-md">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar">
  <div class="size-14 rounded-md">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar">
  <div class="size-16 rounded-md">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>
{{< /code >}}

<!-- Masked avatars -->

{{< headname level="3" >}} Masked avatars {{< /headname >}}

The `mask` class modifier can be applied to define the shape of the avatar.

{{< callout "info">}}
Refer {{< link link="content/mask/" addClass="link link-primary" >}}Mask Element{{< /link >}} for more details.
{{< /callout >}}

{{< code addClass="items-center" >}}

<div class="avatar">
  <div class="size-16 mask mask-decagon">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>
<div class="avatar">
  <div class="size-16 mask mask-hexagon-2">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>
<div class="avatar">
  <div class="size-16 mask mask-heart">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>
{{< /code >}}

<!-------------------- Placeholder -------------------->

{{< headname level="2" >}} Placeholder {{< /headname >}}

<!-- Placeholder icon -->

{{< headname level="3" >}} Placeholder icon {{< /headname >}}

Use `avatar-placeholder` component class with `avatar` for placeholder styles. </br>
Design circular avatar elements featuring placeholder icons.

{{< code addClass="items-center" >}}

<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-6 rounded-full">
    <span class="icon-[tabler--user] size-4"></span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-10 rounded-full">
    <span class="icon-[tabler--user] size-6"></span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-14 rounded-full">
    <span class="icon-[tabler--user] size-8"></span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-16 rounded-full">
    <span class="icon-[tabler--user] size-10"></span>
  </div>
</div>
{{< /code >}}

<!-- Placeholder initials -->

{{< headname level="3" >}} Placeholder initials {{< /headname >}}

Design circular avatar elements featuring placeholder initials.

{{< code addClass="items-center" >}}

<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-6 rounded-full">
    <span class="text-xs uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-14 rounded-full">
    <span class="text-xl uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-16 rounded-full">
    <span class="text-2xl uppercase">cl</span>
  </div>
</div>
{{< /code >}}

<!-------------------- Color variants -------------------->

{{< headname level="2" >}} Color variants {{< /headname >}}

<!-- Solid color -->

{{< headname level="3" >}} Solid color {{< /headname >}}

Pre-configured solid color avatar designs.

{{< code addClass="items-center" >}}

<div class="avatar avatar-placeholder">
  <div class="bg-primary text-primary-content w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-secondary text-secondary-content w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-info text-info-content w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-success text-success-content w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>
<div class="avatar avatar-placeholder">
  <div class="bg-warning text-warning-content w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-error text-error-content w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>
{{< /code >}}

<!-- Soft color -->

{{< headname level="3" >}} Soft color {{< /headname >}}

Pre-configured soft color avatar designs.

{{< code addClass="items-center" >}}

<div class="avatar avatar-placeholder">
  <div class="bg-primary/10 text-primary w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-secondary/10 text-secondary w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-info/10 text-info w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-success/10 text-success w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-warning/10 text-warning w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="bg-error/10 text-error w-10 rounded-full">
    <span class="text-md uppercase">cl</span>
  </div>
</div>
{{< /code >}}

<!-- Outline color -->

{{< headname level="3" >}} Outline color {{< /headname >}}

Pre-configured outline color avatar designs.

{{< code addClass="items-center" >}}

<div class="avatar avatar-placeholder">
  <div class="border-primary text-primary w-10 rounded-full border">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="border-secondary text-secondary w-10 rounded-full border">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="border-info text-info w-10 rounded-full border">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="border-success text-success w-10 rounded-full border">
    <span class="text-md uppercase">cl</span>
  </div>
</div>
<div class="avatar avatar-placeholder">
  <div class="border-warning text-warning w-10 rounded-full border">
    <span class="text-md uppercase">cl</span>
  </div>
</div>

<div class="avatar avatar-placeholder">
  <div class="border-error text-error w-10 rounded-full border">
    <span class="text-md uppercase">cl</span>
  </div>
</div>
{{< /code >}}

<!-------------------- Status -------------------->

{{< headname level="2" >}} Status {{< /headname >}}

<!-- Top status indicators -->

{{< headname level="3" >}} Top status indicators {{< /headname >}}

Avatars featuring various status indicators at top.

{{< code addClass="items-center" >}}

<div class="avatar avatar-online-top">
  <div class="w-6 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar avatar-away-top">
  <div class="w-10 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar avatar-busy-top">
  <div class="w-14 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar avatar-offline-top">
  <div class="w-16 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>
{{< /code >}}

<!-- Bottom status indicators -->

{{< headname level="3" >}} Bottom status indicators {{< /headname >}}

Avatars featuring various status indicators at bottom.

{{< code addClass="items-center" >}}

<div class="avatar avatar-online-bottom">
  <div class="w-6 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar avatar-away-bottom">
  <div class="w-10 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar avatar-busy-bottom">
  <div class="w-14 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>

<div class="avatar avatar-offline-bottom">
  <div class="w-16 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>
{{< /code >}}

<!-- Avatar with logo indicator -->

{{< headname level="3" >}} Avatar with logo indicator {{< /headname >}}

Avatars featuring various status indicators at bottom.

{{< code addClass="items-center" >}}

<div class="avatar ">
  <div class="w-10 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
  <span class="bg-base-100 absolute bottom-0 end-0 flex translate-x-2 translate-y-2 transform items-center rounded-full p-1"><svg xmlns="http://www.w3.org/1000/svg" class="size-4" viewBox="0 0 60 60" preserveAspectRatio="xMidYMid meet" alt="Slack Logo"><path d="M22,12 a6,6 0 1 1 6,-6 v6z M22,16 a6,6 0 0 1 0,12 h-16 a6,6 0 1 1 0,-12" fill="#36C5F0" /><path d="M48,22 a6,6 0 1 1 6,6 h-6z M32,6 a6,6 0 1 1 12,0v16a6,6 0 0 1 -12,0z" fill="#2EB67D" /><path d="M38,48 a6,6 0 1 1 -6,6 v-6z M54,32 a6,6 0 0 1 0,12 h-16 a6,6 0 1 1 0,-12" fill="#ECB22E" /><path d="M12,38 a6,6 0 1 1 -6,-6 h6z M16,38 a6,6 0 1 1 12,0v16a6,6 0 0 1 -12,0z" fill="#E01E5A" /></svg>
  </span>
</div>
<div class="avatar ">
  <div class="w-10 rounded-md">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
  <span class="bg-base-100 absolute bottom-0 end-0 flex translate-x-2 translate-y-2 transform items-center rounded-full p-1"><svg aria-hidden="true" class="size-4" version="1.1" viewBox="0 0 16 16" width="24"><path
        fill-rule="evenodd"
        d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"><path /></svg>
  </span>
</div>
{{< /code >}}

<!-- Avatar group -->

{{< headname level="2" >}} Avatar group {{< /headname >}}

<!-- Basic circular avatar group -->

{{< headname level="3" >}}Basic circular avatar group{{< /headname >}}

The `avatar-group` class acts as a container for avatars, allowing you to manage the spacing between them with the `-space-x-4` class.

{{< code addClass="items-center" >}}

<div class="avatar-group -space-x-5">
  <div class="avatar">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-12.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-10.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png" alt="avatar" />
    </div>
  </div>
</div>

<div class="avatar-group -space-x-5">
  <div class="avatar">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-10.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-12.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar avatar-placeholder">
    <div class="bg-neutral text-neutral-content w-13">
      <span>+9</span>
    </div>
  </div>
</div>
{{< /code >}}

<!--Pull up animation with tooltip  -->

{{< headname level="3" >}} Pull up animation with tooltip {{< /headname >}}

Utilize the `pull-up` class to enable hover functionality for the avatar.

{{< callout "info" >}}
Refer {{< link link="overlays/tooltip/" addClass="link link-primary" >}}Tooltip{{< /link >}} documentation for information on tooltip elements.
{{< /callout >}}

{{< code addClass="items-center" >}}

<div class="avatar-group pull-up -space-x-5">
  <div class="tooltip">
    <div class="tooltip-toggle avatar">
      <div class="w-13">
        <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
      </div>
    </div>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Jhon Doe</span>
    </span>
  </div>
  <div class="tooltip">
    <div class="tooltip-toggle avatar">
      <div class="w-13">
        <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-10.png" alt="avatar" />
      </div>
    </div>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Elliot Chen</span>
    </span>
  </div>
  <div class="tooltip">
    <div class="tooltip-toggle avatar">
      <div class="w-13">
        <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-12.png" alt="avatar" />
      </div>
    </div>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Maya Singh</span>
    </span>
  </div>
  <div class="tooltip">
    <div class="tooltip-toggle avatar">
      <div class="w-13">
        <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png" alt="avatar" />
      </div>
    </div>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Jasmine Rivera</span>
    </span>
  </div>
</div>

<!-- pullup animation with counter -->
<div class="avatar-group pull-up -space-x-5">
  <div class="tooltip">
    <div class="tooltip-toggle avatar">
      <div class="w-13">
        <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-10.png" alt="avatar" />
      </div>
    </div>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Maya Singh</span>
    </span>
  </div>
  <div class="tooltip">
    <div class="tooltip-toggle avatar">
      <div class="w-13">
        <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-12.png" alt="avatar" />
      </div>
    </div>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Jasmine Rivera</span>
    </span>
  </div>
  <div class="tooltip">
    <div class="tooltip-toggle avatar">
      <div class="w-13">
        <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png" alt="avatar" />
      </div>
    </div>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Elliot Chen</span>
    </span>
  </div>
  <div class="tooltip cursor-default">
    <div class="tooltip-toggle avatar avatar-placeholder">
      <div class="bg-neutral text-neutral-content w-13">
        <span>+9</span>
      </div>
    </div>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">9 more</span>
    </span>
  </div>
</div>
{{< /code >}}
