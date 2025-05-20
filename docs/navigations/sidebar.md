---
title: "Sidebar"
description: "Utilize a sidebar component on both sides of the page to display a list of menu items, including multi-level navigation options, for easy website navigation."
bg_image: "svg/navigations/sidebar.svg"
components: 7
menu:
  main:
    parent: "navigations"

previous: Scrollspy
previousLink: navigations/scrollspy/

next: Stepper
nextLink: navigations/stepper/

requires_js: true

---

{{< callout "info" >}}
For more information, please refer to the {{< link link="overlays/drawer/" addClass="link link-primary" >}}Drawer{{< /link >}}, {{< link link="navigations/menu/" addClass="link link-primary" >}}Menu{{< /link >}} and  {{< link link="components/collapse/" addClass="link link-primary" >}}Collapse{{< /link >}} components, which use the overlay drawer, menu and collapse functionality.
{{< /callout >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Create a responsive sidebar menu that contains a list of items, each with an associated icon and label. Utilize the `[--auto-close:*]` responsive value, such as `sm`, `md`, `lg`, `xl`, or `2xl`, to automatically close the overlay based on the screen size.

{{< callout "warning" >}}
Please remove `sm:z-0` and `sm:absolute`, as these were applied for a specific condition in our case. Since some styles are conditional, kindly remove any unnecessary classes.
{{< /callout >}}

{{< code addClass="relative sm:h-[400px] overflow-y-auto !block" >}}
<button type="button" class="btn btn-text max-sm:btn-square sm:hidden" aria-haspopup="dialog" aria-expanded="false" aria-controls="default-sidebar" data-overlay="#default-sidebar" >
  <span class="icon-[tabler--menu-2] size-5"></span>
</button>

<aside id="default-sidebar" class="overlay [--auto-close:sm] sm:shadow-none overlay-open:translate-x-0 drawer drawer-start hidden max-w-64 sm:absolute sm:z-0 sm:flex sm:translate-x-0" role="dialog" tabindex="-1" >
  <div class="drawer-body px-2 pt-4">
    <ul class="menu p-0">
      <li>
        <a href="#">
          <span class="icon-[tabler--home] size-5"></span>
          Home
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--user] size-5"></span>
          Account
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--message] size-5"></span>
          Notifications
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
      <li>
        <a href="#">
          <span class="icon-[tabler--shopping-bag] size-5"></span>
          Product
        </a>
      </li>
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
    </ul>
  </div>
</aside>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Multiple level with separator -->

{{< headname level="3" >}} Multiple level with separator {{< /headname >}}

Use this example to create a multi-level sidebar by utilizing the collapse feature with the menu for collapsible items, and the divider component to create separators.

{{< callout "warning" >}}
Please remove `sm:z-0` and `sm:absolute`, as these were applied for a specific condition in our case. Since some styles are conditional, kindly remove any unnecessary classes.
{{< /callout >}}

{{< code addClass="relative sm:h-[400px] overflow-y-auto !block" >}}
<button type="button" class="btn btn-text max-sm:btn-square sm:hidden" aria-haspopup="dialog" aria-expanded="false" aria-controls="multilevel-with-separator" data-overlay="#multilevel-with-separator" >
  <span class="icon-[tabler--menu-2] size-5"></span>
</button>

