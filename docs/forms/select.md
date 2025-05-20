---
title: "Select"
components: 8
description: "A select element is utilized to choose a value from a range of options."
bg_image: "svg/form-elements/select.svg"
menu:
  main:
    parent: "forms"

previous: Range
previousLink: forms/range/

next: Switch
nextLink: forms/switch/
---

<!-- Class table -->

{{< class-table >}}
select | component | Basic select field.
select-floating | component | Floating select field.
select-floating-label | part | Floats the label to the top.
label-text | part | For label.
helper-text | part | For helper text.
is-valid | state | Adds success style to the input.
is-invalid | state | Adds error style to the input.
select-xs | size | Extra small select size.
select-sm | size | Smaller select size.
select-md | size | Medium(default) select size.
select-lg | size | Larger select size.
select-xl | size | Extra large select size.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic select example.

{{< code >}}

<select class="select max-w-sm appearance-none" aria-label="select">
  <option disabled selected>Pick your favorite Movie</option>
  <option>The Godfather</option>
  <option>The Shawshank Redemption</option>
  <option>Pulp Fiction</option>
  <option>The Dark Knight</option>
  <option>Schindler's List</option>
</select>
{{< /code >}}

<!-------------------- Type -------------------->

{{< headname level="2" >}} Type {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

The `<select>` element's customization options are primarily confined to its initial appearance. Due to browser constraints, modifications to the appearance of `<option>` elements within the dropdown are not possible.

{{< code >}}

<div class="w-96">
  <label class="label-text" for="favorite-simpson">Pick your favorite Movie</label>
  <select class="select" id="favorite-simpson">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
</div>
{{< /code >}}

<!-- Floating label -->

{{< headname level="3" >}} Floating label {{< /headname >}}

The `label` remains in its floated position at all times, unlike with `input` elements. Pair `select-floating` with your `select` element and `select-floating-label` for the label.

{{< code >}}

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
{{< /code >}}

<!-------------------- Size -------------------->

{{< headname level="2" >}} Size {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Add responsive class `select-{size}` where `{size} = xs|sm|md|lg|xl` for select of different sizes.

{{< code addClass="flex-col gap-6" >}}

<select class="select select-xs max-w-sm" aria-label="select">
  <option disabled selected>Pick your favorite Movie</option>
  <option>The Godfather</option>
  <option>The Shawshank Redemption</option>
  <option>Pulp Fiction</option>
  <option>The Dark Knight</option>
  <option>Schindler's List</option>
</select>

<select class="select select-sm max-w-sm" aria-label="select">
  <option disabled selected>Pick your favorite Movie</option>
  <option>The Godfather</option>
  <option>The Shawshank Redemption</option>
  <option>Pulp Fiction</option>
  <option>The Dark Knight</option>
  <option>Schindler's List</option>
</select>

<select class="select max-w-sm" aria-label="select">
  <option disabled selected>Pick your favorite Movie</option>
  <option>The Godfather</option>
  <option>The Shawshank Redemption</option>
  <option>Pulp Fiction</option>
  <option>The Dark Knight</option>
  <option>Schindler's List</option>
</select>

<select class="select select-lg max-w-sm" aria-label="select">
  <option disabled selected>Pick your favorite Movie</option>
  <option>The Godfather</option>
  <option>The Shawshank Redemption</option>
  <option>Pulp Fiction</option>
  <option>The Dark Knight</option>
  <option>Schindler's List</option>
</select>

<select class="select select-xl max-w-sm" aria-label="select">
  <option disabled selected>Pick your favorite Movie</option>
  <option>The Godfather</option>
  <option>The Shawshank Redemption</option>
  <option>Pulp Fiction</option>
  <option>The Dark Knight</option>
  <option>Schindler's List</option>
</select>
{{< /code >}}

<!-- Floating label -->

{{< headname level="3" >}} Floating label {{< /headname >}}

Add responsive class `select-{size}` where `{size} = xs|sm|md|lg|xl` for select of different sizes.

{{< code addClass="flex-col gap-6" >}}

<div class="select-floating max-w-sm">
  <select class="select select-xs" id="selectFloatingExtraSmall" aria-label="floating label">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectFloatingExtraSmall">Pick your favorite Movie</label>
</div>

<div class="select-floating max-w-sm">
  <select class="select select-sm" id="selectFloatingSmall" aria-label="floating label">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectFloatingSmall">Pick your favorite Movie</label>
</div>

<div class="select-floating max-w-sm">
  <select class="select" id="selectFloatingDefault" aria-label="floating label">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectFloatingDefault">Pick your favorite Movie</label>
</div>

<div class="select-floating max-w-sm">
  <select class="select select-lg" id="selectFloatingLarge" aria-label="floating label">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectFloatingLarge">Pick your favorite Movie</label>
</div>

<div class="select-floating max-w-sm">
  <select class="select select-xl" id="selectFloatingExtraLarge" aria-label="floating label">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectFloatingExtraLarge">Pick your favorite Movie</label>
</div>
{{< /code >}}

<!-------------------- Select group -------------------->
{{< headname level="2" >}} Select group {{< /headname >}}

<!-- Leading icons -->

{{< headname level="3" >}} Leading icons {{< /headname >}}

Add a leading icon inside select. There are no tailing icons for select

{{< code addClass="!flex-col space-y-4" >}}

<div class="w-96 select">
 <span class="icon-[tabler--movie] text-base-content/80 my-auto size-5 shrink-0"></span>
  <label class="sr-only" for="favorite-simpson">Pick your favorite Movie</label>
  <select id="favorite-simpson">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
</div>

<div class="select max-w-sm">
  <span class="icon-[tabler--movie] text-base-content/80 my-auto size-5 shrink-0"></span>
  <div class="select-floating">
    <select aria-label="Select floating label" id="selectFloating">
      <option>The Godfather</option>
      <option>The Shawshank Redemption</option>
      <option>Pulp Fiction</option>
      <option>The Dark Knight</option>
      <option>Schindler's List</option>
    </select>
    <label class="select-floating-label" for="selectFloating">Pick your favorite Movie</label>
  </div>
</div>
{{< /code >}}


<!-------------------- Validation states -------------------->

{{< headname level="2" >}} Validation states {{< /headname >}}

<!-- Success state -->

{{< headname level="3" >}} Success state {{< /headname >}}

Success state which can be added by using class `is-valid`.

{{< code addClass="flex-col gap-6" >}}

<div class="max-w-sm">
  <label class="label-text" for="selectStateSuccessDefault"> Full Name </label>
  <select class="select is-valid" id="selectStateSuccessDefault">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <span class="helper-text">Helper text</span>
</div>

<div class="select-floating max-w-sm">
  <select class="select is-valid " id="selectStateSuccessFloating">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectStateSuccessFloating">Pick your favorite Movie</label>
  <span class="helper-text">Helper text</span>
</div>
{{< /code >}}

<!-- Error state -->

{{< headname level="3" >}} Error state {{< /headname >}}

Error state can be added using class `is-invalid`.

{{< code addClass="flex-col gap-6" >}}

<div class="max-w-sm">
  <label class="label-text" for="selectStateErrorDefault"> Full Name </label>
  <select class="select is-invalid" id="selectStateErrorDefault">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <span class="helper-text">Helper text</span>
</div>

<div class="select-floating max-w-sm">
  <select class="select is-invalid" id="selectStateErrorFloating">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectStateErrorFloating">Pick your favorite Movie</label>
  <span class="helper-text ps-3">Helper text</span>
</div>
{{< /code >}}

<!-------------------- Shape -------------------->

{{< headname level="2" >}} Shape {{< /headname >}}

<!-- Pilled select -->

{{< headname level="3" >}} Pilled select {{< /headname >}}

Use the `rounded-full` utility class to make select's circular. The default shape of the select but can be altered by using TailwindCSS <a href="https://tailwindcss.com/docs/border-radius" target="_blank" class="link link-primary">Border Radius</a>.

{{< code addClass="flex-col gap-6" >}}

<select class="select max-w-sm rounded-full" aria-label="Pilled select">
  <option disabled selected>Pick your favorite Movie</option>
  <option>The Godfather</option>
  <option>The Shawshank Redemption</option>
  <option>Pulp Fiction</option>
  <option>The Dark Knight</option>
  <option>Schindler's List</option>
</select>

<div class="select-floating max-w-sm">
  <select class="select rounded-full" id="selectFloatingPilled" aria-label="Pilled select">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectFloatingPilled">Pick your favorite Movie</label>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Label and helper text. -->

{{< headname level="3" >}} Label and helper text {{< /headname >}}

Use the `label-text` for the main label and `helper-text` class for helper text.
{{< code >}}

<div class="w-96">
  <label class="label-text" for="selectHelperText"> Pick your favorite Movie </label>
  <select class="select" id="selectHelperText">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <span class="helper-text">Helper text</span>
</div>
{{< /code >}}

<!-- Hidden label -->

{{< headname level="3" >}} Hidden label {{< /headname >}}

`label` elements hidden using the `.sr-only` class.

{{< code >}}

<div class="w-96">
  <div class="label-text sr-only" for="selectHiddenLabel"> Pick your favorite Movie </div>
  <select class="select" id="selectHiddenLabel">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
</div>
{{< /code >}}

<!-- Disabled -->

{{< headname level="3" >}} Disabled {{< /headname >}}

Disable a `select` element by adding the `disabled` attribute, making it non-selectable.

{{< code addClass="!block space-y-4" >}}

<select class="select max-w-sm" aria-label="Disabled select" disabled>
  <option disabled selected>Pick your favorite Movie</option>
  <option>The Godfather</option>
  <option>The Shawshank Redemption</option>
  <option>Pulp Fiction</option>
  <option>The Dark Knight</option>
  <option>Schindler's List</option>
</select>

<div class="select-floating max-w-sm">
  <select class="select" id="selectDisabledFloating" aria-label="Disabled select" disabled>
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
  <label class="select-floating-label" for="selectDisabledFloating">Pick your favorite Movie</label>
</div>
{{< /code >}}

<!-- Datalist -->

{{< headname level="3" >}} Datalist {{< /headname >}}

Associate a `datalist` element with an `input` to provide a list of suggested options, allowing users to select from predefined choices or enter a custom value.

{{< code  addClass="flex-col gap-6" >}}

<div class="flex flex-col max-w-sm">
  <label for="exampleDataList" class="label-text">Datalist example</label>
  <input class="input" list="datalistOptions" id="exampleDataList" placeholder="Type to search..." />
  <datalist id="datalistOptions">
    <option value="San Francisco"></option>
    <option value="New York"></option>
    <option value="Seattle"></option>
    <option value="Los Angeles"></option>
    <option value="Chicago"></option>
  </datalist>
</div>
{{< /code >}}

<!-- Multiple -->

{{< headname level="3" >}} Multiple {{< /headname >}}

Enable the selection of multiple options in a `select` element by adding the `multiple` attribute.

{{< code >}}

<div class="max-w-sm">
  <label class="label-text" for="fav-movies">Pick your favorite Movies:</label>
  <select multiple class="select h-auto" size="4" name="fav-movies" id="fav-movies">
    <option>The Godfather</option>
    <option>The Shawshank Redemption</option>
    <option>Pulp Fiction</option>
    <option>The Dark Knight</option>
    <option>Schindler's List</option>
  </select>
</div>
{{< /code >}}

<!-- Optgroup -->

{{< headname level="3" >}} Optgroup {{< /headname >}}

Utilize the `optgroup` element to group `option` elements together within a `select` dropdown, creating organized sections.

{{< code >}}

<div class="w-96">
  <label class="label-text" for="technologies">Choose a technology:</label>
  <select class="select" name="technologies" id="technologies">
    <optgroup label="Frontend Technologies">
      <option value="html">HTML</option>
      <option value="css">CSS</option>
      <option value="javascript">JavaScript</option>
    </optgroup>
    <optgroup label="Backend Technologies">
      <option value="nodejs">Node.js</option>
      <option value="python">Python</option>
      <option value="java">Java</option>
    </optgroup>
  </select>
</div>
{{< /code >}}
