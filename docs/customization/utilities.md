---
title: "Utilities and Variables"
description: "Additional utility classes and CSS variables that FlyonUI uses for components and themes."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "customization"
    weight: 6

previous: Themes
previousLink: customization/themes/

next: RTL
nextLink: customization/rtl/
---
<!-------------------- Utility Classes and CSS Variables in FlyonUI -------------------->

{{< headsingle addClass="!mt-0" level="2" >}} Utility classes and CSS Variables {{< /headsingle >}}

FlyonUI provides an adaptable system of utility classes and CSS variables, enabling you to easily integrate components and customize themes across your project.

Below is a comprehensive overview of the essential utility classes and variables used throughout FlyonUI components.

<!-- Color utility classes -->

{{< headsingle level="2" >}} Color utility classes {{< /headsingle >}}

FlyonUI offers a variety of color utilities, including the primary color, which can be applied using standard Tailwind CSS utilities. These utilities can be used across various properties, making it simple to style your elements with ease.

Learn more about {{< link link="customization/colors/" addClass="link link-primary" >}}color names{{< /link >}}.

For example, use the primary color class with any Tailwind CSS utility like so:

{{< table >}}
Class Name|Description
bg-primary|Sets the background color to the primary color
to-primary|Sets the ending color for a gradient to the primary color
via-primary|Sets the middle color for a gradient to the primary color
from-primary|Sets the starting color for a gradient to the primary color
text-primary|Sets the text color to the primary color
ring-primary|Sets the ring color to the primary color
fill-primary|Sets the fill color for SVG elements to the primary color
caret-primary|Sets the caret color to the primary color
stroke-primary|Sets the stroke color for SVG elements to the primary color
border-primary|Sets the border color to the primary color
divide-primary|Sets the dividing border color to the primary color
accent-primary|Sets the accent color to the primary color
shadow-primary|Sets the shadow color to the primary color
outline-primary|Sets the outline color to the primary color
decoration-primary|Sets the text decoration color to the primary color
placeholder-primary|Sets the placeholder text color to the primary color
ring-offset-primary|Sets the ring offset color to the primary color
bg-primary/50|Background with 50% opacity
{{< /table >}}

<!-- Extended border radius utilities  -->

{{< headsingle level="2" >}} Extended border radius utilities {{< /headsingle >}}

FlyonUI includes extended border radius utilities that dynamically adjust based on the active theme. These custom radius classes are designed to provide unique shapes for elements like tooltips, buttons, and cards.

You can apply any Tailwind border-radius utility, such as `rounded-r-box` or `rounded-tr-field`, as needed for different components.

<div class="flex w-full items-center justify-evenly gap-4 py-6">
  <div class="text-bg-primary rounded-selector grid aspect-square w-35 h-28 place-content-center text-sm">rounded-selector</div>
  <div class="text-bg-primary rounded-field grid aspect-square w-35 h-28 place-content-center text-sm">rounded-field</div>
  <div class="text-bg-primary rounded-box grid aspect-square w-35 h-28 place-content-center text-sm">rounded-box</div>
</div>

{{< table >}}
Class Name|CSS Variable|Description
<span class="text-nowrap">rounded-box</span>|<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-radius-box)</span>|For large components like cards, modals, and alerts
rounded-field|<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-radius-field)</span>|For medium-sized components like buttons, inputs, selects, and tabs
rounded-selector|<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-radius-selector)</span>|For small components like checkboxes, toggles, and badges
{{< /table >}}

<!-------------------- Theme-Specific CSS variables -------------------->

{{< headsingle level="2" >}} Theme-Specific CSS variables {{< /headsingle >}}

Customize these CSS variables for each theme. Explore more about {{< link link="customization/colors/" addClass="link link-primary" >}}color names{{< /link >}}.

{{< table >}}
CSS Variable|Description
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-primary)</span>|Primary brand color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-primary-content)</span>|Content color to use on the primary color background
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-secondary)</span>|Secondary brand color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-secondary-content)</span>|Content color to use on the secondary color background
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-accent)</span>|Accent brand color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-accent-content)</span>|Content color to use on the accent color background
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-neutral)</span>|Neutral dark color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-neutral-content)</span>|Content color to use on the neutral color background
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-base-100)</span>|Base color for page backgrounds
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-base-200)</span>|Darker shade of the base color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-base-300)</span>|Even darker shade of the base color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-base-content)</span>|Content color to use on the base color background
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-info)</span>|Info color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-info-content)</span>|Content color to use on the info color background
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-success)</span>|Success color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-success-content)</span>|Content color to use on the success color background
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-warning)</span>|Warning color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-warning-content)</span>|Content color to use on the warning color background
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-error)</span>|Error color
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-color-error-content)</span>|Content color to use on the error color background
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-radius-selector)</span>|Border radius for selectors like checkboxes, toggles, badges, etc.
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-radius-field)</span>|Border radius for fields like inputs, selects, tabs, etc.
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-radius-box)</span>|Border radius for boxes like cards, modals, alerts, etc.
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-size-selector)</span>|Base size for selectors like checkboxes, toggles, badges, etc.
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-size-field)</span>|Base size for fields like inputs, selects, tabs, etc.
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-border)</span>|Border width for all components
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-depth)</span>|(binary) Adds depth effect to relevant components
<span class="badge badge-sm badge-soft text-nowrap rounded-full">var(-\-noise)</span>|(binary) Adds noise effect to the background of relevant components
{{< /table >}}

