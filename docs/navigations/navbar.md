---
title: "Navbar"
description: "The navbar component provides versatile options for displaying navigation links at the top of your page, with various layouts, sizes, and dropdowns."
bg_image: "svg/navigations/navbar.svg"
components: 15
isLanding: true
menu:
  main:
    parent: "navigations"

previous: Menu
previousLink: navigations/menu/

next: Pagination
nextLink: navigations/pagination/
---

<!-- Class Table -->

{{< class-table >}}
navbar | component | Base class for navbar container.
navbar-start | placement | Child element, fills 50% of width to be on start.
navbar-center | placement | Child element, fills remaining space to be on center.
navbar-end | placement | Child element, fills 50% of width to be on end.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic navbar example with title only.

{{< code addClass="!block" >}}

<nav class="navbar rounded-box shadow-base-300/20 shadow-sm">
  <div class="w-full md:flex md:items-center md:gap-2">
    <div class="flex items-center justify-between">
      <div class="navbar-start items-center justify-between max-md:w-full">
        <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">FlyonUI</a>
        <div class="md:hidden">
          <button type="button" class="collapse-toggle btn btn-outline btn-secondary btn-sm btn-square" data-collapse="#default-navbar-collapse" aria-controls="default-navbar-collapse" aria-label="Toggle navigation" >
            <span class="icon-[tabler--menu-2] collapse-open:hidden size-4"></span>
            <span class="icon-[tabler--x] collapse-open:block hidden size-4"></span>
          </button>
        </div>
      </div>
    </div>
    <div id="default-navbar-collapse" class="md:navbar-end collapse hidden grow basis-full overflow-hidden transition-[height] duration-300 max-md:w-full" >
      <ul class="menu md:menu-horizontal gap-2 p-0 text-base max-md:mt-2">
        <li><a href="#">Home</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact us</a></li>
      </ul>
    </div>
  </div>
</nav>
{{< /code >}}

<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!-- With title as logo -->

{{< headname level="3" >}} With title as logo {{< /headname >}}

Basic navbar example with title as logo.

{{< code addClass="!block" >}}

<nav class="navbar rounded-box shadow-base-300/20 shadow-sm">
  <div class="w-full md:flex md:items-center md:gap-2">
    <div class="flex items-center justify-between">
      <div class="navbar-start items-center justify-between max-md:w-full">
        <a href="#" aria-label="Homepage Link">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M17.6745 16.9224L12.6233 10.378C12.2167 9.85117 11.4185 9.8611 11.0251 10.3979L6.45728 16.631C6.26893 16.888 5.96935 17.0398 5.65069 17.0398H3.79114C2.9635 17.0398 2.49412 16.0919 2.99583 15.4336L11.0224 4.90319C11.4206 4.38084 12.2056 4.37762 12.608 4.89668L20.9829 15.6987C21.4923 16.3558 21.024 17.3114 20.1926 17.3114H18.4661C18.1562 17.3114 17.8638 17.1677 17.6745 16.9224ZM12.5866 15.5924L14.8956 18.3593C15.439 19.0105 14.976 20 14.1278 20H9.74075C8.9164 20 8.4461 19.0586 8.94116 18.3994L11.0192 15.6325C11.4065 15.1169 12.1734 15.0972 12.5866 15.5924Z"
            fill="var(--color-primary)"
          /></svg>
        </a>
        <div class="md:hidden">
          <button type="button" class="collapse-toggle btn btn-outline btn-secondary btn-sm btn-square" data-collapse="#logo-navbar-collapse" aria-controls="logo-navbar-collapse" aria-label="Toggle navigation" >
            <span class="icon-[tabler--menu-2] collapse-open:hidden size-4"></span>
            <span class="icon-[tabler--x] collapse-open:block hidden size-4"></span>
          </button>
        </div>
      </div>
    </div>
    <div id="logo-navbar-collapse" class="md:navbar-end collapse hidden grow basis-full overflow-hidden transition-[height] duration-300 max-md:w-full" >
      <ul class="menu md:menu-horizontal gap-2 p-0 text-base max-md:mt-2">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Careers</a></li>
      </ul>
    </div>
  </div>
</nav>
{{< /code >}}

<!-- With dropdown -->

{{< headname level="3" >}} With dropdown {{< /headname >}}

Below given example displays navbar with dropdown menu.

{{< callout "info" >}}
Please refer to the {{< link link="overlays/dropdown/" addClass="link link-primary" >}}Dropdown{{< /link >}} documentation for more details on the dropdown plugin used in the Navbar component for the mega menu.
{{< /callout >}}

{{< code >}}

