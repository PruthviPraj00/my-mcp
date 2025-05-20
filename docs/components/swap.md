---
title: "Swap"
components: 6
description: "Swap enables you to toggle the visibility of two elements using either a checkbox or a class name."
bg_image: "svg/components/swap.svg"
menu:
  main:
    parent: "components"

previous: Status
previousLink: components/status/

next: Theme Controller
nextLink: components/theme-controller/

pageJS:
  - "/js/pages/swap.js"
---

<!-- Class table -->

{{< class-table >}}
swap | component | Base class for swap component.
swap-js | component | It targets the swap component working with JS instead of checkbox.
swap-on | part | It targets a child element that should be visible when the checkbox is checked or when the swap component is active.
swap-off | part | It targets a child element that should not be visible when the checkbox is not checked or when the swap component is inactive.
swap-indeterminate | part | It targets a child element that should be visible when checkbox is indeterminate.
swap-flip | style | Adds flip effect to swap content.
swap-rotate | style | Adds rotate effect to swap content.
swap-active | state | Activates the swap (no need for checkbox).
{{< /class-table >}}

<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!--  Swap text  -->

{{< headname level="3" >}} Swap text {{< /headname >}}

Utilize the `swap` component class along with an empty checkbox input and child component classes `swap-off` and `swap-on` to create a swap component.

{{< code >}}

<label class="swap">
  <input type="checkbox" />
  <span class="swap-off">OFF</span>
  <span class="swap-on">ON</span>
</label>
{{< /code >}}

<!--  Swap volume icons  -->

{{< headname level="3" >}} Swap volume icons {{< /headname >}}

Use below given example for volume/mute swap component.

{{< code >}}

<label class="swap">
  <input type="checkbox" />
  <span class="swap-on icon-[tabler--volume] size-6"></span>
  <span class="swap-off icon-[tabler--volume-off] size-6"></span>
</label>
{{< /code >}}

<!--  Swap icons with rotate effect  -->

{{< headname level="3" >}} Swap icons with rotate effect {{< /headname >}}

Apply the modifier class `swap-rotate` to enable a rotate effect for the swap component.

{{< code >}}

<label class="swap swap-rotate">
  <input type="checkbox" />
  <span class="swap-on icon-[tabler--sun] size-6"></span>
  <span class="swap-off icon-[tabler--moon] size-6"></span>
</label>
{{< /code >}}

<!--  Hamburger button  -->

{{< headname level="3" >}} Hamburger button {{< /headname >}}

Use below given example for hamburger button.

{{< code >}}

<label class="btn btn-circle swap swap-rotate">
  <input type="checkbox" />
  <span class="icon-[tabler--menu-2] swap-off"></span>
  <span class="icon-[tabler--x] swap-on"></span>
</label>
{{< /code >}}

<!--  Emotes with flip effect  -->

{{< headname level="3" >}} Emotes with flip effect {{< /headname >}}

Apply the modifier class `swap-flip` to enable a flip effect for the swap component.

{{< code >}}

<label class="swap swap-flip text-6xl">
  <input type="checkbox" />
  <span class="swap-on">😈</span>
  <span class="swap-off">😇</span>
</label>
{{< /code >}}

{{< headname level="2" >}} With JavaScript {{< /headname >}}

<!--  Using class names  -->

{{< headname level="3" >}} Using class names {{< /headname >}}

Utilize the component class `swap-js` to designate a specific swap component for JavaScript functionality, allowing the swap to function without a checkbox. Toggling the modifier class `swap-active` on a click event of the swap component facilitates this behavior.

{{< code jsCode="true" >}}

<label class="swap swap-js text-6xl">
  <span class="swap-on">🥵</span>
  <span class="swap-off">🥶</span>
</label>
<label class="swap swap-js text-6xl">
  <span class="swap-on">🥳</span>
  <span class="swap-off">😭</span>
</label>

<!-- Js -->
<script>
// Swap elements JS code below
const swapElements = document.querySelectorAll('.swap-js')

// Function to handle click event on swap elements
function handleClick(event) {
  // Toggle the 'swap-active' class on the clicked swap element
  event.currentTarget.classList.toggle('swap-active')

  // Get the 'swap-on' and 'swap-off' elements within the current swap element
  const swapOn = event.currentTarget.querySelector('.swap-on')
  const swapOff = event.currentTarget.querySelector('.swap-off')

  // Determine the value based on the presence of 'swap-active' class
  const value = event.currentTarget.classList.contains('swap-active') ? swapOn.innerHTML : swapOff.innerHTML

  // Log the value to the console
  console.log(`Value: ${value}`)
}

// Iterate through each swap element and add click event listener
swapElements.forEach(swapElement => {
  swapElement.addEventListener('click', handleClick)
})

</script>

{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!--  RTL swap  -->

{{< headname level="3" >}} RTL swap {{< /headname >}}

Use below given example for RTL swap.

{{< code >}}

<label class="swap">
  <input type="checkbox" />
  <span class="swap-off font-medium">LTR</span>
  <span class="swap-on font-medium">RTL</span>
</label>
{{< /code >}}

<!--  Play pause button  -->

{{< headname level="3" >}} Play pause button {{< /headname >}}

Use below given example for play-pause button.

{{< code >}}

<label class="btn btn-circle swap swap-rotate">
  <input type="checkbox" />
  <span class="icon-[tabler--player-play] swap-off"></span>
  <span class="icon-[tabler--player-pause] swap-on"></span>
</label>
{{< /code >}}
