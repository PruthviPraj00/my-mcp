---
title: "Apex charts"
description: "Charts are visual tools that simplify complex data sets, making information more accessible. They include line, bar, and pie charts for specific trends."
bg_image: "svg/third-party-plugins/apex-charts.svg"
components: 16
isLanding: true
menu:
  main:
    parent: "third party plugins"

previous: Animation
previousLink: third-party-plugins/animation/

next: Clipboard
nextLink: third-party-plugins/clipboard/

pageJS:
  - "/js/helper/helper-apexcharts.js"
  - "/js/pages/apexcharts.js"

vendorJS:
  - "https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"
  - "/vendor/apexcharts/apexcharts.js"

vendorCSS:
  - "/vendor/apexcharts/apexcharts.css"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://apexcharts.com/docs/installation/" target="_blank" class="link link-primary">Apexcharts JS</a> with FlyonUI.

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical mb-12 w-full ps-0">
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        1
      </span>
    </div>
    <div class="timeline-end mb-0 ms-1 w-full rounded-lg p-4 pt-1">
      <div class="text-base-content mb-3 font-semibold">Install Required Packages</div>
      <p>Install <code>apexcharts</code> and <code>lodash</code> via npm. The <code>lodash</code> library is required by certain JavaScript helpers for ApexCharts, so ensure both packages are installed.</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}npm i apexcharts lodash{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Third-party JS and CSS include -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 ms-1 w-full rounded-lg p-4 pt-1">
      <div class="text-base-content mb-3 font-semibold">Include ApexCharts JavaScript and CSS</div>
      <p>Add the required ApexCharts CSS and JS files to your page in the following locations:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<head>
  <link rel="stylesheet" href="../path/to/apexcharts/apexcharts.css" />
</head>
<body>
  <script src="../path/to/lodash/lodash.js"></script>
  <script src="../path/to/apexcharts/dist/apexcharts.js"></script>
</body>
{{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> A CDN link won't work here because we need to modify the default Vendor CSS to fit FlyonUI's design.
      </p>
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Helper JS -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        3
      </span>
    </div>
    <div class="timeline-end mb-0 ms-1 w-full rounded-lg p-4 pt-1">
      <div class="text-base-content mb-3 font-semibold">Add the ApexCharts Helper JavaScript (optional)</div>
      <p>The <code>Helper.js</code> file provides four custom tooltip functions and an auto-initialization feature for ApexCharts. To use it, include the <code>helper-apexcharts.js</code> script after the <code>apexcharts.js</code> script.</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}<script src="./node_modules/flyonui/dist/helper-apexcharts.js"></script>{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Update Tailwind Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        4
      </span>
    </div>
    <div class="timeline-end mb-0 ms-1 w-full rounded-lg p-4 pt-1">
      <div class="text-base-content mb-3 font-semibold">Update Tailwind Configuration</div>
      <p>Update your <code>tailwind.css</code> file to incorporate the path for the FlyonUI Apex Charts override CSS.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96" lang="css" >}}@import "flyonui/src/vendor/apexcharts.css";{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Basic Usage -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        5
      </span>
    </div>
    <div class="timeline-end mb-0 ms-1 w-full rounded-lg p-4 pt-1">
      <div class="text-base-content mb-3 font-semibold">Basic Usage</div>
      <p>Use the method below to create an ApexCharts instance. This method contains all necessary settings, specifications, and styles for the chart.</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="js" >}}// helper.js
buildChart('#id', mode => ({ /* Chart details */ }))

// Default Apexchart init
const areaChartEl = document.querySelector('#id'),
areaChartConfig = {
  ...
}
if (typeof areaChartEl !== undefined && areaChartEl !== null) {
  const areaChart = new ApexCharts(areaChartEl, areaChartConfig)
  areaChart.render()
}{{< /code-highlight >}}
    </div>
  </li>
</ul>
<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Single area chart -->

{{< headname level="3" >}} Single area chart {{< /headname >}}

The example below demonstrates how to use a single area chart with Helper.js.

{{< callout "info" false >}}
When working with colors, use CSS variables, for example: `'var(--color-primary)'`. This ensures that when the theme changes, the chart colors update automatically.
{{< /callout >}}

{{< code hasRTL="false" jsCode="true" >}}

<div id="apex-single-area-chart" class="w-full"></div>
<!-- Js -->

<script>
window.addEventListener('load', () => {
  ;(function () {
    // Apex Single Area Chart (Start)
    buildChart('#apex-single-area-chart', mode => ({
      chart: {
        height: 400,
        type: 'area',
        toolbar: {
          show: false
        },
        zoom: {
          enabled: false
        }
      },
      series: [
        {
          name: 'Units',
          data: [0, 100, 50, 125, 70, 150, 100, 170, 120, 175, 100, 200]
        }
      ],
      legend: {
        show: false
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'straight',
        width: 2
      },
      grid: {
        strokeDashArray: 2,
        borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)'
      },
      colors: ['var(--color-primary)'], // color var
      fill: {
        type: 'gradient',
        gradient: {
          shadeIntensity: 1,
          opacityFrom: 0.7,
          gradientToColors: ['var(--color-base-100)'],
          opacityTo: 0.3,
          stops: [0, 90, 100]
        }
      },
      xaxis: {
        type: 'category',
        tickPlacement: 'on',
        categories: [
          '1 March 2024',
          '2 March 2024',
          '3 March 2024',
          '4 March 2024',
          '5 March 2024',
          '6 March 2024',
          '7 March 2024',
          '8 March 2024',
          '9 March 2024',
          '10 March 2024',
          '11 March 2024',
          '12 March 2024'
        ],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        tooltip: {
          enabled: false
        },
        labels: {
          style: {
            colors: 'var(--color-base-content)',
            fontSize: '12px',
            fontWeight: 400
          },
          formatter: title => {
            let t = title

            if (t) {
              const newT = t.split(' ')
              t = `${newT[0]} ${newT[1].slice(0, 3)}`
            }

            return t
          }
        }
      },
      yaxis: {
        labels: {
          align: 'left',
          minWidth: 0,
          maxWidth: 140,
          style: {
            colors: 'var(--color-base-content)',
            fontSize: '12px',
            fontWeight: 400
          },
          formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
        }
      },
      tooltip: {
        x: {
          format: 'MMMM yyyy'
        },
        y: {
          formatter: value => `${value >= 1000 ? `${value / 1000}k` : value}`
        },
        custom: function (props) {
          const { categories } = props.ctx.opts.xaxis
          const { dataPointIndex } = props
          const title = categories[dataPointIndex].split(' ')
          const newTitle = `${title[0]} ${title[1]}`

          return buildTooltip(props, {
            title: newTitle,
            mode,
            valuePrefix: '',
            hasTextLabel: true,
            markerExtClasses: 'bg-primary',
            wrapperExtClasses: ''
          })
        }
      },
      responsive: [
        {
          breakpoint: 568,
          options: {
            chart: {
              height: 300
            },
            labels: {
              style: {
                fontSize: '10px',
                colors: 'var(--color-base-content)'
              },
              offsetX: -2,
              formatter: title => title.slice(0, 3)
            },
            yaxis: {
              labels: {
                align: 'left',
                minWidth: 0,
                maxWidth: 140,
                style: {
                  fontSize: '10px',
                  colors: 'var(--color-base-content)'
                },
                formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
              }
            }
          }
        }
      ]
    }))
    // Apex Single Area Chart (End)
   })()
})
</script>

