---
title: "Drawer (Offcanvas)"
description: "The Drawer component serves as a concealed off-canvas sidebar, ideal for navigation and displaying additional information with various styles and placements."
bg_image: "svg/overlays/drawer.svg"
components: 7
menu:
  main:
    parent: "overlays"

previous:  Context Menu
previousLink: overlays/context-menu/

next: Dropdown
nextLink: overlays/dropdown/

requires_js: true
---

{{< callout "info" >}}
Modal components are adopted from <a href="https://preline.co/docs/offcanvas.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class table -->

{{< class-table >}}
overlay | component | Create an overlay initalize instance.
drawer | component | Provides structure and styling for the modal component.
drawer-header | part | Adds basic style drawer header.
drawer-title | part | Adds basic style for drawer title.
drawer-body | part | Adds basic style for drawer body.
drawer-footer | part | Adds basic style for drawer footer.
overlay-open:{tw-utility-class} | variant | Modifies tailwind classes when the overlay is open.
overlay-backdrop-open:{tw-utility-class} | variant | Defines classes will be applied to backdrop when the overlay is open.
overlay-layout-open{tw-utility-class}: | variant | Defines classes will be applied to any elements inside the body tag when the overlay is open.
drawer-start | placement | Toggles drawer from start position.
drawer-end | placement | Toggles drawer from end position.
drawer-top | placement | Toggles drawer from top position.
drawer-bottom | placement | Toggles drawer from bottom position.
{{< /class-table >}}

<!-------------------- Default -------------------->

{{< headname level="2" >}} Default {{< /headname >}}

<!-- Basic example -->

{{< headname level="3" >}} Basic example {{< /headname >}}

Use the `overlay` class as the JavaScript target for addressing the overlay component, and utilize the `drawer` class for the drawer container. Use the `drawer-start` responsive class to toggle its position from the start. Apply the Tailwind CSS `hidden` class to keep the drawer container hidden until it is opened.

Add modifier class `overlay-open:` with transform class `translate-x-0` to drawer container so that it shows drawer when opened.

Assign the value of the `data-overlay` attribute in any button to the `id` of the targeted overlay component, triggering the drawer to appear upon being clicked.

The drawer structure consists of the component class `drawer`, which serves as the container for the drawer content.

This drawer is further styled using modifier classes such as `drawer-header`, `drawer-title`, `drawer-body` and `drawer-footer`, which collectively define the entire structure of the drawer.

Utilize the provided example for default drawer component.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-example" data-overlay="#overlay-example">Open drawer</button>

<div id="overlay-example" class="overlay overlay-open:translate-x-0 drawer drawer-start hidden" role="dialog" tabindex="-1">
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-example">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-example">Close</button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>
{{< /code >}}

<!-------------------- Placements -------------------->

{{< headname level="2" >}} Placements {{< /headname >}}

<!-- Positions -->

{{< headname level="3" >}} Positions {{< /headname >}}

Utilize the responsive classes `drawer-{position}` to position the drawer in various positions, where `{position}` can be replaced with `start`, `top`, `end`, `middle-start` or `bottom`.

Refer to the provided examples for positioning the drawer at the default start position, as well as the end, top, or bottom positions.

{{< code >}}

<!-- Drawer start -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-start-example" data-overlay="#overlay-start-example">Toggle start</button>

<div id="overlay-start-example" class="overlay overlay-open:translate-x-0 drawer drawer-start hidden" role="dialog" tabindex="-1">
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-start-example">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-start-example">Close</button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>

<!-- Drawer end -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-end-example" data-overlay="#overlay-end-example">Toggle end</button>

<div id="overlay-end-example" class="overlay overlay-open:translate-x-0 drawer drawer-end hidden" role="dialog" tabindex="-1">
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-end-example">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-end-example">Close</button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>

<!-- Drawer top -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-top-example" data-overlay="#overlay-top-example">Toggle top</button>

<div id="overlay-top-example" class="overlay drawer overlay-open:translate-y-0 drawer-top hidden" role="dialog" tabindex="-1">
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-top-example">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-top-example">Close</button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>

<!-- Drawer bottom -->

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-bottom-example" data-overlay="#overlay-bottom-example">Toggle bottom</button>

