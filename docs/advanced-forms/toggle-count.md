---
title: "Toggle Count"
components: 3
description: "The Toggle Count Component simplifies switching between different values, aiding comparison and decision-making on pricing pages."
bg_image: "svg/form-elements/toggle-count.svg"
menu:
  main:
    parent: "advanced forms"

previous: Strong Password
previousLink: advanced-forms/strong-password/

next: Toggle Password
nextLink: advanced-forms/toggle-password/

requires_js: true
pageJS:
  - "/js/pages/toggle-count.js"
---

{{< callout "info" >}}
Toggle Count components are adopted from <a href="https://preline.co/docs/toggle-count.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class Table -->

{{< class-table >}}
switch| component | Component class for switch.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- With radio -->

{{< headname level="3" >}} With radio {{< /headname >}}

Basic example of toggle count with radio input.

{{< code addClass="flex-col" >}}

<div class="mb-3 flex justify-center">
  <div id="toggle-count" class="border-base-content/20 flex gap-0.5 rounded-field border p-0.5">
    <label for="toggle-count-monthly" class="btn btn-sm btn-text has-checked:btn-active">
      <span>Monthly</span>
      <input id="toggle-count-monthly" name="toggle-count" type="radio" class="hidden" checked="" />
    </label>
    <label for="toggle-count-annual" class="btn btn-sm btn-text has-checked:btn-active">
      <span>Annually</span>
      <input id="toggle-count-annual" name="toggle-count" type="radio" class="hidden" />
    </label>
  </div>
</div>

<div class="border-base-content/20 grid grid-cols-1 rounded-xl border sm:grid-cols-2 md:grid-cols-4">
  <div class="flex flex-col items-center gap-2 p-4">
    <p class="mb-1 font-medium">Free</p>
    <div class="text-base-content flex gap-x-1 font-semibold">
      <span class="text-xl">$</span>
      <p
        data-toggle-count='{
          "target": "#toggle-count",
          "min": 0,
          "max": 0
        }'
        class="text-3xl sm:text-5xl">
        0
      </p>
    </div>
    <p class="text-sm text-center">All the basics for the business that are just getting started!</p>
  </div>
  <div class="flex flex-col items-center gap-2 p-4">
    <p class="mb-1 font-medium">Essential</p>
    <div class="text-base-content flex gap-x-1 font-semibold">
      <span class="text-xl">$</span>
      <p
        data-toggle-count='{
          "target": "#toggle-count",
          "min": 15,
          "max": 159
        }'
        class="text-3xl sm:text-5xl">
        15
      </p>
    </div>
    <p class="text-sm text-center">All the essentials for the business that need some added support!</p>
  </div>
  <div class="flex flex-col items-center gap-2 p-4">
    <div class="flex justify-between">
      <p class="mb-1 font-medium">Standard</p>
    </div>
    <div class="text-base-content flex gap-x-1 font-semibold">
      <span class="text-xl">$</span>
      <p
        data-toggle-count='{
          "target": "#toggle-count",
          "min": 60,
          "max": 699
        }'
        class="text-3xl sm:text-5xl">
        60
      </p>
    </div>
    <p class="text-sm text-center">All the standards for the businesses that need more growth.</p>
  </div>
  <div class="flex flex-col items-center gap-2 p-4">
    <p class="mb-1 font-medium">Pro</p>
    <div class="text-base-content flex gap-x-1 font-semibold">
      <span class="text-xl">$</span>
      <p
        data-toggle-count='{
          "target": "#toggle-count",
          "min": 100,
          "max": 999
        }'
        class="text-3xl sm:text-5xl">
        100
      </p>
    </div>
    <p class="text-sm text-center">All the advanced features with pro support & customizations!</p>
  </div>
</div>
{{< /code >}}

<!-- With switch -->

{{< headname level="3" >}} With switch {{< /headname >}}

Basic example of toggle count with switch(checkbox) input.

{{< code addClass="flex-col" >}}

<div class="mb-4 flex justify-center">
  <div class="flex items-center">
    <label for="toggle-count-switch" class="inline-block p-2">
      <span class="text-sm cursor-pointer">Monthly</span>
    </label>
    <input id="toggle-count-switch" name="toggle-count-switch" type="checkbox" class="switch" />
    <label for="toggle-count-switch" class="inline-block p-2">
      <span class="text-sm cursor-pointer">Annually</span>
    </label>
  </div>
</div>

