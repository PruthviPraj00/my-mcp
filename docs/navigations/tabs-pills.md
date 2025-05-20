---
title: "Tabs & Pills"
description: "Tabs allow users to easily switch between different views, providing a seamless and efficient navigation experience."
bg_image: "svg/navigations/tabs-pills.svg"
components: 19
isLanding: true
menu:
  main:
    parent: "navigations"

previous: Stepper
previousLink: navigations/stepper/

next: Context Menu
nextLink: overlays/context-menu/

requires_js: true
pageJS:
  - "/js/pages/tabs-pills.js"
---

{{< callout "info" >}}
Tabs components are adopted from <a href="https://preline.co/docs/tabs.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class Table -->

{{< class-table >}}
tabs | component | Base class for tabs container.
tab | component | Base class for tab items.
tabs-bordered| style| This class adds a bottom border to each tab item.
tabs-lifted | style | This class applies a lifted style to each tab item.
tab-active | state | active state for tabs-bordered and tabs-lifted.
active | state | Enables the selection of a tab to be initially displayed.
active-tab:{tw-utility-class} | variant | The modifier allows setting Tailwind classes when the tab is active for toggle and for content.
tabs-xs|size | Extra small tabs.
tabs-sm|size | Small tabs.
tabs-md|size | Medium(default) tabs.
tabs-lg|size | Large tabs.
tabs-xl|size | Extra large tabs.  
{{< /class-table >}}

<!-- About Tabs -->

{{< headname level="3" >}} About tabs {{< /headname >}}

Utilize the tab JavaScript plugin to improve our navigation tabs and pills, allowing us to create tabbed sections with different content.

For dynamic tabbed interfaces, it's important to include specific elements like `role="tablist"`, `role="tab"`, `role="tabpanel"`, and other attributes as outlined in the [WAI ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/#tabpanel). These help convey the structure and functionality to users who rely on assistive technologies like screen readers. As a good practice, use `button` elements for the tabs instead of links to ensure they trigger changes without navigating to new pages.

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic example of tab.

**Style:**
The `tabs` class serves as the base component for tabbed interfaces, where adding the `tabs-bordered` class gives the tab buttons an underlined appearance. The `tab` class is applied to individual tab buttons, and using the `active` class marks a tab as the initial active tab. The `active-tab:{tw-utility-class}` modifier allows Tailwind utility classes to be applied when the tab is active.

**Functionality:**
The `data-tab` data attribute is used to link each tab button to its corresponding `tabpanel` using an ID. It's crucial to set the `role` attribute on both the `tab` and `tabpanel` elements to ensure proper functionality and accessibility.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-basic-item-1" data-tab="#tabs-basic-1" aria-controls="tabs-basic-1" role="tab" aria-selected="true" >
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-basic-item-2" data-tab="#tabs-basic-2" aria-controls="tabs-basic-2" role="tab" aria-selected="false" >
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-basic-item-3" data-tab="#tabs-basic-3" aria-controls="tabs-basic-3" role="tab" aria-selected="false" >
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-basic-1" role="tabpanel" aria-labelledby="tabs-basic-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-basic-2" class="hidden" role="tabpanel" aria-labelledby="tabs-basic-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-basic-3" class="hidden" role="tabpanel" aria-labelledby="tabs-basic-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code>}}

<!--  Filled -->

{{< headname level="3" >}} Filled {{< /headname >}}

Example with Filled tabs.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active w-full" id="tabs-basic-filled-item-1" data-tab="#tabs-basic-filled-1" aria-controls="tabs-basic-filled-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active w-full" id="tabs-basic-filled-item-2" data-tab="#tabs-basic-filled-2" aria-controls="tabs-basic-filled-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active w-full" id="tabs-basic-filled-item-3" data-tab="#tabs-basic-filled-3" aria-controls="tabs-basic-filled-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-basic-filled-1" role="tabpanel" aria-labelledby="tabs-basic-filled-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-basic-filled-2" class="hidden" role="tabpanel" aria-labelledby="tabs-basic-filled-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-basic-filled-3" class="hidden" role="tabpanel" aria-labelledby="tabs-basic-filled-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code >}}

<!-- Vertical tab -->

{{< headname level="3" >}} Vertical tab {{< /headname >}}

To create vertical tabs, you can use the `tabs-vertical` class. Additionally, you should add a `flex` class to a surrounding `div` to ensure the tabs and their associated content are displayed side by side.

For keyboard accessibility to function properly, please set data-attribute `data-tabs-vertical` to `true`.

{{< code addClass="!block" >}}

