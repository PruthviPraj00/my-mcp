---
title: "Combo Box"
components: 3
description: "The ComboBox JavaScript plugin improves user experience by dynamically suggesting options as users type into an input field."
bg_image: "svg/form-elements/combo-box.svg"
menu:
  main:
    parent: "advanced forms"

previous: Advanced Select
previousLink: advanced-forms/advanced-select/

next: Copy Markup
nextLink: advanced-forms/copy-markup/

requires_js: true
pageJS:
  - "/js/pages/combo-box.js"
---

{{< callout "info" >}}
Combo Box components are adopted from <a href="https://preline.co/docs/combobox.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}


<!-- Class Table -->

{{< class-table >}}
dropdown-item| modifier | Styles applied to individual dropdown items.
combo-box-active:{tw-utility-class}|variant|Modifies tailwind classes when the combo box is active.
combo-box-selected:{tw-utility-class}|variant|Modifies tailwind classes when the combo box is selected.
combo-box-tab-active:{tw-utility-class}|variant|Modifies tailwind classes when the combo box tab is active.
combo-box-has-value:{tw-utility-class} |variant |A modifier that enables you to apply Tailwind classes when the SearchBox's input field contains a value.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- HTML example -->

{{< headname level="3" >}} HTML example {{< /headname >}}

The code snippet outlines a ComboBox with specific `data` attributes to manage its behavior. The outer `<div>` with `data-combo-box` signifies that this section is the main ComboBox component. Within it, an `<input>` field with `data-combo-box-input` allows users to type text to get suggestions.

An accompanying `icon` element with `data-combo-box-toggle` acts as a button to open or close the dropdown menu, indicating it has a dropdown function. The dropdown menu itself is an `<div>` with `data-combo-box-output`, which contains several suggestion items. These individual suggestion items are `<div>` elements with `data-combo-box-output-item`. Each item has a `data-combo-box-search-text` attribute that holds the text displayed for that option in the dropdown.

Below example shows basic use of combo-box.

{{< code addClass="!block h-64" >}}

<div class="relative max-w-sm" data-combo-box="">
  <div class="relative">
    <input class="input" type="text" value="India" role="combobox" aria-expanded="false" data-combo-box-input="" aria-label="Default combobox" />
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" >
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="0" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Venezuela" data-combo-box-value="">Venezuela</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="1" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Papua New Guinea" data-combo-box-value="">Papua New Guinea</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="2" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="South Africa " data-combo-box-value="">South Africa</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="3" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Honduras" data-combo-box-value="">Honduras</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="4" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="India" data-combo-box-value="">India</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="5" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="El Salvador" data-combo-box-value="">El Salvador</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- JSON example -->

{{< headname level="3" >}} JSON example {{< /headname >}}

A JSON-based ComboBox example.

A ComboBox, a dropdown component allowing users to type for suggestions, is being set up. The root `div` includes an attribute `apiUrl`, indicating the ComboBox where to retrieve data.

In this instance, it’s set to `https://www.freetestapi.com/api/v1/countries`, used to obtain a list of countries.

Another attribute, `outputItemTemplate`, defines the layout for each item within the dropdown menu. It comprises HTML structure incorporating `data-combo-box-output-item` to represent individual dropdown items. Each item includes a section for the name (utilizing `data-combo-box-output-item-field="name"`) and a span for a checkmark icon, visible upon item selection.

{{< code addClass="!block h-64" >}}

<div class="relative max-w-sm"
  data-combo-box='{
    "apiUrl": "https://www.freetestapi.com/api/v1/countries",
    "outputItemTemplate": "<div class=\"dropdown-item combo-box-selected:dropdown-active\" data-combo-box-output-item><div class=\"flex justify-between items-center w-full\"><div data-combo-box-output-item-field=\"name\" data-combo-box-search-text data-combo-box-value></div><span class=\"icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0\"></span></div></div>"
  }' >
  <div class="relative">
    <input class="input" type="text" value="India" role="combobox" aria-expanded="false" data-combo-box-input="" aria-label="Json-based combobox" />
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" ></div>
</div>
{{< /code >}}

<!-- JSON Example (based on API pathes) -->

{{< headname level="3" >}} JSON Example (based on API pathes) {{< /headname >}}

A JSON-configured ComboBox that retrieves options from an API. `apiSearchPath` specifies the API endpoint for searching items. `apiSearchDefaultPath` sets the default API endpoint to load all items initially.
{{< code addClass="!block h-64" >}}

<div class="relative max-w-sm"
  data-combo-box='{
    "apiUrl": "https://restcountries.com/v3.1",
    "apiSearchPath": "name",
    "apiSearchDefaultPath": "all",
    "outputItemTemplate": "<div class=\"dropdown-item combo-box-selected:dropdown-active\" data-combo-box-output-item><div class=\"flex justify-between items-center w-full\"><div><div class=\"hidden\" data-combo-box-output-item-field=\"ccn3\"></div><div data-combo-box-output-item-field=\"name.common\" data-combo-box-search-text data-combo-box-value></div></div><span class=\"icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0\"></span></div></div>"
  }' >
  <div class="relative">
    <input class="input" type="text" value="India" role="combobox" aria-expanded="false" data-combo-box-input="" aria-label="based on API pathes combobox" />
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" ></div>
</div>
{{< /code >}}

<!-------------------- Option usage -------------------->

{{< headname level="2" >}} Option usage {{< /headname >}}

