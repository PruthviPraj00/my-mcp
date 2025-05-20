---
title: "Browser"
description: "The browser mockup features a design that resembles a browser window, complete with typical interface elements and layout."
bg_image: "svg/mockups/browser.svg"
components: 1
menu:
  main:
    parent: "mockups"

previous: Table
previousLink: tables/table/

next: Code
nextLink: mockups/code/
---

<!-- Class table -->

{{< class-table >}}
mockup-browser | component | Container element.
mockup-browser-toolbar| part| The toolbar that can include address bar or other things.
{{< /class-table >}}

<!-------------------- Basic examples -------------------->

{{< headname level="2" >}} Basic examples {{< /headname >}}

<!-- Bordered -->

{{< headname level="3" >}} Bordered {{< /headname >}}

The `mockup-browser` class serves as a container for the browser mockup, while `mockup-browser-toolbar` acts as a container for the header links within the mockup.

{{< code >}}

<div class="mockup-browser border border-neutral/30">
  <div class="mockup-browser-toolbar">
    <div class="input border border-neutral/30">https://flyonui.com</div>
  </div>
  <div class="flex justify-center px-4 py-16 border-t border-neutral/30">Hello!</div>
</div>
{{< /code >}}

<!-- Background color -->

{{< headname level="3" >}} Background color {{< /headname >}}

Browser mockup featuring a customizable background color. Update it to your preference using the `bg-*` Tailwind utility class.

{{< code >}}

<div class="mockup-browser bg-base-300/40">
  <div class="mockup-browser-toolbar">
    <div class="input bg-base-200">https://flyonui.com</div>
  </div>
  <div class="flex justify-center px-4 py-16 bg-base-200">Hello!</div>
</div>
{{< /code >}}

<!-- Image -->

{{< headname level="3" >}} Image {{< /headname >}}

Browser mockup featuring a image.

{{< code >}}

<div class="mockup-browser bg-base-300/40">
  <div class="mockup-browser-toolbar">
    <div class="input bg-base-200">https://flyonui.com</div>
  </div>
  <div class="flex h-80 justify-center"><img class="w-full object-cover" src="https://cdn.flyonui.com/fy-assets/components/carousel/image-14.png" alt="browser background" /></div>
</div>
{{< /code >}}
