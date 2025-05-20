---
title: "Carousel"
description: "Utilize the carousel component to navigate through various elements and images with customized controls, indicators, intervals, and settings."
bg_image: "svg/components/carousel.svg"
components: 4
tag_bg: "success"
menu:
  main:
    parent: "components"

previous: Card
previousLink: components/card/

next: Chat Bubble
nextLink: components/chat-bubble/

requires_js: true
pageJS:
  - "/js/pages/carousel.js"
---

{{< callout "info" >}}
Carousel components are adopted from <a href="https://preline.co/docs/carousel.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class table -->

{{< class-table >}}
carousel | component | A wrapper for a collection of slides. It must contain the `overflow-hidden` class, it is needed for the slider to work correctly.
carousel-body | part | Slides container.
carousel-slide | part | Single slide.
carousel-prev | part | Previous slide button.
carousel-next | part | Next slide button.
carousel-pagination | part | Base class for pagination container.
carousel-dot | style | Base class for rounded pagination indicators.
carousel-box | style | Base class for box shape pagination indicators.
active | state | When it is applied, the slide becomes visible.
carousel-active:{tw-utility-class}| variant | It sets Tailwind classes when the active slide is shown.
carousel-disabled:{tw-utility-class}| variant | A modifier that allows you to set Tailwind classes for arrow buttons when the they are `disabled`.
carousel-dragging:{tw-utility-class}| variant | A modifier that allows you to set Tailwind classes for `carousel-body` when dragging.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Below example shows the default carousel with three slides.

{{< code hasRTL="false" >}}

<!-- Slider -->
<div
  data-carousel='{
    "loadingClasses": "opacity-0",
    "dotsItemClasses": "carousel-box carousel-active:bg-primary"
  }' class="relative w-full" >
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <div class="carousel-slide">
        <div class="bg-base-200/60 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">First slide</span>
        </div>
      </div>
      <div class="carousel-slide active">
        <div class="bg-base-200/80 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Second slide</span>
        </div>
      </div>
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Third slide</span>
        </div>
      </div>
    </div>
  </div>

  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5"></span>
    <span class="sr-only">Previous</span>
  </button>
  <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>

  <div class="carousel-pagination absolute bottom-3 end-0 start-0 flex justify-center gap-3"></div>
</div>
<!-- End Slider -->

{{< /code >}}

<!-- Indicators -->

{{< headname level="3" >}} Indicators {{< /headname >}}

The example below demonstrates a carousel with indicators. Use `dotsItemClasses:` to style your custom indicators, and apply `carousel-active` to style the active indicator.

{{< code hasRTL="false" >}}

<div
  id="indicators"
  data-carousel='{ "loadingClasses": "opacity-0", "dotsItemClasses": "carousel-dot carousel-active:bg-primary" }'
  class="relative w-full"
>
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="bg-base-200/60 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="bg-base-200/80 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Third slide</span>
        </div>
      </div>
    </div>
  </div>
  <div class="carousel-pagination absolute bottom-3 end-0 start-0 flex justify-center gap-3"></div>
</div>