<!-------------------- Component-Specific CSS variables -------------------->

{{< headsingle level="2" >}} Component-Specific CSS variables {{< /headsingle >}}

Some FlyonUI components utilize their own CSS variables for fine-grained customization. These allow you to adjust the appearance of individual components with greater control.
{{< table >}}
Component|CSS Variable|Description
Alert|-\-alert-color|Sets the color of the alert
Badge|-\-badge-color|Sets the color of the badge
|-\-size|Sets the size of the badge
Button|-\-btn-color|Sets the background color of the button
|-\-btn-fg|Sets the foreground color of the button
|-\-btn-shadow|Sets the shadow effect of the button
|-\-btn-noise|Sets the noise effect on the button (if enabled)
|-\-btn-p|Sets the padding of the button
|-\-size|Sets the size of the button
|-\-dark-shade|Dark shade generated for gradient buttons based on `btn-color`
Card|-\-card-p|Sets the padding of the card body
|-\-card-border|Sets the border width of the card
|-\-card-shadow|Sets the shadow effect of the card
Checkbox|-\-size|Sets the size of the checkbox
|-\-input-color|Sets the border and background color when the checkbox is checked
Indicator|-\-indicator-t|Sets the top position of the indicator
|-\-indicator-b|Sets the bottom position of the indicator
|-\-indicator-s|Sets the start position of the indicator
|-\-indicator-e|Sets the end position of the indicator
|-\-indicator-y|Sets the vertical position of the indicator
|-\-indicator-x|Sets the horizontal position of the indicator
Input|-\-input-color|Sets the color of the input
|-\-size|Sets the size of the input
Kbd|-\-size|Sets the size of the keyboard element
Link|-\-link-color|Sets the color of the link
Menu|-\-menu-active-fg|Sets the foreground color of the active menu item
|-\-menu-active-bg|Sets the background color of the active menu item
Radial Progress|-\-value|Sets the value of the radial progress
|-\-size|Sets the size of the radial progress
|-\-thickness|Sets the thickness of the radial progress
|-\-radialprogress|Used for calculating the position of the radial progress
Radio|-\-input-color|Sets the border and background color when the radio button is checked
|-\-size|Sets the size of the radio button
Range|-\-range-color|Sets the background color of the range slider thumb
|-\-range-thumb-size|Sets the color of the range slider thumb
|-\-range-thumb-border-width|Sets the size of the range slider thumb
|-\-range-track-height|Sets the track height for the range slider
Select|-\-input-color|Sets the color of the input in the select
|-\-size|Sets the size of the select element
Switches|-\-input-color|Sets the color of the switch's background, border, or text
|-\-toggle-p|Sets the padding of the toggle
|-\-size|Sets the size of the toggle
Tab|-\-tabs-height|Sets the height of the tabs
|-\-tabs-direction|Sets the direction of the tabs
|-\-size| Size of tab
|-\-tab-p|Sets the padding of the tab
|-\-tab-bg|Sets the background color of the tab
|-\-tab-border-color|Sets the border color of the tab
|-\-tab-border| Border width for tab
|-\-tab-grad|  Lifted tab utility
|-\-tab-radius| Lifted tab radius
Textarea|-\-input-color|Sets the color of the textarea
|-\-size|Sets the size of the textarea
Timeline|-\-timeline-row-start|Sets the start position of the timeline row
|-\-timeline-row-end|Sets the end position of the timeline row
|-\-timeline-col-start|Sets the start position of the timeline column
|-\-timeline-col-end|Sets the end position of the timeline column
Glass|-\-glass-blur|Sets the blur intensity of the glass effect
|-\-glass-opacity|Sets the opacity of the glass effect
|-\-glass-reflect-degree|Sets the reflection degree of the glass effect
|-\-glass-reflect-opacity|Sets the opacity of the glass reflection
|-\-glass-border-opacity|Sets the opacity of the glass border
|-\-glass-text-shadow-opacity|Sets the opacity of the glass text shadow
Join|-\-join-ss|Sets the start start border radius for the join
|-\-join-se|Sets the start end border radius for the join
|-\-join-es|Sets the end start border radius for the join
|-\-join-ee|Sets the end end border radius for the join
{{< /table >}}

