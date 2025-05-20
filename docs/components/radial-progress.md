---
title: "Radial progress"
components: 5
description: "Radial progress can visually represent either the completion of a task or the elapsed passage of time."
bg_image: "svg/components/radial-progress.svg"
menu:
  main:
    parent: "components"

previous: Progress
previousLink: components/progress/

next: Remove element
nextLink: components/remove-element/
---

<!-- Class Table -->

{{< class-table >}}
radial-progress | component | Base class for radial progress component.
{{< /class-table >}}

{{< callout "info" >}}
<div>
  <p>The radial progress component requires the <code class="text-sm">--value</code> CSS variable to define its progress percentage.</p>
  <p>To adjust its size, use the <code class="text-sm">--size</code> CSS variable, which defaults to 5rem.</p>
  <p>To modify the thickness of the progress ring, use the <code class="text-sm">--thickness</code> CSS variable, which is set to 10% of the size by default.</p>
</div>
{{< /callout >}}


{{< callout "info" >}}
<div>
  <p> For Radial progress we need to use a <code class="text-sm">div</code> instead of the <code class="text-sm">progress</code> tag because browsers can’t show text inside <code class="text-sm">progress</code> tag, and Firefox doesn’t render pseudo-elements inside <code class="text-sm">progress</code> tag at all.</p>
  <p class="mt-1.5">Adding <code class="text-sm">role="progressbar"</code> makes it accessible to screen readers as well.</p>
</div>
{{< /callout >}}


<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Utilize the `radial-progress` component class and adjust the progress value by setting the CSS variable `--value:*` in
the style attribute of the radial progress component, where `*` represents a numerical value.

{{< code >}}

<div class="radial-progress" style="--value:75;" role="progressbar" aria-label="Radial Progress"></div>
{{< /code >}}

<!-- With values -->

{{< headname level="3" >}} With values {{< /headname >}}

Embed a value in the radial progress component markup to visualize the progress accordingly.

{{< code >}}

<div class="radial-progress" style="--value:0;" role="progressbar" aria-label="0% Radial Progressbar">0%</div>
<div class="radial-progress" style="--value:20;" role="progressbar" aria-label="20% Radial Progressbar">20%</div>
<div class="radial-progress" style="--value:60;" role="progressbar" aria-label="60% Radial Progressbar">60%</div>
<div class="radial-progress" style="--value:80;" role="progressbar" aria-label="80% Radial Progressbar">80%</div>
<div class="radial-progress" style="--value:100;" role="progressbar" aria-label="100% Radial Progressbar">100%</div>
{{< /code >}}

<!-- With text  -->

{{< headname level="3" >}} With text {{< /headname >}}

Embed a value & text in the radial progress component markup to visualize the radial progress with text.

{{< code >}}

<div class="radial-progress" style="--value:60;" role="progressbar" aria-label="60% Radial Progressbar">
  <div class="mx-auto">60%</div>
  <span class="text-secondary text-xs">Loss</span>
</div>
<div class="radial-progress" style="--value:80;" role="progressbar" aria-label="80% Radial Progressbar">
  <div class="mx-auto">80%</div>
  <span class="text-secondary text-xs">Profit</span>
</div>
{{< /code >}}

<!-- Colors -->

{{< headname level="2" >}} Colors {{< /headname >}}

<!-- Semantic -->

{{< headname level="3" >}} Semantic {{< /headname >}}

Apply the text utility class `text-{semantic-color}` to the radial progress to style it with semantic colors.

{{< code >}}

<div class="radial-progress text-neutral" style="--value:70;" role="progressbar" aria-label="Neutral Radial Progressbar">70%</div>
<div class="radial-progress text-primary" style="--value:70;" role="progressbar" aria-label="Primary Radial Progressbar">70%</div>
<div class="radial-progress text-secondary" style="--value:70;" role="progressbar" aria-label="Secondary Radial Progressbar">70%</div>
<div class="radial-progress text-accent" style="--value:70;" role="progressbar" aria-label="Accent Radial Progressbar">70%</div>
<div class="radial-progress text-info" style="--value:70;" role="progressbar" aria-label="Info Radial Progressbar">70%</div>
<div class="radial-progress text-success" style="--value:70;" role="progressbar" aria-label="Success Radial Progressbar">70%</div>
<div class="radial-progress text-warning" style="--value:70;" role="progressbar" aria-label="Warning Radial Progressbar">70%</div>
<div class="radial-progress text-error" style="--value:70;" role="progressbar" aria-label="Error Radial Progressbar">70%</div>
{{< /code >}}

