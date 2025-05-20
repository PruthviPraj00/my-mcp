---
title: "Modal"
description: "A modal serves the purpose of presenting a dialog or box upon clicking a button."
bg_image: "svg/overlays/modal.svg"
components: 27
isLanding: true
menu:
  main:
    parent: "overlays"

previous: Dropdown
previousLink: overlays/dropdown/

next: Popover
nextLink: overlays/popover/

requires_js: true
pageJS:
  - "/js/pages/modal.js"
---

{{< callout "info" >}}
Modal components are adopted from <a href="https://preline.co/docs/modal.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class table -->

{{< class-table >}}
overlay | component | Create an overlay initalize instance.
modal | component | Provides structure and styling for the modal component.
modal-dialog | part | Base class for modal content container.
modal-content | part | Base class for modal content.
modal-header | part | Adds basic style modal header.
modal-title | part | Adds basic style for modal title.
modal-body | part | Adds basic style for modal body.
modal-footer | part | Adds basic style for modal footer.
overlay-animation-target|modifier| Defines an element within the popup. Once the animation of this element is complete, the popup will be fully hidden. This function does not take any parameters.
overlay-open:{tw-utility-class} | variant | Defines classes will be applied to any elements inside the overlay when the it is open.
overlay-backdrop-open:{tw-utility-class} | variant | Defines classes will be applied to backdrop when the overlay is open.
overlay-layout-open:{tw-utility-class} | variant | Defines classes will be applied to any elements inside the body tag when the overlay is open.
modal-dialog-sm | size | Added to modal-dialog for small sized modal.
modal-dialog-md | size | Added to modal-dialog for medium (Default) sized modal.
modal-dialog-lg | size | Added to modal-dialog for large sized modal.
modal-dialog-xl | size | Added to modal-dialog for extra large sized modal.
modal-top-start | placement | Moves the modal to top-start position.
modal-top | placement | Moves the modal to top-center position.
modal-top-end | placement | Moves the modal to top-end position.
modal-middle-start | placement | Moves the modal to middle-start position.
modal-middle | placement | Moves the modal to middle-center position.
modal-middle-end | placement | Moves the modal to middle-end position.
modal-bottom-start | placement | Moves the modal to bottom-start position.
modal-bottom | placement | Moves the modal to bottom-center position.
modal-bottom-end | placement | Moves the modal to bottom-end position.
{{< /class-table >}}

<!-------------------- Basic examples -------------------->

{{< headname level="2" >}} Basic examples {{< /headname >}}

<!--  Default  -->

{{< headname level="3" >}} Default {{< /headname >}}

Utilize the class `overlay` as the target for JavaScript to address the overlay component, and use the class `modal` for the overlay container. Use the Tailwind CSS display utility class `hidden` to keep the modal container hidden until it is opened.

Add modifier class `overlay-open:` with opacity class `opacity-100` to both overlay container & component class `modal-dialog` so that it shows modal when opened.

Assign the value of the `data-overlay` attribute in any button to the `id` of the targeted overlay component, triggering the modal to appear upon being clicked.

The modal structure consists of the component class `modal-dialog`, which serves as the container for the modal content. Within this container, the component class `modal-content` encapsulates all the content of the modal.

This content is further styled using modifier classes such as `modal-header`, `modal-title`, `modal-body` and `modal-footer`, which collectively define the entire structure of the modal.

Utilize the provided example for basic modal.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="basic-modal" data-overlay="#basic-modal" > Open modal </button>

<div id="basic-modal" class="overlay modal overlay-open:opacity-100 hidden overlay-open:duration-300" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#basic-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#basic-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Fullscreen  -->

{{< headname level="3" >}} Fullscreen {{< /headname >}}

Utilize the provided example for a full screen modal.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="fullscreen-modal"  data-overlay="#fullscreen-modal">Fullscreen modal</button>

<div id="fullscreen-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 max-w-none">
    <div class="modal-content h-full max-h-none justify-between">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#fullscreen-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body grow">
        <p>
          This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in
          the modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal
          and demonstrating the overflow scrolling. When content becomes longer than the height of the viewport,
          scrolling will move the modal as needed.
        </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#fullscreen-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Transparent  -->

{{< headname level="3" >}} Transparent {{< /headname >}}

Utilize the provided example for a transparent modal.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="transparent-modal" data-overlay="#transparent-modal">Transparent modal</button>

<div id="transparent-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden place-items-center" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content text-base-content bg-transparent shadow-none">
      <div class="modal-header">
        <h3 class="modal-title text-base-content">Dialog Title</h3>
        <button type="button" class="btn btn-soft btn-circle absolute top-3 end-3" aria-label="Close" data-overlay="#transparent-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-overlay="#transparent-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Sizes -------------------->

{{< headname level="2" >}} Sizes {{< /headname >}}

