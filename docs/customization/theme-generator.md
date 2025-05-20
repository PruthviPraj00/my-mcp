---
title: "Theme Generator"
description: "Design and personalize your own unique theme with ease and make it truly yours. Tailor every detail to reflect your style and preferences!"
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
hide_toc: true
tag: WIP
tag_bg: warning
menu:
  main:
    parent: "customization"
    weight: 8

previous: RTL
previousLink: customization/rtl/

next: Blockquote
nextLink: content/blockquote/

# pageJS:
#   - "/js/pages/theme-generator.js"

vendorJS:
  - "https://cdn.jsdelivr.net/npm/culori@2.0.1"
---

{{< callout "warning" >}}
<span class="font-semibold">Note:</span> The FlyonUI Theme Generator is currently under development.  

<br />
<br />

In the meantime, you can create and customize themes using the <a href="https://daisyui.com/theme-generator/" class="link link-warning font-semibold" target="_blank">daisyUI Theme Generator</a>. It is fully compatible with FlyonUI and integrates seamlessly for a smooth development experience.

<br />

To use a custom theme, simply copy the CSS file from daisyUI and follow the {{< link link="customization/themes/#how-to-add-a-new-custom-theme" addClass="link link-warning font-semibold" >}}Theme Documentation{{< /link >}}. Please ensure that you rename the theme while copying.
{{< /callout >}}

<!-------------------- FlyonUI Themes -------------------->
<!-- 
{{< headsingle addClass="!mt-px" level="2" >}}FlyonUI Theme Generator{{< /headsingle >}}

You can add custom themes to the `tailwind.config.js` file within the `flyonui > themes` array. This page allows you to select desired color values and preview how components will appear with your chosen palette.

Additionally, you can define optional colors to gain finer control over specific elements, such as button focus states or button text colors.

Visit the {{< link link="customization/colors/" addClass="link link-primary font-medium" >}}Colors{{< /link >}} page for a complete list of available color names.

For a detailed guide on customizing design elements like border-radius or animations, check out the {{< link link="customization/themes/" addClass="link link-primary font-medium" >}}Themes{{< /link >}} page.

