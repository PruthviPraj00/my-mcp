---
title: "Base style"
description: "These are the default styles implemented by FlyonUI."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "customization"
    weight: 3

previous: Config
previousLink: customization/config/

next: Colors
nextLink: customization/colors/
---

<!-------------------- FlyonUI base style -------------------->

{{< headsingle level="2" >}} FlyonUI base style {{< /headsingle >}}

FlyonUI applies a few essential base styles to your page to ensure consistency and a better user experience.

These base styles are lightweight—less than a kilobyte in total—so they won’t affect your page's performance.

Below is a breakdown of the styles FlyonUI adds:

{{< table >}}
Name | Description  
**properties** | Includes necessary `@rules`, such as defining variable types (e.g., `--radialprogress`).  
**rootcolor** | Defines the `background-color` and `text color` for `:root` and `[data-theme]`, setting them to `base-100` and `base-content` respectively.  
**scrollbar** | Customizes scrollbar appearance using `scrollbar-color` on `:root`.  
**svg** | Provides small inline SVG assets, including noise filters, chat bubble tails, and tooltip tails. This can be disabled if you prefer using custom images.  
{{< /table >}}

### Opting Out of Specific Base Styles  

If you wish to exclude any of these base styles, you can do so by modifying the FlyonUI configuration using the `exclude` option.  

For example, to opt out of both the scrollbar styles (`scrollbar`, `scrollbar-color`) and the root color styles, add the following to your FlyonUI plugin settings:

```php
@plugin "flyonui" {
  exclude: scrollbar, rootcolor;
}
```

<!-------------------- Source Code -------------------->

{{< headsingle level="2" >}} Source Code {{< /headsingle >}}

You can explore the source code for each base style on GitHub:

- <a href="https://github.com/themeselection/flyonui/blob/main/src/base/properties.css" class="link link-animated link-primary font-semibold not-prose" target="_blank">properties.css</a> – Handles key `@rules` such as variable definitions.
- <a href="https://github.com/themeselection/flyonui/blob/main/src/base/rootcolor.css" class="link link-animated link-primary font-semibold not-prose" target="_blank">rootcolor.css</a> – Manages theme colors for the root element.
- <a href="https://github.com/themeselection/flyonui/blob/main/src/base/scrollbar.css" class="link link-animated link-primary font-semibold not-prose" target="_blank">scrollbar.css</a> – Customizes scrollbar styles.
- <a href="https://github.com/themeselection/flyonui/blob/main/src/base/svg.css" class="link link-animated link-primary font-semibold not-prose" target="_blank">svg.css</a> – Includes small SVG assets used for styling.