<!-- Search and limit parameters -->

{{< headname level="3" >}} Search and limit parameters {{< /headname >}}

`:apiSearchQuery` serves as a property or parameter containing the key name utilized for searching within a dataset when making API calls. Usually, it's combined with user-entered text to generate a query string, which is then appended to the base API endpoint (`apiUrl`), resulting in the complete URL required to fetch the data.

`:apiQuery` represents additional query parameters for the API request, such as `limit`. `:outputEmptyTemplate` enables you to specify the content to display when no matching options are available.

The following example demonstrates the usage of search and limit parameters in a combo box.

{{< code addClass="!block h-64" >}}

<div class="relative max-w-sm"
  data-combo-box='{
  "apiUrl": "https://www.freetestapi.com/api/v1/countries",
  "apiQuery": "limit=7",
  "apiSearchQuery": "search",
  "outputEmptyTemplate": "<div class=\"dropdown-item\">No countries found...</div>",
  "outputItemTemplate": "<div class=\"dropdown-item combo-box-selected:dropdown-active\" data-combo-box-output-item><div class=\"flex justify-between items-center w-full\"><div data-combo-box-output-item-field=\"name\" data-combo-box-search-text data-combo-box-value></div><span class=\"icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0\"></span></div></div>"
}' >
  <div class="relative">
    <input class="input" type="text" value="India" role="combobox" aria-expanded="false" data-combo-box-input="" aria-label="Parameters in combobox" />
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none;" data-combo-box-output="" ></div>
</div>
{{< /code >}}

<!-- Minimum search Length -->

{{< headname level="3" >}} Minimum search Length {{< /headname >}}

Set `"minSearchLength": 2` to define the minimum number of characters required before initiating a search.

{{< code addClass="!block h-64" >}}

<div class="relative max-w-sm"
  data-combo-box='{
  "apiUrl": "https://www.freetestapi.com/api/v1/countries",
  "apiQuery": "limit=15",
  "minSearchLength": 2,
  "apiSearchQuery": "search",
  "outputEmptyTemplate": "<div class=\"dropdown-item\">No countries found...</div>",
  "outputItemTemplate": "<div class=\"dropdown-item combo-box-selected:dropdown-active\" data-combo-box-output-item><div class=\"flex justify-between items-center w-full\"><div data-combo-box-output-item-field=\"name\" data-combo-box-search-text data-combo-box-value></div><span class=\"icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0\"></span></div></div>"
}' >
  <div class="relative">
    <input class="input" type="text" value="India" role="combobox" aria-expanded="false" data-combo-box-input="" aria-label="Parameters in combobox" />
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none;" data-combo-box-output="" ></div>
</div>
{{< /code >}}

<!-- Open on focus -->

{{< headname level="3" >}} Open on focus {{< /headname >}}

When `isOpenOnFocus` is enabled, the dropdown menu will automatically appear upon focusing on the input field.

Alternatively, users have the option to utilize the `data-combo-box-toggle` attribute, designating an element within the ComboBox responsible for toggling the visibility of the dropdown list.

{{< code addClass="!block h-64" >}}

<div class="relative max-w-sm"
  data-combo-box='{
  "apiUrl": "https://www.freetestapi.com/api/v1/countries",
  "isOpenOnFocus": true,
  "outputEmptyTemplate": "<div class=\"dropdown-item\">No countries found...</div>",
  "outputItemTemplate": "<div class=\"dropdown-item combo-box-selected:dropdown-active\" data-combo-box-output-item> <div class=\"flex justify-between items-center w-full\"> <div data-combo-box-output-item-field=\"name\" data-combo-box-search-text data-combo-box-value></div><span class=\"icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0\"></span></div></div>" 
  }' >
  <div class="relative">
    <input class="input" type="text" value="India" role="combobox" aria-expanded="false" data-combo-box-input="" aria-label="open on focus combobox" />
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" ></div>
</div>
{{< /code >}}

<!-- Close Button -->

{{< headname level="3" >}} Close Button {{< /headname >}}

A basic usage of ComboBox with close button.

{{< code addClass="!block h-64" >}}

<div class="relative max-w-sm" data-combo-box="">
  <div class="relative">
    <input class="input" type="text" role="combobox" aria-expanded="false" value="" data-combo-box-input="" aria-label="Combobox with close button" />
    <div class="combo-box-active:flex absolute inset-y-0 end-8 hidden items-center">
      <button type="button" class="btn btn-sm btn-circle btn-text btn-primary" aria-label="Close" data-combo-box-close="" >
        <span class="sr-only">Close</span>
        <span class="icon-[tabler--xbox-x] size-4 shrink-0"></span>
      </button>
    </div>
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" >
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="0" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Venezuela" data-combo-box-value="">Venezuela</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="1" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Papua New Guinea" data-combo-box-value="">Papua New Guinea</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="2" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="South Africa " data-combo-box-value="">South Africa</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="3" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Honduras" data-combo-box-value="">Honduras</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="4" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="India" data-combo-box-value="">India</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="5" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="El Salvador" data-combo-box-value="">El Salvador</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- SearchBox -------------------->

{{< headname level="2" >}} SearchBox {{< /headname >}}

<!-- Html example -->

{{< headname level="3" >}} Html example {{< /headname >}}

Combo box html example with dropdown and modal.

<!-- Dropdown -->

{{< headname level="4" >}} Dropdown {{< /headname >}}

