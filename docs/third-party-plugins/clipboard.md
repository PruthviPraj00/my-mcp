---
title: "Clipboard"
description: "Clipboard components are vital tools that simplify data copying and pasting in applications, boosting user efficiency and enhancing overall interaction."
bg_image: "svg/third-party-plugins/clipboard.svg"
components: 5
menu:
  main:
    parent: "third party plugins"

previous: Apex Charts
previousLink: third-party-plugins/apex-charts/

next: Datamaps
nextLink: third-party-plugins/datamaps/

pageJS:
  - "/js/helper/helper-clipboard.js"

vendorJS:
  - "https://cdn.jsdelivr.net/npm/clipboard@2.0.11/dist/clipboard.min.js"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://clipboardjs.com/" target="_blank" class="link link-primary font-semibold">Clipboard JS</a> into your project for efficient text copying functionality.

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical w-full mb-12 ps-0">
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        1
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Install Clipboard.js</div>
      <p>
        Install
        <code>clipboard</code>
        via npm.
      </p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm i clipboard{{< /code-highlight >}}
    </div>
    <hr class="rounded-none border-transparent !w-0.5" />
  </li>

  <!-- Third-party JS include -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Include Clipboard.js in Your Page</div>
      <p>
        To integrate Clipboard.js, add the following
        <code>&lt;script&gt;</code>
        tag near the end of your
        <code>&lt;/body&gt;</code>
        section.
      </p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}<script src="../path/to/clipboard/dist/clipboard.min.js"></script>{{< /code-highlight >}}
      <div class="text-base-content my-3 font-semibold">Since no custom CSS overrides are required, you can also use a CDN link.</div>
      <p>Include the following <code>&lt;script&gt;</code> tag near the end of your <code>&lt;/body&gt;</code> section:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}<script src="https://cdn.jsdelivr.net/npm/clipboard@2.0.11/dist/clipboard.min.js"></script>{{< /code-highlight >}}
      <p class="!mt-2.5">
        Alternatively, choose from a variety of CDN providers listed
        <a href="https://github.com/zenorocha/clipboard.js/wiki/CDN-Providers" class="link link-primary inline-flex items-center gap-1" target="blank">
          here
          <span class="icon-[tabler--external-link]"></span>
        </a>.
      </p>
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Initialization & Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        3
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Add the FlyonUI Helper JavaScript</div>
      <p>
      Ensure the <code>helper-clipboard.js</code> file is included after the <code>clipboard.js</code> file.
      </p>
      <p>
        For more options and configurations, refer to the Clipboard.js
        <a href="https://clipboardjs.com/" class="link link-primary inline-flex items-center gap-1" target="blank">
          documentation
          <span class="icon-[tabler--external-link]"></span>
        </a>.
      </p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="html" >}}
<script src="./node_modules/flyonui/dist/helper-clipboard.js"></script>
{{< /code-highlight >}}
      </div>
  </li>
</ul>

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

To copy text from a specific element, target it using its `Id` and assign it to the `data-clipboard-target` attribute in the trigger button. Additionally, set the value of the `data-clipboard-action` attribute to `copy`. This setup ensures that clicking the button will copy the text from the targeted element to the clipboard.

The following example demonstrates the default usage of the copy clipboard component.

{{< code >}}

<div class="rounded-box inline-flex items-center gap-1 p-1 shadow-base-300/20 shadow-sm">
  <code id="clipboard-basic" class="px-2 text-base-content text-sm font-medium">npm install flyonui</code>
  <button type="button" class="js-clipboard btn btn-square btn-text" aria-label="Copy text to clipboard" data-clipboard-target="#clipboard-basic" data-clipboard-action="copy">
    <span class="js-clipboard-default icon-[tabler--clipboard] size-5 transition"></span>
    <span class="js-clipboard-success icon-[tabler--clipboard-check] text-primary hidden size-5"></span>
  </button>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Copy from input -->

{{< headname level="3" >}} Copy from input {{< /headname >}}

Use the `js-clipboard-success-text` component class to display default text, and set the value of the data attribute `data-clipboard-success-text` to specify the text that should appear after the content is successfully copied to the clipboard.