<nav class="navbar rounded-box shadow-base-300/20 shadow-sm">
  <div class="w-full md:flex md:items-center md:gap-2">
    <div class="flex items-center justify-between">
      <div class="navbar-start items-center justify-between max-md:w-full">
        <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">FlyonUI</a>
        <div class="md:hidden">
          <button type="button" class="collapse-toggle btn btn-outline btn-secondary btn-sm btn-square" data-collapse="#dropdown-navbar-collapse" aria-controls="dropdown-navbar-collapse" aria-label="Toggle navigation" >
            <span class="icon-[tabler--menu-2] collapse-open:hidden size-4"></span>
            <span class="icon-[tabler--x] collapse-open:block hidden size-4"></span>
          </button>
        </div>
      </div>
    </div>
    <div id="dropdown-navbar-collapse" class="md:navbar-end collapse hidden grow basis-full overflow-hidden transition-[height] duration-300 max-md:w-full" >
      <ul class="menu md:menu-horizontal gap-2 p-0 text-base max-md:mt-2">
        <li><a href="#">Home</a></li>
        <li><a href="#">Services</a></li>
        <li class="dropdown relative inline-flex [--auto-close:inside] [--offset:9] [--placement:bottom-end]">
          <button id="dropdown-nav" type="button" class="dropdown-toggle dropdown-open:bg-base-content/10 dropdown-open:text-base-content" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown" >
            Products
            <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
          </button>
          <ul class="dropdown-menu dropdown-open:opacity-100 hidden" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-nav" >
            <li><a class="dropdown-item" href="#">UI kits</a></li>
            <li><a class="dropdown-item" href="#">Templates</a></li>
            <li><a class="dropdown-item" href="#">Component library</a></li>
            <hr class="border-base-content/25 -mx-2" />
            <li><a class="dropdown-item" href="#">Figma designs</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
{{< /code >}}

<!-- With indicator & avatar -->

{{< headname level="3" >}} With indicator & avatar {{< /headname >}}

Below given example displays navbar with notifications indicator & user details avatar.

{{< code >}}

<nav class="navbar bg-base-100 rounded-box shadow-base-300/20 shadow-sm">
  <div class="flex flex-1 items-center">
    <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">
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
        <div class="overflow-auto text-base-content/80 max-h-56 max-md:max-w-60">
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
{{< /code >}}

<!-- With centered brand name -->

{{< headname level="3" >}} With centered brand name {{< /headname >}}

Below given example displays navbar with centered brand name.

{{< code >}}

<nav class="navbar rounded-box justify-between gap-4 shadow-base-300/20 shadow-sm">
  <div class="navbar-start">
    <div class="dropdown relative inline-flex [--auto-close:inside] [--offset:9]">
      <button id="dropdown-name" type="button" class="dropdown-toggle btn btn-text btn-circle dropdown-open:bg-base-content/10 dropdown-open:text-base-content" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
        <span class="icon-[tabler--menu-2] size-5"></span>
      </button>
      <ul class="dropdown-menu dropdown-open:opacity-100 hidden" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-name">
        <li><a class="dropdown-item" href="#">Link 1</a></li>
        <li><a class="dropdown-item" href="#">Link 2</a></li>
        <li><a class="dropdown-item" href="#">Link 3</a></li>
        <hr class="border-base-content/25 -mx-2" />
        <li><a class="dropdown-item" href="#">Link 4</a></li>
      </ul>
    </div>
  </div>
  <div class="navbar-center flex items-center">
    <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">
      FlyonUI
    </a>
  </div>
  <div class="navbar-end items-center gap-4">
    <button class="btn btn-sm btn-text btn-circle size-8.5" aria-label="Search Button">
      <span class="icon-[tabler--search] size-5.5"></span>
    </button>
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
{{< /code >}}

<!-- With search -->

{{< headname level="3" >}} With search {{< /headname >}}

Below given example displays navbar with search input.

{{< code >}}

<nav class="navbar bg-base-100 rounded-box gap-4 shadow-base-300/20 shadow-sm">
  <div class="navbar-start items-center">
    <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">
      FlyonUI
    </a>
  </div>
  <div class="navbar-end flex items-center gap-4">
    <button class="btn btn-sm btn-text btn-circle size-8.5 md:hidden">
      <span class="icon-[tabler--search] size-5.5"></span>
    </button>
    <div class="input max-md:hidden rounded-full max-w-56">
      <span class="icon-[tabler--search] text-base-content/80 my-auto me-3 size-5 shrink-0"></span>
      <label class="sr-only" for="searchInput">Full Name</label>
      <input type="search" class="grow" placeholder="Search" id="searchInput" />
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
{{< /code >}}

<!-- With CTA button -->

{{< headname level="3" >}} With CTA button {{< /headname >}}

Below given example displays navbar with call to action button.

{{< code >}}

