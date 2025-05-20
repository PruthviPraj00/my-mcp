---
title: "Textarea"
components: 7
description: "A textarea is a multi-line text input field that allows users to enter longer text."
bg_image: "svg/form-elements/textarea.svg"
menu:
  main:
    parent: "forms"

previous: Switch
previousLink: forms/switch/

next: Advanced Select
nextLink: advanced-forms/advanced-select/
---

<!-- Class table -->

{{< class-table >}}
textarea | component | Basic textarea field.
textarea-floating | component | Floating textarea field.
textarea-floating-label | part | Floats the label to the top.
label-text | part | For label.
helper-text | part | For helper text.
is-valid | state | Adds success style to the input.
is-invalid | state | Adds error style to the input.
textarea-xs | size | Extra small Textarea size.
textarea-sm | size | Smaller Textarea size.
textarea-md | size | Medium(default) Textarea size.
textarea-lg | size | Larger Textarea size.
textarea-xl | size | Extra large Textarea size.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic textarea example.

{{< code >}}

<textarea class="textarea max-w-sm" aria-label="Textarea" ></textarea>
{{< /code >}}

<!-- Label and placeholder -->

{{< headname level="3" >}} Label and placeholder {{< /headname >}}

Basic textarea with placeholder.

{{< code >}}

<div class="sm:w-96">
  <label class="label-text" for="textareaLabel"> Your bio </label>
  <textarea class="textarea" placeholder="Hello!!!" id="textareaLabel"></textarea>
</div>
{{< /code >}}

<!-------------------- Type -------------------->

