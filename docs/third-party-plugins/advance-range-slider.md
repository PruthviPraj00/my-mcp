---
title: "Advance Range Slider"
description: "The Slider component enables easy, customizable range selection for user settings."
bg_image: "svg/third-party-plugins/range-slider.svg"
components: 24
menu:
  main:
    parent: "third party plugins"

previous: Window
previousLink: mockups/window/

next: Animation
nextLink: third-party-plugins/animation/

requires_js: true

pageJS:
  - "/js/helper/helper-apexcharts.js"
  - "/js/pages/nouislider.js"

vendorJS:
  - "https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"
  - "/vendor/nouislider/nouislider.js"
  - "/vendor/apexcharts/apexcharts.js"

vendorCSS:
  - "/vendor/nouislider/nouislider.css"
  - "/vendor/apexcharts/apexcharts.css"
---

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://refreshless.com/nouislider/" target="_blank" class="link link-primary font-semibold">noUiSlider</a> with FlyonUI.

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
      <p>Install <code> noUiSlider </code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm i nouislider{{< /code-highlight >}}
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
      <div class="text-base-content mb-3 font-semibold">Include noUiSlider JavaScript</div>
      <p>Include the following  JS files in your page:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<body>
  <script src="../path/to/vendor/nouislider/dist/nouislider.min.js"></script>
</body>{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>
 <!-- noUiSlider Initialization & Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        3
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Initialize noUiSlider</div>
      <p>Basic Initialization: Prefer to design your own style? Here’s a fully unstyled example for customization.</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="html" >}}<div data-range-slider='{
  "start": 50,
  "connect": "lower",
  "range": {
    "min": 0,
    "max": 100
  }
}'></div>{{< /code-highlight >}}
    </div>

  </li>
</ul>

<!-- Class Table -->

{{< class-table >}}
range-slider-disabled:{tw-utility-class} | variant | Apply tailwind classes when the disabled is true.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Simple usage -->

{{< headname level="3" >}} Simple usage {{< /headname >}}

Design a unique range slider.

{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  data-range-slider='{
  "start": 50,
  "connect": "lower",
  "range": {
    "min": 0,
    "max": 100
  },
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>
{{< /code >}}

<!-------------------- Color -------------------->

{{< headname level="2" >}} Color {{< /headname >}}

<!-- Semantic colors -->

{{< headname level="3" >}} Semantic colors {{< /headname >}}

An example showcasing the set of semantic colors.

{{< code hasRTL="false" addClass="!flex-col space-y-5" >}}

<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-2 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
      "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
      "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>

<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-2 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
      "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-secondary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-secondary active:ring-[3px]",
      "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-secondary origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>

<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-2 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
      "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-info rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-info active:ring-[3px]",
      "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-info origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>

<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-2 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
     "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-success rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-success active:ring-[3px]",
      "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-success origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>
<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-2 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
      "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-warning rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-warning active:ring-[3px]",
      "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-warning origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>
<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-2 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
      "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-error rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-error active:ring-[3px]",
      "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-error origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>
{{< /code >}}

<!-------------------- Size -------------------->

{{< headname level="2" >}} Size {{< /headname >}}

<!-- Basic sizing -->

{{< headname level="3" >}} Basic sizing {{< /headname >}}

Sizing for advance range slider.

{{< code hasRTL="false" addClass="!flex-col space-y-5" >}}

<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-1 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
      "handle": "absolute top-1/2 end-0 rtl:start-0 size-2.5 bg-base-100 border-[2.5px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
      "connects": "relative z-0 w-full h-1 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>

<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-1.5 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
      "handle": "absolute top-1/2 end-0 rtl:start-0 size-3 bg-base-100 border-[2.5px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
      "connects": "relative z-0 w-full h-1.5 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>

<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-2 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
      "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
      "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>

<div>
  <label class="sr-only">Example</label>

  <div
    data-range-slider='{
    "start": 50,
    "connect": "lower",
    "range": {
      "min": 0,
      "max": 100
    },
    "cssClasses": {
      "target": "relative h-3 rounded-full bg-neutral/10",
      "base": "size-full relative z-1",
      "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
     "handle": "absolute top-1/2 end-0 rtl:start-0 size-6 bg-base-100 border-4 border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
      "connects": "relative z-0 w-full h-3 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
      "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
    }
  }'>
  </div>
</div>
{{< /code >}}

<!-------------------- Orientation -------------------->

{{< headname level="2" >}} Orientation {{< /headname >}}

<!-- Vertical Default -->

{{< headname level="3" >}} Vertical Default {{< /headname >}}

The orientation setting allows you to configure the slider as either `"vertical"` or `"horizontal"`, with `"horizontal"` as the default.