Below is an example showcasing the utilization of the SearchBox within a dropdown, employing data attributes in HTML. Furthermore, the example illustrates how to create groups.

{{< code addClass="!block" >}}

<div class="max-w-sm">
  <div class="relative"
    data-combo-box='{
      "groupingType": "default",
      "preventSelection": true,
      "isOpenOnFocus": true,
      "groupingTitleTemplate": "<div class=\"block text-xs text-base-content/50 m-3 mb-1\"></div>"
    }' >
    <div class="relative">
      <input class="input ps-8" type="text" placeholder="Search for an action" role="combobox" aria-expanded="false" value="" data-combo-box-input="" />
      <span class="icon-[tabler--search] text-base-content absolute start-3 top-1/2 size-4 shrink-0 -translate-y-1/2" ></span>
    </div>
    <div class="bg-base-100 rounded-box p-2 shadow-base-300/20 shadow-lg" style="display: none" data-combo-box-output="" >
      <div data-combo-box-output-items-wrapper="" class="space-y-0.5">
        <!-- Group: Recent Actions -->
        <div data-combo-box-output-item='{"group": {"name": "recent", "title": "Recent Actions"}}' tabindex="0">
          <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
            <span class="icon-[tabler--writing] text-base-content/80 size-5 shrink-0"></span>
            <span class="text-base-content" data-combo-box-search-text="Write a document" data-combo-box-value="" >
              Write a document
            </span>
            <span class="text-base-content/50 ms-auto hidden text-xs sm:inline" data-combo-box-search-text="Google Docs" data-combo-box-value="" >
              Google Docs
            </span>
          </a>
        </div>
        <div data-combo-box-output-item='{"group": {"name": "recent", "title": "Recent Actions"}}' tabindex="1">
          <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
            <span class="icon-[tabler--calendar] text-base-content/80 size-5 shrink-0"></span>
            <span class="text-base-content" data-combo-box-search-text="Schedule a meeting" data-combo-box-value="" >
              Schedule a meeting
            </span>
            <span class="text-base-content/50 ms-auto hidden text-xs sm:inline" data-combo-box-search-text="Google Calendar" data-combo-box-value="" >
              Google Calendar
            </span>
          </a>
        </div>
        <div data-combo-box-output-item='{"group": {"name": "recent", "title": "Recent Actions"}}' tabindex="2">
          <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
            <span class="icon-[tabler--presentation] text-base-content/80 size-5 shrink-0"></span>
            <span class="text-base-content" data-combo-box-search-text="Create a presentation" data-combo-box-value="" >
              Create a presentation
            </span>
            <span class="text-base-content/50 ms-auto hidden text-xs sm:inline" data-combo-box-search-text="Microsoft PowerPoint" data-combo-box-value="" >
              PowerPoint
            </span>
          </a>
        </div>
        <!-- Group: People -->
        <div data-combo-box-output-item='{"group": {"name": "people", "title": "People"}}' tabindex="4">
          <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
            <img class="size-6 shrink-0 rounded-full" src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="Image Description" />
            <span class="text-base-content" data-combo-box-search-text="Alice Johnson" data-combo-box-value="" >
              Alice Johnson
            </span>
            <span class="ms-auto text-xs text-teal-600" data-combo-box-search-text="Online" data-combo-box-value="">
              Online
            </span>
          </a>
        </div>
        <div data-combo-box-output-item='{"group": {"name": "people", "title": "People"}}' tabindex="5">
          <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
            <img class="size-6 shrink-0 rounded-full" src="https://cdn.flyonui.com/fy-assets/avatar/avatar-11.png" alt="Image Description" />
            <span class="text-base-content" data-combo-box-search-text="David Kim" data-combo-box-value="">
              David Kim
            </span>
            <span class="text-base-content/50 ms-auto text-xs" data-combo-box-search-text="Offline" data-combo-box-value="" >
              Offline
            </span>
          </a>
        </div>
        <div data-combo-box-output-item='{"group": {"name": "people", "title": "People"}}' tabindex="6">
          <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
            <img class="size-6 shrink-0 rounded-full" src="https://cdn.flyonui.com/fy-assets/avatar/avatar-12.png" alt="Image Description" />
            <span class="text-base-content" data-combo-box-search-text="Rosa Martinez" data-combo-box-value="" >
              Rosa Martinez
            </span>
            <span class="text-base-content/50 ms-auto text-xs" data-combo-box-search-text="Offline" data-combo-box-value="" >
              Offline
            </span>
          </a>
        </div>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Modal -->

{{< headname level="4" >}} Modal {{< /headname >}}

A combo box displaying HTML content within a modal.

{{< code addClass="!block" jsCode="true" >}}

<h5 class="text-base-content text-base"> Press <kbd class="kbd kbd-sm">Shift</kbd> + <kbd class="kbd kbd-sm">:</kbd> for SearchBox. </h5>

<!-- SearchBox Trigger -->

<button type="button" class="hidden" aria-haspopup="dialog" aria-expanded="false" aria-controls="html-modal-combo-box" data-overlay="#html-modal-combo-box" ></button>

