---
title: "Context Menu"
description: "Enhance interactivity and user experience on your site by implementing a context menu that offers users relevant actions and options through a right-click."
bg_image: "svg/overlays/context-menu.svg"
components: 1
menu:
  main:
    parent: "overlays"

previous: Tabs & Pills
previousLink: navigations/tabs-pills/

next: Drawer
nextLink: overlays/drawer/

requires_js: true
---

{{< callout "info" >}}
Context menu components are adopted from <a href="https://preline.co/docs/context-menu.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

{{< callout "info" >}}
Note that this component requires the use of the third-party <a href="https://floating-ui.com/" class="link link-primary font-semibold" target="blank">FloatingUI</a> and FlyonUI {{< link link="overlays/dropdown/" addClass="link link-primary font-semibold" >}}Dropdown{{< /link >}} plugin, else you can skip this message if you are already using FlyonUI as a package.
{{< /callout >}}

> We harnessed <a href="https://floating-ui.com/" class="link link-primary font-semibold" target="blank">FloatingUI</a> to supercharge our dropdown experience.

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Utilize `[--trigger:contextmenu]` to activate the context menu.

{{< code  >}}
<div class="dropdown relative inline-flex [--trigger:contextmenu]">
  <div class="dropdown-toggle py-3 px-4 w-60 sm:w-96 h-25 flex justify-center items-center text-sm font-medium rounded-lg border-2 border-dashed border-primary bg-base-100 text-primary shadow-xs">Right click</div>
  <div class="dropdown-menu dropdown-open:opacity-100 hidden min-w-60" role="menu" aria-orientation="vertical" aria-labelledby="default">
    <!-- Core Actions -->
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--arrow-back-up] size-5 shrink-0"></span>
      Reply
    </button>
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--arrow-back-up-double] size-5 shrink-0"></span>
      Reply all
    </button>
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--arrow-forward-up] size-5 shrink-0"></span>
      Forward
    </button>
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--send] size-5 shrink-0"></span>
      Resend
    </button>
    <hr class="border-base-content/25 -mx-2" />
    <!-- Extra Options -->
    <div class="dropdown relative [--offset:15] max-sm:[--placement:bottom-start] [--placement:right-start] [--trigger:hover]">
      <button type="button" class="dropdown-toggle dropdown-item" role="menuitem" tabindex="-1">
        <span class="icon-[tabler--text-plus] size-5 shrink-0"></span>
        More
        <span class="icon-[tabler--chevron-right] rtl:rotate-180 size-5 shrink-0 ms-auto"></span>
      </button>
      <div class="dropdown-menu dropdown-open:opacity-100 hidden min-w-60 before:w-6 before:absolute before:-start-6 before:top-0 before:h-full after:w-6 after:absolute after:-end-6 after:top-0 after:h-full" role="menu" aria-orientation="vertical" aria-labelledby="default">
        <button type="button" class="dropdown-item">
          <span class="icon-[tabler--clipboard-copy] size-5 shrink-0"></span>
          Copy conversation
        </button>
        <button type="button" class="dropdown-item">
          <span class="icon-[tabler--archive] size-5 shrink-0"></span>
          Archive Conversation
        </button>
        <button type="button" class="dropdown-item">
          <span class="icon-[tabler--mail-opened] size-5 shrink-0"></span>
          Move to Folder
        </button>
        <button type="button" class="dropdown-item">
          <span class="icon-[tabler--star] size-5 shrink-0"></span>
          Mark as Important
        </button>
        <button type="button" class="dropdown-item">
          <span class="icon-[tabler--bell-off] size-5 shrink-0"></span>
          Mute Notifications
        </button>
      </div>
    </div>
    <hr class="border-base-content/25 -mx-2" />
    <!-- Status and Other Actions -->
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--mail] size-5 shrink-0"></span>
      Mark as unread
    </button>
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--mail-opened] size-5 shrink-0"></span>
      Mark as read
    </button>
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--archive] size-5 shrink-0"></span>
      Archive
    </button>
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--trash] size-5 shrink-0"></span>
      Delete
    </button>
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--alert-circle] size-5 shrink-0"></span>
      Report Spam
    </button>
    <button type="button" class="dropdown-item">
      <span class="icon-[tabler--file-export] size-5 shrink-0"></span>
      Export Conversation
    </button>
  </div>
</div>
{{< /code >}}
