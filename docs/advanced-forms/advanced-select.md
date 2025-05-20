---
title: "Advanced select"
components: 6
description: "The Advanced Select Component enhances traditional select boxes with features like search and tagging, offering versatility for complex selection needs."
bg_image: "svg/form-elements/advanced-select.svg"
tag: updated
tag_bg: success
menu:
  main:
    parent: "advanced forms"

previous: Text Area
previousLink: forms/textarea/

next: Combo Box
nextLink: advanced-forms/combo-box/

requires_js: true

pageJS:
  - "/js/pages/advance-select.js"
---


{{< callout "info" >}}
Advance select components are adopted from <a href="https://preline.co/docs/advanced-select.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class Table -->

{{< class-table >}}

advance-select-toggle| modifier | The `advance-select-toggle` component class is used for `:toggleClasses`, providing base styles to select toggle.
advance-select-menu | modifier | The `advance-select-menu` component class is used for `:dropdownClasses`, providing base styles to select dropdown menu.
advance-select-option | modifier | The `advance-select-option` component class is used for `:optionClasses`, providing base styles for individual select dropdown options.
advance-select-tag | modifier | The `advance-select-tag` component class is utilized for `wrapperClasses` when `:mode` is configured as tag.
select-active|state| apply active state to advance-select-option.
select-opened:{tw-utility-class} | variant | The modifier allows setting Tailwind classes when a select has been opened.
select-disabled:{tw-utility-class} | variant | The modifier allows setting Tailwind classes when a select has the `disabled` attribute.
selected:{tw-utility-class} | variant | The modifier allows setting Tailwind classes when a option is selected.
advance-select-xs | size | Apply `advance-select-xs` along with `advance-select-toggle` to implement a extra small size.
advance-select-sm | size | Apply `advance-select-sm` along with `advance-select-toggle` to implement a small size.
advance-select-md | size | Apply `advance-select-md` along with `advance-select-toggle` to implement a medium(defautl) size.
advance-select-lg | size | Apply `advance-select-lg` along with `advance-select-toggle` to implement a large size.
advance-select-xl | size | Apply `advance-select-xl` along with `advance-select-toggle` to implement a extra large size.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

A basic usage of advanced select.

Please refer to the <a href="#basic-options" class="link link-primary">Basic option</a> section for all basic functionalities.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>
{{< /code >}}

<!-- Placeholder -->

{{< headname level="3" >}} Placeholder {{< /headname >}}

To customize the placeholder with either an icon or plain text, you can provide custom HTML within the `"placeholder:"` option as demonstrated below.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    data-select='{
    "placeholder": "<span class=\"inline-flex items-center\"><span class=\"icon-[tabler--filter] shrink-0 size-4 me-2\"></span> Filter</span>",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
  }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>
{{< /code >}}

<!-------------------- Size -------------------->

{{< headname level="2" >}} Size {{< /headname >}}

<!-- Advanced select sizes -->

{{< headname level="3" >}} Advanced select sizes {{< /headname >}}

Add responsive class `advance-select-{size}` where `{size} = xs|sm|md|lg|xl` for advance select of different sizes. The size is now determined by the element’s height instead of its padding.

{{< code addClass="!block h-80 overflow-y-auto" >}}

<div class="max-w-sm space-y-4">
  <!-- Extra small -->
  <select
    data-select='{
      "placeholder": "Select option...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle advance-select-xs select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu",
      "dropdownSpace": 5,
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-3.5 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
      }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>

  <!-- Small -->

<select
  data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle advance-select-sm select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "dropdownSpace": 8,
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-3.5 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }' class="hidden" >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
</select>

<!-- Default -->

<select
  data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle advance-select-md select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }' class="hidden" >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
</select>

<!-- Large -->

<select
  data-select='{
  "placeholder": "Select option...",
  "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
  "toggleClasses": "advance-select-toggle advance-select-lg select-disabled:pointer-events-none select-disabled:opacity-40",
  "dropdownClasses": "advance-select-menu",
  "optionClasses": "advance-select-option selected:select-active",
  "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-5 text-primary hidden selected:block \"></span></div>",
  "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-5 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
  }'
  class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>

<!-- Extra large -->

<select
  data-select='{
  "placeholder": "Select option...",
  "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
  "toggleClasses": "advance-select-toggle advance-select-xl select-disabled:pointer-events-none select-disabled:opacity-40",
  "dropdownClasses": "advance-select-menu",
  "optionClasses": "advance-select-option selected:select-active",
  "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-6 text-primary hidden selected:block \"></span></div>",
  "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-5 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
  }'
  class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>
{{< /code >}}

<!-------------------- Validation states -------------------->

{{< headname level="2" >}} Validation states {{< /headname >}}

<!-- Success state -->

{{< headname level="3" >}} Success state {{< /headname >}}

Success state can be show using `is-valid` class.

{{< code addClass="!block h-80" >}}

<div class="max-w-sm">
  <div>
    <label class="label-text" for="validSelect"> Choose your option </label>
    <select
      data-select='{
      "placeholder": "Select option...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
      }'
      class="is-valid hidden" id="validSelect"
    >
      <option value="">Choose</option>
      <option value="name">Full Name</option>
      <option value="email">Email Address</option>
      <option value="description">Project Description</option>
      <option value="user_id">User Identification Number</option>
    </select>
    <span class="helper-text">Helper text</span>
  </div>
</div>
{{< /code >}}

<!-- Error state -->

{{< headname level="3" >}} Error state {{< /headname >}}

Error state can be show using `is-invalid` class.

{{< code addClass="!block h-80" >}}

<div class="max-w-sm">
  <div>
    <label class="label-text" for="invalidSelect"> Choose your option </label>
    <select
      data-select='{
      "placeholder": "Select option...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
      }'
      class="is-invalid hidden" id="invalidSelect"
    >
      <option value="">Choose</option>
      <option value="name">Full Name</option>
      <option value="email">Email Address</option>
      <option value="description">Project Description</option>
      <option value="user_id">User Identification Number</option>
    </select>
    <span class="helper-text">Helper text</span>
  </div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Fixed position -->

{{< headname level="3" >}} Fixed position {{< /headname >}}

To fix the dropdown's vertical placement, you can specify the `dropdownVerticalFixedPlacement:` option and define the desired position, as demonstrated in the example below.

{{< code addClass="!block h-80" >}}

<div class="max-w-sm">
  <select
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "dropdownVerticalFixedPlacement": "bottom",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>
{{< /code >}}

<!-- Disabled -->

{{< headname level="3" >}} Disabled {{< /headname >}}

To render selects as inactive, include the disabled boolean attribute within the `select` element and utilize the class `select-disabled:*` within the `"toggleClasses":` section for styling purposes.

{{< code addClass="!block" >}}

<div class="max-w-sm">
  <select
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content/50 absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
    disabled
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>
{{< /code >}}

<!-- Multiple -->

{{< headname level="3" >}} Multiple {{< /headname >}}

Select multiple options.

Please refer to the <a href="#multiple-options" class="link link-primary">Multiple option</a> section for all multiple related functionalities.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    multiple
    data-select='{
    "placeholder": "Select multiple options...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>
{{< /code >}}

<!-- Multiple with option template  -->

{{< headname level="3" >}} Multiple with option template {{< /headname >}}

