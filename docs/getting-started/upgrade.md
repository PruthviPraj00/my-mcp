---
title: "Upgrade Guide"
description: "This comprehensive guide walks you through updating your project setup and components to Tailwind CSS 4 and FlyonUI 2."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
tag: New
menu:
  main:
    parent: "getting-started"
    weight: 3

previous: Quick start
previousLink: getting-started/quick-start/

next: Usage
nextLink: getting-started/usage/
---

{{< callout "info" >}}
This guide is applicable only for users upgrading from FlyonUI 1.x to 2.0.0
{{< /callout >}}

<!-------------------- FlyonUI upgrade guide -------------------->

{{< headsingle level="2" >}} FlyonUI upgrade guide {{< /headsingle >}} 

<!-- Update Tailwind CSS -->
{{< headsingle level="3" >}} Update Tailwind CSS {{< /headsingle >}}  

Tailwind CSS provides a CLI tool to streamline the upgrade process. This tool automatically applies necessary changes to your project, ensuring compatibility with the latest version.  

**Steps to Upgrade:**

1. **Remove FlyonUI and plugins** from your `tailwind.config.js` file. This allows Tailwind CSS’s upgrade tool to modify configurations safely.  

<!-- Keep the space   -->
<div class="mockup-code not-prose mb-4 before:content-none bg-[#272822]">
  <pre data-prefix=" " class="text-sm text-white"><code>module.exports = {</code></pre>
  <pre data-prefix=" " class="text-sm text-white"><code>  content: ['./your-files/**/*.{html,js,ts}'],</code></pre>
  <pre data-prefix="-" class="text-sm text-error"><code>  flyonui: {</code></pre>
  <pre data-prefix="-" class="text-sm text-error"><code>    themes: ['light', 'dark', 'soft'], </code></pre>
  <pre data-prefix="-" class="text-sm text-error"><code>   },</code></pre>
  <pre data-prefix="-" class="text-sm text-error"><code>   plugins: [require("flyonui"), require(flyonui/plugin)],</code></pre>
  <pre data-prefix=" " class="text-sm text-white"><code>}</code></pre>
</div>  

2. **Run the official Tailwind CSS upgrade tool** to update your setup automatically:  

```bash
npx @tailwindcss/upgrade
```  

<br/>

<!-- Update FlyonUI -->
{{< headsingle level="3" >}} Update FlyonUI {{< /headsingle >}}  

**Steps to Upgrade:**  

1. **Install FlyonUI 2 using npm**:  

```bash
npm i -D flyonui@latest
```  

2. **Import FlyonUI into your CSS file:**  

The `plugin.js` file has been removed, and `variants.css` now contains custom variants, similar to the previous functionality of `plugin.js`, but with the updated method introduced in TailwindCSS v4.

```php
@import "tailwindcss";
@plugin "flyonui";
@import "./node_modules/flyonui/variants.css";  // Extended variants for JS components
```  

3. **Define the built-in theme in the configuration:**  

```php
  @import "tailwindcss";
  @plugin "flyonui" {
    themes: light --default, dark --prefersdark, soft;
  }
```  

4. **Include FlyonUI’s JavaScript file in your HTML:**  

```html
<script src="../node_modules/flyonui/flyonui.js"></script>
```  

<!-------------------- 🚀  FlyonUI 2 Updated & Changes -------------------->

{{< headsingle level="2" >}} 🚀 FlyonUI 2 Updated & Changes {{< /headsingle >}}

This section highlights all the exciting updates and changes made to FlyonUI components (HTML/CSS). Get ready to enhance your user experience with these improvements!

<!-- Content block -->

{{< headsingle level="3" >}} Content block {{< /headsingle >}}
<div class="divider"></div>

<!-- Custom Scrollbar -->

{{< headsingle level="4" >}} Custom Scrollbar {{< /headsingle >}}
<br/>
❎ **Removed:**