{{< /code >}}

<!-- Without helper js -->

{{< headname level="3" >}} Without helper js {{< /headname >}}

Helper.js offers four different tooltip designs and includes an auto-init function, eliminating the need for manual initialization. However, if you prefer, you can remove the Helper.js file and use the default Apex chart initialization. Below is an example, but keep in mind that you will need to enable the vendor option in the config file for CSS generation.

{{< code hasRTL="false" addClass="!block" jsCode="true" >}}

<div id="lineAreaChart"></div>

<!-- Js -->
<script>
window.addEventListener('load', () => {
  ;(function () {
    const areaChartEl = document.querySelector('#lineAreaChart'),
      areaChartConfig = {
        chart: {
          height: 400,
          width: '100%',
          type: 'area',
          parentHeightOffset: 0,
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          show: false,
          curve: 'straight'
        },
        legend: {
          show: true,
          position: 'top',
          horizontalAlign: 'start',
          labels: {
            colors: 'var(--color-base-content)',
            useSeriesColors: false
          }
        },
        grid: {
          borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)',
          xaxis: {
            lines: {
              show: true
            }
          }
        },
        colors: [
          'color-mix(in oklab, var(--color-success) 30%, transparent)',
          'color-mix(in oklab, var(--color-success) 60%, transparent)',
          'color-mix(in oklab, var(--color-success) 90%, transparent)'
        ],
        series: [
          {
            name: 'Visits',
            data: [100, 120, 90, 170, 130, 160, 140, 240, 220, 180, 270, 280, 375]
          },
          {
            name: 'Clicks',
            data: [60, 80, 70, 110, 80, 100, 90, 180, 160, 140, 200, 220, 275]
          },
          {
            name: 'Sales',
            data: [20, 40, 30, 70, 40, 60, 50, 140, 120, 100, 140, 180, 220]
          }
        ],
        xaxis: {
          categories: [
            '7/12',
            '8/12',
            '9/12',
            '10/12',
            '11/12',
            '12/12',
            '13/12',
            '14/12',
            '15/12',
            '16/12',
            '17/12',
            '18/12',
            '19/12',
            '20/12'
          ],
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          labels: {
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '13px'
            }
          }
        },
        yaxis: {
          labels: {
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '13px'
            }
          }
        },
        fill: {
          opacity: 1,
          type: 'solid'
        },
        tooltip: {
          shared: false
        }
      }
    if (typeof areaChartEl !== undefined && areaChartEl !== null) {
      const areaChart = new ApexCharts(areaChartEl, areaChartConfig)
      areaChart.render()
    }
   })()
})
</script>

{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Multiple area charts -->

{{< headname level="3" >}} Multiple area charts {{< /headname >}}

The following example demonstrates the usage of a multiple area charts.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-multiple-area-charts"></div>

<!-- Js -->
<script>
window.addEventListener('load', () => {
  ;(function () {
    buildChart('#apex-multiple-area-charts', mode => ({
      chart: {
        height: 400,
        type: 'area',
        toolbar: {
          show: false
        },
        zoom: {
          enabled: false
        }
      },
      series: [
        {
          name: 'Earnings',
          data: [1400, 1500, 1600, 1700, 1800, 2000, 1900, 2000, 2000, 2000, 2300, 2500]
        },
        {
          name: 'Costs',
          data: [1000, 1600, 1400, 1300, 1400, 1300, 1500, 1400, 1400, 1200, 1800, 1800]
        }
      ],
      legend: {
        show: true,
        position: 'top',
        horizontalAlign: 'right',
        labels: {
          useSeriesColors: true
        }
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'straight',
        width: 2
      },
      grid: {
        strokeDashArray: 2,
        borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)'
      },
      colors: ['var(--color-primary)', 'var(--color-warning)'],
      fill: {
        type: 'gradient',
        gradient: {
          shadeIntensity: 1,
          opacityFrom: 0.7,
          gradientToColors: ['var(--color-base-100)'],
          opacityTo: 0.3,
          stops: [0, 90, 100]
        }
      },
      xaxis: {
        type: 'category',
        tickPlacement: 'on',
        categories: [
          '1 March 2024',
          '1 April 2024',
          '1 May 2024',
          '1 June 2024',
          '1 July 2024',
          '1 August 2024',
          '1 September 2024',
          '1 October 2024',
          '1 November 2024',
          '1 December 2024',
          '1 January 2025',
          '1 February 2025'
        ],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        crosshairs: {
          stroke: {
            dashArray: 0
          },
          dropShadow: {
            show: false
          }
        },
        tooltip: {
          enabled: false
        },
        labels: {
          style: {
            colors: 'var(--color-base-content)',
            fontSize: '12px',
            fontWeight: 400
          },
          formatter: title => {
            let t = title

            if (t) {
              const newT = t.split(' ')
              t = `${newT[0]} ${newT[1].slice(0, 3)}`
            }

            return t
          }
        }
      },
      yaxis: {
        labels: {
          align: 'left',
          minWidth: 0,
          maxWidth: 140,
          style: {
            colors: 'var(--color-base-content)',
            fontSize: '12px',
            fontWeight: 400
          },
          formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
        }
      },
      tooltip: {
        x: {
          format: 'MMMM yyyy'
        },
        y: {
          formatter: value => `$${value >= 1000 ? `${value / 1000}k` : value}`
        },
        custom: function (props) {
          const { categories } = props.ctx.opts.xaxis
          const { dataPointIndex } = props
          const title = categories[dataPointIndex].split(' ')
          const newTitle = `${title[0]} ${title[1]}`

          return buildTooltip(props, {
            title: newTitle,
            mode,
            hasTextLabel: true,
            wrapperExtClasses: 'min-w-28',
            labelDivider: ':',
            labelExtClasses: 'ms-2'
          })
        }
      },
      responsive: [
        {
          breakpoint: 568,
          options: {
            chart: {
              height: 300
            },
            labels: {
              style: {
                fontSize: '10px',
                colors: 'var(--color-base-content)'
              },
              offsetX: -2,
              formatter: title => title.slice(0, 3)
            },
            yaxis: {
              labels: {
                align: 'left',
                minWidth: 0,
                maxWidth: 140,
                style: {
                  colors: 'var(--color-base-content)',
                  fontSize: '10px'
                },
                formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
              }
            }
          }
        }
      ]
    }))
   })()
})
</script>