<nav class="navbar rounded-box flex w-full items-center justify-between gap-2 shadow-base-300/20 shadow-sm">
  <div class="navbar-start max-md:w-1/4">
    <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">
      FlyonUI
    </a>
  </div>
  <div class="navbar-center max-md:hidden">
    <ul class="menu menu-horizontal p-0 font-medium">
      <li><a href="#">Link 1</a></li>
      <li><a href="#">Link 2</a></li>
      <li><a href="#">Link 3</a></li>
    </ul>
  </div>
  <div class="navbar-end items-center gap-4">
    <div class="dropdown relative inline-flex md:hidden">
      <button id="dropdown-default" type="button" class="dropdown-toggle btn btn-text btn-secondary btn-square" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
        <span class="icon-[tabler--menu-2] dropdown-open:hidden size-5"></span>
        <span class="icon-[tabler--x] dropdown-open:block hidden size-5"></span>
      </button>
      <ul class="dropdown-menu dropdown-open:opacity-100 hidden min-w-60" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-default">
        <li><a class="dropdown-item" href="#">Link 1</a></li>
        <li><a class="dropdown-item" href="#">Link 2</a></li>
        <li><a class="dropdown-item" href="#">Link 3</a></li>
      </ul>
    </div>
    <a class="btn max-md:btn-square btn-primary" href="#">
      <span class="max-md:hidden">Get started</span>
      <span class="icon-[tabler--arrow-right] rtl:rotate-180"></span>
    </a>
  </div>
</nav>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Responsive (hamburger) -->

{{< headname level="3" >}} Responsive (hamburger) {{< /headname >}}

The example below demonstrates a responsive navbar that includes a hamburger menu for smaller screens.

{{< code >}}

<nav class="navbar rounded-box shadow-base-300/20 shadow-sm">
  <div class="w-full md:flex md:items-center md:gap-2">
    <div class="flex items-center justify-between">
      <div class="navbar-start items-center justify-between max-md:w-full">
        <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">FlyonUI</a>
        <div class="md:hidden">
          <button type="button" class="collapse-toggle btn btn-outline btn-secondary btn-sm btn-square" data-collapse="#navbar-collapse" aria-controls="navbar-collapse" aria-label="Toggle navigation" >
            <span class="icon-[tabler--menu-2] collapse-open:hidden size-4"></span>
            <span class="icon-[tabler--x] collapse-open:block hidden size-4"></span>
          </button>
        </div>
      </div>
    </div>
    <div id="navbar-collapse" class="md:navbar-end collapse hidden grow basis-full overflow-hidden transition-[height] duration-300 max-md:w-full" >
      <ul class="menu md:menu-horizontal gap-2 p-0 text-base max-md:mt-2">
        <li><a href="#">Link 1</a></li>
        <li><a href="#">Link 2</a></li>
        <li class="dropdown relative inline-flex [--auto-close:inside] [--offset:8] [--placement:bottom-end]">
          <button id="dropdown-link" type="button" class="dropdown-toggle dropdown-open:bg-base-content/10 dropdown-open:text-base-content" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown" >
            Parent
            <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
          </button>
          <ul class="dropdown-menu dropdown-open:opacity-100 hidden" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-link" >
            <li><a class="dropdown-item" href="#">Link 3</a></li>
            <li><a class="dropdown-item" href="#">Link 4</a></li>
            <li><a class="dropdown-item" href="#">Link 5</a></li>
            <hr class="border-base-content/25 -mx-2" />
            <li><a class="dropdown-item" href="#">Link 6</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
{{< /code >}}

<!-- With solid background -->

{{< headname level="3" >}} With solid background {{< /headname >}}

The example below demonstrates a navbar with solid background.

{{< code >}}

<nav class="navbar bg-base-300/30 rounded-box">
  <div class="w-full md:flex md:items-center md:gap-2">
    <div class="flex items-center justify-between">
      <div class="navbar-start items-center justify-between max-md:w-full">
        <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">FlyonUI</a>
        <div class="md:hidden">
          <button type="button" class="collapse-toggle btn btn-outline btn-secondary btn-sm btn-square" data-collapse="#solid-bg-navbar-collapse" aria-controls="solid-bg-navbar-collapse" aria-label="Toggle navigation" >
            <span class="icon-[tabler--menu-2] collapse-open:hidden size-4"></span>
            <span class="icon-[tabler--x] collapse-open:block hidden size-4"></span>
          </button>
        </div>
      </div>
    </div>
    <div id="solid-bg-navbar-collapse" class="md:navbar-end collapse hidden grow basis-full overflow-hidden transition-[height] duration-300 max-md:w-full" >
      <ul class="menu md:menu-horizontal flex-nowrap text-base max-md:mt-2 gap-2 p-px">
        <li><a href="#">Link 1</a></li>
        <li><a href="#">Link 2</a></li>
        <li><a href="#">Link 3</a></li>
      </ul>
    </div>
  </div>
</nav>
{{< /code >}}

<!-- Sticky navbar -->

{{< headname level="3" >}} Sticky navbar {{< /headname >}}

The example below demonstrates a sticky navbar.

{{< code >}}

