---
title: "Strong Password"
components: 9
description: "The Strong Password Component uses a progress bar to display password strength, encouraging users to create stronger passwords during registration or updates."
bg_image: "svg/form-elements/strong-password.svg"
menu:
  main:
    parent: "advanced forms"

previous: Pin Input
previousLink: advanced-forms/pin-input/

next: Toggle Count
nextLink: advanced-forms/toggle-count/

requires_js: true

pageJS:
  - "/js/pages/strong-password.js"
---

{{< callout "info" >}}
Strong password components are adopted from <a href="https://preline.co/docs/strong-password.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class Table -->

{{< class-table >}}
input | component | Basic input field.
strong-password:{tw-utility-class} | variant | The modifier allows setting Tailwind classes for the passed stripes.
strong-password-accepted:{tw-utility-class} | variant | The modifier allows setting Tailwind classes when password strength is accepted.
strong-password-active:{tw-utility-class} | variant | The modifier allows setting Tailwind classes when a password strength rule is active.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic example demonstrating password input with strength meter.

{{< code addClass="!block" >}}

<div class="flex max-w-sm">
  <div class="flex-1">
    <input type="password" id="password-base" class="input" placeholder="Enter password" />
    <div
      data-strong-password='{
        "target": "#password-base",
        "stripClasses": "strong-password:bg-primary strong-password-accepted:bg-teal-500 h-1.5 flex-auto bg-neutral/20"
      }'
      class="rounded-full overflow-hidden mt-2 flex gap-0.5">
    </div>
  </div>
</div>
{{< /code >}}

<!-- Label -->

{{< headname level="3" >}} Label {{< /headname >}}

Password input with label.

{{< code addClass="!block" >}}

<div class="max-w-sm">
  <div class="flex-1">
    <label class="label-text" for="password-label"> Enter password </label>
    <input type="password" id="password-label" class="input" placeholder="Enter password" />
    <div
      data-strong-password='{
        "target": "#password-label",
        "stripClasses": "strong-password:bg-primary strong-password-accepted:bg-teal-500 h-1.5 flex-auto bg-neutral/20"
      }'
      class="rounded-full overflow-hidden mt-2 flex gap-0.5">
    </div>
  </div>
</div>

{{< /code >}}

<!-------------------- Types -------------------->

{{< headname level="2" >}} Types {{< /headname >}}

<!-- Floating -->

{{< headname level="3" >}} Floating {{< /headname >}}

Strong password example with input type.

{{< callout "info" >}}
You can utilize the class "input-floating" along with `input` for password type. For further details, please refer on {{< link link="forms/input/#types" addClass="link link-primary" >}}Input Types{{< /link >}}.
{{< /callout >}}

{{< code addClass="!block space-y-5" >}}

<!-- Floating example -->
<div class="flex max-w-sm">
  <div class="input-floating">
    <input type="password" id="password-floating" class="input" placeholder="Make it strong" />
    <label class="input-floating-label" for="password-floating">Enter password</label>
    <div
      data-strong-password='{
        "target": "#password-floating",
        "stripClasses": "strong-password:bg-primary strong-password-accepted:bg-teal-500 h-1.5 flex-auto bg-neutral/20"
      }'
      class="rounded-full overflow-hidden mt-2 flex gap-0.5">
    </div>
  </div>
</div>
{{< /code >}}

<!-- Illustrations -->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Indicator and Hints -->

{{< headname level="3" >}} Indicator and Hints {{< /headname >}}

Indicators and hints help enhance the user experience.

{{< code addClass="!block" >}}