{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  data-range-slider='{
  "start": [25, 75],
  "orientation": "vertical",
  "range": {
    "min": 0,
    "max": 100
  },
  "connect": true,
  "cssClasses": {
    "target": "relative h-40 w-2 rounded-full bg-neutral/10",
      "base": "size-full relative z-1 h-full",
      "origin": "absolute start-0 top-0 size-full origin-[0_0] rounded-full",
      "handle": "absolute left-1/2 top-0 size-4 bg-base-100 border-[3px] border-primary rounded-full -translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
      "connects": "relative z-0 h-full w-2 overflow-hidden",
      "connect": "absolute bottom-0 z-1 size-full bg-primary origin-[0_0]",
      "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>
{{< /code >}}

<!-- Vertical upper connect -->

{{< headname level="3" >}} Vertical upper connect {{< /headname >}}

Basic Vertical upper connect example.

{{< code hasRTL="false" addClass="!block" >}}

<label class="sr-only">Vertical Slider Example</label>

<div
  data-range-slider='{
  "start": 50,
  "connect": "upper",
  "orientation": "vertical",
  "range": {
    "min": 0,
    "max": 100
  },
  "cssClasses": {
    "target": "relative h-40 w-2 rounded-full bg-neutral/10",
    "base": "size-full relative z-1 h-full",
    "origin": "absolute start-0 top-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute left-1/2 top-0 size-4 bg-base-100 border-[3px] border-primary rounded-full -translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 h-full w-2 rounded-b-full overflow-hidden",
    "connect": "absolute bottom-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>
{{< /code >}}

<!-- Vertical range with tooltip -->

{{< headname level="3" >}} Vertical range with tooltip {{< /headname >}}

Vertical range with tooltip example.

{{< code hasRTL="false" addClass="!block" >}}

<label class="sr-only">Vertical Slider Example</label>

<div
  data-range-slider='{
  "start": 40,
  "connect": "lower",
  "orientation": "vertical",
  "range": {
    "min": 0,
    "max": 100
  },
  "direction": "rtl",
  "tooltips": true,
  "formatter": "integer",
  "cssClasses": {
    "target": "relative h-40 w-2 rounded-full bg-neutral/10",
    "base": "size-full relative z-1 h-full",
    "origin": "absolute start-0 top-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute left-1/2 top-0 size-4 bg-base-100 border-[3px] border-primary rounded-full -translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 h-full w-2 rounded-b-full overflow-hidden",
    "connect": "absolute bottom-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1",
    "tooltip": "bg-neutral text-sm text-neutral-content shadow-base-300/20 py-1 px-2 rounded-selector ms-3 start-3/4 -top-2.5 absolute shadow-md"
  }
}'
></div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Disabled -->

{{< headname level="3" >}} Disabled {{< /headname >}}

Set the `disabled` attribute to `true` on an element to give it a grayed-out appearance, disable pointer events, and prevent it from being focused. Use `range-slider-disabled:{tw-utility-class}` to apply styles to the disabled state.

{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  data-range-slider='{
  "start": 50,
  "disabled": true,
  "connect": "lower",
  "range": {
    "min": 0,
    "max": 100
  },
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>
{{< /code >}}

<!-- RTL -->

{{< headname level="3" >}} RTL {{< /headname >}}

RTL functionality works differently in noUiSlider; setting `dir="rtl"` to the `html` element won’t work. Instead, you need to set `direction: "rtl"` as an option in `data-range-slider`.
{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  data-range-slider='{
  "start": 50,
  "connect": "lower",
  "range": {
    "min": 0,
    "max": 100
  },
  "direction": "rtl",
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 rtl:rounded-s-full rtl:rounded-e-none rounded-e-full overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>
{{< /code >}}

<!-- Steps -->

{{< headname level="3" >}} Steps {{< /headname >}}

Range inputs, by default, `“snap”` to integer values. To adjust this behavior, set the `step` attribute to a specific integer value.

{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  data-range-slider='{
  "start": 3,
  "connect": "lower",
  "range": {
    "min": 0,
    "max": 6
  },
  "step": 1,
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>
{{< /code >}}

<!-- Tooltip -->

{{< headname level="3" >}} Tooltip {{< /headname >}}

Enable the `tooltips` parameter by setting it to `true` to display current values within the tooltip.

{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  class="sm:mt-7 mt-10"
  data-range-slider='{
  "start": 32,
  "connect": "lower",
  "range": {
    "min": 0,
    "max": 100
  },
  "tooltips": true,
  "formatter": "integer",
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1",
    "tooltip": "bg-neutral text-sm text-neutral-content shadow-base-300/20 py-1 px-2 rounded-selector mb-3 absolute bottom-full start-2/4 -translate-x-2/4 rtl:translate-x-2/4 shadow-md"
  }
}'
></div>
{{< /code >}}

<!-- Range -->

{{< headname level="3" >}} Range {{< /headname >}}

To enable range mode, set the `start` parameter to an array containing two values.

{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  data-range-slider='{
  "start": [35, 85],
  "range": {
    "min": 0,
    "max": 100
  },
  "connect": true,
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>
{{< /code >}}

<!-- Range with Tooltip -->

{{< headname level="3" >}} Range with Tooltip {{< /headname >}}

Demonstrating the combination of tooltips and range mode.

{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  class="sm:mt-7 mt-10"
  data-range-slider='{
  "start": [15, 65],
  "range": {
    "min": 0,
    "max": 100
  },
  "connect": true,
  "tooltips": true,
  "formatter": "integer",
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1",
    "tooltip": "bg-neutral text-sm text-neutral-content shadow-base-300/20 py-1 px-2 rounded-selector mb-3 absolute bottom-full start-2/4 -translate-x-2/4 rtl:translate-x-2/4 shadow-md"
  }
}'
></div>
{{< /code >}}

<!-- Pips -->

{{< headname level="3" >}} Pips {{< /headname >}}

To enable the display of pips, set the `pips` parameter to an object with specific configuration settings.

{{< code hasRTL="false" addClass="!block">}}
<label class="sr-only">Example</label>

<div
  class="sm:my-7 my-10 "
  data-range-slider='{
  "start": [110, 430],
  "range": {
    "min": 0,
    "max": 500
  },
  "connect": true,
  "pips": {
    "mode": "values",
    "values": [0, 125, 250, 375, 500],
    "density": 20
  },
  "tooltips": true,
  "formatter": "integer",
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1",
    "tooltip": "bg-neutral text-sm text-neutral-content shadow-base-300/20 py-1 px-2 rounded-selector mb-3 absolute bottom-full start-2/4 -translate-x-2/4 rtl:translate-x-2/4 shadow-md",
    "pips": "relative w-full h-7 mt-3",
    "value": "absolute top-4 -translate-x-2/4 text-sm text-base-content/80",
    "marker": "absolute h-4 border-s border-base-content/25"
  }
}'
></div>
{{< /code >}}

<!-- Pips auto values -->

{{< headname level="3" >}} Pips auto values {{< /headname >}}

Drawing pips according to the number of steps.

{{< code hasRTL="false" addClass="!block">}}
<label class="sr-only">Example</label>

<div
  class="sm:my-7 my-10 "
  data-range-slider='{
  "start": [70, 260],
  "range": {
    "min": 0,
    "max": 500
  },
  "connect": true,
  "pips": {
    "mode": "count",
    "values": 5
  },
  "tooltips": true,
  "formatter": {
    "type": "integer",
    "prefix": "$"
  },
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1",
    "tooltip": "bg-neutral text-sm text-neutral-content shadow-base-300/20 py-1 px-2 rounded-selector mb-3 absolute bottom-full start-2/4 -translate-x-2/4 rtl:translate-x-2/4 shadow-md",
    "pips": "relative w-full h-7 mt-3",
    "value": "absolute top-4 -translate-x-2/4 text-sm text-base-content/80",
    "marker": "absolute border-s border-base-content/25",
    "markerNormal": "h-2",
    "markerLarge": "h-4"
  }
}'
></div>
{{< /code >}}
<!-- Pass value to HTML element -->