{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Progress -->

{{< headname level="3" >}} Progress {{< /headname >}}

Below example shows carousel with progress.

{{< code hasRTL="false" >}}

<div data-carousel='{ "loadingClasses": "opacity-0" }' class="relative w-full" id="carousel-progress">
  <div class="carousel h-80 rounded-none">
    <div class="carousel-body h-full opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="bg-base-200/40 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="bg-base-200/60 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="bg-base-200/60 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Third slide</span>
        </div>
      </div>
      <!-- Slide 4 -->
      <div class="carousel-slide">
        <div class="bg-base-200/80 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Fourth slide</span>
        </div>
      </div>
      <!-- Slide 5 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Fifth slide</span>
        </div>
      </div>
    </div>
    <div class="carousel-pagination absolute end-0 start-0 top-0 justify-start space-x-0">
      <span class="carousel-pagination-item carousel-active:block carousel-active:bg-primary hidden h-1 w-1/5"></span>
      <span class="carousel-pagination-item carousel-active:block carousel-active:bg-primary hidden h-1 w-2/5"></span>
      <span class="carousel-pagination-item carousel-active:block carousel-active:bg-primary hidden h-1 w-3/5"></span>
      <span class="carousel-pagination-item carousel-active:block carousel-active:bg-primary hidden h-1 w-4/5"></span>
      <span class="carousel-pagination-item carousel-active:block carousel-active:bg-primary hidden h-1 w-full"></span>
    </div>
  </div>
  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
  <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
{{< /code >}}

<!-- Image carousel -->

{{< headname level="3" >}} Image carousel {{< /headname >}}

Below example shows the carousel with images.

{{< code hasRTL="false" >}}

<div id="image" data-carousel='{ "loadingClasses": "opacity-0" }' class="relative w-full">
  <div class="carousel">
    <div class="carousel-body h-full opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="flex h-full justify-center">
          <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-22.png" class="size-full object-cover" alt="game" />
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="flex h-full justify-center">
          <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-15.png" class="size-full object-cover" alt="vrbox" />
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="flex h-full justify-center">
          <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-16.png" class="size-full object-cover" alt="laptop" />
        </div>
      </div>
      <!-- Slide 4 -->
      <div class="carousel-slide">
        <div class="flex h-full justify-center">
          <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-8.png" class="size-full object-cover" alt="VRBox" />
        </div>
      </div>
      <!-- Slide 5 -->
      <div class="carousel-slide">
        <div class="flex h-full justify-center">
          <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-23.png" class="size-full object-cover" alt="iwatch" />
        </div>
      </div>
    </div>
  </div>
  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
{{< /code >}}

<!-- Thumbs gallery (Horizontal) -->

{{< headname level="3" >}} Thumbs gallery (Horizontal) {{< /headname >}}

Below example shows the carousel with horizontal thumbnails.

{{< code addClass="max-sm:p-3" hasRTL="false" >}}

<div id="horizontal-thumbnails" data-carousel='{ "loadingClasses": "opacity-0" }' class="relative w-full">
  <div class="carousel">
    <div class="carousel-body h-3/4 opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="flex size-full justify-center">
          <img
            src="https://cdn.flyonui.com/fy-assets/components/carousel/image-21.png"
            class="size-full object-cover"
            alt="mountain"
          />
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="flex size-full justify-center">
          <img
            src="https://cdn.flyonui.com/fy-assets/components/carousel/image-14.png"
            class="size-full object-cover"
            alt="sand"
          />
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="flex size-full justify-center">
          <img
            src="https://cdn.flyonui.com/fy-assets/components/carousel/image-7.png"
            class="size-full object-cover"
            alt="cloud"
          />
        </div>
      </div>
    </div>
    <div class="carousel-pagination bg-base-100 absolute bottom-0 end-0 start-0 z-1 h-1/4 gap-2 flex justify-center gap-2 overflow-x-auto pt-2" >
      <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-21.png" class="carousel-pagination-item carousel-active:opacity-100 grow object-cover opacity-30" alt="mountain" />
      <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-14.png" class="carousel-pagination-item carousel-active:opacity-100 grow object-cover opacity-30" alt="sand" />
      <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-7.png" class="carousel-pagination-item carousel-active:opacity-100 grow object-cover opacity-30" alt="cloud" />
    </div>
    <!-- Previous Slide -->
    <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
      <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
      <span class="sr-only">Previous</span>
    </button>
    <!-- Next Slide -->
    <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
      <span class="icon-[tabler--chevron-right] size-5"></span>
      <span class="sr-only">Next</span>
    </button>
  </div>
</div>
{{< /code >}}

<!-- Thumbs gallery (Vertical) -->

{{< headname level="3" >}} Thumbs gallery (Vertical) {{< /headname >}}

Below example shows the carousel with vertical thumbnails.

{{< code addClass="max-sm:p-3" hasRTL="false" >}}

<div id="vertical-thumbnails" data-carousel='{ "loadingClasses": "opacity-0" }' class="relative w-full">
  <div class="carousel flex space-x-2 rounded-none">
    <div class="flex-none">
      <div class="carousel-pagination h-full max-sm:w-8 w-[200px] flex justify-between flex-col gap-y-2 overflow-hidden">
        <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-21.png" class="carousel-pagination-item carousel-active:opacity-100 grow object-cover opacity-30 rounded-lg" alt="mountain" />
        <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-14.png" class="carousel-pagination-item carousel-active:opacity-100 grow object-cover opacity-30 rounded-lg" alt="sand" />
        <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-7.png" class="carousel-pagination-item carousel-active:opacity-100 grow object-cover opacity-30 rounded-lg" alt="cloud" />
      </div>
    </div>
    <div class="relative grow overflow-hidden rounded-2xl">
      <div class="carousel-body h-80 opacity-0">
        <!-- Slide 1 -->
        <div class="carousel-slide">
          <div class="flex size-full justify-center">
            <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-21.png" class="size-full object-cover" alt="mountain" />
          </div>
        </div>
        <!-- Slide 2 -->
        <div class="carousel-slide">
          <div class="flex size-full justify-center">
            <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-14.png" class="size-full object-cover" alt="sand" />
          </div>
        </div>
        <!-- Slide 3 -->
        <div class="carousel-slide">
          <div class="flex size-full justify-center">
            <img
              src="https://cdn.flyonui.com/fy-assets/components/carousel/image-7.png"
              class="size-full object-cover"
              alt="cloud"
            />
          </div>
        </div>
      </div>
      <!-- Previous Slide -->
      <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
        <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
        <span class="sr-only">Previous</span>
      </button>
      <!-- Next Slide -->
      <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
        <span class="icon-[tabler--chevron-right] size-5"></span>
        <span class="sr-only">Next</span>
      </button>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Multi-Slide Carousel -->

{{< headname level="3" >}} Multi-Slide Carousel {{< /headname >}}

A carousel component displays multiple slides arranged side-by-side.

{{< code hasRTL="false" >}}

<div
  id="multi-slide"
  data-carousel='{ "loadingClasses": "opacity-0", "slidesQty": { "xs": 1, "lg": 3 } }'
  class="relative w-full"
>
  <div class="carousel h-80">
    <div class="carousel-body  h-full opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Third slide</span>
        </div>
      </div>
      <!-- Slide 4 -->
      <div class="carousel-slide">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fourth slide</span>
        </div>
      </div>
      <!-- Slide 5 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fifth slide</span>
        </div>
      </div>
      <!-- Slide 6 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Sixth slide</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
{{< /code >}}

<!-- Centered -->

{{< headname level="3" >}} Centered {{< /headname >}}
Set `isCentered:true` to align the slides to the center of the carousel.

{{< code hasRTL="false" >}}

<div
  id="centered"
  data-carousel='{ "loadingClasses": "opacity-0", "isCentered": true, "slidesQty": { "xs": 1, "lg": 2 } }'
  class="relative w-full"
>
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide px-1">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide px-1">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide px-1">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Third slide</span>
        </div>
      </div>
      <!-- Slide 4 -->
      <div class="carousel-slide px-1">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fourth slide</span>
        </div>
      </div>
      <!-- Slide 5 -->
      <div class="carousel-slide px-1">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fifth slide</span>
        </div>
      </div>
      <!-- Slide 6 -->
      <div class="carousel-slide px-1">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Sixth slide</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Previous Slide -->
   <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
{{< /code >}}

<!-- Draggable Slides -->

{{< headname level="3" >}} Draggable Slides {{< /headname >}}
Set `isDraggable:true` to enable the drag feature for slides. This doesn't work if `isSnap` is enabled.

{{< code hasRTL="false" >}}

<div id="draggable" data-carousel='{ "loadingClasses": "opacity-0","dotsItemClasses": "carousel-dot carousel-active:bg-primary", "slidesQty": { "xs": 1, "lg": 3 }, "isDraggable": true }' class="relative w-full" >
  <div class="carousel h-80">
    <div class="carousel-body h-full carousel-dragging:transition-none carousel-dragging:cursor-grabbing cursor-grab opacity-0" >
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Third slide</span>
        </div>
      </div>
      <!-- Slide 4 -->
      <div class="carousel-slide">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fourth slide</span>
        </div>
      </div>
      <!-- Slide 5 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fifth slide</span>
        </div>
      </div>
      <!-- Slide 6 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Sixth slide</span>
        </div>
      </div>
    </div>
  </div>
  <div class="carousel-pagination absolute bottom-3 end-0 start-0 flex justify-center gap-3"></div>
</div>
{{< /code >}}

<!-- Snap Point Scrolling -->

{{< headname level="3" >}} Snap Point Scrolling {{< /headname >}}
Use `"isSnap": true` to allow slides to scroll and center relative to the carousel’s center. You need to add `snap-x` and `snap-mandatory` classes to `carousel` and `snap-center` classes to each `carousel-slide`.

{{< code hasRTL="false" >}}

<div id="snap" data-carousel='{ "loadingClasses": "opacity-0", "slidesQty": { "xs": 1, "lg": 3 }, "isCentered": true, "isSnap": true }' class="relative w-full" >
  <div class="carousel h-80 flex overflow-y-auto snap-x snap-mandatory overflow-x-auto">
    <div class="carousel-body h-full gap-2 opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Third slide</span>
        </div>
      </div>
      <!-- Slide 4 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fourth slide</span>
        </div>
      </div>
      <!-- Slide 5 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fifth slide</span>
        </div>
      </div>
      <!-- Slide 6 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Sixth slide</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
{{< /code >}}

<!-- Auto Height -->

{{< headname level="3" >}} Auto Height {{< /headname >}}
Set `isAutoHeight:true` to automatically adjust the carousel height with each slide change.

{{< code hasRTL="false" >}}

<div id="auto-height" data-carousel='{ "isAutoHeight": true, "loadingClasses": "opacity-0" }' class="relative w-full">
  <div class="carousel">
    <div class="carousel-body h-full relative opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide h-80 lg:h-96">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl transition duration-700">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide h-80">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl transition duration-700">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide h-80 lg:h-64">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl transition duration-700">Third slide</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
{{< /code >}}

<!-- Info -->

{{< headname level="3" >}} Info {{< /headname >}}

Include `carousel-info` within `data-carousel` and place `carousel-info-current` and `carousel-info-total` inside `carousel-info` to show the current slide number and the total number of slides.

{{< code hasRTL="false" >}}

<div id="info" data-carousel='{ "loadingClasses": "opacity-0", "isInfiniteLoop": true, "slidesQty": 1 }' class="relative w-full">
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Third slide</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
  <div
    class="carousel-info absolute bottom-3 start-[50%] inline-flex -translate-x-[50%] justify-center rounded-lg bg-base-100 px-4"
  >
    <span class="carousel-info-current me-1">0</span>
    /
    <span class="carousel-info-total ms-1">0</span>
  </div>
</div>
{{< /code >}}

<!-- Destroy/Reinitialize -->
{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}
The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a carousel.

{{< code addClass="!block" jsCode="true" >}}

<div
  id="carousel-to-destroy"
  data-carousel='{ "loadingClasses": "opacity-0", "dotsItemClasses": "carousel-dot carousel-active:bg-primary", "slidesQty": { "xs": 1, "lg": 3 }, "isCentered": true, "isSnap": true }'
  class="relative w-full"
>
  <div class="carousel overflow-y-auto flex h-80 snap-x snap-mandatory overflow-x-auto">
    <div class="carousel-body h-full gap-2 opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Third slide</span>
        </div>
      </div>
      <!-- Slide 4 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200/50 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fourth slide</span>
        </div>
      </div>
      <!-- Slide 5 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Fifth slide</span>
        </div>
      </div>
      <!-- Slide 6 -->
      <div class="carousel-slide snap-center">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-lg">Sixth slide</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>

  <div class="carousel-pagination absolute bottom-8 end-0 start-0 flex justify-center gap-3"></div>
</div>

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>


<!-- Js -->
<script>
  window.addEventListener('load', () => {
    // Destroy and reinit variables
    const carousel = document.querySelector('#carousel-to-destroy')
    const destroyBtn = document.querySelector('#destroy-btn')
    const reinitBtn = document.querySelector('#reinit-btn')

    // Destroy usage
    destroyBtn.addEventListener('click', () => {
      const { element } = HSCarousel.getInstance(carousel, true)

      element.destroy()

      destroyBtn.setAttribute('disabled', 'disabled')
      reinitBtn.removeAttribute('disabled')
    })

    // Reinit usage
    reinitBtn.addEventListener('click', () => {
      HSCarousel.autoInit()

      reinitBtn.setAttribute('disabled', 'disabled')
      destroyBtn.removeAttribute('disabled')
    })
  })
</script>
{{< /code >}}

<!-------------------- Options usage -------------------->

{{< headname level="2" >}} Options usage {{< /headname >}}

<!-- Current index -->

{{< headname level="3" >}} Current index {{< /headname >}}

Assign the value of the `data-carousel` attribute as an object. Within this object, set the `currentIndex` option to `index-number` for default active slide based on its index. By default, its value is `0`.

{{< code hasRTL="false" >}}

<div id="current-index" data-carousel='{ "loadingClasses": "opacity-0", "currentIndex": 1 }' class="relative w-full">
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="bg-base-200/60 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="bg-base-200/80 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Third slide</span>
        </div>
      </div>
    </div>
  </div>
  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
{{< /code >}}

<!-- IsAutoPlay & speed -->

{{< headname level="3" >}} IsAutoPlay & speed {{< /headname >}}

Set the `data-carousel` attribute's value as an object. Inside this object, configure the `isAutoPlay` option to `true` to enable auto-play in the carousel. By default, its value is `false`.

In addition to `isAutoPlay`, set the `speed` option to `number` within the configuration to determine the auto-play speed. The default value for this option is `4000`.

{{< code hasRTL="false" >}}

<div id="auto-play" data-carousel='{ "loadingClasses": "opacity-0", "isAutoPlay": true, "speed": 1000 }' class="relative w-full" >
  <div class="carousel h-80">
    <div class="carousel-body opacity-0 h-full">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="bg-base-200/60 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="bg-base-200/80 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Third slide</span>
        </div>
      </div>
    </div>
  </div>
  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
{{< /code >}}

<!-- isInfiniteLoop -->

{{< headname level="3" >}} IsInfiniteLoop {{< /headname >}}

Within the `data-carousel` attribute's value, create an object. Inside this object, set the `isInfiniteLoop` option to `true` to deactivate the infinite looping of slides in the carousel. The default value for this option is `false`.

{{< code hasRTL="false" >}}

<div id="infinite-loop" data-carousel='{ "loadingClasses": "opacity-0", "isInfiniteLoop": true }' class="relative w-full">
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="bg-base-200/60 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="bg-base-200/80 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Third slide</span>
        </div>
      </div>
    </div>
  </div>
  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
{{< /code >}}

<!-- isRTL -->

{{< headname level="3" >}} isRTL {{< /headname >}}

The following example demonstrates how to enable RTL mode in a carousel by setting `"isRTL": true`.

{{< code hasRTL="false" >}}

<!-- Slider -->
<div
  data-carousel='{
    "loadingClasses": "opacity-0",
    "dotsItemClasses": "carousel-box carousel-active:bg-primary",
    "isRTL": true
  }' class="relative w-full" dir="rtl">
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <div class="carousel-slide">
        <div class="bg-base-200/60 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">First slide</span>
        </div>
      </div>
      <div class="carousel-slide">
        <div class="bg-base-200/80 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Second slide</span>
        </div>
      </div>
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Third slide</span>
        </div>
      </div>
    </div>
  </div>

  <button type="button" class="carousel-prev start-5 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer rtl:rotate-180"></span>
    <span class="sr-only">Previous</span>
  </button>
   <button type="button" class="carousel-next end-5 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5 rtl:rotate-180"></span>
    <span class="sr-only">Next</span>
  </button>

  <div class="carousel-pagination absolute bottom-3 end-0 start-0 flex justify-center gap-3"></div>