<div id="overlay-bottom-example" class="overlay drawer overlay-open:translate-y-0 drawer-bottom hidden" role="dialog" tabindex="-1">
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-bottom-example">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-bottom-example">Close</button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Responsive -->

{{< headname level="3" >}} Responsive {{< /headname >}}

Use TailwindCSS classes for <a href="https://tailwindcss.com/docs/responsive-design#targeting-a-breakpoint-range" target="_blank" class="link link-primary">responsive design</a>, such as `sm:`, `md:`, `lg:`, `xl:`, and `2xl:`, along with the responsive class `drawer-{position}` to switch the drawer position at specific breakpoints.

Utilize the provided example for a responsive drawer that moves to start position after `lg:` breakpoint.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-responsive-example" data-overlay="#overlay-responsive-example">Open drawer</button>

<div id="overlay-responsive-example" class="overlay overlay-open:translate-x-0 drawer drawer-end lg:drawer-start hidden" role="dialog" tabindex="-1" >
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-responsive-example">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-responsive-example">Close</button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>
{{< /code >}}

<!-- Drawer with form -->

{{< headname level="3" >}} Drawer with form {{< /headname >}}

Utilize the provided example to implement drawer with form.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-form-example" data-overlay="#overlay-form-example">Toggle form</button>

<div id="overlay-form-example" class="overlay overlay-open:translate-x-0 drawer drawer-end hidden justify-start" role="dialog" tabindex="-1" >
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-form-example">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <form>
    <div class="drawer-body justify-start">
      <div class="mb-4">
        <label class="label-text" for="fullName"> Full Name </label>
        <input type="text" placeholder="John Doe" class="input" id="fullName" />
      </div>
      <div class="mb-4">
        <label class="label-text" for="email"> Email </label>
        <input type="email" placeholder="john.doe@example.com" class="input" id="email" />
      </div>
      <div class="mb-4">
        <label class="label-text" for="contact"> Contact </label>
        <input type="text" placeholder="+91 (106) 234-34-85" class="input" id="contact" />
      </div>
      <div class="mb-4">
        <label class="label-text" for="company"> Company </label>
        <input type="text" placeholder="ABC Technologies Ltd" class="input" id="company" />
      </div>
      <div class="mb-4">
        <label class="label-text" for="country"> Country </label>
        <select class="select" id="country">
          <option disabled selected>Select Country</option>
          <option>USA</option>
          <option>India</option>
          <option>Canada</option>
          <option>Japan</option>
          <option>Russia</option>
        </select>
      </div>
      <div class="mb-4">
        <label class="label-text" for="userRole"> User Role </label>
        <select class="select" id="userRole">
          <option disabled selected>Select Role</option>
          <option>Subscriber</option>
          <option>Maintainer</option>
          <option>Editor</option>
          <option>Author</option>
          <option>Admin</option>
        </select>
      </div>
      <div class="mb-0.5">
        <label class="label-text" for="selectPlan"> Select Plan </label>
        <select class="select" id="selectPlan">
          <option disabled selected>Select Plan</option>
          <option>Basic</option>
          <option>Enterprise</option>
          <option>Company</option>
          <option>Team</option>
        </select>
      </div>
    </div>
    <div class="drawer-footer">
      <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-form-example">Close</button>
      <button type="submit" class="btn btn-primary">Save changes</button>
    </div>
  </form>
</div>
{{< /code >}}

<!-- Drawer with navigation -->

{{< headname level="3" >}} Drawer with navigation {{< /headname >}}

Utilize the provided example to implement drawer with navigation. We have used collapse for collapsible item.

{{< callout "info" >}}
Refer {{< link link="components/collapse/" addClass="link link-primary" >}}Collapse{{< /link >}} plugin for more details.
{{< /callout >}}

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-navigation-example" data-overlay="#overlay-navigation-example" > Drawer with navigation </button>

