---
title: "Toggle Password"
components: 3
description: "The Toggle Password Component allows users to show or hide their password in forms, helping ensure accuracy while keeping sensitive information secure."
bg_image: "svg/form-elements/toggle-password.svg"
menu:
  main:
    parent: "advanced forms"

previous: Toggle Count
previousLink: advanced-forms/toggle-count/


next: Table
nextLink: tables/table/

requires_js: true
pageJS:
  - "/js/pages/toggle-password.js"
---

{{< callout "info" >}}
Toggle password components are adopted from <a href="https://preline.co/docs/toggle-password.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class Table -->

{{< class-table >}}
input | component | Basic input field.
is-valid | state | Adds success style to the input.
is-invalid | state | Adds error style to the input.
password-active:{tw-utility-class} | variant | A method to apply specific Tailwind classes when the password is visible.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic example of toggle password.

{{< code >}}

<div class="input max-w-sm">
  <input id="toggle-password" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
  <button type="button" data-toggle-password='{ "target": "#toggle-password" }' class="block cursor-pointer" aria-label="password toggle" >
    <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
    <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
  </button>
</div>
{{< /code >}}

<!-- Label -->

{{< headname level="3" >}} Label {{< /headname >}}

Password input with label.

{{< code addClass="!block" >}}
<div class="max-w-sm">
  <label class="label-text" for="toggle-password-label">Password</label>
  <div class="input">
    <input id="toggle-password-label" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
    <button type="button" data-toggle-password='{ "target": "#toggle-password-label" }' class="block cursor-pointer" aria-label="password toggle" >
      <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
      <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
    </button>
  </div>
</div>
{{< /code >}}

<!-------------------- Type -------------------->

{{< headname level="2" >}} Type {{< /headname >}}

<!-- Floating -->

{{< headname level="3" >}} Floating {{< /headname >}}

Toggle password example with input type.

{{< callout "info" >}}
You can utilize the input types "floating" along with the password type. For further details, please refer on {{< link link="forms/input/#types" addClass="link link-primary" >}}Input Types{{< /link >}}.
{{< /callout >}}

{{< code addClass="!block space-y-5" >}}

<div class="input max-w-sm">
  <div class="input-floating grow">
    <input id="toggle-password-floating" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
    <label class="input-floating-label ms-0" for="toggle-password-floating">Password</label>
  </div>
  <button type="button" data-toggle-password='{ "target": "#toggle-password-floating" }' class="block cursor-pointer" aria-label="password toggle">
    <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
    <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
  </button>
</div>
{{< /code >}}

<!-------------------- Validation states -------------------->

{{< headname level="2" >}} Validation states {{< /headname >}}

<!-- Success state -->

{{< headname level="3" >}} Success state {{< /headname >}}

Success state can be show using `is-valid` class.

{{< code addClass="!block space-y-5" >}}

<!-- Basis -->
<div class="max-w-sm">
  <label class="label-text" for="toggle-password-basic-success">Password</label>
  <div class="input is-valid">
    <input id="toggle-password-basic-success" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
    <button type="button" data-toggle-password='{ "target": "#toggle-password-basic-success" }' class="block cursor-pointer" aria-label="password toggle" >
      <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
      <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
    </button>
  </div>
</div>
<!-- Floating example -->
<div class="input max-w-sm">
  <div class="input-floating">
    <input id="toggle-password-floating-success" class="is-valid" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
    <label class="input-floating-label ms-0" for="toggle-password-floating-success">Password</label>
  </div>
  <button type="button" data-toggle-password='{ "target": "#toggle-password-floating-success" }' class="block cursor-pointer" aria-label="password toggle" >
    <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
    <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
  </button>
</div>
{{< /code >}}

<!-- Error state -->

{{< headname level="3" >}} Error state {{< /headname >}}

Error state can be show using `is-invalid` class.

{{< code addClass="!block space-y-5" >}}

<!-- Basis -->
<div class="max-w-sm">
  <label class="label-text" for="toggle-password-basic-error">Password</label>
  <div class="input is-invalid">
    <input id="toggle-password-basic-error" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
    <button type="button" data-toggle-password='{ "target": "#toggle-password-basic-error" }' class="block cursor-pointer" aria-label="password toggle" >
      <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
      <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
    </button>
  </div>
