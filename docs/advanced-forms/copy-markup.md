---
title: "Copy Markup"
components: 3
description: "The Copy Markup Component adds extra fields, like address entries, simplifying form expansion and making it ideal for dynamic surveys and registrations."
bg_image: "svg/form-elements/copy-markup.svg"
menu:
  main:
    parent: "advanced forms"

previous: Combo Box
previousLink: advanced-forms/combo-box/

next: Form Wizard
nextLink: advanced-forms/form-wizard/

requires_js: true
pageJS:
  - "/js/pages/copy-markup.js"
---

{{< callout "info" >}}
Copy Markup components are adopted from <a href="https://preline.co/docs/copy-markup.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class Table -->

{{< class-table >}}
input | component | Base class for input field.
select | component | Base class for select field.
{{< /class-table >}}

<!-------------------- Default -------------------->

{{< headname level="2" >}} Default {{< /headname >}}

<!-- Basic example -->

{{< headname level="3" >}} Basic example {{< /headname >}}

The `data-copy-markup` attribute defines the configuration for copying content. It has three key properties:

- `targetSelector`: The element to be copied, specified by a CSS selector.
- `wrapperSelector`: The element where the copied content is placed.
- `limit`: The maximum number of times content can be copied.

In this setup, the "Add Technology" button copies the content from `#content-for-copy` into the `#wrapper-for-copy` container, allowing a maximum of three copies. If the limit is reached, further copies are not allowed.

{{< code addClass="!block" >}}

<p class="mb-4">
  Which technologies have you primarily used? <span class="text-base-content font-medium">(Maximum three)</span>
</p>

<div id="wrapper-for-copy" class="max-w-xs space-y-3">
  <input id="content-for-copy" type="text" class="input" placeholder="Enter Technology Name" />
</div>

<div class="mt-4 flex max-w-xs justify-end">
  <button
    type="button"
    data-copy-markup='{
    "targetSelector": "#content-for-copy",
    "wrapperSelector": "#wrapper-for-copy",
    "limit": 3
    }'
    id="copy-content"
    class="btn btn-sm btn-primary"
  >
    <span class="icon-[tabler--plus]"></span>
    Add Technology
  </button>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- With select -->

{{< headname level="3" >}} With select {{< /headname >}}

Below example shows copy markup with select.

{{< code addClass="!block" >}}

<div id="wrapper-select-for-copy" class="space-y-3">
  <div id="content-select-for-copy" class="flex items-end gap-3 max-sm:flex-col">
    <div class="w-full sm:w-1/4">
      <label class="label-text" for="select"> Options </label>
      <select class="select" aria-label="select option" id="select">
        <option disabled selected>Choose option</option>
        <option value="size">Size</option>
        <option value="color">Color</option>
        <option value="weight">Weight</option>
        <option value="smell">Smell</option>
      </select>
    </div>
    <input type="text" class="input w-full sm:w-3/4" placeholder="Enter Value" />
  </div>
</div>

<p class="mt-4 text-end">
  <button
    type="button"
    data-copy-markup='{
      "targetSelector": "#content-select-for-copy",
      "wrapperSelector": "#wrapper-select-for-copy",
      "limit": 4
    }'
    id="copy-select-content"
    class="btn btn-sm btn-primary"
  >
    Add another option
  </button>
</p>
{{< /code >}}

<!-- Modals -->

{{< headname level="3" >}} Modals {{< /headname >}}

Below example shows copy markup with select in modals.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="modal-with-copy-markup" data-overlay="#modal-with-copy-markup">Open modal</button>

<div id="modal-with-copy-markup" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Skill survey</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#modal-with-copy-markup">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body grow space-y-3">
        <p>
          Which technologies have you primarily used?
          <br />
          <span class="text-base-content font-medium">(Maximum four)</span>
        </p>
        <div id="modal-wrapper-select-for-copy" class="space-y-3">
          <div id="modal-content-select-for-copy">
            <select class="select">
              <option disabled selected>Choose Technology</option>
              <option value="html">HTML</option>
              <option value="css">CSS</option>
              <option value="javascript">JavaScript</option>
              <option value="tailwindcss">TailwindCSS</option>
            </select>
          </div>
        </div>
        <p class="text-end">
          <button
            type="button"
            data-copy-markup='{
              "targetSelector": "#modal-content-select-for-copy",
              "wrapperSelector": "#modal-wrapper-select-for-copy",
              "limit": 4
            }'
            id="copy-select-with-modal-content"
            class="btn btn-sm btn-primary">
            Add another option
          </button>
        </p>
      </div>
      <div class="modal-footer mt-16">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#modal-with-copy-markup">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- With remove option -->