<aside id="overlay-navigation-example" class="overlay overlay-open:translate-x-0 drawer drawer-start hidden max-w-72" tabindex="-1" >
  <div class="drawer-header">
    <h3 class="drawer-title">Menu</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-navigation-example" >
      <span class="icon-[tabler--x] size-4"></span>
    </button>
  </div>
  <div class="drawer-body justify-start pb-6">
    <ul class="menu space-y-0.5 p-0">
      <li>
        <a href="#">
          <span class="icon-[tabler--home] size-5"></span>
          Dashboard
        </a>
      </li>
      <li class="space-x-0.5">
        <a class="collapse-toggle collapse-open:bg-base-content/10" id="layout-collapse" data-collapse="#layout-collapse-menu" >
          <span class="icon-[tabler--layout-navbar] size-5"></span>
          Layouts
          <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
        </a>
        <ul id="layout-collapse-menu" class="collapse hidden w-auto space-y-0.5 overflow-hidden transition-[height] duration-300" aria-labelledby="layout-collapse" >
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Content Navbar
            </a>
          </li>
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Horizontal
            </a>
          </li>
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Without Menu
            </a>
          </li>
        </ul>
      </li>
      <li class="space-y-0.5">
        <a class="collapse-toggle collapse-open:bg-base-content/10" id="front-page-collapse" data-collapse="#front-page-collapse-menu" >
          <span class="icon-[tabler--box-multiple] size-5"></span>
          Front Pages
          <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
        </a>
        <ul id="front-page-collapse-menu" class="collapse hidden w-auto space-y-0.5 overflow-hidden transition-[height] duration-300" aria-labelledby="front-page-collapse" >
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Landing Page
            </a>
          </li>
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Pricing Page
            </a>
          </li>
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Checkout Page
            </a>
          </li>
        </ul>
      </li>
      <div class="divider text-base-content/50 py-6 after:border-0">Apps & Pages</div>
      <li>
        <a href="#">
          <span class="icon-[tabler--message-chatbot] size-5"></span>
          Chat
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--mail] size-5"></span>
          Email
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--calendar] size-5"></span>
          Calendar
        </a>
      </li>
      <li class="space-x-0.5">
        <a class="collapse-toggle collapse-open:bg-base-content/10" id="ecommerce-collapse" data-collapse="#ecommerce-collapse-menu" >
          <span class="icon-[tabler--shopping-cart] size-5"></span>
          Ecommerce
          <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
        </a>
        <ul id="ecommerce-collapse-menu" class="collapse hidden w-auto space-y-0.5 overflow-hidden transition-[height] duration-300" aria-labelledby="ecommerce-collapse" >
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Products
            </a>
          </li>
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Categories
            </a>
          </li>
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Shipping & Delivery
            </a>
          </li>
          <li>
            <a href="#">
              <span class="icon-[tabler--point] size-5"></span>
              Location
            </a>
          </li>
        </ul>
      </li>
      <div class="divider text-base-content/50 py-6 after:border-0">Account</div>
      <li>
        <a href="#">
          <span class="icon-[tabler--login] size-5"></span>
          Sign In
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--logout-2] size-5"></span>
          Sign Out
        </a>
      </li>
      <div class="divider text-base-content/50 py-6 after:border-0">Miscellaneous</div>
      <li>
        <a href="#">
          <span class="icon-[tabler--users-group] size-5"></span>
          Support
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--files] size-5"></span>
          Documentation
        </a>
      </li>
    </ul>
  </div>
</aside>
{{< /code >}}

<!-------------------- Options usage -------------------->

{{< headname level="2" >}} Options usage {{< /headname >}}

<!-- Bodyscroll without backdrop -->

{{< headname level="3" >}} Bodyscroll without backdrop {{< /headname >}}

Utilize the `[--body-scroll:{boolean}]` option to control the scrolling behavior of the layout beneath the overlay component. When set to `true`, it enables scrolling of the body, whereas when set to `false`, it disables body scrolling. By default, its value is `false`.

Set the `[--overlay-backdrop:{string}]` option, where `{string}` can be `static`, `null` or `false`. When set to `false` it creates drawer without backdrop. By default, its value is `null`.

Review the provided example for a drawer with body scroll enabled and without a backdrop.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-body-scrolling" data-overlay="#overlay-body-scrolling">
  Body scrolling (no backdrop)
</button>

<div id="overlay-body-scrolling" class="overlay overlay-open:translate-x-0 drawer drawer-start hidden [--body-scroll:true] [--overlay-backdrop:false]" role="dialog" tabindex="-1">
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-body-scrolling">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-body-scrolling">Close</button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>
{{< /code >}}