{{< /code >}}

<!-- Multiple area charts (comparison tooltip) -->

{{< headname level="3" >}} Multiple area charts (comparison tooltip){{< /headname >}}

The following example demonstrates the usage of a multiple area charts with comparison tooltip.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-multiple-area-charts-compare"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-multiple-area-charts-compare', mode => ({
        chart: {
          height: 400,
          type: 'area',
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: '2024',
            data: [5000, 15000, 8000, 60000, 75000, 85000, 93000, 102000, 87000, 95000, 120000, 130000]
          },
          {
            name: '2023',
            data: [20000, 45000, 70000, 30000, 90000, 40000, 95000, 75000, 105000, 50000, 35000, 65000]
          }
        ],
        legend: {
          show: true,
          position: 'top',
          horizontalAlign: 'right',
          labels: {
            useSeriesColors: true
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight',
          width: 2
        },
        grid: {
          strokeDashArray: 2,
          borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)'
        },
        colors: ['var(--color-info)', 'var(--color-warning)'],

        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.7,
            gradientToColors: ['var(--color-base-100)'],
            opacityTo: 0.3,
            stops: [0, 90, 100]
          }
        },
        xaxis: {
          type: 'category',
          tickPlacement: 'on',
          categories: [
            '1 January',
            '1 February',
            '1 March',
            '1 April',
            '1 May',
            '1 June',
            '1 July',
            '1 August',
            '1 September',
            '1 October',
            '1 November',
            '1 December'
          ],
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          tooltip: {
            enabled: false
          },
          labels: {
            style: {
              fontSize: '12px',
              colors: 'var(--color-base-content)',
              fontWeight: 400
            },
            formatter: title => {
              let t = title

              if (t) {
                const newT = t.split(' ')
                t = `${newT[1].slice(0, 3)}`
              }

              return t
            }
          }
        },
        yaxis: {
          labels: {
            align: 'left',
            minWidth: 0,
            maxWidth: 140,
            style: {
              fontSize: '12px',
              colors: 'var(--color-base-content)',
              fontWeight: 400
            },
            formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
          }
        },
        tooltip: {
          x: {
            format: 'MMMM yyyy'
          },
          y: {
            formatter: value => `$${value >= 1000 ? `${value / 1000}k` : value}`
          },
          custom: function (props) {
            return buildTooltipCompareTwo(props, {
              title: 'Revenue',
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-48',
              markerExtClasses: ''
            })
          }
        },
        responsive: [
          {
            breakpoint: 568,
            options: {
              chart: {
                height: 300
              },
              labels: {
                style: {
                  fontSize: '10px',
                  colors: 'var(--color-base-content)'
                },
                offsetX: -2,
                formatter: title => title.slice(0, 3)
              },
              yaxis: {
                labels: {
                  align: 'left',
                  minWidth: 0,
                  maxWidth: 140,
                  style: {
                    fontSize: '10px',
                    colors: 'var(--color-base-content)'
                  },
                  formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
                }
              }
            }
          }
        ]
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Multiple area charts (comparison alternative) -->

{{< headname level="3" >}} Multiple area charts (comparison alternative) {{< /headname >}}

The following example demonstrates the usage of a multiple area charts with alternative comparison tooltip.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-multiple-area-charts-compare-alt" class="w-full"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-multiple-area-charts-compare-alt', mode => ({
        chart: {
          height: 400,
          type: 'area',
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: '2024',
            data: [5000, 15000, 8000, 60000, 75000, 85000, 93000, 102000, 87000, 95000, 120000, 130000]
          },
          {
            name: '2023',
            data: [20000, 45000, 70000, 30000, 90000, 40000, 95000, 75000, 105000, 50000, 35000, 65000]
          }
        ],
        legend: {
          show: true,
          position: 'top',
          horizontalAlign: 'right',
          labels: {
            useSeriesColors: true
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth',
          width: 2
        },
        grid: {
          strokeDashArray: 2,
          borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)'
        },
        colors: ['var(--color-info)', 'var(--color-accent)'],
        fill: {
          gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.7,
            gradientToColors: ['var(--color-base-100)'],
            opacityTo: 0.3,
            stops: [0, 90, 100]
          }
        },
        xaxis: {
          type: 'category',
          tickPlacement: 'on',
          categories: [
            '1 January',
            '1 February',
            '1 March',
            '1 April',
            '1 May',
            '1 June',
            '1 July',
            '1 August',
            '1 September',
            '1 October',
            '1 November',
            '1 December'
          ],
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          crosshairs: {
            stroke: {
              dashArray: 0
            },
            dropShadow: {
              show: false
            }
          },
          tooltip: {
            enabled: false
          },
          labels: {
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: title => {
              let t = title

              if (t) {
                const newT = t.split(' ')
                t = `${newT[1].slice(0, 3)}`
              }

              return t
            }
          }
        },
        yaxis: {
          labels: {
            align: 'left',
            minWidth: 0,
            maxWidth: 140,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
          }
        },
        tooltip: {
          x: {
            format: 'MMMM yyyy'
          },
          y: {
            formatter: value => `$${value >= 1000 ? `${value / 1000}k` : value}`
          },
          custom: function (props) {
            return buildTooltipCompareTwoAlt(props, {
              title: 'Revenue',
              mode,
              valuePrefix: '$',
              hasTextLabel: true,
              wrapperExtClasses: '',
              markerExtClasses: ''
            })
          }
        },
        responsive: [
          {
            breakpoint: 568,
            options: {
              chart: {
                height: 300
              },
              labels: {
                style: {
                  fontSize: '10px',
                  colors: 'var(--color-base-content)'
                },
                offsetX: -2,
                formatter: title => title.slice(0, 3)
              },
              yaxis: {
                labels: {
                  align: 'left',
                  minWidth: 0,
                  maxWidth: 140,
                  style: {
                    fontSize: '10px',
                    colors: 'var(--color-base-content)'
                  },
                  formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
                }
              }
            }
          }
        ]
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Curved area charts -->

{{< headname level="3" >}} Curved area charts {{< /headname >}}

