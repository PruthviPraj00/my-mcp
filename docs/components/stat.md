---
title: "Stat"
components: 6
description: "Stat is used to display key data and metrics in a clean and customizable layout."
bg_image: "svg/components/stat.svg"
menu:
  main:
    parent: "components"

previous: Stack
previousLink: components/stack/

next: Status
nextLink: components/status/
---

<!-- Class table -->

{{< class-table >}}
stats | component | A container that holds multiple stat items.
stat | part | Represents an individual stat item.
stat-title | part | Displays the title text for a stat item.
stat-value | part | Shows the numerical or main value of a stat item.
stat-desc | part | Provides additional description text for a stat item.
stat-figure | part | Used for displaying an icon, image, or other graphic element.
stat-actions | part | Contains buttons or input fields related to the stat item.
stats-border | style | Applies a border to the stat.
stats-horizontal | direction | Arranges stat items in a horizontal layout (default).
stats-vertical | direction | Arranges stat items in a vertical layout.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!--  Default  -->

{{< headname level="3" >}} Default {{< /headname >}}

This basic example of stat component.

{{< code >}}

<div class="stats">
  <div class="stat">
    <div class="stat-title">Total Emails Sent</div>
    <div class="stat-value">76,250</div>
    <div class="stat-desc">18% more than last month</div>
  </div>
</div>
{{< /code >}}

<!-------------------- Illustration -------------------->

{{< headname level="2" >}} Illustration {{< /headname >}}

<!-- With avatar -->

{{< headname level="3" >}} With avatar {{< /headname >}}

The example below demonstrates a Stat displaying with avatar.

{{< code >}}

<div class="stats">
  <div class="stat">
    <div class="stat-figure">
      <div class="avatar">
        <div class="size-12 rounded-full">
          <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="User Avatar" />
        </div>
      </div>
    </div>
    <div class="stat-title">Total page views</div>
    <div class="stat-value">89,400</div>
    <div class="stat-desc">21% ↗︎ than last month</div>
  </div>
</div>
{{< /code >}}

<!-- With icons and image -->

{{< headname level="3" >}} With icons and image {{< /headname >}}

The example below demonstrates a Stat displaying with icons and images.

{{< code >}}

<div class="stats">
  <div class="stat">
    <div class="stat-figure text-base-content size-8">
      <span class="icon-[tabler--world] size-8"></span>
    </div>
    <div class="stat-title">Website Traffic</div>
    <div class="stat-value">32K</div>
    <div class="stat-desc">5% ↗︎ than last week</div>
  </div>

  <div class="stat">
    <div class="stat-figure text-base-content size-8">
      <span class="icon-[tabler--users-group] size-8"></span>
    </div>
    <div class="stat-title">New Signups</div>
    <div class="stat-value">1.2K</div>
    <div class="stat-desc">12% increase this month</div>
  </div>

  <div class="stat">
    <div class="stat-figure size-12">
      <div class="avatar">
        <div class="size-12 rounded-full">
          <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="User Avatar"/>
        </div>
      </div>
    </div>
    <div class="stat-value text-success">95%</div>
    <div class="stat-title">Customer Retention</div>
    <div class="stat-desc">Steady over last quarter</div>
  </div>
</div>
{{< /code >}}

<!-- Center item -->

{{< headname level="3" >}} Center item {{< /headname >}}

The example below shows a Stat with a centered item layout.

{{< code >}}

<div class="stats">
  <div class="stat place-items-center">
    <div class="stat-title">Total Sales</div>
    <div class="stat-value">52K</div>
    <div class="stat-desc">From Jan 1st to Feb 1st</div>
  </div>

  <div class="stat place-items-center">
    <div class="stat-title">Active Customers</div>
    <div class="stat-value">8,350</div>
    <div class="stat-desc">↗︎ 150 (1.8%)</div>
  </div>

  <div class="stat place-items-center">
    <div class="stat-title">New Signups</div>
    <div class="stat-value">2,400</div>
    <div class="stat-desc">↘︎ 180 (7%)</div>
  </div>
</div>
{{< /code >}}

<!-- Vertical -->

{{< headname level="3" >}} Vertical {{< /headname >}}

The example below illustrates a vertical Stat layout.

{{< code >}}

<div class="stats stats-vertical">
  <div class="stat">
    <div class="stat-title">Total Invoices</div>
    <div class="stat-value">5,780</div>
    <div class="stat-desc">From Jan 1st to Feb 1st</div>
  </div>

  <div class="stat">
    <div class="stat-title">Paid Invoices</div>
    <div class="stat-value">4,320</div>
    <div class="stat-desc">↗︎ 120 (3%)</div>
  </div>

  <div class="stat">
    <div class="stat-title">Pending Invoices</div>
    <div class="stat-value">1,460</div>
    <div class="stat-desc">↘︎ 80 (5%)</div>
  </div>