{{< headname level="3" >}} Pass value to HTML element {{< /headname >}}

Use the `update` method to set a value as the text content of an element.

{{< code hasRTL="false" addClass="!block" jsCode="true">}}
<label class="sr-only">Example</label>

<div
  id="range-element"
  class="--prevent-on-load-init sm:mt-7 mt-10"
  data-range-slider='{
  "start": 302,
  "connect": "lower",
  "range": {
    "min": 0,
    "max": 1000
  },
  "tooltips": true,
  "formatter": "integer",
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1",
    "tooltip": "bg-neutral text-sm text-neutral-content shadow-base-300/20 py-1 px-2 rounded-selector mb-3 absolute bottom-full start-2/4 -translate-x-2/4 rtl:translate-x-2/4 shadow-md"
  }
}'
></div>

<div class="mt-5 text-sm font-medium">
  Value:
  <span id="range-element-target" class="text-primary">750</span>
</div>

<!-- Js -->

<script>
  window.addEventListener('load', function () {
    const range = document.querySelector('#range-element')
    const rangeInstance = new HSRangeSlider(range)
    const target = document.querySelector('#range-element-target')

    range.noUiSlider.on('update', values => (target.innerText = rangeInstance.formattedValue))
  })
</script>

{{< /code >}}

<!-- Pass values to HTML elements (Range) -->

{{< headname level="3" >}} Pass values to HTML elements (Range) {{< /headname >}}

Using the `update` method to assign values as text to the min and max elements.

{{< code hasRTL="false" addClass="!block" jsCode="true">}}

<div class="mb-5 flex w-full justify-center">
  <div class="flex items-center text-sm rtl:flex-row-reverse">
    <div id="range-elements-min-target" class="min-w-16 text-center">310</div>
    -
    <div id="range-elements-max-target" class="min-w-16 text-center">635</div>
  </div>
</div>
<label class="sr-only">Example range</label>
<div
  id="range-multi-elements"
  class="--prevent-on-load-init"
  data-range-slider='{
  "start": [310, 635],
  "range": {
    "min": 0,
    "max": 1000
  },
  "formatter": {
    "type": "integer",
    "prefix": "$"
  },
  "connect": true,
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>

<!-- Js -->

<script>
  window.addEventListener('load', function () {
    const rangeMulti = document.querySelector('#range-multi-elements')
    const rangeMultiInstance = new HSRangeSlider(rangeMulti)
    const min = document.querySelector('#range-elements-min-target')
    const max = document.querySelector('#range-elements-max-target')

    rangeMulti.noUiSlider.on('update', values => {
      min.innerText = rangeMultiInstance.formattedValue[0]
      max.innerText = rangeMultiInstance.formattedValue[1]
    })
  })
</script>

{{< /code >}}

<!-- Applying Thousand Separators and Decimal Formatting -->

