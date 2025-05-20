---
title: "Stepper"
description: "The Stepper Component visually guides users through multi-step processes, such as wizards or forms, displaying their current position and remaining steps."
bg_image: "svg/navigations/stepper.svg"
components: 3
menu:
  main:
    parent: "navigations"

previous: Sidebar
previousLink: navigations/sidebar/

next: Tabs & Pills
nextLink: navigations/tabs-pills/

requires_js: true

pageJS:
  - "/js/pages/stepper.js"
---

{{< callout "info" >}}
Stepper components are adopted from <a href="https://preline.co/docs/stepper.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class Table -->

{{< class-table >}}
`stepper-active:{tw-utility-class}` | variant | Refines the appearance of the active step.  
`stepper-success:{tw-utility-class}` | variant | Adjusts the visual representation of a completed step.  
`stepper-disabled:{tw-utility-class}` | variant | Alters the "back" button appearance when the first step is active.  
`stepper-skipped:{tw-utility-class}` | variant | Modifies the appearance of a step that has been skipped.  
`stepper-error:{tw-utility-class}` | variant | Adjusts the visual representation of a step with an error. Requires manual addition.
`stepper-process:{tw-utility-class}` | variant | Modifies the appearance of a step that is currently being processed. Requires manual addition.
`stepper-completed:{tw-utility-class}` | variant | Refines the appearance of all steps that have been completed.  
{{< /class-table >}}

<!-------------------- Basic -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Static -->

{{< headname level="3" >}} Static {{< /headname >}}

A static stepper usage.

{{< code >}}

<ul class="relative flex w-full gap-x-2">
  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        1
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        2
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        3
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>
</ul>
{{< /code >}}

<!-- Vertical -->

{{< headname level="3" >}} Vertical {{< /headname >}}

Vertical navigation example.

{{< code addClass="!block" >}}

<ul class="relative flex h-96 flex-col gap-y-2">
  <li class="group flex flex-1 shrink basis-0 flex-col w-fit">
    <div class="flex items-center justify-center gap-2.5 text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        1
      </span>
      <div class="text-base-content block">Step</div>
    </div>
    <div class="bg-neutral/20 ms-3.5 mt-2 h-full w-px justify-self-start group-last:hidden"></div>
  </li>

  <li class="group flex flex-1 shrink basis-0 flex-col w-fit">
    <div class="flex items-center justify-center gap-2.5 text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        2
      </span>
      <div class="text-base-content block">Step</div>
    </div>
    <div class="bg-neutral/20 ms-3.5 mt-2 h-full w-px justify-self-start group-last:hidden"></div>
  </li>

  <li class="group flex flex-1 shrink basis-0 flex-col w-fit">
    <div class="flex items-center justify-center gap-2.5 text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        3
      </span>
      <div class="text-base-content block">Step</div>
    </div>
    <div class="bg-neutral/20 ms-3.5 mt-2 h-full w-px justify-self-start group-last:hidden"></div>
  </li>
</ul>
{{< /code >}}

<!-- Linear -->

{{< headname level="3" >}} Linear {{< /headname >}}

Linear navigation example.

{{< code >}}

<ul class="relative flex w-full gap-x-2">
  <li class="group flex flex-1 shrink basis-0 items-center gap-x-2">
    <div class="min-h-7.5 min-w-7.5 inline-flex items-center justify-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        1
      </span>
      <span class="text-base-content ms-2 block max-sm:hidden">Step</span>
    </div>
    <div class="bg-neutral/20 h-px w-full flex-1 group-last:hidden"></div>
  </li>

  <li class="group flex flex-1 shrink basis-0 items-center gap-x-2">
    <div class="min-h-7.5 min-w-7.5 inline-flex items-center justify-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        2
      </span>
      <span class="text-base-content ms-2 block max-sm:hidden">Step</span>
    </div>
    <div class="bg-neutral/20 h-px w-full flex-1 group-last:hidden"></div>
  </li>

  <li class="group flex flex-1 shrink basis-0 items-center gap-x-2">
    <div class="min-h-7.5 min-w-7.5 inline-flex items-center justify-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        3
      </span>
      <span class="text-base-content ms-2 block max-sm:hidden">Step</span>
    </div>
    <div class="bg-neutral/20 h-px w-full flex-1 group-last:hidden"></div>
  </li>
</ul>
{{< /code >}}

<!-------------------- Types -------------------->

{{< headname level="2" >}} Types {{< /headname >}}

<!-- Outlined -->

{{< headname level="3" >}} Outlined {{< /headname >}}

Outlined stepper example.

{{< code >}}

<ul class="relative flex w-full gap-x-2">
  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="border border-neutral-200 text-base-content size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        1
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="border border-neutral-200 text-base-content size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        2
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="border border-neutral-200 text-base-content size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        3
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>
</ul>
{{< /code >}}

<!-- Solid -->

{{< headname level="3" >}} Solid {{< /headname >}}

Solid stepper example.

{{< code >}}

