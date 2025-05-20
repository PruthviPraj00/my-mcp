---
title: "Radio "
components: 5
description: "The radio component allows users to select one option from multiple choices. It comes in various styles, variants, and colors."
bg_image: "svg/form-elements/radio.svg"
menu:
  main:
    parent: "forms"

previous: Join
previousLink: forms/join/

next: Range
nextLink: forms/range/
---

<!-- Class table -->

{{< class-table >}}
radio| component | Component class for radio.
custom-option| component | For custom option container.
custom-soft-option| component | For custom option container with background.
label-text | part | Base class for title label text.
helper-text | part | Base class for helper label text.
radio-inset| style | Targets radio input.
radio-primary | color | Adds 'primary' color to radio.
radio-secondary | color | Adds 'secondary' color to radio.
radio-accent | color | Adds 'accent' color to radio.
radio-info | color | Adds 'info' color to radio.
radio-success | color | Adds 'success' color to radio.
radio-warning | color | Adds 'warning' color to radio.
radio-error | color | Adds 'error' color to radio.
is-valid | state | Adds success style to the input.
is-invalid | state | Adds error style to the input.
radio-xs | size | radio with extra small size.
radio-sm | size | radio with small size.
radio-md | size | radio with medium(default) size.
radio-lg | size | radio with large size.
radio-xl | size | radio with extra large size.
{{< /class-table >}}

<!--------------------  Basic example  -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!--  Default  -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic radio example.

{{< code >}}

<div class="flex items-center gap-1">
  <input type="radio" name="radio-0" class="radio" id="defaultRadio1" />
  <label class="label-text text-base" for="defaultRadio1"> Default </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" name="radio-0" class="radio" id="defaultRadio2" checked />
  <label class="label-text text-base" for="defaultRadio2"> Checked </label>
</div>
{{< /code >}}

<!--  Label and helper text  -->

{{< headname level="3" >}} Label and helper text {{< /headname >}}

Please use `label-text` for the label and `helper-text` for the text that appears at the bottom as helper text.

{{< code addClass="flex-col" >}}

<div class="flex gap-3">
  <input type="radio" name="radio-1" class="radio radio-primary mt-2" id="radioDelete" />
  <label class="label-text cursor-pointer flex flex-col" for="radioDelete">
    <span class="text-base">Delete</span>
    <span>Notify me when this action happens.</span>
  </label>
</div>

<div class="flex gap-3">
  <input type="radio" name="radio-1" class="radio radio-primary mt-2" id="radioArchieve" checked />
  <label class="label-text cursor-pointer flex flex-col" for="radioArchieve">
    <span class="text-base">Archive</span>
    <span>Notify me when this action happens.</span>
  </label>
</div>
{{< /code >}}

<!-------------------- Types -------------------->

{{< headname level="2" >}} Types {{< /headname >}}

<!--  Default  -->

{{< headname level="3" >}} Default {{< /headname >}}

Apply the `radio` class to style radio buttons.

{{< code >}}

<div class="flex items-center gap-1">
  <input type="radio" name="radio-2" class="radio radio-primary" id="radioType1" />
  <label class="label-text text-base" for="radioType1"> Default </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" name="radio-2" class="radio radio-primary" id="radioType2" checked />
  <label class="label-text text-base" for="radioType2"> Checked </label>
</div>
{{< /code >}}

<!--  Inset radio  -->

{{< headname level="3" >}} Inset radio {{< /headname >}}

Use `radio-inset` alongside `radio` to create an inset radio.

{{< code >}}

<div class="flex items-center gap-1">
  <input type="radio" name="radio-3" class="radio radio-inset radio-primary" id="radioType3"  />
  <label class="label-text text-base" for="radioType3"> Default </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" name="radio-3" class="radio radio-inset radio-primary" id="radioType4" checked/>
  <label class="label-text text-base" for="radioType4"> Checked </label>
</div>
{{< /code >}}

<!-------------------- Color -------------------->

{{< headname level="2" >}} Color {{< /headname >}}

<!--  Semantic color  -->

{{< headname level="3" >}} Semantic color {{< /headname >}}

Example of semantic color in default and inset radio.

<!--  Default radio  -->

{{< headname level="4" >}} Default radio {{< /headname >}}

Add color to the radio button by utilizing the `radio-{semantic-color}` class in conjunction with the `radio` class.

{{< code addClass="flex-col gap-3" >}}

