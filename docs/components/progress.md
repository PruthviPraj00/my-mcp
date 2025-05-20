---
title: "Progress"
components: 5
description: "Progress is represented by a linear indicator that displays the user's advancement through a specific task."
bg_image: "svg/components/progress.svg"
menu:
  main:
    parent: "components"

previous: Loading
previousLink: components/loading/

next: Radial progress
nextLink: components/radial-progress/
---

<!-- Class Table -->

{{< class-table >}}
progress | component | Base class for progress container component.
progress-step | component | Base class for progress steps.
progress-bar | part | Base class for progress bar component.
progress-label | part | Creates the basic variant for floating labels.
progress-striped | style | Adds striped background to progress bars.
progress-animated | style | Adds animation to striped bars.
progress-indeterminate | style | Used for progress bars without specific value.
progress-primary | color | Adds 'primary' color to progress bar.
progress-secondary | color | Adds 'secondary' color to progress bar.
progress-accent | color | Adds 'accent' color to progress bar.
progress-info | color | Adds 'info' color to progress bar.
progress-success | color | Adds 'success' color to progress bar.
progress-warning | color | Adds 'warning' color to progress bar.
progress-error | color | Adds 'error' color to progress bar.
progress-vertical | direction | Aligns the progress bar vertically.
progress-horizontal | direction | Aligns the progress bar horizontal(default).
{{< /class-table >}}

<!-------------------- Alignment -------------------->

{{< headname level="2" >}} Alignment {{< /headname >}}

<!-- Horizontal -->

{{< headname level="3" >}} Horizontal {{< /headname >}}

Utilize the `progress` component class for the default horizontal progress component. Use the `w-{number}` utility class
to represent the progress width. Refer TailwindCSS <a href="https://tailwindcss.com/docs/width" class="link link-primary" target="blank">width</a> documentation for more
info.

{{< code addClass="flex-col" >}}

<div class="progress w-56" role="progressbar" aria-label="0% Progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-0"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="25% Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-1/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="50% Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-1/2"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="75% Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="100% Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-full"></div>
</div>
{{< /code >}}

<!-- Vertical -->

{{< headname level="3" >}} Vertical {{< /headname >}}

Use modifier class `progress-vertical` for vertical progress component. Use the `h-{number}` utility class to represent
the progress height. Refer TailwindCSS <a href="https://tailwindcss.com/docs/height" class="link link-primary" target="blank">height</a> documentation for more info.

{{< code addClass="gap-5" >}}

<div class="progress progress-vertical h-56" role="progressbar" aria-label="0% Vertical Progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar h-0"></div>
</div>
<div class="progress progress-vertical h-56" role="progressbar" aria-label="25% Vertical Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" >
  <div class="progress-bar h-1/4"></div>
</div>
<div class="progress progress-vertical h-56" role="progressbar" aria-label="50% Vertical Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100" >
  <div class="progress-bar h-1/2"></div>
</div>
<div class="progress progress-vertical h-56" role="progressbar" aria-label="75% Vertical Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" >
  <div class="progress-bar h-3/4"></div>
</div>
<div class="progress progress-vertical h-56" role="progressbar" aria-label="100% Vertical Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" >
  <div class="progress-bar h-full"></div>
</div>
{{< /code >}}

<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!-- With custom height -->

{{< headname level="3" >}} With custom height {{< /headname >}}

Use TailwindCSS utility class `h-{number}` for custom height(thickness) of progress bar.

<!-- Callout -->

{{< callout "info" >}}
Similarly, TailwindCSS utility class `w-{number}` can be used for custom width(thickness) of vertical progress bars.
{{< /callout >}}

{{< code addClass="flex-col" >}}

<div class="progress w-56" role="progressbar" aria-label="Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-1/2"></div>
</div>
<div class="progress h-2 w-56" role="progressbar" aria-label="Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-1/2"></div>
</div>
<div class="progress h-2.5 w-56" role="progressbar" aria-label="Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-1/2"></div>
</div>
<div class="progress h-3 w-56" role="progressbar" aria-label="Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-1/2"></div>
</div>
<div class="progress h-4 w-56" role="progressbar" aria-label="Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-1/2"></div>
</div>
{{< /code >}}

<!-- With labels (Horizontal) -->

{{< headname level="3" >}} With labels (Horizontal) {{< /headname >}}

Utilize labels for presenting progress information.

<!-- Labels within -->

{{< headname level="4" >}} Labels within {{< /headname >}}

Embedding values directly into the `progress-bar` will display them within the bars.

{{< code addClass="flex-col" >}}