Select multiple options and add an option template.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <!-- Select -->
  <select
    multiple=""
    data-select='{
    "placeholder": "Select multiple options...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><div class=\"me-2\" data-icon></div><div><div class=\"text-sm text-base-content \" data-title></div></div><div class=\"ms-auto\"><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
  }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option
      selected=""
      value="1"
      data-select-option='{ "icon": "<img class=\"shrink-0 size-6 rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-5.png\" alt=\"Ethan Caldwell\" />"}'
    >
      Ethan Caldwell
    </option>
    <option
      value="2"
      data-select-option='{ "icon": "<img class=\"shrink-0 size-6 rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png\" alt=\"Isabella Martinez\" />"}'
    >
      Isabella Martinez
    </option>
    <option
      value="3"
      data-select-option='{ "icon": "<img class=\"shrink-0 size-6 rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Ava Thompson\" />"}'
    >
      Ava Thompson
    </option>
  </select>
  <!-- End Select -->
</div>
{{< /code >}}

<!-- Multiple with counter -->

{{< headname level="3" >}} Multiple with counter {{< /headname >}}

If you only want to display the number of the selected option in multiple select. then use `"toggleCountText":`.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    multiple
    data-select='{
    "placeholder": "Select multiple options...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "toggleCountText": "selected",
    "toggleCountTextMinItems": 2,
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>
{{< /code >}}

<!-- Multiple with conditional counter -->

{{< headname level="3" >}} Multiple with conditional counter {{< /headname >}}

Use `multiple` tag to enable counter option that counts the number of selected options.

{{< code jsCode="true" addClass="!block h-72" >}}

  <!-- Select -->
<div class="max-w-sm">
  <select
    id="multi-cond-count"
    multiple=""
    data-select='{
      "placeholder": "Select multiple options...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "toggleSeparators": {
        "betweenItemsAndCounter": "&"
      },
      "toggleCountText": "+",
      "toggleCountTextPlacement": "prefix-no-space",
      "toggleCountTextMinItems": 3,
      "toggleCountTextMode": "nItemsAndCount",
      "dropdownClasses": "advance-select-menu max-h-44 overflow-y-auto",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option>Name</option>
    <option>Email address</option>
    <option>Description</option>
    <option>User ID</option>
    <option>Address</option>
    <option>City</option>
    <option>Country</option>
  </select>
  <!-- End Select -->
</div>

<div class="mt-4 flex flex-wrap gap-2">
  <button type="button" id="clear-btn" class="btn btn-outline btn-primary btn-sm">Clear</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () =>
    requestAnimationFrame(() => {
      ;(function () {
        const clearBtn = document.querySelector('#clear-btn')

        clearBtn.addEventListener('click', () => {
          const clearSelectBtn = HSSelect.getInstance('#multi-cond-count', true)

          clearSelectBtn.element.setValue([])
        })
      })()
    })
  )
</script>
{{< /code >}}

<!-- Search -->

{{< headname level="3" >}} Search {{< /headname >}}

To enable searching within the dropdown, set `"hasSearch": true`.

Please refer to the <a href="#search-options" class="link link-primary">Search option</a> section for all search-related functionalities.

{{< callout "info" >}}
When utilizing the <code>"searchWrapperClasses"</code> or <code>"searchClasses"</code> options for custom styling, note that the default styling provided by the script file will be removed. Make sure to style these options completely from scratch using Tailwind's classes.
{{< /callout >}}

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    data-select='{
    "placeholder": "Select your sign",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "hasSearch": true,
    "dropdownClasses": "advance-select-menu max-h-52 pt-0 overflow-y-auto",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="aries">Aries</option>
    <option value="taurus">Taurus</option>
    <option value="gemini">Gemini</option>
    <option value="cancer">Cancer</option>
    <option value="leo">Leo</option>
    <option value="virgo">Virgo</option>
    <option value="libra">Libra</option>
    <option value="scorpio">Scorpio</option>
    <option value="sagittarius">Sagittarius</option>
    <option value="capricorn">Capricorn</option>
    <option value="aquarius">Aquarius</option>
    <option value="pisces">Pisces</option>
  </select>
</div>
{{< /code >}}

<!-- Search result limit -->

{{< headname level="3" >}} Search result limit {{< /headname >}}

Set a maximum limit for search results by using the parameter `searchLimit: 5`.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    data-select='{
      "hasSearch": true,
      "searchLimit": 5,
      "placeholder": "Select your sign",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu max-h-52 pt-0 overflow-y-auto",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="aries">Aries</option>
    <option value="taurus">Taurus</option>
    <option value="gemini">Gemini</option>
    <option value="cancer">Cancer</option>
    <option value="leo">Leo</option>
    <option value="virgo">Virgo</option>
    <option value="libra">Libra</option>
    <option value="scorpio">Scorpio</option>
    <option value="sagittarius">Sagittarius</option>
    <option value="capricorn">Capricorn</option>
    <option value="aquarius">Aquarius</option>
    <option value="pisces">Pisces</option>
  </select>
</div>
{{< /code >}}


<!-- Minimum search Length -->

{{< headname level="3" badge-text="new" >}} Minimum search Length {{< /headname >}}

Set `"minSearchLength":2` to define the minimum number of characters required before initiating a search.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    data-select='{
      "hasSearch": true,
      "minSearchLength": 2,
      "placeholder": "Select your sign",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu max-h-52 pt-0 overflow-y-auto",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden overflow"
  >
    <option value="">Choose</option>
    <option value="AF">Afghanistan</option>
    <option value="AX">Aland Islands</option>
    <option value="AL">Albania</option>
    <option value="DZ">Algeria</option>
    <option value="AS">American Samoa</option>
    <option value="AD">Andorra</option>
    <option value="AO">Angola</option>
    <option value="AI">Anguilla</option>
    <option value="AG">Antigua and Barbuda</option>
    <option value="AR">Argentina</option>
    <option value="AM">Armenia</option>
    <option value="AW">Aruba</option>
    <option value="AU">Australia</option>
    <option value="AT">Austria</option>
    <option value="AZ">Azerbaijan</option>
    <option value="BS">Bahamas</option>
    <option value="BH">Bahrain</option>
    <option value="BD">Bangladesh</option>
    <option value="BB">Barbados</option>
    <option value="BY">Belarus</option>
    <option value="BE">Belgium</option>
    <option value="BZ">Belize</option>
    <option value="BJ">Benin</option>
    <option value="BM">Bermuda</option>
    <option value="BT">Bhutan</option>
    <option value="BO">Bolivia (Plurinational State of)</option>
    <option value="BQ">Bonaire, Sint Eustatius and Saba</option>
    <option value="BA">Bosnia and Herzegovina</option>
    <option value="BW">Botswana</option>
    <option value="BR">Brazil</option>
    <option value="IO">British Indian Ocean Territory</option>
    <option value="BN">Brunei Darussalam</option>
    <option value="BG">Bulgaria</option>
    <option value="BF">Burkina Faso</option>
    <option value="BI">Burundi</option>
    <option value="CV">Cabo Verde</option>
    <option value="KH">Cambodia</option>
    <option value="CM">Cameroon</option>
    <option value="CA">Canada</option>
    <option value="KY">Cayman Islands</option>
    <option value="CF">Central African Republic</option>
    <option value="TD">Chad</option>
    <option value="CL">Chile</option>
    <option value="CN">China</option>
    <option value="CX">Christmas Island</option>
    <option value="CC">Cocos (Keeling) Islands</option>
    <option value="CO">Colombia</option>
    <option value="KM">Comoros</option>
    <option value="CK">Cook Islands</option>
    <option value="CR">Costa Rica</option>
    <option value="HR">Croatia</option>
    <option value="CU">Cuba</option>
    <option value="CW">Curaçao</option>
    <option value="CY">Cyprus</option>
    <option value="CZ">Czech Republic</option>
    <option value="CI">Côte Ivoire</option>
    <option value="CD">Democratic Republic of the Congo</option>
    <option value="DK">Denmark</option>
    <option value="DJ">Djibouti</option>
    <option value="DM">Dominica</option>
    <option value="DO">Dominican Republic</option>
    <option value="EC">Ecuador</option>
    <option value="EG">Egypt</option>
    <option value="SV">El Salvador</option>
    <option value="GB-ENG">England</option>
    <option value="GQ">Equatorial Guinea</option>
    <option value="ER">Eritrea</option>
    <option value="EE">Estonia</option>
    <option value="ET">Ethiopia</option>
    <option value="FK">Falkland Islands</option>
    <option value="FO">Faroe Islands</option>
    <option value="FM">Federated States of Micronesia</option>
    <option value="FJ">Fiji</option>
    <option value="FI">Finland</option>
    <option value="FR">France</option>
  </select>