<div class="flex items-center gap-1">
  <input type="radio"  class="radio" id="radioDefault1" checked />
  <label class="label-text text-base" for="radioDefault1"> Default </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio"  class="radio radio-primary" id="radioPrimary1" checked />
  <label class="label-text text-base" for="radioPrimary1"> Primary </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio"  class="radio radio-secondary" id="radioSecondary1" checked />
  <label class="label-text text-base" for="radioSecondary1"> Secondary </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio"  class="radio radio-accent" id="radioAccent1" checked />
  <label class="label-text text-base" for="radioAccent1"> Accent </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio"  class="radio radio-info" id="radioInfo1" checked />
  <label class="label-text text-base" for="radioInfo1"> Info </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio"  class="radio radio-success" id="radioSuccess1" checked />
  <label class="label-text text-base" for="radioSuccess1"> Success </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio"  class="radio radio-warning" for="radioWarning1" checked />
  <label class="label-text text-base" for="radioWarning1"> Warning </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio"  class="radio radio-error" for="radioError1" checked />
  <label class="label-text text-base" for="radioError1"> Error </label>
</div>
{{< /code >}}

<!-- Inset radio -->

{{< headname level="4">}} Inset radio {{< /headname >}}

Use the `radio-{semantic-color}` class in combination with the `radio-inset` class.

{{< code addClass="flex-col gap-3" >}}

<div class="flex items-center gap-1">
  <input type="radio" class="radio radio-inset" id="radioDefault2" checked />
  <label class="label-text text-base" for="radioDefault2"> Default </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" class="radio radio-inset radio-primary" id="radioPrimary2" checked />
  <label class="label-text text-base" for="radioPrimary2"> Primary </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" class="radio radio-inset radio-secondary" id="radioSecondary2" checked />
  <label class="label-text text-base" for="radioSecondary2"> Secondary </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" class="radio radio-inset radio-accent" id="radioAccent2" checked />
  <label class="label-text text-base" for="radioAccent2"> Accent </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" class="radio radio-inset radio-info" id="radioInfo2" checked />
  <label class="label-text text-base" for="radioInfo2"> Info </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" class="radio radio-inset radio-success" id="radioSuccess2" checked />
  <label class="label-text text-base" for="radioSuccess2"> Success </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" class="radio radio-inset radio-warning" id="radioWarning2" checked />
  <label class="label-text text-base" for="radioWarning2"> Warning </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" class="radio radio-inset radio-error" id="radioError2" checked />
  <label class="label-text text-base" for="radioError2"> Error </label>
</div>
{{< /code >}}

<!--  Custom color  -->

{{< headname level="3" >}} Custom color {{< /headname >}}

Example of custom color in default and custom radio.

<!--  Default radio  -->

{{< headname level="4" >}} Default radio {{< /headname >}}

Got it! Here's the rephrased explanation:

To create a custom radio button, you can use `checked:text-*`, but you'll need to apply the `checked:` modifier. Alternatively, you can use `--input-color`, which automatically applies the color when the radio button is checked, without needing the `checked:` modifier.

{{< code >}}

<div class="flex items-center gap-1">
  <input type="radio" name="radio-4" class="radio [--input-color:pink]" id="radioCustomColor1" />
  <label class="label-text text-base" for="radioCustomColor1"> FlyonUI variable </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" name="radio-4" class="radio checked:text-pink-300" id="radioCustomColor2" checked />
  <label class="label-text text-base" for="radioCustomColor2"> Tailwind utility colors </label>
</div>
{{< /code >}}

<!--  Inset radio  -->

{{< headname level="4" >}} Inset radio {{< /headname >}}

Custom inset radio.

{{< code >}}

<div class="flex items-center gap-1">
  <input type="radio" name="radio-5" class="radio radio-inset [--input-color:green]" id="radioCustomColor3"  />
  <label class="label-text text-base" for="radioCustomColor3"> FlyonUI variable </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" name="radio-5" class="radio radio-inset checked:text-green-700" id="radioCustomColor4"  checked />
  <label class="label-text text-base" for="radioCustomColor4"> Tailwind utility colors </label>
</div>
{{< /code >}}

<!-------------------- Sizes -------------------->

{{< headname level="2" >}} Sizes {{< /headname >}}

<!--  Default radio size  -->

{{< headname level="3" >}} Default radio size {{< /headname >}}

Add responsive class `radio-{size}` where `{size} = xs|sm|md|lg|xl` for radio of different sizes.

{{< code >}}

<div class="flex items-center">
  <input type="radio" name="radio-6" class="radio radio-xs radio-primary" id="radioExtraSmall1" />
  <label class="label-text text-xs" for="radioExtraSmall1"> Extra small </label>
