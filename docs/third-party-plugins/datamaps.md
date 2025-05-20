---
title: "Data Maps"
description: "Datamaps are customizable SVG visualizations for the web, providing interactive geospatial insights by converting raw data into visual formats."
bg_image: "svg/third-party-plugins/data-maps.svg"
components: 5
menu:
  main:
    parent: "third party plugins"

previous: Clipboard
previousLink: third-party-plugins/clipboard/

next: Datatables
nextLink: third-party-plugins/datatables/

pageJS:
  - "/js/pages/datamaps.js"

vendorJS:
  - "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"
  - "https://cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min.js"
  - "https://cdn.jsdelivr.net/npm/datamaps@0.5.9/dist/datamaps.all.min.js"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://datamaps.github.io/" target="_blank" class="link link-primary font-semibold">Datamaps JS</a> with FlyonUI.

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical w-full mb-12 ps-0">
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        1
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Install Datamaps</div>
      <p>Install <code>datamaps</code> using npm.</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm i datamaps{{< /code-highlight >}}
    </div>
    <hr class="rounded-none border-transparent !w-0.5" />
  </li>

  <!-- Include Third-party JS -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Include Datamaps JavaScript</div>
      <p>
        To integrate Datamaps, add the following
        <code>&lt;script&gt;</code> 
        tags near the end of your
        <code>&lt;/body&gt;</code>
        section.
      </p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<script src="../path/to/d3/d3.min.js"></script>
<script src="../path/to/topojson/build/topojson.min.js"></script>
<script src="../path/to/datamaps/dist/datamaps.world.min.js"></script>{{< /code-highlight >}}
      <div class="text-base-content my-3 font-semibold">Since no custom CSS overrides are required, you can also use a CDN link.</div>
      <p>Add the following <code>&lt;script&gt;</code> tags near the end of your <code>&lt;/body&gt;</code> section:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/datamaps@0.5.9/dist/datamaps.all.min.js"></script>{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Initialization & Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        3
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Initialize Datamaps</div>
      <p>
        Add the following JavaScript code to initialize Datamaps on a target element using its <code>id</code>, as shown in the <a href="#datamap-example" class="link link-primary">Datamap example</a>. Ensure this script is placed below the Datamaps JS library and in a location where TailwindCSS can monitor it, as mentioned in step 3.
      </p>
      <p>
        For additional options and configurations, refer to the Datamaps JS
        <a href="https://github.com/markmarkoh/datamaps/blob/master/README.md#getting-started" class="link link-primary inline-flex items-center gap-1" target="blank">
          documentation
          <span class="icon-[tabler--external-link]"></span>
        </a>.
      </p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96" lang="html" >}}<script>