<!-- Bodyscroll with backdrop -->

{{< headname level="3" >}} Bodyscroll with backdrop {{< /headname >}}

Review the provided example for a drawer with body scroll enabled and with a backdrop.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-body-scrolling-with-backdrop" data-overlay="#overlay-body-scrolling-with-backdrop">
  Body scrolling (with backdrop)
</button>

<div id="overlay-body-scrolling-with-backdrop" class="overlay overlay-open:translate-x-0 drawer drawer-start hidden [--body-scroll:true]" role="dialog" tabindex="-1" >
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-body-scrolling-with-backdrop">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-body-scrolling-with-backdrop">
      Close
    </button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>
{{< /code >}}

<!-- Backdrop without bodyscroll -->

{{< headname level="3" >}} Backdrop without bodyscroll {{< /headname >}}

Review the provided example for a drawer with body scroll disabled and with a backdrop.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-backdrop-without-body-scrolling" data-overlay="#overlay-backdrop-without-body-scrolling">
  Backdrop (without bodyscroll)
</button>

<div id="overlay-backdrop-without-body-scrolling" class="overlay overlay-open:translate-x-0 drawer drawer-start hidden" role="dialog" tabindex="-1" >
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-backdrop-without-body-scrolling">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-backdrop-without-body-scrolling">
      Close
    </button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>
{{< /code >}}

<!-- Custom backdrop color -->

{{< headname level="3" >}} Custom backdrop color {{< /headname >}}

For customizing the backdrop, there are two methods available:

The first method involves using the backdrop modifier class `overlay-backdrop-open:{custom-color}`, where you can specify any color for the backdrop.

The second method entails assigning an object value to the `data-overlay-options` attribute in the trigger button. Within this object, set the `backdropClasses` key to `transition duration-300 fixed inset-0 bg-success/70 overlay-backdrop` to replace the existing backdrop classes with these customized ones.

Examine the provided examples demonstrating both methods for setting the custom backdrop in drawer.

{{< code >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-custom-backdrop" data-overlay="#overlay-custom-backdrop">Open drawer</button>

<div id="overlay-custom-backdrop" class="overlay overlay-open:translate-x-0 drawer drawer-start overlay-backdrop-open:bg-warning/40 hidden" role="dialog" tabindex="-1" >
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-custom-backdrop">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-custom-backdrop">Close</button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="overlay-custom-backdrop-2" data-overlay="#overlay-custom-backdrop-2" data-overlay-options='{ "backdropClasses": "transition duration-300 fixed inset-0 bg-accent/40 overlay-backdrop" }'> Open drawer</button>

<div id="overlay-custom-backdrop-2" class="overlay overlay-open:translate-x-0 drawer drawer-start hidden" role="dialog" tabindex="-1">
  <div class="drawer-header">
    <h3 class="drawer-title">Drawer Title</h3>
    <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#overlay-custom-backdrop-2">
      <span class="icon-[tabler--x] size-5"></span>
    </button>
  </div>
  <div class="drawer-body">
    <p>
      Some text as placeholder. In real life you can have the elements you have chosen. Like, text, images, lists, etc.
    </p>
  </div>
  <div class="drawer-footer">
    <button type="button" class="btn btn-soft btn-secondary" data-overlay="#overlay-custom-backdrop-2">Close</button>
    <button type="button" class="btn btn-primary">Save changes</button>
  </div>
</div>
{{< /code >}}

<!-- Scoped based drawer -->

{{< headname level="3" >}} Scoped based drawer {{< /headname >}}

This example showcase usage of `:backdropParent`.

{{< callout "info" >}}
You can check out this example on the {{< link link="navigations/sidebar/#scoped-based-sidebar" addClass="link link-primary" >}}Sidebar{{< /link >}} component page.
{{< /callout >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

{{< callout "info" >}}
Please refer to the {{< link link="overlays/modal/#javascript-behavior" addClass="link link-primary" >}}Modal{{< /link >}} component documentation for JavaScript behavior in overlays, which is also applicable to drawers since both modals and drawers utilize the overlay plugin.
{{< /callout >}}
