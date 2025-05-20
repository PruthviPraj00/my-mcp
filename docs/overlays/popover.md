---
title: "Popover"
description: "Popovers provide contextual information and interactive features to enhance user interaction and understanding within an interface."
bg_image: "svg/overlays/popover.svg"
components: 9
menu:
  main:
    parent: "overlays"

previous: Modal
previousLink: overlays/modal/

next: Tooltip
nextLink: overlays/tooltip/

requires_js: true
---

{{< callout "info" >}}
Popover components are adopted from <a href="https://preline.co/docs/popover.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

> We leveraged <a href="https://floating-ui.com/" class="link link-primary font-semibold" target="blank">FloatingUI</a> to elevate our popover experience to the next level.

<!-- Class Table -->

{{< class-table >}}
tooltip | component | Base class for popover component.
tooltip-toggle | part | Base class for toggling the display of popover.
tooltip-content | part | Places for popover content with popper.
tooltip-body | part | Container for popover content.
tooltip-primary | color | Popover with 'primary' color.
tooltip-secondary | color | Popover with 'secondary' color.
tooltip-accent | color | Popover with 'accent' color.
tooltip-info | color | Popover with 'info' color.
tooltip-success | color | Popover with 'success' color.
tooltip-warning | color | Popover with 'warning' color.
tooltip-error | color | Popover with 'error' color.
tooltip-shown:{tw-utility-class} | variant | Adds specific tailwind classes when the popover is open.
{{< /class-table >}}

<!-------------------- Default -------------------->

{{< headname level="2" >}} Default {{< /headname >}}

<!-- Basic example -->

{{< headname level="3" >}} Basic example {{< /headname >}}

The popover component extends the functionality of the tooltip component by triggering upon click and enabling user interaction.

The example below demonstrates a default popover triggered upon a click event.

{{< code addClass="p-10" >}}

<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body bg-base-100 max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Colors -------------------->

{{< headname level="2" >}} Colors {{< /headname >}}

<!-- Semantic variants -->

{{< headname level="3" >}} Semantic variants {{< /headname >}}

Use modifier class `tooltip-{semantic-color}` with component class `tooltip-body` for colored popover.

{{< code addClass="gap-5" >}}

<!-- Primary popover -->
<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square btn-primary" aria-label="Primary Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body tooltip-primary max-w-xs rounded-lg p-4 text-start">
        <span class="text-lg font-medium">Popover title</span>
        <p class="text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
<!-- Secondary popover -->
<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square btn-secondary" aria-label="Secondary Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body tooltip-secondary max-w-xs rounded-lg p-4 text-start">
        <span class="text-lg font-medium">Popover title</span>
        <p class="text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
<!-- Accent popover -->
<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square btn-accent" aria-label="Accent Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body tooltip-accent max-w-xs rounded-lg p-4 text-start">
        <span class="text-lg font-medium">Popover title</span>
        <p class="text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
<!-- Info popover -->
<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square btn-info" aria-label="Info Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body tooltip-info max-w-xs rounded-lg p-4 text-start">
        <span class="text-lg font-medium">Popover title</span>
        <p class="text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
<!-- Success popover -->
<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square btn-success" aria-label="Success Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body tooltip-success max-w-xs rounded-lg p-4 text-start">
        <span class="text-lg font-medium">Popover title</span>
        <p class="text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
<!-- Warning popover -->
<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square btn-warning" aria-label="Warning Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body tooltip-warning max-w-xs rounded-lg p-4 text-start">
        <span class="text-lg font-medium">Popover title</span>
        <p class="text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
<!-- Error popover -->
<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square btn-error" aria-label="Error Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body tooltip-error max-w-xs rounded-lg p-4 text-start">
        <span class="text-lg font-medium">Popover title</span>
        <p class="text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Directions -------------------->

{{< headname level="2" >}} Directions {{< /headname >}}

<!-- Popover placements -->

{{< headname level="3" >}} Popover placements {{< /headname >}}

Utilize the JavaScript option class `[--placement:{direction}]` to specify the popover placement in various directions. Here, `direction` can be `top`, `bottom`, `left`, or `right`. By default, the popover is positioned at the `top`.

{{< code >}}

<!-- Left popover -->
<div class="tooltip [--trigger:click] [--placement:left]">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-left]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body bg-base-100 max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
<!-- Top popover (default) -->
<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body bg-base-100 max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
<!-- Bottom popover -->
<div class="tooltip [--placement:bottom] [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-down]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body bg-base-100 max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
<!-- Right popover -->
<div class="tooltip [--placement:right] [--trigger:click]">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-right]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body bg-base-100 max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Ratings & reviews -->

{{< headname level="3" >}} Ratings & reviews {{< /headname >}}

Below given example shows rating & reviews popover on click.

{{< code >}}