{{< headname level="3" >}} With remove option {{< /headname >}}

Add an attribute named `data-copy-markup-delete-item` to any button within a component identified by a specific ID. This attribute will enable the button to delete the component when clicked.

Below example shows copy markup with remove(delete) option.

{{< code addClass="!block" >}}

<p class="mb-4">
  Which technologies have you primarily used? <span class="text-base-content font-medium">(Maximum three)</span>
</p>
  
<div id="wrapper-remove-for-copy-target" class="max-w-sm space-y-3">
  <div id="content-remove-for-copy-target" class="flex items-center gap-2">
    <input type="text" class="input" placeholder="Enter Technology Name" />
    <button class="btn btn-square btn-outline btn-error" aria-label="delete button" data-copy-markup-delete-item>
      <span class="icon-[tabler--x]"></span>
    </button>
  </div>
</div>
  
<div class="flex max-w-sm justify-end gap-2 mt-4">
  <button
    type="button"
    data-copy-markup='{
    "targetSelector": "#content-remove-for-copy-target",
    "wrapperSelector": "#wrapper-remove-for-copy-target",
    "limit": 3
    }'
    id="copy-content-rem-btn"
    class="btn btn-sm btn-primary">
    <span class="icon-[tabler--plus]"></span>
    Add Technology
  </button>
</div>
{{< /code >}}

<!-- Destroy/Reinitialize -->
{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}
The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a copy markup.

{{< code addClass="!block" jsCode="true" >}}

<p class="mb-4">
  Which technologies have you primarily used? <span class="text-base-content font-medium">(Maximum three)</span>
</p>

<div id="wrapper-for-copy-to-destroy" class="w-full space-y-3">
  <input id="content-for-copy-to-destroy" type="text" class="input" placeholder="Enter Technology Name" />
</div>

<div class="mt-4 flex w-full justify-end">
  <button
    type="button"
    data-copy-markup='{
    "targetSelector": "#content-for-copy-to-destroy",
    "wrapperSelector": "#wrapper-for-copy-to-destroy",
    "limit": 3
    }'
    id="copy-markup-to-destroy"
    class="btn btn-sm btn-primary"
  >
    <span class="icon-[tabler--plus]"></span>
    Add Technology
  </button>