{{< headname level="3" >}} Applying Thousand Separators and Decimal Formatting {{< /headname >}}

Using the `update` method to assign values as text to the min and max elements.

{{< code hasRTL="false" addClass="!block" jsCode="true">}}

<div class="mb-5 flex w-full justify-center">
  <div class="flex items-center text-sm rtl:flex-row-reverse">
    <div id="thousands-separators-and-decimal-points-min-target" class="min-w-36 text-center">130</div>
    -
    <div id="thousands-separators-and-decimal-points-max-target" class="min-w-36 text-center">610</div>
  </div>
</div>
<label class="sr-only">Example range</label>
<div
  id="thousands-separators-and-decimal-points"
  class="--prevent-on-load-init"
  data-range-slider='{
  "start": [1300000, 6100000],
  "range": {
    "min": 0,
    "max": 10000000
  },
  "connect": true,
  "formatter": {
    "prefix": "USD ",
    "type": "thousandsSeparatorAndDecimalPoints"
  },
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>

<!-- Js -->

<script>
  window.addEventListener('load', function () {
    const rangeSeparator = document.querySelector('#thousands-separators-and-decimal-points')
    const rangeSeparatorInstance = new HSRangeSlider(rangeSeparator)
    const minSeparator = document.querySelector('#thousands-separators-and-decimal-points-min-target')
    const maxSeparator = document.querySelector('#thousands-separators-and-decimal-points-max-target')

    rangeSeparator.noUiSlider.on('update', values => {
      minSeparator.innerText = rangeSeparatorInstance.formattedValue[0]
      maxSeparator.innerText = rangeSeparatorInstance.formattedValue[1]
    })
  })
</script>

{{< /code >}}

<!-- Assign value to input -->

{{< headname level="3" >}} Assign value to input {{< /headname >}}

Using the `update` method to set values as input field values.

{{< callout "info" >}}
Some JavaScript helpers in FlyonUI rely on the Lodash library. Make sure to install it if you haven't already: <span class="px-0.5 text-base-content border border-base-content/25 rounded-md text-sm">npm i lodash</span>
{{< /callout >}}

{{< code hasRTL="false" addClass="!block" jsCode="true">}}
<label class="sr-only">Example</label>

<div
  id="range-input-element"
  class="--prevent-on-load-init sm:mt-7 mt-10"
  data-range-slider='{
  "start": 505,
  "connect": "lower",
  "range": {
    "min": 0,
    "max": 1000
  },
  "tooltips": true,
  "formatter": "integer",
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1",
    "tooltip": "bg-neutral text-sm text-neutral-content shadow-base-300/20 py-1 px-2 rounded-selector mb-3 absolute bottom-full start-2/4 -translate-x-2/4 rtl:translate-x-2/4 shadow-md"
  }
}'
></div>

<div class="mt-5 max-w-xs">
  <input id="range-input-target" class="input" type="text" value="505" />
</div>

<!-- Js -->

<script>
  window.addEventListener('load', function () {
    const rangeInput = document.querySelector('#range-input-element')
    const rangeInputInstance = new HSRangeSlider(rangeInput)
    const targetInput = document.querySelector('#range-input-target')

    rangeInput.noUiSlider.on('update', values => (targetInput.value = rangeInputInstance.formattedValue))
    targetInput.addEventListener(
      'input',
      _.debounce(evt => rangeInputInstance.el.noUiSlider.set(evt.target.value)),
      200
    )
  })
</script>

{{< /code >}}

<!-- Assign values to multiple input fields -->

{{< headname level="3" >}} Assign values to multiple input fields {{< /headname >}}

Using the `update` method to pass values as inputs value.

{{< callout "info" >}}
Some JavaScript helpers in FlyonUI rely on the Lodash library. Make sure to install it if you haven't already: <span class="px-0.5 text-base-content border border-base-content/25 rounded-md text-sm">npm i lodash</span>
{{< /callout >}}

{{< code hasRTL="false" addClass="!block" jsCode="true">}}
<label class="sr-only">Example range</label>

<div
  id="range-multi-inputs"
  class="--prevent-on-load-init sm:mt-7 mt-10"
  data-range-slider='{
  "start": [150, 650],
  "range": {
    "min": 0,
    "max": 1000
  },
  "connect": true,
  "tooltips": true,
  "formatter": "integer",
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1",
    "tooltip": "bg-neutral text-sm text-neutral-content shadow-base-300/20 py-1 px-2 rounded-selector mb-3 absolute bottom-full start-2/4 -translate-x-2/4 rtl:translate-x-2/4 shadow-md"
  }
}'
></div>

<div class="mt-5 flex flex-row space-x-4 rtl:flex-row-reverse">
  <div class="basis-1/2">
    <label for="inputs-min-target" class="mb-2 block text-sm font-medium">Min price:</label>
    <input id="inputs-min-target" class="input" type="number" value="150" />
  </div>
  <div class="basis-1/2">
    <label for="inputs-max-target" class="mb-2 block text-sm font-medium">Max price:</label>
    <input id="inputs-max-target" class="input" type="number" value="650" />
  </div>
</div>

<!-- Js -->

