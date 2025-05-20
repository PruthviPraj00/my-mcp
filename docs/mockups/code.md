---
title: "Code"
description: "Code mockup is used to show a block of code in a box that looks like a code editor."
bg_image: "svg/mockups/code.svg"
components: 1
menu:
  main:
    parent: "mockups"

previous: Browser
previousLink: mockups/browser/

next: Phone
nextLink: mockups/phone/
---

<!-- Class table -->

{{< class-table >}}
mockup-code | component | Container element.
{{< /class-table >}}

<!-------------------- Basic examples -------------------->

{{< headname level="2" >}} Basic examples {{< /headname >}}

<!-- Mockup code with line prefix -->

{{< headname level="3" >}} Mockup code with line prefix {{< /headname >}}

The `mockup-code` class is tailored to enhance the presentation of your code with a stylish layout. Use `data-prefix` to incorporate additional prefixes before text, such as `$`, `>`, or numeric indicators.

{{< code >}}

<div class="mockup-code">
  <pre data-prefix="$"><code>npm i -D flyonui@latest</code></pre>
</div>
{{< /code >}}

<!-- Multi line -->

{{< headname level="3" >}} Multi line {{< /headname >}}

Code spanning multiple lines.

{{< code >}}

<div class="mockup-code">
  <pre data-prefix="$"><code>npm i -D flyonui@latest</code></pre>
  <pre data-prefix=">" class="text-warning"><code>installing...</code></pre>
  <pre data-prefix=">" class="text-success"><code>Done!</code></pre>
</div>
{{< /code >}}

<!-- Highlighted line -->

{{< headname level="3" >}} Highlighted line {{< /headname >}}

Code example that highlights syntax.

{{< code >}}

<div class="mockup-code">
  <pre data-prefix="1"><code>npm i -D flyonui@latest</code></pre>
  <pre data-prefix="2"><code>installing...</code></pre>
  <pre data-prefix="3" class="bg-warning text-warning-content"><code>Warning!</code></pre>
</div>

{{< /code >}}

<!-- Scrollable body -->

{{< headname level="3" >}} Scrollable body {{< /headname >}}

Example of a scrollable code container.

{{< code >}}

<div class="mockup-code">
  <pre data-prefix="~"><code>Magnam dolore beatae necessitatibus nemopsum itaque sit. Et porro quae qui et et dolore ratione.</code></pre>
</div>
{{< /code >}}

<!-- Without prefix -->

{{< headname level="3" >}} Without prefix {{< /headname >}}

Example of code without a prefix.

{{< code >}}

<div class="mockup-code">
  <pre><code>without prefix</code></pre>
</div>
{{< /code >}}

<!-- Semantic color -->

{{< headname level="3" >}} Semantic color {{< /headname >}}

You can modify both the background and text colors.

{{< code >}}

<div class="mockup-code bg-primary/20 text-primary rounded-xl">
  <pre><code>can be any color!</code></pre>
</div>
{{< /code >}}