<aside id="multilevel-with-separator" class="overlay [--auto-close:sm] overlay-open:translate-x-0 drawer drawer-start hidden max-w-64 sm:absolute sm:z-0 sm:flex sm:translate-x-0 sm:shadow-none" tabindex="-1" >
  <div class="drawer-body px-2 pt-4">
    <ul class="menu space-y-0.5 p-0">
      <li>
        <a href="#">
          <span class="icon-[tabler--home] size-5"></span>
          Home
        </a>
      </li>
      <li class="space-y-0.5">
        <a class="collapse-toggle collapse-open:bg-base-content/10" id="menu-app" data-collapse="#menu-app-collapse">
          <span class="icon-[tabler--apps] size-5"></span>
          Apps
          <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4 transition-all duration-300"></span>
        </a>
        <ul id="menu-app-collapse" class="collapse hidden w-auto space-y-0.5 overflow-hidden transition-[height] duration-300" aria-labelledby="menu-app" >
          <li>
            <a href="#">
              <span class="icon-[tabler--message] size-5"></span>
              Chat
            </a>
          </li>
          <li>
            <a href="#">
              <span class="icon-[tabler--calendar] size-5"></span>
              Calendar
            </a>
          </li>
          <li class="space-y-0.5">
            <a class="collapse-toggle collapse-open:bg-base-content/10" id="sub-menu-academy" data-collapse="#sub-menu-academy-collapse" >
              <span class="icon-[tabler--book] size-5"></span>
              Academy
              <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
            </a>
            <ul id="sub-menu-academy-collapse" class="collapse hidden w-auto space-y-0.5 overflow-hidden transition-[height] duration-300" aria-labelledby="sub-menu-academy" >
              <li>
                <a href="#">
                  <span class="icon-[tabler--books] size-5"></span>
                  Courses
                </a>
              </li>
              <li>
                <a href="#">
                  <span class="icon-[tabler--list-details] size-5"></span>
                  Course details
                </a>
              </li>
              <li class="space-y-0.5">
                <a class="collapse-toggle collapse-open:bg-base-content/10" id="sub-menu-academy-stats" data-collapse="#sub-menu-academy-stats-collapse" >
                  <span class="icon-[tabler--chart-bar] size-5"></span>
                  Stats
                  <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
                </a>
                <ul id="sub-menu-academy-stats-collapse" class="collapse hidden w-auto space-y-0.5 overflow-hidden transition-[height] duration-300" aria-labelledby="sub-menu-academy-stats" >
                  <li>
                    <a href="#">
                      <span class="icon-[tabler--chart-donut] size-5"></span>
                      Goals
                    </a>
                  </li>
                </ul>
              </li>
            </ul>
          </li>
        </ul>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--settings] size-5"></span>
          Settings
        </a>
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

<!-- CTA button -->

{{< headname level="3" >}} CTA button {{< /headname >}}

Use this example to incorporate a CTA button within the sidebar, guiding users to visit the dedicated page.

{{< callout "warning" >}}
Please remove `sm:z-0` and `sm:absolute`, as these were applied for a specific condition in our case. Since some styles are conditional, kindly remove any unnecessary classes.
{{< /callout >}}

{{< code addClass="relative sm:h-[400px] overflow-y-auto !block" >}}
<button type="button" class="btn btn-text max-sm:btn-square sm:hidden" aria-haspopup="dialog" aria-expanded="false" aria-controls="cta-sidebar" data-overlay="#cta-sidebar" >
  <span class="icon-[tabler--menu-2] size-5"></span>
</button>

<aside id="cta-sidebar" class="overlay [--auto-close:sm] overlay-open:translate-x-0 drawer drawer-start hidden max-w-64 sm:absolute sm:z-0 sm:flex sm:translate-x-0 sm:shadow-none" role="dialog" tabindex="-1" >
  <div class="drawer-body px-2 py-4">
    <ul class="menu p-0">
      <li>
        <a href="#">
          <span class="icon-[tabler--user] size-5"></span>
          Account
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--message] size-5"></span>
          Notifications
        </a>
      </li>
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
    </ul>
    <div class="bg-base-200/30 border-base-content/10 mt-4 rounded-md border p-3">
      <div class="avatar avatar-placeholder">
        <div class="bg-neutral text-neutral-content w-10 rounded-full">
          <span class="icon-[tabler--crown] size-6 shrink-0"></span>
        </div>
      </div>
      <h5 class="text-base-content mt-4 text-lg font-semibold">Upgrade to Pro</h5>
      <p class="text-base-content/80 text-xs">Reminder, extra projects, advanced search and more</p>
      <button class="btn btn-primary btn-block mt-2">Upgrade Now</button>
    </div>
  </div>