<div class="flex">
  <nav class="tabs tabs-bordered tabs-vertical" aria-label="Tabs" role="tablist" data-tabs-vertical="true" aria-orientation="horizontal">
    <button type="button" class="tab active-tab:tab-active active" id="tabs-vertical-item-1" data-tab="#tabs-vertical-1" aria-controls="tabs-vertical-1" role="tab" aria-selected="true">
      Home
    </button>
    <button type="button" class="tab active-tab:tab-active" id="tabs-vertical-item-2" data-tab="#tabs-vertical-2" aria-controls="tabs-vertical-2" role="tab" aria-selected="false">
      Profile
    </button>
    <button type="button" class="tab active-tab:tab-active " id="tabs-vertical-item-3" data-tab="#tabs-vertical-3" aria-controls="tabs-vertical-3" role="tab" aria-selected="false">
      Messages
    </button>
  </nav>

  <div class="ms-3">
    <div id="tabs-vertical-1" role="tabpanel" aria-labelledby="tabs-vertical-item-1">
      <p class="text-base-content/80"> Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here. </p>
    </div>
    <div id="tabs-vertical-2" class="hidden" role="tabpanel" aria-labelledby="tabs-vertical-item-2">
      <p class="text-base-content/80"> This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details. </p>
    </div>
    <div id="tabs-vertical-3" class="hidden" role="tabpanel" aria-labelledby="tabs-vertical-item-3">
      <p class="text-base-content/80"> <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations. </p>
    </div>
  </div>
</div>
{{< /code>}}

<!-------------------- Size variants -------------------->

{{< headname level="2" >}} Size variants {{< /headname >}}

<!-- Extra small tab -->

{{< headname level="3" >}} Extra small tab {{< /headname >}}

Add responsive class `tabs-{size}` where `{size} = xs|sm|md|lg|xl` for tab of different sizes.

{{< code addClass="!block" >}}

<!-- Extra small -->
<nav class="tabs tabs-bordered tabs-xs" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-xs-item-1" data-tab="#tabs-xs-1" aria-controls="tabs-xs-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-xs-item-2" data-tab="#tabs-xs-2" aria-controls="tabs-xs-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-xs-item-3" data-tab="#tabs-xs-3" aria-controls="tabs-xs-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-1.5">
  <div id="tabs-xs-1" role="tabpanel" aria-labelledby="tabs-xs-item-1">
    <p class="text-base-content/80 text-sm">
      Welcome to the
      <span class="text-base-content font-semibold">Home tab!</span>
      Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-xs-2" class="hidden" role="tabpanel" aria-labelledby="tabs-xs-item-2">
    <p class="text-base-content/80 text-sm">
      This is your
      <span class="text-base-content font-semibold">Profile</span>
      tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-xs-3" class="hidden" role="tabpanel" aria-labelledby="tabs-xs-item-3">
    <p class="text-base-content/80 text-sm">
      <span class="text-base-content font-semibold">Messages:</span>
      View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code >}}

<!-- Small tab -->

{{< headname level="3" >}} Small tab {{< /headname >}}

Add responsive class `tabs-{size}` where `{size} = xs|sm|md|lg|xl` for tab of different sizes.

{{< code addClass="!block" >}}

<!-- Small -->
<nav class="tabs tabs-bordered tabs-sm" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-sm-item-1" data-tab="#tabs-sm-1" aria-controls="tabs-sm-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-sm-item-2" data-tab="#tabs-sm-2" aria-controls="tabs-sm-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-sm-item-3" data-tab="#tabs-sm-3" aria-controls="tabs-sm-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-2">
  <div id="tabs-sm-1" role="tabpanel" aria-labelledby="tabs-sm-item-1">
    <p class="text-base-content/80 text-sm">
      Welcome to the
      <span class="text-base-content font-semibold">Home tab!</span>
      Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-sm-2" class="hidden" role="tabpanel" aria-labelledby="tabs-sm-item-2">
    <p class="text-base-content/80 text-sm">
      This is your
      <span class="text-base-content font-semibold">Profile</span>
      tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-sm-3" class="hidden" role="tabpanel" aria-labelledby="tabs-sm-item-3">
    <p class="text-base-content/80 text-sm">
      <span class="text-base-content font-semibold">Messages:</span>
      View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code >}}

<!-- Default tab -->

{{< headname level="3" >}} Default tab {{< /headname >}}