<div class="progress h-4" role="progressbar" aria-label="25% Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-1/4 font-normal">25%</div>
</div>
<div class="progress h-4" role="progressbar" aria-label="50% Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-1/2 font-normal">50%</div>
</div>
<div class="progress h-4" role="progressbar" aria-label="75% Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-3/4 font-normal">75%</div>
</div>
<div class="progress h-4" role="progressbar" aria-label="100% Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-full font-normal">100%</div>
</div>
{{< /code >}}

<!-- Labels at end -->

{{< headname level="4" >}} Labels at end {{< /headname >}}

Use the following example to showcase labels positioned at the end of the progress bar.

{{< code addClass="flex-col" >}}

<div class="flex w-52 items-center gap-2">
  <div class="progress" role="progressbar" aria-label="25% Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-1/4"></div>
  </div>
  <span class="text-base-content text-xs font-light">25%</span>
</div>

<div class="flex w-52 items-center gap-2">
  <div class="progress" role="progressbar" aria-label="50% Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-1/2"></div>
  </div>
  <span class="text-base-content text-xs font-light">50%</span>
</div>

<div class="flex w-52 items-center gap-2">
  <div class="progress" role="progressbar" aria-label="75% Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-3/4"></div>
  </div>
  <span class="text-base-content text-xs font-light">75%</span>
</div>

<div class="flex w-52 items-center gap-2">
  <div class="progress" role="progressbar" aria-label="100% Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-full"></div>
  </div>
  <span class="text-base-content text-xs font-light">100%</span>
</div>
{{< /code >}}

<!-- With title label -->

{{< headname level="4" >}} With title label {{< /headname >}}

Use the following example to showcase progress bar with title label.

{{< code addClass="flex-col" >}}

<div class="w-52">
  <div class="mb-1 flex items-end justify-between">
    <p class="text-base-content text-xs font-medium">Title</p>
    <span class="text-base-content text-xs font-light">25%</span>
  </div>
  <div class="progress" role="progressbar" aria-label="25% Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-1/4"></div>
  </div>
</div>

<div class="w-52">
  <div class="mb-1 flex items-end justify-between">
    <p class="text-base-content text-xs font-medium">Title</p>
    <span class="text-base-content text-xs font-light">50%</span>
  </div>
  <div class="progress" role="progressbar" aria-label="50% Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-1/2"></div>
  </div>
</div>

<div class="w-52">
  <div class="mb-1 flex items-end justify-between">
    <p class="text-base-content text-xs font-medium">Title</p>
    <span class="text-base-content text-xs font-light">75%</span>
  </div>
  <div class="progress" role="progressbar" aria-label="75% Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-3/4"></div>
  </div>
</div>

<div class="w-52">
  <div class="mb-1 flex items-end justify-between">
    <p class="text-base-content text-xs font-medium">Title</p>
    <span class="text-base-content text-xs font-light">100%</span>
  </div>
  <div class="progress" role="progressbar" aria-label="100% Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-full"></div>
  </div>
</div>
{{< /code >}}

<!-- Floating labels -->

{{< headname level="4" >}} Floating labels {{< /headname >}}

Use the following example to showcase floating labels for progress bar. Use modifier class `progress-label` for basic
floating label & position it using arbitrary class `ms-[calc(X% - Yrem)]`, where `X` is progress bar width(%) & `Y` is
half the width of floating label.

<!-- Callout -->

{{< callout "info" >}}
You can also position the floating labels below the progress bar by placing their code below it instead of above.
{{< /callout >}}

{{< code addClass="flex-col" >}}

<div class="flex w-52 flex-col gap-1">
  <span class="progress-label ms-[calc(25%-1.25rem)]">25%</span>
  <div class="progress h-2" role="progressbar" aria-label="25% Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-1/4"></div>
  </div>
</div>
<div class="flex w-52 flex-col gap-1">
  <span class="progress-label ms-[calc(50%-1.25rem)]">50%</span>
  <div class="progress h-2" role="progressbar" aria-label="50% Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-1/2"></div>
  </div>
</div>
<div class="flex w-52 flex-col gap-1">
  <span class="progress-label ms-[calc(75%-1.25rem)]">75%</span>
  <div class="progress h-2" role="progressbar" aria-label="75% Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-3/4"></div>
  </div>
</div>
<div class="flex w-52 flex-col gap-1">
  <span class="progress-label ms-[calc(100%-1.4rem)]">100%</span>
  <div class="progress h-2" role="progressbar" aria-label="100% Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar w-full"></div>
  </div>
</div>
{{< /code >}}

<!-- With labels (Vertical) -->

{{< headname level="3" >}} With labels (Vertical) {{< /headname >}}