</div>
<div class="flex items-center gap-0.5">
  <input type="radio" name="radio-6" class="radio radio-sm radio-primary" id="radioSmall1" />
  <label class="label-text" for="radioSmall1"> Small </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" name="radio-6" class="radio radio-primary" id="radioSizeDefault1" checked />
  <label class="label-text text-base" for="radioSizeDefault1"> Default </label>
</div>
<div class="flex items-center gap-1.5">
  <input type="radio" name="radio-6" class="radio radio-lg radio-primary" id="radioLarge1" />
  <label class="label-text text-lg" for="radioLarge1"> Large </label>
</div>
<div class="flex items-center gap-1.5">
  <input type="radio" name="radio-6" class="radio radio-xl radio-primary" id="radioExtraLarge1" />
  <label class="label-text text-xl" for="radioExtraLarge1"> Extra Large </label>
</div>
{{< /code >}}

<!--  Inset radio size  -->

{{< headname level="3" >}} Inset radio size {{< /headname >}}

Add responsive class `radio-{size}` where `{size} = xs|sm|md|lg|xl` for radio inset of different sizes.

{{< code >}}

<div class="flex items-center">
  <input type="radio" name="radio-7" class="radio radio-inset radio-xs radio-primary" id="radioExtraSmall2" />
  <label class="label-text text-xs" for="radioExtraSmall2"> Extra small </label>
</div>
<div class="flex items-center gap-0.5">
  <input type="radio" name="radio-7" class="radio radio-inset radio-sm radio-primary" id="radioSmall2" />
  <label class="label-text" for="radioSmall2"> Small </label>
</div>
<div class="flex items-center gap-1">
  <input type="radio" name="radio-7" class="radio radio-inset radio-primary" id="radioSizeDefault2" checked />
  <label class="label-text text-base" for="radioSizeDefault2"> Default </label>
</div>
<div class="flex items-center gap-1.5">
  <input type="radio" name="radio-7" class="radio radio-inset radio-lg radio-primary" id="radioLarge" />
  <label class="label-text text-lg" for="radioLarge"> Large </label>
</div>
<div class="flex items-center gap-1.5">
  <input type="radio" name="radio-7" class="radio radio-inset radio-xl radio-primary" id="radioExtraLarge" />
  <label class="label-text text-xl" for="radioExtraLarge"> Extra Large </label>
</div>
{{< /code >}}

<!-------------------- Validation states -------------------->

{{< headname level="2" >}} Validation states {{< /headname >}}

<!-- Success state -->

{{< headname level="3" >}} Success state {{< /headname >}}

Success state can be show using `is-valid` class.

{{< code addClass="flex-col" >}}

<div class="flex gap-3">
  <input type="radio" name="radio-success" class="radio radio-primary is-valid mt-2" id="radioStateSuccess1" checked />
  <label class="label-text cursor-pointer flex flex-col" for="radioStateSuccess1">
    <span class="text-base">Delete</span>
    <span>Notify me when this action happens.</span>
  </label>
</div>
<div class="flex gap-3">
  <input type="radio" name="radio-success" class="radio radio-inset radio-primary is-valid mt-2" id="radioStateSuccess2" checked />
  <label class="label-text cursor-pointer flex flex-col" for="radioStateSuccess2">
    <span class="text-base">Archive</span>
    <span>Notify me when this action happens.</span>
  </label>
</div>
{{< /code >}}

<!-- Error state -->

{{< headname level="3" >}} Error state {{< /headname >}}

Error state can be show using `is-invalid` class.

{{< code addClass="flex-col" >}}

<div class="flex gap-3">
  <input type="radio" name="radio-error" class="radio radio-primary is-invalid mt-2" id="radioStateError1" checked/>
  <label class="label-text cursor-pointer flex flex-col" for="radioStateError1">
    <span class="text-base">Delete</span>
    <span>Notify me when this action happens.</span>
  </label>
</div>
<div class="flex gap-3">
  <input type="radio" name="radio-error" class="radio radio-inset radio-primary is-invalid mt-2" id="radioStateError2" />
  <label class="label-text cursor-pointer flex flex-col" for="radioStateError2">
    <span class="text-base">Archive</span>
    <span>Notify me when this action happens.</span>
  </label>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!--  Disable  -->

{{< headname level="3" >}} Disable {{< /headname >}}

Disable the radio component to prevent user selection by applying the `disabled` attribute.

{{< code addClass="flex-col" >}}