</div>
{{< /code >}}

<!-- Disabling direct match searching -->

{{< headname level="3" >}} Direct match searching Off {{< /headname >}}

Set `isSearchDirectMatch: false` to turn off direct match searching, allowing for broader search results without exact term matching.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    multiple
    data-select='{
      "hasSearch": true,
      "isSearchDirectMatch": false,
      "searchPlaceholder": "Search options...",
      "placeholder": "Select options...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu max-h-48 -ms-1 overflow-y-auto pt-0",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex items-center\"> <div class=\"size-8 me-2\" data-icon></div><div><div class=\"text-sm font-semibold text-base-content\" data-title></div> <div class=\"text-xs text-base-content/80\" data-description></div></div><div class=\"flex justify-between items-center flex-1\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div> </div>",
      "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
    aria-label="Advance select"
  >
    <option value="">Choose</option>
    <option
      selected=""
      value="1"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png\" alt=\"Mark Gilbert\" />"}'
    >
      Mark Gilbert
    </option>
    <option
      value="2"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png\" alt=\"Eugenia Parsons\" />"}'
    >
      Eugenia Parsons
    </option>
    <option
      value="3"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Francis Byrd\" />"}'
    >
      Francis Byrd
    </option>
    <option
      value="4"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png\" alt=\"Jayden Rogers\" />"}'
    >
      Mark@Gilbert
    </option>
     <option
      value="5"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png\" alt=\"Eugenia Parsons\" />"}'
    >
      Eugenia#Parsons
    </option>
    <option
      value="6"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Francis Byrd\" />"}'
    >
      Francis-Byrd
    </option>
    <option
      value="7"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png\" alt=\"Jayden Rogers\" />"}'
    >
      Mark.Gilbert
    </option>
     <option
      value="8"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png\" alt=\"Eugenia Parsons\" />"}'
    >
      Eugenia_Parsons
    </option>
    <option
      value="9"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Francis Byrd\" />"}'
    >
      Francis%Byrd
    </option>
    </option>
    <option
      value="7"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png\" alt=\"Jayden Rogers\" />"}'
    >
      Ma@rk Gilbert
    </option>
     <option
      value="8"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png\" alt=\"Eugenia Parsons\" />"}'
    >
      Eugenia Par-sons
    </option>
    <option
      value="9"
      data-select-option='{
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Francis Byrd\" />"}'
    >
      Francis B#yrd
    </option>
  </select>
</div>
{{< /code >}}

<!-- Tags -->

{{< headname level="3" >}} Tags {{< /headname >}}

Create a custom select with removable tags using the provided options:

- `"wrapperClasses"`: This option wraps the select element. Apply the class `advance-select-tag` for default styling.
- `"tagsItemTemplate"`: This section is dedicated to styling the selected tag.
- Use `data-select-option` to customize options.

Please see the <a href="#tag-options" class="link link-primary">Tags option</a> section for tag-related functionalities.

> Sizing `advance-select-*` doesn't work for tags options

{{< callout "error" >}}
If you adjust the padding at the start within `"wrapperClasses"` to the option menu with the select, apply a negative margin to `dropdownClasses`.
{{< /callout >}}

{{< code addClass="!block h-[450px] sm:h-80 overflow-y-auto" >}}

<div class="max-w-sm">
  <select
    multiple
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu max-h-48 -ms-1 overflow-y-auto",
    "optionClasses": "advance-select-option selected:select-active",
    "mode": "tags",
    "wrapperClasses": "advance-select-tag flex-wrap",
    "tagsItemTemplate": " <div class=\"flex flex-nowrap items-center relative z-10 bg-base-100 border border-base-content/25 rounded-full p-1 m-1\"> <div class=\"size-6 me-1\" data-icon></div> <div class=\"whitespace-nowrap text-base-content\" data-title></div> <div class=\"btn btn-sm min-h-0 size-5 btn-circle btn-soft btn-secondary ms-2 \" data-remove><span class=\"icon-[tabler--x] shrink-0 size-3.5\"></span></div> </div>",
    "tagsInputClasses": "py-2.5 px-2 rounded-lg order-1 text-sm outline-none",
    "optionTemplate": "<div class=\"flex items-center\"> <div class=\"size-8 me-2\" data-icon></div><div><div class=\"text-sm font-semibold text-base-content\" data-title></div> <div class=\"text-xs text-base-content/80\" data-description></div></div><div class=\"flex justify-between items-center flex-1\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div> </div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
    aria-label="Advance select"
  >
    <option value="">Choose</option>
    <option
      selected=""
      value="1"
      data-select-option='{
        "description": "mark",
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png\" alt=\"Mark Gilbert\" />"}'
    >
      Mark Gilbert
    </option>
    <option
      value="2"
      data-select-option='{
        "description": "eug",
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png\" alt=\"Eugenia Parsons\" />"}'
    >
      Eugenia Parsons
    </option>
    <option
      value="3"
      data-select-option='{
        "description": "francis",
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Francis Byrd\" />"}'
    >
      Francis Byrd
    </option>
    <option
      value="4"
      data-select-option='{
        "description": "rogers",
        "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-3.png\" alt=\"Jayden Rogers\" />"}'
    >
      Jayden Rogers
    </option>
  </select>
</div>
{{< /code >}}

<!-- Custom option -->

{{< headname level="3" >}} Custom option {{< /headname >}}

Example of custom option with avatar and icons. Using `data-select-option` for providing content for the option.

<!-- Icon -->

{{< headname level="4" >}} Icon {{< /headname >}}

Basic example of options with icon.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"><span class=\"me-2 flex\" data-icon></span><span class=\"text-base-content\" data-title></span></button>",
    "toggleClasses": "advance-select-toggle items-center",
    "dropdownClasses": "advance-select-menu max-h-44",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div><div class=\"flex items-center\"> <div class=\"me-2 flex\" data-icon></div> <div class=\"font-semibold text-base-content\" data-title></div> </div> <div class=\"mt-1.5 text-sm text-base-content/80\" data-description></div> </div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option
      value="5"
      selected
      data-select-option='{
        "description": "Recommended for beginners.",
        "icon": "<span class=\"icon-[tabler--circle-check] shrink-0 size-4 text-base-content\"></span>"}'
    >
      Beginner-friendly
    </option>
    <option
      value="6"
      data-select-option='{
        "description": "Suitable for advanced users.",
        "icon": "<span class=\"icon-[tabler--target] shrink-0 size-4 text-base-content\"></span>"}'
    >
      Advanced users
    </option>
  </select>