</aside>
{{< /code >}}

<!-- Logo branding -->

{{< headname level="3" >}} Logo branding {{< /headname >}}

Display your brand's logo and link it back to the homepage at the top of the sidebar.

{{< callout "warning" >}}
Please remove `sm:z-0` and `sm:absolute`, as these were applied for a specific condition in our case. Since some styles are conditional, kindly remove any unnecessary classes.
{{< /callout >}}

{{< code addClass="relative sm:h-[400px] overflow-y-auto !block" >}}
<button type="button" class="btn btn-text max-sm:btn-square sm:hidden" aria-haspopup="dialog" aria-expanded="false" aria-controls="logo-sidebar" data-overlay="#logo-sidebar" >
  <span class="icon-[tabler--menu-2] size-5"></span>
</button>

<aside id="logo-sidebar" class="overlay [--auto-close:sm] sm:shadow-none overlay-open:translate-x-0 drawer drawer-start hidden max-w-64 sm:absolute sm:z-0 sm:flex sm:translate-x-0" role="dialog" tabindex="-1" >
  <div class="drawer-header">
    <div class="flex items-center gap-3">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M17.6745 16.9224L12.6233 10.378C12.2167 9.85117 11.4185 9.8611 11.0251 10.3979L6.45728 16.631C6.26893 16.888 5.96935 17.0398 5.65069 17.0398H3.79114C2.9635 17.0398 2.49412 16.0919 2.99583 15.4336L11.0224 4.90319C11.4206 4.38084 12.2056 4.37762 12.608 4.89668L20.9829 15.6987C21.4923 16.3558 21.024 17.3114 20.1926 17.3114H18.4661C18.1562 17.3114 17.8638 17.1677 17.6745 16.9224ZM12.5866 15.5924L14.8956 18.3593C15.439 19.0105 14.976 20 14.1278 20H9.74075C8.9164 20 8.4461 19.0586 8.94116 18.3994L11.0192 15.6325C11.4065 15.1169 12.1734 15.0972 12.5866 15.5924Z" fill="var(--color-primary)"/></svg>
      <h3 class="drawer-title text-xl font-semibold">FlyonUI</h3>
    </div>
  </div>
  <div class="drawer-body px-2">
    <ul class="menu p-0">
      <li>
        <a href="#">
          <span class="icon-[tabler--home] size-5"></span>
          Home
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--user] size-5"></span>
          Account
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--message] size-5"></span>
          Notifications
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
      <li>
        <a href="#">
          <span class="icon-[tabler--shopping-bag] size-5"></span>
          Product
        </a>
      </li>
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
    </ul>
  </div>
</aside>
{{< /code >}}

<!-- With navbar -->

{{< headname level="3" >}} With navbar {{< /headname >}}

Use this example to demonstrate a layout that includes both a navbar and a sidebar for your web application.

{{< callout "warning" >}}
Please remove `sm:z-0` and `sm:absolute`, as these were applied for a specific condition in our case. Since some styles are conditional, kindly remove any unnecessary classes.
{{< /callout >}}

{{< code addClass="relative sm:h-[400px] overflow-y-auto !block sm:!p-0" >}}