<!--  Size variants  -->

{{< headname level="3" >}} Size variants {{< /headname >}}

Use the responsive classes `modal-dialog-{size}` with the `modal-dialog` component class to designate small, large, and extra-large modal sizes, where `{size}` can be replaced with `sm`, `lg`, or `xl`.

Utilize the provided example for a different sized modals.

{{< code >}}

<!-- Small Modal -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="small-modal" data-overlay="#small-modal">Small</button>

<div id="small-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 modal-dialog-sm">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#small-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <p> This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling will move the modal as needed. </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#small-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Default Modal -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="default-modal" data-overlay="#default-modal">Default</button>

<div id="default-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#default-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <p> This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling will move the modal as needed. </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#default-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Large Modal -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="large-modal" data-overlay="#large-modal">Large</button>

<div id="large-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 modal-dialog-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#large-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <p> This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling will move the modal as needed. </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#large-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Extra large modal -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="extra-large-modal" data-overlay="#extra-large-modal">Extra large</button>

<div id="extra-large-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 modal-dialog-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button
          type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#extra-large-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <p> This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling will move the modal as needed. </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#extra-large-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Animated modals -------------------->

{{< headname level="2" >}} Animated modals {{< /headname >}}

<!--  Slide up modal  -->

{{< headname level="3" >}} Slide up modal {{< /headname >}}

Use the `overlay-open:` modifier class along with margin utility classes to create modals with animation. Implement the provided example for a modal with a slide-up animation.

Apply the `overlay-animation-target` class to the target element to track its animation. The plugin will monitor all transitions of these elements and wait until they are complete before hiding the popup.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="slide-up-animated-modal" data-overlay="#slide-up-animated-modal">Open modal</button>

<div id="slide-up-animated-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="overlay-animation-target modal-dialog overlay-open:mt-4 overlay-open:opacity-100 overlay-open:duration-300 mt-12 transition-all ease-out" >
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#slide-up-animated-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#slide-up-animated-modal">
          Close
        </button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Slide down modal  -->

{{< headname level="3" >}} Slide down modal {{< /headname >}}

Utilize the provided example for modal with slide down animation.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="slide-down-animated-modal" data-overlay="#slide-down-animated-modal">Open modal</button>

<div id="slide-down-animated-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:mt-12 overlay-open:opacity-100 overlay-open:duration-300 transition-all ease-out" >
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#slide-down-animated-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#slide-down-animated-modal">
          Close
        </button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Scrolling behavior -------------------->

{{< headname level="2" >}} Scrolling behavior {{< /headname >}}

<!--  Inside body  -->

{{< headname level="3" >}} Inside body {{< /headname >}}

Utilize the given example to create a modal content that allows scrolling within its body.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="scroll-inside-modal" data-overlay="#scroll-inside-modal" > Inside body </button>

<div id="scroll-inside-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#scroll-inside-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <p class="text-justify">
          Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam.
          Morbi leo risus, porta ac consectetur ac, vestibulum at eros.Praesent commodo cursus magna, vel scelerisque
          nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctorAenean lacinia
          bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed
          odio dui. Donec ullamcorper nulla non metus auctor fringilla.Cras mattis consectetur purus sit amet fermentum.
          Cras justo odio, dapibus ac facilisis in, egestas eget quam.
          <br />
          Morbi leo risus, porta ac consectetur ac, vestibulum at eros.Praesent commodo cursus magna, vel scelerisque
          nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.Aenean lacinia
          bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed
          odio dui. Donec ullamcorper nulla non metus auctor fringilla.Cras mattis consectetur purus sit amet fermentum.
          Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac,
          vestibulum at eros.raesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus
          vel augue laoreet rutrum faucibus dolor auctor.Aenean lacinia bibendum nulla sed consectetur.
          <br />
          Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper
          nulla non metus auctor fringilla.Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac
          facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.Praesent commodo
          cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus
          dolor auctor.lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl
          consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.Cras mattis consectetur
          purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam.
          <br />
          Morbi leo risus, porta ac consectetur ac, vestibulum at eros.Praesent commodo cursus magna, vel scelerisque
          nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.Aenean lacinia
          bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed
          odio dui. Donec ullamcorper nulla non metus auctor fringilla.Cras mattis consectetur purus sit amet fermentum.
          Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac,
          vestibulum at eros.Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus
          vel augue laoreet rutrum faucibus dolor auctor.Aenean lacinia bibendum nulla sed consectetur. Praesent commodo
          cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus
          auctor fringilla.
        </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#scroll-inside-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Inside viewport  -->

{{< headname level="3" >}} Inside viewport {{< /headname >}}

Utilize the provided example to implement modal content that remains within the viewport while scrolling.

