---
title: "Collapse"
components: 4
description: "Toggle the visibility of the content in the collapse component, allowing users to expand or collapse sections as desired."
bg_image: "svg/components/collapse.svg"
menu:
  main:
    parent: "components"

previous: Chat Bubble
previousLink: components/chat-bubble/

next: Diff
nextLink: components/diff/

requires_js: true

pageJS:
  - "/js/pages/collapse.js"
---

{{< callout "info" >}}
Collapse components are adopted from <a href="https://preline.co/docs/collapse.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class table -->

{{< class-table >}}
collapse | component | The class for the collapse container which contains content.
collapse-toggle | part | Class for button.
collapse-open:{tw-utility-class} | variant | Modifies tailwind classes when the collapse menu is open.
{{< /class-table >}}

<!-------------------- Basic -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

This basic example of collapse component.

{{< code addClass="!block" >}}

<button type="button" class="collapse-toggle btn btn-primary" id="basic-collapse" aria-expanded="false" aria-controls="basic-collapse-heading" data-collapse="#basic-collapse-heading">
  Collapse
  <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
</button>
<div id="basic-collapse-heading" class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="basic-collapse">
  <div class="border-base-content/25 mt-3 rounded-md border p-3">
    <p class="text-base-content/80">
      The collapsible body remains concealed by default until the collapse plugin dynamically adds specific classes. These classes are instrumental in styling each element, dictating the overall appearance, and managing visibility through CSS transitions.
    </p>
  </div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Background -->

{{< headname level="3" >}} Background {{< /headname >}}

The collapse container features a background color.

{{< code addClass="!block" >}}

<button type="button" class="collapse-toggle btn btn-primary" id="shadow-collapse" aria-expanded="false" aria-controls="shadow-collapse-heading" data-collapse="#shadow-collapse-heading" >
  Collapse
  <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
</button>
<div id="shadow-collapse-heading" class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="shadow-collapse" >
  <div class="bg-primary/20 mt-3 rounded-md p-3">
    <p class="text-primary">
      The collapsible body remains concealed by default until the collapse plugin dynamically adds specific classes.
      These classes are instrumental in styling each element, dictating the overall appearance, and managing visibility
      through CSS transitions.
    </p>
  </div>
</div>
{{< /code >}}

<!-- Dropdown -->

{{< headname level="3" >}} Dropdown {{< /headname >}}

Below example show how can we use collapse inside a dropdown.

{{< callout "info" >}}
Please refer the {{< link link="overlays/dropdown/" addClass="link link-primary" >}}Dropdown{{< /link >}} documentation for more details.
{{< /callout >}}

{{< code >}}

<div class="dropdown relative inline-flex [--auto-close:inside]">
  <button id="dropdown-collapse" type="button" class="dropdown-toggle btn btn-primary" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
    Actions
    <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
  </button>
  <div class="dropdown-menu dropdown-open:opacity-100 hidden min-w-60" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-collapse">
    <div class="dropdown-header">Quick Actions</div>
    <div><a class="dropdown-item" href="#">Send Newsletter</a></div>
    <div><a class="dropdown-item" href="#">View Purchases</a></div>
    <div>
      <button id="nested-collapse-2" class="collapse-toggle dropdown-item justify-between" aria-expanded="false" aria-controls="nested-collapse-content" data-collapse="#nested-collapse-content" >
        More Options
        <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
      </button>
      <div class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="nested-collapse-2" id="nested-collapse-content" >
        <ul class="py-3 ps-3">
          <li><a class="dropdown-item" href="#">Download Documents</a></li>
          <li><a class="dropdown-item" href="#">Manage Team Account</a></li>
        </ul>
      </div>
    </div>
    <div><a class="dropdown-item" href="#">Logout</a></div>
  </div>
</div>
{{< /code >}}

<!-- Show/Hide -->

{{< headname level="3" >}} Show/Hide {{< /headname >}}

Press the buttons below to toggle the visibility of another element.

{{< code addClass="flex-col" >}}

<div>
  <h6 class="text-base-content text-base">How can I track my order?</h6>
  <div id="show-hide-collapse-heading" class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="show-hide-collapse" >
    <p class="text-base-content/80">
      To track your order, simply log in to your account and navigate to the order history section. You'll find detailed
      information about your order status and tracking number there.
    </p>
  </div>
</div>

<button type="button" class="collapse-toggle link link-primary inline-flex items-center" id="show-hide-collapse" aria-expanded="false" aria-controls="show-hide-collapse-heading" data-collapse="#show-hide-collapse-heading" >
  <span class="collapse-open:hidden">Read more</span>
  <span class="collapse-open:block hidden">Read less</span>
  <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 ms-2 size-4"></span>
</button>
{{< /code >}}

<!-- Destroy/Reinitialize -->

{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}

The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a collapse element.

{{< code addClass="!block" jsCode="true" >}}

<button type="button" class="collapse-toggle btn btn-primary" id="collapse-destroy" aria-expanded="false" aria-controls="collapse-destroy-heading" data-collapse="#collapse-destroy-heading">
  Collapse
  <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