<ul class="relative flex w-full gap-x-2">
  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        1
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        2
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        3
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>
</ul>
{{< /code >}}

<!-------------------- Shapes -------------------->

{{< headname level="2" >}} Shapes {{< /headname >}}

<!-- Rounded -->

{{< headname level="3" >}} Rounded {{< /headname >}}

Use the `rounded-*` utility class to make stepper rounded. The default shape of the stepper but can be altered by using TailwindCSS <a href="https://tailwindcss.com/docs/border-radius" target="_blank" class="link link-primary">Border Radius</a> utility classes.

{{< code >}}

<ul class="relative flex w-full gap-x-2">
  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-field text-sm font-medium" >
        1
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-field text-sm font-medium" >
        2
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-field text-sm font-medium" >
        3
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>
</ul>
{{< /code >}}

<!-- Circle (Default) -->

{{< headname level="3" >}} Circle (Default) {{< /headname >}}

This is the default stepper.

{{< code >}}

<ul class="relative flex w-full gap-x-2">
  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        1
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        2
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        3
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>
</ul>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Alignment center -->

{{< headname level="3" >}} Alignment center {{< /headname >}}

Navigation align centered.

{{< code >}}

<ul class="relative mx-auto flex w-96 gap-x-2">
  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        1
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        2
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>

  <li class="group flex-1 shrink basis-0">
    <div class="min-h-7.5 min-w-7.5 inline-flex w-full items-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full text-sm font-medium" >
        3
      </span>
      <div class="bg-neutral/20 ms-2 h-px w-full flex-1 group-last:hidden"></div>
    </div>
    <div class="mt-2.5">
      <span class="text-base-content block">Step</span>
    </div>
  </li>
</ul>
{{< /code >}}

<!-- Utilizing icons and avatars -->

{{< headname level="3" >}} Utilizing icons and avatars {{< /headname >}}

You can also include extra elements like an avatar image or icons.

{{< code >}}

<!-- Stepper -->
<ul class="relative flex w-full gap-x-2">
  <!-- Item -->
  <li class="group flex flex-1 shrink basis-0 items-center gap-x-2">
    <div class="min-h-7.5 min-w-7.5 inline-flex items-center justify-center align-middle text-sm">
      <img class="size-7.5 shrink-0 rounded-full" src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="Image Description" />
      <span class="text-base-content ms-2 block max-sm:hidden">Step</span>
    </div>
    <div class="bg-neutral/20 h-px w-full flex-1 group-last:hidden"></div>
  </li>
  <!-- End Item -->

  <!-- Item -->
  <li class="group flex flex-1 shrink basis-0 items-center gap-x-2">
    <div class="min-h-7.5 min-w-7.5 inline-flex items-center justify-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        <span class="icon-[tabler--arrow-bear-left-2] size-4 shrink-0"></span>
      </span>
      <span class="text-base-content ms-2 block max-sm:hidden">Step</span>
    </div>
    <div class="bg-neutral/20 h-px w-full flex-1 group-last:hidden"></div>
  </li>
  <!-- End Item -->

  <!-- Item -->
  <li class="group flex flex-1 shrink basis-0 items-center gap-x-2">
    <div class="min-h-7.5 min-w-7.5 inline-flex items-center justify-center align-middle text-sm">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        <span class="text-primary inline-block size-4 animate-spin rounded-full border-[3px] border-current border-t-transparent" role="status" aria-label="loading" >
          <span class="sr-only">Loading...</span>
        </span>
      </span>
      <span class="text-base-content ms-2 block max-sm:hidden">Step</span>
    </div>
    <div class="bg-neutral/20 h-px w-full flex-1 group-last:hidden"></div>
  </li>
  <!-- End Item -->
</ul>
<!-- End Stepper -->
{{< /code >}}
<!-------------------- Responsive -------------------->
{{< headname level="2" >}} Responsive {{< /headname >}}

<!-- Static -->

{{< headname level="3" >}} Static {{< /headname >}}

This stepper navigation example aligns horizontally for screen sizes above the `md` breakpoint and vertically for smaller screen sizes.

{{< code >}}