- The classes `vertical-scrollbar`, `horizontal-scrollbar`, and `rounded-scrollbar` have been removed. Scrollbar styles are now globally applied via `scrollbar.css`. For more details, check out the {{< link link="customization/base/" addClass="link link-primary" >}}Base Style{{< /link >}} documentation. Bye-bye cluttered scrollbar classes! 👋

<!-- KBD(keyboard) -->

{{< headsingle level="4" >}} KBD (keyboard) {{< /headsingle >}}
<br/>
🆕 **Added**
- `kbd-md` (default size)
- `kbd-xl` for extra-large keyboard touches!

📝 **Updated**
- Adjusted `kbd` height for all sizes to make typing smoother.

<!-- Typography -->

{{< headsingle level="4" >}} Typography {{< /headsingle >}}
<br/>
🆕 **Added**
- New text background color options! Choose from text with background, soft background, or text with a border. For the full scoop, visit the {{< link link="content/typography/#text-color" addClass="link link-primary" >}}Text Color{{< /link >}} section.
- Support for semantic gradient backgrounds. Learn more in the {{< link link="content/typography/#semantic-gradient-background" addClass="link link-primary" >}}Semantic Gradient Background{{< /link >}} section.

<!-- Components  -->

{{< headsingle level="3" >}} Components {{< /headsingle >}}
<div class="divider"></div>

<!-- Accordion -->

{{< headsingle level="4" >}} Accordion {{< /headsingle >}}
<br/>
🆕 **Added**
- **New option**: `--keep-one-open` to keep at least one accordion always open. (Preline)
- Added events: `beforeOpen` and `beforeClose` that fire before the accordion opens and closes. (Preline)

<!-- Alert -->

{{< headsingle level="4" >}} Alert {{< /headsingle >}}
<br/>
🆕 **Added**
- Added a **dash example** for better design flexibility. 

📝 **Updated**
- The neutral alert is now the default. 🎉

❎ **Removed** 
- `alert-neutral` style is gone. But don’t worry, we’ve made the neutral alert the standard! 😎

<!-- Avatar -->

{{< headsingle level="4" >}} Avatar {{< /headsingle >}}
<br/>
📝 **Updated**
**Breaking Changes: Class Name Renaming**

To improve clarity and consistency, the following class names have been **renamed**:

- `placeholder` → `avatar-placeholder`
- `online-top` → `avatar-online-top`
- `online-bottom` → `avatar-online-bottom`
- `away-top` → `avatar-away-top`
- `away-bottom` → `avatar-away-bottom`
- `busy-top` → `avatar-busy-top`
- `busy-bottom` → `avatar-busy-bottom`
- `offline-top` → `avatar-offline-top`
- `offline-bottom` → `avatar-offline-bottom`


**Placeholder Example:**

```html
<!-- Before -->
<div class="avatar placeholder">
  <div class="bg-neutral text-neutral-content w-10 rounded-full">
    <span class="icon-[tabler--user] size-6"></span>
  </div>
</div>
```
<br/>

```html
<!-- After -->
<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-10 rounded-full">
    <span class="icon-[tabler--user] size-6"></span>
  </div>
</div>
```
<br/>

**Status Example:**

```html
<!-- Before -->
<div class="avatar online-top">
  <div class="w-6 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>
```
<br/>

```html
<!-- After -->
<div class="avatar avatar-online-top">
  <div class="w-6 rounded-full">
    <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
  </div>
</div>
```

<!-- Badge -->

{{< headsingle level="4" >}} Badge {{< /headsingle >}}
<br/>
🆕 **Added**
- New badge sizes: `badge-md` (default) and `badge-xl` for more badge variety.
- **Dash example** added for design flexibility.

📝 **Updated**
- Neutral badge is now the default! 
- Adjusted the badge sizes based on a new scale for better visual consistency.

❎ **Removed:** 
- Removed the `badge-neutral` style. Neutral is the new default! ✨