</div>
{{< /code >}}

<!-- Avatar -->

{{< headname level="4" >}} Avatar {{< /headname >}}

Basic example of options with avatar.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"><span class=\"size-6 me-2\" data-icon></span><span class=\"text-base-content\" data-title></span></button>",
    "toggleClasses": "advance-select-toggle items-center",
    "dropdownClasses": "advance-select-menu max-h-44 overflow-y-auto",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex items-start\"> <div class=\"size-6 me-2\" data-icon></div> <div> <div class=\"text-base-content\" data-title></div><div></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option
      selected=""
      value="1"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png\" alt=\"Mark Gilbert\" />"}'
    >
      Mark Gilbert
    </option>
    <option
      value="2"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png\" alt=\"Eugenia Parsons\" />"}'
    >
      Eugenia Parsons
    </option>
    <option
      value="3"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Francis Byrd\" />"}'
    >
      Francis Byrd
    </option>
    <option
      value="4"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-3.png\" alt=\"Jayden Rogers\" />"}'
    >
      Jayden Rogers
    </option>
  </select>
</div>
{{< /code >}}

<!-- Modal example -->

{{< headname level="3" >}} Modal example {{< /headname >}}

Basic usage in modal window.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="select-modal" data-overlay="#select-modal" > Open modal </button>

<div id="select-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#select-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body h-72">
        <select
          data-select='{
          "placeholder": "Select option...",
          "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
          "toggleClasses": "advance-select-toggle mt-0.5",
          "dropdownClasses": "advance-select-menu shadow-none border border-base-content/25",
          "optionClasses": "advance-select-option selected:select-active",
          "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
          "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
          }'
          class="hidden"
        >
          <option value="">Choose</option>
          <option value="name">Full Name</option>
          <option value="email">Email Address</option>
          <option value="description">Project Description</option>
          <option value="user_id">User Identification Number</option>
        </select>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#select-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Add/Remove option -->

{{< headname level="3" >}} Add/Remove option {{< /headname >}}

Utilize the `addOption` and `removeOption` methods to <a href="#add-method" class="link link-primary">add</a> or <a href="#remove-method" class="link link-primary">remove</a> options, respectively.

{{< code jsCode="true" addClass="!block h-80" >}}

<div class="mb-4 flex gap-3">
  <button class="btn btn-primary" id="add-option">Add</button>
  <button class="btn btn-primary" id="remove-option">Remove</button>
</div>
<div class="max-w-sm">
  <select
    id="add-remove-select"
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu max-h-48 overflow-y-auto",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () =>
    requestAnimationFrame(() => {
      const addRemove = window.HSSelect.getInstance('#add-remove-select')
      const addOptionsBtn = document.querySelector('#add-option')
      const removeOptionsBtn = document.querySelector('#remove-option')

      addOptionsBtn.addEventListener('click', () => {
        addRemove.addOption([
          {
            title: 'James Collins',
            val: '1'
          },
          {
            title: 'Amanda Harvey',
            val: '2'
          }
        ])
      })

      removeOptionsBtn.addEventListener('click', () => {
        addRemove.removeOption(['1', '2'])
      })
    })
  )
</script>
{{< /code >}}

<!-- Destroy/Reinitialize -->

{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}

The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a select element.

{{< code jsCode="true" addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    id="destroy-select"
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span id=\"select-icon\" class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>
<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () =>
    requestAnimationFrame(() => {
      const destroyBtn = document.querySelector('#destroy-btn')
      const reinitBtn = document.querySelector('#reinit-btn')
      const selectEl = document.querySelector('#destroy-select')
      const selectToggleIcon = document.querySelector('#select-icon')
      const destroySelect = window.HSSelect.getInstance('#destroy-select')

      // destroy and reinit select
      destroyBtn.addEventListener('click', () => {
        destroySelect.destroy()
        selectToggleIcon.style.display = 'none'

        reinitBtn.removeAttribute('disabled')
        destroyBtn.setAttribute('disabled', true)
      })

      reinitBtn.addEventListener('click', () => {
        new HSSelect(selectEl)
        selectToggleIcon.style.display = ''

        reinitBtn.setAttribute('disabled', true)
        destroyBtn.removeAttribute('disabled')
      })
    })
  )
</script>
{{< /code >}}

<!-- Set a single value with a setter. -->

{{< headname level="3" >}} Set a single value with a setter. {{< /headname >}}

Provides `setValue` <a href="#set-method" class="link link-primary">method</a> that helps to set a value programmatically.

{{< code jsCode="true" addClass="!block h-72" >}}

<div class="max-w-sm">
  <!-- Select -->
  <select
    id="single-setter"
    data-select='{
    "placeholder": "Select with button",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"><span class=\"size-6 me-2\" data-icon></span><span class=\"text-base-content\" data-title></span></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex items-start\"> <div class=\"size-6 me-2\" data-icon></div> <div> <div class=\"text-base-content\" data-title></div><div></div>",
    "extraMarkup": "<span id=\"select-icon\" class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
  }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option
      selected=""
      value="1"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-5.png\" alt=\"Ethan Caldwell\" />"}'
    >
      Ethan Caldwell
    </option>
    <option
      value="2"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png\" alt=\"Isabella Martinez\" />"}'
    >
      Isabella Martinez
    </option>
    <option
      value="3"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Ava Thompson\" />"}'
    >
      Ava Thompson
    </option>
  </select>
  <!-- End Select -->
</div>

<div class="mt-4 flex flex-wrap gap-2">
  <button type="button" id="set-to-2" class="btn btn-sm btn-primary">
    Set value to "Isabella Martinez"
  </button>
  <button type="button" id="set-to-3" class="btn btn-sm btn-primary">Set value to "Ava Thompson"</button>
</div>

<div class="mt-3 flex flex-wrap gap-2">
  <button type="button" id="reset-single-value" class="btn btn-sm btn-soft btn-secondary">Reset value</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () =>
    requestAnimationFrame(() => {
      const setTo2 = document.querySelector('#set-to-2')
      const setTo3 = document.querySelector('#set-to-3')
      const resetValue = document.querySelector('#reset-single-value')
      const setSelect = window.HSSelect.getInstance('#single-setter')

      setTo2.addEventListener('click', () => {
        setSelect.setValue('2')
      })

      setTo3.addEventListener('click', () => {
        setSelect.setValue('3')
      })

      resetValue.addEventListener('click', () => {
        setSelect.setValue('')
      })
    })
  )
</script>
{{< /code >}}

<!-- Set a multiple value with a setter. -->

{{< headname level="3" >}} Set a multiple value with a setter. {{< /headname >}}

Provides `setValue` <a href="#set-method" class="link link-primary">method</a> that helps to set a value programmatically.

{{< code jsCode="true" addClass="!block h-72" >}}