<!-- Stepper -->
<ul class="relative flex w-full flex-col gap-2 md:flex-row">
  <!-- Item -->
  <li class="group flex flex-1 gap-x-2 md:block md:shrink md:basis-0">
    <div class="min-h-7.5 min-w-7.5 flex flex-col items-center align-middle text-sm md:inline-flex md:w-full md:flex-row md:flex-wrap" >
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        1
      </span>
      <div class="bg-neutral/20 mt-2 h-full w-px group-last:hidden md:ms-2 md:mt-0 md:h-px md:w-full md:flex-1"></div>
    </div>
    <div class="grow pb-5 md:mt-2.5 md:grow-0">
      <span class="text-base-content block">Step</span>
      <p class="text-base-content/50 text-sm">This is a description text.</p>
    </div>
  </li>
  <!-- End Item -->

  <!-- Item -->
  <li class="group flex flex-1 gap-x-2 md:block md:shrink md:basis-0">
    <div class="min-h-7.5 min-w-7.5 flex flex-col items-center align-middle text-sm md:inline-flex md:w-full md:flex-row md:flex-wrap" >
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        2
      </span>
      <div class="bg-neutral/20 mt-2 h-full w-px group-last:hidden md:ms-2 md:mt-0 md:h-px md:w-full md:flex-1"></div>
    </div>
    <div class="grow pb-5 md:mt-2.5 md:grow-0">
      <span class="text-base-content block">Step</span>
      <p class="text-base-content/50 text-sm">This is a description text.</p>
    </div>
  </li>
  <!-- End Item -->

  <!-- Item -->
  <li class="group flex flex-1 gap-x-2 md:block md:shrink md:basis-0">
    <div class="min-h-7.5 min-w-7.5 flex flex-col items-center align-middle text-sm md:inline-flex md:w-full md:flex-row md:flex-wrap" >
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        3
      </span>
      <div class="bg-neutral/20 mt-2 h-full w-px group-last:hidden md:ms-2 md:mt-0 md:h-px md:w-full md:flex-1"></div>
    </div>
    <div class="grow pb-5 md:mt-2.5 md:grow-0">
      <span class="text-base-content block">Step</span>
      <p class="text-base-content/50 text-sm">This is a description text.</p>
    </div>
  </li>
  <!-- End Item -->
</ul>
<!-- End Stepper -->
{{< /code >}}

<!-- Linear -->

{{< headname level="3" >}} Linear {{< /headname >}}

The linear example is horizontally aligned for resolutions larger than or equal to 'md' and vertically aligned for resolutions below that.

{{< code >}}

<!-- Stepper -->
<ul class="relative flex w-full flex-col gap-2 md:flex-row">
  <!-- Item -->
  <li class="group flex flex-1 shrink basis-0 flex-col gap-x-2 md:flex-row md:items-center">
    <div class="min-h-7.5 min-w-7.5 inline-flex grow items-center align-middle text-sm md:grow-0">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        1
      </span>
      <span class="text-base-content ms-2 block grow md:grow-0">Step</span>
    </div>
    <div class="bg-neutral/20 ms-3.5 mt-2 h-4 w-px group-last:hidden md:ms-0 md:mt-0 md:h-px md:w-full md:flex-1" ></div>
  </li>
  <!-- End Item -->

  <!-- Item -->
  <li class="group flex flex-1 shrink basis-0 flex-col gap-x-2 md:flex-row md:items-center">
    <div class="min-h-7.5 min-w-7.5 inline-flex grow items-center align-middle text-sm md:grow-0">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        2
      </span>
      <span class="text-base-content ms-2 block grow md:grow-0">Step</span>
    </div>
    <div class="bg-neutral/20 ms-3.5 mt-2 h-4 w-px group-last:hidden md:ms-0 md:mt-0 md:h-px md:w-full md:flex-1" ></div>
  </li>
  <!-- End Item -->

  <!-- Item -->
  <li class="group flex flex-1 shrink basis-0 flex-col gap-x-2 md:flex-row md:items-center">
    <div class="min-h-7.5 min-w-7.5 inline-flex grow items-center align-middle text-sm md:grow-0">
      <span class="text-bg-soft-neutral size-7.5 flex shrink-0 items-center justify-center rounded-full font-medium" >
        3
      </span>
      <span class="text-base-content ms-2 block grow md:grow-0">Step</span>
    </div>
    <div class="bg-neutral/20 ms-3.5 mt-2 h-4 w-px group-last:hidden md:ms-0 md:mt-0 md:h-px md:w-full md:flex-1" ></div>
  </li>
  <!-- End Item -->
</ul>
<!-- End Stepper -->
{{< /code >}}

<!-------------------- Dynamic form -------------------->

{{< headname level="2" >}} Dynamic form {{< /headname >}}

<!-- Dynamic linear -->

{{< headname level="3" >}} Dynamic linear {{< /headname >}}

An example of a dynamic stepper that walks users through the steps of a task.

The Stepper component is a user interface element designed to guide users through a multi-step process. It features navigation items representing each step and content sections corresponding to these steps. The main data attribute, `data-stepper`, initializes the stepper component and ensures it functions correctly.

Within the stepper, `data-stepper-nav-item` and `data-stepper-content-item` attributes are used to link each step with its respective content, identified by an `index`. This index uniquely associates each navigation item with its corresponding content section.

Additionally, `data-stepper-back-btn` and `data-stepper-next-btn` control the navigation between steps, `data-stepper-finish-btn` is used to complete the process on the final step, and `data-stepper-reset-btn` allows users to reset the stepper. These data attributes work together to provide a smooth and guided user experience through the multi-step process.

{{< code >}}

