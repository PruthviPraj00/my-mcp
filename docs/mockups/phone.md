---
title: "Phone"
description: "The phone mockup presents a design that resembles an iPhone, showcasing its interface and features in a realistic format."
bg_image: "svg/mockups/phone.svg"
components: 1
menu:
  main:
    parent: "mockups"

previous: Code
previousLink: mockups/code/

next: Window
nextLink: mockups/window/
---

<!-- Class table -->

{{< class-table >}}
mockup-phone | component | Container element.
mockup-phone-camera | part | Add iphone dynamic island.
mockup-phone-display | part | Content container.
{{< /class-table >}}

<!-------------------- Basic examples -------------------->

{{< headname level="2" >}} Basic examples {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic example of phone.

Use the `mockup-phone` component class to contain the phone mockup. The `mockup-phone-camera` class introduces dynamic island UI elements. Meanwhile, the `mockup-phone-display` class serves as a container for displaying items.

{{< code >}}

<div class="mockup-phone">
  <div class="mockup-phone-camera"></div> 
  <div class="mockup-phone-display bg-base-200">
    <div class="h-142 w-80 grid place-content-center">Hi.</div>
  </div>
</div>
{{< /code >}}

<!-- Image -->

{{< headname level="3" >}} Image {{< /headname >}}

This demonstrates how we use images as display.

{{< code >}}

<div class="mockup-phone">
  <div class="mockup-phone-camera"></div> 
  <div class="mockup-phone-display flex justify-center">
    <div class="h-142 w-80"><img class="size-full object-cover" src="https://cdn.flyonui.com/fy-assets/components/iphone/image.png" alt="phone background" /></div>
  </div>
</div>
{{< /code >}}