<div class="border-base-content/20 grid grid-cols-1 rounded-xl border sm:grid-cols-2 md:grid-cols-4">
  <div class="flex flex-col items-center gap-2 p-4">
    <p class="mb-1 font-medium">Free</p>
    <div class="text-base-content flex gap-x-1 font-semibold">
      <span class="text-xl">$</span>
      <p
        data-toggle-count='{
          "target": "#toggle-count-switch",
          "min": 0,
          "max": 0
        }'
        class="text-3xl sm:text-5xl">
        0
      </p>
    </div>
    <p class="text-sm text-center">All the basics for the business that are just getting started!</p>
  </div>
  <div class="flex flex-col items-center gap-2 p-4">
    <p class="mb-1 font-medium">Essential</p>
    <div class="text-base-content flex gap-x-1 font-semibold">
      <span class="text-xl">$</span>
      <p
        data-toggle-count='{
          "target": "#toggle-count-switch",
          "min": 15,
          "max": 159
        }'
        class="text-3xl sm:text-5xl">
        15
      </p>
    </div>
    <p class="text-sm text-center">All the essentials for the business that need some added support!</p>
  </div>
  <div class="flex flex-col items-center gap-2 p-4">
    <div class="flex justify-between">
      <p class="mb-1 font-medium">Standard</p>
    </div>
    <div class="text-base-content flex gap-x-1 font-semibold">
      <span class="text-xl">$</span>
      <p
        data-toggle-count='{
          "target": "#toggle-count-switch",
          "min": 60,
          "max": 699
        }'
        class="text-3xl sm:text-5xl">
        60
      </p>
    </div>
    <p class="text-sm text-center">All the standards for the businesses that need more growth.</p>
  </div>
  <div class="flex flex-col items-center gap-2 p-4">
    <p class="mb-1 font-medium">Pro</p>
    <div class="text-base-content flex gap-x-1 font-semibold">
      <span class="text-xl">$</span>
      <p
        data-toggle-count='{
          "target": "#toggle-count-switch",
          "min": 100,
          "max": 999
        }'
        class="text-3xl sm:text-5xl">
        100
      </p>
    </div>
    <p class="text-sm text-center">All the advanced features with pro support & customizations!</p>
  </div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Pricing cards -->

{{< headname level="3" >}} Pricing cards {{< /headname >}}

Basic example demonstrates use of toggle count in pricing cards.

{{< code addClass="flex-col" >}}

<div class="mb-3 flex justify-center">
  <div id="toggle-price-count" class="border-base-content/20 flex gap-0.5 rounded-field border p-0.5">
    <label for="toggle-price-count-monthly" class="btn btn-sm btn-text has-checked:btn-active">
      <span>Monthly</span>
      <input id="toggle-price-count-monthly" name="toggle-price-count" type="radio" class="hidden" checked="" />
    </label>
    <label for="toggle-price-count-annual" class="btn btn-sm btn-text has-checked:btn-active">
      <span>Annually</span>
      <input id="toggle-price-count-annual" name="toggle-price-count" type="radio" class="hidden" />
    </label>
  </div>
</div>