Below example showcases how to utilize the copy clipboard component with an input field.

{{< code >}}

<div class="flex w-full gap-x-3">
  <input id="clipboard-input" type="text" class="input" value="https://www.flyonui.com/design/figma/12345" aria-label="Text to copy" />
  <button type="button" class="js-clipboard btn btn-primary" data-clipboard-target="#clipboard-input" data-clipboard-action="copy" data-clipboard-success-text="Copied!">
    <span class="js-clipboard-default icon-[tabler--clipboard] size-5 transition"></span>
    <span class="js-clipboard-success icon-[tabler--clipboard-check] hidden size-5"></span>
    <span class="js-clipboard-success-text">Copy</span>
  </button>
</div>
{{< /code >}}

<!-- With input group -->

{{< headname level="3" >}} With input group {{< /headname >}}

Below example showcases how to utilize the copy clipboard component with an input group.

{{< code >}}

<label class="input max-w-md flex space-x-3">
  <span class="icon-[tabler--link] text-base-content/80 my-auto size-5 shrink-0"></span>
  <input id="clipboard-input-group" type="text" class="grow" value="https://www.flyonui.com/design/figma/12345" />
  <button type="button" class="js-clipboard my-auto size-5" aria-label="Copy text to clipboard" data-clipboard-target="#clipboard-input-group" data-clipboard-action="copy">
    <span class="js-clipboard-default icon-[tabler--clipboard] size-5 transition"></span>
    <span class="js-clipboard-success icon-[tabler--clipboard-check] text-primary hidden size-5"></span>
  </button>
</label>
{{< /code >}}

<!-- With tooltip -->

{{< headname level="3" >}} With tooltip {{< /headname >}}

Below examples showcases how to utilize the copy clipboard functionality with tooltips.

<!-- With success message only -->

{{< headname level="4" >}} With success message only {{< /headname >}}

The example below illustrates the use of the copy clipboard component along with a tooltip displaying a static success message only.

{{< code >}}

<div class="rounded-box flex min-w-60 items-center justify-between gap-x-4 px-4 py-3 shadow-base-300/20 shadow-sm">
  <code>
    <span class="text-base-content me-2 text-lg font-medium">$</span>
    <span id="clipboard-tooltip" class="text-base-content">npm i flyonui</span>
  </code>
  <div class="js-clipboard tooltip [--trigger:focus]" data-clipboard-target="#clipboard-tooltip" data-clipboard-action="copy">
    <span class="tooltip-toggle flex items-center justify-center">
      <span class="js-clipboard-default icon-[tabler--clipboard] size-6 transition"></span>
      <span class="js-clipboard-success icon-[tabler--clipboard-check] text-primary hidden size-6"></span>
    </span>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Copied!</span>
    </span>
  </div>
</div>
{{< /code >}}

<!-- With dynamic success message -->

{{< headname level="4" >}} With dynamic success message {{< /headname >}}

The example below illustrates the use of the copy clipboard component along with a tooltip displaying a dynamic success message.

{{< code >}}

<div class="rounded-box flex min-w-60 items-center justify-between gap-x-4 px-4 py-3 shadow-base-300/20 shadow-sm">
  <code>
    <span class="text-base-content me-2 text-lg font-medium">$</span>
    <span id="clipboard-tooltip-on-hover" class="text-base-content">npm i flyonui</span>
  </code>
  <button type="button" class="js-clipboard tooltip" aria-label="Copy text to clipboard" data-clipboard-target="#clipboard-tooltip-on-hover" data-clipboard-action="copy" data-clipboard-success-text="Copied!">
    <span class="tooltip-toggle flex items-center justify-center">
      <span class="js-clipboard-default icon-[tabler--clipboard] size-6 transition"></span>
      <span class="js-clipboard-success icon-[tabler--clipboard-check] text-primary hidden size-6"></span>
    </span>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body js-clipboard-success-text">Copy</span>
    </span>
  </button>
</div>
{{< /code >}}

<!-- Extended clipboard with tooltip -->

{{< headname level="4" >}} Extended clipboard with tooltip {{< /headname >}}

