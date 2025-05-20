---
title: "Drag & Drop"
description: "Implement drag-and-drop, reorderable lists for modern browsers and touch devices using Sortable.js."
bg_image: "svg/third-party-plugins/drag-drop.svg"
components: 10
menu:
  main:
    parent: "third party plugins"

previous: Datatables
previousLink: third-party-plugins/datatables/

next: File Upload
nextLink: third-party-plugins/file-upload/

pageJS:
  - "/js/pages/sortable.js"

vendorJS:
  - "/vendor/sortablejs/sortablejs.js"
---

{{< callout "warning" >}}
Note that this component requires the use of the third-party <a href="https://sortablejs.github.io/Sortable/" target="_blank" class="link link-warning font-semibold">SortableJs</a> plugins.
{{< /callout >}}

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://sortablejs.github.io/Sortable/" target="_blank" class="link link-primary font-semibold">SortableJs</a> with FlyonUI.

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical w-full mb-12 ps-0">
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        1
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Installation</div>
      <p>Install <code>Install Sortable.js. </code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm install sortablejs{{< /code-highlight >}}
    </div>
    <hr class="rounded-none border-transparent !w-0.5" />
  </li>

  <!-- Include Third-Party JS and CSS -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Include SortableJs JavaScript</div>
      <p>Include the following  JS files in your page:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<body>
  <script src="../path/to/vendor/sortablejs/Sortable.min.js"></script>
</body>{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>
 <!-- SortableJs Initialization & Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        3
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Initialize SortableJs</div>
      <p>Add the SortableJS initialization JavaScript code below the SortableJS JS library inclusion. Set up the Sortable instance to target elements using their <code>id</code> attribute.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}const example1 = document.querySelector('#example')
  Sortable.create(example1, {
    animation: 150,
});{{< /code-highlight >}}
    </div>
  </li>
</ul>

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Simple list example -->

{{< headname level="3" >}} Simple list example {{< /headname >}}

Here’s how a basic drag-and-drop list appears with the simplest markup.

{{< code jsCode="true" >}}

<ul id="list-example" class="border-base-content/25 divide-base-content/25 rounded-md max-w-sm divide-y border *:cursor-move *:p-3 *:flex *:items-center *:gap-3" >
  <li>
    <span class="icon-[tabler--bell] size-4 shrink-0"></span>
    Weekly Insights
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
  <li>
    <span class="icon-[tabler--cloud-download] size-4 shrink-0"></span>
    Resource Center
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
  <li>
    <span class="icon-[tabler--users] size-4 shrink-0"></span>
    Team Collaboration
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
  <li>
    <span class="icon-[tabler--bell] size-4 shrink-0"></span>
    Product Updates
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
  <li>
    <span class="icon-[tabler--users] size-4 shrink-0"></span>
    Community Forum
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
</ul>

<!-- Js -->
<script>
 window.addEventListener('load', () => {
  ;(function () {
    // Basic example
    const listExample = document.querySelector('#list-example')

    if (listExample) {
      Sortable.create(listExample, {
        animation: 150,
        dragClass: '!border-0'
      })
    }
  })()
})

</script>

