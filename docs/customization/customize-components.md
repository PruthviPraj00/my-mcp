---
title: "Customize components"
description: "Quickly personalize and easily modify components within just a few minutes."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "customization"
    weight: 1

previous: License
previousLink: getting-started/license/

next: Config
nextLink: customization/config/
---

<!-------------------- How to customize FlyonUI? -------------------->

{{< headsingle addClass="!mt-px" level="2" >}} How to customize FlyonUI? {{< /headsingle >}}

FlyonUI components come with many built-in variants, making it unlikely that you'll need to customize anything. However, if needed, you can still modify components in various ways:

- For example, to customize this button:

```html
<button class="btn">Button</button>
```

<button class="btn mt-4">Button</button>

<!-- Use FlyonUI utility classes: -->

{{< headsingle level="4" >}}1. Use FlyonUI utility classes: {{< /headsingle >}}

```html
<button class="btn btn-primary">One</button>
<button class="btn btn-accent btn-gradient">Two</button>
<button class="btn btn-accent btn-outline">Three</button>
```

<div class="flex items-center gap-4 my-4">
  <button class="btn btn-primary">One</button>
  <button class="btn btn-accent btn-gradient">Two</button>
  <button class="btn btn-error btn-outline">Three</button>
</div>

<!-- Use Tailwind's utility classes: -->

{{< headsingle level="4" >}}2. Use Tailwind's utility classes: {{< /headsingle >}}

```html
<button class="btn rounded-full">One</button>
<button class="btn rounded-none px-16">Two</button>
```

<div class="flex items-center gap-4 my-4">
  <button class="btn rounded-full">One</button>
  <button class="btn rounded-none px-16">Two</button>
</div>

<!-- Customize via CSS using Tailwind's `@apply` directive: -->

{{< headsingle level="4" >}}3. Customize via `@apply` directive: {{< /headsingle >}}

```php
.btn {
  @apply rounded-full;
}
```

<br/>

<!-- Other options: -->

{{< headname level="4" >}}4. Other options: {{< /headname >}}

- {{< link link="customization/themes/" addClass="link link-primary" >}}Create your own theme{{< /link >}}.
- Disable FlyonUI's design decisions and use the {{< link link="customization/config/#styled" addClass="link link-primary" >}}unstyled (skeleton){{< /link >}} version of FlyonUI.