<div class="tooltip [--trigger:click]">
  <div class="tooltip-toggle">
    <p class="text-primary cursor-pointer select-none flex items-center gap-1">
      Ratings & reviews
      <span class="icon-[tabler--eye-closed] tooltip-shown:hidden"></span>
      <span class="icon-[tabler--eye] hidden tooltip-shown:inline-block"></span>
    </p>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible p-4" role="popover">
      <div class="tooltip-body bg-base-100 text-base-content/80 flex max-w-xs flex-col gap-1 rounded-lg p-4 text-start" >
        <div class="text-primary text-xl flex items-center gap-1 font-medium">
          4.35
          <span class="icon-[tabler--star-filled] size-5"></span>
        </div>
        <div class="text-base-content font-medium">Total 300 reviews</div>
        <p>All reviews are from genuine customers.</p>
        <div class="mt-4 flex items-center justify-between">
          <span class="badge badge-soft badge-primary rounded-full">+6 this week</span>
          <a href="#" class="link link-primary link-hover text-sm">See all</a>
        </div>
        <div class="divider my-2"></div>
        <div class="space-y-2">
          <div class="flex w-full items-center gap-2">
            <span class="text-sm text-nowrap font-medium leading-5">5 Star</span>
            <div class="progress" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
              <div class="progress-bar progress-primary w-3/4"></div>
            </div>
            <span class="text-sm font-medium leading-5">225</span>
          </div>
          <div class="flex w-full items-center gap-2">
            <span class="text-sm text-nowrap font-medium leading-5">4 Star</span>
            <div class="progress" role="progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">
              <div class="progress-bar progress-primary w-[10%]"></div>
            </div>
            <span class="text-sm font-medium leading-5">30</span>
          </div>
          <div class="flex w-full items-center gap-2">
            <span class="text-sm text-nowrap font-medium leading-5">3 Star</span>
            <div class="progress" role="progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">
              <div class="progress-bar progress-primary w-[10%]"></div>
            </div>
            <span class="text-sm font-medium leading-5">30</span>
          </div>
          <div class="flex w-full items-center gap-2">
            <span class="text-sm text-nowrap font-medium leading-5">2 Star</span>
            <div class="progress" role="progressbar" aria-valuenow="5" aria-valuemin="0" aria-valuemax="100">
              <div class="progress-bar progress-primary w-[5%]"></div>
            </div>
            <span class="text-sm font-medium leading-5">15</span>
          </div>
          <div class="flex w-full items-center gap-2">
            <span class="text-sm text-nowrap font-medium leading-5">1 Star</span>
            <div class="progress" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
              <div class="progress-bar progress-primary w-0"></div>
            </div>
            <span class="text-sm font-medium leading-5">00</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Options usage -------------------->

{{< headname level="2" >}} Options usage {{< /headname >}}

<!-- Trigger -->

{{< headname level="3" >}} Trigger {{< /headname >}}

Use the JavaScript option class `[--trigger:{event}]` to specify the event that opens the tooltip. The event options include `hover`, `focus`, or `click`. By default, the tooltip/popover is triggered on the `hover` event.

<!-- On focus -->

{{< headname level="4" >}} On focus {{< /headname >}}

Utilize the provided example to trigger the tooltip/popover on the `focus` event.

{{< code >}}

<div class="tooltip [--trigger:focus]">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body bg-base-100 max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base py-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
        {{< link link="overlays/tooltip/" addClass="link link-primary" >}}Click me{{< /link >}}
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- On Hover -->

{{< headname level="4" >}} On Hover {{< /headname >}}

Utilize the provided example to trigger the tooltip/popover on the `Hover` event.

{{< code >}}

<div class="tooltip">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body bg-base-100 max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base py-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
        {{< link link="overlays/tooltip/" addClass="link link-primary" >}}Click me{{< /link >}}
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Interaction -->

{{< headname level="3" >}} Interaction {{< /headname >}}

To enable interactivity within the tooltip or popover content, use the JavaScript option class `[--interaction:{boolean}]`. Setting this option to `false` disables interaction, causing the tooltip or popover to close when clicking inside `tooltip-content`. By default, it is set to `true`. Note that this class selector works exclusively with `[--trigger:focus]`.

The provided example disables interaction with the popover content.

{{< code >}}

<div class="tooltip [--trigger:focus] [--interaction:false]">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-up]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible " role="popover">
      <div class="tooltip-body bg-base-100 max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base py-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
        <a href="#" class="link link-primary">Click me</a>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Tooltip strategy -->

{{< headname level="3" >}} Tooltip strategy {{< /headname >}}

Use the JavaScript option class `[--strategy:{position}]` to determine the placement strategy of the tooltip/popover. The `position` parameter can be set to either `fixed` or `absolute`.

When set to `absolute`, the tooltip/popover will be positioned relative to its parent element with the `relative` class, thereby confining the popover/tooltip within that container. By default, the value is `fixed`.

The provided example showcases the behavior of tooltips/popovers when utilizing the absolute positioning strategy.

{{< code addClass="relative h-70 justify-center">}}

<div class="tooltip show [--trigger:click] [--strategy:absolute] [--placement:bottom]">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-down]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body bg-base-100 w-64 sm:max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Prevent popper -->

{{< headname level="3" >}} Prevent popper {{< /headname >}}

Use the JavaScript option class `[--prevent-popper:{boolean}]` to manage the placement calculation with Popper.

When set to `true`, Popper will be prevented from calculating its position, resulting in the tooltip/popover remaining static and ceasing recalculation if there is insufficient space upon scrolling. By default, its value is `false`.

The provided example showcases the behavior of tooltips/popovers when prevent-popper is set to `true`.

{{< code addClass="h-64" >}}

<div class="tooltip show [--trigger:click] [--placement:right-start] [--prevent-popper:true]">
  <div class="tooltip-toggle">
    <button class="btn btn-square" aria-label="Popover Button"><span class="icon-[tabler--chevron-down]"></span></button>
    <div class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="popover">
      <div class="tooltip-body bg-base-100 w-64 sm:max-w-xs rounded-lg p-4 text-start">
        <span class="text-base-content text-lg font-medium">Popover title</span>
        <p class="text-base-content/80 text-base pt-4">
          This text serves as placeholder content for the popover, showcasing its overall look in the user interface.
        </p>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

{{< callout "info" >}}
Please refer to the {{< link link="overlays/tooltip/#javascript-behavior" addClass="link link-primary" >}}Tooltip{{< /link >}} component documentation for JavaScript behavior in popover, since both tooltips and popovers utilize the tooltip plugin.
{{< /callout >}}