<div class="relative h-72 w-full">
  <!-- Sticky navbar -->
  <nav class="navbar bg-base-100 md:h-15 absolute start-0 top-0 z-1 shadow-base-300/20 shadow-sm">
    <div class="w-full md:flex md:items-center md:gap-2">
      <div class="flex items-center justify-between max-md:w-full">
        <div class="navbar-start items-center justify-between max-md:w-full">
          <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">FlyonUI</a>
        </div>
        <div class="md:hidden">
          <button type="button" class="collapse-toggle btn btn-outline btn-secondary btn-sm btn-square" data-collapse="#sticky-navbar-collapse" aria-controls="sticky-navbar-collapse" aria-label="Toggle navigation" >
            <span class="icon-[tabler--menu-2] collapse-open:hidden size-4"></span>
            <span class="icon-[tabler--x] collapse-open:block hidden size-4"></span>
          </button>
        </div>
      </div>
      <div id="sticky-navbar-collapse" class="md:navbar-end collapse hidden grow basis-full overflow-hidden transition-[height] duration-300 max-md:w-full" >
        <ul class="menu md:menu-horizontal gap-2 p-0 text-base max-md:mt-2">
          <li><a href="#">Link 1</a></li>
          <li><a href="#">Link 2</a></li>
          <li class="dropdown relative inline-flex [--auto-close:inside] [--offset:10] [--placement:bottom-end]">
            <button id="dropdown-sticky" type="button" class="dropdown-toggle dropdown-open:bg-base-content/10 dropdown-open:text-base-content" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown" >
              Parent
              <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
            </button>
            <ul class="dropdown-menu dropdown-open:opacity-100 hidden" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-sticky" >
              <li><a class="dropdown-item" href="#">Link 3</a></li>
              <li><a class="dropdown-item" href="#">Link 4</a></li>
              <li><a class="dropdown-item" href="#">Link 5</a></li>
              <hr class="border-base-content/25 -mx-2" />
              <li><a class="dropdown-item" href="#">Link 6</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- Demo content -->
  <div class="overflow-y-auto top-15 absolute h-full w-full pe-2 pt-4">
    <div class="flex w-full flex-col gap-4">
      <div class="mb-4 flex items-center gap-4">
        <div class="skeleton h-16 w-16 rounded-full"></div>
        <div class="flex flex-col gap-4">
          <div class="skeleton h-4 w-52"></div>
          <div class="skeleton h-4 w-52"></div>
        </div>
      </div>
      <div class="skeleton mb-4 h-16 w-full"></div>
      <div class="skeleton mb-4 h-32 w-full"></div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Multilevel navigation (collapse) -->

{{< headname level="3" >}} Multilevel navigation (collapse) {{< /headname >}}

The example below demonstrates a navbar with multi level navigation using collapse.

{{< code >}}