</div>

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    // Destroy and reinit variables
    const copyBtn = document.querySelector('#copy-markup-to-destroy')
    const destroyBtn = document.querySelector('#destroy-btn')
    const reinitBtn = document.querySelector('#reinit-btn')

    // Destroy usage
    destroyBtn.addEventListener('click', () => {
      const { element } = HSCopyMarkup.getInstance(copyBtn, true)

      element.destroy()

      destroyBtn.setAttribute('disabled', 'disabled')
      reinitBtn.removeAttribute('disabled')
    })

    // Reinit usage
    reinitBtn.addEventListener('click', () => {
      HSCopyMarkup.autoInit()

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
FlyonUI is powered by <a href="https://preline.co/plugins/html/copy-markup.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

{{< table >}}
PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-copy-markup`</span> | Activate a Copy Markup by specifying on an element. | `-` | `-`
<span class="text-nowrap">`data-copy-markup-delete-item`</span> | Deletes targeted markup element on click. | `-` | `-`
`:targetSelector` | Specifies the target element to copy. The value must be a valid selector. | string | `-`
`:wrapperSelector` | Specifies which element should be used for copying. The value must be a valid selector. | string | `-`
`:limit` | Specifies how many items you can copy until the button is disabled.| number | `null`
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSCopyMarkup` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`delete(target)` | <div>Remove the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node.</li></ul></div>
`destroy()` | Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSCopyMarkup.getInstance(target, isInstance)` | <div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

Assign an ID to the button containing the `data-copy-markup` attribute, as demonstrated in the public method. To explore additional methods, you can copy them into the console.

{{< code addClass="!block" jsCode="true" >}}

<p class="mb-4">
  Which technologies have you primarily used? <span class="text-base-content font-medium">(Maximum two)</span>
</p>

<div id="wrapper-method" class="max-w-sm space-y-3">
  <div id="content-method" class="flex gap-2">
    <input type="text" class="input" placeholder="Enter Technology Name" />
  </div>
</div>

<div class="mt-4 flex max-w-sm flex-wrap justify-end gap-2">
  <button
    type="button"
    data-copy-markup='{
    "targetSelector": "#content-method",
    "wrapperSelector": "#wrapper-method",
    "limit": 2
    }'
    id="copy-method"
    class="btn btn-sm btn-primary"
  >
    <span class="icon-[tabler--plus]"></span>
    Add Technology
  </button>
  <button id="delete-method" class="btn btn-sm btn-soft btn-error">
    <span class="icon-[tabler--minus]"></span>
    Remove Technology
  </button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    const deleteBtn = document.querySelector('#delete-method')

    deleteBtn.addEventListener('click', () => {
      const copyMarkup = new HSCopyMarkup(document.querySelector('#copy-method'))
      copyMarkup.delete(document.querySelector('#content-method-0'))
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">Toggle the field to type text (public method).</p>

{{< code-highlight lang="js" >}}// This method is used in above example.
const deleteBtn = document.querySelector('#delete-method')

deleteBtn.addEventListener('click', () => {
  const copyMarkup = new HSCopyMarkup(document.querySelector('#copy-method'))
  copyMarkup.delete(document.querySelector('#content-method-0'))
})
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose">Toggle the field to type text (mixed).</p>
{{< code-highlight lang="js" >}}const { element } = HSCopyMarkup.getInstance('#copy-method', true);
const deleteBtn = document.querySelector('#delete-method');

deleteBtn.addEventListener('click', () => {
  element.delete(document.querySelector('#content-method-0'));
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose" id="destroy-method">Destroy instance.</p>

{{< code-highlight lang="js" >}}
const { element } = HSCopyMarkup.getInstance('#copy-markup', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION | RETURNING VALUE
`on:copy`| Called after target element is copied. | Copied element
`on:delete` | Called after target element is deleted. | Deleted element
{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

Assign an ID to the button containing the `data-copy-markup` attribute, and then use that ID to attach an event.
The example below demonstrates a use case of event usage. You can view the output in the console.

{{< code addClass="!block" jsCode="true" >}}

<p class="mb-4">
  Which technologies have you primarily used? <span class="text-base-content font-medium">(Maximum two)</span>
</p>

<div id="wrapper-event" class="max-w-sm space-y-3">
  <input id="content-event" type="text" class="input --prevent-on-load-init" placeholder="Enter Technology Name" />
</div>

<div class="mt-4 flex max-w-sm flex-wrap justify-end gap-2">
  <button
    type="button"
    data-copy-markup='{
    "targetSelector": "#content-event",
    "wrapperSelector": "#wrapper-event",
    "limit": 2
    }'
    id="copy-event"
    class="btn btn-sm btn-primary"
  >
    <span class="icon-[tabler--plus]"></span>
    Add Technology
  </button>
  <button id="delete-event" class="btn btn-sm btn-soft btn-error">
    <span class="icon-[tabler--minus]"></span>
    Remove Technology
  </button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    const el = HSCopyMarkup.getInstance('#copy-event')
    const deleteBtn2 = document.querySelector('#delete-event')

    deleteBtn2.addEventListener('click', () => {
      el.delete(document.querySelector('#content-event-0'))
    })

    el.on('copy', target => {
      console.log('target:', target)
    })
    el.on('delete', target => {
      console.log('target:', target)
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">Call any function on `copy` or `delete` example.</p>
{{< code-highlight lang="js" >}}const el = HSCopyMarkup.getInstance('#copy-event')
const deleteBtn2 = document.querySelector('#delete-event')

deleteBtn2.addEventListener('click', () => {
  el.delete(document.querySelector('#content-event-0'))
})

el.on('copy', target => {
  console.log('target:', target)
})

el.on('delete', target => {
  console.log('target:', target)
})

{{< /code-highlight >}}
