---
title: "File Upload"
components: 4
description: "File Upload enhances web forms with a Tailwind CSS interface, offering drag-and-drop, previews, progress bars, multiple uploads, and file validation."
bg_image: "svg/third-party-plugins/file-upload.svg"
menu:
  main:
    parent: "third party plugins"

previous: Drag & drop
previousLink: third-party-plugins/drag-and-drop/

next: Flatpickr
nextLink: third-party-plugins/flatpickr/

requires_js: true

vendorJS:
  - "https://unpkg.com/dropzone@5/dist/min/dropzone.min.js"
  - "https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"

pageJS:
  - "/js/pages/dropzone.js"
---

{{< callout "warning" >}}
Note that this component requires the use of the third-party <a href="https://www.dropzone.dev/" target="_blank" class="link link-warning font-semibold">Dropzone Js</a> and <a href="https://lodash.com/" target="_blank" class="link link-warning font-semibold">Lodash</a> plugins.
{{< /callout >}}

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate <a href="https://www.dropzone.dev/" target="_blank" class="link link-primary">Dropzone JS</a> with FlyonUI.

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical mb-12 w-full ps-0">
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">
        1
      </span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Installation</div>
      <p>Install <code>Dropzone</code> and <code>lodash</code> using npm. Certain JavaScript helpers for Dropzone require the lodash plugin, so make sure to install it as well.</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm i dropzone lodash{{< /code-highlight >}}
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
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Include Dropzone and Lodash JavaScript and CSS</div>
      <p>Include the necessary CSS and JavaScript files in your project at the specified locations:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<body>
  <script src="../path/to/lodash/lodash.js"></script>
  <script src="../path/to/dropzone/dist/dropzone-min.js"></script>
</body>
{{< /code-highlight >}}
      <div class="text-base-content my-3 font-semibold">Since no custom CSS overrides are required, you can also use a CDN link.</div>
       <p>Insert the following JavaScript and CSS CDN links into their respective sections:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}
<body>
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script src="https://unpkg.com/dropzone@5/dist/min/dropzone.min.js"></script>
</body>
{{< /code-highlight >}}
    </div>
  </li>
</ul>

<!-- Class Table -->

{{< class-table >}}
file-upload-complete:{tw-utility-class} | variant | A modifier that allows you to set Tailwind classes to items that successfully uploaded.
{{< /class-table >}}

<!-------------------- DataTable Structure -------------------->

{{< headname level="2" >}} File Upload Structure {{< /headname >}}

<!-- Basic outline -->

{{< headname level="3" >}} Basic outline {{< /headname >}}

Prefer to create your own style? Here is a completely unstylized example.

{{< code-highlight addClass="h-80" lang="html" >}}

<div data-file-upload='{
  "url": "/upload"
}'>
  <template data-file-upload-preview>
    <button type="button" data-file-upload-remove>
      Delete!
    </button>
    <span data-file-upload-file-icon>
      <img class="hidden" data-dz-thumbnail />
    </span>
    <div>
      <span data-file-upload-file-name></span>.<span data-file-upload-file-ext></span>
    </div>
    <div data-file-upload-file-size></div>
    <div role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" data-file-upload-progress-bar>
      <div style="width: 0" data-file-upload-progress-bar-pane></div>
    </div>
    <span data-file-upload-progress-bar-value>0</span>%
  </template>
  <div class="cursor-pointer" data-file-upload-trigger>
    Drop your file here or browse
  </div>
  <div data-file-upload-previews></div>