<nav class="navbar rounded-box flex w-full gap-2 shadow-base-300/20 shadow-sm">
<div class="w-full md:flex md:items-center md:gap-2">
  <div class="flex items-center justify-between">
    <div class="navbar-start items-center justify-between max-md:w-full">
      <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">
        FlyonUI
      </a>
      <div class="md:hidden">
        <button type="button" class="collapse-toggle btn btn-outline btn-secondary btn-sm btn-square" data-collapse="#multilevel-navbar-collapse" aria-controls="multilevel-navbar-collapse" aria-label="Toggle navigation">
          <span class="icon-[tabler--menu-2] collapse-open:hidden size-4"></span>
          <span class="icon-[tabler--x] collapse-open:block hidden size-4"></span>
        </button>
      </div>
    </div>
  </div>
  <div id="multilevel-navbar-collapse" class="md:navbar-end collapse hidden grow basis-full gap-2 overflow-hidden transition-[height] duration-300 max-md:w-full">
    <div class="dropdown relative inline-flex [--auto-close:inside] [--offset:8] md:[--placement:bottom-end] [--placement:bottom] max-md:mt-2">
      <button id="nested-dropdown" type="button" class="dropdown-toggle btn btn-text text-base-content/80 dropdown-open:bg-base-content/10 dropdown-open:text-base-content max-md:px-2" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
        Pages
        <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
      </button>
      <div class="dropdown-menu dropdown-open:opacity-100 hidden min-w-60" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-collapse">
        <div>
          <a class="dropdown-item" href="#">
            <span class="icon-[tabler--stack-front]"></span>
            Landing page
          </a>
        </div>
        <div>
          <a class="dropdown-item" href="#">
            <span class="icon-[tabler--login]"></span>
            Login page
          </a>
        </div>
        <div>
          <button id="nested-collapse-pages" class="collapse-toggle dropdown-item collapse-open:text-base-content collapse-open:bg-base-content/10 justify-between" data-collapse="#nested-collapse-pages-content">
            <span class="flex items-center gap-x-3.5">
              <span class="icon-[tabler--users]"></span>
              Users
            </span>
            <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
          </button>
          <div class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="nested-collapse-pages" id="nested-collapse-pages-content">
            <ul class="py-3 ps-3">
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  User Details
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Teams
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Projects
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Connections
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div>
          <button id="nested-collapse-pages-2" class="collapse-toggle dropdown-item collapse-open:text-base-content collapse-open:bg-base-content/10 justify-between" data-collapse="#nested-collapse-pages-content-2">
            <span class="flex items-center gap-x-3.5">
              <span class="icon-[tabler--user-pentagon]"></span>
              Account settings
            </span>
            <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
          </button>
          <div class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="nested-collapse-pages-2" id="nested-collapse-pages-content-2">
            <ul class="py-3 ps-3">
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Account
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Security
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Billing & plans
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Notifications
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Memberships
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="dropdown relative inline-flex [--auto-close:inside] [--offset:8] md:[--placement:bottom-end] [--placement:bottom] max-md:mt-2">
      <button id="nested-dropdown" type="button" class="dropdown-toggle btn btn-text text-base-content/80 dropdown-open:bg-base-content/10 dropdown-open:text-base-content max-md:px-2" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
        Apps
        <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
      </button>
      <div class="dropdown-menu dropdown-open:opacity-100 hidden min-w-60" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-collapse">
        <div>
          <a class="dropdown-item" href="#">
            <span class="icon-[tabler--brand-hipchat]"></span>
            Chat
          </a>
        </div>
        <div>
          <a class="dropdown-item" href="#">
            <span class="icon-[tabler--mail]"></span>
            Email
          </a>
        </div>
        <div>
          <button id="nested-collapse" class="collapse-toggle dropdown-item collapse-open:text-base-content collapse-open:bg-base-content/10 justify-between" data-collapse="#nested-collapse-content">
            <span class="flex items-center gap-x-3.5">
              <span class="icon-[tabler--shopping-cart]"></span>
              Ecommerce
            </span>
            <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
          </button>
          <div class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="nested-collapse" id="nested-collapse-content">
            <ul class="py-3 ps-3">
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Dashboard
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Products
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Shipping
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Settings
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div>
          <button id="nested-collapse-2" class="collapse-toggle dropdown-item collapse-open:text-base-content collapse-open:bg-base-content/10 justify-between" data-collapse="#nested-collapse-content-2">
            <span class="flex items-center gap-x-3.5">
              <span class="icon-[tabler--book]"></span>
              Academy
            </span>
            <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
          </button>
          <div class="collapse hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="nested-collapse-2" id="nested-collapse-content-2">
            <ul class="py-3 ps-3">
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Dashboard
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Courses
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Course details
                </a>
              </li>
              <li>
                <a class="dropdown-item" href="#">
                  <span class="icon-[tabler--point]"></span>
                  Certificates
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</nav>
{{< /code >}}

<!-- Multilevel navigation (dropdown) -->

{{< headname level="3" >}} Multilevel navigation (dropdown) {{< /headname >}}

The example below demonstrates a navbar with multi level navigation using dropdown.

{{< code addClass="!block" >}}