{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Stats -->

{{< headname level="3" >}} Stats {{< /headname >}}

These stats represent a real-time overview of key business metrics, including orders, revenue, invoices, and shipments

{{< code jsCode="true" >}}

<div id="stat-example" class="grid md:grid-cols-2 gap-6 *:cursor-move">
  <div class="stats max-sm:w-full">
    <div class="stat">
      <div class="avatar avatar-placeholder">
        <div class="bg-success/20 text-success size-10 rounded-full">
          <span class="icon-[tabler--package] size-6"></span>
        </div>
      </div>
      <div class="stat-value mb-1">Order</div>
      <div class="stat-title">7,500 of 10,000 orders</div>
      <div class="progress bg-success/10 h-2" role="progressbar" aria-label="Order Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" >
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
      <div class="progress bg-warning/10 h-2" role="progressbar" aria-label="Revenue Progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100" >
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
      <div class="progress bg-error/10 h-2" role="progressbar" aria-label="Invoice Progressbar" aria-valuenow="73" aria-valuemin="0" aria-valuemax="100" >
        <div class="progress-bar progress-error w-9/12"></div>
      </div>
    </div>
  </div>

  <!-- Shipment Stats -->
  <div class="stats">
    <div class="stat">
      <div class="avatar avatar-placeholder">
        <div class="bg-info/20 text-info size-10 rounded-full">
          <span class="icon-[tabler--truck] size-6"></span>
        </div>
      </div>
      <div class="stat-value mb-1">Shipments</div>
      <div class="stat-title">10,450 of 12,000 shipments</div>
      <div class="progress bg-info/10 h-2" role="progressbar" aria-label="Invoice Progressbar" aria-valuenow="73" aria-valuemin="0" aria-valuemax="100" >
        <div class="progress-bar progress-info w-11/12"></div>
      </div>
    </div>
  </div>
</div>

<!-- Js -->
<script>
 window.addEventListener('load', () => {
  ;(function () {
     // Stat example
    const statExample = document.querySelector('#stat-example')

    if (statExample) {
      Sortable.create(statExample, {
        animation: 150
      })
    }
  })()
})

</script>

{{< /code >}}

<!-- Images -->

{{< headname level="3" >}} Images {{< /headname >}}

This showcases a list of avatars with a drag-and-drop interaction, perfect for user selection or grouping.

{{< code jsCode="true" >}}

<div class="flew-wrap flex items-center gap-3 *:cursor-move" id="image-example">
  <div class="avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-3.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-5.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-7.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-10.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-12.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-15.png" alt="avatar" />
    </div>
  </div>
</div>

<!-- Js -->

<script>
 window.addEventListener('load', () => {
  ;(function () {
    // Image example
    const imageExample = document.querySelector('#image-example')

    if (imageExample) {
      Sortable.create(imageExample, {
        animation: 150
      })
    }
  })()
})

</script>

{{< /code >}}

<!-- Shared -->

{{< headname level="3" >}} Shared {{< /headname >}}

Example of a shared task list with 'Pending' and 'Completed' tasks, each assigned to a user with an avatar.

{{< code jsCode="true" >}}

<div class="bg-base-100 shadow-base-300/20 rounded-box grid w-full grid-cols-1 gap-5 p-4 shadow-sm sm:grid-cols-2">
  <div>
    <p class="text-base-content text-base font-semibold">Pending Tasks</p>
    <ul class="divide-base-content/25 divide-y *:cursor-move *:p-3 *:flex *:items-center" id="pending-tasks">
      <li>
        <span>Design new company logo.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-11.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Prepare quarterly report.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-12.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Schedule team meeting.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-13.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Update client database.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-14.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Plan marketing campaign.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-15.png" alt="avatar" />
          </div>
        </div>
      </li>
    </ul>
  </div>
  <div>
    <p class="text-base-content text-base font-semibold">Completed Tasks</p>
    <ul class="divide-base-content/25 divide-y *:cursor-move *:p-3 *:flex *:items-center" id="completed-tasks">
      <li>
        <span>Launch new website.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-16.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Finalize budget proposal.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-17.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Conduct employee training.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-18.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Organize office relocation.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-19.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Attend industry conference.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-20.png" alt="avatar" />
          </div>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- Js -->

<script>
 window.addEventListener('load', () => {
  ;(function () {
    // shared example
    const pendingTasks = document.querySelector('#pending-tasks')
    const completedTasks = document.querySelector('#completed-tasks')

    if (pendingTasks) {
      Sortable.create(pendingTasks, {
        animation: 150,
        group: 'taskList',
        dragClass: '!border-0'
      })
    }
    if (completedTasks) {
      Sortable.create(completedTasks, {
        animation: 150,
        group: 'taskList',
        dragClass: '!border-0'
      })
    }
  })()
})

</script>

{{< /code >}}

<!-- Cloning -->

{{< headname level="3" >}} Cloning {{< /headname >}}

Example of a cloned task list with 'Pending Tasks' and 'Completed Tasks', each task assigned to a user with an avatar."

{{< code jsCode="true" >}}

<div class="bg-base-100 shadow-base-300/20 rounded-box grid w-full grid-cols-1 gap-5 p-4 shadow-sm sm:grid-cols-2">
  <div>
    <p class="text-base-content text-base font-semibold">Pending Tasks</p>
    <ul class="divide-base-content/25 divide-y *:flex *:cursor-move *:items-center *:p-3" id="clone-source-1">
      <li>
        <span>Develop mobile app prototype.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-21.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Research market trends.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-22.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Organize product launch event.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-23.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Update company policy documents.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-24.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Design promotional materials.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-25.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Prepare investor pitch deck.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-26.png" alt="avatar" />
          </div>
        </div>
      </li>
    </ul>
  </div>
  <div>
    <p class="text-base-content text-base font-semibold">Completed Tasks</p>
    <ul class="divide-base-content/25 divide-y *:flex *:cursor-move *:items-center *:p-3" id="clone-source-2">
      <li>
        <span>Complete quarterly audit.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-29.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Launch social media campaign.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-8.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Train new staff members.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Upgrade office equipment.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-14.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Submit project deliverables.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-18.png" alt="avatar" />
          </div>
        </div>
      </li>
      <li>
        <span>Host client appreciation dinner.</span>
        <div class="avatar ms-auto">
          <div class="size-6 rounded-full">
            <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-7.png" alt="avatar" />
          </div>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- Js -->

<script>
 window.addEventListener('load', () => {
  ;(function () {
    // Clone example
    (cloneSource1 = document.getElementById('clone-source-1')),
    (cloneSource2 = document.getElementById('clone-source-2'))

    if (cloneSource1) {
      Sortable.create(cloneSource1, {
        animation: 150,
        group: {
          name: 'cloneList',
          pull: 'clone',
          revertClone: true
        },
        dragClass: '!border-0'
      })
    }
    if (cloneSource2) {
      Sortable.create(cloneSource2, {
        animation: 150,
        group: {
          name: 'cloneList',
          pull: 'clone',
          revertClone: true
        },
        dragClass: '!border-0'
      })
    }
  })()
})

</script>

{{< /code >}}

<!-- Disabled Sorting -->

{{< headname level="3" >}} Disabled Sorting {{< /headname >}}

Try sorting the pending tasks. It is not possible because it has it's sort option set to false. However, you can still drag from the list on the pending tast to the list on the completed task.

{{< code jsCode="true" >}}

<div class="bg-base-100 shadow-base-300/20 rounded-box grid w-full grid-cols-1 gap-5 p-4 shadow-sm sm:grid-cols-2">
  <div>
    <p class="text-base-content text-base font-semibold">Pending Tasks</p>
    <ul class="divide-base-content/25 divide-y *:flex *:cursor-move *:items-center *:p-3" id="disabled-source-1">
      <li>
        <span>Compile Q4 financial statements.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
      <li>
        <span>Review vendor contracts.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
      <li>
        <span>Test new software deployment.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
      <li>
        <span>Create new onboarding materials.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
      <li>
        <span>Analyze customer satisfaction survey.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
    </ul>
  </div>
  <div>
    <p class="text-base-content text-base font-semibold">Completed Tasks</p>
    <ul class="divide-base-content/25 divide-y *:flex *:cursor-move *:items-center *:p-3" id="disabled-source-2">
      <li>
        <span>Launch internal newsletter.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
      <li>
        <span>Finalize project timeline for new product.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
      <li>
        <span>Conduct annual security audit.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
      <li>
        <span>Hold Q3 review meeting with stakeholders.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
      <li>
        <span>Complete brand style guide.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
      <li>
        <span>Update remote work policy.</span>
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </li>
    </ul>
  </div>
</div>

<!-- Js -->

<script>
 window.addEventListener('load', () => {
  ;(function () {
    // disabled example
    ;(disabledSource1 = document.getElementById('disabled-source-1')),
      (disabledSource2 = document.getElementById('disabled-source-2'))

    if (disabledSource1) {
      Sortable.create(disabledSource1, {
        animation: 150,
        group: {
          name: 'disabledList',
          pull: 'clone',
          put: false // Do not allow items to be put into this list
        },
        sort: false, // To disable sorting: set sort to false
        dragClass: '!border-0'
      })
    }
    if (disabledSource2) {
      Sortable.create(disabledSource2, {
        animation: 150,
        group: 'disabledList',
        dragClass: '!border-0'
      })
    }
  })()
})

</script>

{{< /code >}}

<!-- Handle -->

{{< headname level="3" >}} Handle {{< /headname >}}

Example of a list where items can be rearranged using a draggable handle, allowing only the handle to be used for drag-and-drop functionality.

{{< code jsCode="true" >}}

<ul id="handle-example" class="border-base-content/25 divide-base-content/25 rounded-md max-w-sm divide-y border *:p-3 *:flex *:items-center *:gap-3" >
  <li>
    <span class="icon-[tabler--arrows-move] text-base-content handle me-1.5 size-4 shrink-0 cursor-move"></span>
    <span class="icon-[tabler--bell] size-4 shrink-0"></span>
    Weekly Insights
  </li>
  <li>
    <span class="icon-[tabler--arrows-move] text-base-content handle me-1.5 size-4 shrink-0 cursor-move"></span>
    <span class="icon-[tabler--cloud-download] size-4 shrink-0"></span>
    Resource Center
  </li>
  <li>
    <span class="icon-[tabler--arrows-move] text-base-content handle me-1.5 size-4 shrink-0 cursor-move"></span>
    <span class="icon-[tabler--users] size-4 shrink-0"></span>
    Team Collaboration
  </li>
  <li>
    <span class="icon-[tabler--arrows-move] text-base-content handle me-1.5 size-4 shrink-0 cursor-move"></span>
    <span class="icon-[tabler--bell] size-4 shrink-0"></span>
    Product Updates
  </li>
  <li>
    <span class="icon-[tabler--arrows-move] text-base-content handle me-1.5 size-4 shrink-0 cursor-move"></span>
    <span class="icon-[tabler--users] size-4 shrink-0"></span>
    Community Forum
  </li>
</ul>

<!-- Js -->
<script>
 window.addEventListener('load', () => {
  ;(function () {
     // Handle example
    const handleExample = document.querySelector('#handle-example')

    if (handleExample) {
      Sortable.create(handleExample, {
        animation: 150,
        dragClass: '!border-0',
        handle: '.handle' // handle's class
      })
    }
  })()
})

</script>

{{< /code >}}

<!-- Nested -->

{{< headname level="3" >}} Nested {{< /headname >}}

Example of a nested list where you can drag and drop items to reorder them, even within different levels. Each item has a handle for easy dragging and rearranging.

{{< callout "info" false >}}
<strong>Note:</strong> When using nested Sortables with animation, it’s advisable to set the <code>fallbackOnBody</code> option to <code>true</code>. Additionally, it's recommended to either set the <code>invertSwap</code> option to <code>true</code> or reduce the <code>swapThreshold</code> to a value lower than the default (e.g., 0.65).
{{< /callout >}}

{{< code jsCode="true" >}}

<div id="nested-sortable" class="w-full">
  <div class="nested-sortable-item space-y-1">
    <div class="nested-1 space-y-1">
      <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-100 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
        Item 1.1
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </div>
      <div class="ps-5 space-y-1 nested-sortable-item">
        <div class="nested-2">
          <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200/60 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
            Item 2.1
            <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
          </div>
        </div>
        <div class="nested-2 space-y-1">
          <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200/60 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
            Item 2.2
            <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
          </div>
          <div class="ps-5 space-y-1 nested-sortable-item">
            <div class="nested-3">
              <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
                Item 3.1
                <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
              </div>
            </div>
            <div class="nested-3">
              <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
                Item 3.2
                <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
              </div>
            </div>
            <div class="nested-3">
              <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
                Item 3.3
                <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
              </div>
            </div>
            <div class="nested-3">
              <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
                Item 3.4
                <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
              </div>
            </div>
          </div>
        </div>
        <div class="nested-2">
          <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200/60 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
            Item 2.3
            <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
          </div>
        </div>
        <div class="nested-2">
          <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200/60 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
            Item 2.4
            <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
          </div>
        </div>
      </div>
    </div>
    <div class="nested-1">
      <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-100 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
        Item 1.2
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </div>
    </div>
    <div class="nested-1">
      <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-100 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
        Item 1.3
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </div>
    </div>
    <div class="nested-1 space-y-1">
      <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-100 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
        Item 1.4
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </div>
      <div class="ps-5 space-y-1 nested-sortable-item">
        <div class="nested-2">
          <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200/60 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
            Item 2.1
            <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
          </div>
        </div>
        <div class="nested-2">
          <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200/60 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
            Item 2.2
            <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
          </div>
        </div>
        <div class="nested-2">
          <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200/60 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
            Item 2.3
            <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
          </div>
        </div>
        <div class="nested-2">
          <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-200/60 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
            Item 2.4
            <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
          </div>
        </div>
      </div>
    </div>
    <div class="nested-1">
      <div class="p-3 flex items-center gap-x-3 cursor-move bg-base-100 border border-base-content/25 rounded-lg font-medium text-sm text-base-content/80">
        Item 1.5
        <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
      </div>
    </div>
  </div>
</div>

<!-- Js -->

<script>
 window.addEventListener('load', () => {
  ;(function () {
     // Nested example
    const nestedSortables = document.querySelectorAll('#nested-sortable .nested-sortable-item')

    for (var i = 0; i < nestedSortables.length; i++) {
      Sortable.create(nestedSortables[i], {
        group: 'nested',
        animation: 150,
        fallbackOnBody: true,
        swapThreshold: 0.65
      })
    }
  })()
})

</script>

{{< /code >}}

<!-- Swap -->

{{< headname level="3" >}} Swap {{< /headname >}}

The <a href="https://github.com/SortableJS/Sortable/tree/master/plugins/Swap" target="_blank" class="link link-primary">Swap</a> plugin changes the behaviour of Sortable to allow for items to be swapped with eachother rather than sorted.

{{< code jsCode="true" >}}

<ul id="swap-example" class="border-base-content/25 divide-base-content/25 rounded-md max-w-sm divide-y border *:cursor-move *:p-3 *:flex *:items-center *:gap-3" >
  <li>
    <span class="icon-[tabler--bell] size-4 shrink-0"></span>
    Weekly Insights
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
  <li>
    <span class="icon-[tabler--cloud-download] size-4 shrink-0"></span>
    Resource Center
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
  <li>
    <span class="icon-[tabler--users] size-4 shrink-0"></span>
    Team Collaboration
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
  <li>
    <span class="icon-[tabler--bell] size-4 shrink-0"></span>
    Product Updates
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
  <li>
    <span class="icon-[tabler--users] size-4 shrink-0"></span>
    Community Forum
    <span class="icon-[tabler--grip-vertical] text-base-content ms-auto size-4 shrink-0"></span>
  </li>
</ul>

<!-- Js -->
<script>
 window.addEventListener('load', () => {
  ;(function () {
    // Swap example
    const swapExample = document.querySelector('#swap-example')

    if (swapExample) {
      Sortable.create(swapExample, {
        animation: 150,
        swap: true, // Enable swap plugin
        swapClass: '!text-bg-soft-primary', // The class applied to the hovered swap item
        dragClass: '!border-0'
      })
    }
  })()
})

</script>

{{< /code >}}
