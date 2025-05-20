---
title: "Menu"
components: 4
description: "The menu component presents a vertical or horizontal list of links for easy navigation within the application or website."
bg_image: "svg/navigations/menu.svg"
menu:
  main:
    parent: "navigations"

previous: Footer
previousLink: navigations/footer/

next: Navbar
nextLink: navigations/navbar/
---

<!-- Class table -->

{{< class-table >}}
menu | component | Base class for menu container.
menu-title | part | Base class for menu title.
menu-disabled | state | Makes menu item (`li`) disabled.
menu-active | state | Makes element inside menu item (`li`) active.
menu-xs | size | Extra small size.
menu-sm | size | Small size.
menu-md | size | Medium(default) size.
menu-lg | size | Large size.
menu-xl | size | Extra-Large size.
menu-vertical | direction | Vertical menu (default).
menu-horizontal | direction | Horizontal menu.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Below example shows default menu component.

{{< code >}}

<ul class="menu">
  <li><a href="#">Home</a></li>
  <li><a href="#">Account</a></li>
  <li><a href="#">Notifications</a></li>
</ul>
{{< /code >}}

<!-------------------- Variants -------------------->

{{< headname level="2" >}} Variants {{< /headname >}}

<!-- Icon menu -->

{{< headname level="3" >}} Icon menu {{< /headname >}}

Below example shows menu with icons.

{{< code >}}

<ul class="menu">
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
</ul>
{{< /code >}}

<!-- With icons only -->

{{< headname level="3" >}} With icons only {{< /headname >}}

Below example shows menu with icons only.

{{< code >}}

<ul class="menu">
  <li>
    <a href="#" aria-label="Home Link"><span class="icon-[tabler--home] size-5"></span></a>
  </li>
  <li>
    <a href="#" aria-label="User Link"><span class="icon-[tabler--user] size-5"></span></a>
  </li>
  <li>
    <a href="#" aria-label="Message Link"><span class="icon-[tabler--message] size-5"></span></a>
  </li>
</ul>
{{< /code >}}

<!-- With icons only (horizontal) -->

{{< headname level="3" >}} With icons only (horizontal) {{< /headname >}}

Use the responsive class `menu-horizontal` with the component class `menu` for a horizontal menu.

Below example shows menu with icons only.

{{< code >}}

<ul class="menu menu-horizontal">
  <li>
    <a href="#" aria-label="Home Link"><span class="icon-[tabler--home] size-5"></span></a>
  </li>
  <li>
    <a href="#" aria-label="User Link"><span class="icon-[tabler--user] size-5"></span></a>
  </li>
  <li>
    <a href="#" aria-label="Message Link"><span class="icon-[tabler--message] size-5"></span></a>
  </li>
</ul>
{{< /code >}}

<!-- With tooltip -->

{{< headname level="3" >}} With tooltip {{< /headname >}}

Below example shows menu with tooltip.

{{< code >}}

<ul class="menu">
  <li class="tooltip [--placement:right]">
    <a href="#" class="tooltip-toggle" aria-label="Home Link"><span class="icon-[tabler--home] size-5"></span></a>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Home</span>
    </span>
  </li>
  <li class="tooltip [--placement:right]">
    <a href="#" class="tooltip-toggle" aria-label="User Link"><span class="icon-[tabler--user] size-5"></span></a>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Account</span>
    </span>
  </li>
  <li class="tooltip [--placement:right]">
    <a href="#" class="tooltip-toggle" aria-label="Message Link"><span class="icon-[tabler--message] size-5"></span></a>
    <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
      <span class="tooltip-body">Notifications</span>
    </span>
  </li>
</ul>
{{< /code >}}

<!-- With disabled items -->

{{< headname level="3" >}} With disabled items {{< /headname >}}

Below example shows menu with disabled items.

{{< code >}}

<ul class="menu">
  <li>
    <a href="#">
      <span class="icon-[tabler--home] size-5"></span>
      Home
    </a>
  </li>
  <li>
    <a href="#">
      <span class="icon-[tabler--settings] size-5"></span>
      Settings
    </a>
  </li>
  <li class="menu-disabled">
    <a href="#">
      <span class="icon-[tabler--lock] size-5"></span>
      Security
    </a>
  </li>
</ul>
{{< /code >}}

<!-- With badges -->

{{< headname level="3" >}} With badges {{< /headname >}}

Below example shows menu with badges.

{{< code >}}

<ul class="menu lg:menu-horizontal">
  <li>
    <a href="#">
      <span class="icon-[tabler--mail] size-5"></span>
      Inbox
      <span class="badge badge-sm badge-primary">1K+</span>
    </a>
  </li>
  <li>
    <a href="#">
      <span class="icon-[tabler--info-circle] size-5"></span>
      Updates
      <span class="badge badge-sm badge-warning">NEW</span>
    </a>
  </li>
  <li>
    <a href="#">

      Status
      <span class="badge badge-success size-3 p-0"></span>
    </a>

  </li>
