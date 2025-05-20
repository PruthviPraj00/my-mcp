---
title: "Status"
components: 5
description: "The Status component is a compact icon designed to visually indicate the current state of an element, such as online, offline, or error."
bg_image: "svg/components/status.svg"
tag: New
menu:
  main:
    parent: "components"

previous: Stat
previousLink: components/stat/

next: Swap
nextLink: components/swap/
---

<!-- Class table -->

{{< class-table >}}
status | component | Status component
status-primary| color | Status with 'primary' color.
status-secondary| color | Status with 'secondary' color.
status-accent| color | Status with 'accent' color.
status-info| color | Status with 'info' color.
status-success| color | Status with 'success' color.
status-warning| color | Status with 'warning' color.
status-error| color | Status with 'error' color.
status-xs| size | Status with extra small size.
status-sm| size | Status with small size.
status-md| size | Status with medium (Default) size.
status-lg| size | Status with large size.
status-xl| size | Status with extra large size.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic example of `status` component.

{{< code >}}
<span class="status"></span>
{{< /code >}}

<!-------------------- Size -------------------->

{{< headname level="2" >}} Size {{< /headname >}}

<!-- Status Sizes -->

{{< headname level="3" >}} Status Sizes {{< /headname >}}

Status sizes with `status-{xs|sm|md|lg|xl}` utility classes.

{{< code addClass="flex items-center" >}}
<div aria-label="status" class="status status-xs"></div>
<div aria-label="status" class="status status-sm"></div>
<div aria-label="status" class="status status-md"></div>
<div aria-label="status" class="status status-lg"></div>
<div aria-label="status" class="status status-xl"></div>
{{< /code >}}

<!-------------------- Color -------------------->

{{< headname level="2" >}} Color {{< /headname >}}

<!-- Semantic colors -->

{{< headname level="3" >}} Semantic colors {{< /headname >}}

Pre-configured color status designs.

{{< code >}}
<div aria-label="status" class="status status-primary"></div>
<div aria-label="status" class="status status-secondary"></div>
<div aria-label="status" class="status status-accent"></div>
<div aria-label="info" class="status status-info"></div>
<div aria-label="success" class="status status-success"></div>
<div aria-label="warning" class="status status-warning"></div>
<div aria-label="error" class="status status-error"></div>
{{< /code >}}

<!-------------------- Animation -------------------->

{{< headname level="2" >}} Animation {{< /headname >}}

<!-- Bounce Animation -->

{{< headname level="3" >}} Bounce Animation {{< /headname >}}

Use the `animate-bounce` utility to apply a bouncing animation to an element, creating a dynamic up-and-down motion. This effect is useful for drawing attention to interactive elements like buttons, notifications, or alerts.

{{< code >}}
<div class="flex items-center gap-2">
  <div class="status status-info animate-bounce"></div>
  <span>Unread messages</span>
</div>
{{< /code >}}

<!-- Ping Animation -->

{{< headname level="3" >}} Ping Animation {{< /headname >}}

Include the `animate-ping` utility to enable an element to scale and fade, resembling a radar ping or water ripple effect, which is beneficial for features like attention to the alert.

{{< code >}}
<div class="flex items-center gap-2">
  <div class="inline-grid *:[grid-area:1/1]">
    <div class="status status-error animate-ping"></div>
    <div class="status status-error"></div>
  </div>
  <span>Server is down</span>
</div>
{{< /code >}}

<!-- Pulse Animation -->

{{< headname level="3" >}} Pulse Animation {{< /headname >}}

Use the `animate-pulse` utility to make an element pulse, drawing attention to important statuses like alerts or maintenance.

{{< code >}}
<div class="flex items-center gap-2">
  <div class="status status-warning animate-pulse"></div>
  <span>Under Maintenance</span>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Status with progress -->

{{< headname level="3" >}} Status with progress {{< /headname >}}

This example demonstrates how to integrate `status` with `progress` for better task visualization.

{{< code addClass="!block" >}}
<div class="progress mb-4 h-3">
  <div class="progress-bar progress-primary w-1/4 rounded-e-none"></div>
  <div class="progress-bar progress-success w-1/4 rounded-none"></div>
  <div class="progress-bar progress-error w-2/4 rounded-s-none"></div>
</div>
<div class="flex items-center gap-4 *:flex *:items-center *:gap-2">
  <div>
    <div aria-label="status" class="status status-primary"></div>
    <span class="text-primary">Initiated</span>
  </div>
  <div>
    <div aria-label="status" class="status status-success"></div>
    <span class="text-success">In Progress</span>
  </div>
  <div>
    <div aria-label="status" class="status status-error"></div>
    <span class="text-error">Completed</span>
  </div>
</div>
{{< /code >}}