<div class="grid grid-cols-1 items-center gap-2 sm:grid-cols-2 md:grid-cols-3">
  <div class="card border-base-content/20 border shadow-none">
    <div class="card-body gap-3 text-center">
      <div>
        <span class="text-base-content text-xl font-medium ">Basic</span>
        <p class="text-sm truncate">A simple start for everyone</p>
      </div>
      <div class="text-primary flex justify-center gap-x-1">
        <span class="text-base-content/80 text-xl">$</span>
        <span
          data-toggle-count='{
          "target": "#toggle-price-count",
          "min": 3,
          "max": 29
        }'
          class="text-5xl font-semibold">
          3
        </span>
      </div>
      <ul class="text-sm space-y-3">
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">100 responses a month</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Unlimited forms & surveys</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Unlimited fields</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Basic form creation tools</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Up to 2 subdomains</span>
        </li>
      </ul>
      <button class="btn btn-outline btn-sm btn-primary mt-4">UPGRADE</button>
    </div>
  </div>
  <div class="card border-primary border shadow-none">
    <div class="relative">
      <span class="badge badge-soft badge-sm badge-primary absolute end-2 top-2">Popular</span>
    </div>
    <div class="card-body gap-3 text-center">
      <div>
        <span class="text-base-content text-xl font-medium ">Standard</span>
        <p class="text-sm">For small to medium businesses</p>
      </div>
      <div class="text-primary flex justify-center gap-x-1">
        <span class="text-base-content/80 text-xl">$</span>
        <span
          data-toggle-count='{
          "target": "#toggle-price-count",
          "min": 15,
          "max": 159
        }'
          class="text-5xl font-semibold">
          15
        </span>
      </div>
      <ul class="text-sm space-y-3">
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Unlimited responses</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Unlimited forms & surveys</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Instagram profile page</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Google Docs integration</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Custom Landing page</span>
        </li>
      </ul>
      <button class="btn btn-sm btn-primary mt-4">UPGRADE</button>
    </div>
  </div>
  <div class="card border-base-content/20 border shadow-none">
    <div class="card-body gap-3 text-center">
      <div>
        <span class="text-base-content text-xl font-medium">Enterprise</span>
        <p class="text-sm truncate">Solution for big organizations</p>
      </div>
      <div class="text-primary flex justify-center gap-x-1">
        <span class="text-base-content/80 text-xl">$</span>
        <span
          data-toggle-count='{
          "target": "#toggle-price-count",
          "min": 79,
          "max": 999
        }'
          class="text-5xl font-semibold">
          79
        </span>
      </div>
      <ul class="text-sm space-y-3">
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">PayPal payments</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Logic Jumps</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">File upload with 5GB storage</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Custom domain support</span>
        </li>
        <li class="flex items-center space-x-3">
          <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
            <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
          </span>
          <span class="text-base-content/80 truncate">Stripe integration</span>
        </li>
      </ul>
      <button class="btn btn-outline btn-sm btn-primary mt-4">UPGRADE</button>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Destroy/Reinitialize -->
{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}
The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a toggle count.

{{< code addClass="!block" jsCode="true" >}}
<div id="toggle-count-destroy">
  <div class="mb-3 flex justify-center">
    <div id="toggle-count-example" class="border-base-content/20 flex gap-0.5 rounded-field border p-0.5">
      <label for="toggle-count-monthly-based" class="btn btn-sm btn-text has-checked:btn-active">
        <span>Monthly</span>
        <input id="toggle-count-monthly-based" name="toggle-count-example" type="radio" class="hidden" checked="" />
      </label>
      <label for="toggle-count-annual-based" class="btn btn-sm btn-text has-checked:btn-active">
        <span>Annually</span>
        <input id="toggle-count-annual-based" name="toggle-count-example" type="radio" class="hidden" />
      </label>
    </div>
  </div>
  
  <div class="border-base-content/20 grid grid-cols-1 rounded-xl border sm:grid-cols-2 md:grid-cols-4">
    <div class="flex flex-col items-center gap-2 p-4">
      <p class="mb-1 font-medium">Free</p>
      <div class="text-base-content flex gap-x-1 font-semibold">
        <span class="text-xl">$</span>
        <p
          data-toggle-count='{
            "target": "#toggle-count-example",
            "min": 0,
            "max": 0
          }'
          class="text-3xl sm:text-5xl">
          0
        </p>
      </div>
      <p class="text-sm text-center">All the basics for the business that are just getting started!</p>
    </div>
    <div class="flex flex-col items-center gap-2 p-4">
      <p class="mb-1 font-medium">Essential</p>
      <div class="text-base-content flex gap-x-1 font-semibold">
        <span class="text-xl">$</span>
        <p
          data-toggle-count='{
            "target": "#toggle-count-example",
            "min": 15,
            "max": 159
          }'
          class="text-3xl sm:text-5xl">
          15
        </p>
      </div>
      <p class="text-sm text-center">All the essentials for the business that need some added support!</p>
    </div>
    <div class="flex flex-col items-center gap-2 p-4">
      <div class="flex justify-between">
        <p class="mb-1 font-medium">Standard</p>
      </div>
      <div class="text-base-content flex gap-x-1 font-semibold">
        <span class="text-xl">$</span>
        <p
          data-toggle-count='{
            "target": "#toggle-count-example",
            "min": 60,
            "max": 699
          }'
          class="text-3xl sm:text-5xl">
          60
        </p>
      </div>
      <p class="text-sm text-center">All the standards for the businesses that need more growth.</p>
    </div>
    <div class="flex flex-col items-center gap-2 p-4">
      <p class="mb-1 font-medium">Pro</p>
      <div class="text-base-content flex gap-x-1 font-semibold">
        <span class="text-xl">$</span>
        <p
          data-toggle-count='{
            "target": "#toggle-count-example",
            "min": 100,
            "max": 999
          }'
          class="text-3xl sm:text-5xl">
          100
        </p>
      </div>
      <p class="text-sm text-center">All the advanced features with pro support & customizations!</p>
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
    const toggleCounts = document.querySelectorAll('#toggle-count-destroy [data-toggle-count]')
    const destroyBtn = document.querySelector('#destroy-btn')
    const reinitBtn = document.querySelector('#reinit-btn')

    // Destroy usage
    destroyBtn.addEventListener('click', () => {
      toggleCounts.forEach(el => {
        const { element } = HSToggleCount.getInstance(el, true)

        element.destroy()
      })

      destroyBtn.setAttribute('disabled', 'disabled')
      reinitBtn.removeAttribute('disabled')
    })

    // Reinit usage
    reinitBtn.addEventListener('click', () => {
      HSToggleCount.autoInit()

      reinitBtn.setAttribute('disabled', 'disabled')
      destroyBtn.removeAttribute('disabled')
    })
  })