</div>
<!-- End Slider -->
{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!--  Options  -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/carousel.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

{{< table >}}

PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
`data-carousel` | Activates a carousel by specifying on an element. | `—` | `—`
`:currentIndex` | Specifies the index of the current slide initially (from 0 to slides quantity). | number |`0`
`:loadingClasses` | Specifies which classes should be removed after the carousel is loaded. CSS classes should be separated with space. | string | `opacity-0`
`:dotsItemClasses` | Defines the classes to be added to the automatically generated point elements. Separate each CSS class with a space. | string| `—`
`:isAutoHeight` | Sets the height of the carousel to the height of the current slide. | boolean | `false`
`:isAutoPlay` | Enables autoplay. | boolean | `false`
`:speed`| Autoplay animation speed. Available if `isAutoplay: true`. | number | `4000`
`:updateDelay`| Allows you to delay the update function while resizing a window, making it well-suited for image sliders to achieve more accurate image size calculations. | number | `0`
`:isInfiniteLoop` | Enables infinite loop. | boolean | `false`
`:isCentered` | Enables centered mode, which adds space on the sides to keep slides centered. | boolean | `false`
`:isSnap` | Activates a mode that lets you scroll the slider's content along the x-axis, keeping the active slide centered within the slider. | boolean | `false`
`:isDraggable` | Allows slide navigation via dragging by adding the `carousel-dragging:transition-none` class to the `carousel-body`. This feature is not compatible with the `isSnap: true` setting. | boolean | `false`
`:isRTL` | Turns on RTL mode. | boolean | `false`
`:hasSnapSpacers` | Adds extra elements to achieve a steady, centered alignment effect. | boolean | `true`
`:slidesQty` | Enables setting the number of slides to display based on screen resolution when the parameter is provided as an object. If a number is provided instead, that number of slides will display across all screen resolutions. | object {'xs' 'sm' 'md' 'lg' 'xl' '2xl', number: number}, number | `1`
{{< /table >}}

<!--  Methods  -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSCarousel` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`goToPrev()` | Go to the previous slide.
`goToNext()`| Go to the next slide.
`goTo(index)` | Go to the slide by index. Starts from 0.
`recalculateWidth()` | Recalculate the width of the carousel.
`destroy()` | Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSCarousel.getInstance(target)`|<div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector)</li><ul></div>
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