<div id="html-modal-combo-box" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="relative"
        data-combo-box='{
          "preventVisibility": true,
          "groupingType": "default",
          "preventSelection": true,
          "isOpenOnFocus": true,
          "groupingTitleTemplate": "<div class=\"block text-xs text-base-content/50 m-3 mb-1\"></div>"
        }' >
        <div class="modal-header block">
          <div class="relative">
            <input class="input ps-8" type="text" placeholder="Search or type a command" role="combobox" aria-expanded="false" value="" autofocus="" data-combo-box-input="" />
            <span class="icon-[tabler--search] text-base-content absolute start-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
          </div>
        </div>
        <!-- SearchBox Modal Body -->
        <div class="modal-body overflow-y-auto mt-0 max-h-72 p-1.5" data-combo-box-output="">
          <div class="space-y-0.5 p-0.5" data-combo-box-output-items-wrapper="">
            <!-- Group: Recent Actions -->
            <div data-combo-box-output-item='{"group": {"name": "recent", "title": "Recent Actions"}}' tabindex="0">
              <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
                <span class="icon-[tabler--writing] text-base-content/80 size-4 shrink-0"></span>
                <span class="text-base-content text-sm" data-combo-box-search-text="Write a document" data-combo-box-value="" >
                  Write a document
                </span>
                <span class="text-base-content/50 ms-auto hidden text-xs sm:inline" data-combo-box-search-text="Google Docs" data-combo-box-value="" >
                  Google Docs
                </span>
              </a>
            </div>
            <div data-combo-box-output-item='{"group": {"name": "recent", "title": "Recent Actions"}}' tabindex="1">
              <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
                <span class="icon-[tabler--calendar] text-base-content/80 size-4 shrink-0"></span>
                <span class="text-base-content text-sm" data-combo-box-search-text="Schedule a meeting" data-combo-box-value="" >
                  Schedule a meeting
                </span>
                <span class="text-base-content/50 ms-auto hidden text-xs sm:inline" data-combo-box-search-text="Google Calendar" data-combo-box-value="" >
                  Google Calendar
                </span>
              </a>
            </div>
            <div data-combo-box-output-item='{"group": {"name": "recent", "title": "Recent Actions"}}' tabindex="2">
              <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
                <span class="icon-[tabler--presentation] text-base-content/80 size-4 shrink-0"></span>
                <span class="text-base-content text-sm" data-combo-box-search-text="Create a presentation" data-combo-box-value="" >
                  Create a presentation
                </span>
                <span class="text-base-content/50 ms-auto hidden text-xs sm:inline" data-combo-box-search-text="Microsoft PowerPoint" data-combo-box-value="" >
                  PowerPoint
                </span>
              </a>
            </div>
            <!-- Group: People -->
            <div data-combo-box-output-item='{"group": {"name": "people", "title": "People"}}' tabindex="4">
              <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
                <img class="size-5 shrink-0 rounded-full" src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="Image Description" />
                <span class="text-base-content text-sm" data-combo-box-search-text="Alice Johnson" data-combo-box-value="" >
                  Alice Johnson
                </span>
                <span class="ms-auto text-xs text-teal-600" data-combo-box-search-text="Online" data-combo-box-value="">
                  Online
                </span>
              </a>
            </div>
            <div data-combo-box-output-item='{"group": {"name": "people", "title": "People"}}' tabindex="5">
              <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
                <img class="size-5 shrink-0 rounded-full" src="https://cdn.flyonui.com/fy-assets/avatar/avatar-11.png" alt="Image Description" />
                <span class="text-base-content text-sm" data-combo-box-search-text="David Kim" data-combo-box-value="" >
                  David Kim
                </span>
                <span class="text-base-content/50 ms-auto text-xs" data-combo-box-search-text="Offline" data-combo-box-value="" >
                  Offline
                </span>
              </a>
            </div>
            <div data-combo-box-output-item='{"group": {"name": "people", "title": "People"}}' tabindex="6">
              <a class="dropdown-item combo-box-selected:dropdown-active" href="#">
                <img class="size-5 shrink-0 rounded-full" src="https://cdn.flyonui.com/fy-assets/avatar/avatar-12.png" alt="Image Description" />
                <span class="text-base-content text-sm" data-combo-box-search-text="Rosa Martinez" data-combo-box-value="" >
                  Rosa Martinez
                </span>
                <span class="text-base-content/50 ms-auto text-xs" data-combo-box-search-text="Offline" data-combo-box-value="" >
                  Offline
                </span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    //HTML modal combo box
    const htmlOverlay = HSOverlay.getInstance('#html-modal-combo-box', true)
    const htmlCombobox = HSComboBox.getInstance('#html-modal-combo-box [data-combo-box]', true)

    window.addEventListener('keydown', function (evt) {
      if (evt.code === 'Semicolon' && evt.shiftKey) {
        if (htmlOverlay.element && htmlOverlay.element.el.classList.contains('open')) return false

        htmlOverlay.element.open()
        htmlCombobox.element.setCurrent()
      }
    })
  })
</script>
{{< /code >}}

<!-- Json example -->

{{< headname level="3" >}} Json example {{< /headname >}}

Combo box example using JSON data displayed within a dropdown and a modal.

<!-- Dropdown -->

{{< headname level="4" >}} Dropdown {{< /headname >}}

Utilizing a JSON example in a dropdown, use option `:apiGroupField` to select a heading. Positions are categorized as headings in this scenario.

{{< code addClass="!block h-80" >}}