</ul>
{{< /code >}}

<!-- With active item -->

{{< headname level="3" >}} With active item {{< /headname >}}

Below example shows menu with active item.

{{< code >}}

<ul class="menu">
  <li>
    <a href="#" class="menu-active">
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
</ul>
{{< /code >}}

<!-------------------- Sizes -------------------->

{{< headname level="2" >}} Sizes {{< /headname >}}

<!-- Basic sizes -->

{{< headname level="3" >}} Basic sizes {{< /headname >}}

Utilize the responsive class `menu-{size}` where `size = xs|sm|md|lg|xl` to render menus of varying sizes.

The following example demonstrates menus with different sizes.

{{< code addClass="flex-col" >}}

<ul class="menu menu-xs w-fit">
  <li><a href="#">Home</a></li>
  <li><a href="#">Account</a></li>
  <li><a href="#">Notifications</a></li>
</ul>
<ul class="menu menu-sm w-fit">
  <li><a href="#">Home</a></li>
  <li><a href="#">Account</a></li>
  <li><a href="#">Notifications</a></li>
</ul>
<ul class="menu menu-md w-fit">
  <li><a href="#">Home</a></li>
  <li><a href="#">Account</a></li>
  <li><a href="#">Notifications</a></li>
</ul>
<ul class="menu menu-lg w-fit">
  <li><a href="#">Home</a></li>
  <li><a href="#">Account</a></li>
  <li><a href="#">Notifications</a></li>
</ul>
<ul class="menu menu-xl w-fit">
  <li><a href="#">Home</a></li>
  <li><a href="#">Account</a></li>
  <li><a href="#">Notifications</a></li>
</ul>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Simple -->

{{< headname level="3" >}} Simple {{< /headname >}}

Below example shows simple menu without rounded borders & padding.

{{< code >}}

<ul class="menu rounded-none p-0 [&_li>*]:rounded-none">
  <li><a href="#">Home</a></li>
  <li><a href="#">Account</a></li>
  <li><a href="#">Notifications</a></li>
</ul>
{{< /code >}}

<!-- With title -->

{{< headname level="3" >}} With title {{< /headname >}}

Below example shows menu with title.

{{< code >}}

<ul class="menu">
  <li class="menu-title">Apps</li>
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
  <li>
    <a href="#">
      <span class="icon-[tabler--book] size-5"></span>
      Academy
    </a>
  </li>
</ul>
{{< /code >}}

<!-- With title as parent -->

{{< headname level="3" >}} With title as parent {{< /headname >}}

Below example shows menu with title as parent.

{{< code >}}

<ul class="menu">
  <li>
    <p class="menu-title">Apps</p>
    <ul>
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
      <li>
        <a href="#">
          <span class="icon-[tabler--book] size-5"></span>
          Academy
        </a>
      </li>
    </ul>
  </li>
</ul>
{{< /code >}}

<!-- With sub-menus -->

{{< headname level="3" >}} With sub-menus {{< /headname >}}

Below example shows menu with sub-menus.

{{< code >}}

<ul class="menu">
  <li>
    <a href="#">
      <span class="icon-[tabler--home] size-5"></span>
      Home
    </a>
  </li>
  <li>
    <a href="#">
      <span class="icon-[tabler--apps] size-5"></span>
      Apps
    </a>
    <ul class="menu">
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
      <li>
        <a href="#">
          <span class="icon-[tabler--book] size-5"></span>
          Academy
        </a>
        <ul class="menu">
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
</ul>
{{< /code >}}

<!-- With collapsible sub-menus -->

{{< headname level="3" >}} With collapsible sub-menus {{< /headname >}}

Below example shows menu with collapsible sub-menus.

{{< callout "info" >}}
This example uses collapse to achieve this. Refer to the {{< link link="components/collapse/" addClass="link link-primary" >}}Collapse{{< /link >}} component for more details.
{{< /callout >}}

{{< code addClass="!block h-125" >}}