</div>
{{< /code >}}

<!-- Responsive -->

{{< headname level="3" >}} Responsive {{< /headname >}}

Use TailwindCSS classes for <a href="https://tailwindcss.com/docs/responsive-design#targeting-a-breakpoint-range" target="_blank" class="link link-primary">responsive design</a>, such as `sm:`, `md:`, `lg:`, `xl:`, and `2xl:`, along with the responsive class `stats-vertical`, to switch the stat alignment to horizontal at specific breakpoints or vice the versa.

{{< code >}}

<div class="stats max-sm:stats-vertical">
  <div class="stat">
    <div class="stat-title">Emails Sent</div>
    <div class="stat-value">58K</div>
    <div class="stat-desc">Jan 1st to Feb 1st</div>
  </div>

  <div class="stat">
    <div class="stat-title">New Subscribers</div>
    <div class="stat-value">3,600</div>
    <div class="stat-desc">↗︎ 450 (14%)</div>
  </div>

  <div class="stat">
    <div class="stat-title">Unsubscribes</div>
    <div class="stat-value">850</div>
    <div class="stat-desc">↘︎ 65 (7%)</div>
  </div>
</div>
{{< /code >}}

<!-- With progress bar -->

{{< headname level="3" >}} With progress bar {{< /headname >}}

The example below shows a Stat with a progress bar.

{{< code >}}

<div class="stats max-sm:w-full">
  <div class="stat">
    <div class="avatar avatar-placeholder">
      <div class="bg-success/20 text-success size-10 rounded-full">
        <span class="icon-[tabler--package] size-6"></span>
      </div>
    </div>
    <div class="stat-value mb-1">Order</div>
    <div class="stat-title">7,500 of 10,000 orders</div>
    <div class="progress bg-success/10 h-2" role="progressbar" aria-label="Order Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
      <div class="progress-bar progress-success w-3/4"></div>
    </div>
  </div>
</div>

<div class="stats max-sm:w-full">
  <div class="stat">
    <div class="avatar avatar-placeholder">
      <div class="bg-warning/20 text-warning size-10 rounded-full">
        <span class="icon-[tabler--cash] size-6"></span>
      </div>
    </div>
    <div class="stat-value mb-1">Revenue</div>
    <div class="stat-title">$45,000 of $100,000</div>
    <div class="progress bg-warning/10 h-2" role="progressbar" aria-label="Revenue Progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100">
      <div class="progress-bar progress-warning w-2/5"></div>
    </div>
  </div>
</div>

<div class="stats max-sm:w-full">
  <div class="stat">
    <div class="avatar avatar-placeholder">
      <div class="bg-error/20 text-error size-10 rounded-full">
        <span class="icon-[tabler--credit-card] size-6"></span>
      </div>
    </div>
    <div class="stat-value mb-1">Invoice</div>
    <div class="stat-title">$18,200 of $25,000</div>
    <div class="progress bg-error/10 h-2" role="progressbar" aria-label="Invoice Progressbar" aria-valuenow="73" aria-valuemin="0" aria-valuemax="100">
      <div class="progress-bar progress-error w-[73%]"></div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- With actions button -->

{{< headname level="3" >}} With actions button {{< /headname >}}

The following example demonstrates the use of an action button within a stat component.

{{< code >}}

<div class="stats max-md:stats-vertical">
  <div class="stat">
    <div class="stat-title">Subscription Plan</div>
    <div class="stat-value">Premium</div>
    <div class="stat-actions">
      <button class="btn btn-sm btn-primary btn-gradient">Upgrade Plan</button>
    </div>
  </div>

  <div class="stat">
    <div class="stat-title">Next Billing Date</div>
    <div class="stat-value">Oct 15, 2024</div>
    <div class="stat-actions flex flex-wrap gap-2">
      <button class="btn btn-sm btn-soft">View Details</button>
      <button class="btn btn-sm btn-warning btn-soft">Change Payment Method</button>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Border layout -->

{{< headname level="3" >}} Border layout {{< /headname >}}

The following example demonstrates a Stat component with a bordered layout using `stats-border`.

{{< code >}}

<div class="stats stats-border shadow-none">
  <div class="stat">
    <div class="stat-title">Total Invoices</div>
    <div class="stat-value">5,780</div>
    <div class="stat-desc">From Jan 1st - Feb 1st</div>
  </div>

  <div class="stat">
    <div class="stat-title">Paid Invoices</div>
    <div class="stat-value">4,320</div>
    <div class="stat-desc">↗︎ 120 (3%)</div>
  </div>

  <div class="stat">
    <div class="stat-title">Pending Invoices</div>
    <div class="stat-value">1,460</div>
    <div class="stat-desc">↘︎ 80 (5%)</div>
  </div>
</div>
{{< /code >}}
