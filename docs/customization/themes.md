---
title: "Themes"
description: "Discover how to customize the default theme and understand the fundamentals of theming in FlyonUI."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "customization"
    weight: 5

previous: Icons
previousLink: customization/icons/

next: Utilities and Variables
nextLink: customization/utilities/
---


> In FlyonUI v1.x, all themes are enabled by default. However, in v2.0.0, only the light and dark themes are enabled by default. Other themes must be enabled manually.

<!-------------------- FlyonUI themes -------------------->

{{< headsingle addClass="!mt-px" level="2" >}} FlyonUI themes {{< /headsingle >}}

**How to use FlyonUI themes?**

FlyonUI comes with 12 built-in themes that can instantly change the look and feel of your website, saving you time by eliminating the need to manually choose color schemes. Focus on the structure and content of your site while FlyonUI handles the design.

You can either use the pre-built themes, create your own custom themes, or further customize the existing ones.

To manage your themes, include brackets around `@plugin "flyonui"` in your CSS file.

<!-- Keep the space in 3rd pre  -->
<div class="mockup-code not-prose mb-4 before:content-none bg-[#272822]">
  <pre data-prefix=" " class="text-sm text-white"><code>@import "tailwindcss";</code></pre>
  <pre data-prefix="-" class="text-sm text-error"><code>@plugin "flyonui";</code></pre>
  <pre data-prefix="+" class="text-sm text-success"><code>@plugin "flyonui" {</code></pre>
  <pre data-prefix="+" class="text-sm text-success"><code>   themes: light --default, dark --prefersdark;</code></pre>
  <pre data-prefix="+" class="text-sm text-success"><code>}</code></pre>
</div>

The `themes` configuration allows you to specify a comma-separated list of theme names you wish to enable. You can assign the `--default` flag to set a theme as the default and the `--prefersdark` flag for dark mode (matching the `prefers-color-scheme: dark` CSS feature).

**How to Enable a Built-in Theme?**

By default, `light` and `dark` themes are enabled. To enable the `gourmet` theme, you can follow this example:

```php
@import "tailwindcss";
@plugin "flyonui" {
  themes: light --default, dark --prefersdark, gourmet;
}
```
<br/>

Then, to apply the `gourmet` theme to the page, use the following HTML:

> If no `data-theme` is applied, the theming will default to the user's system preference. The `--default` theme will be used for light mode, and the `--prefersdark` theme will be applied for dark mode.

```html
<html data-theme="gourmet"></html>
```

<!-------------------- List of themes -------------------->

{{< headsingle level="2" >}} List of themes {{< /headsingle >}}

{{< themes >}}

<br/>

<!-- Font family -->

{{< headname level="3" >}} Font family {{< /headname >}}

<br />

Both `light` and `dark` themes use the default `font-sans` font family, as specified in the <a href="https://tailwindcss.com/docs/font-family" target="_blank">official Tailwind documentation</a>. For further customizations of the font family, refer to the <a href="https://tailwindcss.com/docs/font-family#customizing-the-default-font" target="_blank">Tailwind font family guide</a>.

When using themes like  `corporate`, `ghibli`, `gourmet`, `luxury`, `slack`, `soft` or `valorant` the following font families are required:

```html
<head>
  <!-- Corporate : 'Public Sans' -->
  <link
    href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap"
    rel="stylesheet"
  />
  <!-- Ghibli : 'Amaranth' -->
  <link 
    href="https://fonts.googleapis.com/css2?family=Amaranth:ital,wght@0,400;0,700;1,400;1,700&display=swap"
    rel="stylesheet"
  />
  <!-- Gourmet : 'Rubik' -->
  <link
    href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap"
    rel="stylesheet"
  />
  <!-- Luxury : 'Archivo' -->
  <link
    href="https://fonts.googleapis.com/css?family=Archivo:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap"
    rel="stylesheet"
  />
  <!-- Slack : 'Lato' -->
  <link 
    href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap" 
    rel="stylesheet"
  />
  <!-- Soft : 'Montserrat' -->
  <link
    href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap"
    rel="stylesheet"
  />
  <!-- Valorant : 'Work Sans' -->
  <link 
    href="https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" 
    rel="stylesheet"
  />
</head>
```

<!-------------------- Activate all themes. -------------------->

{{< headsingle level="2" >}} Activate all themes. {{< /headsingle >}}

To enable all 12 built-in themes, set the `themes` option to `all`:

```php
@import "tailwindcss";
@plugin "flyonui" {
  themes: all;
}
```

<!-------------------- How to remove unused themes? -------------------->

{{< headsingle level="2" >}} How to remove unused themes? {{< /headsingle >}}

To optimize your project and reduce CSS file size, you can include only the themes you need. For example:

- `soft` will be the default theme for light mode.
- `dark` will be the default theme for dark mode.
- `gourmet` can be applied to any HTML element using `data-theme='gourmet'`.

```php
@import "tailwindcss";
@plugin "flyonui" {
  themes: soft --default, dark --prefersdark, gourmet ;
}
```