<div class="max-w-sm">
  <div class="relative"
    data-combo-box='{
    "groupingType": "default",
    "isOpenOnFocus": true,
    "apiUrl": "/json/searchbox.json",
    "apiGroupField": "position",
    "outputItemTemplate": "<div class=\"dropdown-item combo-box-selected:dropdown-active\" data-combo-box-output-item> <div class=\"flex items-center justify-between\"> <div class=\"flex items-center w-full\"> <div class=\"flex items-center justify-center rounded-full bg-base-200 size-6 overflow-hidden me-2.5\"> <img class=\"shrink-0\" data-combo-box-output-item-attr=&apos;[{\"valueFrom\": \"image\", \"attr\": \"src\"}, {\"valueFrom\": \"name\", \"attr\": \"alt\"}]&apos; /> </div> <div data-combo-box-output-item-field=\"name\" data-combo-box-search-text data-combo-box-value></div> </div> <span class=\"icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0\"> </span> </div> </div>","groupingTitleTemplate": "<div class=\"block text-xs text-base-content/50 m-3 mb-1\"></div>"
  }' >
    <!-- SearchBox -->
    <div class="relative">
      <input class="input ps-8" type="text" placeholder="Search or type a command" role="combobox" aria-expanded="false" value="" autofocus="" data-combo-box-input="" />
      <span class="icon-[tabler--search] text-base-content absolute start-3 top-1/2 size-4 shrink-0 -translate-y-1/2" ></span>
    </div>
    <!-- SearchBox Body -->
    <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-56 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" ></div>
  </div>
</div>
{{< /code >}}

<!-- Modal -->

{{< headname level="4" >}} Modal {{< /headname >}}

Combo box with json data show in modal.

{{< code jsCode="true" >}}

<h5 class="text-base-content text-base"> Press <kbd class="kbd kbd-sm">Shift</kbd> + <kbd class="kbd kbd-sm">t</kbd> for SearchBox. </h5>

<!-- SearchBox Trigger -->

<button type="button" class="hidden" aria-haspopup="dialog" aria-expanded="false" aria-controls="json-modal-combo-box" data-overlay="#json-modal-combo-box" ></button>

<!-- SearchBox Modal -->
<div id="json-modal-combo-box" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="relative"
        data-combo-box='{
        "preventVisibility": true,
        "groupingType": "default",
        "apiUrl": "/json/searchbox.json",
        "apiGroupField": "position",
        "outputItemTemplate": "<div class=\"dropdown-item combo-box-selected:dropdown-active\" data-combo-box-output-item> <div class=\"flex items-center justify-between\"> <div class=\"flex items-center w-full\"> <div class=\"flex items-center justify-center rounded-full bg-base-200 size-6 overflow-hidden me-2.5\"> <img class=\"shrink-0\" data-combo-box-output-item-attr=&apos;[{\"valueFrom\": \"image\", \"attr\": \"src\"}, {\"valueFrom\": \"name\", \"attr\": \"alt\"}]&apos; /> </div> <div data-combo-box-output-item-field=\"name\" data-combo-box-search-text data-combo-box-value></div> </div> <span class=\"icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0\"> </span> </div> </div>",
        "groupingTitleTemplate": "<div class=\"block text-xs text-base-content/50 m-3 mb-1\"></div>"
      }' >
        <!-- SearchBox -->
        <div class="modal-header block">
          <div class="relative">
            <input class="input ps-8" type="text" placeholder="Search or type a command" role="combobox" aria-expanded="false" value="" autofocus="" data-combo-box-input="" />
            <span class="icon-[tabler--search] text-base-content absolute start-3 top-1/2 size-4 shrink-0 -translate-y-1/2" ></span>
          </div>
        </div>
        <!-- SearchBox Modal Body -->
        <div class="modal-body" data-combo-box-output="">
          <div class="overflow-y-auto max-h-72 space-y-0.5" data-combo-box-output-items-wrapper="" ></div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    //Json modal combo box
    const jsonOverlay = HSOverlay.getInstance('#json-modal-combo-box', true)
    const jsonCombobox = HSComboBox.getInstance('#json-modal-combo-box [data-combo-box]', true)

    window.addEventListener('keydown', function (evt) {
      if (evt.code === 'KeyT' && evt.shiftKey) {
        if (jsonOverlay.element && jsonOverlay.element.el.classList.contains('open')) return false

        jsonOverlay.element.open()
        jsonCombobox.element.setCurrent()
      }
    })
  })
</script>
{{< /code>}}

<!-- Json with tab filter -->

{{< headname level="3" >}} Json with tab filter {{< /headname >}}

Combo box example demonstrating tab filtering functionality, incorporating both dropdown and modal components.

<!-- Dropdown -->

{{< headname level="4" >}} Dropdown {{< /headname >}}

Experience tab filtering within a dropdown. Set `:groupingType` to `tabs`, utilize `:groupingTitleTemplate` to style the filtering tabs, and `:tabsWrapperTemplate` to style the tab wrapper.

{{< code addClass="!block h-80" >}}