<!-- Button -->

{{< headsingle level="4" >}} Button {{< /headsingle >}}
<br/>
🆕 **Added**
- New button sizes: `btn-md` (default) and `btn-xl` for larger buttons.
- Added a **box-shadow** effect if `--depth` is enabled for more dynamic buttons!

📝 **Updated**
- The neutral button is now the default.
- Button sizes have been adjusted to fit the new design scale.

❎ **Removed:** 
- Removed `btn-neutral` style. Neutral is now part of the default button setup! 🎨

<!-- Card -->

{{< headsingle level="4" >}} Card {{< /headsingle >}}
<br/>
🆕 **Added**
- New `card-border` style that adapts the border width from the theme. 
- Support for different card sizes: `card-xs`, `card-sm`, `card-md`, `card-lg`, `card-xl`.

❎ **Removed:** 
- Removed `card-compact` style. Just use `card-sm` instead. Simpler and cleaner! 😉

<!-- Chat -->

{{< headsingle level="4" >}} Chat {{< /headsingle >}}
<br/>
📝 **Updated**
- The chat bubble tail shape has been improved for a prettier, more polished design. 💬

<!-- Diff -->

{{< headsingle level="4" >}} Diff {{< /headsingle >}}
<br/>
📝 **Updated**
- Fixed Firefox lag issue. More smoothness for your browser. ⚡

<!-- Loading -->