The following example demonstrates the usage of a curved area charts.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-curved-area-charts" class="w-full"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-curved-area-charts', mode => ({
        chart: {
          height: 400,
          type: 'area',
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: 'Revenue',
            data: [18000, 32000, 50000, 45000, 60000, 85000, 78000, 92000, 86000, 89000, 95000, 102000]
          },
          {
            name: 'Expenses',
            data: [10000, 20000, 30000, 38000, 42000, 55000, 49000, 70000, 66000, 72000, 75000, 78000]
          }
        ],
        legend: {
          show: true,
          position: 'top',
          horizontalAlign: 'right',
          labels: {
            useSeriesColors: true
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth',
          width: 2
        },
        grid: {
          strokeDashArray: 2,
          borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)'
        },
        colors: ['var(--color-warning)', 'var(--color-accent)'],
        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.7,
            gradientToColors: ['var(--color-base-100)'],
            opacityTo: 0.3,
            stops: [0, 90, 100]
          }
        },
        xaxis: {
          type: 'category',
          tickPlacement: 'on',
          categories: [
            '1 March 2024',
            '1 April 2024',
            '1 May 2024',
            '1 June 2024',
            '1 July 2024',
            '1 August 2024',
            '1 September 2024',
            '1 October 2024',
            '1 November 2024',
            '1 December 2024',
            '1 January 2025',
            '1 February 2025'
          ],
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          tooltip: {
            enabled: false
          },
          labels: {
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: title => {
              let t = title

              if (t) {
                const newT = t.split(' ')
                t = `${newT[0]} ${newT[1].slice(0, 3)}`
              }

              return t
            }
          }
        },
        yaxis: {
          labels: {
            align: 'left',
            minWidth: 0,
            maxWidth: 140,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
          }
        },
        tooltip: {
          x: {
            format: 'MMMM yyyy'
          },
          y: {
            formatter: value => `$${value >= 1000 ? `${value / 1000}k` : value}`
          },
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex].split(' ')
            const newTitle = `${title[0]} ${title[1]}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-28',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        },
        responsive: [
          {
            breakpoint: 568,
            options: {
              chart: {
                height: 300
              },
              labels: {
                style: {
                  fontSize: '10px',
                  colors: 'var(--color-base-content)'
                },
                offsetX: -2,
                formatter: title => title.slice(0, 3)
              },
              yaxis: {
                labels: {
                  align: 'left',
                  minWidth: 0,
                  maxWidth: 140,
                  style: {
                    fontSize: '10px',
                    colors: 'var(--color-base-content)'
                  },
                  formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
                }
              }
            }
          }
        ]
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Column chart -->

{{< headname level="3" >}} Column chart {{< /headname >}}

The following example demonstrates the usage of a Column chart.

{{< code hasRTL="false" addClass="!block" jsCode="true" >}}

<div id="apex-column-bar-chart" class="w-full"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-column-bar-chart', mode => ({
        chart: {
          type: 'bar',
          height: 400,
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: 'Investment',
            data: [25000, 39000, 65000, 45000, 79000, 80000, 69000, 63000, 60000, 66000, 90000, 78000]
          }
        ],
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '30px'
          }
        },
        legend: {
          show: false
        },
        dataLabels: {
          enabled: false
        },
        colors: ['var(--color-primary)', 'var(--color-base-100)'],
        xaxis: {
          categories: [
            'Cook',
            'Erin',
            'Jack',
            'Will',
            'Gayle',
            'Megan',
            'John',
            'Luke',
            'Ellis',
            'Mason',
            'Elvis',
            'Liam'
          ],
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          labels: {
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            }
          }
        },
        yaxis: {
          labels: {
            align: 'left',
            minWidth: 0,
            maxWidth: 140,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
          }
        },
        states: {
          hover: {
            filter: {
              type: 'darken',
              value: 0.9
            }
          }
        },
        tooltip: {
          y: {
            formatter: value => `$${value >= 1000 ? `${value / 1000}k` : value}`
          },
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex]
            const newTitle = `${title}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-28',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        },
        responsive: [
          {
            breakpoint: 568,
            options: {
              chart: {
                height: 300
              },
              plotOptions: {
                bar: {
                  columnWidth: '10px'
                }
              },
              stroke: {
                width: 8
              },
              labels: {
                style: {
                  fontSize: '10px',
                  colors: 'var(--color-base-content)'
                },
                formatter: title => title.slice(0, 3)
              },
              yaxis: {
                labels: {
                  align: 'left',
                  minWidth: 0,
                  maxWidth: 140,
                  style: {
                    fontSize: '10px',
                    colors: 'var(--color-base-content)'
                  },
                  formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
                }
              }
            }
          }
        ]
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Multiple column charts -->

{{< headname level="3" >}} Multiple column charts {{< /headname >}}

The following example demonstrates the usage of a multiple column charts.

{{< code hasRTL="false" addClass="!block" jsCode="true" >}}

<div id="apex-multiple-column-charts" class="w-full"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-multiple-column-charts', mode => ({
        chart: {
          type: 'bar',
          height: 400,
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: 'Investment',
            data: [25000, 47000, 59000, 67000, 66000, 66000, 78000, 43000, 40000, 56000, 54000, 78000]
          },
          {
            name: 'Revenue',
            data: [34000, 56000, 85000, 90000, 70000, 80000, 100000, 40000, 50000, 44000, 47000, 96000]
          }
        ],
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '12px',
            borderRadius: 0
          }
        },
        legend: {
          show: true,
          position: 'top',
          horizontalAlign: 'right',
          labels: {
            useSeriesColors: true
          },
          markers: {
            shape: 'circle'
          }
        },
        dataLabels: {
          enabled: false
        },
        colors: ['var(--color-primary)', 'var(--color-success)'],
        xaxis: {
          categories: [
            'Cook',
            'Erin',
            'Jack',
            'Will',
            'Gayle',
            'Megan',
            'John',
            'Luke',
            'Ellis',
            'Mason',
            'Elvis',
            'Liam'
          ],
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          crosshairs: {
            show: false
          },
          labels: {
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            }
          }
        },
        yaxis: {
          labels: {
            align: 'left',
            minWidth: 0,
            maxWidth: 140,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
          }
        },
        states: {
          hover: {
            filter: {
              type: 'darken',
              value: 0.9
            }
          }
        },
        tooltip: {
          y: {
            formatter: value => `$${value >= 1000 ? `${value / 1000}k` : value}`
          },
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex]
            const newTitle = `${title}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-28',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        },
        responsive: [
          {
            breakpoint: 568,
            options: {
              chart: {
                height: 300
              },
              plotOptions: {
                bar: {
                  columnWidth: '4px'
                }
              },
              labels: {
                style: {
                  fontSize: '10px',
                  colors: 'var(--color-base-content)'
                },
                offsetX: -2,
                formatter: title => title.slice(0, 3)
              },
              yaxis: {
                labels: {
                  align: 'left',
                  minWidth: 0,
                  maxWidth: 140,
                  style: {
                    fontSize: '10px',
                    colors: 'var(--color-base-content)'
                  },
                  formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
                }
              }
            }
          }
        ]
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Single line chart -->

{{< headname level="3" >}} Single line chart {{< /headname >}}

The following example demonstrates the usage of a single line chart.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-single-line-chart" class="w-full"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-single-line-chart', mode => ({
        chart: {
          height: 300,
          type: 'line',
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: 'Views',
            data: [0, 5000, 15000, 25000, 40000, 30000, 20000, 15000, 25000, 40000, 30000, 20000]
          }
        ],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight',
          width: [4, 4, 4]
        },
        title: {
          show: false
        },
        legend: {
          show: false
        },
        grid: {
          strokeDashArray: 0,
          borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)',
          padding: {
            top: -20,
            right: 0
          }
        },
        colors: ['var(--color-primary)'],
        xaxis: {
          type: 'category',
          categories: [
            '1 January 2024',
            '1 February 2024',
            '1 March 2024',
            '1 April 2024',
            '1 May 2024',
            '1 June 2024',
            '1 July 2024',
            '1 August 2024',
            '1 September 2024',
            '1 October 2024',
            '1 November 2024',
            '1 December 2024'
          ],
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          tooltip: {
            enabled: false
          },
          labels: {
            offsetY: 5,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: title => {
              let t = title

              if (t) {
                const newT = t.split(' ')
                t = `${newT[0]} ${newT[1].slice(0, 3)}`
              }

              return t
            }
          }
        },
        yaxis: {
          min: 0,
          max: 40000,
          tickAmount: 4,
          labels: {
            align: 'left',
            minWidth: 0,
            maxWidth: 140,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
          }
        },
        tooltip: {
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex].split(' ')
            const newTitle = `${title[0]} ${title[1]}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-28',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        }
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Multiple line charts -->