<div class="space-x-3">
  <input type="radio" name="radio-8" class="radio" aria-label="disabled radio" checked disabled />
  <input type="radio" name="radio-8" class="radio" aria-label="disabled radio" disabled />
</div>
<div class="space-x-3">
  <input type="radio" name="radio-9" class="radio radio-inset" aria-label="disabled radio" checked disabled />
  <input type="radio" name="radio-9" class="radio radio-inset" aria-label="disabled radio" disabled />
</div>
{{< /code >}}

<!--  Inline radio group  -->

{{< headname level="3" >}} Inline radio group {{< /headname >}}

A group of radio components.

{{< code >}}

<div class="flex gap-4 overflow-x-auto">
  <div class="flex items-center gap-2">
    <input type="radio" name="radio-10" class="radio radio-primary" id="radioInline1" />
    <label class="label-text text-base" for="radioInline1"> Vue </label>
  </div>
  <div class="flex items-center gap-2">
    <input type="radio" name="radio-10" class="radio radio-primary" id="radioInline2" checked />
    <label class="label-text text-base" for="radioInline2"> Angular </label>
  </div>
  <div class="flex items-center gap-2">
    <input type="radio" name="radio-10" class="radio radio-primary" id="radioInline3" />
    <label class="label-text text-base" for="radioInline3"> React </label>
  </div>
</div>
{{< /code >}}

<!--  Vertical radio group  -->

{{< headname level="3" >}} Vertical radio group {{< /headname >}}

A vertical group of radio components.

{{< code >}}

<div class="flex flex-col gap-2">
  <div class="flex items-center gap-2">
    <input type="radio" name="radio-11" class="radio radio-primary" id="radioVertical1" />
    <label class="label-text text-base" for="radioVertical1"> Vue </label>
  </div>
  <div class="flex items-center gap-2">
    <input type="radio" name="radio-11" class="radio radio-primary" id="radioVertical2" checked />
    <label class="label-text text-base" for="radioVertical2"> Angular </label>
  </div>
  <div class="flex items-center gap-2">
    <input type="radio" name="radio-11" class="radio radio-primary" id="radioVertical3" />
    <label class="label-text text-base" for="radioVertical3"> React </label>
  </div>
</div>
{{< /code >}}

<!--  Radio in dropdown  -->

{{< headname level="3" >}} Radio in dropdown {{< /headname >}}

Here’s an example of a radio in dropdown that you can use right away.

{{< callout "info" >}}
To learn more about dropdowns, refer to the {{< link link="overlays/dropdown/" addClass="link link-primary" >}}Dropdown{{< /link >}} documentation.
{{< /callout >}}

{{< code >}}

<div class="dropdown relative inline-flex [--auto-close:inside]">
  <button id="dropdown-radio" type="button" class="dropdown-toggle btn btn-primary" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
    Dropdown radio
    <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
  </button>
  <div class="dropdown-menu dropdown-open:opacity-100 hidden min-w-60" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-radio">
    <div class="dropdown-item flex-col items-center gap-4 sm:flex-row sm:items-start">
      <input name="radio-12" type="radio" class="radio radio-primary mt-2" id="radioDropdown1" checked />
      <label class="label-text cursor-pointer flex flex-col" for="radioDropdown1">
        <span class="font-semibold">Rename</span>
        <span class="text-base-content/50">Notify me when this action happens.</span>
      </label>
    </div>
    <div class="dropdown-item flex-col items-center gap-4 sm:flex-row sm:items-start">
      <input name="radio-12" type="radio" class="radio radio-primary mt-2" id="radioDropdown2" />
      <label class="label-text cursor-pointer flex flex-col" for="radioDropdown2">
        <span class="font-semibold">Move</span>
        <span class="text-base-content/50">Notify me when this action happens.</span>
      </label>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Radio list group  -->

{{< headname level="3" >}} Radio list group {{< /headname >}}

Below given example can be used to show a list of radio buttons inside a grouped list.

{{< code addClass="!block" >}}

<h6 class="text-base text-base-content mb-1">Select you favourite language:</h6>
<ul class="border-base-content/25 divide-base-content/25 rounded-box max-w-sm divide-y border *:cursor-pointer">
  <li>
    <label class="flex items-center gap-3 p-3">
      <input type="radio" name="radio-13" class="radio radio-primary" />
      <span class="label-text text-base"> C++ </span>
    </label>
  </li>
  <li>
    <label class="flex items-center gap-3 p-3">
      <input type="radio" name="radio-13" class="radio radio-primary" checked />
      <span class="label-text text-base"> Ruby </span>
    </label>
  </li>
  <li>
    <label class="flex items-center gap-3 p-3">
      <input type="radio" name="radio-13" class="radio radio-primary" />
      <span class="label-text text-base"> Swift </span>
    </label>
  </li>