The JavaScript part is necessary if you want the modal to close when clicking on the backdrop.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="scroll-inside-view-modal" data-overlay="#scroll-inside-view-modal">Inside viewport</button>

<div id="scroll-inside-view-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 pointer-events-auto hidden overflow-y-auto overflow-x-hidden" onclick="backdropClose(this)" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content max-h-none">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#scroll-inside-view-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <p class="text-justify">
          Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam.
          Morbi leo risus, porta ac consectetur ac, vestibulum at eros.Praesent commodo cursus magna, vel scelerisque
          nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctorAenean lacinia
          bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed
          odio dui. Donec ullamcorper nulla non metus auctor fringilla.Cras mattis consectetur purus sit amet fermentum.
          Cras justo odio, dapibus ac facilisis in, egestas eget quam.<br />Morbi leo risus, porta ac consectetur ac,
          vestibulum at eros.Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus
          vel augue laoreet rutrum faucibus dolor auctor.Aenean lacinia bibendum nulla sed consectetur. Praesent commodo
          cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus
          auctor fringilla.Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in,
          egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.raesent commodo cursus magna,
          vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor
          auctor.Aenean lacinia bibendum nulla sed consectetur.<br />Praesent commodo cursus magna, vel scelerisque nisl
          consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.Cras mattis consectetur
          purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta
          ac consectetur ac, vestibulum at eros.Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
          Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.lacinia bibendum nulla sed consectetur.
          Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper
          nulla non metus auctor fringilla.Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac
          facilisis in, egestas eget quam.<br />Morbi leo risus, porta ac consectetur ac, vestibulum at eros.Praesent
          commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum
          faucibus dolor auctor.Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel
          scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.Cras
          mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam.
          Morbi leo risus, porta ac consectetur ac, vestibulum at eros.Praesent commodo cursus magna, vel scelerisque
          nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.Aenean lacinia
          bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed
          odio dui. Donec ullamcorper nulla non metus auctor fringilla.
        </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#scroll-inside-view-modal">
          Close
        </button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
<!-- Js -->
<script>
  function backdropClose(element) {
    const backdrop = document.querySelector(`#${element.id}-backdrop`) 
    if (backdrop) {
      backdrop.click()
    }
}
</script>
{{< /code >}}

<!-------------------- Placement -------------------->

{{< headname level="2" >}} Placement {{< /headname >}}

<!--  Positions  -->

{{< headname level="3" >}} Positions {{< /headname >}}

Utilize the responsive classes `modal-{position}` to position the modal in various positions, where `{position}` can be replaced with `top-start`, `top`, `top-end`, `middle-start`, `middle`, `middle-end`, `bottom-start`, `bottom`, or `bottom-end`.

Utilize the provided examples for placing modal in top-start, top(default) or top-end position.

<!--  Top  -->

{{< headname level="4" >}} Top {{< /headname >}}

{{< code >}}

<!-- Top Start -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="top-start-modal" data-overlay="#top-start-modal">Top start</button>

<div id="top-start-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-top-start hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#top-start-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#top-start-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Top Center (Default) -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="top-center-modal" data-overlay="#top-center-modal">Top center (default)</button>

<div id="top-center-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-top-center hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#top-center-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#top-center-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Top End -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="top-end-modal" data-overlay="#top-end-modal">Top end</button>

<div id="top-end-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-top-end hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#top-end-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#top-end-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Middle  -->

{{< headname level="4" >}} Middle {{< /headname >}}

Utilize the provided examples for placing modal in middle-start, middle or middle-end position.

{{< code >}}

<!-- Middle Start -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="middle-start-modal" data-overlay="#middle-start-modal">Middle start</button>

<div id="middle-start-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-middle-start hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#middle-start-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#middle-start-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Middle Center -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="middle-center-modal" data-overlay="#middle-center-modal">Middle center</button>

<div id="middle-center-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-middle hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#middle-center-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#middle-center-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Middle End -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="middle-end-modal" data-overlay="#middle-end-modal">Middle end</button>

<div id="middle-end-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-middle-end hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#middle-end-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#middle-end-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Bottom  -->

{{< headname level="4" >}} Bottom {{< /headname >}}

Utilize the provided examples for placing modal in bottom-start, bottom or bottom-end position.

{{< code >}}

<!-- Bottom Start -->

<button type="button" class="btn btn-primary"  aria-haspopup="dialog" aria-expanded="false" aria-controls="bottom-start-modal" data-overlay="#bottom-start-modal">Bottom start</button>

<div id="bottom-start-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-bottom-start hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#bottom-start-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#bottom-start-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Bottom Center -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="bottom-center-modal" data-overlay="#bottom-center-modal">Bottom center</button>

<div id="bottom-center-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-bottom hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#bottom-center-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#bottom-center-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Bottom End -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="bottom-end-modal" data-overlay="#bottom-end-modal">Bottom end</button>