</button>
<div id="collapse-destroy-heading" class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="collapse-destroy">
  <div class="border-base-content/25 mt-3 rounded-md border p-3">
    <p class="text-base-content/80">
      The collapsible body remains concealed by default until the collapse plugin dynamically adds specific classes. These classes are instrumental in styling each element, dictating the overall appearance, and managing visibility through CSS transitions.
    </p>
  </div>
</div>

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    ;(function () {
      const collapse = document.querySelector('#collapse-destroy')
      const destroy = document.querySelector('#destroy-btn')
      const reinit = document.querySelector('#reinit-btn')

      destroy.addEventListener('click', () => {
        const { element } = HSCollapse.getInstance(collapse, true)
        element.destroy()

        destroy.setAttribute('disabled', 'disabled')
        reinit.removeAttribute('disabled')
      })

      reinit.addEventListener('click', () => {
        HSCollapse.autoInit()

        reinit.setAttribute('disabled', 'disabled')
        destroy.removeAttribute('disabled')
      })
    })()
  });
</script>
{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/collapse.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< table >}}
PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-collapse`</span>| <span class="text-pretty">Collapse the container for the given ID.</span>|string|`null`

{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSCollapse` object exists within the global `window` object.

{{< table >}}

METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`show()`| Open collapsed item.
`hide()`| Collapse item.
`destroy()`| Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSCollapse.getInstance(target)`|<div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li></ul></div>
`HSCollapse.show(target)`|Open collapsed item.
`HSCollapse.hide(target)`|Collapse item.
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

The method is triggered by the Id of the button. Below, you'll find example of public methods. To use other methods copy a method from below and paste it into your console, then try clicking the corresponding button to see it in action.

{{< code jsCode="true" addClass="!block" >}}

<div class="mb-4 flex gap-3">
  <button type="button" class="btn btn-primary" id="show-btn">Show</button>
  <button type="button" class="btn btn-primary" id="hide-btn">Hide</button>
</div>
<div>
  <button type="button" class="collapse-toggle btn btn-primary" id="method-collapse" aria-expanded="false" aria-controls="method-collapse-heading" data-collapse="#method-collapse-heading" disabled>
    Collapse
    <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
  </button>
  <div id="method-collapse-heading" class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="method-collapse" >
    <div class="border-base-content/25 mt-3 rounded-md border p-3">
      <p class="text-base-content/80">
        The collapsible body remains concealed by default until the collapse plugin dynamically adds specific classes.
        These classes are instrumental in styling each element, dictating the overall appearance, and managing
        visibility through CSS transitions.
      </p>
    </div>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const collapse = new HSCollapse(document.querySelector('#method-collapse'))
    const showBtn = document.querySelector('#show-btn')
    const hideBtn = document.querySelector('#hide-btn')

    showBtn.addEventListener('click', () => {
    collapse.show()
    })
    hideBtn.addEventListener('click', () => {
      collapse.hide()
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">Open item (public method).</p>

{{< code-highlight lang="js" >}}// This method is used in above example.
const collapse = new HSCollapse(document.querySelector('#method-collapse'));
const showBtn = document.querySelector('#show-btn');

showBtn.addEventListener('click', () => {
  collapse.show();
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose">Open item (static method).</p>
{{< code-highlight lang="js" >}}const showBtn = document.querySelector('#show-btn');

showBtn.addEventListener('click', () => {
  HSCollapse.show('#method-collapse');
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose">Open item (mixed).</p>
{{< code-highlight lang="js" >}}const { element } = HSCollapse.getInstance('#method-collapse', true);
const showBtn = document.querySelector('#show-btn');

showBtn.addEventListener('click', () => {
  element.show();
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose" id="destroy-method">Destroy instance</p>
{{< code-highlight lang="js" >}}const { element } = HSCollapse.getInstance('#method-collapse', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy()
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION
`on:open`|Called when any item is opened.
`on:hide`|Called when any item is closed.
{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

The event is triggered by the ID of the button.

{{< code jsCode="true" addClass="!block" >}}

<button type="button" class="collapse-toggle btn btn-primary" id="event-collapse" data-collapse="#event-collapse-heading" aria-expanded="false" aria-controls="event-collapse-heading" >
  Event
  <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
</button>
<div id="event-collapse-heading" class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="event-collapse" >
  <div class="border-base-content/25 mt-3 rounded-md border p-3">
    <p class="text-base-content/80">
      The collapsible body remains concealed by default until the collapse plugin dynamically adds specific classes.
      These classes are instrumental in styling each element, dictating the overall appearance, and managing visibility
      through CSS transitions.
    </p>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const { element } = HSCollapse.getInstance('#event-collapse', true)

    element.on('open', instance => { console.log('open') })
    element.on('hide', instance => { console.log('close') })
  })
</script>

{{< /code >}}

{{< code-highlight lang="js" >}}const { element } = HSCollapse.getInstance('#event-collapse', true)

element.on('open', (instance) => {console.log("open")});
element.on('hide', (instance) => {console.log("close")});
{{< /code-highlight >}}
