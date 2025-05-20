---
title: "Animation"
description: "Enhance your projects effortlessly with Tailwindcss Motion, a powerful Tailwind CSS plugin offering a range of pre-designed motion classes for seamless animation integration."
bg_image: "svg/third-party-plugins/animation.svg"
components: 6
menu:
  main:
    parent: "third party plugins"

previous: Advance Range slider
previousLink: third-party-plugins/advance-range-slider/

next: Apex Charts
nextLink: third-party-plugins/apex-charts/

pageJS:
  - "/js/pages/animation.js"
  
vendorJS: 
  - "https://unpkg.com/tailwindcss-intersect@2.x.x/dist/observer.min.js"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Easily unlock a range of pre-built animation classes by integrating <a href="https://rombo.co/tailwind/" target="_blank" class="link link-primary font-semibold">tailwindcss-motion</a> with FlyonUI. To enable scroll-based functionality in FlyonUI, simply integrate <a href="https://github.com/heidkaemper/tailwindcss-intersect" target="_blank" class="link link-primary font-semibold">tailwindcss-intersect</a>. Just follow these simple steps to get started:

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical w-full mb-12 ps-0">
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        1
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold"><code>tailwindcss-motion</code> Installation</div>
      <p>Install <code>tailwindcss-motion</code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm install tailwindcss-motion{{< /code-highlight >}}
    </div>
    <hr class="rounded-none border-transparent !w-0.5" />
  </li>

  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        2
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold"><code>tailwindcss-intersect</code> Installation</div>
      <p>Please refer to the <a href="https://github.com/heidkaemper/tailwindcss-intersect?tab=readme-ov-file#installation" target="_blank" class="link link-primary font-semibold">official installation documentation</a> for more details:</p>
      <p>Install <code>tailwindcss-intersect</code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm install tailwindcss-intersect{{< /code-highlight >}}
    </div>
    <hr class="rounded-none border-transparent !w-0.5" />
  </li>

  <!-- Include Third-Party JS and CSS -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        3
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Configure Tailwind</div>
      <p>
         Update your <code>tailwind.css</code> file to include the plugin:
      </p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="css" >}}
// tailwind.css
@import "tailwindcss";
@import "tailwindcss-intersect";
@plugin "tailwindcss-motion";
{{</code-highlight >}}
</div>
<hr class="rounded-none border-transparent !w-0.5" />
</li>
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        4
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Setting up <code>taillwindcss-intersect</code> observer</div>
      <p class="text-base-content">
         Via CDN:
      </p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<script defer src="https://unpkg.com/tailwindcss-intersect@2.x.x/dist/observer.min.js"></script>
{{</code-highlight >}}
      <p class="text-base-content !mt-4">
         Via NPM:
      </p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="js" >}}
import { Observer } from 'tailwindcss-intersect';
 
Observer.start();
{{</code-highlight >}}
</div>
</li>
</ul>

<!-- Basic Example -->

{{< headname level="2" >}} Basic Example {{< /headname >}}

Below is a basic implementation showcasing various motion presets provided by `tailwindcss-motion`.

{{< code addClass="h-96" hasRTL="false" jsCode="true" >}}