<div class="max-w-sm">
  <div
    class="relative"
    data-combo-box='{
      "groupingType": "tabs",
      "isOpenOnFocus": true,
      "apiUrl": "https://fakestoreapi.com/products",
      "apiGroupField": "category",
      "outputItemTemplate": "<div class=\"dropdown-item combo-box-selected:dropdown-active\" data-combo-box-output-item> <div class=\"flex justify-between items-center w-full\"> <div class=\"truncate\" data-combo-box-output-item-field=\"title\" data-combo-box-search-text data-combo-box-value></div> <span class=\"icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0\"> </span> </div> </div>",
      "groupingTitleTemplate": "<button type=\"button\" class=\"btn btn-sm btn-text capitalize combo-box-tab-active:btn-active\"></button>",
      "tabsWrapperTemplate": "<div class=\"overflow-x-auto mb-1 pb-2\"></div>"
    }' >
    <!-- SearchBox -->
    <div class="relative">
      <input class="input ps-8" type="text" placeholder="Search or type a command" role="combobox" aria-expanded="false" value="" autofocus="" data-combo-box-input="" />
      <span class="icon-[tabler--search] text-base-content absolute start-3 top-1/2 size-4 shrink-0 -translate-y-1/2" ></span>
    </div>
    <!-- SearchBox body -->
    <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-56 w-full overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" >
      <div data-combo-box-output-items-wrapper="" class="space-y-0.5"></div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Modal -->

{{< headname level="4" >}} Modal {{< /headname >}}

In this example, a modal popup is employed to provide a user-friendly tab filtering experience.

{{< code addClass="!block" jsCode="true" >}}

<h5 class="text-base-content text-base"> Press <kbd class="kbd kbd-sm">\</kbd> for SearchBox. </h5>

<!-- SearchBox Trigger -->

<button type="button" class="hidden" aria-haspopup="dialog" aria-expanded="false" aria-controls="tab-modal-combo-box" data-overlay="#tab-modal-combo-box" ></button>

<!-- SearchBox Modal -->
<div id="tab-modal-combo-box" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 overflow-x-hidden">
    <div class="modal-content max-h-full">
      <div class="relative"
        data-combo-box='{
            "preventVisibility": true,
            "groupingType": "tabs",
            "isOpenOnFocus": true,
            "apiUrl": "https://fakestoreapi.com/products",
            "apiGroupField": "category",
            "outputItemTemplate": "<div class=\"dropdown-item combo-box-selected:dropdown-active\" data-combo-box-output-item> <div  class=\"flex justify-between items-center w-full\"> <div class=\"truncate\" data-combo-box-output-item-field=\"title\" data-combo-box-search-text data-combo-box-value></div> <span class=\"icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0\"> </span> </div> </div>",
            "groupingTitleTemplate": "<button type=\"button\" class=\"btn btn-sm btn-text capitalize combo-box-tab-active:btn-active\"></button>",
            "tabsWrapperTemplate": "<div class=\"overflow-x-auto mb-1 pb-2\"></div>"
            }' >
        <div class="modal-header block">
          <div class="relative">
            <input class="input ps-8" type="text" placeholder="Search or type a command" role="combobox" aria-expanded="false" value="" autofocus="" data-combo-box-input="" />
            <span class="icon-[tabler--search] text-base-content absolute start-3 top-1/2 size-4 shrink-0 -translate-y-1/2" ></span>
          </div>
        </div>
        <!-- SearchBox Modal Body -->
        <div class="modal-body" data-combo-box-output="">
          <div class="overflow-y-auto max-h-72 space-y-0.5" data-combo-box-output-items-wrapper="" ></div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    //tab modal combo box
    const tabOverlay = HSOverlay.getInstance('#tab-modal-combo-box', true)
    const tabCombobox = HSComboBox.getInstance('#tab-modal-combo-box [data-combo-box]', true)

    window.addEventListener('keydown', function (evt) {
      if (evt.code === 'Backslash') {
        if (tabOverlay.element && tabOverlay.element.el.classList.contains('open')) return false

        tabOverlay.element.open()
        tabCombobox.element.setCurrent()
      }
    })
  })
</script>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Destroy/Reinitialize -->
{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}
The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a toggle count.

{{< code addClass="!block h-64" jsCode="true" >}}
<div id="combo-box-to-destroy" class="relative max-w-sm" data-combo-box="">
  <div class="relative">
    <input class="input" type="text" value="India" role="combobox" aria-expanded="false" data-combo-box-input="" aria-label="Combobox Destroy" />
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" >
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="0" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Venezuela" data-combo-box-value="">Venezuela</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="1" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Papua New Guinea" data-combo-box-value="">Papua New Guinea</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="2" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="South Africa " data-combo-box-value="">South Africa</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="3" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Honduras" data-combo-box-value="">Honduras</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="4" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="India" data-combo-box-value="">India</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="5" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="El Salvador" data-combo-box-value="">El Salvador</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
  </div>
</div>

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    // Destroy and reinit variables
    const combobox = document.querySelector('#combo-box-to-destroy')
    const destroyBtn = document.querySelector('#destroy-btn')
    const reinitBtn = document.querySelector('#reinit-btn')

    // Destroy usage
    destroyBtn.addEventListener('click', () => {
      const { element } = HSComboBox.getInstance(combobox, true)

      element.destroy()

      destroyBtn.setAttribute('disabled', 'disabled')
      reinitBtn.removeAttribute('disabled')
    })

    // Reinit usage
    reinitBtn.addEventListener('click', () => {
      HSComboBox.autoInit()

      reinitBtn.setAttribute('disabled', 'disabled')
      destroyBtn.removeAttribute('disabled')
    })    
  })
</script>
{{< /code >}}

<!-------------------- Accessibility notes -------------------->

{{< headname level="2" >}} Accessibility notes {{< /headname >}}

<!-- Keyboard interactions -->

{{< headname level="3" >}} Keyboard interactions {{< /headname >}}

<!-- interactions table -->