Add responsive class `tabs-{size}` where `{size} = xs|sm|md|lg|xl` for tab of different sizes.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered tabs-md" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-default-item-1" data-tab="#tabs-default-1" aria-controls="tabs-default-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-default-item-2" data-tab="#tabs-default-2" aria-controls="tabs-default-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-default-item-3" data-tab="#tabs-default-3" aria-controls="tabs-default-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-2.5">
  <div id="tabs-default-1" role="tabpanel" aria-labelledby="tabs-default-item-1">
    <p class="text-base-content/80 text-lg">
      Welcome to the
      <span class="text-base-content font-semibold">Home tab!</span>
      Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-default-2" class="hidden" role="tabpanel" aria-labelledby="tabs-default-item-2">
    <p class="text-base-content/80 text-lg">
      This is your
      <span class="text-base-content font-semibold">Profile</span>
      tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-default-3" class="hidden" role="tabpanel" aria-labelledby="tabs-default-item-3">
    <p class="text-base-content/80 text-lg">
      <span class="text-base-content font-semibold">Messages:</span>
      View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code >}}

<!-- Large tab -->

{{< headname level="3" >}} Large tab {{< /headname >}}

Add responsive class `tabs-{size}` where `{size} = xs|sm|md|lg|xl` for tab of different sizes.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered tabs-lg overflow-x-auto" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-large-item-1" data-tab="#tabs-large-1" aria-controls="tabs-large-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-large-item-2" data-tab="#tabs-large-2" aria-controls="tabs-large-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-large-item-3" data-tab="#tabs-large-3" aria-controls="tabs-large-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3.5">
  <div id="tabs-large-1" role="tabpanel" aria-labelledby="tabs-large-item-1">
    <p class="text-base-content/80 text-lg">
      Welcome to the
      <span class="text-base-content font-semibold">Home tab!</span>
      Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-large-2" class="hidden" role="tabpanel" aria-labelledby="tabs-large-item-2">
    <p class="text-base-content/80 text-lg">
      This is your
      <span class="text-base-content font-semibold">Profile</span>
      tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-large-3" class="hidden" role="tabpanel" aria-labelledby="tabs-large-item-3">
    <p class="text-base-content/80 text-lg">
      <span class="text-base-content font-semibold">Messages:</span>
      View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code >}}

<!-- Extra large tab -->

{{< headname level="3" >}} Extra large tab {{< /headname >}}

Add responsive class `tabs-{size}` where `{size} = xs|sm|md|lg|xl` for tab of different sizes.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered tabs-xl overflow-x-auto" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-extra-large-item-1" data-tab="#tabs-extra-large-1" aria-controls="tabs-extra-large-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-extra-large-item-2" data-tab="#tabs-extra-large-2" aria-controls="tabs-extra-large-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-extra-large-item-3" data-tab="#tabs-extra-large-3" aria-controls="tabs-extra-large-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3.5">
  <div id="tabs-extra-large-1" role="tabpanel" aria-labelledby="tabs-extra-large-item-1">
    <p class="text-base-content/80 text-lg">
      Welcome to the
      <span class="text-base-content font-semibold">Home tab!</span>
      Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-extra-large-2" class="hidden" role="tabpanel" aria-labelledby="tabs-extra-large-item-2">
    <p class="text-base-content/80 text-lg">
      This is your
      <span class="text-base-content font-semibold">Profile</span>
      tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-extra-large-3" class="hidden" role="tabpanel" aria-labelledby="tabs-extra-large-item-3">
    <p class="text-base-content/80 text-lg">
      <span class="text-base-content font-semibold">Messages:</span>
      View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code >}}

<!-------------------- Alignment -------------------->

{{< headname level="2" >}} Alignment {{< /headname >}}

<!--  Align center -->

{{< headname level="3" >}} Align center {{< /headname >}}

Centered with TailwindCSS class `justify-center`.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered  justify-center" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-center-item-1" data-tab="#tabs-center-1" aria-controls="tabs-center-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-center-item-2" data-tab="#tabs-center-2" aria-controls="tabs-center-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-center-item-3" data-tab="#tabs-center-3" aria-controls="tabs-center-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-center-1" role="tabpanel" aria-labelledby="tabs-center-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-center-2" class="hidden" role="tabpanel" aria-labelledby="tabs-center-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-center-3" class="hidden" role="tabpanel" aria-labelledby="tabs-center-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code>}}

<!--  Align end -->

{{< headname level="3" >}} Align end {{< /headname >}}

Align at the end TailwindCSS class `justify-end`.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered  justify-end" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-end-item-1" data-tab="#tabs-end-1" aria-controls="tabs-end-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-end-item-2" data-tab="#tabs-end-2" aria-controls="tabs-end-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-end-item-3" data-tab="#tabs-end-3" aria-controls="tabs-end-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-end-1" role="tabpanel" aria-labelledby="tabs-end-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-end-2" class="hidden" role="tabpanel" aria-labelledby="tabs-end-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-end-3" class="hidden" role="tabpanel" aria-labelledby="tabs-end-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code>}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Icons -->