<div class="max-w-sm">
  <!-- Select -->
  <select
    id="multiple-setter"
    multiple=""
    data-select='{
      "placeholder": "Select multiple option with button",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex items-start\"> <div class=\"size-6 me-2\" data-icon></div> <div> <div class=\"text-base-content\" data-title></div><div></div>",
      "extraMarkup": "<span id=\"select-icon\" class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option
      value="1"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-5.png\" alt=\"Ethan Caldwell\" />"}'
    >
      Ethan Caldwell
    </option>
    <option
      value="2"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png\" alt=\"Isabella Martinez\" />"}'
    >
      Isabella Martinez
    </option>
    <option
      value="3"
      data-select-option='{ "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Ava Thompson\" />"}'
    >
      Ava Thompson
    </option>
  </select>
</div>

<div class="mt-4 flex flex-wrap gap-2">
  <button type="button" id="set-to-1-and-2" class="btn btn-sm btn-primary">
    Set value to "Isabella Martinez" and ""
  </button>
  <button type="button" id="set-to-2-and-3" class="btn btn-sm btn-primary">
    Set value to "Ava Thompson" and ""
  </button>
</div>
<div class="mt-3 flex flex-wrap gap-2">
  <button type="button" id="reset-multiple-value" class="btn btn-sm btn-soft btn-secondary">Reset value</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () =>
    requestAnimationFrame(() => {
      const setTo1and2 = document.querySelector('#set-to-1-and-2')
      const setTo2and3 = document.querySelector('#set-to-2-and-3')
      const resetValueMulti = document.querySelector('#reset-multiple-value')
      const setSelectMulti = window.HSSelect.getInstance('#multiple-setter')

      setTo1and2.addEventListener('click', () => {
        setSelectMulti.setValue(['1', '2'])
      })

      setTo2and3.addEventListener('click', () => {
        setSelectMulti.setValue(['2', '3'])
      })

      resetValueMulti.addEventListener('click', () => {
        setSelectMulti.setValue([])
      })
    })
  )
</script>
{{< /code >}}

<!-- Remote data selection -->

{{< headname level="3" >}} Remote data selection {{< /headname >}}

Set `apiUrl: "https://some-path.com/api"` to configure selection based on remote data, allowing data to be fetched dynamically from the specified API endpoint.

{{< code addClass="!block h-72" >}}
<div class="max-w-sm">
  <select
    data-select='{
      "apiUrl": "https://fakestoreapi.com/products",
      "apiQuery": "limit=10",
      "apiFieldsMap": {
        "id": "id",
        "val": "id",
        "title": "title",
        "icon": "image",
        "description": "description"
      },
      "apiIconTag": "<img />",
      "hasSearch": true,
      "searchPlaceholder": "Search...",
      "placeholder": "Select product...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu max-h-48 pt-0 overflow-y-auto",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex items-center gap-2\"><div class=\"size-8 overflow-hidden flex-none rounded-full\" data-icon></div><div><div class=\"text-sm font-semibold\" data-title></div><div class=\"text-xs \" data-description></div></div><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span id=\"select-icon\" class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden">
    <option value="">Choose</option>
  </select>
</div>
{{< /code >}}

<!-- Remote data selection (multiple options) -->

{{< headname level="3" >}} Remote data selection (multiple options) {{< /headname >}}

Allow multiple options to be selected by setting `apiUrl: "https://some-path.com/api"`, enabling dynamic selection from remote data provided by the specified API endpoint.

{{< code addClass="!block h-72" >}}
<div class="max-w-sm">
  <select
    multiple
    data-select='{
      "apiUrl": "https://fakestoreapi.com/products",
      "apiQuery": "limit=10",
      "apiFieldsMap": {
        "id": "id",
        "val": "id",
        "title": "title",
        "icon": "image",
        "description": "description"
      },
      "apiIconTag": "<img />",
      "placeholder": "Select product...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu max-h-48 pt-0 overflow-y-auto",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex items-center gap-2\"><div class=\"size-8 overflow-hidden flex-none rounded-full\" data-icon></div><div><div class=\"text-sm font-semibold\" data-title></div><div class=\"text-xs \" data-description></div></div><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span id=\"select-icon\" class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden">
    <option value="">Choose</option>
  </select>
</div>
{{< /code >}}

<!-- Remote data selection with removable tags -->

{{< headname level="3" >}} Remote data selection with removable tags {{< /headname >}}

Enable selection with removable tags using `apiUrl: "https://some-path.com/api"`, allowing choices to be dynamically loaded from remote data and displayed as tags.

{{< code addClass="!block h-72" >}}
<div class="max-w-sm">
  <select
    multiple
    data-select='{
      "apiUrl": "https://fakestoreapi.com/products",
      "apiQuery": "limit=10",
      "apiFieldsMap": {
        "id": "id",
        "val": "id",
        "title": "title",
        "icon": "image",
        "description": "description"
      },
      "apiIconTag": "<img />",
      "placeholder": "Select product...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "mode": "tags",
      "wrapperClasses": "advance-select-tag text-wrap flex-wrap",
      "tagsItemTemplate": " <div class=\"flex flex-nowrap items-center relative z-10 bg-base-100 border border-base-content/25 rounded-full p-1 m-1\"> <div class=\"size-6 overflow-hidden flex-none rounded-full me-1\" data-icon></div> <div class=\"truncate whitespace-break-spaces text-base-content\" data-title></div> <div class=\"btn btn-sm min-h-0 size-5 btn-circle btn-soft btn-secondary ms-2 \" data-remove><span class=\"icon-[tabler--x] shrink-0 size-3.5\"></span></div> </div>",
      "tagsInputClasses": "py-2.5 px-2 rounded-lg order-1 text-sm outline-none",
      "dropdownClasses": "advance-select-menu max-h-48 pt-0 overflow-y-auto",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex items-center gap-2\"><div class=\"size-8 overflow-hidden flex-none rounded-full\" data-icon></div><div><div class=\"text-sm font-semibold\" data-title></div><div class=\"text-xs \" data-description></div></div> <span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span id=\"select-icon\" class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden">
    <option value="">Choose</option>
  </select>
</div>
{{< /code >}}

<!-- Multiple selection with option template (remote data) -->

{{< headname level="3" >}} Multiple selection with option template (remote data) {{< /headname >}}

Enable multiple option selection with a custom template by setting `apiUrl: "https://some-path.com/api"`. This allows selections to be dynamically built from remote data with a specified option format.

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select
    multiple
    data-select='{
      "apiUrl": "https://fakestoreapi.com/products",
      "apiQuery": "limit=10",
      "apiFieldsMap": {
        "id": "id",
        "title": "title"
      },
      "apiIconTag": "<img />",
      "placeholder": "Select product...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "toggleCountText": "selected",
      "toggleCountTextMinItems": 2,
      "dropdownClasses": "advance-select-menu max-h-48 pt-0 overflow-y-auto",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span id=\"select-icon\" class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden">
  
    <option value="">Choose</option>
  </select>
</div>
{{< /code >}}

<!-- Multiple selection with conditional counter (remote data) -->

{{< headname level="3" >}} Multiple with conditional counter (remote data) {{< /headname >}}

Use `multiple` tag to enable counter option that counts the number of selected options. Use `apiUrl: "https://some-path.com/api"` to enable build select according to the remote data.

{{< code addClass="!block h-72" jsCode="true" >}}

