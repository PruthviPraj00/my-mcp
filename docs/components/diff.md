---
title: "Diff"
description: "The Diff component allows for a side-by-side comparison of two items, making it easy to identify their differences and similarities."
bg_image: "svg/components/diff.svg"
components: 2
menu:
  main:
    parent: "components"

previous: Collapse
previousLink: components/collapse/

next: Indicator
nextLink: components/indicator/
---

<!-- Class table -->

{{< class-table >}}
diff| component | Base class for the diff component
diff-item-1 | part | Base class for the first item in the diff
diff-item-2 | part | Base class for the second item in the diff
diff-resizer | part | Base class for the resizer in the diff
blur-xs | modifier | Adds a small blur effect to the image
{{< /class-table >}}

<!-------------------- Type variants -------------------->

{{< headname level="2" >}} Type variants {{< /headname >}}

<!-- Image diff -->

{{< headname level="3" >}} Image diff {{< /headname >}}

The standard format for the diff is component class `diff` with two child div's with class `diff-item-1` and
`diff-item-2` respectively whereas the `diff-resizer` class is used to resize the diff.

{{< code >}}

<div class="diff aspect-video">
  <div class="diff-item-1">
    <img
      alt="mountains"
      src="https://cdn.flyonui.com/fy-assets/components/diff/image-1.png"
    />
  </div>
  <div class="diff-item-2">
    <img
      alt="flowers"
      src="https://cdn.flyonui.com/fy-assets/components/diff/image-2.png"
    />
  </div>
  <div class="diff-resizer"></div>
</div>
{{< /code >}}

<!-- Image diff with blur -->

{{< headname level="3" >}} Image diff with blur {{< /headname >}}

Use the `blur-xs` utility class to add a blur effect to the image. The intensity of the blur effect can be adjusted using the TailwindCSS <a href="https://tailwindcss.com/docs/blur" target="blank" class="link link-primary">Blur</a> utility classes.

{{< code >}}

<div class="diff aspect-video">
  <div class="diff-item-1">
    <img
      alt="mountain"
      src="https://cdn.flyonui.com/fy-assets/components/diff/image-1.png"
    />
  </div>
  <div class="diff-item-2">
    <img
      alt="mountain Blur"
      src="https://cdn.flyonui.com/fy-assets/components/diff/image-1.png"
      class="blur-xs"
    />
  </div>
  <div class="diff-resizer"></div>
</div>
{{< /code >}}

<!-- Text diff -->

{{< headname level="3" >}} Text diff {{< /headname >}}

Use div's with custom text and background color in `diff` to create a text diff.

{{< code >}}

<div class="diff aspect-video">
  <div class="diff-item-1">
    <div class="bg-primary text-primary-content grid place-content-center text-4xl sm:text-7xl font-black">FlyonUI</div>
  </div>
  <div class="diff-item-2">
    <div class="bg-base-200 grid place-content-center text-4xl sm:text-7xl font-black">FlyonUI</div>
  </div>
  <div class="diff-resizer"></div>
</div>
{{< /code >}}