<script>
  window.addEventListener('load', function () {
    const rangeMultiple = document.querySelector('#range-multi-inputs')
    const rangeMultipleInstance = new HSRangeSlider(rangeMultiple)
    const minValue = document.querySelector('#inputs-min-target')
    const maxValue = document.querySelector('#inputs-max-target')

    rangeMultiple.noUiSlider.on('update', values => {
      minValue.value = rangeMultipleInstance.formattedValue[0]
      maxValue.value = rangeMultipleInstance.formattedValue[1]
    })
    minValue.addEventListener(
      'input',
      _.debounce(evt => rangeMultipleInstance.el.noUiSlider.set([evt.target.value, maxValue.value]), 200)
    )
    maxValue.addEventListener(
      'input',
      _.debounce(evt => rangeMultipleInstance.el.noUiSlider.set([minValue.value, evt.target.value]), 200)
    )
  })
</script>

{{< /code >}}

<!-- Range with Charts Example -->

{{< headname level="3" >}} Range with Charts Example {{< /headname >}}

Using the `update` method and its returned values to adjust the foreground chart width.

{{< callout "info" >}}
Please note that this demo requires the third-party <a href="https://apexcharts.com/docs/installation/" target="_blank" class="link link-primary font-medium">ApexCharts JS</a> plugin. For more details, refer to the {{< link link="third-party-plugins/apex-charts/" addClass="link font-medium link-primary" >}}FlyonUI ApexCharts documentation{{< /link >}}.
{{< /callout >}}

{{< callout "info" >}}
Some JavaScript helpers in FlyonUI rely on the Lodash library. Make sure to install it if you haven't already: <span class="px-0.5 text-base-content border border-base-content/25 rounded-md text-sm">npm i lodash</span>
{{< /callout >}}

{{< code hasRTL="false" addClass="!block" jsCode="true">}}
<label class="sr-only">Example range</label>

<div class="relative" dir="ltr">
  <div id="range-chart-background"></div>
  <div class="absolute start-0 top-0 size-full overflow-hidden">
    <div id="range-chart-foreground"></div>
  </div>
</div>
<div
  id="range-charts"
  class="--prevent-on-load-init mt-4"
  data-range-slider='{
  "start": [130, 520],
  "range": {
    "min": 0,
    "max": 1000
  },
  "connect": true,
  "formatter": "integer",
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>

<div class="mt-5">
  <div class="mb-2 text-sm font-medium">Custom range:</div>
  <div class="flex flex-row gap-4">
    <div class="basis-1/2">
      <input id="range-charts-inputs-min-target" class="input" type="number" value="130" />
    </div>
    <div class="basis-1/2">
      <input id="range-charts-inputs-max-target" class="input" type="number" value="520" />
    </div>
  </div>
</div>

<!-- Js -->

<script>
window.addEventListener('load', () => {
  ;(function () {
    const updateForegroundChart = (foregroundParent, foreground, values) => {
      const from = (100 * values[0]) / 1000
      const to = (100 * values[1]) / 1000
      const width = 100 - (from + (100 - to))

      foregroundParent.style.left = `${from}%`
      foregroundParent.style.width = `${width}%`
      foreground.style.width = `${foregroundParent.parentElement.clientWidth}px`
      foreground.style.marginLeft = `${-((foregroundParent.parentElement.clientWidth / 100) * from)}px`
    }

    const range = document.querySelector('#range-charts')
    const rangeInstance = new HSRangeSlider(range)
    const min = document.querySelector('#range-charts-inputs-min-target')
    const max = document.querySelector('#range-charts-inputs-max-target')
    const foreground = document.querySelector('#range-chart-foreground')
    const foregroundParent = foreground.parentElement
    // Backgound chart
    buildChart('#range-chart-background', mode => ({
      series: [
        {
          name: 'Sales',
          data: [
            0, 20, 24, 45, 47, 50, 60, 70, 80, 75, 65, 55, 50, 40, 30, 30, 35, 45, 50, 60, 70, 80, 75, 65, 55, 50, 40,
            35, 40
          ]
        }
      ],
      chart: {
        height: 150,
        type: 'area',
        sparkline: {
          enabled: true
        }
      },
      colors: ['color-mix(in oklab, var(--color-base-content) 5%, transparent)'],
      fill: {
        type: 'gradient',
        gradient: {
          shadeIntensity: 1,
          opacityFrom: 0.7,
          gradientToColors: ['color-mix(in oklab, var(--color-base-300) 20%, transparent)'],
          opacityTo: 0.3,
          stops: [0, 90, 100]
        }
      },
      stroke: {
        curve: 'smooth',
        width: 2
      },
      xaxis: {
        type: 'category',
        crosshairs: {
          show: false
        }
      },
      states: {
        hover: {
          filter: {
            type: 'none'
          }
        },
        active: {
          allowMultipleDataPointsSelection: false,
          filter: {
            type: 'none'
          }
        }
      },
      tooltip: {
        enabled: false
      }
    }))
    // Foreground chart
    buildChart('#range-chart-foreground', mode => ({
      series: [
        {
          name: 'Sales',
          data: [
            0, 20, 24, 45, 47, 50, 60, 70, 80, 75, 65, 55, 50, 40, 30, 30, 35, 45, 50, 60, 70, 80, 75, 65, 55, 50, 40,
            35, 40
          ]
        }
      ],
      chart: {
        height: 150,
        type: 'area',
        sparkline: {
          enabled: true
        }
      },
      colors: ['var(--color-primary)'],
      stroke: {
        curve: 'smooth',
        width: 2
      },
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
      grid: {
        borderColor: 'color-mix(in oklab, var(--color-base-200) 40%, transparent)'
      },
      xaxis: {
        type: 'category',
        crosshairs: {
          show: false
        }
      },
      states: {
        hover: {
          filter: {
            type: 'none'
          }
        },
        active: {
          allowMultipleDataPointsSelection: false,
          filter: {
            type: 'none'
          }
        }
      },
      tooltip: {
        enabled: false
      }
    }))

    range.noUiSlider.on('update', values => {
      min.value = rangeInstance.formattedValue[0]
      max.value = rangeInstance.formattedValue[1]

      updateForegroundChart(foregroundParent, foreground, values)
    })

    min.addEventListener(
      'input',
      _.debounce(evt => rangeInstance.el.noUiSlider.set([evt.target.value, max.value]), 200)
    )
    max.addEventListener(
      'input',
      _.debounce(evt => rangeInstance.el.noUiSlider.set([min.value, evt.target.value]), 200)
    )

    window.addEventListener('resize', () => updateForegroundChart(foregroundParent, foreground, range.noUiSlider.get()))
  })()
})
</script>