<div class="flex flex-col gap-4 xl:flex-row">
  <div class="shrink-0">
    <div class="mb-3 flex flex-wrap justify-between gap-2">
      <div class="text-base-content text-xl font-semibold">tailwind.config.js</div>
      <div class="flex gap-2">
        <div class="tooltip">
          <button class="btn btn-circle btn-sm btn-soft" id="toggle-optional-color-icon" aria-label="Circle Outline Icon Button" >
            <span class="icon-[tabler--switch-vertical] size-5"></span>
          </button>
          <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
            <span class="tooltip-body">Toggle Optional Colors</span>
          </span>
        </div>
        <div class="tooltip">
          <button class="btn btn-circle btn-sm btn-soft" id="contrast-icon" aria-label="Circle Outline Icon Button">
            <span class="icon-[tabler--contrast-filled] size-5"></span>
          </button>
          <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
            <span class="tooltip-body">Fixed Contrast</span>
          </span>
        </div>
        <div class="tooltip">
          <button class="btn btn-circle btn-sm btn-soft" id="reset-icon" aria-label="Circle Outline Icon Button">
            <span class="icon-[tabler--reload] size-5"></span>
          </button>
          <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
            <span class="tooltip-body">Reset</span>
          </span>
        </div>
        <div class="tooltip">
          <button class="btn btn-circle btn-sm btn-soft" id="random-icon" aria-label="Circle Outline Icon Button">
            <span class="icon-[tabler--dice-6] size-5"></span>
          </button>
          <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
            <span class="tooltip-body">Randomize</span>
          </span>
        </div>
        <div class="tooltip">
          <button class="btn btn-circle btn-sm btn-soft" id="copy-theme">
            <span class="icon-[tabler--clipboard] size-5"></span>
          </button>
          <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
            <span class="tooltip-body">Copy Theme</span>
          </span>
        </div>
      </div>
    </div>
    <pre class="text-sm bg-base-content/90 mt-0"><code class="text-neutral-content/30">module.exports = {</code>
<code>flyonui: {
  themes: [
    {
      mytheme: {</code><div class="ms-4 flex gap-1"><span class="badge mt-1 badge-warning badge-xs select-none">Pick</span>
        <div id="color-picker-container"></div>
      </div>      },
    },
  ],
},
<code class="text-neutral-content/30">plugins: [
  require('flyonui'),
],
//...
}</code></pre>
  </div>

  <div>
    <div class="text-base-content mb-3 text-xl font-semibold">Preview</div>
    <div class="preview-box rounded-box bg-base-100 border p-6">
      <div class="grid grid-cols-2 gap-2 md:grid-cols-4">
          <button class="btn">Default</button>
          <button class="btn btn-primary">Primary</button>
          <button class="btn btn-secondary">Secondary</button>
          <button class="btn btn-accent">Accent</button>
          <button class="btn btn-info">Info</button>
          <button class="btn btn-success">Success</button>
          <button class="btn btn-warning">Warning</button>
          <button class="btn btn-error">Error</button>
        </div>

        <div class="grid grid-cols-3 place-items-center gap-2 sm:grid-cols-5 my-4">
          <span class="badge">Default</span>
          <span class="badge badge-neutral">Neutral</span>
          <span class="badge badge-primary">Primary</span>
          <span class="badge badge-secondary">Secondary</span>
          <span class="badge badge-accent">Accent</span>
          <span class="badge badge-info">Info</span>
          <span class="badge badge-success">Success</span>
          <span class="badge badge-warning">Warning</span>
          <span class="badge badge-error">Error</span>
        </div>

      <div class="flex flex-col gap-4 my-4">
          <div class="flex flex-col gap-3 md:flex-row">
            <div class="md:w-1/2">

              <div class="inline-flex flex-col mb-3">
                <span class="link link-animated">I'm a simple link</span>
                <span class="link link-primary link-animated">I'm a simple link</span>
                <span class="link link-secondary link-animated">I'm a simple link</span>
                <span class="link link-accent link-animated">I'm a simple link</span>
              </div>
              <div class="space-x-2">
                <span class="loading loading-spinner text-primary"></span>
                <span class="loading loading-spinner text-secondary"></span>
                <span class="loading loading-spinner text-info"></span>
                <span class="loading loading-spinner text-warning"></span>
                <span class="loading loading-spinner text-error"></span>
              </div>
            </div>
            <div class="flex flex-col gap-3 md:w-1/2">
              <div class="progress w-56" role="progressbar" aria-label="Primary Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
                <div class="progress-bar progress-primary progress-striped w-3/4"></div>
              </div>
              <div class="progress w-56" role="progressbar" aria-label="Secondary Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
                <div class="progress-bar progress-secondary progress-striped w-3/4"></div>
              </div>
              <div class="progress w-56" role="progressbar" aria-label="Accent Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
                <div class="progress-bar progress-accent progress-striped w-3/4"></div>
              </div>
              <div class="progress w-56" role="progressbar" aria-label="Info Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
                <div class="progress-bar progress-info progress-striped w-3/4"></div>
              </div>
              <div class="progress w-56" role="progressbar" aria-label="Success Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
                <div class="progress-bar progress-success progress-striped w-3/4"></div>
              </div>
              <div class="progress w-56" role="progressbar" aria-label="Warning Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
                <div class="progress-bar progress-warning progress-striped w-3/4"></div>
              </div>
              <div class="progress w-56" role="progressbar" aria-label="Error Progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
                <div class="progress-bar progress-error progress-striped w-3/4"></div>
              </div>
            </div>
          </div>
          <div class="flex gap-3 max-md:flex-col md:items-center">

            <div class="flex gap-3 md:w-1/2">
              <div class="tooltip [--placement:left]">
                <button type="button" class="tooltip-toggle btn btn-square" aria-label="Tooltip">
                  <span class="icon-[tabler--chevron-left]"></span>
                </button>
                <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
                  <span class="tooltip-body">Tooltip on left</span>
                </span>
              </div>
              <div class="tooltip">
                <button type="button" class="tooltip-toggle btn btn-square" aria-label="Tooltip">
                  <span class="icon-[tabler--chevron-up]"></span>
                </button>
                <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
                  <span class="tooltip-body">Tooltip on top</span>
                </span>
              </div>
              <div class="tooltip [--placement:bottom]">
                <button type="button" class="tooltip-toggle btn btn-square" aria-label="Tooltip">
                  <span class="icon-[tabler--chevron-down]"></span>
                </button>
                <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
                  <span class="tooltip-body">Tooltip on bottom</span>
                </span>
              </div>
              <div class="tooltip [--placement:right]">
                <button type="button" class="tooltip-toggle btn btn-square" aria-label="Tooltip">
                  <span class="icon-[tabler--chevron-right]"></span>
                </button>
                <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
                  <span class="tooltip-body">Tooltip on right</span>
                </span>
              </div>
            </div>

            <div class="flex flex-wrap items-center gap-3 md:w-1/2">
                <div class="radial-progress" style="--value:60;--size:3.5rem">60%</div>
                <div class="radial-progress text-warning" style="--value:75;--size:3.5rem">75%</div>
                <div class="radial-progress text-info" style="--value:90;--size:3.5rem">90%</div>
            </div>
          </div>
        </div>
      <div class="flex flex-col gap-4">
          <div class="flex flex-col gap-3 md:flex-row">
            <div class="md:w-1/2">

              <div>
                <input type="checkbox" class="switch" checked="checked" />
                <input type="checkbox" class="switch switch-primary" checked="checked" />
                <input type="checkbox" class="switch switch-secondary" checked="checked" />
                <input type="checkbox" class="switch switch-accent" checked="checked" />
              </div>

              <div>
                <input type="checkbox" class="checkbox" checked="checked" />
                <input type="checkbox" class="checkbox checkbox-primary" checked="checked" />
                <input type="checkbox" class="checkbox checkbox-secondary" checked="checked" />
                <input type="checkbox" class="checkbox checkbox-accent" checked="checked" />
              </div>

              <div>
                <input type="radio" name="radio-1" class="radio" checked="checked" />
                <input type="radio" name="radio-1" class="radio radio-primary" />
                <input type="radio" name="radio-1" class="radio radio-secondary" />
                <input type="radio" name="radio-1" class="radio radio-accent" />
              </div>
            </div>

            <div class="md:w-1/2">
              <input type="range" min="0" max="100" value="70" class="range range-sm" />
              <input type="range" min="0" max="100" value="60" class="range range-sm range-primary" />
              <input type="range" min="0" max="100" value="50" class="range range-sm range-secondary" />
              <input type="range" min="0" max="100" value="40" class="range range-sm range-accent" />
            </div>
          </div>

          <div class="bg-base-200 p-4 rounded-lg">
            <div class="chat chat-receiver">
              <div class="chat-avatar avatar not-prose">
                <div class="size-10 rounded-full">
                  <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
                </div>
              </div>
              <div class="chat-bubble">I finally finished the marathon!</div>
            </div>
            <div class="chat chat-sender">
              <div class="chat-avatar avatar not-prose">
                <div class="size-10 rounded-full">
                  <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="avatar" />
                </div>
              </div>
              <div class="chat-bubble">Wow, that's incredible! I'm so proud of you!</div>
            </div>
          </div>
        </div>
        <div class="space-y-3 mt-4">
          <div class="alert alert-primary" role="alert">Welcome to our platform! Explore our latest features and updates.</div>
          <div class="alert alert-info" role="alert">Stay tuned for our upcoming events and announcements.</div>
          <div class="alert alert-success" role="alert">Your transaction was successful. Thank you for choosing our service!</div>
          <div class="alert alert-warning" role="alert">
            Attention! Your account security may be at risk. Enable two-factor authentication now.
          </div>
          <div class="alert alert-error" role="alert">Oops! It seems there was an unexpected error. Please try again later.</div>
        </div>
    </div>
  </div>
</div> -->