Use the labels to showcase progress for vertical bars.

<!-- In center  -->

{{< headname level="4" >}} In center {{< /headname >}}

Use below given examples to showcase labels within squared progress bars in center.

{{< code addClass="gap-5" >}}

<div class="progress progress-vertical h-56 w-4 rounded-none" role="progressbar" aria-label="25% Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar h-1/4 rounded-none font-normal"><span class="-rotate-90">25%</span></div>
</div>
<div class="progress progress-vertical h-56 w-4 rounded-none" role="progressbar" aria-label="50% Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar h-1/2 rounded-none font-normal"><span class="-rotate-90">50%</span></div>
</div>
<div class="progress progress-vertical h-56 w-4 rounded-none" role="progressbar" aria-label="75% Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar h-3/4 rounded-none font-normal"><span class="-rotate-90">75%</span></div>
</div>
<div class="progress progress-vertical h-56 w-4 rounded-none" role="progressbar" aria-label="100% Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar h-full rounded-none font-normal"><span class="-rotate-90">100%</span></div>
</div>
{{< /code >}}

<!-- At top  -->

{{< headname level="4" >}} At top {{< /headname >}}

Use below given examples to showcase labels at top of vertical progress bars.

{{< code addClass="gap-5" >}}

<div class="flex h-56 flex-col items-center gap-2">
  <span class="text-base-content text-xs font-light">25%</span>
  <div class="progress progress-vertical w-4" role="progressbar" aria-label="25% Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar h-1/4"></div>
  </div>
</div>
<div class="flex h-56 flex-col items-center gap-2">
  <span class="text-base-content text-xs font-light">50%</span>
  <div class="progress progress-vertical w-4" role="progressbar" aria-label="50% Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar h-1/2"></div>
  </div>
</div>
<div class="flex h-56 flex-col items-center gap-2">
  <span class="text-base-content text-xs font-light">75%</span>
  <div class="progress progress-vertical w-4" role="progressbar" aria-label="75% Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar h-3/4"></div>
  </div>
</div>
<div class="flex h-56 flex-col items-center gap-2">
  <span class="text-base-content text-xs font-light">100%</span>
  <div class="progress progress-vertical w-4" role="progressbar" aria-label="100% Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar h-full"></div>
  </div>
</div>
{{< /code >}}

<!-- With labels & title -->

{{< headname level="4" >}} With labels & title {{< /headname >}}

Use below given examples to showcase labels with title in vertical progress bars.

{{< code addClass="gap-5" >}}

<div class="flex h-56 flex-col items-center justify-between gap-1">
  <span class="text-base-content text-xs font-light">25%</span>
  <div class="progress progress-vertical w-4" role="progressbar" aria-label="25% Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar h-1/4"></div>
  </div>
  <p class="text-base-content text-xs font-medium">Title</p>
</div>
<div class="flex h-56 flex-col items-center justify-between gap-1">
  <span class="text-base-content text-xs font-light">50%</span>
  <div class="progress progress-vertical w-4" role="progressbar" aria-label="50% Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar h-1/2"></div>
  </div>
  <p class="text-base-content text-xs font-medium">Title</p>
</div>
<div class="flex h-56 flex-col items-center justify-between gap-1">
  <span class="text-base-content text-xs font-light">75%</span>
  <div class="progress progress-vertical w-4" role="progressbar" aria-label="75% Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar h-3/4"></div>
  </div>
  <p class="text-base-content text-xs font-medium">Title</p>
</div>
<div class="flex h-56 flex-col items-center justify-between gap-1">
  <span class="text-base-content text-xs font-light">100%</span>
  <div class="progress progress-vertical w-4" role="progressbar" aria-label="100% Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar h-full"></div>
  </div>
  <p class="text-base-content text-xs font-medium">Title</p>
</div>
{{< /code >}}

<!-- Floating labels -->

{{< headname level="4" >}} Floating labels {{< /headname >}}

Implement floating labels for vertical progress bars using the provided example. Utilize the `progress-label` modifier
class for the basic floating label and position it with the `bottom-[calc(X% - Yrem)]` class alongside classes `absolute
start-0`. Here, `X` represents the progress bar height percentage, and `Y` signifies half the height of the floating
label within the relative TailwindCSS position class.

{{< code addClass="gap-5" >}}