{{< /code >}}

<!-- Range with Charts Example (Modal) -->

{{< headname level="3" >}} Range with Charts Example (Modal) {{< /headname >}}

Adjust the chart’s foreground width inside a `modal` using the `update` method’s return values.

{{< callout "info" >}}
Please note that this demo requires the third-party <a href="https://apexcharts.com/docs/installation/" target="_blank" class="link link-primary font-medium">ApexCharts JS</a> plugin. For more details, refer to the {{< link link="third-party-plugins/apex-charts/" addClass="link font-medium link-primary" >}}FlyonUI ApexCharts documentation{{< /link >}}.
{{< /callout >}}

{{< callout "info" >}}
Some JavaScript helpers in FlyonUI rely on the Lodash library. Make sure to install it if you haven't already: <span class="px-0.5 text-base-content border border-base-content/25 rounded-md text-sm">npm i lodash</span>
{{< /callout >}}

{{< code hasRTL="false" addClass="!block" jsCode="true">}}
<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="range-with-chart-modal" data-overlay="#range-with-chart-modal" >
  Open modal
</button>

<div id="range-with-chart-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 modal-dialog-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Dialog Title</h3>
        <button
          type="button"
          class="btn btn-text btn-circle btn-sm absolute end-3 top-3"
          aria-label="Close"
          data-overlay="#range-with-chart-modal"
        >
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <label class="sr-only">Example range</label>
        <div class="relative" dir="ltr">
          <div id="range-chart-background-modal"></div>
          <div class="absolute start-0 top-0 size-full overflow-hidden">
            <div id="range-chart-foreground-modal"></div>
          </div>
        </div>
        <div
          id="range-charts-with-modal"
          class="--prevent-on-load-init mt-4"
          data-range-slider='{
          "start": [290, 680],
          "range": {
            "min": 0,
            "max": 1000
          },
          "connect": true,
          "formatter": "integer",
          "cssClasses": {
            "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
            "base": "size-full relative z-[1]",
            "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
            "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
            "connects": "relative z-0 w-full h-2 overflow-hidden",
            "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
            "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
          }
        }'
        ></div>
        <div class="mt-5">
          <div class="mb-2 text-sm font-medium">Custom range:</div>
          <div class="flex flex-row gap-4">
            <div class="basis-1/2">
              <input id="range-charts-inputs-min-target-modal" class="input" type="number" value="290" />
            </div>
            <div class="basis-1/2">
              <input id="range-charts-inputs-max-target-modal" class="input" type="number" value="680" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Js -->