<div class="flex w-full items-center justify-around max-sm:flex-col-reverse sm:gap-8">
  <ul class="divide-base-content/25 bg-base-100 shadow-base-300/20 h-80 w-64 divide-y overflow-y-auto rounded-xs shadow-xs **:rounded-none max-sm:h-48" >
    <li><button class="dropdown-item animation-button" value="motion-preset-fade">Fade</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-slide-right">Slide</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-focus">Focus</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-blur-right">Blur</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-expand">Expand</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-shrink">Shrink</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-pop">Pop</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-shake">Shake</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-bounce">Bounce</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-compress">Compress</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-pulse">Pulse</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-wobble">Wobble</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-seesaw">Seesaw</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-oscillate">Oscillate</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-stretch">Stretch</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-float">Float</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-spin">Spin</button></li>
    <li><button class="dropdown-item animation-button" value="motion-preset-blink">Blink</button></li>
    <li>
      <a class="dropdown-item link link-hover link-primary group justify-between" href="https://rombo.co/tailwind/" target="_blank" >
        More Animations
        <span class="icon-[tabler--chevron-right] -mb-0.5 size-4 group-hover:translate-x-1 rtl:rotate-180"></span>
      </a>
    </li>
  </ul>

  <div id="animated-box" class="mx-auto self-center">
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
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const animationButtons = document.querySelectorAll('.animation-button')
    const box = document.getElementById('animated-box')

    animationButtons.forEach(button => {
      button.addEventListener('click', () => {
        const animationClass = button.value

        // Remove all existing motion- classes
        const currentClasses = Array.from(box.classList)
        const motionClasses = currentClasses.filter(className => className.startsWith('motion-'))
        motionClasses.forEach(className => box.classList.remove(className))

        // Temporarily remove the animation class to re-trigger it
        void box.offsetWidth // Trigger reflow to allow re-adding the class
        box.classList.add(animationClass, 'motion-duration-1000')
      })
    })
  })
</script>

{{< /code >}}

{{< callout "info" >}}
To create your own custom animation, you can {{< link link="https://rombo.co/tailwind/" addClass="link link-primary" >}}refer{{< /link >}}
{{< /callout >}}

<!-- Illustration -->

{{< headname level="2" >}} Illustration {{< /headname >}}

<!-- Animated avatar group -->

{{< headname level="3" >}} Animated avatar group{{< /headname >}}

Demonstrates animated avatar groups using the `tailwindcss-motion` plugin.

{{< code >}}

<div class="avatar-group -space-x-5">
  <div class="avatar hover:motion-scale-out-110 motion-ease-spring-smooth hover:z-30">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar hover:motion-scale-out-110 motion-ease-spring-smooth hover:z-30">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-12.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar hover:motion-scale-out-110 motion-ease-spring-smooth hover:z-30">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-10.png" alt="avatar" />
    </div>
  </div>
  <div class="avatar hover:motion-scale-out-110 motion-ease-spring-smooth hover:z-30">
    <div class="w-13">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-6.png" alt="avatar" />
    </div>
  </div>
</div>
{{< /code >}}

<!-- Animated Button -->

{{< headname level="3" >}} Animated button {{< /headname >}}

Here are example of interactive button with unique motion effect designed with the `tailwindcss-motion` plugin.

{{< code addClass="flex items-center h-32" >}}
<button class="btn btn-square btn-text btn-error *:active:motion-preset-shake" aria-label="Soft Icon Button">
  <span class="icon-[tabler--bell-ringing] motion-duration-500 size-6"></span>
</button>

{{< /code >}}

<!-- Animated card -->

{{< headname level="3" >}} Animated Card {{< /headname >}}

This example demonstrates using `tailwindcss-motion` and `tailwindcss-intersect` plugins to create scroll-based animated cards.

{{< code addClass="h-max" hasRTL="false" >}}

<div class="card intersect:motion-scale-in-0 intersect:motion-opacity-in-0 intersect:motion-blur-in-[5px] intersect:motion-ease-spring-smooth intersect-half origin-bottom-right sm:max-w-sm" >
  <figure><img src="https://cdn.flyonui.com/fy-assets/components/card/image-7.png" alt="headphone" /></figure>
  <div class="card-body">
    <h5 class="card-title mb-2.5">Airpods Max</h5>
    <p class="mb-4">A perfect balance of exhilarating high-fidelity audio and the effortless magic of Airpods.</p>
    <div class="card-actions">
      <button class="btn btn-primary intersect:motion-delay-[400ms] intersect:motion-ease-spring-bouncy intersect:motion-scale-in-0" >
        Buy Now
      </button>
      <button class="btn btn-secondary btn-soft intersect:motion-delay-[500ms] intersect:motion-ease-spring-bouncy intersect:motion-scale-in-0" >
        Add to cart
      </button>
    </div>
  </div>
