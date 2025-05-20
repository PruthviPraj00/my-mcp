---
title: "Pin Input"
components: 13
description: "The Pin Input component enables quick entry for scenarios such as multi-factor authentication, offering features like regex validation and clipboard pasting."
bg_image: "svg/form-elements/pin-input.svg"
menu:
  main:
    parent: "advanced forms"

previous: Input Number
previousLink: advanced-forms/input-number/

next: Strong Password
nextLink: advanced-forms/strong-password/

requires_js: true
pageJS:
  - "/js/pages/pin-input.js"
---

{{< callout "info" >}}
Pin input components are adopted from <a href="https://preline.co/docs/pin-input.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class Table -->

{{< class-table >}}
pin-input | component | Container style class.
pin-input-underline | style | Underline style.
pin-input-active:{tw-utility-class} | variant | Adds tailwind classes when the pin input is active (triggered when the PIN has set up).
pin-input-xs | size | Pin input with extra small size.
pin-input-sm | size | Pin input with small size.
pin-input-md | size | Pin input with medium(default) size.
pin-input-lg | size | Pin input with large size.
pin-input-xl | size | Pin input with large size.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic pin input example.

{{< code >}}

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input" aria-label="pin input" data-pin-input-item autofocus />
  <input type="text" class="pin-input" aria-label="pin input" data-pin-input-item />
  <input type="text" class="pin-input" aria-label="pin input" data-pin-input-item />
  <input type="text" class="pin-input" aria-label="pin input" data-pin-input-item />
</div>
{{< /code >}}

<!-- Placeholder -->

{{< headname level="3" >}} Placeholder {{< /headname >}}

Pin input with placeholder.

{{< code >}}

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-------------------- Types -------------------->

{{< headname level="2" >}} Types {{< /headname >}}

<!-- Outline -->

{{< headname level="3" >}} Outline {{< /headname >}}

Default pin input example.

{{< code >}}

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-- Underline -->

{{< headname level="3" >}} Underline {{< /headname >}}

Apply the `pin-input-underline` class to change the pin input style to an underline.

{{< code >}}

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-underline" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-------------------- Sizes -------------------->

{{< headname level="2" >}} Sizes {{< /headname >}}

<!-- Outline -->

{{< headname level="3" >}} Outline {{< /headname >}}

Add responsive class `pin-input-{size}` where `{size} = xs|sm|md|lg|xl` for pin input of different sizes.

{{< code addClass="flex-col gap-6" >}}

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-xs" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-xs" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-xs" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-xs" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-sm" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-sm" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-sm" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-sm" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-lg" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-lg" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-lg" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-lg" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-xl" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-xl" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-xl" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-xl" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-- Underline -->

{{< headname level="3" >}} Underline {{< /headname >}}

Underline pin input sizes example.

{{< code addClass="flex-col gap-6" >}}

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-underline pin-input-xs" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-xs" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-xs" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-xs" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-underline pin-input-sm" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-sm" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-sm" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-sm" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-underline" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-underline pin-input-lg" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-lg" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-lg" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-lg" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input pin-input-underline pin-input-xl" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-xl" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-xl" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input pin-input-underline pin-input-xl" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Disabled -->

{{< headname level="3" >}} Disabled {{< /headname >}}

To disable pointer events and prevent focusing, add the `disabled` boolean attribute to an input.

{{< code >}}

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item disabled />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item disabled />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item disabled />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item disabled />
</div>
{{< /code >}}

<!-- Length -->

{{< headname level="3" >}} Length {{< /headname >}}

Control the number of pin input as per you preference.

{{< code addClass="flex-col gap-6" >}}

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
</div>

<div class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-- Input type -->

{{< headname level="3" >}} Input type {{< /headname >}}

By default, this accepts both letters and numbers. To restrict input to numbers/letters only, set `"availableCharsRE"` to `"^[a-z]+$"` / `"^[0-9]+$"`.

{{< code >}}

<div class="flex space-x-3" data-pin-input='{"availableCharsRE": "^[a-z]+$"}'>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-- Regex type -->

{{< headname level="3" >}} Regex type {{< /headname >}}

To restrict the pin input to accept only specific numbers, you can use a regular expression. For example, to ensure the pin input accepts only the numbers 1 to 5, set `"availableCharsRE"` to `"^[1-5]+$"`.

{{< code >}}

