---
title: "Config"
description: "A guide to configuring and customizing the default FlyonUI and Tailwind CSS options and styles."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "customization"
    weight: 2

previous: Customize components
previousLink: customization/customize-components/

next: Base style
nextLink: customization/base/
---

<!-------------------- Config -------------------->

{{< headsingle addClass="!mt-px" level="2" >}} Config {{< /headsingle >}}

How can you adjust the default configuration of FlyonUI?

FlyonUI is highly configurable via your CSS file. To customize it, replace the semicolon `;` after `@plugin "flyonui"` with curly braces `{}` and insert your desired configuration settings inside these braces.

> **Note**: Due to integration with Preline JS, FlyonUI does not support the prefix option like DaisyUI.


<div class="mockup-code not-prose mb-4 before:content-none bg-[#272822]">
  <pre data-prefix="-" class="text-sm text-error"><code>@plugin "flyonui";</code></pre>
  <pre data-prefix="+" class="text-sm text-success"><code>@plugin "flyonui" {</code></pre>
  <pre data-prefix="+" class="text-sm text-success"><code>}</code></pre>
</div>

Default config:


```php
@plugin "flyonui" {
  themes: light --default, dark --prefersdark;
  root: ":root";
  include: ;
  exclude: ;
  logs: true;
}
```

{{< headsingle addClass="!mb-0" level="2" >}} Configuration options explained: {{< /headsingle >}}

<!-- themes -->

{{< headsingle level="3" >}} themes {{< /headsingle >}}

{{< table >}}
Default Value|Type|Description
`light --default, dark --prefersdark`|string or comma-separated list, or `false` or `all`|A list of themes to enable. Use `false` to disable all themes, or `all` to enable every theme. The `--default` flag marks a theme as the default, while `--prefersdark` sets a theme as the default for dark mode.
{{< /table >}}

Here, we define four themes: `soft` as the default theme, `luxury` for dark mode, and `gourmet` and `corporate` as additional themes that can be used.

```php
@plugin "flyonui" {
  themes: soft --default, luxury --prefersdark, gourmet, corporate;
}
```
<br/>

Enabling all themes:

```php
@plugin "flyonui" {
  themes: all;
}
```

<br/>

Disabling all themes to add your own custom themes via {{< link link="customization/themes/" addClass="link link-primary" >}}@plugin "flyonui/theme"{{< /link >}}

```php
@plugin "flyonui" {
  themes: false;
}
```
<br/>

Setting only `soft` as the available theme. This restricts the theme to a single choice unless additional custom themes are added {{< link link="customization/themes/" addClass="link link-primary" >}}@plugin "flyonui/theme"{{< /link >}}

```php
@plugin "flyonui" {
  themes: soft --default;
}
```

<!-- :root -->

{{< headsingle level="3" >}} :root {{< /headsingle >}}

{{< table >}}
Default Value|Type|Description
`:root`|string|The CSS selector where FlyonUI's CSS variables will be applied.
{{< /table >}}

Changing the root to `#app` instead of `:root`. This ensures that all FlyonUI variables are scoped to `#app`. This is useful in environments like web components, shadow DOMs, or a specific section of a page.

```php
@plugin "flyonui" {
  root: "#app";
}
```

<!-- include -->

{{< headsingle level="3" >}} include {{< /headsingle >}}

{{< table >}}
Default Value|Type|Description
|comma-separated list|List of components to include.
{{< /table >}}

In the example below, only the `button`, `input`, and `select` components are included. All other components from FlyonUI will be excluded.

```php
@plugin "flyonui" {
  include: badge, dropdow, timeline;
}
```
<!-- exclude -->

{{< headsingle level="3" >}} exclude {{< /headsingle >}}

{{< table >}}
Default Value|Type|Description
|comma-separated list|List of components to exclude.
{{< /table >}}

In below example, we excluded the radio, chat, and timeline components. All other styles of FlyonUi library will be excluded.
Here are the file names you can exclude.

```php
@plugin "flyonui" {
  exclude: radio, chat , timeline;
}
```
<!-- logs -->

{{< headsingle level="3" >}} logs {{< /headsingle >}}

{{< table >}}
Default value|Type|Description
`true`|boolean|Enable or disable logs.
{{< /table >}}

In this case, we disable logging to clean up the console output.

```php
@plugin "flyonui" {
  logs: false;
}
```
---

### Additional Notes:

- **Customization**: FlyonUI offers flexible configurations, allowing you to tailor your UI to specific requirements.
- **Component Control**: Use the `include` and `exclude` options to fine-tune the set of components you want to use, optimizing your build size.
- **Logs**: Disabling logs in production environments helps reduce unnecessary console clutter.