<nav class="navbar bg-base-100 max-sm:rounded-box max-sm:shadow-sm sm:border-b border-base-content/25 sm:z-1 relative">
  <button type="button" class="btn btn-text max-sm:btn-square sm:hidden me-2" aria-haspopup="dialog" aria-expanded="false" aria-controls="with-navbar-sidebar" data-overlay="#with-navbar-sidebar" >
    <span class="icon-[tabler--menu-2] size-5"></span>
  </button>
  <div class="flex flex-1 items-center">
    <a class="link text-base-content link-neutral text-xl font-semibold no-underline" href="#">
      FlyonUI
    </a>
  </div>
  <div class="navbar-end flex items-center gap-4">
    <div class="dropdown relative inline-flex [--auto-close:inside] [--offset:8] [--placement:bottom-end]">
      <button id="dropdown-scrollable" type="button" class="dropdown-toggle btn btn-text btn-circle dropdown-open:bg-base-content/10 size-10" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
        <div class="indicator">
          <span class="indicator-item bg-error size-2 rounded-full"></span>
          <span class="icon-[tabler--bell] text-base-content size-5.5"></span>
        </div>
      </button>
      <div class="dropdown-menu dropdown-open:opacity-100 hidden" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-scrollable">
        <div class="dropdown-header justify-center">
          <h6 class="text-base-content text-base">Notifications</h6>
        </div>
        <div class="overflow-y-auto overflow-x-auto text-base-content/80 max-h-56 overflow-auto max-md:max-w-60">
          <div class="dropdown-item">
            <div class="avatar avatar-away-bottom">
              <div class="w-10 rounded-full">
                <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar 1" />
              </div>
            </div>
            <div class="w-60">
              <h6 class="truncate text-base">Charles Franklin</h6>
              <small class="text-base-content/50 truncate">Accepted your connection</small>
            </div>
          </div>
          <div class="dropdown-item">
            <div class="avatar">
              <div class="w-10 rounded-full">
                <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="avatar 2" />
              </div>
            </div>
            <div class="w-60">
              <h6 class="truncate text-base">Martian added moved Charts & Maps task to the done board.</h6>
              <small class="text-base-content/50 truncate">Today 10:00 AM</small>
            </div>
          </div>
          <div class="dropdown-item">
            <div class="avatar avatar-online-bottom">
              <div class="w-10 rounded-full">
                <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png" alt="avatar 8" />
              </div>
            </div>
            <div class="w-60">
              <h6 class="truncate text-base">New Message</h6>
              <small class="text-base-content/50 truncate">You have new message from Natalie</small>
            </div>
          </div>
          <div class="dropdown-item">
            <div class="avatar avatar-placeholder">
              <div class="bg-neutral text-neutral-content w-10 rounded-full p-2">
                <span class="icon-[tabler--user] size-full"></span>
              </div>
            </div>
            <div class="w-60">
              <h6 class="truncate text-base">Application has been approved 🚀</h6>
              <small class="text-base-content/50 text-wrap">Your ABC project application has been approved.</small>
            </div>
          </div>
          <div class="dropdown-item">
            <div class="avatar">
              <div class="w-10 rounded-full">
                <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-10.png" alt="avatar 10" />
              </div>
            </div>
            <div class="w-60">
              <h6 class="truncate text-base">New message from Jane</h6>
              <small class="text-base-content/50 text-wrap">Your have new message from Jane</small>
            </div>
          </div>
          <div class="dropdown-item">
            <div class="avatar">
              <div class="w-10 rounded-full">
                <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-3.png" alt="avatar 3" />
              </div>
            </div>
            <div class="w-60">
              <h6 class="truncate text-base">Barry Commented on App review task.</h6>
              <small class="text-base-content/50 truncate">Today 8:32 AM</small>
            </div>
          </div>
        </div>
        <a href="#" class="dropdown-footer justify-center gap-1">
          <span class="icon-[tabler--eye] size-4"></span>
          View all
        </a>
      </div>
    </div>
    <div class="dropdown relative inline-flex [--auto-close:inside] [--offset:8] [--placement:bottom-end]">
      <button id="dropdown-scrollable" type="button" class="dropdown-toggle flex items-center" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
        <div class="avatar">
          <div class="size-9.5 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar 1" />
          </div>
        </div>
      </button>
      <ul class="dropdown-menu dropdown-open:opacity-100 hidden min-w-60" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-avatar">
        <li class="dropdown-header gap-2">
          <div class="avatar">
            <div class="w-10 rounded-full">
              <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
            </div>
          </div>
          <div>
            <h6 class="text-base-content text-base font-semibold">John Doe</h6>
            <small class="text-base-content/50">Admin</small>
          </div>
        </li>
        <li>
          <a class="dropdown-item" href="#">
            <span class="icon-[tabler--user]"></span>
            My Profile
          </a>
        </li>
        <li>
          <a class="dropdown-item" href="#">
            <span class="icon-[tabler--settings]"></span>
            Settings
          </a>
        </li>
        <li>
          <a class="dropdown-item" href="#">
            <span class="icon-[tabler--receipt-rupee]"></span>
            Billing
          </a>
        </li>
        <li>
          <a class="dropdown-item" href="#">
            <span class="icon-[tabler--help-triangle]"></span>
            FAQs
          </a>
        </li>
        <li class="dropdown-footer gap-2">
          <a class="btn btn-error btn-soft btn-block" href="#">
            <span class="icon-[tabler--logout]"></span>
            Sign out
          </a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<aside id="with-navbar-sidebar" class="overlay [--auto-close:sm] sm:shadow-none overlay-open:translate-x-0 drawer drawer-start hidden max-w-64 sm:absolute sm:z-0 sm:flex sm:translate-x-0 pt-16" role="dialog" tabindex="-1" >
  <div class="drawer-body px-2 pt-4">
    <ul class="menu p-0">
      <li>
        <a href="#">
          <span class="icon-[tabler--home] size-5"></span>
          Home
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--user] size-5"></span>
          Account
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--message] size-5"></span>
          Notifications
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
      <li>
        <a href="#">
          <span class="icon-[tabler--shopping-bag] size-5"></span>
          Product
        </a>
      </li>
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
    </ul>
  </div>