{{< headname level="3" >}} Multiple line charts {{< /headname >}}

The following example demonstrates the usage of a multiple line charts.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-multiple-line-charts" class="w-full"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-multiple-line-charts', mode => ({
        chart: {
          height: 350,
          type: 'line',
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: 'Eric',
            data: [0, 17000, 35000, 23000, 40000]
          },
          {
            name: 'John',
            data: [0, 15000, 19000, 32500, 27000]
          },
          {
            name: 'Gwen',
            data: [0, 12000, 16000, 20000, 30000]
          }
        ],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight',
          width: [4, 4, 4]
        },
        title: {
          show: false
        },
        legend: {
          show: true,
          position: 'top',
          horizontalAlign: 'right',
          labels: {
            useSeriesColors: true
          }
        },
        grid: {
          strokeDashArray: 0,
          borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)',
          padding: {
            top: 0,
            right: 0,
            bottom: 10
          }
        },
        colors: ['var(--color-primary)', 'var(--color-success)', 'var(--color-error)'],
        xaxis: {
          type: 'category',
          categories: ['1 January 2024', '1 February 2023', '1 March 2023', '1 April 2023', '1 May 2023'],
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          tooltip: {
            enabled: false
          },
          labels: {
            offsetY: 5,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: title => {
              let t = title

              if (t) {
                const newT = t.split(' ')
                t = `${newT[0]} ${newT[1].slice(0, 3)}`
              }

              return t
            }
          }
        },
        yaxis: {
          min: 0,
          max: 40000,
          tickAmount: 4,
          labels: {
            align: 'left',
            minWidth: 0,
            maxWidth: 140,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
          }
        },
        tooltip: {
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex].split(' ')
            const newTitle = `${title[0]} ${title[1]}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-36',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        }
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Curved line charts -->

{{< headname level="3" >}} Curved line charts {{< /headname >}}

The following example demonstrates the usage of a Curved line charts.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-curved-line-charts" class="w-full"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-curved-line-charts', mode => ({
        chart: {
          height: 300,
          type: 'line',
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: 'Eric',
            data: [0, 17000, 35000, 23000, 40000]
          },
          {
            name: 'John',
            data: [0, 15000, 19000, 32500, 27000]
          },
          {
            name: 'Gwen',
            data: [0, 12000, 16000, 20000, 30000]
          }
        ],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth',
          width: [4, 4, 4]
        },
        title: {
          show: false
        },
        legend: {
          show: true,
          position: 'top',
          horizontalAlign: 'right',
          labels: {
            useSeriesColors: true
          }
        },
        grid: {
          strokeDashArray: 0,
          borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)',
          padding: {
            top: 0,
            right: 0,
            bottom: 10
          }
        },
        colors: ['var(--color-primary)', 'var(--color-success)', 'var(--color-error)'],
        xaxis: {
          type: 'category',
          categories: ['1 January 2024', '1 February 2023', '1 March 2023', '1 April 2023', '1 May 2023'],
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          tooltip: {
            enabled: false
          },
          labels: {
            offsetY: 5,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: title => {
              let t = title

              if (t) {
                const newT = t.split(' ')
                t = `${newT[0]} ${newT[1].slice(0, 3)}`
              }
              return t
            }
          }
        },
        yaxis: {
          min: 0,
          max: 40000,
          tickAmount: 4,
          labels: {
            align: 'left',
            minWidth: 0,
            maxWidth: 140,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
          }
        },
        tooltip: {
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex].split(' ')
            const newTitle = `${title[0]} ${title[1]}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-36',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        }
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Candle Stick Chart -->

{{< headname level="3" badge-text="new" >}} Candle Stick Chart {{< /headname >}}

The following example demonstrates the usage of a Candle Stick chart.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="candleStickChart"></div>

<!-- Js -->
<script>
window.addEventListener('load', () => {
  ;(function () {
    buildChart('#candleStickChart', mode => ({
      chart: {
        height: 410,
        type: 'candlestick',
        parentHeightOffset: 0,
        toolbar: {
          show: false
        }
      },
      series: [
        {
          data: [
            {
              x: new Date(1538778600000),
              y: [150, 170, 50, 100]
            },
            {
              x: new Date(1538780400000),
              y: [200, 400, 170, 330]
            },
            {
              x: new Date(1538782200000),
              y: [330, 340, 250, 280]
            },
            {
              x: new Date(1538784000000),
              y: [300, 330, 200, 320]
            },
            {
              x: new Date(1538785800000),
              y: [320, 450, 280, 350]
            },
            {
              x: new Date(1538787600000),
              y: [300, 350, 80, 250]
            },
            {
              x: new Date(1538789400000),
              y: [200, 330, 170, 300]
            },
            {
              x: new Date(1538791200000),
              y: [200, 220, 70, 130]
            },
            {
              x: new Date(1538793000000),
              y: [220, 270, 180, 250]
            },
            {
              x: new Date(1538794800000),
              y: [200, 250, 80, 100]
            },
            {
              x: new Date(1538796600000),
              y: [150, 170, 50, 120]
            },
            {
              x: new Date(1538798400000),
              y: [110, 450, 10, 420]
            },
            {
              x: new Date(1538800200000),
              y: [400, 480, 300, 320]
            },
            {
              x: new Date(1538802000000),
              y: [380, 480, 350, 450]
            }
          ]
        }
      ],
      xaxis: {
        type: 'datetime',
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        labels: {
          style: {
            colors: 'var(--color-base-content)',
            fontSize: '13px'
          }
        }
      },
      yaxis: {
        tickAmount: 5,
        tooltip: {
          enabled: true
        },
        labels: {
          style: {
            colors: 'var(--color-base-content)',
            fontSize: '13px'
          }
        }
      },
      grid: {
        borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)',
        xaxis: {
          lines: {
            show: true
          }
        },
        padding: {
          top: -20
        }
      },
      plotOptions: {
        candlestick: {
          colors: {
            upward: 'var(--color-success)',
            downward: 'var(--color-error)'
          }
        },
        bar: {
          columnWidth: '40%'
        }
      }
    }))
  })()
})
</script>