{{< headname level="3" >}} Icons {{< /headname >}}

Below example shows tabs with icons.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered overflow-x-auto" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-icons-item-1" data-tab="#tabs-icons-1" aria-controls="tabs-icons-1" role="tab" aria-selected="true">
    <span class="icon-[tabler--home] size-5 shrink-0 me-2"></span>
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-icons-item-2" data-tab="#tabs-icons-2" aria-controls="tabs-icons-2" role="tab" aria-selected="false">
    <span class="icon-[tabler--user] size-5 shrink-0 me-2"></span>
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-icons-item-3" data-tab="#tabs-icons-3" aria-controls="tabs-icons-3" role="tab" aria-selected="false">
    <span class="icon-[tabler--message] size-5 shrink-0 me-2"></span>
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-icons-1" role="tabpanel" aria-labelledby="tabs-icons-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-icons-2" class="hidden" role="tabpanel" aria-labelledby="tabs-icons-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-icons-3" class="hidden" role="tabpanel" aria-labelledby="tabs-icons-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code>}}

<!-- Badges -->

{{< headname level="3" >}} Badges {{< /headname >}}

Below example shows tabs with badges.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered overflow-x-auto" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-badges-item-1" data-tab="#tabs-badges-1" aria-controls="tabs-badges-1" role="tab" aria-selected="true">
    Home
    <span class="badge badge-soft badge-primary badge-sm ms-2 rounded-full">+99</span>
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-badges-item-2" data-tab="#tabs-badges-2" aria-controls="tabs-badges-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-badges-item-3" data-tab="#tabs-badges-3" aria-controls="tabs-badges-3" role="tab" aria-selected="false">
    Messages
    <span class="badge badge-soft badge-primary badge-sm ms-2 rounded-full">+200</span>
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-badges-1" role="tabpanel" aria-labelledby="tabs-badges-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-badges-2" class="hidden" role="tabpanel" aria-labelledby="tabs-badges-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-badges-3" class="hidden" role="tabpanel" aria-labelledby="tabs-badges-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code >}}

<!-- Lifted tab -->

{{< headname level="3" >}} Lifted tab {{< /headname >}}

Apply the `tabs-lifted` component class along with `tabs` to display the tab in a lifted style.

{{< code addClass="!block" >}}

<nav class="tabs tabs-lifted" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-lifted-item-1" data-tab="#tabs-lifted-1" aria-controls="tabs-lifted-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-lifted-item-2" data-tab="#tabs-lifted-2" aria-controls="tabs-lifted-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-lifted-item-3" data-tab="#tabs-lifted-3" aria-controls="tabs-lifted-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-lifted-1" role="tabpanel" aria-labelledby="tabs-lifted-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-lifted-2" class="hidden" role="tabpanel" aria-labelledby="tabs-lifted-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-lifted-3" class="hidden" role="tabpanel" aria-labelledby="tabs-lifted-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code >}}

<!-- Horizontal scroll -->

{{< headname level="3" >}} Horizontal scroll {{< /headname >}}

When content extends beyond the screen, a horizontal scrollbar ensures the tab bar remains aligned. Apply the `overflow-x-auto` class for a  scrollbar. Resize the window to see an example.

{{< code addClass="!block" >}}

<nav class="tabs tabs-bordered overflow-x-auto" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-scroll-item-1" data-tab="#tabs-scroll-1" aria-controls="#tabs-scroll-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-scroll-item-2" data-tab="#tabs-scroll-2" aria-controls="#tabs-scroll-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-scroll-item-3" data-tab="#tabs-scroll-3" aria-controls="#tabs-scroll-3" role="tab" aria-selected="false">
    Messages
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-scroll-item-4" data-tab="#tabs-scroll-4" aria-controls="#tabs-scroll-4" role="tab" aria-selected="false">
    Settings
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-scroll-item-5" data-tab="#tabs-scroll-5" aria-controls="#tabs-scroll-5" role="tab" aria-selected="false">
    Help
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-scroll-item-6" data-tab="#tabs-scroll-6" aria-controls="#tabs-scroll-6" role="tab" aria-selected="false">
    Notifications
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-scroll-item-7" data-tab="#tabs-scroll-7" aria-controls="#tabs-scroll-7" role="tab" aria-selected="false">
    Feedback
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-scroll-1" role="tabpanel" aria-labelledby="tabs-scroll-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-scroll-2" class="hidden" role="tabpanel" aria-labelledby="tabs-scroll-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-scroll-3" class="hidden" role="tabpanel" aria-labelledby="tabs-scroll-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
  <div id="tabs-scroll-4" class="hidden" role="tabpanel" aria-labelledby="tabs-scroll-item-4">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Settings:</span> Adjust your preferences, manage your account, and configure your privacy settings here.
    </p>
  </div>
  <div id="tabs-scroll-5" class="hidden" role="tabpanel" aria-labelledby="tabs-scroll-item-5">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Help:</span> Find answers to frequently asked questions, get in touch with support, or read through user guides.
    </p>
  </div>
  <div id="tabs-scroll-6" class="hidden" role="tabpanel" aria-labelledby="tabs-scroll-item-6">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Notifications:</span> Manage your notifications, set preferences, and view your notification history.
    </p>
  </div>
  <div id="tabs-scroll-7" class="hidden" role="tabpanel" aria-labelledby="tabs-scroll-item-7">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Feedback:</span> Share your thoughts, report issues, or suggest new features to improve the platform.
    </p>
  </div>