<div class="max-w-sm">
  <select
    id="remote-multi-cond-count"
    multiple
    data-select='{
      "apiUrl": "https://fakestoreapi.com/products",
      "apiQuery": "limit=10",
      "apiFieldsMap": {
        "id": "id",
        "title": "title"
      },
      "apiIconTag": "<img />",
      "searchPlaceholder": "Search...",
      "placeholder": "Select product...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "toggleSeparators": {
        "betweenItemsAndCounter": "&"
      },
      "toggleCountText": "selected",
      "toggleCountTextMinItems": 2,
      "toggleCountTextMode": "nItemsAndCount",
      "dropdownClasses": "advance-select-menu max-h-48 pt-0 overflow-y-auto",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span id=\"select-icon\" class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden">
    <option value="">Choose</option>
  </select>
</div>
<!-- Clear Button -->
<div class="mt-4 flex flex-wrap gap-2">
  <button type="button" id="remote-clear-btn" class="btn btn-outline btn-primary btn-sm">Clear</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () =>
    requestAnimationFrame(() => {
      ;(function () {
        const clearBtn = document.querySelector('#remote-clear-btn')

        clearBtn.addEventListener('click', () => {
          const clearSelectBtn = HSSelect.getInstance('#remote-multi-cond-count', true)

          clearSelectBtn.element.setValue([])
        })
      })()
    })
  )
</script>

{{< /code >}}

<!-- Custom template with avatars (remote data) -->

{{< headname level="3" >}} Custom template with avatars (remote data) {{< /headname >}}

Create a custom selection design featuring avatars by setting `apiUrl: "https://some-path.com/api"`. This enables options to be dynamically loaded from remote data and displayed with personalized avatar styling..

{{< code addClass="!block h-72" >}}

<div class="max-w-sm">
  <select 
    data-select='{
      "apiUrl": "https://fakestoreapi.com/products",
      "apiQuery": "limit=10",
      "apiFieldsMap": {
        "id": "id",
        "val": "id",
        "title": "title",
        "icon": "image"
      },
      "apiIconTag": "<img />",
      "placeholder": "Select product...",
      "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
      "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
      "dropdownClasses": "advance-select-menu max-h-48 pt-0 overflow-y-auto",
      "optionClasses": "advance-select-option selected:select-active",
      "optionTemplate": "<div class=\"flex items-center gap-2\"><div class=\"size-8 overflow-hidden flex-none rounded-full\" data-icon></div><div class=\"text-sm font-semibold\" data-title></div><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
      "extraMarkup": "<span id=\"select-icon\" class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }' 
    class="hidden"
  >
    <option value="">Choose</option>
  </select>
</div>
{{< /code >}}

<!-- Modal example with overflow:hidden -->

{{< headname level="3" >}} Modal example with overflow:hidden {{< /headname >}}

{{< callout "warning" >}}
Please note that the demos below use the third-party library: <a href="https://floating-ui.com/" class="link link-warning" target="_blank">Floating UI</a>.
{{< /callout >}}

Use `dropdownScope: "window"` to display a select dropdown inside a parent element with hidden overflow, ensuring the dropdown remains visible and accessible within the window scope.

When `dropdownScope` is set to `window`, the `dropdownClasses` include `w-full` (required to update `updateDropdownWidth()`) and `z-80` (necessary to ensure the dropdown displays above the backdrop).

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overflow-animation-modal" data-overlay="#overflow-animation-modal" > Open modal </button>

<div id="overflow-animation-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1" aria-labelledby="overflow-animation-modal-label" >
  <div class="overlay-animation-target modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overflow-animation-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="space-y-3 overflow-y-auto p-4">
        <!-- Select -->
        <select
          data-select='{
            "placeholder": "Select option...",
            "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
            "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
            "dropdownClasses": "advance-select-menu z-80 w-full",
            "dropdownScope": "window",
            "optionClasses": "advance-select-option selected:select-active",
            "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
            "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
            }'
          class="hidden" >
          <option value="">Choose</option>
          <option value="name">Full Name</option>
          <option value="email">Email Address</option>
          <option value="description">Project Description</option>
          <option value="user_id">User Identification Number</option>
        </select>
        <!-- End Select -->
        <!-- Select -->
        <select
          multiple
          data-select='{
            "placeholder": "Select multiple options...",
            "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
            "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
            "dropdownClasses": "advance-select-menu z-80 w-full",
            "dropdownScope": "window",
            "optionClasses": "advance-select-option selected:select-active",
            "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
            "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
            }' class="hidden" >
          <option value="">Choose</option>
          <option value="name">Full Name</option>
          <option value="email">Email Address</option>
          <option value="description">Project Description</option>
          <option value="user_id">User Identification Number</option>
        </select>
        <!-- End Select -->
        <!-- Select -->
        <label class="hidden" for="tags-modal">Tags modal label</label>
        <select
          multiple
          data-select='{
            "placeholder": "Select option...",
            "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
            "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
            "dropdownClasses": "advance-select-menu w-full z-80 max-h-48 -ms-1 overflow-y-auto",
            "optionClasses": "advance-select-option selected:select-active",
            "mode": "tags",
            "dropdownScope": "window",
            "wrapperClasses": "advance-select-tag flex-wrap",
            "tagsItemTemplate": " <div class=\"flex flex-nowrap items-center relative z-10 bg-base-100 border border-base-content/25 rounded-full p-1 m-1\"> <div class=\"size-6 me-1\" data-icon></div> <div class=\"whitespace-nowrap text-base-content\" data-title></div> <div class=\"btn btn-sm min-h-0 size-5 btn-circle btn-soft btn-secondary ms-2 \" data-remove><span class=\"icon-[tabler--x] shrink-0 size-3.5\"></span></div> </div>",
            "tagsInputClasses": "py-2.5 px-2 rounded-lg order-1 text-sm outline-none",
            "optionTemplate": "<div class=\"flex items-center\"> <div class=\"size-8 me-2\" data-icon></div><div><div class=\"text-sm font-semibold text-base-content\" data-title></div> <div class=\"text-xs text-base-content/80\" data-description></div></div><div class=\"flex justify-between items-center flex-1\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div> </div>",
            "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
            }'
          class="hidden" aria-label="Advance select" id="tags-modal" >
          <option value="">Choose</option>
          <option
            selected=""
            value="1"
            data-select-option='{
              "description": "mark",
              "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png\" alt=\"Mark Gilbert\" />"}'
                  >
            Mark Gilbert
          </option>
          <option
            value="2"
            data-select-option='{
              "description": "eug",
              "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png\" alt=\"Eugenia Parsons\" />"}'>
            Eugenia Parsons
          </option>
          <option
            value="3"
            data-select-option='{
              "description": "francis",
              "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png\" alt=\"Francis Byrd\" />"}'>
            Francis Byrd
          </option>
          <option
            value="4"
            data-select-option='{
              "description": "rogers",
              "icon": "<img class=\"rounded-full\" src=\"https://cdn.flyonui.com/fy-assets/avatar/avatar-3.png\" alt=\"Jayden Rogers\" />"}'>
            Jayden Rogers
          </option>
        </select>
        <!-- End Select -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overflow-animation-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/advanced-select.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}