{{< /code >}}

<!-- Horizontal bar chart -->

{{< headname level="3" >}} Horizontal bar chart {{< /headname >}}

The following example demonstrates the usage of a Horizontal bar chart.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-horizontal-bar-chart" class="w-full"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-horizontal-bar-chart', mode => ({
        chart: {
          type: 'bar',
          height: 400,
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          {
            name: 'Transactions 2023',
            data: [21000, 42000, 55000, 67000, 66000, 61000, 48000, 33000, 40000, 56000, 84000, 28000]
          },
          {
            name: 'Transactions 2024',
            data: [25000, 39000, 50000, 70000, 69000, 62000, 49000, 35000, 43000, 57000, 86000, 30000]
          }
        ],
        plotOptions: {
          bar: {
            horizontal: true,
            columnWidth: '16px',
            borderRadius: 4,
            borderRadiusApplication: 'end'
          }
        },
        legend: {
          show: true,
          position: 'top',
          markers: {
            shape: 'circle'
          },
          labels: {
            colors: 'var(--color-base-content)',
            useSeriesColors: false
          }
        },
        dataLabels: {
          enabled: false
        },
        colors: ['var(--color-accent)', 'var(--color-warning)'],
        xaxis: {
          categories: [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
          ],
          crosshairs: {
            show: false
          },
          labels: {
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            offsetX: -2,
            formatter: value => (value >= 1000 ? `${value / 1000}k` : value)
          }
        },
        yaxis: {
          crosshairs: {
            show: false
          },
          labels: {
            align: 'left',
            minWidth: 0,
            maxWidth: 140,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px',
              fontWeight: 400
            },
            offsetX: -10,
            formatter: title => (typeof title === 'string' ? title.slice(0, 3) : title)
          }
        },
        states: {
          hover: {
            filter: {
              type: 'darken',
              value: 0.9
            }
          }
        },
        tooltip: {
          y: {
            formatter: value => `$${value >= 1000 ? `${value / 1000}k` : value}`
          },
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex]
            const newTitle = `${title}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-28',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        }
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Doughnut chart -->

{{< headname level="3" >}} Doughnut chart {{< /headname >}}

The following example demonstrates the usage of a doughnut chart.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-doughnut-chart"></div>

<!-- Js -->
<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-doughnut-chart', mode => ({
        chart: {
          height: 300,
          type: 'donut'
        },
        plotOptions: {
          pie: {
            donut: {
              size: '70%',
              labels: {
                show: true,
                name: {
                  fontSize: '2rem'
                },
                value: {
                  fontSize: '1.5rem',
                  color: 'var(--color-base-content)',
                  formatter: function (val) {
                    return parseInt(val, 10) + '%'
                  }
                },
                total: {
                  show: true,
                  fontSize: '1rem',
                  label: 'Operational',
                  color: 'var(--color-primary)',
                  formatter: function (w) {
                    return '42%'
                  }
                }
              }
            }
          }
        },
        series: [42, 7, 25, 25],
        labels: ['Operational', 'Networking', 'Hiring', 'R&D'],
        legend: {
          show: true,
          position: 'bottom',
          markers: { offsetX: -3 },
          labels: {
            useSeriesColors: true
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          show: false,
          curve: 'straight'
        },
        colors: ['var(--color-primary)', 'var(--color-success)', 'var(--color-error)', 'var(--color-warning)'],
        states: {
          hover: {
            filter: {
              type: 'none'
            }
          }
        },
        tooltip: {
          enabled: true
        }
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Bubble chart -->

{{< headname level="3" >}} Bubble chart {{< /headname >}}

The following example demonstrates the usage of a bubble chart.

{{< code hasRTL="false" addClass="flex-col h-[420px]" jsCode="true" >}}

<div id="apex-bubble-chart"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
       buildChart('#apex-bubble-chart', mode => ({
        chart: {
          height: '100%',
          type: 'bubble',
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        series: [
          { name: 'Focus', data: [[5, 6, 70]] },
          { name: 'Accuracy', data: [[6, 3, 40]] },
          { name: 'Efficiency', data: [[7, 10, 80]] }
        ],
        dataLabels: {
          style: {
            fontSize: '12px',
            fontWeight: '400',
            colors: ['var(--color-primary-content)', 'var(--color-success-content)', 'var(--color-error-content)']
          },
          formatter: value => (value ? `${value}%` : '')
        },
        fill: {
          opacity: 1
        },
        colors: ['var(--color-primary)', 'var(--color-success)', 'var(--color-error)'],
        legend: {
          show: true,
          position: 'bottom',
          markers: { offsetX: -3, offsetY: -1 },
          labels: {
            useSeriesColors: true
          }
        },
        plotOptions: {
          bubble: {
            zScaling: false,
            minBubbleRadius: 40
          }
        },
        grid: {
          show: false
        },
        xaxis: {
          min: 0,
          max: 15,
          labels: {
            show: false
          },
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          }
        },
        yaxis: {
          min: 0,
          max: 15,
          labels: {
            show: false
          }
        },
        tooltip: {
          enabled: false
        },
        states: {
          hover: {
            filter: {
              type: 'none'
            }
          }
        },
        responsive: [
          {
            breakpoint: 565,
            options: {
              height: '80%'
            }
          }
        ]
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Pie chart -->

{{< headname level="3" >}} Pie chart {{< /headname >}}

The following example demonstrates the usage of a pie chart.

{{< code hasRTL="false" addClass="flex-col h-96" jsCode="true" >}}

<div id="apex-pie-chart"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-pie-chart', mode => ({
        chart: {
          height: '100%',
          type: 'pie',
          zoom: {
            enabled: false
          }
        },
        series: [40, 20, 10, 10, 8, 6, 6],
        labels: ['Rent', 'Food', 'Utilities', 'Transport', 'Health', 'Education', 'Miscellaneous'],
        title: {
          show: false
        },
        colors: [
          'var(--color-primary)',
          'var(--color-neutral)',
          'var(--color-accent)',
          'var(--color-info)',
          'var(--color-warning)',
          'var(--color-success)',
          'var(--color-error)'
        ],
        dataLabels: {
          style: {
            fontSize: '12px',
            fontWeight: '500',
            colors: [
              'var(--color-primary-content)',
              'var(--color-neutral-content)',
              'var(--color-accent-content)',
              'var(--color-info-content)',
              'var(--color-warning-content)',
              'var(--color-success-content)',
              'var(--color-error-content)'
            ]
          },
          dropShadow: {
            enabled: false
          },
          formatter: value => `${value.toFixed(1)} %`
        },
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -15
            }
          }
        },
        legend: {
          show: true,
          position: 'bottom',
          markers: { offsetX: -2 },
          labels: {
            useSeriesColors: true
          }
        },
        stroke: {
          show: false
        },
        tooltip: {
          enabled: false
        },
        states: {
          hover: {
            filter: {
              type: 'none'
            }
          }
        }
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Radial bar chart -->

{{< headname level="3" >}} Radial bar chart {{< /headname >}}

The following example demonstrates the usage of a radial bar chart.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-radial-bar-chart"></div>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-radial-bar-chart', mode => ({
        chart: {
          height: 380,
          type: 'radialBar'
        },
        colors: ['var(--color-error)', 'var(--color-accent)', 'var(--color-warning)'],
        plotOptions: {
          radialBar: {
            size: 185,
            hollow: {
              size: '40%'
            },
            track: {
              margin: 10,
              background: 'var(--color-base-200)'
            },
            dataLabels: {
              name: {
                fontSize: '1.5rem'
              },
              value: {
                fontSize: '1rem',
                color: 'var(--color-base-content)'
              },
              total: {
                show: true,
                fontWeight: 400,
                color: 'var(--color-base-content)',
                fontSize: '1.3rem',
                label: 'Total',
                formatter: function (w) {
                  return '69%'
                }
              }
            }
          }
        },
        grid: {
          borderColor: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)',
          padding: {
            top: 0,
            bottom: 0
          }
        },
        legend: {
          show: true,
          position: 'bottom',
          labels: {
            useSeriesColors: true
          }
        },
        stroke: {
          lineCap: 'round'
        },
        series: [80, 50, 35],
        labels: ['Comments', 'Replies', 'Shares']
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Radar chart -->

{{< headname level="3" >}} Radar chart {{< /headname >}}

The following example demonstrates the usage of a radar chart.

{{< code hasRTL="false" addClass="flex-col" jsCode="true" >}}

<div id="apex-radar-chart"></div>

<!-- Js -->
<script>
  window.addEventListener("load", () => {
    ;(function () {
      buildChart('#apex-radar-chart', mode => ({
        chart: {
          height: 350,
          width: '100%',
          type: 'radar',
          toolbar: {
            show: false
          },
          dropShadow: {
            enabled: false,
            blur: 8,
            left: 1,
            top: 1,
            opacity: 0.2
          }
        },
        legend: {
          show: true,
          position: 'bottom',
          labels: {
            useSeriesColors: true
          }
        },
        plotOptions: {
          radar: {
            polygons: {
              strokeColors: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)',
              connectorColors: 'color-mix(in oklab, var(--color-base-content) 40%, transparent)'
            }
          }
        },
        yaxis: {
          show: false
        },
        series: [
          {
            name: 'iPhone 15 Pro Max',
            data: [41, 64, 81, 60, 42, 42, 33, 23]
          },
          {
            name: 'Samsung s24 Ultra',
            data: [65, 46, 42, 25, 58, 63, 76, 43]
          }
        ],
        colors: [
          'color-mix(in oklab, var(--color-primary) 70%, transparent)',
          'color-mix(in oklab, var(--color-warning) 90%, transparent)'
        ],
        xaxis: {
          categories: ['Battery', 'Brand', 'Camera', 'Memory', 'Storage', 'Display', 'OS', 'Price'],
          labels: {
            show: true,
            style: {
              colors: 'var(--color-base-content)',
              fontSize: '12px'
            }
          }
        },
        stroke: {
          show: false,
          width: 0
        },
        markers: {
          size: 0
        },
        grid: {
          show: false,
          padding: {
            top: -20,
            bottom: -20
          }
        }
      }))
    })()
  })
</script>

{{< /code >}}

<!-- Small sized sparklines -->

{{< headname level="3" >}} Small sized sparklines {{< /headname >}}

The following example demonstrates the usage of a small sized sparkline charts.

{{< code hasRTL="false" addClass="flex-col" >}}

<ul class="border-base-content/25 divide-base-content/25 w-full divide-y rounded-md border *:p-3">
  <li class="bg-base-200/40 text-base-content grid-cols-2 grid items-center gap-x-2">
    <span>Chart types</span>
    <span>Description</span>
  </li>
  <li class="grid-cols-2 grid items-center gap-x-2">
    <div id="apex-sparklines-area-chart"></div>
    <span>Inline area chart.</span>
  </li>
  <li class="grid-cols-2 grid items-center gap-x-2">
    <div id="apex-sparklines-bar-chart"></div>
    <span>Inline bar chart.</span>
  </li>
  <li class="grid-cols-2 grid items-center gap-x-2">
    <div id="apex-sparklines-pie-chart"></div>
    <span>Inline pie chart.</span>
  </li>
  <li class="grid-cols-2 grid items-center gap-x-2">
    <div id="apex-sparklines-line-chart"></div>
    <span>Inline line chart.</span>
  </li>
  <li class="grid-cols-2 grid items-center gap-x-2">
    <div id="apex-sparklines-candles-chart"></div>
    <span>Inline candles chart.</span>
  </li>
</ul>

<!-- Js -->

<script>
  window.addEventListener("load", () => {
    ;(function () {
      // Sparklines charts (Start)
      // Sparklines area chart (Start)
      buildChart('#apex-sparklines-area-chart', mode => ({
        series: [
          {
            name: 'Sales',
            data: [20, 30, 34, 42, 45, 35, 39, 37, 50, 37, 45, 30]
          }
        ],
        chart: {
          width: 100,
          height: 30,
          type: 'area',
          sparkline: {
            enabled: true
          }
        },
        stroke: {
          curve: 'smooth',
          width: 0
        },
        fill: {
          type: 'solid'
        },
        colors: ['var(--color-primary)'],
        xaxis: {
          type: 'category',
          categories: [
            '1 March 2024',
            '2 March 2024',
            '3 March 2024',
            '4 March 2024',
            '5 March 2024',
            '6 March 2024',
            '7 March 2024',
            '8 March 2024',
            '9 March 2024',
            '10 March 2024',
            '11 March 2024',
            '12 March 2024'
          ],
          crosshairs: {
            show: false
          }
        },
        markers: {
          hover: {
            size: 0
          }
        },
        tooltip: {
          marker: {
            show: false
          },
          fixed: {
            enabled: true,
            position: 'bottomLeft',
            offsetX: 10,
            offsetY: -15
          },
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex].split(' ')
            const newTitle = `${title[0]} ${title[1]}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-28',
              titleExtClasses: 'text-left',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        }
      }))
      // Sparklines area chart (End)

      // Sparklines bar chart (Start)
      buildChart('#apex-sparklines-bar-chart', mode => ({
        series: [
          {
            name: 'Sales',
            data: [11, 23, 29, 40, 47, 15, 10, -35, -45, -30, 40, 20]
          }
        ],
        chart: {
          width: 100,
          height: 50,
          type: 'bar',
          sparkline: {
            enabled: true
          }
        },
        plotOptions: {
          bar: {
            colors: {
              ranges: [
                {
                  from: -45,
                  to: 0,
                  color: 'var(--color-error)'
                }
              ]
            }
          }
        },
        colors: ['var(--color-primary)'],
        xaxis: {
          type: 'category',
          categories: [
            '1 March 2024',
            '2 March 2024',
            '3 March 2024',
            '4 March 2024',
            '5 March 2024',
            '6 March 2024',
            '7 March 2024',
            '8 March 2024',
            '9 March 2024',
            '10 March 2024',
            '11 March 2024',
            '12 March 2024'
          ],
          crosshairs: {
            show: false
          }
        },
        tooltip: {
          marker: {
            show: false
          },
          fixed: {
            enabled: true,
            position: 'bottomLeft',
            offsetX: 10,
            offsetY: -15
          },
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex].split(' ')
            const newTitle = `${title[0]} ${title[1]}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-28',
              titleExtClasses: 'text-left',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        }
      }))
      // Sparklines bar chart (End)

      // Sparklines pie chart (Start)
      buildChart('#apex-sparklines-pie-chart', mode => ({
        chart: {
          width: 50,
          height: 50,
          type: 'pie',
          sparkline: {
            enabled: true
          }
        },
        series: [60, 18, 12, 10],
        labels: ['TailwindCSS', 'JS', 'TS', 'React'],
        plotOptions: {
          pie: {
            expandOnClick: false
          }
        },
        colors: ['var(--color-primary)', 'var(--color-warning)', 'var(--color-accent)', 'var(--color-info)'],
        stroke: {
          width: 0
        },
        tooltip: {
          enabled: false
        },
        states: {
          hover: {
            filter: {
              type: 'none'
            }
          }
        }
      }))
      // Sparklines pie chart (End)

      // Sparklines line chart (Start)
      buildChart('#apex-sparklines-line-chart', mode => ({
        series: [
          {
            name: 'Sales',
            data: [20, 30, 34, 42, 45, 35, 39, 37, 50, 37, 45, 30]
          }
        ],
        chart: {
          width: 100,
          height: 30,
          type: 'line',
          sparkline: {
            enabled: true
          }
        },
        stroke: {
          curve: 'smooth',
          width: 2
        },
        colors: ['var(--color-primary)'],
        xaxis: {
          type: 'category',
          categories: [
            '1 March 2024',
            '2 March 2024',
            '3 March 2024',
            '4 March 2024',
            '5 March 2024',
            '6 March 2024',
            '7 March 2024',
            '8 March 2024',
            '9 March 2024',
            '10 March 2024',
            '11 March 2024',
            '12 March 2024'
          ],
          crosshairs: {
            show: false
          }
        },
        markers: {
          hover: {
            size: 0
          }
        },
        tooltip: {
          marker: {
            show: false
          },
          fixed: {
            enabled: true,
            position: 'bottomLeft',
            offsetX: 10,
            offsetY: -15
          },
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex].split(' ')
            const newTitle = `${title[0]} ${title[1]}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-28',
              titleExtClasses: 'text-left',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        }
      }))
      // Sparklines line chart (End)

      // Sparklines candlestick chart (Start)
      buildChart('#apex-sparklines-candles-chart', mode => ({
        series: [
          {
            name: 'Shares',
            data: [
              {
                x: '1 March 2024',
                y: [6500.9, 6501.12, 6480, 6490.25]
              },
              {
                x: '2 March 2024',
                y: [6491.35, 6510, 6490, 6505.5]
              },
              {
                x: '3 March 2024',
                y: [6505.89, 6509.99, 6495, 6498.67]
              },
              {
                x: '4 March 2024',
                y: [6498.67, 6502.78, 6480.34, 6490]
              },
              {
                x: '5 March 2024',
                y: [6490.25, 6493.9, 6481.25, 6491.12]
              },
              {
                x: '6 March 2024',
                y: [6491.25, 6492.75, 6480.12, 6490.01]
              },
              {
                x: '7 March 2024',
                y: [6490.01, 6503.12, 6485.89, 6502.67]
              },
              {
                x: '8 March 2024',
                y: [6502.67, 6507.8, 6490.5, 6503.01]
              },
              {
                x: '8 March 2024',
                y: [6503.1, 6509.99, 6502.8, 6508.01]
              },
              {
                x: '9 March 2024',
                y: [6508.55, 6512.3, 6501.78, 6508.9]
              },
              {
                x: '10 March 2024',
                y: [6509.01, 6512.5, 6501.9, 6507.89]
              }
            ]
          }
        ],
        chart: {
          width: 100,
          height: 50,
          type: 'candlestick',
          sparkline: {
            enabled: true
          }
        },
        plotOptions: {
          candlestick: {
            colors: {
              upward: 'var(--color-primary)',
              downward: 'var(--color-primary)'
            }
          }
        },
        colors: ['var(--color-primary)'],
        xaxis: {
          type: 'category',
          categories: [
            '1 March 2024',
            '2 March 2024',
            '3 March 2024',
            '4 March 2024',
            '5 March 2024',
            '6 March 2024',
            '7 March 2024',
            '8 March 2024',
            '9 March 2024',
            '10 March 2024'
          ],
          crosshairs: {
            show: false
          }
        },
        tooltip: {
          marker: {
            show: false
          },
          fixed: {
            enabled: true,
            position: 'bottomLeft',
            offsetX: 10,
            offsetY: -15
          },
          custom: function (props) {
            const { categories } = props.ctx.opts.xaxis
            const { dataPointIndex } = props
            const title = categories[dataPointIndex].split(' ')
            const newTitle = `${title[0]} ${title[1]}`

            return buildTooltip(props, {
              title: newTitle,
              mode,
              hasTextLabel: true,
              wrapperExtClasses: 'min-w-28',
              titleExtClasses: 'text-left',
              labelDivider: ':',
              labelExtClasses: 'ms-2'
            })
          }
        }
      }))
      // Sparklines candlestick chart (End)
      // Sparklines charts (End)
    })()
  })
</script>

{{< /code >}}