</div>
{{< /code>}}

<!-- Hover -->
{{< headname level="3" >}} Hover {{< /headname >}}

This example demonstrates tabs that dynamically open and close on hover, highlighting the use of `eventType:`.

{{< code   addClass="!block" >}}

<nav class="tabs tabs-bordered" aria-label="Tabs" role="tablist" aria-orientation="horizontal" data-tabs='{
      "eventType": "hover"
    }'>
  <button type="button" class="tab active-tab:tab-active active" id="tabs-hover-item-1" data-tab="#tabs-hover-1" aria-controls="tabs-hover-1" role="tab" aria-selected="true" >
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-hover-item-2" data-tab="#tabs-hover-2" aria-controls="tabs-hover-2" role="tab" aria-selected="false" >
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-hover-item-3" data-tab="#tabs-hover-3" aria-controls="tabs-hover-3" role="tab" aria-selected="false" >
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-hover-1" role="tabpanel" aria-labelledby="tabs-hover-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-hover-2" class="hidden" role="tabpanel" aria-labelledby="tabs-hover-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-hover-3" class="hidden" role="tabpanel" aria-labelledby="tabs-hover-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code>}}

<!-- Destroy/Reinitialize -->

{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}

The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a tab element.

{{< code addClass="!block" jsCode="true" >}}
<nav id="tabs-to-destroy" class="tabs tabs-bordered" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-destroy-item-1" data-tab="#tabs-destroy-1" aria-controls="tabs-destroy-1" role="tab" aria-selected="true" >
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-destroy-item-2" data-tab="#tabs-destroy-2" aria-controls="tabs-destroy-2" role="tab" aria-selected="false" >
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-destroy-item-3" data-tab="#tabs-destroy-3" aria-controls="tabs-destroy-3" role="tab" aria-selected="false" >
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-destroy-1" role="tabpanel" aria-labelledby="tabs-destroy-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-destroy-2" class="hidden" role="tabpanel" aria-labelledby="tabs-destroy-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-destroy-3" class="hidden" role="tabpanel" aria-labelledby="tabs-destroy-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    ;(function () {
      const tabs = document.querySelector('#tabs-to-destroy')
      const destroy = document.querySelector('#destroy-btn')
      const reinit = document.querySelector('#reinit-btn')

      destroy.addEventListener('click', () => {
        const { element } = HSTabs.getInstance(tabs, true)

        element.destroy()

        destroy.setAttribute('disabled', 'disabled')
        reinit.removeAttribute('disabled')
      })

      reinit.addEventListener('click', () => {
        HSTabs.autoInit()

        reinit.setAttribute('disabled', 'disabled')
        destroy.removeAttribute('disabled')
      })
    })()
  });
</script>
{{< /code>}}

<!-------------------- Responsive -------------------->

{{< headname level="2" >}} Responsive {{< /headname >}}

<!-- Select on mobile -->

{{< headname level="3" >}} Select {{< /headname >}}

The demonstration illustrates responsiveness by showcasing how the tabs switch to a select menu on smaller screens.

{{< code addClass="!block" >}}

<select id="tab-select" class="select sm:hidden inline-flex" aria-label="Tabs">
  <option value="#tabs-responsive-1">Home</option>
  <option value="#tabs-responsive-2">Profile</option>
  <option value="#tabs-responsive-3">Messages</option>
</select>

<nav class="tabs tabs-bordered hidden sm:flex" aria-label="Tabs" role="tablist" data-tab-select="#tab-select">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-responsive-item-1" data-tab="#tabs-responsive-1" aria-controls="tabs-responsive-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-responsive-item-2" data-tab="#tabs-responsive-2" aria-controls="tabs-responsive-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-responsive-item-3" data-tab="#tabs-responsive-3" aria-controls="tabs-responsive-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-responsive-1" role="tabpanel" aria-labelledby="tabs-responsive-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-responsive-2" class="hidden" role="tabpanel" aria-labelledby="tabs-responsive-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-responsive-3" class="hidden" role="tabpanel" aria-labelledby="tabs-responsive-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code>}}