;(function () {
  // Dataset containing import and export data for various countries
  const dataSet = {
    CHN: {
      import: {
        value: '11,250',
        percent: '14.5',
        isGrown: true
      },
      export: {
        value: '680',
        percent: '0.5',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'cn'
    },
    DEU: {
      import: {
        value: '9,320',
        percent: '6.1',
        isGrown: true
      },
      export: {
        value: '1,200',
        percent: '6.3',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'de'
    },
    GBR: {
      import: {
        value: '5,050',
        percent: '8.9',
        isGrown: false
      },
      export: {
        value: '2,150',
        percent: '3.7',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'gb'
    },
    IND: {
      import: {
        value: '1,500',
        percent: '18.5',
        isGrown: false
      },
      export: {
        value: '450',
        percent: '12.0',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'in'
    },
    USA: {
      import: {
        value: '480',
        percent: '1.1',
        isGrown: false
      },
      export: {
        value: '1,600',
        percent: '2.5',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'us',
      customName: 'United States'
    },
    CAN: {
      import: {
        value: '2,500',
        percent: '22.0',
        isGrown: true
      },
      export: {
        value: '600',
        percent: '13.0',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'ca'
    },
    AUS: {
      import: {
        value: '1,350',
        percent: '12.0',
        isGrown: true
      },
      export: {
        value: '330',
        percent: '10.0',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'au'
    },
    FRA: {
      import: {
        value: '3,800',
        percent: '16.0',
        isGrown: true
      },
      export: {
        value: '820',
        percent: '15.0',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'fr'
    },
    JPN: {
      import: {
        value: '4,200',
        percent: '21.0',
        isGrown: true
      },
      export: {
        value: '710',
        percent: '18.0',
        isGrown: false
      },
      fillKey: 'MAJOR',
      short: 'jp'
    },
    ITA: {
      import: {
        value: '3,200',
        percent: '14.8',
        isGrown: false
      },
      export: {
        value: '640',
        percent: '12.5',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'it'
    },
    RUS: {
      import: {
        value: '5,600',
        percent: '19.5',
        isGrown: true
      },
      export: {
        value: '1,000',
        percent: '10.5',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'ru'
    },
    MEX: {
      import: {
        value: '2,750',
        percent: '17.5',
        isGrown: false
      },
      export: {
        value: '520',
        percent: '9.2',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'mx'
    },
    ZAF: {
      import: {
        value: '1,800',
        percent: '10.5',
        isGrown: true
      },
      export: {
        value: '450',
        percent: '8.0',
        isGrown: true
      },
      fillKey: 'MAJOR',
      short: 'za'
    }
  }

  // Initialize Datamap
  const dataMap = new Datamap({
    element: document.querySelector('#countries-datamap'), // HTML element to render the map
    projection: 'mercator', // Projection type
    responsive: true, // Enable responsiveness
    fills: {
      defaultFill: `color-mix(in oklab, var(--color-base-200) 60%, transparent)`,
      MAJOR: `color-mix(in oklab, var(--color-neutral) 30%, transparent)`
    },
    data: dataSet, // Country-specific data
    geographyConfig: {
      borderColor: `color-mix(in oklab, var(--color-base-content) 50%, transparent)`, // Border color for countries
      highlightFillColor: `color-mix(in oklab, var(--color-primary) 20%, transparent)`, // Highlight fill color on hover
      highlightBorderColor: `var(--color-primary)`, // Highlight border color on hover
      popupTemplate: function (geo, data) {
        // Popup template for displaying country data
        const growUp = `<span class="icon-[tabler--trending-up] text-success size-4"></span>`
        const growDown = `<span class="icon-[tabler--trending-down] text-error size-4"></span>`
        return `
          <div class="bg-base-100 rounded-lg overflow-hidden shadow-base-300/20 shadow-sm min-w-32 me-2">
            <div class="flex items-center gap-2 bg-base-200 p-2">
              <div class="flex items-center">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
                <span class="fi fi-${data.short.toLowerCase()} h-4 w-5 rounded-sm"></span>
              </div>
              <span class="text-sm font-medium text-base-content">${data.customName || geo.properties.name}</span>
            </div>
            <div class="p-2 space-y-1">
              <div class="flex items-center justify-between text-xs gap-2">
                <div class="text-base-content/80 text-nowrap">Import: <span class="font-medium">${
                  data.import.value
                }M</span></div>
                <span class="flex items-center gap-0.5 ${data.import.isGrown ? 'text-success' : 'text-error'}">${
                  data.import.percent
                }${data.import.isGrown ? growUp : growDown}</span>
              </div>
              <div class="flex items-center justify-between text-xs gap-2">
                <div class="text-base-content/80 text-nowrap">Export: <span class="font-medium">${
                  data.export.value
                }</span>M</div>
                <span class="flex items-center gap-0.5 ${data.export.isGrown ? 'text-success' : 'text-error'}">${
                  data.export.percent
                }${data.export.isGrown ? growUp : growDown}</span>
              </div>
            </div>
          </div>`
      }
    }
  })
  // Event listener for window resize to make Datamap responsive
  window.addEventListener('resize', function () {
    dataMap.resize()
  })
})()

</script>{{< /code-highlight >}}

</div>
  </li>
</ul>

<!-------------------- Basic usage -------------------->

{{< headname level="2" >}} Basic usage {{< /headname >}}

<!-- Datamap example -->

{{< headname level="3" >}} Datamap example {{< /headname >}}

The following example demonstrates the usage of a data map, initialized with the JavaScript code provided above.

{{< code-highlight addClass="mt-6" lang="html" >}}<div id="countries-datamap"></div>{{< /code-highlight >}}

<div class="ring-base-content/25 rounded-box max-xl:overflow-x-auto mb-10 w-full p-4 ring-1 max-xl:pb-20 max-sm:py-24">
  <div id="countries-datamap"></div>
</div>
