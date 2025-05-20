---
title: "Range"
description: "A range slider is used to modify a value by sliding a handle along a track, allowing for precise adjustments."
bg_image: "svg/form-elements/range.svg"
components: 1
menu:
  main:
    parent: "forms"

previous: Radio
previousLink: forms/radio/

next: Select
nextLink: forms/select/
---

<!-- Class table -->

{{< class-table >}}
range | component | Range input
range-primary | color | Adds 'primary' to range
range-secondary | color | Adds 'secondary' to range
range-accent | color | Adds 'accent' to range
range-info | color | Adds 'info' to range
range-success | color | Adds 'success' to range
range-warning | color | Adds 'warning' to range
range-error | color | Adds 'error' to range
range-xs | size | Extra small range
range-sm | size | Small range
range-md | size | Medium (Default) range
range-lg | size | Large range
range-xl | size | Extra Large range
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic input `range` example.

{{< code >}}
<input type="range" class="range" aria-label="range" />
{{< /code >}}

<!-------------------- Size -------------------->

{{< headname level="2" >}} Size {{< /headname >}}

<!-- Range sizes -->

{{< headname level="3" >}} Range sizes {{< /headname >}}

The Range inputs are stacked in three sizes:extra small `xs`, small `sm`, default, and large `lg`.

{{< code addClass="flex-col gap-6">}}
<input type="range" class="range range-xs" aria-label="range" />
<input type="range" class="range range-sm" aria-label="range" />
<input type="range" class="range" aria-label="range" />
<input type="range" class="range range-lg" aria-label="range" />
<input type="range" class="range range-xl" aria-label="range" />
{{< /code >}}

<!-------------------- Color  -------------------->

{{< headname level="2" >}} Color {{< /headname >}}

<!-- Semantic colors -->

{{< headname level="3" >}} Semantic colors {{< /headname >}}

The standard format for range is accompanied by the component class `range` and modifier class `range-{semantic-color}`.

{{< code addClass="flex-col gap-6" >}}
<input type="range" class="range" aria-label="range" />
<input type="range" class="range range-primary" aria-label="primary range" />
<input type="range" class="range range-secondary" aria-label="secondary range" />
<input type="range" class="range range-info" aria-label="info range" />
<input type="range" class="range range-success" aria-label="success range" />
<input type="range" class="range range-warning" aria-label="warning range" />
<input type="range" class="range range-error" aria-label="error range" />
{{< /code >}}

<!-- Custom color -->

{{< headname level="3" >}} Custom color {{< /headname >}}

Utilize `[--range-color:]` to incorporate your custom color.

{{< code >}}
<input type="range" class="range [--range-color:teal]" aria-label="custom range" />
{{< /code >}}

<!-------------------- Illustration -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Disabled -->

{{< headname level="3" >}} Disabled {{< /headname >}}

Apply the `disabled` boolean attribute to a range input to disable pointer events and prevent focusing.

{{< code >}}
<input type="range" class="range" aria-label="disabled range" disabled />
{{< /code >}}

<!-- Min and max -->

{{< headname level="3" >}} Min and max {{< /headname >}}

Range inputs inherently have default values for `min` and `max` - 0 and 100, respectively. You can customize these values using the `min` and `max` attributes.

{{< code >}}
<input type="range" class="range" min="0" max="100" value="40" aria-label="range">
{{< /code >}}

<!-- Steps -->

{{< headname level="3" >}} Steps {{< /headname >}}

The `step` attribute specifies the interval between legal numbers in an `<input>` element.

{{< code >}}
<input type="range" min="0" max="100" value="25" class="range" step="25" aria-label="range" />

<div class="w-full flex justify-between text-xs px-2">
  <span>|</span>
  <span>|</span>
  <span>|</span>
  <span>|</span>
  <span>|</span>
</div>
{{< /code >}}