<!-- Stepper -->
<div data-stepper="" class="w-full">
  <!-- Stepper Nav -->
  <ul class="relative flex flex-row gap-x-2">
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 1 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">1</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 2 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">2</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 3 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">3</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <!-- End Item -->
  </ul>
  <!-- End Stepper Nav -->

  <!-- Stepper Content -->
  <div class="mt-5 sm:mt-8">
    <!-- First Content -->
    <div data-stepper-content-item='{ "index": 1 }'>
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">First content</h3>
      </div>
    </div>
    <!-- End First Content -->
    <!-- Second Content -->
    <div data-stepper-content-item='{ "index": 2 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Second content</h3>
      </div>
    </div>
    <!-- End Second Content -->
    <!-- Third Content -->
    <div data-stepper-content-item='{ "index": 3 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Third content</h3>
      </div>
    </div>
    <!-- End Third Content -->
    <!-- Final Content -->
    <div data-stepper-content-item='{ "isFinal": true }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Final content</h3>
      </div>
    </div>
    <!-- End Final Content -->
    <!-- Button Group -->
    <div class="mt-5 flex items-center justify-between gap-x-2">
      <button type="button" class="btn btn-primary" data-stepper-back-btn="">
        <span class="icon-[tabler--chevron-left] text-primary-content rtl:rotate-180"></span>
        Back
      </button>
      <button type="button" class="btn btn-primary" data-stepper-next-btn="">
        Next
        <span class="icon-[tabler--chevron-right] text-primary-content rtl:rotate-180"></span>
      </button>
      <button type="button" class="btn btn-primary" data-stepper-finish-btn="" style="display: none;"> Finish </button>
      <button type="reset" class="btn btn-primary" data-stepper-reset-btn="" style="display: none;"> Reset </button>
    </div>
    <!-- End Button Group -->
  </div>
  <!-- End Stepper Content -->
</div>
<!-- End Stepper -->
{{< /code >}}

<!-- Non-linear -->

{{< headname level="3" >}} Non-linear {{< /headname >}}

Featuring a "Complete Step" button, the Stepper component can be enhanced with `"mode": "non-linear"` in the `data-stepper` attribute, allowing users to click on navigation items to switch steps. The `data-stepper-complete-step-btn` attribute is used for the complete button.

{{< code >}}

<!-- Stepper -->
<div data-stepper='{ "mode": "non-linear" }' class="w-full" >
  <!-- Stepper Nav -->
  <ul class="relative flex flex-row gap-x-2">
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 1 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">1</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 2 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">2</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 3 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">3</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <!-- End Item -->
  </ul>
  <!-- End Stepper Nav -->

  <!-- Stepper Content -->
  <div class="mt-5 sm:mt-8">
    <!-- First Content -->
    <div data-stepper-content-item='{ "index": 1 }'>
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">First content</h3>
      </div>
    </div>
    <!-- End First Content -->
    <!-- Second Content -->
    <div data-stepper-content-item='{ "index": 2 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Second content</h3>
      </div>
    </div>
    <!-- End Second Content -->
    <!-- Third Content -->
    <div data-stepper-content-item='{ "index": 3 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Third content</h3>
      </div>
    </div>
    <!-- End Third Content -->
    <!-- Final Content -->
    <div data-stepper-content-item='{ "isFinal": true }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Final content</h3>
      </div>
    </div>
    <!-- End Final Content -->
    <!-- Button Group -->
    <div class="mt-5 flex items-center justify-center sm:justify-between gap-x-2">
      <button type="button" class="btn btn-primary" data-stepper-back-btn="">
        <span class="icon-[tabler--chevron-left] text-primary-content rtl:rotate-180"></span>
        <span class="max-sm:hidden">Back</span>
      </button>
      <button type="button" class="btn btn-primary" data-stepper-complete-step-btn=' { "completedText": "This step is completed" }' >
        Complete Step
      </button>
      <button type="button" class="btn btn-primary" data-stepper-next-btn="">
        <span class="max-sm:hidden">Next</span>
        <span class="icon-[tabler--chevron-right] text-primary-content rtl:rotate-180"></span>
      </button>
      <button type="button" class="btn btn-primary" data-stepper-finish-btn="" style="display: none;"> Finish </button>
      <button type="reset" class="btn btn-primary" data-stepper-reset-btn="" style="display: none;"> Reset </button>
    </div>
    <!-- End Button Group -->
  </div>
  <!-- End Stepper Content -->
</div>
<!-- End Stepper -->
{{< /code >}}

<!-- Skip -->

{{< headname level="3" >}} Skip {{< /headname >}}

Example of a Step with a Skip Button: To incorporate a skip button, utilize `data-stepper-skip-btn` to designate the button that allows skipping the step. Specify the index for this button by including `data-stepper-nav-item='{ "isOptional": true }'`.

{{< code >}}