<!-------------------- Pill Illustrations -------------------->

{{< headname level="2" >}} Pill Illustrations {{< /headname >}}

<!-- Segments -->

{{< headname level="3" >}} Segments {{< /headname >}}

Below example shows tabs as segments.

{{< code addClass="!block" >}}

<nav class="tabs bg-base-200 rounded-field w-fit space-x-1 overflow-x-auto p-1" aria-label="Tabs" role="tablist" aria-orientation="horizontal" >
  <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary active hover:bg-transparent" id="tabs-segment-item-1" data-tab="#tabs-segment-1" aria-controls="tabs-segment-1" role="tab" aria-selected="true" >
    Home
  </button>
  <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-transparent" id="tabs-segment-item-2" data-tab="#tabs-segment-2" aria-controls="tabs-segment-2" role="tab" aria-selected="false" >
    Profile
  </button>
  <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-transparent" id="tabs-segment-item-3" data-tab="#tabs-segment-3" aria-controls="tabs-segment-3" role="tab" aria-selected="false" >
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-segment-1" role="tabpanel" aria-labelledby="tabs-segment-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-segment-2" class="hidden" role="tabpanel" aria-labelledby="tabs-segment-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-segment-3" class="hidden" role="tabpanel" aria-labelledby="tabs-segment-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code>}}

<!-- Pill with semantic color -->

{{< headname level="3" >}} Pill with semantic color {{< /headname >}}

Use component classes `btn` and `btn-text` to style pills with a button-like appearance.

{{< code addClass="!block" >}}

<nav class="tabs space-x-1 overflow-x-auto" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary active hover:bg-primary/20" id="tabs-pill-item-1" data-tab="#tabs-pill-1" aria-controls="tabs-pill-1" role="tab"> 
    Home 
  </button> 
  <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-primary/20" id="tabs-pill-item-2" data-tab="#tabs-pill-2" aria-controls="tabs-pill-2" role="tab">
    Profile
  </button>
  <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-primary/20" id="tabs-pill-item-3" data-tab="#tabs-pill-3" aria-controls="tabs-pill-3" role="tab">
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-pill-1" role="tabpanel" aria-labelledby="tabs-pill-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-pill-2" class="hidden" role="tabpanel" aria-labelledby="tabs-pill-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-pill-3" class="hidden" role="tabpanel" aria-labelledby="tabs-pill-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code>}}

<!-- Pills with icon-->

{{< headname level="3" >}} Pills with icon{{< /headname >}}

Below example shows pills with icons.

{{< code addClass="!block" >}}

<nav class="tabs overflow-x-auto space-x-1 p-1" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary active hover:bg-primary/20" id="tabs-pill-icon-item-1" data-tab="#tabs-pill-icon-1" aria-controls="tabs-pill-icon-1" role="tab" aria-selected="false">
    <span class="icon-[tabler--home] size-5 shrink-0"></span>
    <span class="hidden sm:inline">Home</span>
  </button>
  <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-primary/20" id="tabs-pill-icon-item-2" data-tab="#tabs-pill-icon-2" aria-controls="tabs-pill-icon-2" role="tab" aria-selected="false">
    <span class="icon-[tabler--user] size-5 shrink-0"></span>
    <span class="hidden sm:inline">Profile</span>
  </button>
  <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-primary/20" id="tabs-pill-icon-item-3" data-tab="#tabs-pill-icon-3" aria-controls="tabs-pill-icon-3" role="tab" aria-selected="false">
    <span class="icon-[tabler--message] size-5 shrink-0"></span>
    <span class="hidden sm:inline">Messages<span>
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-pill-icon-1" role="tabpanel" aria-labelledby="tabs-pill-icon-item-1">
    <p class="text-base-content/80"> 
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here. 
    </p>
  </div>
  <div id="tabs-pill-icon-2" class="hidden" role="tabpanel" aria-labelledby="tabs-pill-icon-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details. 
     </p>
  </div>
  <div id="tabs-pill-icon-3" class="hidden" role="tabpanel" aria-labelledby="tabs-pill-icon-item-3">
    <p class="text-base-content/80"> 
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
     </p>
  </div>
</div>
{{< /code >}}

<!-- Filled pills -->

{{< headname level="3" >}} Filled pills {{< /headname >}}

Below example shows Filled pills.

{{< code addClass="!block" >}}