<script>
window.addEventListener('load', () => {
  ;(function () {
    const updateForegroundChart = (foregroundParent, foreground, values) => {
      const from = (100 * values[0]) / 1000
      const to = (100 * values[1]) / 1000
      const width = 100 - (from + (100 - to))

      foregroundParent.style.left = `${from}%`
      foregroundParent.style.width = `${width}%`
      foreground.style.width = `${foregroundParent.parentElement.clientWidth}px`
      foreground.style.marginLeft = `${-((foregroundParent.parentElement.clientWidth / 100) * from)}px`
    }

    const range = document.querySelector('#range-charts-with-modal')
    const rangeInstance = new HSRangeSlider(range)
    const min = document.querySelector('#range-charts-inputs-min-target-modal')
    const max = document.querySelector('#range-charts-inputs-max-target-modal')
    const foreground = document.querySelector('#range-chart-foreground-modal')
    const foregroundParent = foreground.parentElement
    // Backgound chart
    buildChart('#range-chart-background-modal', mode => ({
      series: [
        {
          name: 'Sales',
          data: [
            0, 20, 24, 45, 47, 50, 60, 70, 80, 75, 65, 55, 50, 40, 30, 30, 35, 45, 50, 60, 70, 80, 75, 65, 55, 50, 40,
            35, 40
          ]
        }
      ],
      chart: {
        height: 150,
        type: 'area',
        sparkline: {
          enabled: true
        }
      },

      colors: ['color-mix(in oklab, var(--color-base-content) 5%, transparent)'],
      fill: {
        type: 'gradient',
        gradient: {
          shadeIntensity: 1,
          opacityFrom: 0.7,
          gradientToColors: ['color-mix(in oklab, var(--color-base-300) 20%, transparent)'],
          opacityTo: 0.3,
          stops: [0, 90, 100]
        }
      },
      stroke: {
        curve: 'smooth',
        width: 2
      },
      xaxis: {
        type: 'category',
        crosshairs: {
          show: false
        }
      },
      states: {
        hover: {
          filter: {
            type: 'none'
          }
        },
        active: {
          allowMultipleDataPointsSelection: false,
          filter: {
            type: 'none'
          }
        }
      },
      tooltip: {
        enabled: false
      }
    }))
    // Foreground chart
    buildChart('#range-chart-foreground-modal', mode => ({
      series: [
        {
          name: 'Sales',
          data: [
            0, 20, 24, 45, 47, 50, 60, 70, 80, 75, 65, 55, 50, 40, 30, 30, 35, 45, 50, 60, 70, 80, 75, 65, 55, 50, 40,
            35, 40
          ]
        }
      ],
      chart: {
        height: 150,
        type: 'area',
        sparkline: {
          enabled: true
        }
      },
      colors: ['var(--color-primary)'],
      stroke: {
        curve: 'smooth',
        width: 2
      },
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
      grid: {
        borderColor: 'color-mix(in oklab, var(--color-base-200) 40%, transparent)'
      },
      xaxis: {
        type: 'category',
        crosshairs: {
          show: false
        }
      },
      states: {
        hover: {
          filter: {
            type: 'none'
          }
        },
        active: {
          allowMultipleDataPointsSelection: false,
          filter: {
            type: 'none'
          }
        }
      },
      tooltip: {
        enabled: false
      }
    }))

    range.noUiSlider.on('update', values => {
      min.value = rangeInstance.formattedValue[0]
      max.value = rangeInstance.formattedValue[1]

      updateForegroundChart(foregroundParent, foreground, values)
    })

    min.addEventListener(
      'input',
      _.debounce(evt => rangeInstance.el.noUiSlider.set([evt.target.value, max.value]), 200)
    )
    max.addEventListener(
      'input',
      _.debounce(evt => rangeInstance.el.noUiSlider.set([min.value, evt.target.value]), 200)
    )

    window.addEventListener('resize', () => updateForegroundChart(foregroundParent, foreground, range.noUiSlider.get()))

    // Please add it for the popup to work correctly.
    const popup = HSOverlay.getInstance('#range-with-chart-modal', true)

    popup.element.on('open', () => updateForegroundChart(foregroundParent, foreground, range.noUiSlider.get()))
  })()
})
</script>

{{< /code >}}

<!-- Destroy/Reinitialize -->
{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}
The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a advance range slider.

{{< code addClass="!block" jsCode="true" >}}
<label class="sr-only">Example</label>

<div
  id="range-slider-to-destroy"
  data-range-slider='{
  "start": [25, 75],
  "range": {
    "min": 0,
    "max": 100
  },
  "connect": true,
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    // Destroy and reinit variables
  const slider = document.querySelector('#range-slider-to-destroy')
  const destroyBtn = document.querySelector('#destroy-btn')
  const reinitBtn = document.querySelector('#reinit-btn')

  // Destroy usage
  destroyBtn.addEventListener('click', () => {
    const { element } = HSRangeSlider.getInstance(slider, true)

    element.destroy()

    destroyBtn.setAttribute('disabled', 'disabled')
    reinitBtn.removeAttribute('disabled')
  })

  // Reinit usage
  reinitBtn.addEventListener('click', () => {
    HSRangeSlider.autoInit()

    reinitBtn.setAttribute('disabled', 'disabled')
    destroyBtn.removeAttribute('disabled')
  })
  })
</script>
{{< /code >}}

<!-------------------- Slider behaviour -------------------->

{{< headname level="2" >}} Slider behaviour {{< /headname >}}

<!-- Tap -->

{{< headname level="3" >}} Tap {{< /headname >}}

A handle snaps to a clicked location. A smooth transition is used. This option is **default**.