<div class="h-96 max-md:h-[31.25rem]">
  <nav class="navbar rounded-box shadow-base-300/20 shadow-sm">
    <div class="navbar-start">
      <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">
        FlyonUI
      </a>
    </div>
    <div class="navbar-center max-md:hidden">
      <ul class="menu menu-horizontal gap-2 p-0 text-base rtl:ml-20">
        <li class="dropdown relative inline-flex [--auto-close:inside] [--offset:9] [--placement:bottom-end]">
          <button id="dropdown-end" type="button" class="dropdown-toggle dropdown-open:bg-base-content/10 dropdown-open:text-base-content max-md:px-2" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
            Products
            <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
          </button>
          <ul class="dropdown-menu dropdown-open:opacity-100 hidden w-48" role="menu" aria-orientation="vertical" aria-labelledby="nested-dropdown">
            <li><a class="dropdown-item" href="#">Templates</a></li>
            <li><a class="dropdown-item" href="#">UI kits</a></li>
            <li class="dropdown relative [--auto-close:inside] [--offset:10] [--placement:right-start]">
              <button id="nested-dropdown-2" class="dropdown-toggle dropdown-item dropdown-open:bg-base-content/10 dropdown-open:text-base-content justify-between" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
                Components
                <span class="icon-[tabler--chevron-right] size-4 rtl:rotate-180"></span>
              </button>
              <ul class="dropdown-menu dropdown-open:opacity-100 hidden w-48" role="menu" aria-orientation="vertical" aria-labelledby="nested-dropdown-2">
                <li><a class="dropdown-item" href="#">Basic</a></li>
                <li>
                  <a class="dropdown-item" href="#">
                    Advanced
                    <span class="badge badge-sm badge-soft badge-primary rounded-full">Pro</span>
                  </a>
                </li>
                <li class="dropdown relative [--auto-close:inside] [--offset:10] rtl:[--placement:left-start] [--placement:right-start]">
                  <button id="nested-dropdown-2" class="dropdown-toggle dropdown-item dropdown-open:bg-base-content/10 dropdown-open:text-base-content justify-between" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
                    Vendor
                    <span class="icon-[tabler--chevron-right] size-4 rtl:rotate-180"></span>
                  </button>
                  <ul class="dropdown-menu dropdown-open:opacity-100 hidden w-48" role="menu" aria-orientation="vertical" aria-labelledby="nested-dropdown-2">
                    <li>
                      <a class="dropdown-item" href="#">
                        Data tables
                        <span class="badge badge-sm badge-soft badge-primary rounded-full">Pro</span>
                      </a>
                    </li>
                    <li>
                      <a class="dropdown-item" href="#">
                        Apex charts
                        <span class="badge badge-sm badge-soft badge-primary rounded-full">Pro</span>
                      </a>
                    </li>
                    <li><a class="dropdown-item" href="#">Clipboard</a></li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>
        </li>
        <li><a href="#">About</a></li>
        <li><a href="#">Careers</a></li>
      </ul>
    </div>
    <div class="navbar-end items-center gap-4">
      <div class="dropdown relative inline-flex [--placement:bottom] md:hidden">
        <button id="dropdown-default" type="button" class="dropdown-toggle btn btn-text btn-secondary btn-square" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
          <span class="icon-[tabler--menu-2] dropdown-open:hidden size-5"></span>
          <span class="icon-[tabler--x] dropdown-open:block hidden size-5"></span>
        </button>
        <ul class="dropdown-menu dropdown-open:opacity-100 hidden min-w-60" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-default">
          <li class="dropdown relative [--auto-close:inside] [--offset:9] [--placement:bottom]">
            <button id="dropdown-end-2" class="dropdown-toggle dropdown-item dropdown-open:bg-base-content/10 dropdown-open:text-base-content justify-between" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
              Products
              <span class="icon-[tabler--chevron-right] size-4 rtl:rotate-180"></span>
            </button>
            <ul class="dropdown-menu dropdown-open:opacity-100 hidden w-48" role="menu" aria-orientation="vertical" aria-labelledby="nested-dropdown">
              <li><a class="dropdown-item" href="#">Templates</a></li>
              <li><a class="dropdown-item" href="#">UI kits</a></li>
              <li class="dropdown relative [--auto-close:inside] [--offset:10] md:[--placement:right-start] [--placement:bottom]">
                <button id="nested-dropdown-2" class="dropdown-toggle dropdown-item dropdown-open:bg-base-content/10 dropdown-open:text-base-content justify-between" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
                  Components
                  <span class="icon-[tabler--chevron-right] size-4 rtl:rotate-180"></span>
                </button>
                <ul class="dropdown-menu dropdown-open:opacity-100 hidden w-48" role="menu" aria-orientation="vertical" aria-labelledby="nested-dropdown-2">
                  <li><a class="dropdown-item" href="#">Basic</a></li>
                  <li>
                    <a class="dropdown-item" href="#">
                      Advanced
                      <span class="badge badge-sm badge-soft badge-primary rounded-full">Pro</span>
                    </a>
                  </li>
                  <li class="dropdown relative [--auto-close:inside] [--offset:10] md:[--placement:right-start] [--placement:bottom]">
                    <button id="nested-dropdown-2" class="dropdown-toggle dropdown-item dropdown-open:bg-base-content/10 dropdown-open:text-base-content justify-between" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
                      Vendor
                      <span class="icon-[tabler--chevron-right] size-4 rtl:rotate-180"></span>
                    </button>
                    <ul class="dropdown-menu dropdown-open:opacity-100 hidden w-48" role="menu" aria-orientation="vertical" aria-labelledby="nested-dropdown-2">
                      <li>
                        <a class="dropdown-item" href="#">
                          Data tables
                          <span class="badge badge-sm badge-soft badge-primary rounded-full">Pro</span>
                        </a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="#">
                          Apex charts
                          <span class="badge badge-sm badge-soft badge-primary rounded-full">Pro</span>
                        </a>
                      </li>
                      <li><a class="dropdown-item" href="#">Clipboard</a></li>
                    </ul>
                  </li>
                </ul>
              </li>
            </ul>
          </li>
          <li><a class="dropdown-item" href="#">About</a></li>
          <li><a class="dropdown-item" href="#">Careers</a></li>
        </ul>
      </div>
      <a class="btn btn-primary" href="#">Login</a>
    </div>
  </nav>
</div>
{{< /code >}}

<!-- With submenu -->

{{< headname level="3" >}} With submenu {{< /headname >}}

The example below demonstrates a navbar with submenu.