{{< table >}}
COMMAND| DESCRIPTION
<kbd class="kbd kbd-sm">Enter</kbd>| Activates the selected tab.

<div class="flex gap-3"><kbd class="kbd kbd-sm">A-Z</kbd> <kbd class="kbd kbd-sm">a-z</kbd></div>| Focuses first item that matches keyboard input.
<div class="flex gap-3"><kbd class="kbd kbd-sm">Home</kbd> <kbd class="kbd kbd-sm">End</kbd></div>| Focuses first/last non-disabled item.
<kbd class="kbd kbd-sm">Esc</kbd>| Closes any open Menus.
<div class="flex gap-3"><kbd class="kbd"><span class="icon-[tabler--caret-up-filled] size-5"></span></kbd> <kbd class="kbd"><span class="icon-[tabler--caret-down-filled] size-5"></span></kbd></div>| Focuses previous/next non-disabled item.
{{< /table >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

<!-- Options table -->

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/combobox.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

{{< table >}}
PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span colspan="4" class="text-base-content font-semibold">General Options</span>
<span class="text-nowrap">`data-combo-box`</span> | Activates a ComboBox on a specific element. | — | —
`:gap` | Defines the gap between the input field and the dropdown list. | number | `6`
`:viewport` | Specifies the parent element for calculating dropdown list position, by default relative to the document. | string, HTMLElement | `—`
`:preventVisibility` | If `true`, prevents visibility changes in the ComboBox. | boolean | `false`
`:preventSelection` | If `true`, prevents item selection in the dropdown list. | boolean | `false`
`:isOpenOnFocus` | If `true`, the dropdown list opens when the field is focused. | boolean | `false`
`:groupingType` | Type of grouping used in the dropdown. | default, tags | `—`
`:groupingTitleTemplate` | Template for the title in grouped ComboBox. | One line HTML markup | `—`
`:preventAutoPosition` | If `true`, it disables dropdown auto-positioning. | boolean | `false`
`:tabsWrapperTemplate` | Template for the tabs wrapper in the ComboBox. | One line HTML markup | `<div class="overflow-x-auto p-4"></div>`
`:minSearchLength` | Sets the minimum number of characters required to activate the search functionality. | number | `0`
<span colspan="4" class="text-base-content font-semibold">API Options</span>
`:apiUrl` | The URL endpoint for fetching data via API. | string, null | `—`
`:apiDataPart` | Specifies the part of the returned data to use as the primary data array. | string, null | `—`
`:apiQuery` | Parameters for API requests, like limiting results. | string, null | `—`
`:apiSearchQuery` | Parameter name used for search queries. | string, null | `—`
`:apiHeaders` | Headers to include in API requests. | object | `{}`
`:apiGroupField` | Field in the API response used for data grouping. | string, null | `—`
`:apiSearchPath` | A string that specifies the endpoint path for the API request, excluding the base URL. For example, if the full API URL is `https://some-api.com/part/of/the/url`, apiSearchPath should be set to `part/of/the/url`. Note: The parameters `apiSearchPath` and `apiSearchDefaultPath` are mutually exclusive with `apiSearchQuery`. Only one of these options should be used in a request to define the API endpoint path. | string, null | `—`
`:apiSearchDefaultPath` | A string that defines the default API endpoint path to be used when the input field is empty or an empty request is sent. This path provides a fallback for requests without specific search terms. For example, if the full API URL is `https://some-api.com/countries/all`, set `apiSearchDefaultPath` to `countries/all`. Note: The parameters `apiSearchPath` and `apiSearchDefaultPath` are mutually exclusive with `apiSearchQuery`. Only one of these options should be used in a request to define the API endpoint path.| string, null | `—`

<span colspan="4" class="text-base-content font-semibold">Template Options</span>
`:outputItemTemplate` | Template for individual items in the dropdown list. | string, null | `<div class="dropdown-item combo-box-selected:dropdown-active" data-combo-box-output-item> ... </div>`
`:outputEmptyTemplate` | Template for when no data is found in the dropdown. | string, null | `Nothing found...`
`:outputLoaderTemplate` | Template for the loader when fetching data. | string, null | `<span class="loading loading-spinner text-primary"></span>`
`:searchWrapperTemplate` | Template for the search field wrapper. | string, null | `<div></div>`

<span colspan="4" class="text-base-content font-semibold">Input & Output Options</span>
`data-combo-box-input` | Identifies the element responsible for data entry in the ComboBox. | — | `—`
`data-combo-box-output` | Identifies the element that outputs data from the ComboBox. | — | `—`
`data-combo-box-toggle` | Element that toggles the dropdown list. | — | `—`
`data-combo-box-open` | Element that open the dropdown list. | — | `—`
`data-combo-box-close` | Element that close the dropdown list. | — | `—`
`data-combo-box-output-item` |Defines an element within the initialized container that will handle the display of each individual data item.| — |`—`
`> data-combo-box-search-text` |Defines the element within which text will be searched.| — | `—`
`> data-combo-box-value` |Defines an element whose text will be set as a value when selected.| — | `—`
`> data-combo-box-output-item-field`| Defines a data field that will be taken to fill the element with text.| — | `—`
`> data-combo-box-output-item-attr` |Defines the attributes that will be filled with the corresponding data. For example, the src attribute of an image. | — | `—`
`:valueFrom` | Field name from which data will be taken. | string | `—`
`:attr` | Attribute name where data will be supplied. | string | `—`
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSCombobox` object is contained within the global `window` object.

{{< table >}}

METHOD | DESCRIPTION
<span colspan="3" class="text-base-content font-semibold">PUBLIC METHODS</span>
`getCurrentData` | Returns the data of the selected element as an object. This data must first be assigned as a value to the data parameter `data-combo-box-item-stored-data`, when standard rendering. And when rendering via the API, the data is automatically substituted into the data attribute (no need to do it yourself).
`open()` | Opens the autosuggestion list.
`close()` | Closes the autosuggestion list.
`recalculateDirection()` | Forces recalculation of the autosuggestion list's positions.
`destroy()` | Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="4" class="text-base-content font-semibold">STATIC METHODS</span>
`HSCombobox.getInstance(target, isInstance)` | <div>Returns the element associated with the <code>target</code>. <ul class="m-0"><li>The <code>target</code> can be a <code>Node</code> or a valid CSS selector.</li><li><code>isInstance</code> (boolean) - returns the instance instead of the <code>Node</code> if <code>true</code>.</li></ul></div>
`HSCombobox.autoInit()` | Reinitializes all ComboBoxes on the page.
`HSCombobox.close(target)` | <div>Closes the target ComboBox. <ul class="m-0"><li>The <code>target</code> should be a <code>Node</code> or a valid CSS selector.</li></ul></div>
`HSCombobox.closeCurrentlyOpened()` | Closes the currently opened ComboBox.
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

Below, is the demonstration on how to use the methods. To test other methods, copy the following methods into your console and click the button.

{{< code addClass="!block h-64 relative" jsCode="true" >}}

<!-- Basic ComboBox structure with JavaScript event handling -->
<div class="relative max-w-sm" id="combo-box-method" data-combo-box="">
  <div class="relative">
    <input class="input" type="text" value="India" role="combobox" aria-expanded="false" data-combo-box-input="" aria-label="Default combobox" />
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" >
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="0" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Venezuela" data-combo-box-value="">Venezuela</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="1" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Papua New Guinea" data-combo-box-value="">Papua New Guinea</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="2" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="South Africa " data-combo-box-value="">South Africa</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="3" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Honduras" data-combo-box-value="">Honduras</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="4" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="India" data-combo-box-value="">India</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="5" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="El Salvador" data-combo-box-value="">El Salvador</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
  </div>
</div>

<button id="open-btn" class="btn btn-primary mt-4 absolute top-28 sm:top-2 sm:end-6">Open ComboBox</button>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const comboBox = new HSComboBox(document.querySelector('#combo-box-method'))
    const openBtn = document.querySelector('#open-btn')

    openBtn.addEventListener('click', () => {
      comboBox.open()
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">Open item (public method).</p>

{{< code-highlight lang="js" >}}// This method is used in above example.
const comboBox = new HSComboBox(document.querySelector('#combo-box-method'));
const openBtn = document.querySelector('#open-btn')

openBtn.addEventListener('click', () => {
  comboBox.open()
})
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose">Open item (mixed).</p>

{{< code-highlight lang="js" >}}const { element } = HSComboBox.getInstance('#combo-box-method', true);
const openBtn = document.querySelector('#open-btn');

openBtn.addEventListener('click', () => {
  element.open();
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose" id="destroy-method">Destroy instance.</p>

{{< code-highlight lang="js" >}}
const { element } = HSComboBox.getInstance('#combo-box-to-destroy', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION | RETURNING VALUE
`on:select`| Called when any select is changed. | Current value
{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

Display a console log message when an option is selected.

{{< code addClass="!block h-72" jsCode="true" >}}

<div class="relative max-w-sm" id="combo-box-event" data-combo-box="">
  <div class="relative">
    <input class="input" type="text" value="India" role="combobox" aria-expanded="false" data-combo-box-input="" aria-label="Default combobox" />
    <span class="icon-[tabler--caret-up-down] text-base-content absolute end-3 top-1/2 size-4 shrink-0 -translate-y-1/2" data-combo-box-toggle="" ></span>
  </div>
  <div class="bg-base-100 rounded-box shadow-base-300/20 absolute z-50 max-h-44 w-full space-y-0.5 overflow-y-auto p-2 shadow-lg" style="display: none" data-combo-box-output="" >
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="0" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Venezuela" data-combo-box-value="">Venezuela</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="1" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Papua New Guinea" data-combo-box-value="">Papua New Guinea</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="2" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="South Africa " data-combo-box-value="">South Africa</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="3" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="Honduras" data-combo-box-value="">Honduras</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="4" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="India" data-combo-box-value="">India</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
    <div class="dropdown-item combo-box-selected:dropdown-active" tabindex="5" data-combo-box-output-item="">
      <div class="flex items-center justify-between">
        <span data-combo-box-search-text="El Salvador" data-combo-box-value="">El Salvador</span>
        <span class="icon-[tabler--check] text-primary combo-box-selected:block hidden size-4 shrink-0"></span>
      </div>
    </div>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () =>
    const comboBoxEvent = HSComboBox.getInstance('#combo-box-event', true).element
    comboBoxEvent.on('select', value => {
      console.log(comboBoxEvent.value)
    })
  )
</script>

{{< /code >}}

<p class="mt-12 mb-1.5 not-prose">When select changes event example.</p>

{{< code-highlight lang="js" >}}const {element} = HSComboBox.getInstance('#event-select', true);

element.on('select', (value) => {console.log("element.value")});
{{< /code-highlight >}}