<!-- With background -->

{{< headname level="3" >}} With background {{< /headname >}}

Utilize the provided examples to implement radial progress with semantic background colors.

{{< code >}}

<div class="radial-progress bg-neutral text-neutral-content border-neutral border-4" style="--value:70;" role="progressbar" aria-label="Neutral Radial Progressbar">70%</div>
<div class="radial-progress bg-primary text-primary-content border-primary border-4" style="--value:70;" role="progressbar" aria-label="Primary Radial Progressbar">70%</div>
<div class="radial-progress bg-secondary text-secondary-content border-secondary border-4"style="--value:70;"role="progressbar" aria-label="Secondary Radial Progressbar">70%</div>
<div class="radial-progress bg-accent text-accent-content border-accent border-4" style="--value:70;" role="progressbar" aria-label="Accent Radial Progressbar">70%</div>
<div class="radial-progress bg-info text-info-content border-info border-4" style="--value:70;" role="progressbar" aria-label="Info Radial Progressbar">70%</div>
<div class="radial-progress bg-success text-success-content border-success border-4" style="--value:70;" role="progressbar" aria-label="Success Radial Progressbar">70%</div>
<div class="radial-progress bg-warning text-warning-content border-warning border-4" style="--value:70;" role="progressbar" aria-label="Warning Radial Progressbar">70%</div>
<div class="radial-progress bg-error text-error-content border-error border-4" style="--value:70;" role="progressbar" aria-label="Error Radial Progressbar">70%</div>
{{< /code >}}

<!-- With soft background -->

{{< headname level="3" >}} With soft background {{< /headname >}}

Utilize the provided examples to implement radial progress with soft semantic background colors.

{{< code >}}

<div class="radial-progress bg-neutral/10 text-neutral border-4 border-transparent" style="--value:70;" role="progressbar" aria-label="Neutral Radial Progressbar">70%</div>
<div class="radial-progress bg-primary/10 text-primary border-4 border-transparent" style="--value:70;" role="progressbar" aria-label="Primary Radial Progressbar">70%</div>
<div class="radial-progress bg-secondary/10 text-secondary border-4 border-transparent" style="--value:70;" role="progressbar" aria-label="Secondary Radial Progressbar">70%</div>
<div class="radial-progress bg-accent/10 text-accent border-4 border-transparent" style="--value:70;" role="progressbar" aria-label="Accent Radial Progressbar">70%</div>
<div class="radial-progress bg-info/10 text-info border-4 border-transparent" style="--value:70;" role="progressbar" aria-label="Info Radial Progressbar">70%</div>
<div class="radial-progress bg-success/10 text-success border-4 border-transparent" style="--value:70;" role="progressbar" aria-label="Success Radial Progressbar">70%</div>
<div class="radial-progress bg-warning/10 text-warning border-4 border-transparent" style="--value:70;" role="progressbar" aria-label="Warning Radial Progressbar">70%</div>
<div class="radial-progress bg-error/10 text-error border-4 border-transparent" style="--value:70;" role="progressbar" aria-label="Error Radial Progressbar">70%</div>
{{< /code >}}

<!-------------------- Sizes -------------------->

{{< headname level="2" >}} Sizes {{< /headname >}}

<!-- Custom size & thickness -->

{{< headname level="3" >}} Custom size & thickness {{< /headname >}}

Modify the size and thickness of the progress by defining the CSS variables `--size:*` and `--thickness:*` within the style attribute of the radial progress component, where `*` denotes a numerical value along with the unit.

{{< code >}}

<div class="radial-progress" style="--value:70; --size:12rem; --thickness: 2px;" role="progressbar" aria-label="Radial Progressbar">70%</div>
<div class="radial-progress" style="--value:70; --size:12rem; --thickness: 2rem;" role="progressbar" aria-label="Radial Progressbar">70%</div>
<div class="radial-progress bg-primary/10 text-primary border-4 border-transparent" style="--value:70; --size:12rem; --thickness: 1rem;" role="progressbar" aria-label="Radial Progressbar">70%</div>
{{< /code >}}