{{< code addClass="!block" >}}

<nav class="navbar rounded-t-box gap-4">
  <div class="navbar-start items-center">
    <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#">
      FlyonUI
    </a>
  </div>
  <div class="navbar-end flex items-center gap-4">
    <button class="btn btn-sm btn-text btn-circle size-8.5 md:hidden">
      <span class="icon-[tabler--search] size-5.5"></span>
    </button>
    <div class="input max-md:hidden rounded-full max-w-56">
      <span class="icon-[tabler--search] text-base-content/80 my-auto me-3 size-5 shrink-0"></span>
      <label class="sr-only" for="submenuInput">Full Name</label>
      <input type="search" class="grow" placeholder="Search" id="submenuInput" />
    </div>
    <div class="dropdown relative inline-flex [--auto-close:inside] [--offset:8] [--placement:bottom-end]">
      <button id="dropdown-scrollable" type="button" class="dropdown-toggle flex items-center" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
        <div class="avatar">
          <div class="size-9.5 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar 1" />
          </div>
        </div>
      </button>
      <ul class="dropdown-menu dropdown-open:opacity-100 hidden min-w-52" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-avatar">
        <li class="dropdown-header gap-3 border-0 pt-3">
          <div class="avatar">
            <div class="w-10 rounded-full">
              <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" href="#" alt="avatar 1" />
            </div>
          </div>
          <div>
            <h6 class="text-base-content text-base font-semibold">John Doe</h6>
            <small class="text-base-content/50">Admin</small>
          </div>
        </li>
        <li><hr class="border-base-content/25 -mx-2 " /></li>
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
        <li><hr class="border-base-content/25 -mx-2" /></li>
        <li>
          <a class="dropdown-item btn btn-text btn-error" href="#">
            <span class="icon-[tabler--logout]"></span>
            Sign out
          </a>
        </li>
      </ul>
    </div>
  </div>
</nav>
<div class="bg-base-100 flex w-full items-center">
  <ul class="menu menu-horizontal gap-2 text-base">
    <li><a href="#">Link 1</a></li>
    <li><a href="#">Link 2</a></li>
    <li><a href="#">Link 3</a></li>
  </ul>
</div>
{{< /code >}}

<!-------------------- Mega menu -------------------->

{{< headname level="2" >}} Mega menu {{< /headname >}}

<!-- On click -->

{{< headname level="3" >}} On click {{< /headname >}}

Craft user-friendly Mega Menus with Tailwind CSS, incorporating multi-level dropdown navigation to streamline content access and enhance the browsing experience for website visitors.

The example below shows a navbar that features a mega menu activated by clicking.

{{< code addClass="relative h-fit md:h-[28rem] items-start overflow-y-auto" >}}

<header class=" bg-base-100 flex w-full flex-wrap py-4 text-sm md:flex-nowrap md:justify-start md:py-0">
  <nav class="mx-auto w-full px-4" aria-label="Global">
    <div class="relative md:flex md:items-center">
      <div class="flex items-center justify-between">
        <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#" >
          FlyonUI
        </a>
        <div class="md:hidden">
          <button type="button" class="collapse-toggle btn btn-outline btn-secondary btn-sm btn-square" data-collapse="#navbar-mega-menu-click" aria-controls="navbar-mega-menu-click" aria-label="Toggle navigation" >
            <span class="icon-[tabler--menu-2] collapse-open:hidden size-4"></span>
            <span class="icon-[tabler--x] collapse-open:block hidden size-4"></span>
          </button>
        </div>
      </div>
      <div id="navbar-mega-menu-click" class="collapse hidden grow basis-full overflow-hidden rounded-lg transition-all duration-300 md:block" >
        <div class="flex flex-col rounded-lg max-md:mt-3 max-md:border max-md:p-2 md:flex-row md:items-center md:justify-end md:ps-5 md:pe-0.5 gap-2 max-md:border-base-content/20" >
          <ul class="menu md:menu-horizontal text-base px-0 max-md:w-fit max-md:py-0 gap-2">
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
          </ul>
          <div class="dropdown [--adaptive:none] [--auto-close:inside] [--strategy:static] md:[--strategy:absolute]">
            <button type="button" class="dropdown-toggle btn btn-text text-base-content/80 dropdown-open:bg-base-content/10 dropdown-open:text-base-content max-md:px-3" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
              Mega menu
              <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
            </button>
            <div class="dropdown-menu dropdown-open:opacity-100 start-0 top-full hidden w-full min-w-60 rounded-lg py-2 opacity-0 transition-[opacity,margin] duration-[0.1ms] before:absolute max-md:border max-md:shadow-none max-md:border-base-content/20" role="menu" aria-orientation="vertical">
              <ul class="menu md:menu-horizontal rounded-box w-full max-xl:gap-4 p-0">
                <li>
                  <a href="#" class="menu-title">Services</a>
                  <ul class="menu">
                    <li><a href="#">Design Solutions</a></li>
                    <li><a href="#">Software Development</a></li>
                    <li><a href="#">Web Hosting</a></li>
                    <li><a href="#">Domain Registration</a></li>
                  </ul>
                </li>
                <li>
                  <a href="#" class="menu-title">Corporate Solutions</a>
                  <ul class="menu">
                    <li><a href="#">CRM</a></li>
                    <li><a href="#">Management Solutions</a></li>
                    <li><a href="#">Security Services</a></li>
                    <li><a href="#">Consulting Services</a></li>
                  </ul>
                </li>
                <li>
                  <a href="#" class="menu-title">Product Offerings</a>
                  <ul class="menu">
                    <li><a href="#">UI Kits</a></li>
                    <li><a href="#">Component Library</a></li>
                    <li><a href="#">WordPress Plugins</a></li>
                    <li>
                      <a href="#" class="menu-title">Open Source Projects</a>
                      <ul class="menu">
                        <li><a href="#">Authentication System</a></li>
                        <li><a href="#">FlyonUI Theme</a></li>
                      </ul>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</header>
{{< /code >}}