Below, we demonstrate how to use the methods. Apply the ID to the `carousel` container. To test the other method, copy the provided code into your console and click the button.

{{< code jsCode="true" hasRTL="false" >}}

<div data-carousel='{ "loadingClasses": "opacity-0" }' class="relative w-full" id="carouselTarget">
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <!-- Slide 1 -->
      <div class="carousel-slide">
        <div class="bg-base-200/60 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">First slide</span>
        </div>
      </div>
      <!-- Slide 2 -->
      <div class="carousel-slide">
        <div class="bg-base-200/80 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Second slide</span>
        </div>
      </div>
      <!-- Slide 3 -->
      <div class="carousel-slide">
        <div class="bg-base-200 flex h-full justify-center p-6">
          <span class="self-center text-2xl sm:text-4xl">Third slide</span>
        </div>
      </div>
    </div>
  </div>
  <!-- Previous Slide -->
  <button type="button" class="carousel-prev start-5 max-sm:start-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-left] size-5 cursor-pointer"></span>
    <span class="sr-only">Previous</span>
  </button>
  <!-- Next Slide -->
   <button type="button" class="carousel-next end-5 max-sm:end-3 carousel-disabled:opacity-50 size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
    <span class="icon-[tabler--chevron-right] size-5"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
<div>
  <button id="go-to-2-slide" class="btn btn-primary">Go to slide 2</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const goTo2Btn = document.querySelector('#go-to-2-slide')

    goTo2Btn.addEventListener('click', () => {
      const carousel = new HSCarousel(document.querySelector('#carouselTarget'))
      carousel.goTo(1)
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">Go to certain slide by button click example (public method).</p>

{{< code-highlight lang="js" >}}// This method is used in above example.
const goTo2Btn = document.querySelector('#go-to-2-slide');

goTo2Btn.addEventListener('click', () => {
  const carousel = new HSCarousel(document.querySelector('#carouselTarget'));
  carousel.goTo(1);
});
{{< /code-highlight >}}

<p class="mt-10 mb-1.5 not-prose">Go to certain slide by button click example (mixed method).</p>

{{< code-highlight lang="js" >}}const carousel = HSCarousel.getInstance('#carouselTarget');
const goTo2Btn = document.querySelector('#go-to-2-slide');

goTo2Btn.addEventListener('click', () => {
  carousel.goTo(1);
});
{{< /code-highlight >}}

<p id="destroy-method" class="mt-10 mb-1.5 not-prose">Destroy instance.</p>

{{< code-highlight lang="js" >}}
const { element } = HSCarousel.getInstance('#carousel-to-destroy', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}
