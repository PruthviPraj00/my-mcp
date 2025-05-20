---
title: "Javascript"
description: "This page describes how FlyonUI JavaScript functions, outlines its approach, and offers several examples to illustrate its use."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "getting-started"
    weight: 6

previous: Usage
previousLink: getting-started/usage/

next: Framework guides
nextLink: getting-started/framework-guides/
---

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins.html" class="link font-semibold link-primary" target="_blank">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-------------------- Helper for Dynamically Added Components -------------------->

{{< headsingle addClass="!mt-px" level="2" >}} Helper for Dynamically Added Components {{< /headsingle >}}

FlyonUI includes a JavaScript plugin method `autoInit()` in the `HSStaticMethods` object, which allows you to reinitialize elements that are dynamically added to the page. This is particularly useful when content is loaded via AJAX or when new UI components are added after the initial page load.

<!-- Example: Initializing All Components -->

{{< headsingle level="4" >}} Example: Initializing All Components {{< /headsingle >}}

To reinitialize **all** components on the page, you can use:

```javascript
window.HSStaticMethods.autoInit()
```

<!-- Initializing Specific Components -->

{{< headsingle level="4" >}} Initializing Specific Components {{< /headsingle >}}

If you only want to reinitialize **specific** components, such as carousels and dropdowns, you can pass an array of component names:

```javascript
window.HSStaticMethods.autoInit(["carousel", "dropdown"])
```

<!-------------------- Using `autoInit` with AJAX-Loaded Elements -------------------->

{{< headsingle level="2" >}} Using `autoInit` with AJAX-Loaded Elements {{< /headsingle >}}

Imagine a situation where you want to load options dynamically into a `<select>` dropdown via an AJAX request, and you want to initialize it only after the options are loaded.

<!-- HTML Example: -->

{{< headsingle level="4" >}} HTML Example: {{< /headsingle >}}

```html
<select
  id="dynamic-select-options"
  data-select='{
  "placeholder": "Select option..."
}'
  class="--prevent-on-load-init hidden"
></select>
<button type="button" id="load-options">Load Options</button>
```

<!-- JavaScript Example: -->

{{< headsingle level="4" >}} JavaScript Example: {{< /headsingle >}}

Here’s the script that dynamically fetches options from an API, populates the select element, and reinitializes it:

```javascript
document.getElementById("load-options").addEventListener("click", function () {
  loadOptions()
})

function loadOptions() {
  const xhr = new XMLHttpRequest()

  xhr.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      const options = JSON.parse(this.responseText)
      populateOptions(options)
    } else if (this.readyState == 4) {
      console.error("Failed to load options:", this.status, this.statusText)
    }
  }

  xhr.open("GET", "https://some-api.com/options", true)
  xhr.send()
}

function populateOptions(options) {
  const selectElement = document.getElementById("dynamic-select-options")
  selectElement.innerHTML = "" // Clear existing options

  options.forEach(option => {
    const optionElement = document.createElement("option")
    optionElement.value = option.value
    optionElement.textContent = option.text
    selectElement.appendChild(optionElement)
  })

  // Reinitialize the select element after populating it
  window.HSStaticMethods.autoInit(["select"])
}
```

<!-------------------- Using Static Methods in TypeScript (TS) -------------------->

{{< headsingle level="2" >}} Using Static Methods in TypeScript (TS) {{< /headsingle >}}

When working with TypeScript, you need to declare the interface for `HSStaticMethods` to prevent any errors or warnings about accessing it on the `window` object.

<!-- Example: -->

{{< headsingle level="4" >}} Example: {{< /headsingle >}}

```typescript
import { IStaticMethods } from "flyonui/flyonui"

declare global {
  interface Window {
    HSStaticMethods: IStaticMethods
  }
}

window.HSStaticMethods.autoInit() // No TS warnings/errors now
```

<br />

This makes sure that TypeScript knows about the `HSStaticMethods` object on the global `window`.

<!-------------------- Preventing Auto-Initialization -------------------->

{{< headsingle level="2" >}} Preventing Auto-Initialization {{< /headsingle >}}

Sometimes, you might not want certain elements to be automatically initialized on page load. For example, you may want to initialize them in response to a specific user interaction or an event. To do this, you can add the CSS class `--prevent-on-load-init` to the element.

<!-- HTML Example: -->

{{< headsingle level="4" >}} HTML Example: {{< /headsingle >}}

```html
<select
  data-select='{
    "placeholder": "Select option..."
  }'
  class="--prevent-on-load-init hidden"
>
  <option value="">Choose</option>
  <!-- Other options -->
</select>
```

<br />

Then, you can manually initialize these elements later when needed:

<!-- JavaScript Example: -->

{{< headsingle level="4" >}} JavaScript Example: {{< /headsingle >}}

```javascript
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-select].--prevent-on-load-init").forEach(el => {
    new HSSelect(el) // Manually initialize
  })
})
```