<!-- On hover -->

{{< headname level="3" >}} On hover {{< /headname >}}

The example below shows a navbar that features a mega menu activated on hover.

{{< code addClass="relative h-fit md:h-[28rem] items-start overflow-y-auto" >}}

<header class="bg-base-100 flex w-full flex-wrap py-2 text-sm md:flex-nowrap md:justify-start md:py-0">
  <nav class="mx-auto w-full px-4" aria-label="Global">
    <div class="relative md:flex md:items-center">
      <div class="flex items-center justify-between">
        <a class="link text-base-content link-neutral text-xl font-bold no-underline" href="#" >
          FlyonUI
        </a>
        <div class="md:hidden">
          <button type="button" class="collapse-toggle btn btn-outline btn-secondary btn-sm btn-square" data-collapse="#navbar-mega-menu-hover" aria-controls="navbar-mega-menu-hover" aria-label="Toggle navigation" >
            <span class="icon-[tabler--menu-2] collapse-open:hidden size-4"></span>
            <span class="icon-[tabler--x] collapse-open:block hidden size-4"></span>
          </button>
        </div>
      </div>
      <div id="navbar-mega-menu-hover" class="collapse hidden grow basis-full overflow-hidden rounded-lg transition-all duration-300 md:block" >
        <div class="flex flex-col rounded-lg max-md:mt-3 max-md:border max-md:p-2 md:flex-row md:items-center md:justify-end gap-2 md:ps-5 md:pe-0.5 md:py-0.5 max-md:border-base-content/20" >
          <ul class="menu md:menu-horizontal p-0 font-medium max-md:w-fit gap-2">
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
          </ul>
          <div class="dropdown [--adaptive:none] [--auto-close:inside] [--strategy:static] [--trigger:hover] md:[--strategy:absolute]" >
            <button type="button" class="dropdown-toggle btn btn-text text-base-content/80 dropdown-open:bg-base-content/10 dropdown-open:text-base-content max-md:px-3" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
              Mega menu
              <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
            </button>
            <div class="dropdown-menu dropdown-open:opacity-100 start-0 top-full hidden w-full min-w-60 rounded-lg p-0 opacity-0 shadow-none transition-[opacity,margin] duration-[0.1ms] before:absolute" role="menu" aria-orientation="vertical">
              <ul class="menu md:menu-horizontal rounded-box w-full max-xl:gap-4 max-md:border shadow-base-300/20 md:shadow-sm max-md:border-base-content/20">
                <li>
                  <a href="#" class="menu-title">Services</a>
                  <ul class="menu">
                    <li><a href="#">Design Solutions</a></li>
                    <li><a href="#">Software Development</a></li>
                    <li><a href="#">Web Hosting</a></li>
                    <li><a href="#">Domain Registration</a></li>
                  </ul>
                </li>
                <li>
                  <a href="#" class="menu-title">Corporate Solutions</a>
                  <ul class="menu">
                    <li><a href="#">CRM</a></li>
                    <li><a href="#">Management Solutions</a></li>
                    <li><a href="#">Security Services</a></li>
                    <li><a href="#">Consulting Services</a></li>
                  </ul>
                </li>
                <li>
                  <a href="#" class="menu-title">Product Offerings</a>
                  <ul class="menu">
                    <li><a href="#">UI Kits</a></li>
                    <li><a href="#">Component Library</a></li>
                    <li><a href="#">WordPress Plugins</a></li>
                    <li>
                      <a href="#" class="menu-title">Open Source Projects</a>
                      <ul class="menu">
                        <li><a href="#">Authentication System</a></li>
                        <li><a href="#">FlyonUI Theme</a></li>
                      </ul>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</header>
{{< /code >}}
