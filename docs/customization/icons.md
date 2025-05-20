---
title: "Icons"
description: "Guide on using and customizing icons in FlyonUI with Iconify integration."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "customization"
    weight: 5

previous: Colors
previousLink: customization/colors/

next: Themes
nextLink: customization/themes/
---

<!-------------------- Icons -------------------->

{{< headsingle addClass="!mt-px" level="2" >}} Icons {{< /headsingle >}}


FlyonUI uses Tabler icons from Iconify. To include them, follow the steps outlined in the {{< link link="getting-started/quick-start/#setup-icons" addClass="link link-primary" >}}docs{{< /link >}}.

**<a href="https://iconify.design" target="_blank">Iconify</a>** provides access to a wide range of open-source icon sets, making it easier to use and customize icons with a large selection of open-source components.



<!-- Using Different Icons  -->

{{< headname level="3" >}} Using Different Icons {{< /headname >}}

If users have specific icon requirements, they can follow the steps below to include different icons in their projects. For more details, refer to the <a href="https://iconify.design/docs/usage/css/tailwind/" class="link link-primary" target="_blank">official Iconify documentation</a>.

1. Install the necessary Iconify packages via npm:

   {{< code-highlight addClass="mt-3" lang="bash" >}}npm i -D @iconify/tailwind4 @iconify/json{{< /code-highlight >}}

   - `@iconify/json`: Includes all icons from Iconify.
   - `@iconify-json/tabler`: Includes specific icon libraries (in this case, Solar Icons).

2. To include the icons, add the following line to your CSS file::

{{< code-highlight addClass="mt-3" lang="bash" >}}@plugin "@iconify/tailwind4";{{< /code-highlight >}}

3. Use the icon in your HTML by specifying the appropriate class. For example, to use the Solar icon:

```html
<div class="flex items-center">
  <span class="icon-[solar--user-bold] size-10"></span>
  <span class="icon-[ic--sharp-account-circle] size-10"></span>
  <span class="icon-[mdi--account-child] size-10"></span>
  <span class="icon-[line-md--account] size-10"></span>
  <span class="icon-[svg-spinners--3-dots-move] size-10"></span>
</div>
```

Here’s an example of the different icon in action:

<div class="flex items-center mt-5 gap-5">
  <span class="icon-[solar--user-bold] size-10"></span>
  <span class="icon-[ic--sharp-account-circle] size-10"></span>
  <span class="icon-[mdi--account-child] size-10"></span>
  <span class="icon-[line-md--account] size-10"></span>
  <span class="icon-[svg-spinners--3-dots-move] size-10"></span>
</div>