<div class="flex gap-5">
  <div class="flex h-56 gap-1">
    <div class="relative w-10"><span class="progress-label absolute bottom-[calc(25%-0.75rem)] start-0">25%</span></div>
    <div class="progress progress-vertical w-2" role="progressbar" aria-label="25% Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" >
      <div class="progress-bar h-1/4"></div>
    </div>
  </div>
  
  <div class="flex h-56 gap-1">
    <div class="progress progress-vertical w-2" role="progressbar" aria-label="50% Progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100" >
      <div class="progress-bar h-1/2"></div>
    </div>
    <div class="relative w-10"><span class="progress-label absolute bottom-[calc(50%-0.75rem)] start-0">50%</span></div>
  </div>
</div>

<div class="flex gap-5">
  <div class="flex h-56 gap-1">
    <div class="relative w-10">
      <span class="progress-label border-primary text-primary absolute bottom-[calc(75%-0.75rem)] start-0">75%</span>
    </div>
    <div class="progress progress-vertical w-2" role="progressbar" aria-label="75% Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" >
      <div class="progress-bar progress-primary h-3/4"></div>
    </div>
  </div>
  
  <div class="flex h-56 gap-1">
    <div class="progress progress-vertical w-2" role="progressbar" aria-label="100% Progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" >
      <div class="progress-bar progress-primary h-full"></div>
    </div>
    <div class="relative w-11">
      <span class="progress-label border-primary text-primary absolute bottom-[calc(100%-0.75rem)] start-0">100%</span>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Backgrounds -------------------->

{{< headname level="2" >}} Backgrounds {{< /headname >}}

<!-- Semantic bars -->

{{< headname level="3" >}} Semantic bars {{< /headname >}}

To apply semantic colors to progress bars, utilize the `progress-{semantic-color}` class alongside the component class
`progress-bar`.

{{< code addClass="flex-col" >}}

<div class="progress w-56" role="progressbar" aria-label="Neutral Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Primary Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-primary w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Secondary Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-secondary w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Accent Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-accent w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Info Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-info w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Success Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-success w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Warning Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-warning w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Error Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-error w-3/4"></div>
</div>
{{< /code >}}

<!-- Striped bars -->

{{< headname level="3" >}} Striped bars {{< /headname >}}

Include the modifier class `progress-striped` with the `progress-bar` component class for striped progress bars.

{{< code addClass="flex-col" >}}

<div class="progress w-56" role="progressbar" aria-label="Neutral Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-striped w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Primary Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-primary progress-striped w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Secondary Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-secondary progress-striped w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Accent Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-accent progress-striped w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Info Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-info progress-striped w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Success Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-success progress-striped w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Warning Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-warning progress-striped w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Error Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-error progress-striped w-3/4"></div>
</div>
{{< /code >}}

<!-- Animated bars -->

{{< headname level="3" >}} Animated bars {{< /headname >}}

Utilize the modifier classes `progress-striped` and `progress-animated` in conjunction with the component class
`progress-bar` to create animated striped bars.

{{< code addClass="flex-col" >}}

<div class="progress w-56" role="progressbar" aria-label="Neutral Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-striped progress-animated w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Primary Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-primary progress-striped progress-animated w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Secondary Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-secondary progress-striped progress-animated w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Accent Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-accent progress-striped progress-animated w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Info Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-info progress-striped progress-animated w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Success Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-success progress-striped progress-animated w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Warning Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-warning progress-striped progress-animated w-3/4"></div>
</div>
<div class="progress w-56" role="progressbar" aria-label="Error Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-error progress-striped progress-animated w-3/4"></div>
</div>
{{< /code >}}

<!-------------------- Shape -------------------->

{{< headname level="2" >}} Shape {{< /headname >}}

<!-- Rounded -->

{{< headname level="3" >}} Rounded {{< /headname >}}

This is the default shape of progress bars. Refer TailwindCSS <a href="https://tailwindcss.com/docs/border-radius" class="link link-primary" target="blank">border radius</a> documentation for more options.

{{< code addClass="flex-col" >}}

<div class="progress w-56" role="progressbar" aria-label="Rounded Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-primary w-3/4"></div>
</div>
{{< /code >}}

<!-- Squared -->

{{< headname level="3" >}} Squared {{< /headname >}}

Apply the TailwindCSS utility class `rounded-none` to both the component classes `progress` and `progress-bar` to create
a squared progress bar.

{{< code addClass="flex-col" >}}

<div class="progress w-56 rounded-none" role="progressbar" aria-label="Squared Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-primary w-3/4 rounded-none"></div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Multiple progress -->

{{< headname level="3" >}} Multiple progress {{< /headname >}}

Utilize the provided examples to implement multiple progress bars along with corresponding options such as default,
striped, and animated.

{{< code addClass="flex-col" >}}

<!-- Default -->