<nav class="tabs space-x-1 overflow-x-auto" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="grow btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary active hover:bg-primary/20" id="tabs-fill-item-1" data-tab="#tabs-fill-1" aria-controls="tabs-fill-1" role="tab" aria-selected="false">
    Home
  </button>
  <button type="button" class="grow btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-primary/20" id="tabs-fill-item-2" data-tab="#tabs-fill-2" aria-controls="tabs-fill-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="grow btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-primary/20" id="tabs-fill-item-3" data-tab="#tabs-fill-3" aria-controls="tabs-fill-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-fill-1" role="tabpanel" aria-labelledby="tabs-fill-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-fill-2" class="hidden" role="tabpanel" aria-labelledby="tabs-fill-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-fill-3" class="hidden" role="tabpanel" aria-labelledby="tabs-fill-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>
{{< /code>}}

<!-- Vertical Pill  -->

{{< headname level="3" >}} Vertical Pill {{< /headname >}}

For tabs styled with the `tabs-vertical` class and pills styled with Tailwind classes, please make sure they are distinct and not linked.

For keyboard accessibility to function properly, please set data-attribute `data-tabs-vertical` to `true`.

{{< code addClass="!block" >}}

<div class="flex">
  <nav class="tabs flex-col items-start space-y-1" aria-label="Tabs" role="tablist" data-tabs-vertical="true" aria-orientation="horizontal" >
    <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-primary/20 active w-full" id="tabs-pill-vertical-item-1" data-tab="#tabs-pill-vertical-1" aria-controls="tabs-pill-vertical-1" role="tab" aria-selected="true" >
      Home
    </button>
    <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-primary/20 w-full" id="tabs-pill-vertical-item-2" data-tab="#tabs-pill-vertical-2" aria-controls="tabs-pill-vertical-2" role="tab" aria-selected="false" >
      Profile
    </button>
    <button type="button" class="btn btn-text active-tab:bg-primary active-tab:text-white hover:text-primary hover:bg-primary/20 w-full" id="tabs-pill-vertical-item-3" data-tab="#tabs-pill-vertical-3" aria-controls="tabs-pill-vertical-3" role="tab" aria-selected="false" >
      Messages
    </button>
  </nav>

  <div class="ms-3">
    <div id="tabs-pill-vertical-1" role="tabpanel" aria-labelledby="tabs-pill-vertical-item-1">
      <p class="text-base-content/80">
        Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
      </p>
    </div>
    <div id="tabs-pill-vertical-2" class="hidden" role="tabpanel" aria-labelledby="tabs-pill-vertical-item-2">
      <p class="text-base-content/80">
        This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
      </p>
    </div>
    <div id="tabs-pill-vertical-3" class="hidden" role="tabpanel" aria-labelledby="tabs-pill-vertical-item-3">
      <p class="text-base-content/80">
        <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
      </p>
    </div>
  </div>
</div>
{{< /code>}}

<!-------------------- Accessibility notes -------------------->

{{< headname level="2" >}} Accessibility notes {{< /headname >}}

<!-- Keyboard interactions -->

{{< headname level="3" >}} Keyboard interactions {{< /headname >}}

<!-- interactions table -->

{{< table >}}
COMMAND| DESCRIPTION
<kbd class="kbd kbd-sm">Enter</kbd>| Activates the selected tab.

