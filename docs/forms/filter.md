---
title: "Filter"
description: "A group of radio buttons that lets you pick one option, hiding the rest, with a reset button to change your choice."
bg_image: "svg/form-elements/filter.svg"
components: 2
tag: "new"
menu:
  main:
    parent: "forms"

previous: File Input
previousLink: forms/file-input/

next: Input
nextLink: forms/input/
---

<!-- Class table -->

{{< class-table >}}

filter | component | Applies to `forms` or `divs` containing radio buttons for item filtering.
filter-reset | part | Reset button alternative for non-form elements.
{{< /class-table >}}


<!-- Filtering with HTML Form: Radio Buttons and Reset Button -->
{{< headname level="3" >}} Filter with HTML form: radio buttons and reset button {{< /headname >}}

A HTML form for filtering with radio buttons and a reset option.

{{< code addClass="justify-center" >}}
<form class="filter">
  <input class="btn btn-square" type="reset" value="×"/>
  <input class="btn" type="radio" name="drink" aria-label="Tea"/>
  <input class="btn" type="radio" name="drink" aria-label="Coffee"/>
  <input class="btn" type="radio" name="drink" aria-label="Smoothie"/>
</form>
{{< /code >}}

<!-- Filter without HTML form -->
{{< headname level="3" >}} Implementing filter without HTML forms {{< /headname >}}

Use this method when HTML forms are not an option.

{{< code addClass="justify-center" >}}
<div class="filter">
  <input class="btn filter-reset" type="radio" name="destination" aria-label="All"/>
  <input class="btn" type="radio" name="destination" aria-label="Jungle"/>
  <input class="btn" type="radio" name="destination" aria-label="Beach"/>
  <input class="btn" type="radio" name="destination" aria-label="Mountain"/>
</div>
{{< /code >}}