</aside>
{{< /code >}}

<!--  Scoped based Sidebar  -->

{{< headname level="3" >}}  Scoped based Sidebar  {{< /headname >}}

This example uses `:backdropParent:` to scope the backdrop within a specific block. By default, the backdrop has a `fixed` class applied. To customize the backdrop styling, you can use the `:backdropClasses` option, which completely overrides all default classes for the backdrop. Alternatively, to add additional classes while retaining the default ones, use the `:backdropExtraClasses` option. For more details about these options, please refer to the {{< link link="overlays/modal/#options" addClass="link link-primary" >}}Overlay options.{{< /link >}}


{{< code addClass="relative h-[400px] overflow-y-auto !block" >}}
<button type="button" class="btn btn-text max-sm:btn-square sm:hidden" aria-haspopup="dialog" aria-expanded="false" aria-controls="scoped-sidebar" data-overlay="#scoped-sidebar" data-overlay-options='{ "backdropExtraClasses": "!absolute", "backdropParent": "#custom-backdrop-container" }'>
  <span class="icon-[tabler--menu-2] size-5"></span>
</button>

<aside id="scoped-sidebar" class="overlay [--auto-close:sm] sm:shadow-none overlay-open:translate-x-0 drawer drawer-start hidden max-w-64 absolute z-1 sm:flex sm:translate-x-0 [--body-scroll:true]" role="dialog" tabindex="-1">
  <div class="drawer-body px-2 pt-4">
    <ul class="menu p-0">
      <li>
        <a href="#">
          <span class="icon-[tabler--home] size-5"></span>
          Home
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--user] size-5"></span>
          Account
        </a>
      </li>
      <li>
        <a href="#">
          <span class="icon-[tabler--message] size-5"></span>
          Notifications
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
      <li>
        <a href="#">
          <span class="icon-[tabler--shopping-bag] size-5"></span>
          Product
        </a>
      </li>
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
    </ul>
  </div>
</aside>
<div id="custom-backdrop-container"></div>
{{< /code >}}

<!-- Drawer sidebar -->
 
{{< headname level="3" >}} Drawer sidebar {{< /headname >}}

Use this example to implement drawer as an navigation component that appears when an element is clicked.


{{< callout "info" >}}
You can check out this example on the {{< link link="overlays/drawer/#drawer-with-navigation" addClass="link link-primary" >}}Drawer{{< /link >}} component page.
{{< /callout >}}