</div>
{{< /code-highlight >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Using the most basic file upload markup, here's how file upload look.

Use `<template>` to style your file upload output. The following example demonstrates the default template layout.

{{< code addClass="!block" >}}

<div
  data-file-upload='{
    "url": "/upload",
    "extensions": {
      "csv": {
        "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M4 22h14a2 2 0 0 0 2-2V7l-5-5H6a2 2 0 0 0-2 2v4\"/><path d=\"M14 2v4a2 2 0 0 0 2 2h4\"/><path d=\"m5 12-3 3 3 3\"/><path d=\"m9 18 3-3-3-3\"/></svg>",
        "class": "shrink-0 size-5"
      }
    }
  }' >

  <div class="bg-base-200/60 rounded-box flex flex-col justify-center border-2 border-base-content/20 border-dashed"  >
    <div class="text-center cursor-pointer p-12" data-file-upload-trigger="">
      <p class="text-base-content/50 mb-3 text-sm">Choose a file with a size up to 2MB.</p>
      <button class="btn btn-soft btn-sm btn-primary text-nowrap"> <span class="icon-[tabler--file-upload] size-4.5 shrink-0"></span> Drag & Drop to Upload </button>
      <p class="text-base-content/50 my-2 text-xs">or</p>
      <p class="link link-animated link-primary font-medium text-sm">Browse</p>
    </div>
    <div class="mx-12 mb-8 space-y-2 empty:m-0" data-file-upload-previews=""></div>
  </div>
</div>
{{< /code >}}

<!-- Error state -->

{{< headname level="3" >}} Error state {{< /headname >}}

The system will throw an error if the file size exceeds 1 MB.

{{< code addClass="!block" jsCode="true" >}}

<div
  id="file-upload-limit"
  data-file-upload='{
  "url": "/upload",
  "maxFilesize": 1,
  "extensions": {
    "csv": {
      "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M4 22h14a2 2 0 0 0 2-2V7l-5-5H6a2 2 0 0 0-2 2v4\"/><path d=\"M14 2v4a2 2 0 0 0 2 2h4\"/><path d=\"m5 12-3 3 3 3\"/><path d=\"m9 18 3-3-3-3\"/></svg>",
      "class": "shrink-0 size-5"
    }
  }
}' >
  <template data-file-upload-preview="">
    <div class="rounded-box bg-base-100 shadow-base-300/20 p-3 shadow-lg">
      <div class="mb-1 flex items-center justify-between">
        <div class="flex items-center gap-x-3">
          <span class="text-base-content/80 border-base-content/20 flex size-8 items-center justify-center rounded-lg border p-0.5" data-file-upload-file-icon="" >
            <img class="hidden rounded-md" data-dz-thumbnail="" />
          </span>
          <div>
            <p class="text-base-content text-sm font-medium">
              <span class="inline-block truncate align-bottom" data-file-upload-file-name=""></span>
              .
              <span data-file-upload-file-ext=""></span>
            </p>
            <p class="text-base-content/50 text-xs" data-file-upload-file-size="" data-file-upload-file-success=""></p>
            <p class="text-error text-xs" style="display: none" data-file-upload-file-error="">
              File exceeds size limit.
            </p>
          </div>
        </div>
        <div class="flex items-center">
          <div class="tooltip [--placement:top]" style="display: none" data-file-upload-file-error="">
            <button type="button" class="tooltip-toggle btn btn-sm btn-circle btn-text btn-error">
              <span class="icon-[tabler--alert-circle] size-4 shrink-0"></span>
            </button>
            <span class="tooltip-content tooltip-shown:opacity-100 tooltip-shown:visible" role="tooltip">
              <span class="tooltip-body">Please try to upload a file smaller than 1MB.</span>
            </span>
          </div>
          <button type="button" class="btn btn-sm btn-circle btn-text" data-file-upload-reload="">
            <span class="icon-[tabler--refresh] size-4 shrink-0"></span>
          </button>
          <button type="button" class="btn btn-sm btn-circle btn-text" data-file-upload-remove="">
            <span class="icon-[tabler--trash] size-4 shrink-0"></span>
          </button>
        </div>
      </div>
      <div class="flex items-center gap-x-3 whitespace-nowrap">
        <div class="progress h-2" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" data-file-upload-progress-bar="" >
          <div class="progress-bar progress-primary file-upload-complete:progress-success transition-all duration-500" style="width: 0" data-file-upload-progress-bar-pane="" ></div>
        </div>
        <span class="text-base-content mb-0.5 text-sm">
          <span data-file-upload-progress-bar-value="">0</span>%
        </span>
      </div>
    </div>
  </template>

  <div class="bg-base-200/60 rounded-box flex flex-col justify-center border-2 border-base-content/20 border-dashed"  >
    <div class="text-center cursor-pointer p-12" data-file-upload-trigger="">
      <p class="text-base-content/50 mb-3 text-sm">Choose a file no larger than 1MB.</p>
      <button class="btn btn-soft btn-sm btn-primary text-nowrap"> <span class="icon-[tabler--file-upload] size-4.5 shrink-0"></span> Drag & Drop to Upload </button>
      <p class="text-base-content/50 my-2 text-xs">or</p>
      <p class="link link-animated link-primary font-medium text-sm">Browse</p>
    </div>
    <div class="mx-12 mb-8 space-y-2 empty:m-0" data-file-upload-previews=""></div>
  </div>