Below is an example demonstrating the extended functionality of the copy clipboard component. It includes a centered tooltip that dynamically displays a success message. This setup enables copying by clicking anywhere within the element.

{{< code >}}

<input type="hidden" id="clipboard-tooltip-centered" value="npm i flyonui" />

<button type="button" class="js-clipboard tooltip rounded-box relative flex min-w-60 items-center justify-between gap-x-4 px-4 py-3 shadow-base-300/20 shadow-sm" data-clipboard-target="#clipboard-tooltip-centered" data-clipboard-action="copy" data-clipboard-success-text="Copied!">
  <code>
    <span class="text-base-content font-medium">$</span>
    <span class="text-base-content">npm i flyonui</span>
  </code>
  <span class="flex items-center justify-center">
    <span class="js-clipboard-default icon-[tabler--clipboard] size-6 transition"></span>
    <span class="js-clipboard-success icon-[tabler--clipboard-check] text-primary hidden size-6"></span>
  </span>
  <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
    <span class="tooltip-body js-clipboard-success-text">Copy</span>
  </span>
</button>
{{< /code >}}

<!-- In modals -->

{{< headname level="3" >}} In modals {{< /headname >}}

The example below illustrates the use of the copy clipboard component in modals.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="clipboard-modal" data-overlay="#clipboard-modal">Open modal</button>

<div id="clipboard-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Personal Access Token</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#clipboard-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <div class="flex gap-3 pt-2">
          <div class="input">
            <span class="icon-[tabler--key] text-base-content/80 my-auto me-3 size-5 shrink-0"></span>
            <label class="sr-only" for="clipboard-input-modal">Full Name</label>
            <input type="text" class="grow" placeholder="John Doe" id="clipboard-input-modal" value="9A8b7c6d-5e4F-3g2h-1I0j-k9l8m7n6O5p4-q3r2s1t0-u9v8W7x6y5z4-a1b2c3d4e5F6" />
          </div>
          <button type="button" class="js-clipboard btn btn-primary h-9.5" data-clipboard-target="#clipboard-input-modal" data-clipboard-action="copy" data-clipboard-success-text="Copied!">
            <span class="js-clipboard-default icon-[tabler--clipboard] size-5 transition"></span>
            <span class="js-clipboard-success icon-[tabler--clipboard-check] hidden size-5"></span>
            <span class="js-clipboard-success-text">Copy</span>
          </button>
        </div>
        <p class="mt-3 text-xs">
          Do not share this PAT key with anyone or lose it. Add this key in your own PAT key in your account & actions.
          If you have any questions or need further assistance, please contact our support team.
        </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#clipboard-modal">Close</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Copy source code block -->

{{< headname level="3" >}} Copy source code block {{< /headname >}}

The example below illustrates the use of the copy clipboard component in source code block.

{{< code >}}

<div class="mockup-code bg-base-200/40 rounded-box relative pb-0 before:content-none">
  <pre id="clipboard-source-code" class="overflow-x-auto text-sm"><code>const clipboard = new ClipboardJS(el, {
    text: trigger => {
    const clipboardText = trigger.dataset.clipboardText

    if (clipboardText) return clipboardText

    const clipboardTarget = trigger.dataset.clipboardTarget
    const $element = document.querySelector(clipboardTarget)

    if ($element.tagName === 'SELECT' || $element.tagName === 'INPUT' || $element.tagName === 'TEXTAREA')
      return $element.value
    else return $element.textContent
    }

})</code></pre>

  <button type="button" class="js-clipboard tooltip absolute end-2 top-2" aria-label="Copy text to clipboard" data-clipboard-target="#clipboard-source-code" data-clipboard-action="copy" data-clipboard-success-text="Copied!">
    <span class="toolttip-toggle btn btn-square btn-primary">
      <span class="js-clipboard-default icon-[tabler--clipboard] size-5 transition"></span>
      <span class="js-clipboard-success icon-[tabler--clipboard-check] hidden size-5"></span>
    </span>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body js-clipboard-success-text">Copy</span>
    </span>
  </button>
</div>
{{< /code >}}