<!-- Stepper -->
<div data-stepper="" class="w-full">
  <!-- Stepper Nav -->
  <ul class="relative flex flex-row gap-x-2">
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 1,  "isOptional": true }' >
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">1</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 2,  "isOptional": true }' >
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">2</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 3 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">3</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <!-- End Item -->
  </ul>
  <!-- End Stepper Nav -->

  <!-- Stepper Content -->
  <div class="mt-5 sm:mt-8">
    <!-- First Content -->
    <div data-stepper-content-item='{ "index": 1 }'>
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">First content</h3>
      </div>
    </div>
    <!-- End First Content -->
    <!-- Second Content -->
    <div data-stepper-content-item='{ "index": 2 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Second content</h3>
      </div>
    </div>
    <!-- End Second Content -->
    <!-- Third Content -->
    <div data-stepper-content-item='{ "index": 3 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Third content</h3>
      </div>
    </div>
    <!-- End Third Content -->
    <!-- Final Content -->
    <div data-stepper-content-item='{ "isFinal": true }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Final content</h3>
      </div>
    </div>
    <!-- End Final Content -->
    <!-- Button Group -->
    <div class="mt-5 flex items-center justify-center sm:justify-between gap-x-2">
      <button type="button" class="btn btn-primary" data-stepper-back-btn="">
        <span class="icon-[tabler--chevron-left] text-primary-content rtl:rotate-180"></span>
        Back
      </button>
      <button type="button" class="btn btn-primary" data-stepper-skip-btn="" style="display: none;"> Skip </button>
      <button type="button" class="btn btn-primary" data-stepper-next-btn="">
        Next
        <span class="icon-[tabler--chevron-right] text-primary-content rtl:rotate-180"></span>
      </button>
      <button type="button" class="btn btn-primary" data-stepper-finish-btn="" style="display: none;"> Finish </button>
      <button type="reset" class="btn btn-primary" data-stepper-reset-btn="" style="display: none;"> Reset </button>
    </div>
    <!-- End Button Group -->
  </div>
  <!-- End Stepper Content -->
</div>
<!-- End Stepper -->
{{< /code >}}

<!-- Active -->

{{< headname level="3" >}} Active {{< /headname >}}

Active stepper example.

{{< code >}}

<!-- Stepper -->
<div data-stepper='{ "currentIndex": 2 }' class="w-full">
  <!-- Stepper Nav -->
  <ul class="relative flex flex-row gap-x-2">
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 1,  "isCompleted": true }' >
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">1</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 2 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">2</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 3 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">3</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <!-- End Item -->
  </ul>
  <!-- End Stepper Nav -->

  <!-- Stepper Content -->
  <div class="mt-5 sm:mt-8">
    <!-- First Content -->
    <div data-stepper-content-item='{ "index": 1 }'>
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">First content</h3>
      </div>
    </div>
    <!-- End First Content -->
    <!-- Second Content -->
    <div data-stepper-content-item='{ "index": 2 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Second content</h3>
      </div>
    </div>
    <!-- End Second Content -->
    <!-- Third Content -->
    <div data-stepper-content-item='{ "index": 3 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Third content</h3>
      </div>
    </div>
    <!-- End Third Content -->
    <!-- Final Content -->
    <div data-stepper-content-item='{ "isFinal": true }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Final content</h3>
      </div>
    </div>
    <!-- End Final Content -->
    <!-- Button Group -->
    <div class="mt-5 flex items-center justify-between gap-x-2">
      <button type="button" class="btn btn-primary" data-stepper-back-btn="">
        <span class="icon-[tabler--chevron-left] text-primary-content rtl:rotate-180"></span>
        Back
      </button>
      <button type="button" class="btn btn-primary" data-stepper-next-btn="">
        Next
        <span class="icon-[tabler--chevron-right] text-primary-content rtl:rotate-180"></span>
      </button>
      <button type="button" class="btn btn-primary" data-stepper-finish-btn="" style="display: none;"> Finish </button>
      <button type="reset" class="btn btn-primary" data-stepper-reset-btn="" style="display: none;"> Reset </button>
    </div>
    <!-- End Button Group -->
  </div>
  <!-- End Stepper Content -->
</div>
<!-- End Stepper -->
{{< /code >}}

<!-- Success -->

{{< headname level="3" >}} Success {{< /headname >}}

Example of a Successful Stepper: This example demonstrates what a properly completed stepper should look like.

{{< code >}}