</div>

<!-- Js -->

<script>
  ;(function () {
    const { element } = HSFileUpload.getInstance('#file-upload-limit', true)

    element.dropzone.on('error', (file, response) => {
      if (file.size > element.concatOptions.maxFilesize * 1024 * 1024) {
        const filePreview = file.previewElement

        const successEls = filePreview.querySelectorAll('[data-file-upload-file-success]')
        const errorEls = filePreview.querySelectorAll('[data-file-upload-file-error]')
        if (successEls) successEls.forEach(el => (el.style.display = 'none'))
        errorEls.forEach(el => (el.style.display = ''))
        HSStaticMethods.autoInit(['tooltip'])
      }
    })
  })()
</script>

{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Gallery -->

{{< headname level="3" >}} Gallery {{< /headname >}}

Using file upload as a gallery.

{{< code addClass="!block" >}}

<div
  data-file-upload='{
  "url": "/upload",
  "acceptedFiles": "image/*",
  "autoHideTrigger": false,
  "extensions": {
    "csv": {
      "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M4 22h14a2 2 0 0 0 2-2V7l-5-5H6a2 2 0 0 0-2 2v4\"/><path d=\"M14 2v4a2 2 0 0 0 2 2h4\"/><path d=\"m5 12-3 3 3 3\"/><path d=\"m9 18 3-3-3-3\"/></svg>",
      "class": "shrink-0 size-5"
    }
  }
}' >
  <template data-file-upload-preview="">
    <div class="rounded-box bg-base-100 shadow-base-300/20 relative mt-2 p-2 shadow-lg">
      <img class="mb-2 w-full rounded-lg object-cover" data-dz-thumbnail="" />
      <div class="mb-1 flex items-center justify-between gap-x-3 whitespace-nowrap">
        <div class="w-10">
          <span class="text-base-content mb-0.5 text-sm">
            <span data-file-upload-progress-bar-value="">0</span>%</span>
        </div>
        <div class="flex items-center gap-x-2">
          <button type="button" class="btn btn-sm btn-circle btn-text" data-file-upload-remove="">
            <span class="icon-[tabler--trash] size-4 shrink-0"></span>
          </button>
        </div>
      </div>
      <div class="progress h-2" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" data-file-upload-progress-bar="" >
        <div class="progress-bar progress-primary file-upload-complete:progress-success transition-all duration-500" style="width: 0" data-file-upload-progress-bar-pane="" ></div>
      </div>
    </div>
  </template>

  <div class="bg-base-200/60 rounded-box flex flex-col justify-center border-2 border-base-content/20 border-dashed"  >
    <div class="text-center cursor-pointer p-12" data-file-upload-trigger="">
      <p class="text-base-content/50 mb-3 text-sm">Choose a file with a size up to 2MB.</p>
      <button class="btn btn-soft btn-sm btn-primary text-nowrap"> <span class="icon-[tabler--file-upload] size-4.5 shrink-0"></span> Drag & Drop to Upload </button>
      <p class="text-base-content/50 my-2 text-xs">or</p>
      <p class="link link-animated link-primary font-medium text-sm">Browse</p>
    </div>
    <div class="mx-12 mb-8 empty:m-0 grid grid-cols-4 gap-2 empty:gap-0 max-sm:grid-cols-2" data-file-upload-previews=""></div>
  </div>
</div>
{{< /code >}}

<!-- Upload single image -->

{{< headname level="3" >}} Upload single image {{< /headname >}}

Use file upload for a single image.

{{< code addClass="!block" >}}