<!-------------------- How to disable themes? -------------------->

{{< headsingle level="2" >}} How to disable themes? {{< /headsingle >}}

If you only need the default light and dark themes, you can disable all others by setting the `themes` option to `false`:

```php
@import "tailwindcss";
@plugin "flyonui" {
  themes: false;
}
```

<br/>

If you wish to disable just the `dark` theme, simply remove it from the list. This way, only the light theme will be active:

```php
 @import "tailwindcss";
 @plugin "flyonui" {
  themes: light --default;
 }
```

<!-------------------- How to use a theme only for a section of a page? -------------------->

{{< headsingle level="2" >}} How to use a theme only for a section of a page? {{< /headsingle >}}

You can apply a theme to a specific section of your page by adding the `data-theme='THEME_NAME'` attribute to any element. All child elements will inherit that theme. You can nest themes within each other without restrictions.

```html
<html data-theme="dark">
  <div data-theme="light">
    This div will always use the light theme.
    <span data-theme="corporate">This span will always use the corporate theme!</span>
  </div>
</html>
```

<!-------------------- How to add a new custom theme? -------------------->

{{< headsingle level="2" >}} How to add a new custom theme? {{< /headsingle >}}

To create a new custom theme, use `@plugin "flyonui/theme" {}` in your CSS file. The structure is as follows:

```php
@import "tailwindcss";
@plugin "flyonui";
@plugin "flyonui/theme" {
  name: "maintheme";
  default: true; /* Set as default theme */
  prefersdark: false; /* Set dark mode for prefers-color-scheme: dark */
  color-scheme: light; /* Defines the color of browser UI */

  --color-base-100: oklch(98.8% 0.0069 304.24);
  --color-base-200: oklch(90.02% 0.0364 308.84);
  --color-base-300: oklch(88.09% 0.0421 307.21);
  --color-base-content: oklch(32.61% 0.0705 305.29);
  --color-primary: oklch(72.17% 0.1767 305.5);
  --color-primary-content: oklch(94.64% 0.0327 307.17);
  --color-secondary: oklch(66.8% 0.0184 304.67);
  --color-accent: oklch(71.37% 0.1434 254.62);
  --color-accent-content: oklch(89.94% 0.0589 343.23);
  --color-neutral: oklch(32.61% 0.0705 305.29);
  --color-neutral-content: oklch(99.54% 0.0028 308.43);
  --color-info: oklch(79.71% 0.1339 211.53);
  --color-info-content: oklch(95.63% 0.0443 203.39);
  --color-success: oklch(77.29% 0.1535 163.22);
  --color-success-content: oklch(95.05% 0.0507 163.05);
  --color-warning: oklch(75.76% 0.159 55.93);
  --color-warning-content: oklch(95.42% 0.03715446392304164 75.16435946755645);
  --color-error: oklch(75.88% 0.1385 31.29);
  --color-error-content: oklch(97.58% 0.0151 61.35);

  /* Border Radius */
  --radius-selector: 1rem;
  --radius-field: 0.25rem;
  --radius-box: 0.5rem;

  /* Base Sizes */
  --size-selector: 0.25rem;
  --size-field: 0.25rem;

  /* Border Size */
  --border: 1px;

  /* Effects */
  --depth: 1;
  --noise: 0;
}
```
<!-------------------- Custom CSS for a FlyonUI theme -------------------->

{{< headsingle level="2" >}} Custom CSS for a FlyonUI theme {{< /headsingle >}}

You can write custom CSS styles specifically for a theme. For instance, this style applies only to the `light` theme:

```php
[data-theme="light"] {
  .my-btn {
    background-color: #1EA1F1;
    border-color: #1EA1F1;
  }
  .my-btn:hover {
    background-color: #1C96E1;
    border-color: #1C96E1;
  }
}
```

<!-------------------- How to customize an existing theme? -------------------->

{{< headsingle level="2" >}} How to customize an existing theme? {{< /headsingle >}}

To modify an existing theme, use the same structure as adding a new theme but specify the built-in theme's name. For example, to customize the `light` theme:

```php
@import "tailwindcss";
@plugin "flyonui";
@plugin "flyonui/theme" {
  name: "light";
  default: true;
  --color-primary: blue;
  --color-secondary: teal;
}
```

<br/>

All other values will inherit from the original theme.

<!-------------------- How to apply Tailwind's 'dark:' selector for specific themes? -------------------->

{{< headsingle level="2" >}} How to apply Tailwind's 'dark:' selector for specific themes? {{< /headsingle >}}

To use Tailwind's `dark:` selector with a specific theme, such as applying padding for a `luxury` theme in dark mode, use the following syntax:

```php
@import "tailwindcss";
@plugin "flyonui" {
  themes: soft --default, luxury --prefersdark;
}

@custom-variant dark (&:where([data-theme=luxury], [data-theme=luxury] *));
```
<br/>

```html
<div class="p-10 dark:p-20">
  I will have 10 padding on the soft theme and 20 padding on the luxury theme or when dark
</div>
```