{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  data-range-slider='{
  "start": 50,
  "connect": "lower",
  "behaviour": "tap",
  "range": {
    "min": 0,
    "max": 100
  },
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>
{{< /code >}}

<!-- Drag -->

{{< headname level="3" >}} Drag {{< /headname >}}

Enables dragging of the range (the connecting bar between handles). This requires two handles, and the `connect` option **must** be set to `true`. When dragging the range, the slide event triggers for both handles.

{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div data-range-slider='{
  "start": [25, 75],
  "behaviour": "drag",
  "range": {
    "min": 0,
    "max": 100
  },
  "connect": true,
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'></div>
{{< /code >}}

<!-- Fixed dragging -->

{{< headname level="3" >}} Fixed dragging {{< /headname >}}

Maintains a fixed distance between handles when the `drag-fixed` flag is enabled.
{{< code hasRTL="false" addClass="!block" >}}
<label class="sr-only">Example</label>

<div
  data-range-slider='{
  "start": [30, 60],
  "behaviour": "drag-fixed",
  "range": {
    "min": 0,
    "max": 100
  },
  "connect": true,
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>
{{< /code >}}

<!-- Hover -->

{{< headname level="3" >}} Hover {{< /headname >}}

Enabling this option allows the slider to trigger `hover` events when a mouse or pen hovers over it, providing the slider value at the hovered position. The event **does not** trigger while the slider is being dragged with a mouse or pen, but it **does** activate for touch interactions.

{{< code hasRTL="false" addClass="!block" jsCode="true">}}
<label class="sr-only">Example</label>

<div
  id="range-hover-element"
  data-range-slider='{
  "start": 500,
  "behaviour": "hover-snap",
  "connect": "lower",
  "range": {
    "min": 0,
    "max": 1000
  },
  "cssClasses": {
    "target": "relative h-2 rounded-full bg-neutral/10 range-slider-disabled:pointer-events-none range-slider-disabled:opacity-50",
    "base": "size-full relative z-1",
    "origin": "absolute top-0 end-0 rtl:start-0 size-full origin-[0_0] rounded-full",
    "handle": "absolute top-1/2 end-0 rtl:start-0 size-4 bg-base-100 border-[3px] border-primary rounded-full translate-x-2/4 -translate-y-2/4 hover:cursor-grab active:cursor-grabbing hover:ring-2 ring-primary active:ring-[3px]",
    "connects": "relative z-0 w-full h-2 rtl:rounded-e-full rtl:rounded-s-none rounded-s-full overflow-hidden",
    "connect": "absolute top-0 end-0 rtl:start-0 z-1 size-full bg-primary origin-[0_0]",
    "touchArea": "absolute -top-1 -bottom-1 -start-1 -end-1"
  }
}'
></div>

<div class="mt-5 text-sm font-medium">
  Value:
  <span id="range-hover-element-target" class="text-primary">500</span>
</div>

<!-- Js -->

<script>
  window.addEventListener('load', function () {
    const rangeHover = document.querySelector('#range-hover-element')
    const rangeHoverTarget = document.querySelector('#range-hover-element-target')

    rangeHover.noUiSlider.on('hover', values => (rangeHoverTarget.innerText = values))
  })
</script>

{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

<!-- Options table -->

{{< table >}}

PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-range-slider`</span>| <span class="text-pretty">Activate a Range Slider by applying it to a specified element. Attach it to the initialized element. As our plugin extends the <a href="https://refreshless.com/nouislider/" target="_blank" class="link link-primary font-semibold">noUiSlider</a> plugin, all noUiSlider <a href="https://refreshless.com/nouislider/slider-options/" target="_blank" class="link link-primary font-semibold">events</a> can be passed directly as parameters to our plugin.</span> | boolean | `false`
`:disabled`|Disables user interaction with the element, rendering it inactive.|boolean|`false`
`:formatter`|Customizes the output format of the slider values.|string/object|`-`
`:formatter:type`|Sets the output format type, such as integer or thousands separator with decimal points.|"integer" / "thousandsSeparatorAndDecimalPoints" / null|`-`
`:formatter:prefix`|Adds a prefix to the tooltip's output value.|string|`-`
`:formatter:postfix`|Adds a postfix to the tooltip's output value.|string|`-`
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSRangeSlider` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`formattedValue`| Retrieves the current values, formatted according to the specified `formatter` option.
`destroy()`| Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSRangeSlider.getInstance(target, isInstance)`|<div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
{{< /table >}}

<p class="mt-10 mb-1.5 not-prose">Open item (public method), Refer <a href="#pass-value-to-html-element" class="link link-primary">Pass value to HTML element</a>.</p>

{{< code-highlight lang="js" >}}// This method is used in above example.
const rangeInstance = new HSRangeSlider(document.querySelector('#range-element'))
const target = document.querySelector('#range-element-target')

range.noUiSlider.on('update', values => (target.innerText = rangeInstance.formattedValue))
{{< /code-highlight >}}

<p id="destroy-method" class="mt-5 mb-1.5 not-prose">Destroy instance.</p>

{{< code-highlight lang="js" >}}
const { element } = HSRangeSlider.getInstance('#range-slider-to-destroy', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< callout "warning" >}}
All <a href="https://refreshless.com/nouislider/events-callbacks/" target="_blank" class="link link-warning font-semibold">events</a> available in the <a href="https://refreshless.com/nouislider/" target="_blank" class="link link-warning font-semibold">noUiSlider</a> plugin are also supported in our plugin. Simply use `el.noUiSlider` to manage these events.
{{< /callout >}}

{{< table >}}
METHOD| DESCRIPTION | RETURNING VALUE
`on:update`|Called when any item was selected. | `[integer, integer?]`.
{{< /table >}}

<p class="mt-12 mb-1.5 not-prose">Example of an event triggered when the slider is updated.</p>

{{< code-highlight lang="js" >}}const { element } = HSRangeSlider.getInstance('#range-slider', true);

element.el.noUiSlider.on('update', (values) => {
 console.log(element.formattedValue);
});
{{< /code-highlight >}}