<div
  data-file-upload='{
  "url": "/upload",
  "acceptedFiles": "image/*",
  "maxFiles": 1,
  "singleton": true
}' >
  <template data-file-upload-preview="">
    <div class="size-20">
      <img class="w-full rounded-full object-contain" data-dz-thumbnail="" />
    </div>
  </template>

  <div class="flex flex-wrap items-center gap-3 sm:gap-5">
    <div class="group" data-file-upload-previews="" data-file-upload-pseudo-trigger="">
      <span class="border-base-content/30 text-base-content/50 flex size-17 shrink-0 cursor-pointer items-center justify-center rounded-box border-2 border-dotted hover:bg-base-200/60 group-has-[div]:hidden" >
        <span class="icon-[tabler--user-square] size-9 shrink-0"></span>
      </span>
    </div>
    <div class="grow">
      <div class="flex items-center gap-x-2">
        <button type="button" class="btn btn-primary" data-file-upload-trigger="">
          <span class="icon-[tabler--upload] size-4 shrink-0"></span>
          Upload photo
        </button>
        <button type="button" class="btn btn-outline btn-error" data-file-upload-clear="">Delete</button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Input file -->

{{< headname level="3" >}} Input file {{< /headname >}}

Using file upload as a simple file upload.

{{< code addClass="!block" >}}

<div
  data-file-upload='{
  "url": "/upload",
  "maxFiles": 1,
  "singleton": true
}'
>
  <template data-file-upload-preview="">
    <div class="flex w-full items-center">
      <span class="grow-0 overflow-hidden truncate" data-file-upload-file-name=""></span>
      <span class="grow-0">.</span>
      <span class="grow-0" data-file-upload-file-ext=""></span>
    </div>
  </template>

  <button type="button" class="relative flex w-full overflow-hidden rounded-lg border border-base-content/20 text-sm focus:z-10 focus:ring-1 focus:border-primary focus:ring-primary focus:outline-none disabled:pointer-events-none disabled:opacity-50" >
    <span class="h-full text-nowrap bg-primary text-primary-content rounded-s-lg px-4 py-3">Choose File</span>
    <span class="group flex h-full grow overflow-hidden px-4 py-3 text-base-content" data-file-upload-previews="">
      <span class="group-has-[div]:hidden">No Chosen File</span>
    </span>
    <span class="absolute left-0 top-0 h-full w-full" data-file-upload-trigger=""></span>
  </button>
</div>
{{< /code >}}

<!-- Destroy/Reinitialize -->
{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}
The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a file upload.

{{< code addClass="!block" jsCode="true" >}}
<div
id="file-upload-to-destroy"
  data-file-upload='{
    "url": "/upload",
    "extensions": {
      "csv": {
        "icon": "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M4 22h14a2 2 0 0 0 2-2V7l-5-5H6a2 2 0 0 0-2 2v4\"/><path d=\"M14 2v4a2 2 0 0 0 2 2h4\"/><path d=\"m5 12-3 3 3 3\"/><path d=\"m9 18 3-3-3-3\"/></svg>",
        "class": "shrink-0 size-5"
      }
    }
  }' >

  <div class="bg-base-200/60 rounded-box flex flex-col justify-center border-2 border-base-content/20 border-dashed"  >
    <div class="text-center cursor-pointer p-12" data-file-upload-trigger="">
      <p class="text-base-content/50 mb-3 text-sm">Choose a file with a size up to 2MB.</p>
      <button class="btn btn-soft btn-sm btn-primary text-nowrap"> <span class="icon-[tabler--file-upload] size-4.5 shrink-0"></span> Drag & Drop to Upload </button>
      <p class="text-base-content/50 my-2 text-xs">or</p>
      <p class="link link-animated link-primary font-medium text-sm">Browse</p>
    </div>
    <div class="mx-12 mb-8 space-y-2 empty:m-0" data-file-upload-previews=""></div>
  </div>
</div>

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    // Destroy and reinit variables
    const fileUpload = document.querySelector('#file-upload-to-destroy')
    const destroyBtn = document.querySelector('#destroy-btn')
    const reinitBtn = document.querySelector('#reinit-btn')

    // Destroy usage
    destroyBtn.addEventListener('click', () => {
      const { element } = HSFileUpload.getInstance(fileUpload, true)

      element.destroy()

      destroyBtn.setAttribute('disabled', 'disabled')
      reinitBtn.removeAttribute('disabled')
    })

    // Reinit usage
    reinitBtn.addEventListener('click', () => {
      HSFileUpload.autoInit()

      reinitBtn.setAttribute('disabled', 'disabled')
      destroyBtn.removeAttribute('disabled')
    })
  })