<!-- Stepper -->
<div data-stepper='{ "isCompleted": true }' class="completed w-full" >
  <!-- Stepper Nav -->
  <ul class="relative flex flex-row gap-x-2">
    <li class="is-valid group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 1,  "isCompleted": true }' >
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">1</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="is-valid group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 2,  "isCompleted": true }' >
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">2</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="is-valid group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 3,  "isCompleted": true }' >
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">3</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <!-- End Item -->
  </ul>
  <!-- End Stepper Nav -->

  <!-- Stepper Content -->
  <div class="mt-5 sm:mt-8">
    <!-- First Content -->
    <div data-stepper-content-item='{ "index": 1,  "isCompleted": true }'>
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">First content</h3>
      </div>
    </div>
    <!-- End First Content -->
    <!-- Second Content -->
    <div data-stepper-content-item='{ "index": 2,  "isCompleted": true }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Second content</h3>
      </div>
    </div>
    <!-- End Second Content -->
    <!-- Third Content -->
    <div data-stepper-content-item='{ "index": 3,  "isCompleted": true }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Third content</h3>
      </div>
    </div>
    <!-- End Third Content -->
    <!-- Final Content -->
    <div data-stepper-content-item='{ "isFinal": true }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Final content</h3>
      </div>
    </div>
    <!-- End Final Content -->
    <!-- Button Group -->
    <div class="mt-5 flex items-center justify-between gap-x-2">
      <button type="button" class="btn btn-primary" data-stepper-back-btn="" style="display: none;">
        <span class="icon-[tabler--chevron-left] text-primary-content rtl:rotate-180"></span>
        Back
      </button>
      <button type="button" class="btn btn-primary" data-stepper-next-btn="" style="display: none;">
        Next
        <span class="icon-[tabler--chevron-right] text-primary-content rtl:rotate-180"></span>
      </button>
      <button type="button" class="btn btn-primary" data-stepper-finish-btn="" style="display: none;"> Finish </button>
      <button type="reset" class="btn btn-primary" data-stepper-reset-btn="">Reset</button>
    </div>
    <!-- End Button Group -->
  </div>
  <!-- End Stepper Content -->
</div>
<!-- End Stepper -->
{{< /code >}}

<!-- Error -->

{{< headname level="3" >}} Error {{< /headname >}}

Error stepper example.

{{< code jsCode="true" >}}

<!-- Stepper -->
<div id="error-stepper" data-stepper="" class="w-full">
  <!-- Stepper Nav -->
  <ul class="relative flex flex-row gap-x-2">
    <li class="is-invalid group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 1, "isInvalid": true  }' >
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error stepper-processed:bg-base-200 text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-error:hidden stepper-completed:hidden stepper-processed:hidden">
            1
          </span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
          <span class="icon-[tabler--x] stepper-error:block hidden size-4 shrink-0"></span>
          <span class="text-error stepper-processed:inline-block hidden size-4 animate-spin rounded-full border-[3px] border-current border-t-transparent" role="status" aria-label="loading" >
            <span class="sr-only">Loading...</span>
          </span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 2 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error stepper-processed:bg-base-200 text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-error:hidden stepper-completed:hidden stepper-processed:hidden">
            2
          </span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
          <span class="icon-[tabler--x] stepper-error:block hidden size-4 shrink-0"></span>
          <span class="text-error stepper-processed:inline-block hidden size-4 animate-spin rounded-full border-[3px] border-current border-t-transparent" role="status" aria-label="loading" >
            <span class="sr-only">Loading...</span>
          </span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 3 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error stepper-processed:bg-base-200 text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-error:hidden stepper-completed:hidden">3</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
          <span class="icon-[tabler--x] stepper-error:block hidden size-4 shrink-0"></span>
          <span class="text-error stepper-processed:inline-block hidden size-4 animate-spin rounded-full border-[3px] border-current border-t-transparent" role="status" aria-label="loading" >
            <span class="sr-only">Loading...</span>
          </span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <!-- End Item -->
  </ul>
  <!-- End Stepper Nav -->

  <!-- Stepper Content -->
  <div class="mt-5 sm:mt-8">
    <!-- First Content -->
    <div data-stepper-content-item='{ "index": 1 }'>
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">First content</h3>
      </div>
    </div>
    <!-- End First Content -->
    <!-- Second Content -->
    <div data-stepper-content-item='{ "index": 2 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Second content</h3>
      </div>
    </div>
    <!-- End Second Content -->
    <!-- Third Content -->
    <div data-stepper-content-item='{ "index": 3 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Third content</h3>
      </div>
    </div>
    <!-- End Third Content -->
    <!-- Final Content -->
    <div data-stepper-content-item='{ "isFinal": true }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Final content</h3>
      </div>
    </div>
    <!-- End Final Content -->
    <!-- Button Group -->
    <div class="mt-5 flex items-center justify-between gap-x-2">
      <button type="button" class="btn btn-primary" data-stepper-back-btn="">
        <span class="icon-[tabler--chevron-left] text-primary-content rtl:rotate-180"></span>
        Back
      </button>
      <button type="button" class="btn btn-primary" data-stepper-next-btn="">
        Next
        <span class="icon-[tabler--chevron-right] text-primary-content rtl:rotate-180"></span>
      </button>
      <button type="button" class="btn btn-primary" data-stepper-finish-btn="" style="display: none;"> Finish </button>
      <button type="reset" class="btn btn-primary" data-stepper-reset-btn="" style="display: none;"> Reset </button>
    </div>
    <!-- End Button Group -->
  </div>
  <!-- End Stepper Content -->