<div id="bottom-end-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-bottom-end hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#bottom-end-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#bottom-end-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!--  Toggle between modals  -->

{{< headname level="3" >}} Toggle between modals {{< /headname >}}

Utilize the provided example to implement modals that can be toggled between one another.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="toggle-bn-first-modal" data-overlay="#toggle-bn-first-modal">Toggle between Modals</button>

<!-- Modal 1 -->

<div id="toggle-bn-first-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:mt-12 overlay-open:opacity-100 overlay-open:duration-300 transition-all ease-out" >
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">First modal</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#toggle-bn-first-modal" data-overlay-close>
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="toggle-bn-second-modal" data-overlay="#toggle-bn-second-modal">
          Open second modal
        </button>
      </div>
    </div>
  </div>
</div>

<!-- Modal 2 -->

<div id="toggle-bn-second-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:mt-12 overlay-open:opacity-100 overlay-open:duration-300 transition-all ease-out" >
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Second modal</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#toggle-bn-second-modal" data-overlay-close>
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="toggle-bn-first-modal" data-overlay="#toggle-bn-first-modal">Back to first</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Modal with form  -->

{{< headname level="3" >}} Modal with form {{< /headname >}}

Utilize the provided example to implement modal with form.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="form-modal" data-overlay="#form-modal">Modal with form</button>

<div id="form-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">User details</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#form-modal"><span class="icon-[tabler--x] size-4"></span></button>
      </div>
      <form>
        <div class="modal-body pt-0">
          <div class="mb-4">
            <label class="label-text" for="fullName"> Full Name </label>
            <input type="text" placeholder="John Doe" class="input" id="fullName" />
          </div>
          <div class="mb-0.5 flex gap-4 max-sm:flex-col">
            <div class="w-full">
              <label class="label-text" for="email"> Email </label>
              <input type="email" placeholder="johndoe@123@gmail.com" class="input" id="email" />
            </div>
            <div class="w-full">
              <label class="label-text" for="dateOfBirth"> DOB </label>
              <input type="date" class="input" id="dateOfBirth" />
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-soft btn-secondary" data-overlay="#form-modal">Close</button>
          <button type="submit" class="btn btn-primary">Save changes</button>
        </div>
      </form>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Video modal (YouTube)  -->

{{< headname level="3" >}} Video modal (YouTube) {{< /headname >}}

Utilize the provided example to incorporate a modal featuring a YouTube video.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="video-modal" data-overlay="#video-modal">Open modal</button>

<div id="video-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-body rounded-lg p-0">
        <iframe src="https://www.youtube.com/embed/EngW7tLk6R8?privacy-enhanced=true" class="aspect-video h-96 w-full"></iframe>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Responsive  -->

{{< headname level="3" >}} Responsive {{< /headname >}}

Use TailwindCSS classes for <a href="https://tailwindcss.com/docs/responsive-design#targeting-a-breakpoint-range" target="_blank" class="link link-primary">responsive design</a>, such as `sm:`, `md:`, `lg:`, `xl:`, and `2xl:`, along with the responsive class `modal-{position}` or `modal-{size}`, to switch the modal position or change sizes at specific breakpoints.

Utilize the provided example for a responsive modal that moves to bottom position after small breakpoint.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="responsive-modal" data-overlay="#responsive-modal">Responsive modal</button>

<div id="responsive-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 sm:modal-bottom hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#responsive-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#responsive-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Destroy/Reinitialize  -->

{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}

The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a modal element.