</ul>
{{< /code >}}

<!--  Horizontal list group  -->

{{< headname level="3" >}} Horizontal list group {{< /headname >}}

Use below example to group up radio button components inside a list.

{{< code addClass="!block" >}}

<h6 class="text-base text-base-content mb-1">Select you favourite language:</h6>
<ul
  class="border-base-content/25 divide-base-content/25 rounded-box flex w-full flex-col border *:w-full *:cursor-pointer max-sm:divide-y sm:flex-row sm:divide-x">
  <li>
    <label class="flex items-center gap-2 p-3">
      <input type="radio" name="radio-14" class="radio radio-primary ms-3" />
      <span class="label-text text-base"> Python </span>
    </label>
  </li>
  <li>
    <label class="flex items-center gap-2 p-3">
      <input type="radio" name="radio-14" class="radio radio-primary ms-3" checked />
      <span class="label-text text-base"> JavaScript </span>
    </label>
  </li>
  <li>
    <label class="flex items-center gap-2 p-3">
      <input type="radio" name="radio-14" class="radio radio-primary ms-3" />
      <span class="label-text text-base"> Java </span>
    </label>
  </li>
</ul>
{{< /code >}}

<!--  Join radio with btn style  -->

{{< headname level="3" >}} Join radio with btn style {{< /headname >}}

Create a radio button group using the `join` and `btn` component classes.

{{< callout "info" >}}
To learn more about Radio, refer to the {{< link link="forms/join/" addClass="link link-primary" >}}Join{{< /link >}} documentation.
{{< /callout >}}

{{< code >}}

<div class="join drop-shadow">
  <input class="join-item btn btn-soft" type="radio" name="radio-15" aria-label="Radio 1" checked/>
  <input class="join-item btn btn-soft" type="radio" name="radio-15" aria-label="Radio 2" />
  <input class="join-item btn btn-soft" type="radio" name="radio-15" aria-label="Radio 3" />
</div>
{{< /code >}}

<!-------------------- Custom Options -------------------->

{{< headname level="2" >}} Custom options {{< /headname >}}

<!--  Basic radio  -->

{{< headname level="3" >}} Basic radio {{< /headname >}}

Utilizing the `custom-option` class within the `label` enables the creation of custom radio buttons with improved styling and functionality.

{{< code >}}

<div class="flex w-full items-start gap-3 flex-wrap sm:flex-nowrap">
  <label class="custom-option flex sm:w-1/2 flex-row items-start gap-3">
    <input type="radio" name="radio-16" class="radio radio-primary mt-2" checked />
    <span class="label-text w-full text-start">
      <span class="flex justify-between mb-1">
        <span class="text-base font-medium">Basic</span>
        <span class="text-base-content/50 text-base">Free</span>
      </span>
      <span class="text-base-content/80">Get 1 project with 1 teams members.</span>
    </span>
  </label>
  <label class="custom-option flex sm:w-1/2 flex-row items-start gap-3">
    <input type="radio" name="radio-16" class="radio radio-primary mt-2" />
    <span class="label-text w-full text-start">
      <span class="flex justify-between mb-1">
        <span class="text-base font-medium">Premium</span>
        <span class="text-base-content/50 text-base">$ 5.00</span>
      </span>
      <span class="text-base-content/80">Get 5 projects with 5 team members.</span>
    </span>
  </label>
</div>
{{< /code >}}

<!--  Hidden radio button  -->

{{< headname level="3" >}} Hidden radio button {{< /headname >}}

Utilize the `hidden` TailwindCSS utility class to conceal the radio button.

{{< code >}}

<div class="flex w-full items-start gap-3 flex-wrap sm:flex-nowrap">
  <label class="custom-option flex sm:w-1/2 flex-row items-start gap-3">
    <input type="radio" name="radio-17" class="radio hidden" checked />
    <span class="label-text w-full text-start">
      <span class="flex justify-between mb-1">
        <span class="text-base font-medium">Basic</span>
        <span class="text-base-content/50 text-base">Free</span>
      </span>
      <span class="text-base-content/80">Get 1 project with 1 teams members.</span>
    </span>
  </label>
  <label class="custom-option flex sm:w-1/2 flex-row items-start gap-3">
    <input type="radio" name="radio-17" class="radio hidden" />
    <span class="label-text w-full text-start">
      <span class="flex justify-between mb-1">
        <span class="text-base font-medium">Premium</span>
        <span class="text-base-content/50 text-base">$ 5.00</span>
      </span>
      <span class="text-base-content/80">Get 5 projects with 5 team members.</span>
    </span>
  </label>