</div>
<!-- End Stepper -->

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    ;(function () {
      const errorStepper = HSStepper.getInstance('#error-stepper')
      let errorSuccessState = 1

      errorStepper.on('beforeNext', ind => {
        if (ind === 1) {
          errorStepper.setProcessedNavItem(ind)

          setTimeout(() => {
            errorStepper.unsetProcessedNavItem(ind)
            errorStepper.enableButtons()

            if (errorSuccessState) {
              errorStepper.goToNext()
            } else {
              errorStepper.setErrorNavItem(ind)
            }

            errorSuccessState = !errorSuccessState
          }, 2000)
        }
      })
    })()
  })
</script>

{{< /code >}}

<!-- Destroy/Reinitialize -->

{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}

The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a stepper element.

{{< code jsCode="true" >}}

<!-- Stepper -->
<div data-stepper="" id="stepper-to-destroy" class="w-full">
  <!-- Stepper Nav -->
  <ul class="relative flex flex-row gap-x-2">
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 1 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">1</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 2 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">2</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <li class="group flex flex-1 shrink basis-0 items-center gap-x-2" data-stepper-nav-item='{ "index": 3 }'>
      <span class="min-h-7.5 min-w-7.5 inline-flex items-center align-middle text-sm">
        <span class="stepper-active:text-bg-primary stepper-active:shadow-sm shadow-base-300/20 stepper-success:text-bg-primary stepper-success:shadow-sm stepper-completed:text-bg-success stepper-error:text-bg-error text-bg-soft-neutral flex size-7.5 shrink-0 items-center justify-center rounded-full font-medium" >
          <span class="stepper-success:hidden stepper-completed:hidden">3</span>
          <span class="icon-[tabler--check] stepper-success:block hidden size-4 shrink-0"></span>
        </span>
        <span class="text-base-content ms-2 max-sm:hidden">Step</span>
      </span>
      <div class="stepper-success:bg-primary stepper-completed:bg-success bg-neutral/20 h-px w-full flex-1 group-last:hidden" ></div>
    </li>
    <!-- End Item -->
  </ul>
  <!-- End Stepper Nav -->

  <!-- Stepper Content -->
  <div class="mt-5 sm:mt-8">
    <!-- First Content -->
    <div data-stepper-content-item='{ "index": 1 }'>
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">First content</h3>
      </div>
    </div>
    <!-- End First Content -->
    <!-- Second Content -->
    <div data-stepper-content-item='{ "index": 2 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Second content</h3>
      </div>
    </div>
    <!-- End Second Content -->
    <!-- Third Content -->
    <div data-stepper-content-item='{ "index": 3 }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Third content</h3>
      </div>
    </div>
    <!-- End Third Content -->
    <!-- Final Content -->
    <div data-stepper-content-item='{ "isFinal": true }' style="display: none;">
      <div class="border-base-content/40 bg-base-200/50 flex h-48 items-center justify-center rounded-xl border border-dashed p-4" >
        <h3 class="text-base-content/50 text-2xl">Final content</h3>
      </div>
    </div>
    <!-- End Final Content -->
    <!-- Button Group -->
    <div class="mt-5 flex items-center justify-between gap-x-2">
      <button type="button" class="btn btn-primary" data-stepper-back-btn="">
        <span class="icon-[tabler--chevron-left] text-primary-content rtl:rotate-180"></span>
        Back
      </button>
      <button type="button" class="btn btn-primary" data-stepper-next-btn="">
        Next
        <span class="icon-[tabler--chevron-right] text-primary-content rtl:rotate-180"></span>
      </button>
      <button type="button" class="btn btn-primary" data-stepper-finish-btn="" style="display: none;"> Finish </button>
      <button type="reset" class="btn btn-primary" data-stepper-reset-btn="" style="display: none;"> Reset </button>
    </div>
    <!-- End Button Group -->
  </div>
  <!-- End Stepper Content -->
</div>
<!-- End Stepper -->

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    ;(function () {
      const stepper = document.querySelector('#stepper-to-destroy')
      const destroy = document.querySelector('#destroy-btn')
      const reinit = document.querySelector('#reinit-btn')

      destroy.addEventListener('click', () => {
        const { element } = HSStepper.getInstance(stepper, true)

        element.destroy()

        destroy.setAttribute('disabled', 'disabled')
        reinit.removeAttribute('disabled')
      })

      reinit.addEventListener('click', () => {
        HSStepper.autoInit()

        reinit.setAttribute('disabled', 'disabled')
        destroy.removeAttribute('disabled')
      })
    })()
  });
</script>

