---
title: "Input "
description: "A fundamental tool for receiving user input is a text field, which allows data to be provided or altered using either the keyboard or mouse."
bg_image: "svg/form-elements/input.svg"
components: 30
isLanding: true
menu:
  main:
    parent: "forms"
    
previous: Filter
previousLink: forms/filter/

next: Join
nextLink: forms/join/
---

<!-- Class table -->

{{< class-table >}}

input | component | Base class for form input.
input-floating | component | Base class for floating form input.
input-floating-label | part | Floats the label to the top.
label-text | part | Base class for title label text.
helper-text | part | Base class for helper label text.
no-focus|modifier| remove default focus from input.
is-valid | state | Adds success style to the input.
is-invalid | state | Adds error style to the input.
input-xs | size | Input with Extra small size.
input-sm | size | Input with Smaller size.
input-md | size | Input with medium(default) size.
input-lg | size | Input with Larger size.
input-xl | size | Input with Extra large size.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic examples {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Utilize the `input` component class to style the input.

{{< code >}}

<input type="text" class="input max-w-sm" aria-label="input" />
{{< /code >}}

<!-- Placeholder -->

{{< headname level="3" >}} Placeholder {{< /headname >}}

Basic input with placeholder.

{{< code >}}

<input type="text" placeholder="Type here" class="input max-w-sm" />
{{< /code >}}

<!-- Label and helper text -->

{{< headname level="3" >}} Label and helper text {{< /headname >}}

Please use `label-text` for the label and `helper-text` for the text that appears at the bottom as helper text.

{{< code addClass="flex-col" >}}

<div class="w-96">
  <label class="label-text" for="labelAndHelperText">Full Name</label>
  <input type="text" placeholder="John Doe" class="input" id="labelAndHelperText" />
  <span class="helper-text">Please write your full name</span>
</div>

<div class="w-96">
  <label class="label-text" for="labelAndHelperTextRight">Full Name</label>
  <input type="text" placeholder="John Doe" class="input" id="labelAndHelperTextRight" />
  <span class="helper-text text-end">Please write your full name</span>
</div>
{{< /code >}}

<!-- Hidden label -->

{{< headname level="3" >}} Hidden label {{< /headname >}}

`label` elements hidden using the `.sr-only` class.

{{< code  >}}

<div class="w-96">
  <label class="label-text sr-only" for="hiddenLabel">Full name</label>
  <input type="text" id="hiddenLabel" class="input" placeholder="John Doe" />
</div>
{{< /code >}}

<!-------------------- Types -------------------->

{{< headname level="2" >}} Types {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Default Input.

{{< code >}}

<div class="w-96">
  <label class="label-text" for="defaultInput">Full name</label>
  <input type="text" placeholder="John Doe" class="input" id="defaultInput" />
</div>
{{< /code >}}

<!-- Floating label -->

{{< headname level="3" >}} Floating label {{< /headname >}}

The **Floating Input Component** provides a text input with a floating label. Use `.input-floating` for the wrapper, `.input` for the input field, and `.input-floating-label` for the label.

{{< code >}}

<div class="input-floating w-96">
  <input type="text" placeholder="John Doe" class="input" id="floatingInput" />
  <label class="input-floating-label" for="floatingInput">Full name</label>
</div>
{{< /code >}}


<!-------------------- Size -------------------->

{{< headname level="2" >}} Sizes {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Add responsive class `input-{size}` where `{size} = xs|sm|md|lg|xl` for input of different sizes.

{{< code addClass="flex-col gap-6" >}}

<input type="text" placeholder="John Doe" class="input input-xs max-w-sm" />
<input type="text" placeholder="John Doe" class="input input-sm max-w-sm" />
<input type="text" placeholder="John Doe" class="input max-w-sm" />
<input type="text" placeholder="John Doe" class="input input-lg max-w-sm" />
<input type="text" placeholder="John Doe" class="input input-xl max-w-sm" />
{{< /code >}}

<!-- Floating label -->

{{< headname level="3" >}} Floating label {{< /headname >}}

Add responsive class `input-{size}` where `{size} = xs|sm|md|lg|xl` for input of different sizes for floating label.

{{< code addClass="flex-col gap-6" >}}


<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input input-xs" id="floatingLabelExtraSmall" />
  <label class="input-floating-label" for="floatingLabelExtraSmall">Full name</label>
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input input-sm" id="floatingLabelSmall" />
  <label class="input-floating-label" for="floatingLabelSmall">Full name</label>
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input" id="floatingLabelDefault" />
  <label class="input-floating-label" for="floatingLabelDefault">Full name</label>
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input input-lg" id="floatingLabelLarge" />
  <label class="input-floating-label" for="floatingLabelLarge">Full Name</label>
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input input-xl" id="floatingLabelExtraLarge" />
  <label class="input-floating-label" for="floatingLabelExtraLarge">Full Name</label>
</div>
{{< /code >}}

<!-------------------- Validation State -------------------->

{{< headname level="2" >}} Validation State {{< /headname >}}

<!-- Success state -->

{{< headname level="3" >}} Success state {{< /headname >}}

Success state can be show using `is-valid` class.

{{< code addClass="flex-col gap-6" >}}

<div class="max-w-sm">
  <label class="label-text" for="successInput">Full Name</label>
  <input type="text" placeholder="John Doe" class="input is-valid" id="successInput" />
  <span class="helper-text">Helper text</span>
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input is-valid" id="successFloatingInput" />
  <label class="input-floating-label" for="successFloatingInput">Full name</label>
  <span class="helper-text ps-3">Helper text</span>
</div>
{{< /code >}}

<!-- Error state -->

{{< headname level="3" >}} Error state {{< /headname >}}

Error state can be show using `is-invalid` class.

{{< code addClass="flex-col gap-6" >}}

<div class="max-w-sm">
  <label class="label-text" for="errorInput">Full Name</label>
  <input type="text" placeholder="John Doe" class="input is-invalid" id="errorInput" />
  <span class="helper-text">Helper text</span>
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input is-invalid" id="errorFloatingInput" />
  <label class="input-floating-label" for="errorFloatingInput">Full name</label>
  <span class="helper-text ps-3">Helper text</span>
</div>
{{< /code >}}

<!-------------------- Input Group -------------------->

{{< headname level="2" >}} Input Group {{< /headname >}}

<!-- Inline label -->

{{< headname level="3" >}} Inline label {{< /headname >}}

To create an input group, use `input` as a wrapper. To align the `label` or `icons`, apply the `my-auto` class. This ensures consistent vertical alignment within the group.

{{< code addClass="flex-col gap-6" >}}

<div class="input max-w-sm">
  <label class="label-text my-auto me-3 p-0" for="inlineLabelName">Name</label>
  <input type="text" class="grow" placeholder="FlyonUI" id="inlineLabelName" />
</div>
<div class="input max-w-sm">
  <label class="label-text my-auto me-3 p-0" for="inlineLabelEmail">Email</label>
  <input type="email" class="grow" placeholder="admin@site.com" id="inlineLabelEmail" />
</div>
{{< /code >}}

<!-- Leading icon -->

{{< headname level="3" >}} Leading icon {{< /headname >}}

Add a leading icon inside input.

{{< code addClass="flex-col gap-6" >}}

<div class="input max-w-sm">
  <span class="icon-[tabler--user] text-base-content/80 my-auto me-3 size-5 shrink-0"></span>
  <label class="sr-only" for="leadingIconDefault">Full Name</label>
  <input type="text" class="grow" placeholder="John Doe" id="leadingIconDefault" />
</div>

<div class="input max-w-sm">
  <span class="icon-[tabler--user] text-base-content/80 my-auto size-5 shrink-0"></span>
  <div class="input-floating grow">
    <input type="text" placeholder="John Doe" class="ps-3" id="leadingIconFloating" />
    <label class="input-floating-label" for="leadingIconFloating">Full name</label>
  </div>
</div>
{{< /code >}}

<!-- Trailing icon -->

{{< headname level="3" >}} Trailing icon {{< /headname >}}

Add a trailing icon inside input.

{{< code addClass="flex-col gap-6" >}}

<div class="input max-w-sm">
  <input type="text" class="grow" placeholder="xxxx-xxxx-xxxx-xxxx" id="trailingIconDefault" />
  <label class="sr-only" for="trailingIconDefault">Card Number</label>
  <span class="icon-[tabler--brand-mastercard] text-base-content/80 my-auto ms-3 size-5 shrink-0"></span>
</div>

<div class="input max-w-sm">
  <div class="input-floating grow">
    <input type="text" class="grow" placeholder="xxxx-xxxx-xxxx-xxxx" id="trailingIconFloating" />
    <label class="input-floating-label ms-0" for="trailingIconFloating">Full name</label>
  </div>
  <span class="icon-[tabler--brand-mastercard] text-base-content/80 my-auto ms-3 size-5 shrink-0"></span>
</div>
{{< /code >}}

<!-- Leading and trailing icon -->

{{< headname level="3" >}} Leading and trailing icon {{< /headname >}}

Add a leading and trailing icon inside input.

{{< code >}}

<div class="input max-w-sm space-x-3">
  <span class="label-text my-auto">$</span>
  <input type="number" class="grow" placeholder="00.00" id="trailingAndLeadingInput" />
  <label class="sr-only" for="trailingAndLeadingInput">Enter amount</label>
  <span class="label-text my-auto">USD</span>
</div>
{{< /code >}}

<!-- With keyboard shortcut -->

{{< headname level="3" >}} With keyboard shortcut {{< /headname >}}

Utilizes `kbd` component class with input.

{{< code >}}

<div class="input input-lg flex max-w-sm space-x-4">
  <span class="icon-[tabler--search] text-base-content/80 my-auto size-6 shrink-0"></span>
  <input type="search" class="grow" placeholder="Search" id="kbdInput" />
  <label class="sr-only" for="kbdInput">Search</label>
  <span class="my-auto flex gap-2">
    <kbd class="kbd kbd-sm">⌘</kbd>
    <kbd class="kbd kbd-sm">K</kbd>
  </span>
</div>
{{< /code >}}

<!-- Checkbox and radios -->

{{< headname level="3" >}} Checkbox and radios {{< /headname >}}

Place any checkbox or radio option within an input group’s addon instead of text.

{{< code addClass="flex-col gap-6" >}}

<div class="input max-w-sm">
  <input type="checkbox" class="checkbox checkbox-primary my-auto me-3" />
  <input type="text" class="grow" placeholder="John Doe" />
</div>

<div class="input max-w-sm">
  <input type="radio" name="radio-1" class="radio radio-primary my-auto me-3" />
  <input type="text" class="grow" placeholder="John Doe" />
</div>
{{< /code >}}

<!-- Inline select -->
{{< headname level="3" >}} Inline select {{< /headname >}}

This example demonstrates an inline select component. The `.input` class serves as a wrapper, incorporating `pe-0` for padding reset and `items-center` for vertical alignment. Additionally, `ms-3` is used to manage spacing.  


{{< code >}}

<div class="input items-center pe-0 max-w-sm">
  <input class="grow" placeholder="Search" />
  <select class="select ms-3" aria-label="select">
    <option disabled selected>Filter</option>
    <option>Sci-fi</option>
    <option>Drama</option>
    <option>Action</option>
  </select>
</div>
{{< /code >}}

<!-------------------- Shape -------------------->

{{< headname level="2" >}} Shape {{< /headname >}}

<!-- Pill input -->

{{< headname level="3" >}} Pill input {{< /headname >}}

We can manage the input's radius using the <a href="https://tailwindcss.com/docs/border-radius" target="_blank" class="link link-primary">rounded</a> utility class provided by Tailwind CSS.


{{< code addClass="flex-col gap-6" >}}

<div class="max-w-sm">
  <label class="label-text" for="pillInput">Full Name</label>
  <input type="text" placeholder="John Doe" class="input rounded-full" id="pillInput" />
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input rounded-full" id="pillFloatingInput" />
  <label class="input-floating-label" for="pillFloatingInput">Full name</label>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Helper text -->

{{< headname level="3" >}} Helper text {{< /headname >}}

Implement varying input styles accompanied by helper text.

{{< code addClass="flex-col gap-6" >}}

<div class="space-y-3">
  <div class="relative">
    <label class="label-text" for="helperTextInput">Full Name</label>
    <input type="text" placeholder="John Doe" class="input max-w-sm" id="helperTextInput" />
    <span class="helper-text">Please write your full name</span>
  </div>

  <div class="input-floating max-w-sm">
    <input type="text" placeholder="John Doe" class="input" id="helperTextFloatingInput" />
    <label class="input-floating-label" for="helperTextFloatingInput">Full Name</label>
    <span class="helper-text ps-3">Please write your full name</span>
  </div>
</div>
{{< /code >}}

<!-- No focus -->

{{< headname level="3" >}} No focus {{< /headname >}}

Disable the default focus on the `input` using `no-focus` class when necessary.

{{< code >}}

<input type="text" placeholder="Type here" class="input no-focus border-0 max-w-sm" />
{{< /code >}}


<!-- Disabled -->

{{< headname level="3" >}} Disabled {{< /headname >}}

Add the `disabled` boolean attribute on an input to remove pointer events, and prevent focusing.

{{< code addClass="!block space-y-4" >}}

<div class="w-96">
  <label class="label-text" for="disabledInput"> What is your name? </label>
  <input type="text" placeholder="John Doe" class="input" id="disabledInput" disabled />
</div>

<div class="input-floating max-w-sm">
  <input type="text" placeholder="John Doe" class="input" id="disabledFloatingInput" disabled/>
  <label class="input-floating-label" for="disabledFloatingInput">Full Name</label>
</div>
{{< /code >}}

<!-- Readonly -->

{{< headname level="3" >}} Readonly {{< /headname >}}

Add the `readonly` boolean attribute on an input to prevent modification of the input’s value.

{{< code >}}

<div class="w-96">
  <label class="label-text" for="readonlyInput">What is your name?</label>
  <input type="text" placeholder="John Doe" class="input" id="readonlyInput" readonly />
</div>
{{< /code >}}

<!-------------------- Join -------------------->

{{< headname level="2" >}} Join {{< /headname >}}

<!-- Input with button -->

{{< headname level="3" >}} Input with button {{< /headname >}}

Combine a button with the input field using the `join` method.

{{< callout "info" >}}
Use {{< link link="forms/join/" addClass="link link-primary" >}}Join{{< /link >}} component to combine two components, like an input with a button, button groups, or an input paired with a dropdown.
{{< /callout >}}

{{< code addClass="flex-col gap-6" >}}

<div class="join max-w-sm">
  <input class="input join-item" placeholder="Search" />
  <button class="btn btn-outline btn-secondary join-item">Search</button>
</div>

<div class="join max-w-sm">
  <button class="btn btn-outline btn-secondary join-item">Search</button>
  <input class="input join-item" placeholder="Search" />
</div>
{{< /code >}}

<!-- Input group with button -->

{{< headname level="3" >}} Input group with button {{< /headname >}}

Combine a button with the input input.

{{< code >}}

<div class="join w-96">
  <div class="input join-item flex">
    <span class="icon-[tabler--user] text-base-content/80 my-auto me-3 size-5 shrink-0"></span>
    <label class="sr-only" for="groupInput">Full Name</label>
    <input type="text" class="grow" placeholder="John Doe" id="groupInput" />
  </div>
  <button class="btn btn-outline btn-secondary join-item h-auto">Search</button>
</div>
{{< /code >}}

<!-- Input with select -->

{{< headname level="3" >}} Input with select {{< /headname >}}

Combine a select with the input input.

{{< code >}}

<div class="join w-96">
  <input class="input join-item" placeholder="Search" />
  <select class="select join-item w-36" aria-label="select">
    <option disabled selected>Filter</option>
    <option>Sci-fi</option>
    <option>Drama</option>
    <option>Action</option>
  </select>
</div>
{{< /code >}}