</div>

<!-- Floating example -->
<div class="input max-w-sm">
  <div class="input-floating">
    <input id="toggle-password-floating-error" class="is-invalid" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
    <label class="input-floating-label ms-0" for="toggle-password-floating-error">Password</label>
  </div>
  <button type="button" data-toggle-password='{ "target": "#toggle-password-floating-error" }' class="block cursor-pointer" aria-label="password toggle" >
    <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
    <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
  </button>
</div>
{{< /code >}}

<!-------------------- Illustrations` -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Multiple -->

{{< headname level="3" >}} Multiple {{< /headname >}}

Utilize the `data-toggle-password-group` attribute to consolidate multiple passwords under a single toggle icon.

{{< code addClass="!block" >}}



<div data-toggle-password-group>
  <!-- Current password -->
  <div class="mb-4 max-w-sm">
    <label class="label-text" for="toggle-password-multiple1">Current Password</label>
    <div class="input">
      <input id="toggle-password-multiple1" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
      <button type="button" data-toggle-password='{ "target": ["#toggle-password-multiple1","#toggle-password-multiple2"] }' class="block cursor-pointer" aria-label="password toggle" >
        <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
        <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
      </button>
    </div>
  </div>
  <!-- New password -->
  <div class="max-w-sm">
    <label class="label-text" for="toggle-password-multiple2">New Password</label>
    <div class="input">
      <input id="toggle-password-multiple2" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
      <button type="button" data-toggle-password='{ "target": ["#toggle-password-multiple1","#toggle-password-multiple2"] }' class="block cursor-pointer" aria-label="password toggle" >
        <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
        <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
      </button>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Checkbox -->

{{< headname level="3" >}} Checkbox {{< /headname >}}

Toggle password visibility with a checkbox.

{{< code addClass="!block" >}}

<div class="mb-3 max-w-sm">
  <label class="label-text" for="toggle-password-checkbox">Password</label>
  <input id="toggle-password-checkbox" type="password" class="input" placeholder="Enter password" value="Pwd_1242@mA1" />
</div>

<div class="flex items-center gap-2">
  <input id="toggleCheckboxPassword" type="checkbox" data-toggle-password='{ "target": "#toggle-password-checkbox" }' class="checkbox checkbox-primary" />
  <label class="label-text text-base" for="toggleCheckboxPassword">Show password</label>
</div>
{{< /code >}}

<!-- Modal -->

{{< headname level="3" >}} Modal {{< /headname >}}

Basic usage in modal window.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="password-modal" data-overlay="#password-modal" >
  Open modal
</button>

<div id="password-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Check Password</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#password-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <label class="label-text" for="toggle-password-modal">Password</label>
        <div class="input">
          <input id="toggle-password-modal" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
          <button type="button" data-toggle-password='{ "target": "#toggle-password-modal" }' class="block cursor-pointer" aria-label="password toggle" >
            <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
            <span
              class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"
            ></span>
          </button>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#password-modal">Close</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Destroy/Reinitialize -->
{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}
The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a toggle password.

{{< code addClass="!block" jsCode="true" >}}
<div id="toggle-password-to-destroy" data-toggle-password-group>
  <!-- Current password -->
  <div class="mb-4 max-w-sm">
    <label class="label-text" for="toggle-password-destroy">Current Password</label>
    <div class="input">
      <input id="toggle-password-destroy" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
      <button type="button" data-toggle-password='{ "target": ["#toggle-password-destroy","#toggle-password-destroy2"] }' class="block cursor-pointer" aria-label="password toggle" >
        <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
        <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
      </button>
    </div>
  </div>
  <!-- New password -->
  <div class="max-w-sm">
    <label class="label-text" for="toggle-password-destroy2">New Password</label>
    <div class="input">
      <input id="toggle-password-destroy2" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
      <button type="button" data-toggle-password='{ "target": ["#toggle-password-destroy","#toggle-password-destroy2"] }' class="block cursor-pointer" aria-label="password toggle" >
        <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
        <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
      </button>
    </div>
  </div>
</div>

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    // Destroy and reinit variables
    const togglesPassword = document.querySelectorAll('#toggle-password-to-destroy [data-toggle-password]')
    const destroyBtn = document.querySelector('#destroy-btn')
    const reinitBtn = document.querySelector('#reinit-btn')

    destroyBtn.addEventListener('click', () => {
      togglesPassword.forEach(el => {
        const { element } = HSTogglePassword.getInstance(el, true)

        element.destroy()
      })

      destroyBtn.setAttribute('disabled', 'disabled')
      reinitBtn.removeAttribute('disabled')
    })

    reinitBtn.addEventListener('click', () => {
      HSTogglePassword.autoInit()

      reinitBtn.setAttribute('disabled', 'disabled')
      destroyBtn.removeAttribute('disabled')
    })
  })
</script>
{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/toggle-password.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

{{< table >}}
PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-toggle-password`</span>| <span class="text-pretty">Enable a Toggle Password feature by specifying it on an element.</span>|`-`|`-`
`:target` (required) | This function accepts the ID of the content element that should be toggle, typically the ID of an `input` element.| string | `-`
`:isShown` | Determines password visibility. | boolean | `false`
`:eventType` |Determines event type.| change or click | `click`
`data-toggle-password-group`| This feature enables you to group multiple toggle password elements together, allowing them to be toggled simultaneously. It should be applied to the parent element containing the toggle password elements.|`-`|`-`
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSTogglePassword` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`show()` | Toggle the field to type text.
`hide()` | Toggle the field to type password.
`destroy()` | Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSTogglePassword.getInstance(target, isInstance)` | <div>Returns the element linked to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