<div class="max-w-sm">
  <div class="flex mb-2">
    <div class="flex-1">
      <input type="password" id="password-hints" class="input" placeholder="Enter password" />
      <div
        data-strong-password='{
          "target": "#password-hints",
          "hints": "#password-hints-content",
          "stripClasses": "strong-password:bg-primary strong-password-accepted:bg-teal-500 h-1.5 flex-auto bg-neutral/20"
        }'
        class="rounded-full overflow-hidden mt-2 flex gap-0.5">
      </div>
    </div>
  </div>
  <div id="password-hints-content" class="mb-3">
    <div>
      <span class="text-sm text-base-content">Level:</span>
      <span
        data-pw-strength-hint='["Empty", "Weak", "Medium", "Strong", "Very Strong", "Super Strong"]'
        class="text-base-content text-sm font-semibold">
      </span>
    </div>
    <h6 class="my-2 text-base font-semibold text-base-content">Your password must contain:</h6>
    <ul class="text-base-content/80 space-y-1 text-sm">
      <li data-pw-strength-rule="min-length" class="strong-password-active:text-success flex items-center gap-x-2">
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Minimum number of characters is 6.
      </li>
      <li data-pw-strength-rule="lowercase" class="strong-password-active:text-success flex items-center gap-x-2">
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Should contain lowercase.
      </li>
      <li data-pw-strength-rule="uppercase" class="strong-password-active:text-success flex items-center gap-x-2">
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Should contain uppercase.
      </li>
      <li data-pw-strength-rule="numbers" class="strong-password-active:text-success flex items-center gap-x-2">
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Should contain numbers.
      </li>
      <li data-pw-strength-rule="special-characters" class="strong-password-active:text-success flex items-center gap-x-2" >
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Should contain special characters.
      </li>
    </ul>
  </div>
</div>
{{< /code >}}

<!-- Minimum length -->

{{< headname level="3" >}} Minimum length {{< /headname >}}

In this example, the `minLength` property is used to specify the minimum number of characters, which is set to 7.

To test this, we've disabled the inclusion of `lowercase`, `uppercase`, `numbers`, and `special characters` using the `:checksExclude` property. Now, only the `min-length` requirement is active.

{{< code addClass="!block" >}}

<div class="flex max-w-sm">
  <div class="flex-1">
    <input type="password" id="min-length" class="input" placeholder="Enter password" />
    <div
      data-strong-password='{
        "target": "#min-length",
        "stripClasses": "strong-password-accepted:bg-teal-500 h-1.5 flex-auto rounded-full bg-neutral/20",
        "minLength": "7",
        "checksExclude": ["lowercase", "uppercase", "numbers", "special-characters"]
      }'
      class="mt-2">
    </div>
  </div>
</div>
{{< /code >}}

<!-- API -->

{{< headname level="3" >}} API {{< /headname >}}

Use the `specialCharactersSet` property to specify a custom set of special characters. In below example, only `&`, `!`, and `@` will satisfy the special character condition.

{{< code addClass="!block" >}}

<div class="flex max-w-sm">
  <div class="flex-1">
    <input type="password" id="password-special-character" class="input" placeholder="Enter password" />
    <div
      data-strong-password='{
        "target": "#password-special-character",
        "stripClasses": "strong-password:bg-primary strong-password-accepted:bg-teal-500 h-1.5 flex-auto bg-neutral/20",
        "specialCharactersSet": "&!@"
      }'
      class="rounded-full overflow-hidden mt-2 flex gap-0.5">
    </div>
  </div>
</div>
{{< /code >}}

<!-- Popover example -->

{{< headname level="3" >}} Popover example {{< /headname >}}

Indicator and hints inside a popover.

{{< callout "info" >}}
The example below demonstrates the use of the popover plugin on input. For more information, please consult the {{< link link="overlays/popover/" addClass="link link-primary" >}}Popover{{< /link >}}.
{{< /callout >}}

{{< code addClass="!block h-[32rem] max-sm:overflow-y-auto sm:pt-60" >}}

<div class="max-w-sm">
  <div class="flex">
    <div class="relative flex-1">
      <input type="password" id="password-popover" class="input" placeholder="Enter password"/>
      <div id="password-popover-content" class="card absolute z-10 w-full hidden p-4">
        <div
          data-strong-password='{
            "target": "#password-popover",
            "hints": "#password-popover-content",
            "stripClasses": "strong-password:bg-primary strong-password-accepted:bg-teal-500 h-1.5 flex-auto bg-neutral/20",
            "mode": "popover"
          }'
          class="rounded-full overflow-hidden mt-2.5 flex gap-0.5">
        </div>
        <h6 class="text-base text-base-content my-2 font-semibold">Your password must contain:</h6>
        <ul class="text-base-content/80 space-y-1 text-sm">
          <li data-pw-strength-rule="min-length" class="strong-password-active:text-success flex items-center gap-x-2">
            <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
            <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
            Minimum number of characters is 6.
          </li>
          <li data-pw-strength-rule="lowercase" class="strong-password-active:text-success flex items-center gap-x-2">
            <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
            <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
            Should contain lowercase.
          </li>
          <li data-pw-strength-rule="uppercase" class="strong-password-active:text-success flex items-center gap-x-2">
            <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
            <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
            Should contain uppercase.
          </li>
          <li data-pw-strength-rule="numbers" class="strong-password-active:text-success flex items-center gap-x-2">
            <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
            <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
            Should contain numbers.
          </li>
          <li data-pw-strength-rule="special-characters" class="strong-password-active:text-success flex items-center gap-x-2" >
            <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
            <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
            Should contain special characters.
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Destroy/Reinitialize -->
{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}
The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a strong password.

