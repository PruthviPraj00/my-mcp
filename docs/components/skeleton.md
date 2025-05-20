---
title: "Skeleton"
components: 6
description: "The skeleton component is utilized to display the loading state of a component."
bg_image: "svg/components/skeleton.svg"
menu:
  main:
    parent: "components"

previous: Progress
previousLink: components/progress/

next: Stack
nextLink: components/stack/
---

<!-- Class table -->

{{< class-table >}}
skeleton | component | Displays a markup's structure.
skeleton-animated | modifier | Displays skeleton with loading animation.
{{< /class-table >}}

<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!--  Default skeleton  -->

{{< headname level="3" >}} Default skeleton {{< /headname >}}

Apply the `skeleton` component class to any markup to showcase it's structure.

{{< code >}}

<div class="skeleton h-32 w-32"></div>
{{< /code >}}

<!--  Animated skeleton  -->

{{< headname level="3" >}} Animated skeleton {{< /headname >}}

Apply the `skeleton-animated` modifier class to any markup to showcase it's structure with loading animation.

{{< code >}}

<div class="skeleton skeleton-animated h-32 w-32"></div>
{{< /code >}}

<!--  Active skeleton  -->

{{< headname level="3" >}} Active skeleton {{< /headname >}}

Add the `animate-pulse` animation class to any markup to display its structure with an active animation. For additional options, refer to the TailwindCSS <a href="https://tailwindcss.com/docs/animation" target="_blank" class="link link-primary">animation</a> documentation.

{{< code >}}

<div class="skeleton h-32 w-32 animate-pulse"></div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!--  Circle with content  -->

{{< headname level="3" >}} Circle with content {{< /headname >}}

Utilize the provided example to present a skeleton featuring a circular shape and content.

{{< code >}}

<div class="flex w-52 flex-col gap-4">
  <div class="flex items-center gap-4">
    <div class="skeleton h-16 w-16 shrink-0 rounded-full"></div>
    <div class="flex flex-col gap-4">
      <div class="skeleton h-4 w-20"></div>
      <div class="skeleton h-4 w-28"></div>
    </div>
  </div>
  <div class="skeleton h-32 w-full"></div>
</div>
{{< /code >}}

<!--  Rectangle with content  -->

{{< headname level="3" >}} Rectangle with content {{< /headname >}}

Utilize the provided example to present a skeleton featuring a Rectangular shape and content with loading animation.

{{< code >}}

<div class="flex w-52 flex-col gap-4">
  <div class="skeleton skeleton-animated h-32 w-full"></div>
  <div class="skeleton skeleton-animated h-4 w-28"></div>
  <div class="skeleton skeleton-animated h-4 w-full"></div>
  <div class="skeleton skeleton-animated h-4 w-full"></div>
</div>
{{< /code >}}