{{< headname level="2" >}} Types {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

{{< code >}}

<textarea class="textarea max-w-sm" placeholder="Hello!!!" ></textarea>
{{< /code >}}

<!-- Floating label -->

{{< headname level="3" >}} Floating label {{< /headname >}}

The `textarea-floating` style is used to define the appearance of the textarea, while the `textarea-floating-label` is the container for the label text.

{{< code addClass="!block" >}}

<div class="textarea-floating sm:w-96">
  <textarea class="textarea" placeholder="Hello!!!" id="textareaFloating"></textarea>
  <label class="textarea-floating-label" for="textareaFloating">Your bio</label>
</div>
{{< /code >}}

<!-------------------- Size -------------------->

{{< headname level="2" >}} Size {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Add responsive class `textarea-{size}` where `{size} = xs|sm|md|lg|xl` for textarea of different sizes.

{{< code addClass="flex-col gap-6" >}}

<textarea class="textarea textarea-xs max-w-sm" placeholder="Hello!!!" ></textarea>

<textarea class="textarea textarea-sm max-w-sm" placeholder="Hello!!!" ></textarea>

<textarea class="textarea max-w-sm" placeholder="Hello!!!" ></textarea>

<textarea class="textarea textarea-lg max-w-sm" placeholder="Hello!!!" ></textarea>

<textarea class="textarea textarea-xl max-w-sm" placeholder="Hello!!!" ></textarea>
{{< /code >}}

<!-- Floating label -->

{{< headname level="3" >}} Floating label {{< /headname >}}

Add responsive class `select-{size}` where `{size} = xs|sm|md|lg|xl` for select of different sizes.

{{< code addClass="flex-col gap-6" >}}

<div class="textarea-floating sm:w-96">
  <textarea class="textarea textarea-xs" placeholder="Hello!!!" id="textareaFloatingExtraSmall"></textarea>
  <label class="textarea-floating-label" for="textareaFloatingExtraSmall">Your bio</label>
</div>

<div class="textarea-floating sm:w-96">
  <textarea class="textarea textarea-sm" placeholder="Hello!!!" id="textareaFloatingSmall"></textarea>
  <label class="textarea-floating-label" for="textareaFloatingSmall">Your bio</label>
</div>

<div class="textarea-floating sm:w-96">
  <textarea class="textarea" placeholder="Hello!!!" id="textareaFloatingMedium"></textarea>
  <label class="textarea-floating-label" for="textareaFloatingMedium">Your bio</label>
</div>

<div class="textarea-floating sm:w-96">
  <textarea class="textarea textarea-lg" placeholder="Hello!!!" id="textareaFloatingLarge"></textarea>
  <label class="textarea-floating-label" for="textareaFloatingLarge">Your bio</label>
</div>

<div class="textarea-floating sm:w-96">
  <textarea class="textarea textarea-xl" placeholder="Hello!!!" id="textareaFloatingExtraLarge"></textarea>
  <label class="textarea-floating-label" for="textareaFloatingExtraLarge">Your bio</label>
</div>
{{< /code >}}

<!-------------------- Textarea group -------------------->
{{< headname level="2" >}} Textarea group {{< /headname >}}

<!-- Leading icons -->

{{< headname level="3" >}} Leading icons {{< /headname >}}

Add a leading icon inside textarea.

{{< code addClass="!flex-col space-y-4"  >}}

<div class="textarea max-w-sm">
  <span class="icon-[tabler--message] text-base-content/80 mt-2 mx-4 size-5 shrink-0"></span>
  <textarea class="grow" placeholder="Hello!!!"></textarea>
</div>

<div class="textarea max-w-sm">
  <span class="icon-[tabler--message] text-base-content/80 mt-2 mx-4 size-5 shrink-0"></span>
  <div class="textarea-floating grow">
    <textarea placeholder="Hello!!!" id="textareaFloatingMedium"></textarea>
    <label class="textarea-floating-label" for="textareaFloatingMedium">Your bio</label>
  </div>
</div>
{{< /code >}}

<!-- Tailing icons -->

{{< headname level="3" >}} Tailing icons {{< /headname >}}

Add a tailing icon inside textarea.

{{< code addClass="!flex-col space-y-4"  >}}

<div class="textarea max-w-sm">
  <textarea class="grow resize-none" placeholder="Hello!!!"></textarea>
  <span class="icon-[tabler--message] text-base-content/80 mt-2 mx-4 size-5 shrink-0"></span>
</div>

<div class="textarea max-w-sm">
  <div class="textarea-floating grow">
    <textarea class="resize-none" placeholder="Hello!!!" id="textareaFloatingMedium"></textarea>
    <label class="textarea-floating-label" for="textareaFloatingMedium">Your bio</label>
  </div>
  <span class="icon-[tabler--message] text-base-content/80 mt-2 mx-4 size-5 shrink-0"></span>
</div>
{{< /code >}}


<!-------------------- Validation states -------------------->

{{< headname level="2" >}} Validation states {{< /headname >}}

<!-- Success state -->

{{< headname level="3" >}} Success state {{< /headname >}}

Success state can be show using `is-valid` class.

{{< code addClass="!block space-y-4" >}}

<!-- Basic -->

<div class="sm:w-96">
  <label class="label-text" for="textareaStateSuccessDefault"> Full Name </label>
  <textarea class="textarea is-valid" placeholder="Hello!!!" id="textareaStateSuccessDefault"></textarea>
  <span class="helper-text">Helper text</span>
</div>

<!-- Floating -->

<div class="textarea-floating sm:w-96">
  <textarea class="textarea is-valid" placeholder="Hello!!!" id="textareaStateSuccessFloating"></textarea>
  <label class="textarea-floating-label" for="textareaStateSuccessFloating">Your bio</label>
  <span class="helper-text">Helper text</span>
</div>
{{< /code >}}

<!-- Error state -->

{{< headname level="3" >}} Error state {{< /headname >}}

Error state can be show using `is-invalid` class.

{{< code addClass="!block space-y-4" >}}

<!-- Basic -->

<div class="sm:w-96">
  <label class="label-text" for="textareaStateErrorDefault"> Full Name </label>
  <textarea class="textarea is-invalid" placeholder="Hello!!!" id="textareaStateErrorDefault"></textarea>
  <span class="helper-text">Helper text</span>
</div>

<!-- Floating -->

<div class="textarea-floating sm:w-96">
  <textarea class="textarea is-invalid" placeholder="Hello!!!" id="textareaStateErrorFloating"></textarea>
  <label class="textarea-floating-label" for="textareaStateErrorFloating">Your bio</label>
  <span class="helper-text">Helper text</span>
</div>
{{< /code >}}

<!-------------------- Illustration -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Hidden label -->

{{< headname level="3" >}} Hidden label {{< /headname >}}

`label` elements hidden using the .sr-only class.

{{< code >}}

<div class="w-full sm:w-96">
  <label class="label-text sr-only" for="textareaHiddenLabel"> Your bio </label>
  <textarea class="textarea" placeholder="Hello!!!" id="textareaHiddenLabel"></textarea>
</div>
{{< /code >}}

<!-- Disable -->

{{< headname level="3" >}} Disable {{< /headname >}}

Add the `disabled` boolean attribute on an textarea to remove pointer events, and prevent focusing.

{{< code addClass="!block space-y-4" >}}

<div class="w-full sm:w-96">
  <label class="label-text sr-only" for="textareaDisabledefault"> Your bio </label>
  <textarea class="textarea" placeholder="Hello!!!" id="textareaDisabledefault" disabled></textarea>
</div>

<div class="textarea-floating sm:w-96">
  <textarea class="textarea" placeholder="Hello!!!" id="textareaDisabledoating" disabled></textarea>
  <label class="textarea-floating-label" for="textareaDisabledoating">Your bio</label>
</div>
{{< /code >}}

<!-- Readonly -->

{{< headname level="3" >}} Readonly {{< /headname >}}

Add the `readonly` boolean attribute on an textarea to prevent modification of the textarea value.

{{< code >}}

<div class="w-full sm:w-96">
  <label class="label-text sr-only" for="textareaReadonly"> Your bio </label>
  <textarea class="textarea" placeholder="Hello!!!" id="textareaReadonly" readonly></textarea>
</div>
{{< /code >}}

<!-- Helper text -->

{{< headname level="3" >}} Helper text {{< /headname >}}

Basic textarea example with helper text and hints.

{{< code addClass="!block space-y-4" >}}

<!-- Basic -->
<div class="w-full sm:w-96">
  <label class="label-text" for="textareaHelperTextDefault"> Full Name </label>
  <textarea class="textarea" placeholder="Hello!!!" id="textareaHelperTextDefault"></textarea>
  <span class="helper-text">Helper text</span>
</div>

<!-- Floating -->
<div class="textarea-floating sm:w-96">
  <textarea class="textarea" placeholder="Hello!!!" id="textareaHelperTextFloating"></textarea>
  <label class="textarea-floating-label" for="textareaHelperTextFloating">Your bio</label>
  <span class="helper-text">Helper text</span>
</div>
{{< /code >}}