</div>

{{< /code >}}

<!-- Animated List -->

{{< headname level="3" >}} Animated List {{< /headname >}}

This example demonstrates leveraging `tailwindcss-motion` and `tailwindcss-intersect` plugins to create a seamlessly scroll-animated list.

{{< code addClass="h-96 flex-col gap-6" hasRTL="false" >}}
<ul class="flex w-96 flex-col gap-2 rounded-md *:rounded-md *:p-3 *:shadow-sm *:shadow-base-300/20" >
  <li class="bg-base-100 intersect:motion-scale-in-0 intersect:motion-opacity-in-0 origin-top">
    <div class="flex w-full items-center gap-2">
      <span class="icon-[tabler--brand-whatsapp] text-success size-6"></span>
      New Message(13)
    </div>
  </li>
  <li class="origin-to intersect:motion-delay-[500ms] bg-base-100 intersect:motion-scale-in-0 intersect:motion-opacity-in-0" >
    <div class="flex w-full items-center gap-2">
      <span class="icon-[tabler--brand-uber] text-base-content size-6"></span>
      Your ride is waiting outside
    </div>
  </li>
  <li class="origin-to intersect:motion-delay-[1000ms] bg-base-100 intersect:motion-scale-in-0 intersect:motion-opacity-in-0" >
    <div class="flex w-full items-center gap-2">
      <span class="icon-[tabler--brand-amazon] text-warning size-6"></span>
      You forget something in your cart
    </div>
  </li>
  <li class="origin-to intersect:motion-delay-[1500ms] bg-base-100 intersect:motion-scale-in-0 intersect:motion-opacity-in-0" >
    <div class="flex w-full items-center gap-2">
      <span class="icon-[tabler--brand-netflix] text-error size-6"></span>
      New series just dropped
    </div>
  </li>
</ul>

{{< /code >}}

<!-- Animate your pages seamlessly -->

{{< headname level="3" >}} Animate your pages seamlessly {{< /headname >}}

Enhance your pages with smooth scroll-based animations and dynamic transitions using the tailwindcss-motion and tailwindcss-intersect plugins.

{{< code addClass="h-max gap-8" hasRTL="false" >}}

<div class="flex flex-wrap gap-6">
  <div class="stats intersect:motion-preset-slide-left intersect:motion-ease-spring-bouncier max-sm:w-full">
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

  <div class="stats intersect:motion-preset-slide-left intersect:motion-delay-[400ms] intersect:motion-ease-spring-bouncier max-sm:w-full" >
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

  <div class="stats intersect:motion-preset-slide-left intersect:motion-delay-[800ms] intersect:motion-ease-spring-bouncier max-sm:w-full" >
    <div class="stat">
      <div class="avatar avatar-placeholder">
        <div class="bg-error/20 text-error size-10 rounded-full">
          <span class="icon-[tabler--credit-card] size-6"></span>
        </div>
      </div>
      <div class="stat-value mb-1">Invoice</div>
      <div class="stat-title">$18,200 of $25,000</div>
      <div class="progress bg-error/10 h-2" role="progressbar" aria-label="Invoice Progressbar" aria-valuenow="73" aria-valuemin="0" aria-valuemax="100" >
        <div class="progress-bar progress-error w-[73%]"></div>
      </div>
    </div>
  </div>
</div>

<div>
  <h2 class="intersect:motion-preset-blur-left intersect:motion-delay-[1000ms] mb-4 text-3xl font-bold">
    Track Your Stats
  </h2>

  <p class="intersect:motion-preset-focus intersect:motion-delay-[1400ms]">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
    aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
    sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
  </p>
</div>

{{< /code >}}