{{< code addClass="!block" jsCode="true" >}}
<div class="max-w-sm">
  <div class="flex mb-2">
    <div class="flex-1">
      <input type="password" id="password-hints-to-destroy" class="input" placeholder="Enter password" />
      <div
        id="strong-password-to-destroy"
        data-strong-password='{
          "target": "#password-hints-to-destroy",
          "hints": "#password-hints-content-to-destroy",
          "stripClasses": "strong-password:bg-primary strong-password-accepted:bg-teal-500 h-1.5 flex-auto bg-neutral/20"
        }'
        class="rounded-full overflow-hidden mt-2 flex gap-0.5">
      </div>
    </div>
  </div>
  <div id="password-hints-content-to-destroy" class="mb-3">
    <div>
      <span class="text-sm text-base-content">Level:</span>
      <span
        data-pw-strength-hint='["Empty", "Weak", "Medium", "Strong", "Very Strong", "Super Strong"]'
        class="text-base-content text-sm font-semibold">
      </span>
    </div>
    <h6 class="my-2 text-base font-semibold text-base-content">Your password must contain:</h6>
    <ul class="text-base-content/80 space-y-1 text-sm">
      <li data-pw-strength-rule="min-length" class="strong-password-active:text-success flex items-center gap-x-2">
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Minimum number of characters is 6.
      </li>
      <li data-pw-strength-rule="lowercase" class="strong-password-active:text-success flex items-center gap-x-2">
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Should contain lowercase.
      </li>
      <li data-pw-strength-rule="uppercase" class="strong-password-active:text-success flex items-center gap-x-2">
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Should contain uppercase.
      </li>
      <li data-pw-strength-rule="numbers" class="strong-password-active:text-success flex items-center gap-x-2">
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Should contain numbers.
      </li>
      <li data-pw-strength-rule="special-characters" class="strong-password-active:text-success flex items-center gap-x-2" >
        <span class="icon-[tabler--circle-check] hidden size-5 shrink-0" data-check></span>
        <span class="icon-[tabler--circle-x] hidden size-5 shrink-0" data-uncheck></span>
        Should contain special characters.
      </li>
    </ul>
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
    const strongPassword = document.querySelector('#strong-password-to-destroy')
    const destroyBtn = document.querySelector('#destroy-btn')
    const reinitBtn = document.querySelector('#reinit-btn')

    // Destroy usage
    destroyBtn.addEventListener('click', () => {
      const { element } = HSStrongPassword.getInstance(strongPassword, true)

      element.destroy()

      destroyBtn.setAttribute('disabled', 'disabled')
      reinitBtn.removeAttribute('disabled')
    })

    // Reinit usage
    reinitBtn.addEventListener('click', () => {
      HSStrongPassword.autoInit()

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
FlyonUI is powered by <a href="https://preline.co/plugins/html/strong-password.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

{{< table >}}
PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-strong-password`</span>| <span class="text-pretty">Enable strong password requirements for a specific element. The password must include at least one lowercase letter, one uppercase letter, one number, one special character (!%&@#$^\*?\_~), and be a minimum of 6 characters long.</span>|`-`|`-`
`:target` (required) | This function accepts the ID of the content element that should be observed, typically the ID of an `input` element.| string | `-`
`:stripClasses` | Defines CSS classes for each strip. | `-` | `-`
`:minLength` | Specifies the minimum length required for a password.| number | `6`
`:mode` | Specifies the mode to be used. If "popover" is selected, the hints will be displayed as a popover.| default or popover | `default`
`:popoverSpace` | This option is available when the mode is set to "popover". It specifies the space between the popover and the target element.| number | `10`
`:checksExclude` | Specifies which checks should be excluded. It accepts an array of strings, such as ["min-length", "lowercase", "uppercase", "numbers", "special-characters"]. | array | `[]`
`:specialCharactersSet`|Specifies which special characters should be used for checking. It accepts a string containing the available characters, for example, "!%&".| string |<span><code>!"#$%&\'()\*+,-./:;<=>?@[\\\\\\]^\_\`\{}~</code><span>
`:hints`|Specifies the element to be observed as the hints container. This must be a valid selector. Some selectors available for use inside the hints include:<ul> <li>`[data-pw-strength-hint]` Specifies the element to be observed as the weakness text container. It should contain an array of strings, such as ["Empty", "Weak", "Medium", "Strong", "Very Strong", "Super Strong"]. Each text corresponds to a specific strength value. For example, "Medium" has an index of 2 and will be displayed when the strength is also 2. "Empty" has an index of 0 and will be shown when the field is empty and has no strength. </li> <li>`[data-pw-strength-rule]` Specifies the element to be observed as the rule text container. It can have one of the following values: "min-length", "lowercase", "uppercase", "numbers", or "special-characters".</li> <li>`[data-check]`Specifies the element to be observed inside the [data-pw-strength-rule] attribute as the rule check icon container.</li> <li>`[data-uncheck]`Specifies the element to be observed inside the [data-pw-strength-rule] attribute as the rule uncheck icon container.</li> </ul>| string|`-`
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSStrongPassword` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`recalculateDirection()` | Force recalculation for dropdown hint.
`destroy()` | Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSStrongPassword.getInstance(target)` | <div>Returns the element linked to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li></ul></div>
{{< /table >}}

<p class="mt-10 mb-1.5 not-prose">Force dropdown hint position to be recalculated when scrolling (public method).</p>

{{< code-highlight lang="js" >}}const strongPassword = new HSStrongPassword(document.querySelector('#strong-password'));

document.addEventListener('scroll', () => {
  if (strongPassword) strongPassword.recalculateDirection();
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose">Force dropdown hint position to be recalculated when scrolling (mixed).</p>
{{< code-highlight lang="js" >}}const strongPassword = HSStrongPassword.getInstance('#strong-password');

document.addEventListener('scroll', () => {
  if (strongPassword) strongPassword.recalculateDirection();
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose" id="destroy-method">Destroy instance.</p>

{{< code-highlight lang="js" >}}
const { element } = HSStrongPassword.getInstance('#strong-password-destroy', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION | RETURNING VALUE
`on:change`| Called when target element was changed. | <ul class="m-0"><li><code>strength</code> number. Current level of strength (0 - 4). Default - 0</li><li><code>rules</code> array. Current set of passed checks ("lowercase", "uppercase", "numbers", "special-characters")</li></ul>
{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

Assign an ID to the div that contains the `data-strong-password` attribute, and then use that ID to attach an event.

The example below demonstrates a use case of event usage. You can view the output in the console by typing in `input`.

{{< code jsCode="true" addClass="!block" >}}

<div class="flex max-w-sm">
  <div class="flex-1">
    <input type="password" id="password-event" class="input" placeholder="Enter password" />
    <div
      id="strong-password"
      data-strong-password='{
        "target": "#password-event",
        "stripClasses": "strong-password:bg-primary strong-password-accepted:bg-teal-500 h-1.5 flex-auto bg-neutral/20"
      }'
      class="rounded-full overflow-hidden mt-2 flex gap-0.5">
    </div>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const el = HSStrongPassword.getInstance('#strong-password', true).element
    el.on('change', ({ strength, rules }) => {
      console.log('strength:', strength)
      console.log('rules:', rules)
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">An example where a function is run every time a value changes.</p>
{{< code-highlight lang="js" >}}const {element } =  HSStrongPassword.getInstance('#strong-password', true);
element.on('change', ({strength, rules}) => {
  console.log('strength:', strength)
  console.log('rules:', rules)
});
{{< /code-highlight >}}
