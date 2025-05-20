---
title: "File input"
components: 5
description: "File inputs enable users to choose files from their device, allowing them to upload documents, images, or other types of files."
bg_image: "svg/form-elements/file-input.svg"
menu:
  main:
    parent: "forms"

previous: Checkbox
previousLink: forms/checkbox/

next: Filter
nextLink: forms/filter/
---

<!-- Class table -->

{{< class-table >}}
input | component | Base class for form input.
input-floating | component | Base class for floating form input.
label-text | part | Base class for title label text.
input-floating-label | part | Floats the label to the top.
helper-text | part | Base class for helper label text.
is-valid | state | Adds success style to the input.
is-invalid | state | Adds error style to the input.
file:{tw-utility-class} | modifier | Adds tailwind classes to update file input.
input-xs | size | Input with Extra small size.
input-sm | size | Input with Smaller size.
input-md | size | Input with medium(default) size.
input-lg | size | Input with Larger size.
input-xl | size | Input with Extra large size.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!--  Default  -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic file input example.

{{< code >}}
<input type="file" class="input max-w-sm" aria-label="file-input" />
{{< /code >}}

<!--  Label  -->

{{< headname level="3" >}} Label {{< /headname >}}

Basic file input example with label.

{{< code addClass="!block" >}}

<div class="max-w-sm">
  <label class="label-text" for="fileInputLabel"> Pick a file </label>
  <input type="file" class="input" id="fileInputLabel" />
</div>
{{< /code >}}

<!-------------------- Size -------------------->

{{< headname level="2" >}} Size {{< /headname >}}

<!--  File input sizes  -->

{{< headname level="3" >}} File input sizes {{< /headname >}}

Add responsive class `input-{size}` where `{size} = xs|sm|md|lg|xl` for file input of different sizes.

{{< code addClass="flex-col gap-6" >}}
<input type="file" class="input max-w-sm input-xs" aria-label="file-input" />
<input type="file" class="input max-w-sm input-sm" aria-label="file-input" />
<input type="file" class="input max-w-sm" aria-label="file-input" />
<input type="file" class="input max-w-sm input-lg" aria-label="file-input" />
<input type="file" class="input max-w-sm input-xl" aria-label="file-input" />
{{< /code >}}

<!-------------------- Types -------------------->

{{< headname level="2" >}} Types {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Default type.

{{< code  addClass="!block" >}}

<div class="max-w-sm">
  <label class="label-text" for="inpuFileTypeDefault"> Pick a file </label>
  <input type="file" class="input" id="inpuFileTypeDefault" />
</div>
{{< /code >}}

<!-- Floating label -->

{{< headname level="3" >}} Floating label {{< /headname >}}

Floating label example.

{{< code  addClass="!block" >}}

<div class="max-w-sm input-floating">
  <input type="file" placeholder="John Doe" class="input" id="inpuFileTypeFloating" />
  <label class="input-floating-label" for="inpuFileTypeFloating">Upload</label>
</div>
{{< /code >}}

<!-------------------- Validation states -------------------->

{{< headname level="2" >}} Validation states {{< /headname >}}

<!-- Success state -->

{{< headname level="3" >}} Success state {{< /headname >}}

Success state can be show using `is-valid` class.

{{< code addClass="flex-col" >}}

<div class="max-w-sm">
  <label class="label-text" for="fileInputStateSuccess"> Pick a file </label>
  <input type="file" class="input is-valid" id="fileInputStateSuccess" />
  <span class="helper-text">Helper text</span>
</div>
<div class="input-floating max-w-sm">
  <input type="file" placeholder="John Doe" class="input is-valid" id="fileInputStateSuccessFloating" />
  <label class="input-floating-label" for="fileInputStateSuccessFloating">Upload</label>
 <span class="helper-text">Helper text</span>
</div>
{{< /code >}}

<!-- Error state -->

{{< headname level="3" >}} Error state {{< /headname >}}

Error state can be show using `is-invalid` class.

{{< code addClass="flex-col" >}}

<div class="max-w-sm">
  <label class="label-text" for="fileInputStateError"> Pick a file </label>
  <input type="file" class="input is-invalid" id="fileInputStateError" />
  <span class="helper-text">Helper text</span>
</div>
<div class="input-floating max-w-sm">
  <input type="file" placeholder="John Doe" class="input is-invalid" id="fileInputStateErrorFloating" />
  <label class="input-floating-label" for="fileInputStateErrorFloating">Upload</label>
  <span class="helper-text">Helper text</span>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!--  File input with button  -->

{{< headname level="3" >}} File input with button {{< /headname >}}

The `file:` prefix in Tailwind allows us to style the `::file-selector-button`, and it can be combined with the `btn` class.

{{< code >}}
<input type="file" class="block cursor-pointer text-sm file:uppercase file:text-bg-primary file:px-4 file:h-9.5 file:rounded-field cursor-pointer file:font-medium file:text-base file:me-3" aria-label="file-input" />
{{< /code >}}

<!--  Disabled  -->

{{< headname level="3" >}} Disabled {{< /headname >}}

Add the `disabled` boolean attribute on an file input to remove pointer events, and prevent focusing.

{{< code >}}
<input type="file" class="input max-w-sm" aria-label="file-input" disabled />
{{< /code >}}

<!--  Helper text and label  -->

{{< headname level="3" >}} Helper text and label {{< /headname >}}

Placement of helper text and label.

{{< code  addClass="!block" >}}

<div class="max-w-sm">
  <label class="label-text" for="fileInputHelperText"> Pick a file </label>
  <input type="file" class="input" id="fileInputHelperText" />
  <span class="helper-text">Helper text</span>
</div>
{{< /code >}}

<!--  Multiple files  -->

{{< headname level="3" >}} Multiple files {{< /headname >}}

Add `multiple` attribute to select more then 1 file.

{{< code >}}

<input type="file" class="input max-w-sm" aria-label="file-input" multiple />
{{< /code >}}

<!-- Avatar -->

{{< headname level="3" >}} Avatar {{< /headname >}}

The following example showcases a file input with an avatar.

{{< code >}}

<div class="flex items-center gap-2 max-sm:flex-wrap">
  <div class="avatar">
    <div class="size-14 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="Avatar" />
    </div>
  </div>
  <input type="file" class="file:text-bg-primary file:px-4 file:h-9.5 cursor-pointer file:font-medium file:text-base block text-sm file:me-3 file:rounded-full file:uppercase" aria-label="file-input" />
</div>
{{< /code >}}