<ul class="menu w-64 space-y-0.5">
  <li>
    <a href="#">
      <span class="icon-[tabler--home] size-5"></span>
      Home
    </a>
  </li>
  <li class="space-y-0.5">
    <a class="collapse-toggle collapse-open:bg-base-content/10 open" id="menu-app" data-collapse="#menu-app-collapse">
      <span class="icon-[tabler--apps] size-5"></span>
      Apps
      <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4 transition-all duration-300"></span>
    </a>
    <ul id="menu-app-collapse" class="open collapse w-auto space-y-0.5 overflow-hidden transition-[height] duration-300" aria-labelledby="menu-app" >
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
        <a class="collapse-toggle collapse-open:bg-base-content/10 open" id="sub-menu-academy" data-collapse="#sub-menu-academy-collapse" >
          <span class="icon-[tabler--book] size-5"></span>
          Academy
          <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
        </a>
        <ul id="sub-menu-academy-collapse" class="open collapse w-auto space-y-0.5 overflow-hidden transition-[height] duration-300" aria-labelledby="sub-menu-academy" >
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
            <a class="collapse-toggle collapse-open:bg-base-content/10 open" id="sub-menu-academy-stats" data-collapse="#sub-menu-academy-stats-collapse" >
              <span class="icon-[tabler--chart-bar] size-5"></span>
              Stats
              <span class="icon-[tabler--chevron-down] collapse-open:rotate-180 size-4"></span>
            </a>
            <ul id="sub-menu-academy-stats-collapse" class="open collapse w-auto space-y-0.5 overflow-hidden transition-[height] duration-300" aria-labelledby="sub-menu-academy-stats" >
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
</ul>
{{< /code >}}

<!-- With horizontal sub-menu -->

{{< headname level="3" >}} With horizontal sub-menu {{< /headname >}}

Below example shows horizontal menu with sub-menu.

{{< code >}}

<ul class="menu sm:menu-horizontal">
  <li>
    <a href="#">
      <span class="icon-[tabler--home] size-5"></span>
      Home
    </a>
  </li>
  <li>
    <a href="#">
      <span class="icon-[tabler--apps] size-5"></span>
      Apps
    </a>
    <ul class="menu">
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
      <li>
        <a href="#">
          <span class="icon-[tabler--book] size-5"></span>
          Academy
        </a>
      </li>
    </ul>
  </li>
  <li>
    <a href="#">
      <span class="icon-[tabler--settings] size-5"></span>
      Settings
    </a>
  </li>
</ul>
{{< /code >}}

<!-- Mega menu with sub-menu -->

{{< headname level="3" >}} Mega menu with sub-menu {{< /headname >}}

Below example shows mega menu with sub-menu.

{{< code >}}

<ul class="menu sm:menu-horizontal">
  <li>
    <span class="menu-title">Services</span>
    <ul class="menu">
      <li><a href="#">Design Solutions</a></li>
      <li><a href="#">Software Development</a></li>
      <li><a href="#">Web Hosting</a></li>
      <li><a href="#">Domain Registration</a></li>
    </ul>
  </li>
  <li>
    <span class="menu-title">Corporate Solutions</span>
    <ul class="menu">
      <li><a href="#">CRM</a></li>
      <li><a href="#">Management Solutions</a></li>
      <li><a href="#">Security Services</a></li>
      <li><a href="#">Consulting Services</a></li>
    </ul>
  </li>
  <li>
    <span class="menu-title">Product Offerings</span>
    <ul class="menu">
      <li><a href="#">UI Kits</a></li>
      <li><a href="#">Component Library</a></li>
      <li><a href="#">WordPress Plugins</a></li>
      <li>
        <span class="menu-title">Open Source Projects</span>
        <ul class="menu">
          <li><a href="#">Authentication System</a></li>
          <li><a href="#">FlyonUI Theme</a></li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    <span class="menu-title">Company</span>
    <ul class="menu">
      <li><a href="#">About us</a></li>
      <li><a href="#">Contact us</a></li>
      <li><a href="#">Privacy policy</a></li>
      <li><a href="#">Careers</a></li>
    </ul>
  </li>
</ul>
{{< /code >}}

<!-- Menu with dropdown -->

{{< headname level="3" >}} Menu with dropdown {{< /headname >}}

Below example shows menu with dropdown.

{{< code >}}

<ul class="menu menu-horizontal space-x-0.5">
  <li><a href="#">Home</a></li>
  <li><a href="#">Services</a></li>
  <li class="dropdown relative inline-flex [--auto-close:inside] [--offset:9] [--placement:bottom-end]">
    <button id="dropdown-end" type="button" class="dropdown-toggle dropdown-open:bg-base-content/10 dropdown-open:text-base-content max-sm:px-2" aria-haspopup="menu" aria-expanded="false" aria-label="Dropdown">
      Products
      <span class="icon-[tabler--chevron-down] dropdown-open:rotate-180 size-4"></span>
    </button>
    <ul class="dropdown-menu dropdown-open:opacity-100 hidden" role="menu" aria-orientation="vertical" aria-labelledby="dropdown-end">
      <li><a class="dropdown-item" href="#">UI kits</a></li>
      <li><a class="dropdown-item" href="#">Templates</a></li>
      <li><a class="dropdown-item" href="#">Component library</a></li>
      <hr class="border-base-content/25 -mx-2 my-3" />
      <li><a class="dropdown-item" href="#">Figma designs</a></li>
    </ul>
  </li>
</ul>
{{< /code >}}