</script>
{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Options table -->

Please understand that this component requires the <a href="https://www.dropzone.dev/" target="_blank" class="link link-primary font-semibold">Dropzone.js</a> plugin. Most of the plugin's options are also available in our wrapper.

<a href="https://docs.dropzone.dev/configuration/basics/configuration-options" target="_blank" class="link link-animated link-primary font-semibold mt-2">View Options</a>

{{< table >}}

PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-file-upload`</span>| <span class="text-pretty">Activate a File Upload by specifying on an element.</span>|`-`|`-`
`:extensions` | A list of extensions and their corresponding icons will be added to the container with the `data-file-upload-file-icon` selector if they match the extension name. | object| `Includes markup. See the code.`
`:autoHideTrigger` | If the attribute value is `true`, then `data-file-upload-trigger` will disappear if at least one item is added to the upload and will appear if more than one item is not in the upload.| boolean| `false`
`:singleton` | If the attribute value is `true`, the plugin will remove any previously uploaded files. This is necessary to emulate the behavior of a simple file input.| boolean| `false`
{{< /table >}}

<!-- Selector -->

{{< headname level="3" >}} Selector {{< /headname >}}

<!-- Selector table -->

{{< table >}}

Name|Description
`data-file-upload-trigger` | Specifies which element within the initialized container will serve as the clickable element.
`data-file-upload-previews` | Specifies which element within the initialized container will act as a wrapper for uploaded items.
`data-file-upload-clear` | Specifies which element within the initialized container will serve as the button to delete all files.
`data-file-upload-preview` | Specifies which element within the initialized container will act as a template for the uploading item. This should be an HTML `template` element.
`data-file-upload-file-icon` | Specifies which element within the uploading item will act as a wrapper for the file icon defined in the `extensions` property.
`data-file-upload-file-name` | Specifies which element within the uploading item will act as a wrapper for the file name.
`data-file-upload-file-ext` | Specifies which element within the uploading item will act as a wrapper for the file extension.
`data-file-upload-file-size` | Specifies which element within the uploading item will act as a wrapper for the file size.
`data-file-upload-remove` | Specifies which element within the uploading item will act as the remove button.
`data-file-upload-reload` | Specifies which element within the uploading item will act as the re-upload button.
`data-file-upload-progress-bar` | Specifies which element within the uploading item will act as the progress bar.
`data-file-upload-progress-bar-pane` | Specifies which element within the uploading item will act as the progress bar pane, whose width will dynamically increase during the upload process.
`data-file-upload-progress-bar-value` | Specifies which element within the uploading item will display the current progress value, which will dynamically increase during the upload process.
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSRemoveElement` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`destroy()`| Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSRemoveElement.getInstance(target, isInstance)`|<div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
{{< /table >}}

<p id="destroy-method" class="mt-5 mb-1.5 not-prose">Destroy instance.</p>

{{< code-highlight lang="js" >}}
const { element } = HSFileUpload.getInstance('#file-upload-to-destroy', true);
const destroyBtn = document.querySelector('#destroy-btn');

destroyBtn.addEventListener('click', () => {
  element.destroy();
});
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< callout "info" >}}
Please note that this component requires the <a href="https://www.dropzone.dev/" target="_blank" class="link link-primary font-semibold">Dropzone.js</a> plugin. Most events available in the plugin are available in our wrapper.

<a href="https://docs.dropzone.dev/configuration/basics/methods" target="_blank" class="link link-animated link-primary font-semibold mt-2">View Events</a>
{{< /callout >}}

Example of an event triggered when an item is successfully uploaded to the server.

{{< code-highlight lang="js" >}}const { element } = HSFileUpload.getInstance('#file-upload', true);
const { dropzone } = element;

dropzone.on('complete', () => {
  console.log('Item uploaded!');
});
{{< /code-highlight >}}
