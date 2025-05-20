---
title: "Window"
description: "The window mockup features a design that resembles a typical operating system window interface."
bg_image: "svg/mockups/window.svg"
components: 1
menu:
  main:
    parent: "mockups"

previous: Phone
previousLink: mockups/phone/

next: Advance Range slider
nextLink: third-party-plugins/advance-range-slider/
---

<!-- Class table -->

{{< class-table >}}
mockup-window | component | Container element.
{{< /class-table >}}

<!-------------------- Basic examples -------------------->

{{< headname level="2" >}} Basic examples {{< /headname >}}

<!-- Bordered -->

{{< headname level="3" >}} Bordered {{< /headname >}}

Wtilize the `mockup-window` class as a container for the window mockup and apply Tailwind utility classes such as `border` and `background-color` for styling.

{{< code >}}

<div class="mockup-window border border-base-content/20">
  <div class="flex justify-center px-4 py-16 border-t border-base-content/20">Hello!</div>
</div>
{{< /code >}}

<!-- Background color -->

{{< headname level="3" >}} Background color {{< /headname >}}

Window mockup featuring a customizable background color. Update it to your preference using the `bg-*` Tailwind utility class.

{{< code >}}

<div class="mockup-window border border-base-content/20 bg-base-300/40">
  <div class="flex justify-center px-4 py-16 bg-base-200">Hello!</div>
</div>
{{< /code >}}

<!-- Image -->

{{< headname level="3" >}} Image {{< /headname >}}

Window mockup featuring a image.

{{< code >}}

<div class="mockup-window border border-base-content/20 bg-base-200">
   <div class="flex justify-center h-80"><img class="w-full object-cover" src="https://cdn.flyonui.com/fy-assets/components/carousel/image-21.png" alt="window background" /></div>
</div>
{{< /code >}}
