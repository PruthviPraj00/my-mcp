---
title: "WYSIWYG Editor"
components: 3
description: "Utilize the WYSIWYG text editor to create and modify content, adjusting paragraphs, headings, images, and styling options."
bg_image: "svg/third-party-plugins/editor.svg"
menu:
  main:
    parent: "third party plugins"

previous: Wave Effect
previousLink: third-party-plugins/wave-effect/

pageJS:
  - "/js/pages/editor.js"

vendorJS:
  - "vendor/editorjs/editorjs.js"
  - "vendor/editorjs/header.js"
  - "vendor/editorjs/raw.js"
  - "vendor/editorjs/image.js"
  - "vendor/editorjs/checklist.js"
  - "vendor/editorjs/embed.js"
  - "vendor/editorjs/quote.js"
  - "vendor/editorjs/marker.js"
  - "vendor/editorjs/table.js"
  - "vendor/editorjs/inline-code.js"
  - "vendor/editorjs/warning.js"
  - "vendor/editorjs/nested-list.js"
---

<!-------------------- Getting started -------------------->

{{< headname level="2" >}} Getting started {{< /headname >}}

<!-- Setup -->

{{< headname level="3" >}} Setup {{< /headname >}}

Below are the comprehensively outlined steps you can follow to seamlessly integrate Editor JS into your project. This is official <a href="https://editorjs.io/" target="_blank" class="link link-primary">EditorJS</a> site.

<ul class="timeline timeline-snap-icon timeline-compact timeline-vertical mb-12 w-full ps-0">
  <!-- Installation -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">1</span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Installation</div>
      <p>Install <code>EditorJS</code> using npm:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="bash" >}}npm install @editorjs/editorjs --save{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Include Third-Party JS -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">2</span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Include EditorJS JavaScript</div>
      <p>Add the following <code>&lt;script&gt;</code> tag near the end of your <code>&lt;/body&gt;</code> section to include EditorJS:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="html" >}}<script src="../path/to/editor.js"></script>{{< /code-highlight >}}
      <p class="!mt-4">
        <strong>Note:</strong> A CDN link will not work here because customization of the default Vendor CSS is required to fit FlyonUI's design.
      </p>
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Tailwind Configuration -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">3</span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Update Tailwind Configuration</div>
      <p>Update your <code>tailwind.css</code> file to include the path for the FlyonUI editor's override CSS</p>
      {{< code-highlight addClass="!mb-0 mt-2 max-h-96 highlight-top-rounded-none" lang="css" >}}
@import "flyonui/src/vendor/editor.css";
{{< /code-highlight >}}
    </div>
    <hr class="!w-0.5 rounded-none border-transparent" />
  </li>

  <!-- Basic Usage -->
  <li class="mt-0 mb-0 ps-0">
    <div class="timeline-middle mb-2">
      <span class="text-base-content flex size-7 items-center justify-center rounded-full border border-base-content/20 font-semibold">4</span>
    </div>
    <div class="timeline-end mb-0 w-full rounded-lg p-4 m-0">
      <div class="text-base-content mb-3 font-semibold">Basic Usage</div>
      <p>This is a basic example of how to create an EditorJS instance:</p>
      {{< code-highlight addClass="!mb-0 mt-2" lang="js" >}}import EditorJS from '@editorjs/editorjs';

const editor = new EditorJS({
  holder: 'editorjs', // Replace 'editorjs' with your container's id
});{{< /code-highlight >}}

</div>

  </li>
</ul>

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default{{< /headname >}}

This is a basic example of a text editor using <a href="https://editorjs.io/" target="_blank" class="link link-primary">EditorJS</a>. With EditorJS, we can create a Notion-like text editor. The text editor below includes basic tools such as heading, nested list, table, inline code, and more. For additional tools, you can refer to the <a href="https://github.com/codex-team/editor.js" rel="nofollow noindex" target="_blank" class="link link-primary">EditorJS repository</a> and check out the <a href="https://github.com/editor-js/awesome-editorjs" target="_blank" class="link link-primary">Awesome Editor.js</a> list for more tools.

For images, we use the Simple Image plugin, which allows you to drag and drop images or paste the image URL directly, but no UI option will be visible in the toolbar.

{{< code jsCode="true" >}}

<div id="basic" class="bg-base-100 shadow-base-300/20 rounded-box w-full p-4 shadow-sm"></div>

