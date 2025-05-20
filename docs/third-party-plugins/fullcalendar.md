---
title: "Full Calendar"
description: "FullCalendar is a versatile JavaScript component that offers a dynamic, customizable interface for displaying events in monthly, weekly, or daily views."
bg_image: "svg/third-party-plugins/full-calendar.svg"
components: 5
menu:
  main:
    parent: "third party plugins"

previous: Form Validation
previousLink: third-party-plugins/form-validation/

next: Notyf (Toasts)
nextLink: third-party-plugins/notyf/

pageJS:
  - "/js/pages/fullcalendar.js"

vendorJS:
  - "/vendor/fullcalendar/fullcalendar.js"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://fullcalendar.io/" target="_blank" class="link link-primary font-semibold">FullCalendar JS </a> with FlyonUI.

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
      <p>Install <code>fullcalendar</code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm install fullcalendar{{< /code-highlight >}}
    </div>
    <hr class="rounded-none border-transparent !w-0.5" />
  </li>

  <!-- Include Third-Party JS -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Include FullCalendar JavaScript</div>
      <p>Add the following script to your page:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}} <script src="../path/to/fullcalendar/index.global.js"></script> {{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> A CDN link won't work here because we need to customize the default Vendor CSS to match FlyonUI's design.
      </p>
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Tailwind Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        3
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Update Tailwind Configuration</div>
      <p>Update your <code>tailwind.css</code> file to incorporate the path for the FlyonUI Fullcalendar override CSS.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="css" >}}@import "flyonui/src/vendor/fullcalendar.css";{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Initialization & Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        4
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Initialize FullCalendar</div>
      <p>Add the initialization JavaScript code for FullCalendar after including the FullCalendar JS library:</p>
      <p>For more options and detailed configurations, refer to the FullCalendar JS <a href="https://fullcalendar.io/docs/getting-started" class="link link-primary inline-flex items-center gap-1" target="_blank">documentation <span class="icon-[tabler--external-link]"></span></a>.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="js" >}}
const calendarDefault = new FullCalendar.Calendar(document.getElementById('calendar-container'), {
  initialView: 'dayGridMonth',
  events: [
        // Your events here
  ]
});
calendarDefault.render();{{< /code-highlight >}}
    </div>
  </li>
</ul>

<!-- Class table -->

{{< class-table >}}
fc-event-disabled | state | Makes disabled range to prevent events.
fc-event-primary | color | Makes event of primary variant.
fc-event-secondary | color | Makes event of secondary variant.
fc-event-info | color | Makes event of info variant.
fc-event-success | color | Makes event of success variant.
fc-event-warning | color | Makes event of warning variant.
fc-event-error | color | Makes event of error variant.
{{< /class-table >}}

<!-------------------- Basic usage -------------------->

{{< headname level="2" >}} Basic usage {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default example {{< /headname >}}

The following example demonstrates the usage of a default full calendar, initialized with the JavaScript code provided below.

{{< code jsCode="true" >}}

<div class="card flex not-prose p-4 w-full">
  <div id='calendar' class="w-full"></div>
</div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const calendarDefaultExample = document.getElementById('calendar')
  const eventDay = new Date()
  const calendarDefault = new FullCalendar.Calendar(calendarDefaultExample, {
    initialView: 'dayGridMonth',
    buttonText: {
      today: 'Today'
    },
    events: [
      {
        title: 'Learn JavaScript',
        start: eventDay.toISOString().split('T')[0],
        classNames: ['fc-event-primary']
      }
    ]
  })
})
calendarDefault.render()
</script>

{{< /code >}}

<!-- Custom example -->

{{< headname level="3" >}} Custom example {{< /headname >}}

The following example demonstrates the usage of a custom functional full calendar with event modal, initialized with the JavaScript code provided below.

{{< code jsCode="true" >}}

<div class="card flex not-prose p-4 w-full">
<div id="calendar-custom"></div>
</div>
<!-- Modal Button (Hidden) -->

<button type="button" class="btn hidden" id="modalTrigger"  aria-haspopup="dialog" aria-expanded="false" aria-controls="calendar-event-modal" data-overlay="#calendar-event-modal"></button>

<!-- Modal -->
<div id="calendar-event-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title" id="modalTitle">Event</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#calendar-event-modal"><span class="icon-[tabler--x] size-4"></span></button>
      </div>
      <form id="eventForm">
        <div class="modal-body pt-0">
          <div class="mb-4">
            <label class="label-text" for="eventTitle"> Add event title below </label>
            <input type="text" id="eventTitle" class="input" placeholder="Event title" required />
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-soft btn-secondary" data-overlay="#calendar-event-modal">Close</button>
          <button type="submit" class="btn btn-primary">Save changes</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- Js -->