<!-------------------- Custom JS component variants -------------------->

{{< headsingle level="2" >}} Custom JS Component Variants {{< /headsingle >}}

These variants are designed for headless JS components like dropdowns, overlays, tooltips, etc. They function similarly to other TailwindCSS-like state or responsive variants (e.g., `checked:` and `md:`).

These variants apply specific TailwindCSS utility classes based on a particular component's state or condition.

{{< table >}}
Variants|Description
dropdown-open:{tw-utility-classes}|Applies TailwindCSS classes when the dropdown is open
removing:{tw-utility-classes}|Applies TailwindCSS classes during element removal
tooltip-shown:{tw-utility-classes}|Applies TailwindCSS classes when the tooltip is visible
accordion-item-active:{tw-utility-classes}|Applies TailwindCSS classes when an accordion item is active
accordion-selected:{tw-utility-classes}|Applies TailwindCSS classes when an accordion item is selected
collapse-open:{tw-utility-classes}|Applies TailwindCSS classes when a collapse element is open
active-tab:{tw-utility-classes}|Applies TailwindCSS classes when a tab is active
overlay-open:{tw-utility-classes}|Applies TailwindCSS classes when an overlay is open
overlay-layout-open:{tw-utility-classes}|Applies TailwindCSS classes when an overlay layout is open
overlay-backdrop-open:{tw-utility-classes}|Applies TailwindCSS classes when an overlay backdrop is open
scrollspy-active:{tw-utility-classes}|Applies TailwindCSS classes when an element is active in scrollspy
carousel-active:{tw-utility-classes}|Applies TailwindCSS classes when a carousel item is active
carousel-disabled:{tw-utility-classes}|Applies TailwindCSS classes when a carousel item is disabled
selected:{tw-utility-classes}|Applies TailwindCSS classes when an element is selected
select-disabled:{tw-utility-classes}|Applies TailwindCSS classes when a select element is disabled
select-active:{tw-utility-classes}|Applies TailwindCSS classes when a select element is active
select-opened:{tw-utility-classes}|Applies TailwindCSS classes when a select dropdown is opened
input-number-disabled:{tw-utility-classes}|Applies TailwindCSS classes when a number input is disabled
pin-input-active:{tw-utility-classes}|Applies TailwindCSS classes when a pin input field is active
password-active:{tw-utility-classes}|Applies TailwindCSS classes when a password field is active
stepper-active:{tw-utility-classes}|Applies TailwindCSS classes when a stepper step is active
stepper-success:{tw-utility-classes}|Applies TailwindCSS classes when a stepper step is successful
stepper-completed:{tw-utility-classes}|Applies TailwindCSS classes when a stepper step is completed
stepper-error:{tw-utility-classes}|Applies TailwindCSS classes when a stepper step encounters an error
stepper-processed:{tw-utility-classes}|Applies TailwindCSS classes when a stepper step is processed
stepper-disabled:{tw-utility-classes}|Applies TailwindCSS classes when a stepper step is disabled
stepper-skipped:{tw-utility-classes}|Applies TailwindCSS classes when a stepper step is skipped
strong-password:{tw-utility-classes}|Applies TailwindCSS classes when a password is strong
strong-password-accepted:{tw-utility-classes}|Applies TailwindCSS classes when a strong password is accepted
strong-password-active:{tw-utility-classes}|Applies TailwindCSS classes when a strong password is actively typed
combo-box-active:{tw-utility-classes}|Applies TailwindCSS classes when a combo box is active
combo-box-selected:{tw-utility-classes}|Applies TailwindCSS classes when a combo box item is selected
combo-box-has-value:{tw-utility-classes}|Applies TailwindCSS classes when a combo box has a value
combo-box-tab-active:{tw-utility-classes}|Applies TailwindCSS classes when a tab in the combo box is active
file-upload-complete:{tw-utility-classes}|Applies TailwindCSS classes when a file upload is complete
{{< /table >}}

<!-------------------- Glass Effect -------------------->

{{< headsingle level="2" >}} Glass Effect {{< /headsingle >}}

Create a stunning frosted-glass appearance in your UI with the `glass` class. This effect adds a sleek matte finish to your components, ideal for modern, layered UI designs.

<div class="w-full rounded-sm p-10 mb-4" style="background-image: url(https://cdn.flyonui.com/fy-assets/components/carousel/image-21.png);" >
  <div class="glass rounded-box grid h-40 w-full place-content-center">Glass</div>
</div>

```html
<div class="glass">Glass</div>
```