{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/stepper.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Options table -->

{{< table >}}
PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-stepper`</span>| <span class="text-pretty">Activate a Stepper by specifying on an element. | `-` |`-`
<span class="text-nowrap">`data-stepper-nav-item`</span> | Activate a Stepper Nav Item by specifying on an element. | `-` | `-`  
<span class="text-nowrap">`data-stepper-content-item`</span> | Activate a Stepper Content Item by specifying on an element. | `-` | `-`
<span class="text-nowrap">`data-stepper-back-btn`</span>| Enables the Back button functionality on the specified element.| `-` | `-`
<span class="text-nowrap">`data-stepper-next-btn`</span>| Enables the Next button functionality on the specified element.| `-` | `-`
<span class="text-nowrap">`data-stepper-finish-btn`</span>| Enables the Finish button functionality on the specified element.| `-` | `-`
<span class="text-nowrap">`data-stepper-reset-btn`</span>| Enables the Reset button functionality on the specified element.| `-` | `-`
<span class="text-nowrap">`data-stepper-skip-btn`</span>| Enables the Skip button functionality on the specified element.| `-` | `-`
<span class="text-nowrap">`data-stepper-complete-step-btn`</span>| Enables the Complete button functionality on the specified element.| `-` | `-`
`:currentIndex` | Index of the current step. Must be a number between 1 and the maximum number of steps. | number | `1`  
`:mode` | Mode of the stepper. In "non-linear" mode, users can navigate to any step. | "linear" \ "non-linear" | "linear"  
`:index` | Index of the step to which the item belongs. Must be a number between 1 and the maximum steps. | `-` | `-`  
`:isOptional` | Whether the step is optional. | boolean | `false`  
`:isSkip` | Whether the step is skipped. | boolean | `false`  
`:isInvalid` | Whether the step has an error. | boolean | `false`    
`:isCompleted` | Whether the step is completed. | boolean | `false`  
`:isFinal` | Whether the step is final. | boolean | `false`  
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSStepper` object is contained within the global `window` object

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`setProcessedNavItem(n)`| Set the nav item as processed. Available parameters: <ul><li>`n` the index of the step to which the item belongs</li></ul>
`setErrorNavItem(n)` | Set the nav item as error. Available parameters:<ul><li>`n` the index of the step to which the item belongs</li></ul>
`unsetProcessedNavItem(n)` | Unset the nav item as processed. Available parameters:<ul><li>`n` the index of the step to which the item belongs</li></ul>
`goToNext()`| Moves to the next step. Returns the index of the next step. If already at the last step, returns the current step's index.
`disableButtons()` | Disable the "next" and "back" buttons.
`enableButtons()` | Enable the "next" and "back" buttons.
`destroy()`| Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">Private METHODS</span>
`handleFinishButtonClick()` | Handles the click event to proceed to the finish.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSStepper.getInstance(target, isInstance)` | <div>Retrieves the associated element. Parameters <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
{{< /table >}}

<p class="mt-10 mb-1.5 not-prose">Randomize an error state (public method).</p>

{{< code-highlight lang="js" >}}const stepper = new HSStepper(document.querySelector('#stepper'));
let invalidState = 1;

stepper.on('beforeNext', (index) => {
  if (index === 1) {
    stepper.setProcessedNavItem(index);

    setTimeout(() => {
      stepper.unsetProcessedNavItem(index);
      stepper.enableButtons();

      if (invalidState) {
        stepper.goToNext();
      } else {
        stepper.setErrorNavItem(index);
      }

      invalidState = !invalidState;
    }, 2000);
  }
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose">Randomize an error state (mixed).</p>

{{< code-highlight lang="js" >}}const stepper = HSStepper.getInstance('#stepper');
let invalidState = 1;

stepper.on('beforeNext', (index) => {
  if (index === 2) {
    stepper.setProcessedNavItem(index);

    setTimeout(() => {
      stepper.unsetProcessedNavItem(index);
      stepper.enableButtons();

      if (invalidState) {
        stepper.goToNext();
      } else {
        stepper.setErrorNavItem(index);
      }
      invalidState = !invalidState;
    }, 2000);
  }
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose" id="destroy-method">Destroy Instance (public)</p>

{{< code-highlight lang="js" >}}const stepper = document.querySelector('#stepper-to-destroy')
const destroy = document.querySelector('#destroy-btn')

destroy.addEventListener('click', () => {
  const { element } = HSStepper.getInstance(stepper, true)
  element.destroy()
})
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION | RETURNING VALUE
`on:active` | Triggered when the "active" class is set. | `currentIndex`
`on:beforeNext` | Triggered before the "next" button is clicked. | `currentIndex`
`on:next` | Triggered when the "next" button is clicked. | `currentIndex`
`on:back` | Triggered when the "back" button is clicked. | `currentIndex`
`on:complete` | Triggered when the "complete" button is clicked. | `currentIndex`
`on:beforeFinish` | Triggered before the "finish" button is clicked. | `currentIndex`
`on:finish` | Triggered when the "finish" button is clicked. | `currentIndex`
`on:skip` | Triggered when the "skip" button is clicked. | `currentIndex`
`on:reset` | Triggered when the "reset" button is clicked. | `currentIndex`
{{< /table >}}

<!-- //TODO - Uncomment when we have solved the formvalidation issue and provide valdiation in wizard -->
<!-- Event usage -->

<!-- {{< headname level="4" >}} Event usage {{< /headname >}} -->

{{< code-highlight lang="js" >}}const el = HSStepper.getInstance('#stepper');

el.on('next', (currentIndex) => {...});
{{< /code-highlight >}}