<!-- Js -->
<script>
  const editor = new EditorJS({
    holder: 'basic', // id of the element
    // placeholder
    placeholder: 'Type text or paste a link',

    // Tools
    tools: {
      header: {
        class: Header,
        inlineToolbar: ['marker', 'link'],
        config: {
          placeholder: 'Header'
        },
        shortcut: 'CMD+SHIFT+H'
      },
      raw: RawTool,
      image: SimpleImage,
      checklist: {
        class: Checklist,
        inlineToolbar: true
      },
      list: {
        class: NestedList,
        inlineToolbar: true,
        shortcut: 'CMD+SHIFT+L'
      },
      embed: Embed,
      quote: {
        class: Quote,
        inlineToolbar: true,
        config: {
          quotePlaceholder: 'Enter a quote',
          captionPlaceholder: "Quote's author"
        },
        shortcut: 'CMD+SHIFT+O'
      },
      marker: {
        class: Marker,
        shortcut: 'CMD+SHIFT+M'
      },
      table: {
        class: Table,
        inlineToolbar: true,
        shortcut: 'CMD+ALT+T'
      },
      inlineCode: {
        class: InlineCode,
        shortcut: 'CMD+SHIFT+I'
      },
      warning: {
        class: Warning,
        inlineToolbar: true,
        shortcut: 'CMD+SHIFT+W',
        config: {
          titlePlaceholder: 'Title',
          messagePlaceholder: 'Message'
        }
      }
    },

    onChange: () => {
      editor
        .save()
        .then(outputData => {
          displayJSON(outputData)
        })
        .catch(error => {
          console.error('Saving failed: ', error)
        })
    }
  })

  // Function to display JSON data
  function displayJSON(data) {
    const outputElement = document.getElementById('output')
    outputElement.textContent = JSON.stringify(data, null, 2) // Pretty print JSON with indentation
  }
</script>

{{< /code >}}

<span class="font-medium text-base-content text-base">This block displays the data in JSON format.</span>

<pre id="output" class="bg-neutral/20 text-base-content rounded-box p-3 w-full my-4 min-h-20"></pre>

<!-- Modal -->

{{< headname level="3" >}} Modal {{< /headname >}}

Example showcasing a text editor in a modal.

{{< code jsCode="true" >}}

<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="text-editor-modal" data-overlay="#text-editor-modal">Daily tasks</button>

<div id="text-editor-modal" class="overlay modal overlay-open:opacity-100 overlay-open:duration-300 hidden" role="dialog" tabindex="-1">
  <div class="modal-dialog overlay-open:opacity-100 overlay-open:duration-300 modal-dialog-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Daily tasks</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#text-editor-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        <div id="modal-editor" class="border border-base-content/25 rounded-box p-4"></div>
      </div>
    </div>
  </div>
</div>

<!-- Js -->
<script>
  const modaleditor = new EditorJS({
    holder: 'modal-editor', // id of the element
    // placeholder
    placeholder: 'Type text or paste a link',

    // Tools
    tools: {
      header: {
        class: Header,
        inlineToolbar: ['marker', 'link'],
        config: {
          placeholder: 'Header'
        },
        shortcut: 'CMD+SHIFT+H'
      },
      raw: RawTool,
      image: SimpleImage,
      checklist: {
        class: Checklist,
        inlineToolbar: true
      },
      list: {
        class: NestedList,
        inlineToolbar: true,
        shortcut: 'CMD+SHIFT+L'
      },
      embed: Embed,
      quote: {
        class: Quote,
        inlineToolbar: true,
        config: {
          quotePlaceholder: 'Enter a quote',
          captionPlaceholder: "Quote's author"
        },
        shortcut: 'CMD+SHIFT+O'
      },
      marker: {
        class: Marker,
        shortcut: 'CMD+SHIFT+M'
      },
      table: {
        class: Table,
        inlineToolbar: true,
        shortcut: 'CMD+ALT+T'
      },
      inlineCode: {
        class: InlineCode,
        shortcut: 'CMD+SHIFT+I'
      },
      warning: {
        class: Warning,
        inlineToolbar: true,
        shortcut: 'CMD+SHIFT+W',
        config: {
          titlePlaceholder: 'Title',
          messagePlaceholder: 'Message'
        }
      }
    }
  })
</script>

{{< /code >}}