{{< code jsCode="true" addClass="!block" >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="destroy-modal" data-overlay="#destroy-modal">Open modal</button>

<div id="destroy-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#destroy-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#destroy-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
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
  window.addEventListener('load', function () {
    ;(function () {
      const modal = document.querySelector('#destroy-modal')
      const destroy = document.querySelector('#destroy-btn')
      const reinit = document.querySelector('#reinit-btn')

      destroy.addEventListener('click', () => {
        const { element } = HSOverlay.getInstance(modal, true)

        element.destroy()

        destroy.setAttribute('disabled', 'disabled')
        reinit.removeAttribute('disabled')
      })

      reinit.addEventListener('click', () => {
        HSOverlay.autoInit()

        reinit.setAttribute('disabled', 'disabled')
        destroy.removeAttribute('disabled')
      })
    })()
  })
</script>  
{{< /code >}}

<!-------------------- Options usage -------------------->

{{< headname level="2" >}} Options usage {{< /headname >}}

<!--  Stacked overlays  -->

{{< headname level="3" >}} Stacked overlays {{< /headname >}}

In the trigger button, assign the value of the `data-overlay-options` attribute as an object. Within this object, set the `isClosePrev` key to `false` to keep the previous modal open, and set it to `true` to close the previous modal.

Utilize the provided example for stacked modals (overlays). In this scenario, the first two modals will close upon opening the third stacked modal, as `isClosePrev` is set to `true` for it which will close previous modals.

<!-- In the trigger button, assign the `data-overlay-options` attribute as an object. Set the `isClosePrev` key to `false` to keep the previous modal open or `true` to close it. For stacked modals, as shown in the example, the first two modals will close when the third is opened, since `isClosePrev` is set to `true`.

Use `[--has-dynamic-z-index:*]` to ensure each new modal receives an incremented z-index, appearing above previous modals. -->

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="stacked-modal-1" data-overlay="#stacked-modal-1">Stacked overlays</button>

<!-- Modal 1 -->

<div id="stacked-modal-1" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-middle hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 modal-dialog-sm mt-36">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Modal 1</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#stacked-modal-1">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="stacked-modal-2" data-overlay="#stacked-modal-2" data-overlay-options='{ "isClosePrev": false }' >
          Open modal 2
        </button>
      </div>
    </div>
  </div>
</div>

<!-- Modal 2 (stacked) -->

<div id="stacked-modal-2" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-middle hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 modal-dialog-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Modal 2</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#stacked-modal-2">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="stacked-modal-3" data-overlay="#stacked-modal-3" data-overlay-options='{ "isClosePrev": true }' >
          Open modal 3
        </button>
      </div>
    </div>
  </div>
</div>

<!-- Modal 3 (stacked) -->

<div id="stacked-modal-3" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 modal-middle hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 modal-dialog-xl -mt-36">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Modal 3</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#stacked-modal-3">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-overlay="#stacked-modal-3">Close modal 3</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Focus management  -->

{{< headname level="3" >}} Focus management {{< /headname >}}

Utilize the `[--has-autofocus:{boolean}]` option to manage autofocus within any modal. When set to `false`, it prevents the `autofocus` attribute from automatically assigning focus to any element within the modal. By default, its value is `true`.

Examine the provided example for focus management in modals.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="focus-modal" data-overlay="#focus-modal" > Modal with focus </button>

<div id="focus-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden [--has-autofocus:false]" role="dialog" tabindex="-1" >
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#focus-modal" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <form>
        <div class="modal-body pt-0">
          <div class="mb-4">
            <label class="label-text" for="modalFullName"> Full Name </label>
            <input type="text" placeholder="John Doe" class="input" id="modalFullName" autofocus="" />
          </div>
          <div class="mb-0.5">
            <label class="label-text" for="modalEmail"> Email </label>
            <input type="email" placeholder="johndoe@123@gmail.com" class="input" id="modalEmail" />
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-soft btn-secondary" data-overlay="#focus-modal">Close</button>
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </form>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Tab accessibility  -->

{{< headname level="3" >}} Tab accessibility {{< /headname >}}

Use the `[--tab-accessibility-limited:{boolean}]` option to manage <kbd class="kbd kbd-sm">Tab</kbd> accessibility within overlay components. When set to `false`, it permits <kbd class="kbd kbd-sm">Tab</kbd> navigation outside the modal to the entire browser, whereas when set to `true`, it confines <kbd class="kbd kbd-sm">Tab</kbd> access within the modal only. By default, its value is `true`.

Examine the provided example for tab accessibility in modals.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="tab-modal" data-overlay="#tab-modal">Modal tab accessibility</button>

<div id="tab-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden [--tab-accessibility-limited:false]" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#tab-modal"><span class="icon-[tabler--x] size-4"></span></button>
      </div>
      <form>
        <div class="modal-body">
          <div class="mb-4">
            <label class="label-text" for="modalTabFullName"> Full Name </label>
            <input type="text" placeholder="John Doe" class="input" id="modalTabFullName" />
          </div>
          <div class="mb-0.5">
            <label class="label-text" for="modalTabEmail"> Email </label>
            <input type="email" placeholder="john@123@gmail.com" class="input" id="modalTabEmail" />
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-soft btn-secondary" data-overlay="#tab-modal">Close</button>
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </form>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Body scroll  -->

{{< headname level="3" >}} Body scroll {{< /headname >}}

Utilize the `[--body-scroll:{boolean}]` option to control the scrolling behavior of the layout beneath the overlay component. When set to `true`, it enables scrolling of the body, whereas when set to `false`, it disables body scrolling. By default, its value is `false`.

Examine the provided example for body scroll behavior in overlays.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="body-scroll-modal" data-overlay="#body-scroll-modal">Modal with body scroll</button>

<div id="body-scroll-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden [--body-scroll:true]" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#body-scroll-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <p class="text-justify">
          This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in
          the modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal
          and demonstrating the overflow scrolling. When content becomes longer than the height of the viewport,
          scrolling will move the modal as needed.
        </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#body-scroll-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Autohide  -->

{{< headname level="3" >}} Autohide {{< /headname >}}

Utilize the `[--auto-hide:{number}]` option to enable the modal to automatically close itself after a specified duration of `{number}` milliseconds. Setting it to `0` will disable auto-closing. By default, its value is `0`.

Examine the provided example for auto closing modal.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="autohide-modal" data-overlay="#autohide-modal">Auto hide modal</button>

<div id="autohide-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden [--auto-hide:2000]" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#autohide-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body pb-6">This modal will close automatically in <span class="text-2xl">2</span> seconds.</div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Custom backdrop  -->

{{< headname level="3" >}} Custom backdrop {{< /headname >}}

For customizing the backdrop, there are two methods available:

The first method involves using the backdrop modifier class `overlay-backdrop-open:{custom-color}`, where you can specify any color for the backdrop.

The second method entails assigning an object value to the `data-overlay-options` attribute in the trigger button. Within this object, set the `backdropClasses` key to `transition duration-300 fixed inset-0 bg-success/70 overlay-backdrop` to replace the existing backdrop classes with these customized ones.

To add additional classes to `backdropClasses`, use `backdropExtraClasses`. This will append the extra classes to the existing `backdropClasses`.

Examine the provided examples demonstrating both methods for setting the backdrop.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="custom-backdrop-modal" data-overlay="#custom-backdrop-modal">Method 1</button>

<!-- Method 1 -->

<div id="custom-backdrop-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 overlay-backdrop-open:bg-primary/30 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#custom-backdrop-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#custom-backdrop-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="custom-backdrop-modal-2" data-overlay="#custom-backdrop-modal-2" data-overlay-options='{ "backdropClasses": "transition duration-300 fixed inset-0 bg-success/30 overlay-backdrop" }'> Method 2</button>

<!-- Method 2 -->

<div id="custom-backdrop-modal-2" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#custom-backdrop-modal-2">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#custom-backdrop-modal-2">
          Close
        </button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Keyboard control  -->

{{< headname level="3" >}} Keyboard control {{< /headname >}}

Set the value of the `data-overlay-keyboard` attribute to `false` to disable the modal from closing when the <kbd class="kbd kbd-sm">Esc</kbd> key is pressed. By default, this attribute's value is `true`.

Examine the below given example for keyboard control in modals.

{{< code >}}

<button type="button" class="btn btn-primary"  aria-haspopup="dialog" aria-expanded="false" aria-controls="key-control-modal" data-overlay="#key-control-modal">Open modal</button>

<div id="key-control-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" data-overlay-keyboard="false" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#key-control-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        If the <code>data-overlay-keyboard</code> attribute is set to <code>false</code>, pressing the
        <kbd class="kbd kbd-sm">Esc</kbd> key will not close this modal.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#key-control-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Layout affect  -->

{{< headname level="3" >}} Layout affect {{< /headname >}}

Utilize the `[--is-layout-affect:{boolean}]` option to inform plugin that overlay instance will affect site layout ..ie, it adds class `overlay-body-open` to the `<body>` of site if `true`. By default, its value is `false`.

When `[--is-layout-affect:true]`, the overlay plugin enables customization of other layout components that are not part of the overlay component. This can be achieved by using the modifier class `overlay-layout-open:{tw-utility-class}`, where any custom class specified will be applied to the layout component when the overlay component is open.

Refer below example for layout affect in overlays.

{{< code >}}

<button type="button" class="btn btn-primary overlay-layout-open:bg-green-500 overlay-layout-open:border-green-500"  aria-haspopup="dialog" aria-expanded="false" aria-controls="layout-affect-modal" data-overlay="#layout-affect-modal" > Open modal</button>

<div id="layout-affect-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden [--is-layout-affect:true]" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#layout-affect-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        When this modal is opened, the button that triggers it will change to the success color.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#layout-affect-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Hidden class  -->

{{< headname level="3" >}} Hidden class {{< /headname >}}

In the trigger button, set the value of the `data-overlay-options` attribute to an object. Inside this object, specify the `hiddenClass` key as `custom-class`, which should be removed once the modal is opened. By default, it is set to the `hidden` class.

Refer below example for hiddenClass option usecase.

{{< code >}}

<button type="button" class="btn btn-primary"  aria-haspopup="dialog" aria-expanded="false" aria-controls="demo-hidden-modal" data-overlay="#demo-hidden-modal" data-overlay-options='{ "hiddenClass": "hidden" }'> Open modal</button>

<div id="demo-hidden-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#demo-hidden-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#demo-hidden-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Autoclose & opened  -->

{{< headname level="3" >}} Autoclose & opened {{< /headname >}}

The options `[--auto-close:*]` and `[--opened:*]`, where `*` represents a number or breakpoints (sm, md, lg, xl, xxl), control the modal behavior upon window resizing. They determine whether the modal should automatically close on resize or remain open when the browser window is resized.

Configuring values at specific breakpoints or resolution levels enables this open-close behavior for the modal upon resizing.

Refer to the following examples to better understand the use cases of the autoclose and opened options when resizing the window <span class="icon-[tabler--resize] cursor-pointer text-error"></span>.

<!-- The options `[--auto-close:*]` and `[--opened:*]`, where * represents a number or breakpoints (sm, md, lg, xl, xxl), control the modal behavior upon window resizing. They determine whether the modal should automatically close on resize or remain open when the browser window is resized. The option `[--auto-close-equality-type:less-than]` specifies that the modal should close when the window width is less than or equal to the defined threshold.

Configuring values at specific breakpoints or resolution levels enables this open-close behavior for the modal upon resizing.

Refer to the following examples to better understand the use cases of the autoclose and opened options when resizing the window <span class="icon-[tabler--resize] cursor-pointer text-error"></span>. -->

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="auto-close-modal" data-overlay="#auto-close-modal">Autoclose</button>

<!-- Autoclose at breakpoint sm -->

<div id="auto-close-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden [--auto-close:sm]" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#auto-close-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#auto-close-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!--  Static backdrop  -->

{{< headname level="3" >}} Static backdrop {{< /headname >}}

Here’s a more spaced-out and clearer version:

You can use the `[--overlay-backdrop:{string}]` option to control the modal backdrop behavior. The `{string}` can be set to `static`, `false`, or `null`. By default, the value is `null`.When set to `static`, the modal's backdrop becomes unclickable, meaning the modal won't close when clicking outside its area.

When using the `static` option, include the attribute `data-overlay-keyboard="false"` to disable closing the modal via the `Esc` key.

Here’s an example demonstrating how to create a static backdrop modal.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="static-backdrop-modal" data-overlay="#static-backdrop-modal">Open modal</button>

<div id="static-backdrop-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden [--overlay-backdrop:static]" role="dialog" tabindex="-1" data-overlay-keyboard="false">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#static-backdrop-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#static-backdrop-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Disabled backdrop -->

{{< headname level="3" >}} Disabled backdrop {{< /headname >}}

When `[--overlay-backdrop:{string}]` is set to `false`, it creates a modal with a no backdrop.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="disabled-backdrop-modal" data-overlay="#disabled-backdrop-modal">Open modal</button>

<div id="disabled-backdrop-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden [--overlay-backdrop:false]" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#disabled-backdrop-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Insted of raepeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#disabled-backdrop-modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!--  Options  -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/overlay.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

{{< table >}}

PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span colspan="4" class="text-base-content font-semibold">Data Options</span>
`data-overlay`| Serves as a toggle button for the modal. |`-`|`-`
`data-overlay-options`|Defines the modal. Should be added to the button (trigger).|`-`|`-`
`:hiddenClass`| Defines which classes will be added/removed when modal toggle.| string | `hidden`
`:isClosePrev`| Determines whether the previous open modal will be closed when the next one is opened.| boolean | `true`
`:emulateScrollbarSpace`|If `true`, then adds right padding to the body equal to the size of the scrollbar.|boolean|`false`
`:backdropClasses`| Defines which classes will be added to the modals' backdrop.| string | `transition duration-300 fixed inset-0 bg-base-content/60 overlay-backdrop`
`:backdropExtraClasses`|Allows to add additional classes besides those specified in `backdropClasses`.|string|`-`
`:backdropParent`| Allows to specify the selector of the element where the backdrop will be generated.|string|`-`
`:moveOverlayToBody`| Moves the overlay to the body tag if the screen width is less than the value specified.|`number` / `null` |`null`
<code class="sm:text-nowrap">data-overlay-backdrop-container</code> | Backdrop element selector. | `-` | `null`
`data-overlay-keyboard`| When set to false, the modal will not close when pressing the ESC button on the keyboard. | boolean | `true`
<span colspan="4" class="text-base-content font-semibold">Class Options</span>
`autofocus`| Focus the first input in a modal with the autofocus attribute on opening. Must be added to an input element inside a modal window. | `-` | `-`
`[--overlay-backdrop:*]`| When backdrop is set to `static`, the modal will not close when clicking outside it. When set to `false` the backdrop will be disabled. | 'static', null, 'false' | `null`
`[--auto-hide:*]`| Milliseconds for auto-closing a modal. When set to 0, the modal will not close. | number | `0`
`[--auto-close:*]`| Screen resolution at which the overlay will close automatically. | 'sm', 'md', 'lg', 'xl', 'xxl', number | `null`
`[--auto-close-equality-type:*]` | This option controls when the overlay closes based on window width. "Less-than" closes it when the width is ≤ `[--auto-close:]`, otherwise it closes when the width ≥ `[--auto-close:]`.Add to the overlay content. | 'less-than'/null | `null`
`[--opened:*]`| Screen resolution at which the plugin will apply functionality for the initially opened overlay. | 'sm', 'md', 'lg', 'xl', 'xxl', number | `null`
`[--body-scroll:*]`| When set to false, the body scroll will be hidden as soon as the modal opens. | boolean | `true`
`[--tab-accessibility-limited:*]`| Restricts focus to elements within an overlay (or modal). | boolean | `true`
`[--has-autofocus:*]`| Disables autofocus on the first focusable element when opening an overlay. | boolean | `true`
`[--has-dynamic-z-index:*]` | When set to `true`, each new element in the group gets an incremented `z-index`, ensuring it appears above previous elements. Add to the overlay content. | boolean | `false`
`[--is-layout-affect:*]`| Informs the plugin that the instance affects to the website layout. | boolean | `false`
{{< /table >}}

<!--  Methods  -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSOverlay` object is contained within the global `window` object.

{{< table >}}

METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`open()`| Force open modal.
`close()`| Force close modal.
`destroy()`| Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSOverlay.getInstance(target, isInstance)`|<div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true.</code></li></ul></div>
`HSOverlay.open(target)`|<div>Open modal.<ul class="m-0"><li><code>target</code> should be a Node.</li></ul></div>
`HSOverlay.close(target)`|<div>Close modal.<ul class="m-0"><li><code>target</code> should be a Node.</li></ul></div>
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

Here's a demonstration of how to utilize methods on overlays such as modals and drawers. To test other methods, just copy them into your browser's console and then click the `Open modal using methods` button.

{{< code jsCode="true" >}}

<button id="open-btn" type="button" class="btn btn-primary">Open modal using methods</button>

<div id="modal-target" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden --prevent-on-load-init" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#modal-target" >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#modal-target">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const modal = new HSOverlay(document.querySelector('#modal-target'))
    const openBtn = document.querySelector('#open-btn')

    openBtn.addEventListener('click', () => {
      modal.open()
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">Open item (public method).</p>

{{< callout "info" >}}
<strong>Note(only for public method)</strong>: To prevent initialization, add the <code class="text-sm ">--prevent-on-load-init</code> class to the modal element before initializing it with <code class="text-sm">new</code>. {{< /callout >}}
{{< code-highlight lang="html" >}}
<button class="--prevent-on-load-init" data-overlay="#id">
...
</button>
{{< /code-highlight >}}

{{< code-highlight lang="js" >}}// This method is used in above example.
const modal = new HSOverlay(document.querySelector('#modal-target'));
const openBtn = document.querySelector('#open-btn');

openBtn.addEventListener('click', () => {
  modal.open();
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose">Open item (static method).</p>

{{< code-highlight lang="js" >}}const openBtn = document.querySelector('#open-btn');

openBtn.addEventListener('click', () => {
  HSOverlay.open('#modal-target');
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose">Open item (mixed).</p>

{{< code-highlight lang="js" >}}const { element } = HSOverlay.getInstance('#modal-target', true);
const openBtn = document.querySelector('#open-btn');

openBtn.addEventListener('click', () => {
  element.open();
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose" id="destroy-method">Destroy Instance(public).</p>

{{< code-highlight lang="js" >}}
const modals = document.querySelectorAll('[data-overlay="#destroy-modal"]')
const destroy = document.querySelector('#destroy-btn')

destroy.addEventListener('click', () => {
  modals.forEach(el => {
    const { element } = HSOverlay.getInstance(el, true)
    element.destroy()
  })
})
{{< /code-highlight >}}

<!--  Events  -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION
`on:open`| Called when modal is open.
`on:close`| Called when modal is closed.
{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

Here's a demonstration of how to utilize events on overlays like modals and drawers. To test these events, just copy them into your browser's console and see the output in the console when the modal opens and closes.

{{< code jsCode="true" >}}

<button id="modal-trigger-2" type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="modal-target-2" data-overlay="#modal-target-2">Open modal</button>

<div id="modal-target-2" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#modal-target-2">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the
        modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and
        demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling
        will move the modal as needed.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#modal-target-2">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Js -->
<script>
window.addEventListener('load', function () {
  const { element } = HSOverlay.getInstance('#modal-target-2', true)

  element.on('open', instance => {
    console.log('open')
  })
  element.on('close', instance => {
    console.log('close')
  })
})
</script>

{{< /code >}}

<p class="mt-12 mb-1.5 not-prose">Open any overlay event example.</p>

{{< code-highlight lang="js" >}}const { element } = HSOverlay.getInstance('#modal-target-2', true)

element.on('open', instance => { console.log('open') })
element.on('close', instance => { console.log('close') })
{{< /code-highlight >}}