</div>
{{< /code >}}

<!--  Basic label radio  -->

{{< headname level="3" >}} Basic label radio {{< /headname >}}

Utilizing the `custom-soft-option` class within the `label` demonstrates this distinctive styling approach, where the label background becomes primary when checked.

{{< code >}}

<div class="flex w-full items-start gap-3 flex-wrap sm:flex-nowrap">
  <label class="custom-soft-option flex sm:w-1/2 flex-row items-start gap-3">
    <input type="radio" name="radio-18" class="radio radio-primary mt-2" checked />
    <span class="label-text w-full text-start">
      <span class="flex justify-between mb-1">
        <span class="text-base font-medium">Basic</span>
        <span class="text-base-content/50 text-base">Free</span>
      </span>
      <span class="text-base-content/80">Get 1 project with 1 teams members.</span>
    </span>
  </label>
  <label class="custom-soft-option flex sm:w-1/2 flex-row items-start gap-3">
    <input type="radio" name="radio-18" class="radio radio-primary mt-2" />
    <span class="label-text w-full text-start">
      <span class="flex justify-between mb-1">
        <span class="text-base font-medium">Premium</span>
        <span class="text-base-content/50 text-base">$ 5.00</span>
      </span>
      <span class="text-base-content/80">Get 5 projects with 5 team members.</span>
    </span>
  </label>
</div>
{{< /code >}}

<!--  Iconic custom radios  -->

{{< headname level="3" >}} Iconic custom radios {{< /headname >}}

Customize the styling using utility classes according to your custom preferences, as illustrated below.

{{< code >}}

<div class="flex w-full items-start gap-3 flex-wrap sm:flex-nowrap">
  <label class="custom-option flex sm:w-1/2 flex-col items-center gap-3">
    <span class="icon-[tabler--rocket] size-10"></span>
    <div class="label-text">
      <h6 class="text-base font-medium mb-1">Starter</h6>
      <span class="text-base-content/80"> Cake sugar plum fruitcake I love sweet roll jelly-o</span>
    </div>
    <input type="radio" name="radio-19" class="radio radio-primary" />
  </label>
  <label class="custom-option flex sm:w-1/2 flex-col items-center gap-3">
    <span class="icon-[tabler--user] size-10"></span>
    <div class="label-text">
      <h6 class="text-base font-medium mb-1">Personal</h6>
      <span class="text-base-content/80"> Cake sugar plum fruitcake I love sweet roll jelly-o.</span>
    </div>
    <input type="radio" name="radio-19" class="radio radio-primary" checked />
  </label>
  <label class="custom-option flex sm:w-1/2 flex-col items-center gap-3">
    <span class="icon-[tabler--crown] size-10"></span>
    <div class="label-text">
      <h6 class="text-base font-medium mb-1">Enterprise</h6>
      <span class="text-base-content/80"> Cake sugar plum fruitcake I love sweet roll jelly-o.</span>
    </div>
    <input type="radio" name="radio-19" class="radio radio-primary" />
  </label>
</div>
{{< /code >}}

<!--  Image as radio button  -->

{{< headname level="3" >}} Image as radio button {{< /headname >}}

This example displays an image as a radio button.

{{< code >}}

<div class="flex items-start gap-3 flex-nowrap">
  <label class="custom-option p-0">
    <span class="w-full">
      <img src="https://cdn.flyonui.com/fy-assets/components/radio/image-6.png" class="bg-contain" alt="Radio image"/>
    </span>
    <input type="radio" name="radio-20" class="radio hidden" />
  </label>
  <label class="custom-option p-0">
    <span class="w-full">
      <img src="https://cdn.flyonui.com/fy-assets/components/radio/image-3.png" class="bg-contain" alt="Radio image"/>
    </span>
    <input type="radio" name="radio-20" class="radio hidden" checked />
  </label>
  <label class="custom-option p-0">
    <span class="w-full">
     <img src="https://cdn.flyonui.com/fy-assets/components/radio/image-5.png" class="bg-contain" alt="Radio image"/>
    </span>
    <input type="radio" name="radio-20" class="radio hidden" />
  </label>
</div>
{{< /code >}}