{{< headsingle level="4" >}} Loading {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes: `loading-md` (default) and `loading-xl`.

📝 **Updated**
- **SVG animations** have replaced CSS animations for better performance. No more sluggish loading! 🌀
- Fixed a bug where Safari sometimes froze the animation. 🚀

<!-- Progress -->

{{< headsingle level="4" >}} Progress {{< /headsingle >}}
<br/>
🆕 **Added**
- A new `progress-horizonatal` class. 

<!-- Radial Progress -->

{{< headsingle level="4" >}} Radial Progress {{< /headsingle >}}
<br/>
🆕 **Added**
- Added an animation effect to the `--value` when it changes. ✨
- Improved accessibility for screen readers. Now, it's more inclusive!

<!-- Stack -->

{{< headsingle level="4" >}} Stack {{< /headsingle >}}
<br/>
🆕 **Added**
- `stack-start` and `stack-end` for controlling the stack direction.

📝 **Updated**
- Removed `h-*` and `w-*` from each stack child and applied them to the stack component itself.

```html
<div class="stack">
  <div class="bg-primary text-primary-content grid h-20 w-32 place-content-center rounded">1</div>
  <div class="bg-success text-success-content grid h-20 w-32 place-content-center rounded">2</div>
  <div class="bg-warning text-warning-content grid h-20 w-32 place-content-center rounded">3</div>  
</div>
```
<br/>

```html
<div class="stack h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-sm">1</div>
  <div class="bg-success text-success-content grid place-content-center rounded-sm">2</div>
  <div class="bg-warning text-warning-content grid place-content-center rounded-sm">3</div>  
</div>
```

<!-- Stat -->

{{< headsingle level="4" >}} Stat {{< /headsingle >}}
<br/>
🆕 **Added**
- New `card-border` style that adapts to the border width from the theme.
- Added `stats-horizontal` class for horizontal stat layout. Perfect for dashboards! 📊

<!-- Navigations  -->

{{< headsingle level="3" >}} Navigations {{< /headsingle >}}
<div class="divider"></div>

<!-- Menu -->

{{< headsingle level="4" >}} Menu {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes for the menu: `menu-md` (default) and `menu-xl`.

📝 **Updated**
- **Breaking Change:** Renamed `disabled` to `menu-disabled`.
- **Breaking Change:** Renamed `focus` to `menu-focus`.
- **Breaking Change:** Renamed `active` to `menu-active`. Now it's clearer! ✅

<!-- Sidebar -->
{{< headsingle level="4" >}} Sidebar {{< /headsingle >}}
<br/>
📝 **Updated**
- The structure for collapsibles menu/sidebar has been updated. For more details, refer to the [menu collapse documentation](https://flyonui.com/docs/navigations/sidebar/#multiple-level-with-separator).


<!-- Tabs -->

{{< headsingle level="4" >}} Tabs {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes for tabs: `tab-md` (default) and `tab-xl`. 🏷️

<!-- Overlays  -->

{{< headsingle level="3" >}} Overlays {{< /headsingle >}}
<div class="divider"></div>

<!-- Dropdown  -->
{{< headsingle level="4" >}} Dropdown  {{< /headsingle >}}
<br/>
🆕 **Added**
- Added `[--scope:*]` option for determines whether the dropdown will be moved outside the parent for correct display.**(Preline)**
- Added `[--has-autofocus:*]` option for disable autofocus on the first focusable element **(Preline)**
- Added `[--gpu-acceleration:*]` option for disable/enable position calculation using the transform property. **(Preline)**

📝 **Updated**
- Breaking Changes: Rename `active` class of dropdown items to `dropdown-active`
- Breaking Changes: Rename `disabled` class of dropdown items to `dropdown-disabled`
- **Migrate** : [Floating UI](https://floating-ui.com/) has now completely replaced Popper.js across all plugins.

❎ **Removed:** 
  - Removed `[--skidding:*] option from dropdown.

<!-- Modal  -->
{{< headsingle level="4" >}} Modal  {{< /headsingle >}}
<br/>
🆕 **Added**
- Add `modal-dialog-md` default for the modal width.
- Added [--auto-close-equality-type:*] option for auto close **(Preline)**
- Added [--has-dynamic-z-index:*] option for handling the dynamic z-index **(Preline)**

📝 **Updated**
- Updated backdrop color to `bg-base-300/60`.
- Now use `overlay-open:duration-500` with modal and modal-dialog


<!-- Popover/Tooltip  -->
{{< headsingle level="4" >}} Popover/Tooltip  {{< /headsingle >}}
<br/>
📝 **Updated**
- **Migrate** : [Floating UI](https://floating-ui.com/) has now completely replaced Popper.js across all plugins.

<!-- Forms elements  -->

{{< headsingle level="3" >}} Forms elements {{< /headsingle >}}
<div class="divider"></div>

<!-- Checkbox -->

{{< headsingle level="4" >}} Checkbox {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes: `checkbox-md` (default) and `checkbox-xl`.
- Now print-friendly. No more issues when printing your forms! 🖨️

📝 **Updated**
- Improved the checkmark icon and its animation.
- Enhanced accessibility features with improved focus styling.
- Adjusted the size scale to better align with other components.

<!-- File input -->

{{< headsingle level="4" >}} File input {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes: `file-input-md` (default) and `file-input-xl`.

📝 **Updated**
- Adjusted padding and font size for a more polished look.

<!-- Input -->

{{< headsingle level="4" >}} Input {{< /headsingle >}}
<br/>
🆕 **Added**
- Added `helper-text` for additional guidance on inputs.
- New sizes: `input-md` (default) and `input-xl`.

📝 **Updated**
- **Breaking Change**: Removed `input-group`. Grouping can now be achieved by wrapping inputs with the `.input` class.
- Adjusted size scale for better uniformity across components.

❎ **Removed:**  
- Removed the `input-filled` variant.

**Input label and helper text**

```html
<!-- Before -->
<div class="w-96">
  <label class="label label-text" for="labelAndHelperText"> Full Name </label>
  <input type="text" placeholder="John Doe" class="input" id="labelAndHelperText" />
  <span class="label">
    <span class="label-text-alt">Please write your full name</span>
  </span>
</div>
```
<br/>

```html
<!-- After -->
<div class="w-96">
  <label class="label-text" for="labelAndHelperText">Full Name</label>
  <input type="text" placeholder="John Doe" class="input" id="labelAndHelperText" />
  <span class="helper-text">Please write your full name</span>
</div>
```
<br/>

**Input floating**

```html
<!-- Before -->
<div class="relative max-w-sm">
  <input type="text" placeholder="John Doe" class="input input-floating peer" id="floatingLabelDefault" />
  <label class="input-floating-label" for="floatingLabelDefault">Full Name</label>
</div>
```
<br/>

```html
<!-- After -->
<div class="input-floating w-96">
  <input type="text" placeholder="John Doe" class="input" id="floatingInput" />
  <label class="input-floating-label" for="floatingInput">Full Name</label>
</div>
```
<br/>

**Input Group changes**

```html
<!-- Before -->
<div class="input-group max-w-sm">
  <label class="input-group-text" for="inlineLabelName">Name</label>
  <input type="text" class="input grow" placeholder="FlyonUI" id="inlineLabelName" />
</div>
```
<br/>

```html
<!-- After -->
<div class="input max-w-sm">
  <label class="label-text my-auto me-3" for="inlineLabelName">Name</label>
  <input type="text" class="grow" placeholder="FlyonUI" id="inlineLabelName" />
</div>
```


<!-- Radio -->

{{< headsingle level="4" >}} Radio {{< /headsingle >}}
<br/>
🆕 **Added**
- New radio sizes: `radio-md` (default) and `radio-xl`.
- Radios are now print-friendly! 📄

📝 **Updated**
- Change `radio-inset` to `style` instead of using it as a component.
- Enhanced accessibility with improved forced color mode.
- Adjusted the size scale to better align with other components.

❎ **Removed:**  
 - The `radio-inset-{sizes}` and `radio-inset-{semantic-color}` classes associated with `radio-inset` have been removed.

**Radio Inset**

```html
<!-- Before -->
<div class="flex items-center gap-1">
  <input type="radio" name="radio-3" class="radio-inset radio-inset-primary" id="radioType3"  />
  <label class="label label-text text-base" for="radioType3"> Default </label>
</div>
```
<br/>

```html
<!-- After -->
<div class="flex items-center gap-1">
  <input type="radio" name="radio-3" class="radio radio-inset radio-primary" id="radioType3"  />
  <label class="label-text text-base" for="radioType3"> Default </label>
</div>
```


<!-- Range -->

{{< headsingle level="4" >}} Range {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes: `range-md` (default) and `range-xl`. 
- Range sliders are now print-friendly. 🖨️

📝 **Updated**
- Updated variable name from `--range-shdw` to `--range-color` for better clarity and consistency.
- Adjusted the size scale to better align with other components.

<!-- Select -->

{{< headsingle level="4" >}} Select {{< /headsingle >}}
<br/>
🆕 **Added**
- New select sizes: `select-md` (default) and `select-xl`. 
- Added examples for select groups. Perfect for dynamic forms. 🎯

📝 **Updated**
- Updated select-floating structure for a cleaner design.
- Adjusted the size scale to better align with other components.
  
❎ **Removed:**  
- Removed `select-filled` variant. 

**Select floating**

```html
<!-- Before -->
<div class="relative w-full">
  <select class="select select-floating max-w-sm" aria-label="Select floating label" id="selectFloating">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectFloating">Pick your favorite Movie</label>
</div>
```
<br/>

```html
<!-- After -->
<div class="select-floating w-96">
  <select class="select" aria-label="Select floating label" id="selectFloating">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectFloating">Pick your favorite Movie</label>
</div>
```

<!-- Switch -->

{{< headsingle level="4" >}} Switch {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes: `switch-md` (default) and `switch-xl`.
- Switches are now print-friendly. 📑

📝 **Updated**
- Uses CSS pseudo-elements for the toggle thumb instead of box shadow, making it more accessible and polished. 👍
- Enhanced forced color mode for better accessibility.

<!-- Textarea -->

{{< headsingle level="4" >}} Textarea {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes: `textarea-xs`, `textarea-sm`, `textarea-md` (default), `textarea-lg`, `textarea-xl`.
- Added example for Textarea group layout. Perfect for responsive forms! 📝

📝 **Updated**
- Updated `textarea-floating` structure for a cleaner and more streamlined layout.
- Adjusted the size scale to better align with other components.

❎ **Removed:**  
- Removed `textarea-filled` variant.

**Textarea floating**

```html
<!-- Before -->
<div class="relative sm:w-96">
  <textarea class="textarea textarea-floating peer" placeholder="Hello!!!" id="textareaFloating"></textarea>
  <label class="textarea-floating-label" for="textareaFloating">Your bio</label>
</div>
```
<br/>

```html
<!-- After -->
<div class="textarea-floating sm:w-96">
  <textarea class="textarea" placeholder="Hello!!!" id="textareaFloating"></textarea>
  <label class="textarea-floating-label" for="textareaFloating">Your bio</label>
</div>
```


<!-- Advanced forms -->

{{< headsingle level="3" >}} Advanced forms {{< /headsingle >}}
<div class="divider"></div>

<!-- Advanced select -->

{{< headsingle level="4" >}} Advanced select {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes: `advance-select-md` (default) and `advance-select-xl` for advance select (not for `tag` option).

<!--  Input Number  -->
{{< headsingle level="4" >}}  Input Number  {{< /headsingle >}}
📝 **Updated**
- After removing the `input-group`, the structure for certain input number fields has been changed.

```html
<!-- Before -->
<div class="input-group max-w-sm" data-input-number>
  <input class="input" type="text" value="1" aria-label="Input number" data-input-number-input />
  <span class="input-group-text gap-3">
    <button type="button" class="btn btn-primary btn-soft size-[22px] rounded min-h-0 p-0" aria-label="Decrement button" data-input-number-decrement>
      <span class="icon-[tabler--minus] size-3.5 flex-shrink-0"></span>
    </button>
    <button type="button" class="btn btn-primary btn-soft size-[22px] rounded min-h-0 p-0" aria-label="Increment button" data-input-number-increment>
      <span class="icon-[tabler--plus] size-3.5 flex-shrink-0"></span>
    </button>
  </span>
</div>
```
<br/>

```html
<!-- After -->
<div class="input max-w-sm" data-input-number>
  <input type="text" value="1" aria-label="Input number" data-input-number-input />
  <span class="my-auto flex gap-3">
    <button type="button" class="btn btn-primary btn-soft size-5.5 min-h-0 rounded-sm p-0" aria-label="Decrement button" data-input-number-decrement >
      <span class="icon-[tabler--minus] size-3.5 shrink-0"></span>
    </button>
    <button type="button" class="btn btn-primary btn-soft size-5.5 min-h-0 rounded-sm p-0" aria-label="Increment button" data-input-number-increment >
      <span class="icon-[tabler--plus] size-3.5 shrink-0"></span>
    </button>
  </span>
</div>
```

<!--  Pin Input  -->

{{< headsingle level="4" >}}  Pin Input  {{< /headsingle >}}
<br/>
🆕 **Added**
- New sizes: `pin-input-xs`, `pin-input-md` (default) and `pin-input-xl` for pin input.

<!--  Toggle Password  -->
{{< headsingle level="4" >}}  Toggle Password  {{< /headsingle >}}
📝 **Updated**
- After removing the `input-group`, the structure for toggle password example has been changed.

```html
<!-- Before -->
<div class="input-group max-w-sm">
  <input id="toggle-password" type="password" class="input" placeholder="Enter password" value="Pwd_1242@mA1" />
  <span class="input-group-text">
    <button type="button" data-toggle-password='{ "target": "#toggle-password" }' class="block" aria-label="password toggle">
      <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 flex-shrink-0"></span>
      <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 flex-shrink-0"></span>
    </button>
  </span>
</div>
```
<br/>

```html
<!-- After -->
<div class="input max-w-sm">
  <input id="toggle-password" type="password" placeholder="Enter password" value="Pwd_1242@mA1" />
  <button type="button" data-toggle-password='{ "target": "#toggle-password" }' class="block cursor-pointer" aria-label="password toggle" >
    <span class="icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0"></span>
    <span class="icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0"></span>
  </button>
</div>
```

<!-- Tables -->

{{< headsingle level="3" >}} Tables {{< /headsingle >}}
<div class="divider"></div>

<!-- Table -->

{{< headsingle level="4" >}} Table {{< /headsingle >}}
<br/>
🆕 **Added**
- New table sizes: `table-md` (default) and `table-xl`.

📝 **Updated**
- **Breaking Change**: Renamed `.hover` to `.row-hover`.
- **Breaking Change**: Renamed `.active` to `.row-active`. These changes are clearer and make the table interaction easier to understand. 💡

<!-- Mockups -->

{{< headsingle level="3" >}} Mockups {{< /headsingle >}}
<div class="divider"></div>

<!-- Artboard -->

{{< headsingle level="4" >}} Artboard {{< /headsingle >}}
<br/>
❎ **Removed**  
- **Breaking Change**: Removed all `artboard` and `phone-*` classes. These classes only set the width and height of the div, and now we recommend using Tailwind CSS `w-*` and `h-*` classes for better control and flexibility.

```html
<!-- Before -->
<div class="artboard artboard-demo phone-1">320 × 568</div>
```
<br/>

```html
<!-- After -->
<div class="w-[320px] h-[568px]">
```


<!-- Phone -->

{{< headsingle level="4" >}} Phone {{< /headsingle >}}
<br/>
📝 **Updated**  
- **Breaking Change**: Renamed `camera` to `mockup-phone-camera`. 
- **Breaking Change**: Renamed `display` to `mockup-phone-display`. 
- Removed the use of `artboard` in phone components.
➡️ The height and width are now defined inline for better control and flexibility.

<!-- Third party plugins -->

{{< headsingle level="3" >}} Third-party plugins {{< /headsingle >}}
<div class="divider"></div>

> ⚠️ **Important Note**: The installation steps for third-party components have been updated.  
➡️ Make sure your project follows the latest guidelines to ensure everything works smoothly. 🚀

<!-- Apexchart -->

{{< headsingle level="4" >}} Apexchart {{< /headsingle >}}
<br/>
📝 **Updated**  
- **Change**: Updated how to use semantic colors in JS files.  
➡️ **Why**: Previously, CSS variables only contained the oklch values (97.8% 0.005 297.73) without the `oklch()` function, allowing opacity to be added directly. Now, the variables include the full `oklch()` function (e.g., `oklch(97.8% 0.005 297.73)`), meaning opacity can no longer be appended directly.

```js
// Before
'oklch(var(--bc) / 0.4)'
```

<br/>


```js
// After
'color-mix(in oklab, var(--color-base-content) 40%, transparent)'
```

<!-- Datamaps -->

{{< headsingle level="4" >}} Datamaps {{< /headsingle >}}
<br/>
📝 **Updated**  
- **Change**: Updated how to use semantic colors in JS files.  
➡️ **Why**: Like Apexchart, the CSS variable now includes the `oklch()` function (e.g., `oklch(97.8% 0.005 297.73)`), so direct opacity adjustments are no longer possible.

```js
// Before
'oklch(var(--bc) / 0.4)'
```
<br/>

```js
// After
'color-mix(in oklab, var(--color-base-content) 40%, transparent)'
```
<br/>
<div class="divider my-4"></div>

That's it! You've reached the end of the FlyonUI 2 Update Guide. 🎉