<div class="flex gap-3"><kbd class="kbd kbd-sm">Home</kbd> <kbd class="kbd kbd-sm">End</kbd></div>| Focuses first/last non-disabled item.
<div class="flex gap-3"><kbd class="kbd"><span class="icon-[tabler--caret-up-filled] size-5"></span></kbd> <kbd class="kbd"><span class="icon-[tabler--caret-down-filled] size-5"></span></kbd></div>| Selects the previous/next non-disabled tab in vertical mode.
<div class="flex gap-3"><kbd class="kbd"><span class="icon-[tabler--caret-left-filled] size-5"></span></kbd> <kbd class="kbd"><span class="icon-[tabler--caret-right-filled] size-5"></span></kbd></div>| Selects the previous/next non-disabled tab.
{{< /table >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/tabs.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Options table -->

{{< table >}}

PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
`data-tabs`|Includes configuration options for customizing the behavior and appearance of tabs. Should be incorporated into the tab list.|`-`|`-`
`data-tab` | <span class="text-pretty">Activate a tab by specifying on an element. This must be a valid selector.</span>|`-`|`-`
`:eventType`|Use `hover` to activate tabs on mouseover, or `click` to activate them manually (which is the default setting).|"click" & "hover"|`click`
`data-tab-select`| It accepts an `id` parameter, which allows the select options to function as tabs.| `-` | `-`
<span class="text-nowrap">`data-tabs-vertical`</span> |Enabling this setting facilitates vertical keyboard accessibility. | boolean| `-`
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSTabs` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`destroy()`| Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSTabs.getInstance(target, isInstance)`|<div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
`HSTabs.open(target)`|<div>Opens the element associated to the <code>target</code>.<ul class="m-0"><li>The <code>target</code> must be a Node.</li></ul></div>
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

Below is a demonstration illustrating how to use the public methods. It might seem a bit complex because the `open()` method requires the ID of the button with `role="tab"` and `data-tab="tabpanel-id"`, rather than just the `tabpanel-id`.

In the example below, we've provided the ID `tabs-method-3` and added an event listener to the `openBtn`.

{{< code jsCode="true" addClass="!block" >}}

<nav class="tabs tabs-bordered" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-method-item-1" data-tab="#tabs-method-1" aria-controls="tabs-method-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-method-item-2" data-tab="#tabs-method-2" aria-controls="tabs-method-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-method-item-3" data-tab="#tabs-method-3" aria-controls="tabs-method-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-method-1" role="tabpanel" aria-labelledby="tabs-method-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-method-2" class="hidden" role="tabpanel" aria-labelledby="tabs-method-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-method-3" class="hidden" role="tabpanel" aria-labelledby="tabs-method-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>

<button type="button" class="btn btn-primary mt-3" id="open-btn"> Messages </button>

<!-- Js -->
<script>                        
  window.addEventListener('load', function () {
    const openBtn = document.querySelector('#open-btn')
    
    openBtn.addEventListener('click', () => {
      HSTabs.open(document.querySelector('#tabs-method-item-3'))
    })
  })
</script>

{{< /code>}}

<p class="mb-1.5 not-prose">Open item (static method).</p>

{{< code-highlight lang="js" >}}// This method is used in above example.
const openBtn = document.querySelector('#open-btn');

openBtn.addEventListener('click', () => {
  HSTabs.open(document.querySelector('#tabs-method-item-3'))
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose" id="destroy-method">Destroy instance(public method)</p>

{{< code-highlight lang="js" >}}const { element } = HSTabs.getInstance('#tabs', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION|RETURNED VALUE
`on:change`|Triggered whenever a dropdown menu is opened.| <ul><li><code>el</code> HTMLElement. Toggle button (element that was clicked).</li><li><code>prev</code> string. Previous tab ID.</li><li><code>current</code> string. Current tab ID.</li></ul>

{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

Below, is the demonstration on how to use the event. Apply the ID to the `role=tablist` component class. To test these event, copy the following event into your console and click the button.

{{< code jsCode="true" addClass="!block" >}}

<nav class="tabs tabs-bordered" aria-label="Tabs" role="tablist" id="tabs-event" aria-orientation="horizontal">
  <button type="button" class="tab active-tab:tab-active active" id="tabs-event-item-1" data-tab="#tabs-event-1" aria-controls="tabs-event-1" role="tab" aria-selected="true">
    Home
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-event-item-2" data-tab="#tabs-event-2" aria-controls="tabs-event-2" role="tab" aria-selected="false">
    Profile
  </button>
  <button type="button" class="tab active-tab:tab-active" id="tabs-event-item-3" data-tab="#tabs-event-3" aria-controls="tabs-event-3" role="tab" aria-selected="false">
    Messages
  </button>
</nav>

<div class="mt-3">
  <div id="tabs-event-1" role="tabpanel" aria-labelledby="tabs-event-item-1">
    <p class="text-base-content/80">
      Welcome to the <span class="text-base-content font-semibold">Home tab!</span> Explore the latest updates and news here.
    </p>
  </div>
  <div id="tabs-event-2" class="hidden" role="tabpanel" aria-labelledby="tabs-event-item-2">
    <p class="text-base-content/80">
      This is your <span class="text-base-content font-semibold">Profile</span> tab, where you can update your personal information and manage your account details.
    </p>
  </div>
  <div id="tabs-event-3" class="hidden" role="tabpanel" aria-labelledby="tabs-event-item-3">
    <p class="text-base-content/80">
      <span class="text-base-content font-semibold">Messages:</span> View your recent messages, chat with friends, and manage your conversations.
    </p>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const el = HSTabs.getInstance('#tabs-event')

    el.on('change', ({ el, prev, current }) => {
      console.log('el', el)
      console.log('prev', prev)
      console.log('current', current)
    })
  })
</script>

{{< /code>}}

{{< code-highlight lang="js" >}}const el = HSTabs.getInstance('#tabs-event');

el.on('change', ({ el, prev, current }) => {
  console.log('el', el)
  console.log('prev', prev)
  console.log('current', current)
})
{{< /code-highlight >}}