<script>
document.addEventListener('DOMContentLoaded', function () {
  const calendarCustomExample = document.getElementById('calendar-custom')
  let selectedEvent = null
  let selectedDateInfo = null
  function addDays(date, days) {
    const result = new Date(date)
    result.setDate(result.getDate() + days)
    return result
  }
  function formatDate(date) {
    return date.toLocaleDateString('en-GB', {
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    })
  }
  const today = new Date()
  const events = [
    {
      title: 'Past Event',
      start: addDays(today, -2).toISOString().split('T')[0],
      classNames: ['fc-event-info']
    },
    {
      title: 'All Day Event',
      start: addDays(today, 2).toISOString().split('T')[0],
      classNames: ['fc-event-info']
    },
    {
      title: 'Long Event',
      start: addDays(today, 2).toISOString().split('T')[0],
      end: addDays(today, 5).toISOString().split('T')[0],
      classNames: ['fc-event-primary']
    },
    {
      title: 'Confirm tech stack',
      start: addDays(today, 0).toISOString().split('T')[0] + 'T10:00:00',
      end: addDays(today, 0).toISOString().split('T')[0] + 'T18:00:00',
      classNames: ['fc-event-success']
    },
    {
      groupId: '999',
      title: 'Coding session',
      start: addDays(today, 1).toISOString().split('T')[0] + 'T16:00:00',
      classNames: ['fc-event-secondary']
    },
    {
      groupId: '999',
      title: 'Coding session',
      start: addDays(today, 8).toISOString().split('T')[0] + 'T16:00:00',
      classNames: ['fc-event-secondary']
    },
    {
      title: 'Conference',
      start: addDays(today, 9).toISOString().split('T')[0],
      end: addDays(today, 10).toISOString().split('T')[0],
      classNames: ['fc-event-primary']
    },
    {
      title: 'Meeting',
      start: addDays(today, 9).toISOString().split('T')[0] + 'T10:30:00',
      end: addDays(today, 9).toISOString().split('T')[0] + 'T12:30:00',
      classNames: ['fc-event-error']
    },
    {
      title: 'Lunch',
      start: addDays(today, 9).toISOString().split('T')[0] + 'T12:40:00',
      classNames: ['fc-event-warning']
    },
    {
      title: 'Meeting',
      start: addDays(today, 9).toISOString().split('T')[0] + 'T14:30:00',
      classNames: ['fc-event-error']
    },
    {
      title: 'Picnic',
      start: addDays(today, 12).toISOString().split('T')[0],
      classNames: ['fc-event-success']
    },
    {
      title: 'Yoga',
      start: addDays(today, 15).toISOString().split('T')[0],
      classNames: ['fc-event-info']
    },
    {
      title: 'Credit Card Payment',
      start: addDays(today, 23).toISOString().split('T')[0],
      end: addDays(today, 24).toISOString().split('T')[0],
      classNames: ['fc-event-warning']
    },
    {
      title: 'Meeting with client',
      start: addDays(today, 27).toISOString().split('T')[0],
      classNames: ['fc-event-success']
    },
    {
      start: addDays(today, 17).toISOString().split('T')[0],
      end: addDays(today, 20).toISOString().split('T')[0],
      display: 'background',
      classNames: ['fc-event-disabled']
    }
  ]
  const calendarCustom = new FullCalendar.Calendar(calendarCustomExample, {
    initialView: 'dayGridMonth',
    initialDate: today.toISOString().split('T')[0],
    editable: true,
    dragScroll: true,
    dayMaxEvents: 2,
    direction: 'ltr', // use 'rtl' for right-to-left language support
    eventResizableFromStart: true,
    selectable: true,
    headerToolbar: {
      left: 'prev,next title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
    },
    buttonText: {
      month: 'Month',
      week: 'Week',
      day: 'Day',
      list: 'List'
    },
    events: events,
    select: function (info) {
      // Check if the selected range overlaps with the blocked range
      const blockedStart = addDays(today, 17).getTime()
      const blockedEnd = addDays(today, 20).getTime()
      const selectedStart = info.start.getTime()
      const selectedEnd = info.end ? info.end.getTime() : selectedStart
      if (
        (selectedStart < blockedEnd && selectedEnd > blockedStart) ||
        (selectedEnd > blockedStart && selectedStart < blockedEnd)
      ) {
        alert('Events cannot be added in the blocked date range.')
        calendarCustom.unselect()
        return
      }
      selectedEvent = null
      selectedDateInfo = info
      document.getElementById('modalTitle').textContent = `${formatDate(info.start)}`
      document.getElementById('eventForm').reset()
      document.getElementById('modalTrigger').click()
    },
    eventClick: function (info) {
      selectedEvent = info.event
      document.getElementById('modalTitle').textContent = `${formatDate(info.event.start)}`
      document.getElementById('eventTitle').value = info.event.title
      document.getElementById('modalTrigger').click()
    },
    eventTimeFormat: {
      hour: '2-digit',
      minute: '2-digit',
      hour12: false // This will use the 24-hour format
    },
    allDayText: 'All day'
  })
  calendarCustom.render()
  document.getElementById('eventForm').addEventListener('submit', function (e) {
    e.preventDefault()
    const title = document.getElementById('eventTitle').value
    if (title) {
      if (selectedEvent) {
        selectedEvent.setProp('title', title)
      } else {
        calendarCustom.addEvent({
          title: title,
          start: selectedDateInfo.startStr,
          end: selectedDateInfo.endStr,
          allDay: true
        })
      }
      HSOverlay.close('#calendar-event-modal')
    }
  })
})
</script>

{{< /code >}}