{{< table >}}
PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span colspan="4" class="text-base-content font-semibold" id="basic-options">Basic Options</span>
<span class="text-nowrap">`data-select`</span>| <span class="text-pretty">Used to create a custom select options.</span>|`-`|`-`
<span class="text-nowrap">`data-select-option`</span>| <span class="text-pretty">Used to add a custom option with a description and an icon.</span>|`-`|`-`
`:placeholder` | Define a default placeholder when nothing is selected. | string | `Select...`
`:toggleClasses` |Define CSS classes for the selects' toggle (styles the button). CSS classes must be separated by a space.|string| `-`
`:toggleTag` |Define the markup structure for the select toggle.<span class="font-medium">Note:</span> `data-title` is required if you are using a custom placeholder.| One line HTML markup| —
`:dropdownClasses` | Define CSS classes for the dropdown menu. CSS classes must be separated by a space.| string | `-`
`:dropdownPlacement` | Specifies the position of the menu when opened.| top, top-start, top-end, bottom, bottom-start, bottom-end, right, right-start, right-end, left, left-start, left-end | `bottom`
`:dropdownVerticalFixedPlacement` | Specifies a fixed vertical position for the menu when opened. It will not change when scrolling.| `"top"` / `"bottom"` / null |`null`
`:dropdownScope` | Determines whether the dropdown will be moved outside the parent, for correct display in elements with hidden overflow. Requires the `Popper` plugin. | window, parent| parent
`:optionClasses` | Styling is applied to individual options, so use Tailwind CSS classes to style the options. | string | `-`
`:optionTemplate` | Define template for the single option. It could contain:<ul> <li><code>data-icon</code> attribute: If the target <code>option</code> tag contains <code>data-select-option:icon</code>, the specified image will be placed within the tag with this attribute.</li> <li><code>data-title</code> attribute: The text from the target option will be inserted inside the tag with this attribute.</li> <li><code>data-description</code> attribute: If the target <code>option</code> tag contains <code>data-select-option:description</code>, the specified text will be placed inside the tag with this attribute.</li> </ul> | One line HTML markup | `-`
`:extraMarkup` |Provide markup that can be added to the select wrapper for decorative purposes. | One line HTML markup or Array of one line HTML markup | `-`
`:isOpened` | If the value is `true`, the select is opened. | boolean | `false`
`:dropdownSpace` | You have the ability to adjust the spacing between the select element and its menu. | number | `10`
`:optionTag` | Define the markup for the wrapper tag of a single option. </br> `Do not update`. This HTML markup must remain as is. Changing it could potentially cause issues.| One line HTML markup | `<div></div>`
`:descriptionClasses`| Specify CSS classes for the description within each individual option. Ensure that the classes are separated by a space. | string | `-`
`:iconClasses` | Specify CSS classes for the icons within each individual option. Ensure that the classes are separated by a space. | string | `-`
<span colspan="4" class="text-base-content font-semibold" id="multiple-options">Multiple Options</span>
`:toggleCountText` | This feature is exclusive to multiple select. It defines the text to appear after the counter and activates the counting mode.|string | `-`
`:toggleCountTextPlacement` | Allows to specify where the text specified in the `toggleCountText` parameter will be located relative to the counter.| `'postfix'` / `'prefix'` / `'postfix-no-space'` / `'prefix-no-space'` | `postfix`
`:toggleCountTextMinItems` | This feature is specific to multiple selects. It sets the minimum number of selected items required to activate the counting mode. | number | `1`
`:toggleSeparators`|Define separators for the toggle options in the selects.| object | `-`
`:toggleSeparators:items`| Define which separator will be used for separate selected items.|string`|`,`
`:toggleSeparators:betweenItemsAndCounter`|Define which separator will be used for separate selected items and counter text.|string |`and`
`:toggleCountTextMode`| This option is only available for multiple select. controls the display of the contents of the button title.| 'countAfterLimit' or 'nItemsAndCount'|`countAfterLimit`

<span colspan="4" class="text-base-content font-semibold" id="search-options">Search Options</span>
`:hasSearch` | If the value is `true`, include a search field within the dropdown.|boolean| `false`
`:preventSearchFocus` | If the value is true, disable autofocus for the search field within the dropdown list. | boolean | `false`
`:searchWrapperTemplate` | Define the markup for the wrapper tag for the search. </br> `Do not update`. This HTML markup must remain as is. Changing it could potentially cause issues. | One line HTML markup |`<div></div>`
`:searchWrapperClasses` | Provide the option to style the search wrapper using Tailwind classes. Make sure the classes are separated by spaces. |string | `bg-base-100 sticky top-0 mb-2 px-2 pt-3`
`:searchId` | This option is only available when `hasSearch: true`. This option is useful if there is a need to associate a `label` outside the initialized element with the search input. |string | `-`
`:searchClasses` | Apply Tailwind CSS classes to style the search bar. Ensure that the classes are separated by a space.| string | `border-base-content/40 focus:border-primary focus:outline-primary bg-base-100 block w-full rounded-field border px-3 py-2 text-base focus:outline-1`
`:searchPlaceholder` |This option is applicable only when the `:hasSearch` attribute is set to `true`. It specifies the placeholder text for the search field within the dropdown. | string | `Search...`
`:searchNoResultText` |Specifies the text to be shown when no results are found. | string | `No options found...`
`:searchNoResultClasses` | Specify CSS classes for the wrapper surrounding the "no results" message. Ensure that the classes are separated by a space. | string | `block advance-select-option` <br><hr class="my-2"> `advance-select-option` class is a custom class. Refer to the class table for more details.
`:optionAllowEmptyOption` | This option allows the inclusion of an empty option in the list. When enabled (`true`), an additional option with an empty string (`""`) as its value will be displayed, providing users the ability to select a blank choice if necessary. | boolean | `false`
`:searchLimit` | This option is only available when `hasSearch: true`. If this option is enabled, the search will display only the first 'n' matching items. | number | infinity
`:minSearchLength` | Sets the minimum number of characters required to activate the search functionality. | number | `0`
`:isSearchDirectMatch` | This option is only available when `hasSearch: true`. If the option is disabled, then in the search results you will be able to see non-direct matches by text. For example, if you entered `england` in the search field, then `Eng-land`, `Eng.land`, `Eng_land` will also be shown. | boolean | `true`
`:searchNoResultTemplate` | This option is only available when `:hasSearch` attribute is `true`. Define a markup for the "no result" text. | string | `<span></span>`
<span colspan="4" class="text-base-content font-semibold" id="tag-options">Tags Options</span>
`:mode` | Define a select mode. | default or tags | `default`
`:dropdownTag` | Specify the markup for the dropdown accordingly. </br> `Do not update`. This HTML markup must remain as is. Changing it could potentially cause issues. | One line HTML markup | `<div></div>`
`:wrapperClasses` | Define CSS classes for the wrapper of the select elements. These classes are applied to the main wrapper. Ensure that the classes are separated by spaces. |string | `-`
`:tagsItemTemplate` | Define template for the single option. It could contain:<ul> <li><code>data-icon</code> attribute: If the target <code>option</code> tag contains <code>data-select-option:icon</code>, the specified image will be placed within the tag with this attribute.</li> <li><code>data-title</code> attribute: The text from the target option will be inserted inside the tag with this attribute.</li> <li><code>data-description</code> attribute: If the target <code>option</code> tag contains <code>data-select-option:description</code>, the specified text will be placed inside the tag with this attribute.</li> </ul> | One line HTML markup | `-`
`:tagsItemClasses` | Apply styling to the select tag wrapper. Ensure that the classes are separated by spaces. |string | `-`
`:tagsInputId` | This option is only available when tags mode is set up. This option is useful if there is a need to associate a `label` outside the initialized element with the tags input. |string | `-`
`:tagsInputClasses` | This work as input for search. Specify CSS classes for the input field within the dropdown list. Ensure that the classes are separated by spaces. | string | `-`
`:isAddTagOnEnter` | When you search and press Enter, it creates an entry within the options. This setting determines whether a tag will be added when the Enter key is pressed. | boolean | `true`
<span colspan="4" class="text-base-content font-semibold" id="tag-options">Remote Data Options</span>
`:apiUrl` | Defines the address where the API is located. | string, null | null
`:apiQuery` | Defines query parameters that are separated by `?`. | string, null | null
`:apiOptions` | Defines options for the fetch function. | RequestInit , null | null
`:apiDataPart` | If data is in some first level parameter, then it allows you to specify the name of this parameter to extract the data. | string , null | null
`:apiSearchQueryKey` | Defines the key for the query search parameter. | string , null | null
`:apiFieldsMap` | Allows you to convert fields from the API to the fields required for the plugin to work. | `{ id: string; title: string; icon?: string, null; description?: string, null}` , null | null
`:apiIconTag` | Allows to define an `img` tag that will be used when rendering options and in the trigger button. | string , null | null
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSSelect` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`destroy()` | Destroys select.
`open()` | Open dropdown list.
`close()` | Close dropdown list.
`setValue()`| Set the select value: use a string for a single select and an array for a multiple select.
`addOption(items)` | Include an option, or potentially multiple options, to the select menu. Each individual option should adhere to this interface. <br> `{ title: string; val: string; options?: { description: string; icon: string; }; }`
`removeOption(val)` | Remove an option by its value (multiple options possible).
`recalculateDirection()`| Trigger a recalculation for the dropdown list.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSSelect.getInstance(target, isInstance)` | <div>Returns the element linked to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
`HSSelect.close(target)`. | <div>Close the element linked to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li></ul></div>
`HSSelect.closeCurrentlyOpened(evtTarget)` | <div>Close the element linked to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node.</li></ul></div>
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

Below is a demonstration of how to use the methods. Assign an ID to the `data-select` element. To test other methods, copy the following code into your console and click the button.

{{< code addClass="!block h-80" jsCode="true" >}}

<button class="btn btn-primary mb-4" id="open-btn">Open</button>

<div class="max-w-sm">
  <select
    id="method-select"
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu max-h-44 overflow-y-auto",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="--prevent-on-load-init hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () =>
    requestAnimationFrame(() => {
      const select = new HSSelect(document.querySelector('#method-select'))
      const openBtn = document.querySelector('#open-btn')

      //Method usage
      openBtn.addEventListener('click', () => {
        select.open()
      })
    })
  )
</script>

{{< /code >}}

<p class="mb-1.5 not-prose">Open item (public method).</p>

{{< callout "info" >}}
<strong>Note(only for public method)</strong>: To prevent initialization, add the <code class="text-sm">--prevent-on-load-init</code> class to the select element before initializing it with <code class="text-sm">new</code>.
{{< /callout >}}
{{< code-highlight lang="html" >}}
<select id="select" class="--prevent-on-load-init" data-select>
...
</select>
{{< /code-highlight >}}

{{< code-highlight lang="js" >}}// This method is used in above example.
const select = new HSSelect(document.querySelector('#method-select'));
const openBtn = document.querySelector('#open-btn');

openBtn.addEventListener('click', () => {
  select.open();
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose">Open item (static method).</p>

{{< code-highlight lang="js" >}}const openBtn = document.querySelector('#open-btn');

openBtn.addEventListener('click', () => {
  HSSelect.open('#select');
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose">Open item (mixed).</p>

{{< code-highlight lang="js" >}}
const { element } = HSSelect.getInstance('#method-select', true);
const openBtn = document.querySelector('#open-btn');

openBtn.addEventListener('click', () => {
  element.open();
});
{{< /code-highlight >}}

<!-- Set value. -->

{{< headname level="4" >}} Set value method {{< /headname >}}

<p class="mb-1.5 not-prose" id="set-method">Set value.</p>

{{< code-highlight lang="js" >}}const select = HSSelect.getInstance('#select');
const setValueBtn = document.querySelector('#set-value-btn');

setValueBtn.addEventListener('click', () => {
  select.setValue('address');
  // if select is multiple
  // select.setValue(['address', 'email']);
});
{{< /code-highlight >}}

<!-- Add option -->

{{< headname level="4" >}} Add & Remove options {{< /headname >}}

<p class="mb-1.5 not-prose" id="add-method">Add options (public method).</p>

{{< code-highlight lang="js" >}}const select = window.HSSelect.getInstance('#add-remove-select');
const addOptionsBtn = document.querySelector('#add-option');

addOptionsBtn.addEventListener('click', () => {
  select.addOption([
    {
      title: "James Collins",
      val: "1",
    },
    {
      title: "Amanda Harvey",
      val: "2",
    }
  ]);
});
{{< /code-highlight >}}

<!-- Remove options -->

<p class="mb-1.5 not-prose" id="remove-method">Remove options (public method).</p>

{{< code-highlight lang="js" >}}const select = window.HSSelect.getInstance('#add-remove-select');
const removeOptionsBtn = document.querySelector('#remove-option');
removeOptionsBtn.addEventListener('click', () => {
  select.removeOption(["1", "2"]);
});
{{< /code-highlight >}}

<!-- Destroy instance -->

{{< headname level="4" >}} Destroy instance {{< /headname >}}

<p class="mb-1.5 not-prose" id="destroy-method">Destroy instance (public method).</p>

{{< code-highlight lang="js" >}}const destroyBtn = document.querySelector('#destroy-btn');
const select = window.HSSelect.getInstance('#destroy-select');
destroyBtn.addEventListener('click', () => {
  select.destroy();
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION | RETURNING VALUE
`on:change`| Called when any select is changed. | Current value
{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

Display a console log message when an option is selected.

{{< code addClass="!block h-72" jsCode="true" >}}

<div class="max-w-sm">
  <select
    id="event-select"
    data-select='{
    "placeholder": "Select option...",
    "toggleTag": "<button type=\"button\" aria-expanded=\"false\"></button>",
    "toggleClasses": "advance-select-toggle select-disabled:pointer-events-none select-disabled:opacity-40",
    "dropdownClasses": "advance-select-menu",
    "optionClasses": "advance-select-option selected:select-active",
    "optionTemplate": "<div class=\"flex justify-between items-center w-full\"><span data-title></span><span class=\"icon-[tabler--check] shrink-0 size-4 text-primary hidden selected:block \"></span></div>",
    "extraMarkup": "<span class=\"icon-[tabler--caret-up-down] shrink-0 size-4 text-base-content absolute top-1/2 end-3 -translate-y-1/2 \"></span>"
    }'
    class="hidden"
  >
    <option value="">Choose</option>
    <option value="name">Full Name</option>
    <option value="email">Email Address</option>
    <option value="description">Project Description</option>
    <option value="user_id">User Identification Number</option>
  </select>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () =>
    requestAnimationFrame(() => {
      const el = HSSelect.getInstance('#event-select')
      //Event usage
      el.on('change', instance => {
        console.log('selected')
      })
    })
  )
</script>

{{< /code >}}

<p class="mt-12 mb-1.5 not-prose">When select changes event example.</p>

{{< code-highlight lang="js" >}}const el = HSSelect.getInstance(document.getElementById('event-select'));

el.on('change', (instance) => {console.log("selected")});
{{< /code-highlight >}}