<div>
  <div class="text-base-content mb-1 text-sm font-semibold">Default</div>
  <div class="progress h-3">
    <div class="progress-bar progress-primary w-1/4 rounded-e-none"></div> 
    <div class="progress-bar progress-success w-1/4 rounded-none"></div>
    <div class="progress-bar progress-error w-1/4 rounded-s-none"></div>
  </div>
</div>

<!-- Striped -->

<div>
  <div class="text-base-content mb-1 text-sm font-semibold">Striped</div>
  <div class="progress h-3">
    <div class="progress-bar progress-primary progress-striped w-1/4 rounded-e-none"></div>
    <div class="progress-bar progress-success progress-striped w-1/4 rounded-none"></div>
    <div class="progress-bar progress-error progress-striped w-1/4 rounded-s-none"></div>
  </div>
</div>

<!-- Animated -->

<div>
  <div class="text-base-content mb-1 text-sm font-semibold">Animated</div>
  <div class="progress h-3">
    <div class="progress-bar progress-primary progress-striped progress-animated w-1/4 rounded-e-none"></div>
    <div class="progress-bar progress-success progress-striped progress-animated w-1/4 rounded-none"></div>
    <div class="progress-bar progress-error progress-striped progress-animated w-1/4 rounded-s-none"></div>
  </div>
</div>
{{< /code >}}

<!-- Indeterminate -->

{{< headname level="3" >}} Indeterminate {{< /headname >}}

Apply the modifier class `progress-indeterminate` to the component class `progress-bar` to create a progress bar without
a specific value.

{{< code addClass="flex-col" >}}

<div class="progress w-56">
  <div class="progress-bar progress-indeterminate"></div>
</div>
<div class="progress w-56">
  <div class="progress-bar progress-indeterminate progress-primary"></div>
</div>
<div class="progress w-56">
  <div class="progress-bar progress-indeterminate progress-secondary"></div>
</div>
<div class="progress w-56">
  <div class="progress-bar progress-indeterminate progress-accent"></div>
</div>
<div class="progress w-56">
  <div class="progress-bar progress-indeterminate progress-info"></div>
</div>
<div class="progress w-56">
  <div class="progress-bar progress-indeterminate progress-success"></div>
</div>
<div class="progress w-56">
  <div class="progress-bar progress-indeterminate progress-warning"></div>
</div>
<div class="progress w-56">
  <div class="progress-bar progress-indeterminate progress-error"></div>
</div>
{{< /code >}}

<!-- Stepped bars -->

{{< headname level="3" >}} Stepped bars {{< /headname >}}

Implement the component class `progress-step` for the steps of the progress bar according to the provided examples.

{{< code addClass="flex-col" >}}

<!-- Step variant 1 -->

<div class="flex max-w-40 items-center gap-x-1">
  <div class="progress-step bg-primary" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-primary/10" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-primary/10" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-primary/10" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <p class="text-xs text-primary ms-1 font-medium">25%</p>
</div>

<!-- Step variant 1.1 -->

<div class="flex items-center gap-x-1">
  <div class="progress-step bg-primary" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-primary/10" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-primary/10" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-primary/10" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <p class="text-xs text-primary ms-1 font-medium">25%</p>
</div>

<!-- Step variant 2 -->

<div class="flex max-w-40 items-center gap-x-1">
  <div class="progress-step bg-warning" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-warning" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
  <p class="text-xs text-warning ms-1 font-medium">50%</p>
</div>

<!-- Step variant 2.1 -->

<div class="flex items-center gap-x-1">
  <div class="progress-step bg-warning" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-warning" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
  <p class="text-xs text-warning ms-1 font-medium">50%</p>
</div>

<!-- Step variant 3 -->

<div class="flex max-w-40 items-center gap-x-1">
  <div class="progress-step bg-success" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-success" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-success" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-success" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <p class="text-xs text-success ms-1 font-medium">100%</p>
</div>

<!-- Step variant 3.1 -->

<div class="flex items-center gap-x-1">
  <div class="progress-step bg-success" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-success" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-success" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <div class="progress-step bg-success" role="progressbar" aria-label="Progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" ></div>
  <p class="text-xs text-success ms-1 font-medium">100%</p>
</div>

<!-- Step variant 4 -->

<div class="flex max-w-40 items-center gap-x-1">
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <p class="size-6"><span class="icon-[tabler--circle-check-filled] text-info size-6"></span></p>
</div>

<!-- Step variant 4.1 -->

<div class="flex items-center gap-x-1">
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-step bg-info" role="progressbar" aria-label="Progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
  <p class="size-6"><span class="icon-[tabler--circle-check-filled] text-info size-6"></span></p>
</div>
{{< /code >}}