<div class="flex space-x-3" data-pin-input='{"availableCharsRE": "^[1-5]+$"}'>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-- Protected -->

{{< headname level="3" >}} Protected {{< /headname >}}

Conceal the entered value by setting the type attribute to "password".

{{< code >}}

<div class="flex space-x-3" data-pin-input>
  <input type="password" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="password" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="password" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="password" class="pin-input" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-- Display number keyboard -->

{{< headname level="3" >}} Display number keyboard {{< /headname >}}

To display a numeric keyboard on iOS (note: this does not apply for Android), Use `autocomplete="one-time-code"` and `type="tel"`.

{{< code >}}

<div class="flex space-x-3" data-pin-input='{"availableCharsRE": "^[0-9]+$"}'>
  <input type="tel" class="pin-input" placeholder="○" data-pin-input-item  autocomplete="one-time-code"/>
  <input type="tel" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="tel" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="tel" class="pin-input" placeholder="○" data-pin-input-item />
</div>
{{< /code >}}

<!-- Destroy/Reinitialize -->

{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}

The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a pin-input element.

{{< code jsCode="true" addClass="!block" >}}

<div id="pin-input-to-destroy" class="flex space-x-3" data-pin-input>
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
  <input type="text" class="pin-input" placeholder="○" data-pin-input-item />
</div>

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    ;(function () {
      const pinInput = document.querySelector('#pin-input-to-destroy')
      const destroy = document.querySelector('#destroy-btn')
      const reinit = document.querySelector('#reinit-btn')

      destroy.addEventListener('click', () => {
        const { element } = HSPinInput.getInstance(pinInput, true)

        element.destroy()

        destroy.setAttribute('disabled', 'disabled')
        reinit.removeAttribute('disabled')
      })

      reinit.addEventListener('click', () => {
        HSPinInput.autoInit()

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
FlyonUI is powered by <a href="https://preline.co/plugins/html/pin-input.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Options table -->

{{< table >}}

PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-pin-input`</span>| <span class="text-pretty">Activate a Pin Input by specifying on an element. | `-` | `-`
<span class="text-nowrap">`:availableCharsRE`</span>| <span class="text-pretty">String of regular expression for allowed characters. | RegExp | <code class="text-nowrap">^[a-zA-Z0-9]+$</code>
<span class="text-nowrap">`data-pin-input-item`</span>| <span class="text-pretty">Identifies the element in the container responsible for data entry. | `-` | `-`
{{< /table >}}

<!-- Class Options -->
{{< headname level="3" >}} Class Options {{< /headname >}}

{{< table >}}
PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`autofocus`</span>| <span class="text-pretty"> If one of the fields has this class, it will be focused when the page loads. | `-` | `-`
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}
The `HSPinInput` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`destroy()`| Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSPinInput.getInstance(target, isInstance)`|<div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
{{< /table >}}

<p class="mt-10 mb-1.5 not-prose" id="destroy-method">Destroy instance.</p>

{{< code-highlight lang="js" >}}const { element } = HSPinInput.getInstance('#pin-input', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION | RETURNING VALUE
`on:completed`|The event is triggered when the PIN has set up.| Current value
{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

Assign an ID to `data-pin-input`, and you can then trigger an event using that ID.

Below is a demonstration of how to use the event. We've included JavaScript to handle the events, allowing it to execute when the corresponding event is fired. To test these events, monitor your console.

{{< code jsCode="true" addClass="justify-between flex-wrap" >}}

<div class="flex space-x-3" data-pin-input id="pin-input-log">
  <input type="text" class="pin-input" aria-label="pin input" data-pin-input-item autofocus />
  <input type="text" class="pin-input" aria-label="pin input" data-pin-input-item />
  <input type="text" class="pin-input" aria-label="pin input" data-pin-input-item />
  <input type="text" class="pin-input" aria-label="pin input" data-pin-input-item />
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const el = HSPinInput.getInstance('#pin-input-log')
    
    el.on('completed', ({ instance }) => {
      console.log('Hello')
    })
  })
</script>

{{< /code >}}

<p class="mt-12 mb-1.5 not-prose">When pin input is completed example.</p>

{{< code-highlight lang="js" >}}const el = HSPinInput.getInstance('#pin-input-log');

el.on('completed', ({instance}) => {console.log("Hello")});
{{< /code-highlight >}}