</script>
{{< /code >}}

<!-------------------- Options usage -------------------->

{{< headname level="2" >}} Options usage {{< /headname >}}

<!-- Current Index -->

{{< headname level="3" >}} Duration {{< /headname >}}

Assign the value of the `data-toggle-count` attribute as an object. Within this object, set the `duration` option to `number` to set counting speed(animation). By default, its value is `700`.

{{< code >}}

<div class="card w-40">
  <div class="text-base-content card-body font-semibold">
    <p
      data-toggle-count='{
        "target": "#toggle-duration-usage",
        "min": 10,
        "max": 100,
        "duration":100
      }'
      class="mb-2 text-center text-5xl">
      10
    </p>
    <input id="toggle-duration-usage" name="toggle-count-method" type="checkbox" class="switch switch-primary mx-auto" aria-label="toggle count" />
  </div>
</div>

{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/toggle-count.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

{{< table >}}
PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-toggle-count`</span> | Activate a Toggle Count by specifying on an element. | `-` | `-`
`:target` (required) | Specifies default number. | string | `-`
`:min` | Specifies the target element to copy. The value must be a valid selector. | number | `0`
`:max` | Specifies the number to which the count up will go. | number | `0`
`:duration` | Counting speed (animation). | number | `700`
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSToggleCount` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`countUp()` | Force count up.
`countDown()` | Force count down.
`destroy()` | Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSToggleCount.getInstance(target, isInstance)` | <div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

Assign an ID to the button containing the `data-toggle-count` attribute, as demonstrated in the public method. To explore additional methods, you can copy them into the console.

{{< code jsCode="true" addClass="flex-col" >}}

<div class="card w-40">
  <div class="text-base-content card-body font-semibold">
    <input id="toggle-input-method" name="toggle-count-method" type="checkbox" class="hidden" />
    <p
      id="toggle-count-method"
      data-toggle-count='{
        "target": "#toggle-input-method",
        "min": 10,
        "max": 100
      }'
      class="text-center text-5xl">
      10
    </p>
  </div>
  <div class="flex justify-between p-2 pt-0">
    <button id="count-down-method" class="btn btn-soft btn-error btn-square" aria-label="decrement">
      <span class="icon-[tabler--minus]"></span>
    </button>
    <button id="count-up-method" class="btn btn-soft btn-primary btn-square" aria-label="increment">
      <span class="icon-[tabler--plus]"></span>
    </button>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const toggleCount = new HSToggleCount(document.querySelector('#toggle-count-method'))
    const countUpBtn = document.querySelector('#count-up-method')
    const countDownBtn = document.querySelector('#count-down-method')
    
    countUpBtn.addEventListener('click', () => {
      toggleCount.countUp()
    })
    countDownBtn.addEventListener('click', () => {
      toggleCount.countDown()
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">Force count up (public method).</p>

{{< code-highlight lang="js" >}}// This method is used in above example.
const toggleCount = new HSToggleCount(document.querySelector('#toggle-count-method'));
const countUpBtn = document.querySelector('#count-up-method');
const countDownBtn = document.querySelector('#count-down-method');

countUpBtn.addEventListener('click', () => {
  toggleCount.countUp();
});

countDownBtn.addEventListener('click', () => {
  toggleCount.countDown();
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose">Force count up (mixed).</p>
{{< code-highlight lang="js" >}}const { element } = HSToggleCount.getInstance('#toggle-count-method', true);
const countUpBtn = document.querySelector('#count-up-method');

countUpBtn.addEventListener('click', () => {
  element.countUp();
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose" id="destroy-method">Destroy instance.</p>

{{< code-highlight lang="js" >}}
const { element } = HSToggleCount.getInstance('#toggle-count-destroy', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}
