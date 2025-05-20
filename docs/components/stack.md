---
title: "Stack"
components: 6
description: "Stack elements positions them on top of each other in a visual manner."
bg_image: "svg/components/stack.svg"
menu:
  main:
    parent: "components"

previous: Skeleton
previousLink: components/skeleton/

next: Stat
nextLink: components/stat/
---

<!-- Class table -->

{{< class-table >}}
stack | component | Stacks the child elements on top of each other.
stack-start | placement | Sets stacking direction to start.
stack-end | placement | Sets stacking direction to end.
stack-bottom-start | placement | Sets stacking direction to bottom-start.
stack-bottom-end | placement | Sets stacking direction to bottom-end.
stack-top | placement | Sets stacking direction to top.
stack-top-start | placement | Sets stacking direction to top-start.
stack-top-end | placement | Sets stacking direction to top-end.
stack-animated | placement | Adds animation to stack when hovered over.
{{< /class-table >}}

<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!--  Without stack  -->

{{< headname level="3" >}} Without stack {{< /headname >}}

The following example displays div's without stacking.

{{< code >}}

<div>
  <div class="bg-primary text-primary-content grid h-20 w-32 place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid h-20 w-32 place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid h-20 w-32 place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!--  With stack  -->

{{< headname level="3" >}} With stack {{< /headname >}}

Wrap the stacked div's with a wrapper div using the component class `stack`.

{{< code >}}

<div class="stack h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>  
</div>
{{< /code >}}

<!-- Animated stack  -->

{{< headname level="3" >}} Animated stack {{< /headname >}}

Apply the modifier class stack-animated to enable animation on hover.

{{< callout "info" >}}
The `stack-animated modifier` class is also applicable to stacks with various positions.
{{< /callout >}}

{{< code >}}

<div class="stack stack-bottom-start stack-animated h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!-------------------- Positions -------------------->

{{< headname level="2" >}} Positions {{< /headname >}}

<!-- Bottom (default)  -->

{{< headname level="3" >}} Bottom (default) {{< /headname >}}

By default, the stacking direction is from the bottom.

{{< code >}}

<div class="stack h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!-- Bottom start  -->

{{< headname level="3" >}} Bottom start {{< /headname >}}

Apply the modifier class `stack-bottom-start` to set the stack direction to bottom-start.

{{< code >}}

<div class="stack stack-bottom-start h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!--  Bottom end  -->

{{< headname level="3" >}} Bottom end {{< /headname >}}

Apply the modifier class `stack-bottom-end` to set the stack direction to bottom-end.

{{< code >}}

<div class="stack stack-bottom-end h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!-- Top  -->

{{< headname level="3" >}} Top {{< /headname >}}

Apply the modifier class `stack-top` to set the stack direction to top.

{{< code >}}

<div class="stack stack-top h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!-- Top start  -->

{{< headname level="3" >}} Top start {{< /headname >}}

Apply the modifier class `stack-top-start` to set the stack direction to top-start.

{{< code >}}

<div class="stack stack-top-start h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!-- Top end  -->

{{< headname level="3" >}} Top end {{< /headname >}}

Apply the modifier class `stack-top-end` to set the stack direction to stack-end.

{{< code >}}

<div class="stack stack-top-end h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!-- Start  -->

{{< headname level="3" >}} Start {{< /headname >}}

Apply the modifier class `stack-start` to set the stack direction to start.

{{< code >}}

<div class="stack stack-start h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!-- End  -->

{{< headname level="3" >}} End {{< /headname >}}

Apply the modifier class `stack-end` to set the stack direction to end.

{{< code >}}

<div class="stack stack-end h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>
</div>
{{< /code >}}

<!-- Illustrations -->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Stacked images  -->

{{< headname level="3" >}} Stacked images {{< /headname >}}

The example below demonstrates a stack with images.

{{< code >}}

<div class="stack w-32">
  <img src="https://cdn.flyonui.com/fy-assets/components/card/image-1.png" alt="iphone" class="rounded-sm" />
  <img src="https://cdn.flyonui.com/fy-assets/components/card/image-2.png" alt="sydney" class="rounded-sm" />
  <img src="https://cdn.flyonui.com/fy-assets/components/card/image-3.png" alt="rome" class="rounded-sm" />
</div>
{{< /code >}}

<!--  Stacked cards  -->

{{< headname level="3" >}} Stacked cards {{< /headname >}}

The example below demonstrates a stack with cards.

{{< code >}}

<div class="stack w-32">
  <div class="card border-base-content border shadow-none">
    <div class="card-body text-center">
      <p>Card A</p>
    </div>
  </div>
  <div class="card border-base-content border shadow-none">
    <div class="card-body text-center">
      <p>Card B</p>
    </div>
  </div>
  <div class="card border-base-content border shadow-none">
    <div class="card-body text-center">
      <p>Card C</p>
    </div>
  </div>
</div>
{{< /code >}}

<!--  notifications  -->

{{< headname level="3" >}} Stacked notifications {{< /headname >}}

The example below demonstrates a notifications stack.

{{< code >}}

<div class="stack stack-animated">
  <div class="card bg-primary text-primary-content shadow-none">
    <div class="card-body">
      <h5 class="card-title text-primary-content">3 Notifications</h5>
      <p>You have 3 unread messages. Tap here to see.</p>
    </div>
  </div>
  <div class="card bg-info text-info-content shadow-none">
    <div class="card-body">
      <h5 class="card-title text-info-content">2 Notifications</h5>
      <p>You have 2 unread messages. Tap here to see.</p>
    </div>
  </div>
  <div class="card bg-secondary text-secbg-secondary-content shadow-none">
    <div class="card-body">
      <h5 class="card-title text-secbg-secondary-content">Notification 1</h5>
      <p>You have an unread message. Tap here to see.</p>
    </div>
  </div>
</div>
{{< /code >}}