Assign an ID to the div containing the `data-toggle-password` attribute, as demonstrated in the public method. To explore additional methods, you can copy them into the console.

{{< code jsCode="true" addClass="flex-col gap-4" >}}

<div class="input max-w-sm">
  <input id="toggle-password-mt" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
  <button id="toggle-password-method" type="button" data-toggle-password='{ "target": "#toggle-password-mt" }' class="block cursor-pointer" aria-label="password toggle">
    <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
    <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
  </button>
</div>

<button type="button" class="btn btn-primary w-max" id="show-btn">Show Btn</button>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const togglePassword = new HSTogglePassword(document.querySelector('#toggle-password-method'))
    const showBtn = document.querySelector('#show-btn')

    showBtn.addEventListener('click', () => {
      togglePassword.show()
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">Toggle the field to type text (public method).</p>

{{< code-highlight lang="js" >}}// This method is used in above example.
const togglePassword = new HSTogglePassword(document.querySelector('#toggle-password-method'));
const showBtn = document.querySelector('#show-btn');

showBtn.addEventListener('click', () => {
  togglePassword.show();
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose">Toggle the field to type text (mixed).</p>
{{< code-highlight lang="js" >}}const { element } = HSTogglePassword.getInstance('#toggle-password-method', true);
const showBtn = document.querySelector('#show-btn');

showBtn.addEventListener('click', () => {
  element.show();
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose" id="destroy-method">Destroy instance.</p>

{{< code-highlight lang="js" >}}
const { element } = HSTogglePassword.getInstance('#toggle-password-to-destroy', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION | RETURNING VALUE
`on:toggle`| Called when the password is shown or hidden. |Target
{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

Assign an ID to the div that contains the `data-toggle-password` attribute, and then use that ID to attach an event.
The example below demonstrates a use case of event usage. You can view the output in the console by typing in `input`.

{{< code jsCode="true" addClass="!block" >}}

<div class="input max-w-sm">
  <input id="toggle-password-el" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
  <button id="toggle-password-event" type="button" data-toggle-password='{ "target": "#toggle-password-el" }' class="block cursor-pointer" aria-label="password toggle" >
    <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
    <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
  </button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const el = HSTogglePassword.getInstance('#toggle-password-event')

    el.on('toggle', target => {
      console.log('target:', target)
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">An example where a function is run every time a field changes visibility.</p>
{{< code-highlight lang="js" >}}const el = HSTogglePassword.getInstance('#toggle-password-event');

el.on('toggle', (target) => {console.log('target:', target)});
{{< /code-highlight >}}
