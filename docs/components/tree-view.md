---
title: "Tree View"
description: "Use Tree View to navigate hierarchical data, making it perfect for directories, hierarchies, and more. Effortlessly expand, collapse, and select tree nodes."
bg_image: "svg/components/tree-view.svg"
components: 1
menu:
  main:
    parent: "components"

previous: Timeline
previousLink: components/timeline/

next: Breadcrumb
nextLink: navigations/breadcrumb/

requires_js: true

pageJS:
  - "/js/pages/tree-view.js"

vendorJS:
  - "https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"
  - "/vendor/sortablejs/sortablejs.js"
---

{{< callout "info" >}}
Tree View components are adopted from <a href="https://preline.co/docs/tree-view.html" target="_blank" class="link link-primary font-semibold">Preline UI</a> components using <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Class Table -->

{{< class-table >}}
accordion-heading | part | Container class specifically for child elements within `accordion-item`.
accordion-toggle | part | This class is responsible for toggling the tree-view between open and closed states.
accordion-content | part | This class defines the content within each tree-view section.
accordion-item | part | This class represents each individual item within the tree-view structure.
accordion-item-active | state | This class applies styling to indicate an active item within the tree-view.
tree-view-space| modifier | Style space and border for sub-menu.
tree-view-selected:{tw-utility-class} | variant | A utility that applies specific Tailwind classes when an item is selected.
tree-view-disabled:{tw-utility-class} | variant | A utility that applies specific Tailwind classes when an item has "disabled" class.
{{< /class-table >}}

{{< callout "info" >}}
Please note that this plugin utilizes both the {{< link link="components/accordion/" addClass="link font-semibold link-primary" >}}Accordion{{< /link >}} and <span class="font-semibold">TreeView</span> plugins. The TreeView plugin supports multi-select functionality, allowing you to select multiple folders or files by holding down the <code>Shift</code>, <code>Ctrl</code>, or <code>Cmd</code> key.
{{< /callout >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

To initialize the Tree View component, apply the `data-tree-view` attribute to the wrapper element. This attribute activates the Tree View functionality on the specified element.

Each item in the Tree View is defined by the `data-tree-view-item` attribute. Add this attribute to the individual item elements within the Tree View to indicate which parts of the structure are items that can be interacted with.

Utilize the provided example for Tree View. You can change icon, text as per your needs.

{{< code >}}

<div id="tree-view" class="rounded-sm" role="tree" aria-orientation="vertical" data-tree-view="">
  <!-- 1st Level Accordion -->
  <div class="accordion-item active" role="treeitem" aria-expanded="true" id="basic-tree-view-heading-one"
    data-tree-view-item='{
    "value": "assets",
    "isDir": true
  }'
  >
    <!-- 1st Level Accordion Heading -->
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="basic-tree-view-collapse-one" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">assets</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End 1st Level Accordion Heading -->
    <!-- 1st Level Collapse -->
    <div id="basic-tree-view-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="basic-tree-view-heading-one" >
      <!-- 2nd Level Accordion Group -->
      <div class="tree-view-space">
        <!-- 2nd Level Nested Accordion -->
        <div class="accordion-item active" role="treeitem" aria-expanded="true" id="basic-tree-view-sub-heading-one"
          data-tree-view-item='{
          "value": "css",
          "isDir": true
        }'
        >
          <!-- 2nd Level Accordion Heading -->
          <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
            <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="basic-tree-view-sub-collapse-one" >
              <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
            </button>
            <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
              <div class="flex items-center gap-x-3">
                <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                <div class="grow">
                  <span class="text-base-content">css</span>
                </div>
              </div>
            </div>
          </div>
          <!-- End 2nd Level Accordion Heading -->
          <!-- 2nd Level Collapse -->
          <div id="basic-tree-view-sub-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="basic-tree-view-sub-heading-one" >
            <!-- 3rd Level Accordion Group -->
            <div class="tree-view-space">
              <!-- 3rd Level Accordion -->
              <div class="accordion-item active" role="treeitem" aria-expanded="true" id="basic-tree-view-sub-level-two-heading-one"
                data-tree-view-item='{
                "value": "main",
                "isDir": true
              }'
              >
                <!-- 3rd Level Accordion Heading -->
                <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                  <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="basic-tree-view-sub-level-two-collapse-one" >
                    <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                  </button>
                  <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                    <div class="flex items-center gap-x-3">
                      <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                      <div class="grow">
                        <span class="text-base-content">main</span>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- End 3rd Level Accordion Heading -->
                <!-- 3rd Level Collapse -->
                <div id="basic-tree-view-sub-level-two-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="basic-tree-view-sub-level-two-heading-one" >
                  <div class="tree-view-space">
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                      data-tree-view-item='{
                      "value": "main.css",
                      "isDir": false
                    }'
                    >
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">main.css</span>
                        </div>
                      </div>
                    </div>
                    <!-- End 3rd Level Item -->
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                      data-tree-view-item='{
                      "value": "docs.css",
                      "isDir": false
                    }'
                    >
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">docs.css</span>
                        </div>
                      </div>
                    </div>
                    <!-- End 3rd Level Item -->
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 rounded-md px-2"
                      data-tree-view-item='{
                      "value": "README.txt",
                      "isDir": false
                    }'
                    >
                      <span class="text-base-content">README.txt</span>
                    </div>
                    <!-- End 3rd Level Item -->
                  </div>
                </div>
                <!-- End 3rd Level Collapse -->
              </div>
              <!-- End 3rd Level Accordion -->
              <!-- 3rd Level Accordion -->
              <div class="accordion-item" role="treeitem" aria-expanded="false" id="basic-tree-view-sub-level-two-heading-two"
                data-tree-view-item='{
                "value": "tailwind",
                "isDir": true
              }'
              >
                <!-- 3rd Level Accordion Heading -->
                <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                  <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="basic-tree-view-sub-level-two-collapse-two" >
                    <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                  </button>
                  <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                    <div class="flex items-center gap-x-3">
                      <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                      <div class="grow">
                        <span class="text-base-content">tailwind</span>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- End 3rd Level Accordion Heading -->
                <!-- 3rd Level Collapse -->
                <div id="basic-tree-view-sub-level-two-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="basic-tree-view-sub-level-two-heading-two" >
                  <div class="tree-view-space">
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                      data-tree-view-item='{
                      "value": "input.css",
                      "isDir": false
                    }'
                    >
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">input.css</span>
                        </div>
                      </div>
                    </div>
                    <!-- End 3rd Level Item -->
                  </div>
                </div>
                <!-- End 3rd Level Collapse -->
              </div>
              <!-- End 3rd Level Accordion -->
              <!-- 3rd Level Heading -->
              <div class="tree-view-selected:bg-base-300/40 rounded-md px-1.5 py-0.5" role="treeitem"
                data-tree-view-item='{
                "value": ".gitignore",
                "isDir": false
              }'
              >
                <span class="text-base-content">.gitignore</span>
              </div>
              <!-- End 3rd Level Heading -->
            </div>
            <!-- End 3rd Level Accordion Group -->
          </div>
          <!-- End 2nd Level Collapse -->
        </div>
        <!-- End 2nd Level Nested Accordion -->
        <!-- 2nd Level Nested Accordion -->
        <div class="accordion-item" role="treeitem" aria-expanded="false" id="basic-tree-view-sub-heading-two"
          data-tree-view-item='{
          "value": "img",
          "isDir": true
        }'
        >
          <!-- 2nd Level Accordion Heading -->
          <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
            <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="basic-tree-view-sub-collapse-two" >
              <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
            </button>
            <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
              <div class="flex items-center gap-x-3">
                <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                <div class="grow">
                  <span class="text-base-content">img</span>
                </div>
              </div>
            </div>
          </div>
          <!-- End 2nd Level Accordion Heading -->
          <!-- 2nd Level Collapse -->
          <div id="basic-tree-view-sub-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="basic-tree-view-sub-heading-two" >
            <div class="tree-view-space">
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                "value": "hero.jpg",
                "isDir": false
              }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">hero.jpg</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                "value": "tailwind.png",
                "isDir": false
              }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">tailwind.png</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                "value": "untitled.png",
                "isDir": false
              }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">untitled.png</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
            </div>
          </div>
          <!-- End 2nd Level Collapse -->
        </div>
        <!-- End 2nd Level Nested Accordion -->
        <!-- 2nd Level Nested Accordion -->
        <div class="accordion-item" role="treeitem" aria-expanded="false" id="basic-tree-view-sub-heading-three"
          data-tree-view-item='{
          "value": "js",
          "isDir": true
        }'
        >
          <!-- 2nd Level Accordion Heading -->
          <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
            <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="basic-tree-view-sub-collapse-three" >
              <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
            </button>
            <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
              <div class="flex items-center gap-x-3">
                <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                <div class="grow">
                  <span class="text-base-content">js</span>
                </div>
              </div>
            </div>
          </div>
          <!-- End 2nd Level Accordion Heading -->
          <!-- 2nd Level Collapse -->
          <div id="basic-tree-view-sub-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="basic-tree-view-sub-heading-three" >
            <div class="tree-view-space">
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                "value": "flyonui.jpg",
                "isDir": false
              }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">flyonui.jpg</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
            </div>
          </div>
          <!-- End 2nd Level Collapse -->
        </div>
        <!-- End 2nd Level Nested Accordion -->
      </div>
      <!-- 2nd Level Accordion Group -->
    </div>
    <!-- End 1st Level Collapse -->

  </div>
  <!-- End 1st Level Accordion -->

  <!-- 1st Level Accordion -->
  <div class="accordion-item" role="treeitem" aria-expanded="false" id="basic-tree-view-heading-two"
    data-tree-view-item='{
    "value": "scripts",
    "isDir": true
  }'
  >
    <!-- 1st Level Accordion Heading -->
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="basic-tree-view-collapse-two" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">scripts</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End 1st Level Accordion Heading -->
    <!-- 1st Level Collapse -->
    <div id="basic-tree-view-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="basic-tree-view-heading-two" >
      <div class="tree-view-space">
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
          "value": "flyonui.js",
          "isDir": false
        }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">flyonui.js</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
          "value": "tailwind.js",
          "isDir": false
        }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">tailwind.js</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
          "value": "www.js",
          "isDir": false
        }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">www.js</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
      </div>
    </div>
    <!-- End 1st Level Collapse -->

  </div>
  <!-- End 1st Level Accordion -->

  <!-- 1st Level Accordion -->
  <div class="accordion-item" role="treeitem" aria-expanded="false" id="basic-tree-view-heading-three"
    data-tree-view-item='{
    "value": "templates",
    "isDir": true
  }'
  >
    <!-- 1st Level Accordion Heading -->
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="basic-tree-view-collapse-three" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">templates</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End 1st Level Accordion Heading -->
    <!-- 1st Level Collapse -->
    <div id="basic-tree-view-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="basic-tree-view-heading-three" >
      <div class="tree-view-space">
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
          "value": "index.html",
          "isDir": false
        }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">index.html</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
      </div>
    </div>
    <!-- End 1st Level Collapse -->

  </div>
  <!-- End 1st Level Accordion -->
</div>

{{< /code >}}

<!-- Close Active Element -->

{{< headname level="3" >}} Close Active Element {{< /headname >}}

This demo demonstrates how to close the currently open element within its group.

{{< code >}}

<div id="tree-view" class="rounded-sm" role="tree" aria-orientation="vertical" data-tree-view="">
  <div class="accordion">
  <!-- 1st Level Accordion -->
  <div class="accordion-item active" role="treeitem" aria-expanded="true" id="close-currently-opened-heading-one"
    data-tree-view-item='{
    "value": "assets",
    "isDir": true
  }'
  >
    <!-- 1st Level Accordion Heading -->
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="close-currently-opened-collapse-one" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">assets</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End 1st Level Accordion Heading -->
    <!-- 1st Level Collapse -->
    <div id="close-currently-opened-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="close-currently-opened-heading-one" >
      <!-- 2nd Level Accordion Group -->
      <div class="accordion tree-view-space">
        <!-- 2nd Level Nested Accordion -->
        <div class="accordion-item active" role="treeitem" aria-expanded="true" id="close-currently-opened-sub-heading-one"
          data-tree-view-item='{
          "value": "css",
          "isDir": true
        }'
        >
          <!-- 2nd Level Accordion Heading -->
          <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
            <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="close-currently-opened-sub-collapse-one" >
              <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
            </button>
            <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
              <div class="flex items-center gap-x-3">
                <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                <div class="grow">
                  <span class="text-base-content">css</span>
                </div>
              </div>
            </div>
          </div>
          <!-- End 2nd Level Accordion Heading -->
          <!-- 2nd Level Collapse -->
          <div id="close-currently-opened-sub-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="close-currently-opened-sub-heading-one" >
            <!-- 3rd Level Accordion Group -->
            <div class="accordion tree-view-space">
              <!-- 3rd Level Accordion -->
              <div class="accordion-item active" role="treeitem" aria-expanded="true" id="close-currently-opened-sub-level-two-heading-one"
                data-tree-view-item='{
                "value": "main",
                "isDir": true
              }'
              >
                <!-- 3rd Level Accordion Heading -->
                <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                  <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="close-currently-opened-sub-level-two-collapse-one" >
                    <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                  </button>
                  <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                    <div class="flex items-center gap-x-3">
                      <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                      <div class="grow">
                        <span class="text-base-content">main</span>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- End 3rd Level Accordion Heading -->
                <!-- 3rd Level Collapse -->
                <div id="close-currently-opened-sub-level-two-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="close-currently-opened-sub-level-two-heading-one" >
                  <div class="tree-view-space">
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                      data-tree-view-item='{
                      "value": "main.css",
                      "isDir": false
                    }'
                    >
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">main.css</span>
                        </div>
                      </div>
                    </div>
                    <!-- End 3rd Level Item -->
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                      data-tree-view-item='{
                      "value": "docs.css",
                      "isDir": false
                    }'
                    >
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">docs.css</span>
                        </div>
                      </div>
                    </div>
                    <!-- End 3rd Level Item -->
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 rounded-md px-2"
                      data-tree-view-item='{
                      "value": "README.txt",
                      "isDir": false
                    }'
                    >
                      <span class="text-base-content">README.txt</span>
                    </div>
                    <!-- End 3rd Level Item -->
                  </div>
                </div>
                <!-- End 3rd Level Collapse -->
              </div>
              <!-- End 3rd Level Accordion -->
              <!-- 3rd Level Accordion -->
              <div class="accordion-item" role="treeitem" aria-expanded="false" id="close-currently-opened-sub-level-two-heading-two"
                data-tree-view-item='{
                "value": "tailwind",
                "isDir": true
              }'
              >
                <!-- 3rd Level Accordion Heading -->
                <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                  <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="close-currently-opened-sub-level-two-collapse-two" >
                    <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                  </button>
                  <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                    <div class="flex items-center gap-x-3">
                      <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                      <div class="grow">
                        <span class="text-base-content">tailwind</span>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- End 3rd Level Accordion Heading -->
                <!-- 3rd Level Collapse -->
                <div id="close-currently-opened-sub-level-two-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="close-currently-opened-sub-level-two-heading-two" >
                  <div class="tree-view-space">
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                      data-tree-view-item='{
                      "value": "input.css",
                      "isDir": false
                    }'
                    >
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">input.css</span>
                        </div>
                      </div>
                    </div>
                    <!-- End 3rd Level Item -->
                  </div>
                </div>
                <!-- End 3rd Level Collapse -->
              </div>
              <!-- End 3rd Level Accordion -->
              <!-- 3rd Level Heading -->
              <div class="tree-view-selected:bg-base-300/40 rounded-md px-1.5 py-0.5" role="treeitem"
                data-tree-view-item='{
                "value": ".gitignore",
                "isDir": false
              }'
              >
                <span class="text-base-content">.gitignore</span>
              </div>
              <!-- End 3rd Level Heading -->
            </div>
            <!-- End 3rd Level Accordion Group -->
          </div>
          <!-- End 2nd Level Collapse -->
        </div>
        <!-- End 2nd Level Nested Accordion -->
        <!-- 2nd Level Nested Accordion -->
        <div class="accordion-item" role="treeitem" aria-expanded="false" id="close-currently-opened-sub-heading-two"
          data-tree-view-item='{
          "value": "img",
          "isDir": true
        }'
        >
          <!-- 2nd Level Accordion Heading -->
          <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
            <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="close-currently-opened-sub-collapse-two" >
              <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
            </button>
            <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
              <div class="flex items-center gap-x-3">
                <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                <div class="grow">
                  <span class="text-base-content">img</span>
                </div>
              </div>
            </div>
          </div>
          <!-- End 2nd Level Accordion Heading -->
          <!-- 2nd Level Collapse -->
          <div id="close-currently-opened-sub-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="close-currently-opened-sub-heading-two" >
            <div class="tree-view-space">
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                "value": "hero.jpg",
                "isDir": false
              }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">hero.jpg</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                "value": "tailwind.png",
                "isDir": false
              }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">tailwind.png</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                "value": "untitled.png",
                "isDir": false
              }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">untitled.png</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
            </div>
          </div>
          <!-- End 2nd Level Collapse -->
        </div>
        <!-- End 2nd Level Nested Accordion -->
        <!-- 2nd Level Nested Accordion -->
        <div class="accordion-item" role="treeitem" aria-expanded="false" id="close-currently-opened-sub-heading-three"
          data-tree-view-item='{
          "value": "js",
          "isDir": true
        }'
        >
          <!-- 2nd Level Accordion Heading -->
          <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
            <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="close-currently-opened-sub-collapse-three" >
              <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
            </button>
            <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
              <div class="flex items-center gap-x-3">
                <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                <div class="grow">
                  <span class="text-base-content">js</span>
                </div>
              </div>
            </div>
          </div>
          <!-- End 2nd Level Accordion Heading -->
          <!-- 2nd Level Collapse -->
          <div id="close-currently-opened-sub-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="close-currently-opened-sub-heading-three" >
            <div class="tree-view-space">
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                "value": "flyonui.jpg",
                "isDir": false
              }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">flyonui.jpg</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
            </div>
          </div>
          <!-- End 2nd Level Collapse -->
        </div>
        <!-- End 2nd Level Nested Accordion -->
      </div>
      <!-- 2nd Level Accordion Group -->
    </div>
    <!-- End 1st Level Collapse -->

  </div>
  <!-- End 1st Level Accordion -->

  <!-- 1st Level Accordion -->
  <div class="accordion-item" role="treeitem" aria-expanded="false" id="close-currently-opened-heading-two"
    data-tree-view-item='{
    "value": "scripts",
    "isDir": true
  }'
  >
    <!-- 1st Level Accordion Heading -->
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="close-currently-opened-collapse-two" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">scripts</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End 1st Level Accordion Heading -->
    <!-- 1st Level Collapse -->
    <div id="close-currently-opened-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="close-currently-opened-heading-two" >
      <div class="tree-view-space">
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
          "value": "flyonui.js",
          "isDir": false
        }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">flyonui.js</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
          "value": "tailwind.js",
          "isDir": false
        }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">tailwind.js</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
          "value": "www.js",
          "isDir": false
        }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">www.js</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
      </div>
    </div>
    <!-- End 1st Level Collapse -->

  </div>
  <!-- End 1st Level Accordion -->

  <!-- 1st Level Accordion -->
  <div class="accordion-item" role="treeitem" aria-expanded="false" id="close-currently-opened-heading-three"
    data-tree-view-item='{
    "value": "templates",
    "isDir": true
  }'
  >
    <!-- 1st Level Accordion Heading -->
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="close-currently-opened-collapse-three" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">templates</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End 1st Level Accordion Heading -->
    <!-- 1st Level Collapse -->
    <div id="close-currently-opened-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="close-currently-opened-heading-three" >
      <div class="tree-view-space">
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
          "value": "index.html",
          "isDir": false
        }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">index.html</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
      </div>
    </div>
    <!-- End 1st Level Collapse -->
  </div>
  </div>
  <!-- End 1st Level Accordion -->
</div>

{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

{{< callout "warning" >}}
Please note that below demos use the third-party library <a href="https://sortablejs.github.io/Sortable/" target="_blank" class="link link-warning font-semibold">Sortable.js</a> and <a href="https://lodash.com/" target="_blank" class="link link-warning font-semibold">Lodash</a> for drag-and-drop functionality. Refer {{< link link="third-party-plugins/drag-and-drop/" addClass="link font-semibold link-warning" >}}Drag and Drop{{< /link >}} Component for more info.
<br />
<br />
You may select multiple folders/files by holding <code>shift</code>, <code>ctrl</code> | <code>cmd</code> key.
{{< /callout >}}

<!-- Draggable -->

{{< headname level="3" >}} Draggable {{< /headname >}}

The example below demonstrates the drag-and-drop functionality for items.

{{< code jsCode="true" >}}

<div id="tree-view-nested" class="rounded-sm" role="tree" aria-orientation="vertical" data-tree-view="">
  <!-- 1st Level Accordion Group -->
  <div data-nested-draggable="">
    <!-- 1st Level Accordion -->
    <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-1 active" role="treeitem" aria-expanded="true" id="draggable-tree-heading-one"
      data-tree-view-item='{
        "value": "assets",
        "isDir": true
      }'
    >
      <!-- 1st Level Accordion Heading -->
      <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
        <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="draggable-tree-collapse-one" >
          <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
        </button>
        <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">assets</span>
            </div>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->
      <!-- 1st Level Collapse -->
      <div id="draggable-tree-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-tree-heading-one" >
        <!-- 2nd Level Accordion Group -->
        <div class="tree-view-space" data-nested-draggable="">
          <!-- 2nd Level Nested Accordion -->
          <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2 active" role="treeitem" aria-expanded="true" id="draggable-tree-sub-heading-one"
            data-tree-view-item='{
              "value": "css",
              "isDir": true
            }'
          >
            <!-- 2nd Level Accordion Heading -->
            <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
              <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="draggable-tree-sub-collapse-one" >
                <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
              </button>
              <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">css</span>
                  </div>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->
            <!-- 2nd Level Collapse -->
            <div id="draggable-tree-sub-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-tree-sub-heading-one" >
              <!-- 3rd Level Accordion Group -->
              <div class="tree-view-space" data-nested-draggable="">
                <!-- 3rd Level Accordion -->
                <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-3 active" role="treeitem" aria-expanded="true" id="draggable-tree-sub-level-two-heading-one"
                  data-tree-view-item='{
                    "value": "main",
                    "isDir": true
                  }'
                >
                  <!-- 3rd Level Accordion Heading -->
                  <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                    <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="draggable-tree-sub-level-two-collapse-one" >
                      <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                    </button>
                    <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">main</span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- End 3rd Level Accordion Heading -->
                  <!-- 3rd Level Collapse -->
                  <div id="draggable-tree-sub-level-two-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-tree-sub-level-two-heading-one" >
                    <div class="tree-view-space" data-nested-draggable="">
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-4 cursor-pointer rounded-md px-2" role="treeitem"
                        data-tree-view-item='{
                          "value": "main.css",
                          "isDir": false
                        }'
                      >
                        <div class="flex items-center gap-x-3">
                          <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                          <div class="grow">
                            <span class="text-base-content">main.css</span>
                          </div>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-4 cursor-pointer rounded-md px-2" role="treeitem"
                        data-tree-view-item='{
                          "value": "docs.css",
                          "isDir": false
                        }'
                      >
                        <div class="flex items-center gap-x-3">
                          <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                          <div class="grow">
                            <span class="text-base-content">docs.css</span>
                          </div>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-4 rounded-md px-2"
                        data-tree-view-item='{
                          "value": "README.txt",
                          "isDir": false
                        }'
                      >
                        <span class="text-base-content">README.txt</span>
                      </div>
                      <!-- End 3rd Level Item -->
                    </div>
                  </div>
                  <!-- End 3rd Level Collapse -->
                </div>
                <!-- End 3rd Level Accordion -->
                <!-- 3rd Level Accordion -->
                <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-3" role="treeitem" aria-expanded="false" id="draggable-tree-sub-level-two-heading-two"
                  data-tree-view-item='{
                    "value": "tailwind",
                    "isDir": true
                  }'
                >
                  <!-- 3rd Level Accordion Heading -->
                  <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                    <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="draggable-tree-sub-level-two-collapse-two" >
                      <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                    </button>
                    <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">tailwind</span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- End 3rd Level Accordion Heading -->
                  <!-- 3rd Level Collapse -->
                  <div id="draggable-tree-sub-level-two-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-tree-sub-level-two-heading-two" >
                    <div class="tree-view-space" data-nested-draggable="">
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                        data-tree-view-item='{
                          "value": "input.css",
                          "isDir": false
                        }'
                      >
                        <div class="flex items-center gap-x-3">
                          <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                          <div class="grow">
                            <span class="text-base-content">input.css</span>
                          </div>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                    </div>
                  </div>
                  <!-- End 3rd Level Collapse -->
                </div>
                <!-- End 3rd Level Accordion -->
                <!-- 3rd Level Heading -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-3 rounded-md px-1.5 py-0.5" role="treeitem"
                  data-tree-view-item='{
                      "value": ".gitignore",
                      "isDir": false
                    }'
                >
                  <span class="text-base-content">.gitignore</span>
                </div>
                <!-- End 3rd Level Heading -->
              </div>
              <!-- End 3rd Level Accordion Group -->
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
          <!-- 2nd Level Nested Accordion -->
          <div class="accordion-item" role="treeitem" aria-expanded="false" id="draggable-tree-sub-heading-two"
            data-tree-view-item='{
              "value": "img",
              "isDir": true
            }'
          >
            <!-- 2nd Level Accordion Heading -->
            <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
              <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="draggable-tree-sub-collapse-two" >
                <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
              </button>
              <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">img</span>
                  </div>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->
            <!-- 2nd Level Collapse -->
            <div id="draggable-tree-sub-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-tree-sub-heading-two" >
              <div class="tree-view-space" data-nested-draggable="">
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                    "value": "hero.jpg",
                    "isDir": false
                  }'
                >
                  <div class="flex items-center gap-x-3">
                    <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                    <div class="grow">
                      <span class="text-base-content">hero.jpg</span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
                <!-- 2nd Level Item -->
                <div role="treeitem" class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                    "value": "tailwind.png",
                    "isDir": false
                  }'
                >
                  <div class="flex items-center gap-x-3">
                    <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                    <div class="grow">
                      <span class="text-base-content">tailwind.png</span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                    "value": "untitled.png",
                    "isDir": false
                  }'
                >
                  <div class="flex items-center gap-x-3">
                    <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                    <div class="grow">
                      <span class="text-base-content">untitled.png</span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
              </div>
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
          <!-- 2nd Level Nested Accordion -->
          <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2" role="treeitem" aria-expanded="false" id="draggable-tree-sub-heading-three"
            data-tree-view-item='{
              "value": "js",
              "isDir": true
            }'
          >
            <!-- 2nd Level Accordion Heading -->
            <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
              <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="draggable-tree-sub-collapse-three" >
                <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
              </button>
              <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">js</span>
                  </div>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->
            <!-- 2nd Level Collapse -->
            <div id="draggable-tree-sub-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-tree-sub-heading-three" >
              <div class="tree-view-space" data-nested-draggable="">
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                    "value": "flyonui.jpg",
                    "isDir": false
                  }'
                >
                  <div class="flex items-center gap-x-3">
                    <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                    <div class="grow">
                      <span class="text-base-content">flyonui.jpg</span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
              </div>
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
        </div>
        <!-- 2nd Level Accordion Group -->
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->
    <!-- 1st Level Accordion -->
    <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-1" role="treeitem" aria-expanded="false" id="draggable-tree-heading-two"
      data-tree-view-item='{
        "value": "scripts",
        "isDir": true
      }'
    >
      <!-- 1st Level Accordion Heading -->
      <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
        <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="draggable-tree-collapse-two" >
          <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
        </button>
        <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">scripts</span>
            </div>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->
      <!-- 1st Level Collapse -->
      <div id="draggable-tree-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-tree-heading-two" >
        <div class="tree-view-space" data-nested-draggable="">
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
              "value": "flyonui.js",
              "isDir": false
            }'
          >
            <div class="flex items-center gap-x-3">
              <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
              <div class="grow">
                <span class="text-base-content">flyonui.js</span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
              "value": "tailwind.js",
              "isDir": false
            }'
          >
            <div class="flex items-center gap-x-3">
              <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
              <div class="grow">
                <span class="text-base-content">tailwind.js</span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
              "value": "www.js",
              "isDir": false
            }'
          >
            <div class="flex items-center gap-x-3">
              <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
              <div class="grow">
                <span class="text-base-content">www.js</span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
        </div>
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->
    <!-- 1st Level Accordion -->
    <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-1" role="treeitem" aria-expanded="false" id="draggable-tree-heading-three"
      data-tree-view-item='{
        "value": "templates",
        "isDir": true
      }'
    >
      <!-- 1st Level Accordion Heading -->
      <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
        <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="draggable-tree-collapse-three" >
          <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
        </button>
        <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">templates</span>
            </div>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->
      <!-- 1st Level Collapse -->
      <div id="draggable-tree-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-tree-heading-three" >
        <div class="tree-view-space" data-nested-draggable="">
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
              "value": "index.html",
              "isDir": false
            }'
          >
            <div class="flex items-center gap-x-3">
              <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
              <div class="grow">
                <span class="text-base-content">index.html</span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
        </div>
      </div>
      <!-- End 1st Level Collapse -->
    </div>
  </div>
  <!-- End 1st Level Accordion Group -->
</div>
<!-- End Tree Root -->

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    ;(function () {
      const draggable = document.querySelectorAll('[data-nested-draggable]')

      draggable.forEach(el => {
        const options = {
          group: 'nested',
          animation: 150,
          fallbackOnBody: true,
          swapThreshold: 0.65,
          ghostClass: 'dragged',
          onEnd: evt => {
            const { item } = evt

            if (item.classList.contains('accordion')) {
              let existingInstance = HSAccordion.getInstance(item, true)
              let updatedInstance

              existingInstance.element.update()
              updatedInstance = HSAccordion.getInstance(item, true)
              window.$hsAccordionCollection.map(el => {
                if (
                  el.element.el !== existingInstance.element.el &&
                  el.element.group === existingInstance.element.group &&
                  el.element.el.closest('.accordion') &&
                  el.element.el.classList.contains('active') &&
                  existingInstance.element.el.classList.contains('active')
                )
                  el.element.hide()

                return el
              })
            }

            if (!!item.hasAttribute('data-tree-view-item')) {
              const treeViewItem = HSTreeView.getInstance(item.closest('[data-tree-view]'), true)

              treeViewItem.element.update()
            }
          }
        }
        const data = el.getAttribute('data-nested-draggable')
        const dataOptions = data ? JSON.parse(data) : {}
        const sortable = new Sortable(el, _.merge(options, dataOptions))
      })
    })()
  })
</script>

{{< /code >}}

<!--  Draggable and close active element -->

{{< headname level="3" >}} Draggable and close active element {{< /headname >}}

The example below demonstrates drag-and-drop functionality, including the ability to close the currently open element within its group.

{{< code jsCode="true" >}}

<!-- Tree Root -->
<div id="tree-view-nested-alt" class="rounded-sm" role="tree" aria-orientation="vertical" data-tree-view="">
  <!-- 1st Level Accordion Group -->
  <div class="accordion" data-nested-draggable="">
    <!-- 1st Level Accordion -->
    <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-1 active" role="treeitem" aria-expanded="true" id="draggable-and-auto-collapse-one-level-group-tree-heading-one"
      data-tree-view-item='{
      "value": "assets",
      "isDir": true
    }'
    >
      <!-- 1st Level Accordion Heading -->
      <div
        class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5"
      >
        <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="draggable-and-auto-collapse-one-level-group-tree-collapse-one" >
          <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
        </button>
        <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">assets</span>
            </div>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->
      <!-- 1st Level Collapse -->
      <div id="draggable-and-auto-collapse-one-level-group-tree-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-and-auto-collapse-one-level-group-tree-heading-one" >
        <!-- 2nd Level Accordion Group -->
        <div class="accordion tree-view-space" data-nested-draggable="">
          <!-- 2nd Level Nested Accordion -->
          <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2 active" role="treeitem" aria-expanded="true" id="draggable-and-auto-collapse-one-level-group-tree-sub-heading-one"
            data-tree-view-item='{
            "value": "css",
            "isDir": true
          }'
          >
            <!-- 2nd Level Accordion Heading -->
            <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
              <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="draggable-and-auto-collapse-one-level-group-tree-sub-collapse-one" >
                <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
              </button>
              <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">css</span>
                  </div>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->
            <!-- 2nd Level Collapse -->
            <div id="draggable-and-auto-collapse-one-level-group-tree-sub-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-and-auto-collapse-one-level-group-tree-sub-heading-one" >
              <!-- 3rd Level Accordion Group -->
              <div class="accordion tree-view-space" data-nested-draggable="">
                <!-- 3rd Level Accordion -->
                <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-3 active" role="treeitem" aria-expanded="true" id="draggable-and-auto-collapse-one-level-group-tree-sub-level-two-heading-one"
                  data-tree-view-item='{
                  "value": "main",
                  "isDir": true
                }'
                >
                  <!-- 3rd Level Accordion Heading -->
                  <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                    <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="draggable-and-auto-collapse-one-level-group-tree-sub-level-two-collapse-one" >
                      <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                    </button>
                    <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">main</span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- End 3rd Level Accordion Heading -->
                  <!-- 3rd Level Collapse -->
                  <div id="draggable-and-auto-collapse-one-level-group-tree-sub-level-two-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-and-auto-collapse-one-level-group-tree-sub-level-two-heading-one" >
                    <div class="tree-view-space" data-nested-draggable="">
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-4 cursor-pointer rounded-md px-2" role="treeitem"
                        data-tree-view-item='{
                        "value": "main.css",
                        "isDir": false
                      }'
                      >
                        <div class="flex items-center gap-x-3">
                          <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                          <div class="grow">
                            <span class="text-base-content">main.css</span>
                          </div>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-4 cursor-pointer rounded-md px-2" role="treeitem"
                        data-tree-view-item='{
                        "value": "docs.css",
                        "isDir": false
                      }'
                      >
                        <div class="flex items-center gap-x-3">
                          <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                          <div class="grow">
                            <span class="text-base-content">docs.css</span>
                          </div>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-4 tree-view-disabled:opacity-50 disabled px-2"
                        data-tree-view-item='{
                        "value": "README.txt",
                        "isDir": false
                      }'
                      >
                        <span class="text-base-content">README.txt</span>
                      </div>
                      <!-- End 3rd Level Item -->
                    </div>
                  </div>
                  <!-- End 3rd Level Collapse -->
                </div>
                <!-- End 3rd Level Accordion -->
                <!-- 3rd Level Accordion -->
                <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-3" role="treeitem" aria-expanded="false" id="draggable-and-auto-collapse-one-level-group-tree-sub-level-two-heading-two"
                  data-tree-view-item='{
                  "value": "tailwind",
                  "isDir": true
                }'
                >
                  <!-- 3rd Level Accordion Heading -->
                  <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                    <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="draggable-and-auto-collapse-one-level-group-tree-sub-level-two-collapse-two" >
                      <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                    </button>
                    <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">tailwind</span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- End 3rd Level Accordion Heading -->
                  <!-- 3rd Level Collapse -->
                  <div id="draggable-and-auto-collapse-one-level-group-tree-sub-level-two-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-and-auto-collapse-one-level-group-tree-sub-level-two-heading-two" >
                    <div class="tree-view-space" data-nested-draggable="">
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-4 cursor-pointer rounded-md px-2" role="treeitem"
                        data-tree-view-item='{
                        "value": "input.css",
                        "isDir": false
                      }'
                      >
                        <div class="flex items-center gap-x-3">
                          <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                          <div class="grow">
                            <span class="text-base-content">input.css</span>
                          </div>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                    </div>
                  </div>
                  <!-- End 3rd Level Collapse -->
                </div>
                <!-- End 3rd Level Accordion -->
                <!-- 3rd Level Heading -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-3 rounded-md px-1.5 py-0.5" role="treeitem"
                  data-tree-view-item='{
                  "value": ".gitignore",
                  "isDir": false
                }'
                >
                  <span class="text-base-content">.gitignore</span>
                </div>
                <!-- End 3rd Level Heading -->
              </div>
              <!-- End 3rd Level Accordion Group -->
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
          <!-- 2nd Level Nested Accordion -->
          <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2" role="treeitem" aria-expanded="false" id="draggable-and-auto-collapse-one-level-group-tree-sub-heading-two"
            data-tree-view-item='{
            "value": "img",
            "isDir": true
          }'
          >
            <!-- 2nd Level Accordion Heading -->
            <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
              <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="draggable-and-auto-collapse-one-level-group-tree-sub-collapse-two" >
                <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
              </button>
              <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">img</span>
                  </div>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->
            <!-- 2nd Level Collapse -->
            <div id="draggable-and-auto-collapse-one-level-group-tree-sub-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-and-auto-collapse-one-level-group-tree-sub-heading-two" >
              <div class="tree-view-space" data-nested-draggable="">
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                  "value": "hero.jpg",
                  "isDir": false
                }'
                >
                  <div class="flex items-center gap-x-3">
                    <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                    <div class="grow">
                      <span class="text-base-content">hero.jpg</span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                  "value": "tailwind.png",
                  "isDir": false
                }'
                >
                  <div class="flex items-center gap-x-3">
                    <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                    <div class="grow">
                      <span class="text-base-content">tailwind.png</span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                  "value": "untitled.png",
                  "isDir": false
                }'
                >
                  <div class="flex items-center gap-x-3">
                    <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                    <div class="grow">
                      <span class="text-base-content">untitled.png</span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
              </div>
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
          <!-- 2nd Level Nested Accordion -->
          <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2" role="treeitem" aria-expanded="false" id="draggable-and-auto-collapse-one-level-group-tree-sub-heading-three"
            data-tree-view-item='{
            "value": "js",
            "isDir": true
          }'
          >
            <!-- 2nd Level Accordion Heading -->
            <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
              <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="draggable-and-auto-collapse-one-level-group-tree-sub-collapse-three" >
                <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
              </button>
              <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">js</span>
                  </div>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->
            <!-- 2nd Level Collapse -->
            <div id="draggable-and-auto-collapse-one-level-group-tree-sub-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-and-auto-collapse-one-level-group-tree-sub-heading-three" >
              <div class="tree-view-space" data-nested-draggable="">
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                  "value": "flyonui.jpg",
                  "isDir": false
                }'
                >
                  <div class="flex items-center gap-x-3">
                    <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                    <div class="grow">
                      <span class="text-base-content">flyonui.jpg</span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
              </div>
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
        </div>
        <!-- 2nd Level Accordion Group -->
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->
    <!-- 1st Level Accordion -->
    <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-1" role="treeitem" aria-expanded="false" id="draggable-and-auto-collapse-one-level-group-tree-heading-two"
      data-tree-view-item='{
      "value": "scripts",
      "isDir": true
    }'
    >
      <!-- 1st Level Accordion Heading -->
      <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
        <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="draggable-and-auto-collapse-one-level-group-tree-collapse-two" >
          <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
        </button>
        <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">scripts</span>
            </div>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->
      <!-- 1st Level Collapse -->
      <div id="draggable-and-auto-collapse-one-level-group-tree-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-and-auto-collapse-one-level-group-tree-heading-two" >
        <div class="tree-view-space" data-nested-draggable="">
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
            "value": "flyonui.js",
            "isDir": false
          }'
          >
            <div class="flex items-center gap-x-3">
              <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
              <div class="grow">
                <span class="text-base-content">flyonui.js</span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
            "value": "tailwind.js",
            "isDir": false
          }'
          >
            <div class="flex items-center gap-x-3">
              <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
              <div class="grow">
                <span class="text-base-content">tailwind.js</span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
            "value": "www.js",
            "isDir": false
          }'
          >
            <div class="flex items-center gap-x-3">
              <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
              <div class="grow">
                <span class="text-base-content">www.js</span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
        </div>
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->
    <!-- 1st Level Accordion -->
    <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-1 tree-view-disabled:opacity-50 disabled" role="treeitem" aria-expanded="false" id="draggable-and-auto-collapse-one-level-group-tree-heading-three"
      data-tree-view-item='{
      "value": "templates",
      "isDir": true
    }'
    >
      <!-- 1st Level Accordion Heading -->
      <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
        <button class="accordion-toggle tree-view-disabled:pointer-events-none btn btn-sm btn-circle btn-text" disabled="" aria-expanded="false" aria-controls="draggable-and-auto-collapse-one-level-group-tree-collapse-three" >
          <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
        </button>
        <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">templates</span>
            </div>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->
      <!-- 1st Level Collapse -->
      <div id="draggable-and-auto-collapse-one-level-group-tree-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="draggable-and-auto-collapse-one-level-group-tree-heading-three" >
        <div class="tree-view-space" data-nested-draggable="">
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
            "value": "index.html",
            "isDir": false
          }'
          >
            <div class="flex items-center gap-x-3">
              <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
              <div class="grow">
                <span class="text-base-content">index.html</span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
        </div>
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->

  </div>
  <!-- End 1st Level Accordion Group -->
</div>
<!-- End Tree Root -->

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    ;(function () {
      const draggable = document.querySelectorAll('[data-nested-draggable]')

      draggable.forEach(el => {
        const options = {
          group: 'nested',
          animation: 150,
          fallbackOnBody: true,
          swapThreshold: 0.65,
          ghostClass: 'dragged',
          onEnd: evt => {
            const { item } = evt

            if (item.classList.contains('accordion')) {
              let existingInstance = HSAccordion.getInstance(item, true)
              let updatedInstance

              existingInstance.element.update()
              updatedInstance = HSAccordion.getInstance(item, true)
              window.$hsAccordionCollection.map(el => {
                if (
                  el.element.el !== existingInstance.element.el &&
                  el.element.group === existingInstance.element.group &&
                  el.element.el.closest('.accordion') &&
                  el.element.el.classList.contains('active') &&
                  existingInstance.element.el.classList.contains('active')
                )
                  el.element.hide()

                return el
              })
            }

            if (!!item.hasAttribute('data-tree-view-item')) {
              const treeViewItem = HSTreeView.getInstance(item.closest('[data-tree-view]'), true)

              treeViewItem.element.update()
            }
          }
        }
        const data = el.getAttribute('data-nested-draggable')
        const dataOptions = data ? JSON.parse(data) : {}
        const sortable = new Sortable(el, _.merge(options, dataOptions))
      })
    })()
  })
</script>

{{< /code >}}

<!-- Checkbox -->

{{< headname level="3" >}} Checkbox {{< /headname >}}

You can select folders and files by marking the checkboxes.

{{< code jsCode="true" >}}

<!-- Tree Root -->
<div id="tree-view-checkbox" role="tree" aria-orientation="vertical"
  data-tree-view='{
  "controlBy": "checkbox",
  "autoSelectChildren": true
}'
>
  <!-- 1st Level Accordion Group -->
  <div data-nested-draggable="">
    <!-- 1st Level Accordion -->
    <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2-1 active" role="treeitem" aria-expanded="true" id="checkbox-tree-heading-one"
      data-tree-view-item='{
      "value": "assets",
      "isDir": true
    }'
    >
      <!-- 1st Level Accordion Heading -->
      <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
        <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="checkbox-tree-collapse-one" >
          <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
        </button>
        <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
          <div class="flex items-center gap-2">
            <input type="checkbox" class="checkbox checkbox-xs" id="assets" value="assets" />
            <label class="label-text text-base" for="assets">assets</label>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->
      <!-- 1st Level Collapse -->
      <div id="checkbox-tree-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="checkbox-tree-heading-one" >
        <!-- 2nd Level Accordion Group -->
        <div class="tree-view-space" data-nested-draggable="">
          <!-- 2nd Level Nested Accordion -->
          <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2-2 active" role="treeitem" aria-expanded="true" id="checkbox-tree-sub-heading-one"
            data-tree-view-item='{
            "value": "css",
            "isDir": true
          }'
          >
            <!-- 2nd Level Accordion Heading -->
            <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
              <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="checkbox-tree-sub-collapse-one" >
                <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
              </button>
              <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                <div class="flex items-center gap-2">
                  <input type="checkbox" class="checkbox checkbox-xs" id="css" value="css" />
                  <label class="label-text text-base" for="css">css</label>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->
            <!-- 2nd Level Collapse -->
            <div id="checkbox-tree-sub-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="checkbox-tree-sub-heading-one" >
              <!-- 3rd Level Accordion Group -->
              <div class="tree-view-space" data-nested-draggable="">
                <!-- 3rd Level Accordion -->
                <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2-3 active" role="treeitem" aria-expanded="true" id="checkbox-tree-sub-level-two-heading-one"
                  data-tree-view-item='{
                  "value": "main",
                  "isDir": true
                }'
                >
                  <!-- 3rd Level Accordion Heading -->
                  <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                    <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="checkbox-tree-sub-level-two-collapse-one" >
                      <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                    </button>
                    <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                      <div class="flex items-center gap-2">
                        <input type="checkbox" class="checkbox checkbox-xs" id="main" value="main" />
                        <label class="label-text text-base" for="main">main</label>
                      </div>
                    </div>
                  </div>
                  <!-- End 3rd Level Accordion Heading -->
                  <!-- 3rd Level Collapse -->
                  <div id="checkbox-tree-sub-level-two-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="checkbox-tree-sub-level-two-heading-one" >
                    <div class="tree-view-space" data-nested-draggable="">
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-4 cursor-pointer rounded-md px-2" role="treeitem"
                        data-tree-view-item='{
                        "value": "main.css",
                        "isDir": false
                      }'
                      >
                        <div class="flex items-center gap-2">
                          <input type="checkbox" class="checkbox checkbox-xs" id="mainCss" value="main.css" />
                          <label class="label-text text-base" for="mainCss">main.css</label>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-4 cursor-pointer rounded-md px-2" role="treeitem"
                        data-tree-view-item='{
                        "value": "docs.css",
                        "isDir": false
                      }'
                      >
                        <div class="flex items-center gap-2">
                          <input type="checkbox" class="checkbox checkbox-xs" id="docs" value="docs.css" />
                          <label class="label-text text-base" for="docs">docs.css</label>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-4 tree-view-disabled:opacity-50 disabled px-2"
                        data-tree-view-item='{
                        "value": "README.txt",
                        "isDir": false
                      }'
                      >
                        <div class="flex items-center gap-2">
                          <input type="checkbox" class="checkbox checkbox-xs" id="readme" value="README.txt" disabled />
                          <label class="label-text text-base" for="readme">README.txt</label>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                    </div>
                  </div>
                  <!-- End 3rd Level Collapse -->
                </div>
                <!-- End 3rd Level Accordion -->
                <!-- 3rd Level Accordion -->
                <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2-3" role="treeitem" aria-expanded="false" id="checkbox-tree-sub-level-two-heading-two"
                  data-tree-view-item='{
                  "value": "tailwind",
                  "isDir": true
                }'
                >
                  <!-- 3rd Level Accordion Heading -->
                  <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                    <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="checkbox-tree-sub-level-two-collapse-two" >
                      <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                    </button>
                    <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                      <div class="flex items-center gap-2">
                        <input type="checkbox" class="checkbox checkbox-xs" id="tailwind" value="tailwind" />
                        <label class="label-text text-base" for="tailwind">tailwind</label>
                      </div>
                    </div>
                  </div>
                  <!-- End 3rd Level Accordion Heading -->
                  <!-- 3rd Level Collapse -->
                  <div id="checkbox-tree-sub-level-two-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="checkbox-tree-sub-level-two-heading-two" >
                    <div class="tree-view-space" data-nested-draggable="">
                      <!-- 3rd Level Item -->
                      <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-4 cursor-pointer rounded-md px-2" role="treeitem"
                        data-tree-view-item='{
                        "value": "input.css",
                        "isDir": false
                      }'
                      >
                        <div class="flex items-center gap-2">
                          <input type="checkbox" class="checkbox checkbox-xs" id="inputCss" value="input.css" />
                          <label class="label-text text-base" for="inputCss">input.css</label>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                    </div>
                  </div>
                  <!-- End 3rd Level Collapse -->
                </div>
                <!-- End 3rd Level Accordion -->
                <!-- 3rd Level Heading -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-3 rounded-md px-1.5 py-0.5" role="treeitem"
                  data-tree-view-item='{
                  "value": ".gitignore",
                  "isDir": false
                }'
                >
                  <div class="flex items-center gap-2">
                    <input type="checkbox" class="checkbox checkbox-xs" id="gitignore" value=".gitignore" />
                    <label class="label-text text-base" for="gitignore">.gitignore</label>
                  </div>
                </div>
                <!-- End 3rd Level Heading -->
              </div>
              <!-- End 3rd Level Accordion Group -->
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
          <!-- 2nd Level Nested Accordion -->
          <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2-2" role="treeitem" aria-expanded="false" id="checkbox-tree-sub-heading-two"
            data-tree-view-item='{
            "value": "img",
            "isDir": true
          }'
          >
            <!-- 2nd Level Accordion Heading -->
            <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
              <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="checkbox-tree-sub-collapse-two" >
                <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
              </button>
              <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                <div class="flex items-center gap-2">
                  <input type="checkbox" class="checkbox checkbox-xs" id="img" value="img" />
                  <label class="label-text text-base" for="img">img</label>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->
            <!-- 2nd Level Collapse -->
            <div id="checkbox-tree-sub-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="checkbox-tree-sub-heading-two" >
              <div class="tree-view-space" data-nested-draggable="">
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                  "value": "hero.jpg",
                  "isDir": false
                }'
                >
                  <div class="flex items-center gap-2">
                    <input type="checkbox" class="checkbox checkbox-xs" id="hero" value="hero.jpg" />
                    <label class="label-text text-base" for="hero">hero.jpg</label>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                  "value": "tailwind.png",
                  "isDir": false
                }'
                >
                  <div class="flex items-center gap-2">
                    <input type="checkbox" class="checkbox checkbox-xs" id="tailwindPng" value="tailwind.png" />
                    <label class="label-text text-base" for="tailwindPng">tailwind.png</label>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                  "value": "untitled.png",
                  "isDir": false
                }'
                >
                  <div class="flex items-center gap-2">
                    <input type="checkbox" class="checkbox checkbox-xs" id="untitled" value="untitled.png" />
                    <label class="label-text text-base" for="untitled">untitled.png</label>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
              </div>
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
          <!-- 2nd Level Nested Accordion -->
          <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2-2" role="treeitem" aria-expanded="false" id="checkbox-tree-sub-heading-three"
            data-tree-view-item='{
            "value": "js",
            "isDir": true
          }'
          >
            <!-- 2nd Level Accordion Heading -->
            <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
              <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="checkbox-tree-sub-collapse-three" >
                <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
              </button>
              <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                <div class="flex items-center gap-2">
                  <input type="checkbox" class="checkbox checkbox-xs" id="js" value="js" />
                  <label class="label-text text-base" for="js">js</label>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->
            <!-- 2nd Level Collapse -->
            <div id="checkbox-tree-sub-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="checkbox-tree-sub-heading-three" >
              <div class="tree-view-space" data-nested-draggable="">
                <!-- 2nd Level Item -->
                <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-3 cursor-pointer rounded-md px-2" role="treeitem"
                  data-tree-view-item='{
                  "value": "flyonui.jpg",
                  "isDir": false
                }'
                >
                  <div class="flex items-center gap-2">
                    <input type="checkbox" class="checkbox checkbox-xs" id="flyonuiJpg" value="flyonui.jpg" />
                    <label class="label-text text-base" for="flyonuiJpg">flyonui.jpg</label>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
              </div>
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
        </div>
        <!-- 2nd Level Accordion Group -->
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->
    <!-- 1st Level Accordion -->
    <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2-1" role="treeitem" aria-expanded="false" id="checkbox-tree-heading-two"
      data-tree-view-item='{
      "value": "scripts",
      "isDir": true
    }'
    >
      <!-- 1st Level Accordion Heading -->
      <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
        <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="checkbox-tree-collapse-two" >
          <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
        </button>
        <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
          <div class="flex items-center gap-2">
            <input type="checkbox" class="checkbox checkbox-xs" id="scripts" value="scripts" />
            <label class="label-text text-base" for="scripts">scripts</label>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->
      <!-- 1st Level Collapse -->
      <div id="checkbox-tree-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="checkbox-tree-heading-two" >
        <div class="tree-view-space" data-nested-draggable="">
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
            "value": "flyonui.js",
            "isDir": false
          }'
          >
            <div class="flex items-center gap-2">
              <input type="checkbox" class="checkbox checkbox-xs" id="flyonuiJs" value="flyonui.js" />
              <label class="label-text text-base" for="flyonuiJs">flyonui.js</label>
            </div>
          </div>
          <!-- End 1st Level Item -->
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
            "value": "tailwind.js",
            "isDir": false
          }'
          >
            <div class="flex items-center gap-2">
              <input type="checkbox" class="checkbox checkbox-xs" id="tailwindJS" value="tailwind.js" />
              <label class="label-text text-base" for="tailwindJS">tailwind.js</label>
            </div>
          </div>
          <!-- End 1st Level Item -->
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
            "value": "www.js",
            "isDir": false
          }'
          >
            <div class="flex items-center gap-2">
              <input type="checkbox" class="checkbox checkbox-xs" id="www" value="www.js" />
              <label class="label-text text-base" for="www">www.js</label>
            </div>
          </div>
          <!-- End 1st Level Item -->
        </div>
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->
    <!-- 1st Level Accordion -->
    <div class="accordion-item dragged:bg-primary/20 dragged:rounded-sm nested-2-1 tree-view-disabled:opacity-50 disabled" role="treeitem" aria-expanded="false" id="checkbox-tree-heading-three"
      data-tree-view-item='{
      "value": "templates",
      "isDir": true
    }'
    >
      <!-- 1st Level Accordion Heading -->
      <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
        <button class="accordion-toggle tree-view-disabled:pointer-events-none btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="checkbox-tree-collapse-three" disabled="" >
          <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
        </button>
        <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
          <span class="text-base-content">
            <div class="flex items-center gap-2">
              <input type="checkbox" class="checkbox checkbox-xs" id="templates" value="templates" disabled />
              <label class="label-text text-base" for="templates">templates</label>
            </div>
          </span>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->
      <!-- 1st Level Collapse -->
      <div id="checkbox-tree-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="checkbox-tree-heading-three" >
        <div class="tree-view-space" data-nested-draggable="">
          <!-- 1st Level Item -->
          <div class="tree-view-selected:bg-base-300/40 dragged:bg-primary/20 dragged:rounded-sm nested-2-2 cursor-pointer rounded-md px-2" role="treeitem"
            data-tree-view-item='{
            "value": "index.html",
            "isDir": false
          }'
          >
            <div class="flex items-center gap-2">
              <input type="checkbox" class="checkbox checkbox-xs" id="indexHtml" value="index.html" />
              <label class="label-text text-base" for="indexHtml">index.html</label>
            </div>
          </div>
          <!-- End 1st Level Item -->
        </div>
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->

  </div>
  <!-- End 1st Level Accordion Group -->
</div>
<!-- End Tree Root -->

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    ;(function () {
      const draggable = document.querySelectorAll('[data-nested-draggable]')

      draggable.forEach(el => {
        const options = {
          group: 'nested',
          animation: 150,
          fallbackOnBody: true,
          swapThreshold: 0.65,
          ghostClass: 'dragged',
          onEnd: evt => {
            const { item } = evt

            if (item.classList.contains('accordion')) {
              let existingInstance = HSAccordion.getInstance(item, true)
              let updatedInstance

              existingInstance.element.update()
              updatedInstance = HSAccordion.getInstance(item, true)
              window.$hsAccordionCollection.map(el => {
                if (
                  el.element.el !== existingInstance.element.el &&
                  el.element.group === existingInstance.element.group &&
                  el.element.el.closest('.accordion') &&
                  el.element.el.classList.contains('active') &&
                  existingInstance.element.el.classList.contains('active')
                )
                  el.element.hide()

                return el
              })
            }

            if (!!item.hasAttribute('data-tree-view-item')) {
              const treeViewItem = HSTreeView.getInstance(item.closest('[data-tree-view]'), true)

              treeViewItem.element.update()
            }
          }
        }
        const data = el.getAttribute('data-nested-draggable')
        const dataOptions = data ? JSON.parse(data) : {}
        const sortable = new Sortable(el, _.merge(options, dataOptions))
      })
    })()
  })
</script>

{{< /code >}}

<!-- Destroy/Reinitialize -->

{{< headname level="3" >}} Destroy/Reinitialize {{< /headname >}}

The `destroy` <a href="#destroy-method" class="link link-primary">method</a> is provided to facilitate the destruction of a tree-view element.

{{< code jsCode="true" addClass="flex-col" >}}

<div id="tree-view-to-destroy" class="rounded-sm w-fit" role="tree" aria-orientation="vertical" data-tree-view="">
  <!-- 1st Level Accordion Group -->
  <!-- 1st Level Accordion -->
  <div class="accordion-item active" role="treeitem" aria-expanded="true" id="destroy-tree-view-heading-one"
    data-tree-view-item='{
      "value": "assets",
      "isDir": true
    }'
  >
    <!-- 1st Level Accordion Heading -->
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="destroy-tree-view-collapse-one" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">assets</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End 1st Level Accordion Heading -->
    <!-- 1st Level Collapse -->
    <div id="destroy-tree-view-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="destroy-tree-view-heading-one" >
      <!-- 2nd Level Accordion Group -->
      <div class="tree-view-space">
        <!-- 2nd Level Nested Accordion -->
        <div class="accordion-item active" role="treeitem" aria-expanded="true" id="destroy-tree-view-sub-heading-one"
          data-tree-view-item='{
            "value": "css",
            "isDir": true
          }'
        >
          <!-- 2nd Level Accordion Heading -->
          <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
            <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="destroy-tree-view-sub-collapse-one" >
              <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
            </button>
            <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
              <div class="flex items-center gap-x-3">
                <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                <div class="grow">
                  <span class="text-base-content">css</span>
                </div>
              </div>
            </div>
          </div>
          <!-- End 2nd Level Accordion Heading -->
          <!-- 2nd Level Collapse -->
          <div id="destroy-tree-view-sub-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="destroy-tree-view-sub-heading-one" >
            <!-- 3rd Level Accordion Group -->
            <div class="tree-view-space">
              <!-- 3rd Level Accordion -->
              <div class="accordion-item active" role="treeitem" aria-expanded="true" id="destroy-tree-view-sub-level-two-heading-one"
                data-tree-view-item='{
                  "value": "main",
                  "isDir": true
                }'
              >
                <!-- 3rd Level Accordion Heading -->
                <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                  <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="destroy-tree-view-sub-level-two-collapse-one" >
                    <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                  </button>
                  <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                    <div class="flex items-center gap-x-3">
                      <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                      <div class="grow">
                        <span class="text-base-content">main</span>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- End 3rd Level Accordion Heading -->
                <!-- 3rd Level Collapse -->
                <div id="destroy-tree-view-sub-level-two-collapse-one" class="accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="destroy-tree-view-sub-level-two-heading-one" >
                  <div class="tree-view-space">
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                      data-tree-view-item='{
                        "value": "main.css",
                        "isDir": false
                      }'
                    >
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">main.css</span>
                        </div>
                      </div>
                    </div>
                    <!-- End 3rd Level Item -->
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                      data-tree-view-item='{
                        "value": "docs.css",
                        "isDir": false
                      }'
                    >
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">docs.css</span>
                        </div>
                      </div>
                    </div>
                    <!-- End 3rd Level Item -->
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 rounded-md px-2"
                      data-tree-view-item='{
                        "value": "README.txt",
                        "isDir": false
                      }'
                    >
                      <span class="text-base-content">README.txt</span>
                    </div>
                    <!-- End 3rd Level Item -->
                  </div>
                </div>
                <!-- End 3rd Level Collapse -->
              </div>
              <!-- End 3rd Level Accordion -->
              <!-- 3rd Level Accordion -->
              <div class="accordion-item" role="treeitem" aria-expanded="false" id="destroy-tree-view-sub-level-two-heading-two"
                data-tree-view-item='{
                  "value": "tailwind",
                  "isDir": true
                }'
              >
                <!-- 3rd Level Accordion Heading -->
                <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
                  <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="destroy-tree-view-sub-level-two-collapse-two" >
                    <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
                  </button>
                  <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
                    <div class="flex items-center gap-x-3">
                      <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                      <div class="grow">
                        <span class="text-base-content">tailwind</span>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- End 3rd Level Accordion Heading -->
                <!-- 3rd Level Collapse -->
                <div id="destroy-tree-view-sub-level-two-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="destroy-tree-view-sub-level-two-heading-two" >
                  <div class="tree-view-space">
                    <!-- 3rd Level Item -->
                    <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                      data-tree-view-item='{
                        "value": "input.css",
                        "isDir": false
                      }'
                    >
                      <div class="flex items-center gap-x-3">
                        <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
                        <div class="grow">
                          <span class="text-base-content">input.css</span>
                        </div>
                      </div>
                    </div>
                    <!-- End 3rd Level Item -->
                  </div>
                </div>
                <!-- End 3rd Level Collapse -->
              </div>
              <!-- End 3rd Level Accordion -->
              <!-- 3rd Level Heading -->
              <div class="tree-view-selected:bg-base-300/40 rounded-md px-1.5 py-0.5" role="treeitem"
                data-tree-view-item='{
                    "value": ".gitignore",
                    "isDir": false
                  }'
              >
                <span class="text-base-content">.gitignore</span>
              </div>
              <!-- End 3rd Level Heading -->
            </div>
            <!-- End 3rd Level Accordion Group -->
          </div>
          <!-- End 2nd Level Collapse -->
        </div>
        <!-- End 2nd Level Nested Accordion -->
        <!-- 2nd Level Nested Accordion -->
        <div class="accordion-item" role="treeitem" aria-expanded="false" id="destroy-tree-view-sub-heading-two"
          data-tree-view-item='{
            "value": "img",
            "isDir": true
          }'
        >
          <!-- 2nd Level Accordion Heading -->
          <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
            <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="destroy-tree-view-sub-collapse-two" >
              <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
            </button>
            <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
              <div class="flex items-center gap-x-3">
                <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                <div class="grow">
                  <span class="text-base-content">img</span>
                </div>
              </div>
            </div>
          </div>
          <!-- End 2nd Level Accordion Heading -->
          <!-- 2nd Level Collapse -->
          <div id="destroy-tree-view-sub-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="destroy-tree-view-sub-heading-two" >
            <div class="tree-view-space">
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                  "value": "hero.jpg",
                  "isDir": false
                }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">hero.jpg</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
              <!-- 2nd Level Item -->
              <div role="treeitem" class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                  "value": "tailwind.png",
                  "isDir": false
                }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">tailwind.png</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                  "value": "untitled.png",
                  "isDir": false
                }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">untitled.png</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
            </div>
          </div>
          <!-- End 2nd Level Collapse -->
        </div>
        <!-- End 2nd Level Nested Accordion -->
        <!-- 2nd Level Nested Accordion -->
        <div class="accordion-item" role="treeitem" aria-expanded="false" id="destroy-tree-view-sub-heading-three"
          data-tree-view-item='{
            "value": "js",
            "isDir": true
          }'
        >
          <!-- 2nd Level Accordion Heading -->
          <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
            <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="destroy-tree-view-sub-collapse-three" >
              <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
            </button>
            <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
              <div class="flex items-center gap-x-3">
                <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
                <div class="grow">
                  <span class="text-base-content">js</span>
                </div>
              </div>
            </div>
          </div>
          <!-- End 2nd Level Accordion Heading -->
          <!-- 2nd Level Collapse -->
          <div id="destroy-tree-view-sub-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="destroy-tree-view-sub-heading-three" >
            <div class="tree-view-space">
              <!-- 2nd Level Item -->
              <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
                data-tree-view-item='{
                  "value": "flyonui.jpg",
                  "isDir": false
                }'
              >
                <div class="flex items-center gap-x-3">
                  <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
                  <div class="grow">
                    <span class="text-base-content">flyonui.jpg</span>
                  </div>
                </div>
              </div>
              <!-- End 2nd Level Item -->
            </div>
          </div>
          <!-- End 2nd Level Collapse -->
        </div>
        <!-- End 2nd Level Nested Accordion -->
      </div>
      <!-- 2nd Level Accordion Group -->
    </div>
    <!-- End 1st Level Collapse -->
  </div>
  <!-- End 1st Level Accordion -->
  <!-- 1st Level Accordion -->
  <div class="accordion-item" role="treeitem" aria-expanded="false" id="destroy-tree-view-heading-two"
    data-tree-view-item='{
      "value": "scripts",
      "isDir": true
    }'
  >
    <!-- 1st Level Accordion Heading -->
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="destroy-tree-view-collapse-two" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">scripts</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End 1st Level Accordion Heading -->
    <!-- 1st Level Collapse -->
    <div id="destroy-tree-view-collapse-two" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="destroy-tree-view-heading-two" >
      <div class="tree-view-space">
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
            "value": "flyonui.js",
            "isDir": false
          }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">flyonui.js</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
            "value": "tailwind.js",
            "isDir": false
          }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">tailwind.js</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
            "value": "www.js",
            "isDir": false
          }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">www.js</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
      </div>
    </div>
    <!-- End 1st Level Collapse -->
  </div>
  <!-- End 1st Level Accordion -->
  <!-- 1st Level Accordion -->
  <div class="accordion-item" role="treeitem" aria-expanded="false" id="destroy-tree-view-heading-three"
    data-tree-view-item='{
      "value": "templates",
      "isDir": true
    }'
  >
    <!-- 1st Level Accordion Heading -->
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="false" aria-controls="destroy-tree-view-collapse-three" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      <div class="tree-view-selected:bg-base-300/40 grow cursor-pointer rounded-md px-1.5">
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--folder] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">templates</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End 1st Level Accordion Heading -->
    <!-- 1st Level Collapse -->
    <div id="destroy-tree-view-collapse-three" class="accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="destroy-tree-view-heading-three" >
      <div class="tree-view-space">
        <!-- 1st Level Item -->
        <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
          data-tree-view-item='{
            "value": "index.html",
            "isDir": false
          }'
        >
          <div class="flex items-center gap-x-3">
            <span class="icon-[tabler--file] text-base-content size-4 shrink-0"></span>
            <div class="grow">
              <span class="text-base-content">index.html</span>
            </div>
          </div>
        </div>
        <!-- End 1st Level Item -->
      </div>
    </div>
    <!-- End 1st Level Collapse -->
  </div>
  <!-- End 1st Level Accordion Group -->
</div>
<!-- End Tree Root -->

<div class="mt-4 flex gap-3">
  <button class="btn btn-primary" id="destroy-btn">Destroy</button>
  <button class="btn btn-primary" id="reinit-btn" disabled>Reinitialize</button>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', () => {
    ;(function () {
      const treeView = document.querySelector('#tree-view-to-destroy')
      const accordions = document.querySelectorAll('#tree-view-to-destroy .accordion-item')
      const destroy = document.querySelector('#destroy-btn')
      const reinit = document.querySelector('#reinit-btn')

      destroy.addEventListener('click', () => {
        const treeViewInstance = HSTreeView.getInstance(treeView, true)

        treeViewInstance.element.destroy()
        accordions.forEach(el => {
          const accordionInstance = HSAccordion.getInstance(el, true)

          accordionInstance.element.destroy()
        })

        destroy.setAttribute('disabled', 'disabled')
        reinit.removeAttribute('disabled')
      })

      reinit.addEventListener('click', () => {
        HSTreeView.autoInit()
        HSAccordion.autoInit()

        reinit.setAttribute('disabled', 'disabled')
        destroy.removeAttribute('disabled')
      })
    })()
  })
</script>

{{< /code >}}

<!-------------------- JavaScript behavior -------------------->

{{< headname level="2" >}} JavaScript behavior {{< /headname >}}

<!-- Options -->

{{< headname level="3" >}} Options {{< /headname >}}

{{< callout "info" >}}
FlyonUI is powered by <a href="https://preline.co/plugins/html/tree-view.html" target="_blank" class="link link-primary font-semibold">Preline’s</a> unstyled, headless Tailwind plugins to deliver accessible and responsive user interfaces.
{{< /callout >}}

<!-- Options table -->

{{< table >}}

PARAMETERS|DESCRIPTION|OPTIONS|DEFAULT VALUE
<span class="text-nowrap">`data-tree-view`</span>| Activate the Tree View by applying it to the element, and ensure it is added to the wrapper. | `-` | `-`
<span class="text-nowrap">`:controlBy`</span>| Informs the plugin of the active mode and handles events based on the selected mode. | `checkbox` / `button` | `button`
<span class="text-nowrap">`:autoSelectChildren`</span>| This option is available when the controlBy parameter is set to `checkbox` and the item is a directory `(isDir: true)`. When the item is selected, all nested items inherit the value of the parent. | boolean | `false`
<span class="text-nowrap">`:isIndeterminate`</span>| Applies an indeterminate visual style when the controlBy parameter is set to `checkbox`. | boolean | `true`
<span class="text-nowrap">`data-tree-view-item`</span>| Specifies the element within the initialized component that represents the item. This should be applied to the item itself. | `-` | `-`
<span class="text-nowrap">`:id`</span>| Optional. Desired identifier. | string | `-`
<span class="text-nowrap">`:value`</span>| The value that will be included in the resulting array. | string | `-`
<span class="text-nowrap">`:isDir`</span>| Determines that the element is a directory and handles it accordingly. | boolean | `false`
{{< /table >}}

<!-- Methods -->

{{< headname level="3" >}} Methods {{< /headname >}}

The `HSTreeView` object is contained within the global `window` object.

{{< table >}}
METHOD|DESCRIPTION
<span colspan="2" class="text-base-content font-semibold">PUBLIC METHODS</span>
`update()`| Update the element, particularly when rearranging the order of items.
`getSelectedItems()`| Returns a list of selected items.
`destroy()`| Destroys the instance, removes generated markup (if any), removes added classes and attributes.
<span colspan="2" class="text-base-content font-semibold">STATIC METHODS</span>
`HSTreeView.getInstance(target, isInstance)`|<div>Returns the element associated to the <code>target</code>.<ul class="m-0"><li><code>target</code> should be a Node or string (valid selector).</li><li><code>isInstance</code> boolean. Returns the instance instead of Node if <code>true</code>.</li></ul></div>
{{< /table >}}

<!-- Method usage -->

{{< headname level="4" >}} Method usage {{< /headname >}}

Below, we demonstrate how to use the update methods. Assign an ID to the `data-tree-view` as shown.

{{< code jsCode="true" addClass="justify-between flex-wrap" >}}

<div role="tree" id="tree-view-method" aria-orientation="vertical" data-tree-view>
  <div class="accordion-item active" role="treeitem" aria-expanded="true" id="cco-four-heading-one"
    data-tree-view-item='{
    "value": "assets",
    "isDir": true
  }'
  >
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="cco-four-collapse-one" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      assets
    </div>
    <div id="cco-four-collapse-one" class="accordion-content overflow-hidden px-2 transition-[height] duration-300" role="group" aria-labelledby="cco-four-heading-one" >
      <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
        data-tree-view-item='{
          "value": "image.jpg",
          "isDir": false
        }'
      >
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">image.jpg</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<hr />

<button class="btn btn-outline" id="get-items-btn">Log Selected</button>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    // Update Methods
    const treeView = HSTreeView.getInstance('#tree-view-method', true)
    const getItemsBtn = document.querySelector('#get-items-btn')

    getItemsBtn.addEventListener('click', () => {
      console.log(treeView.element.getSelectedItems())
    })
  })
</script>

{{< /code >}}

<p class="mt-10 mb-1.5 not-prose">Update Element</p>

{{< code-highlight lang="js" >}}const treeView = HSTreeView.getInstance('#tree-view-method', true);
const updateBtn = document.querySelector('#update-btn');

updateBtn.addEventListener('click', () => {
  treeView.element.update();
});
{{< /code-highlight >}}

<p class="mb-1.5 not-prose">Get selected items</p>

{{< code-highlight lang="js" >}}// This method is used in above example.
const treeView = HSTreeView.getInstance('#tree-view-method', true)
const getItemsBtn = document.querySelector('#get-items-btn')

getItemsBtn.addEventListener('click', () => {
  console.log(treeView.element.getSelectedItems())
})
{{< /code-highlight >}}

<p class="mb-1.5 not-prose" id="destroy-method">Destroy instance</p>

{{< code-highlight lang="js" >}}const treeView = document.querySelector('#tree-view-to-destroy')
const accordions = document.querySelectorAll('#tree-view-to-destroy .accordion-item')
const destroy = document.querySelector('#destroy-btn')

destroy.addEventListener('click', () => {
  const treeViewInstance = HSTreeView.getInstance(treeView, true)

  treeViewInstance.element.destroy()
  accordions.forEach(el => {
    const accordionInstance = HSAccordion.getInstance(el, true)

    accordionInstance.element.destroy()
  })
})
{{< /code-highlight >}}

<!-- Events -->

{{< headname level="3" >}} Events {{< /headname >}}

{{< table >}}
METHOD| DESCRIPTION | RETURNING VALUE
`on:click`| Called when any item was selected. | `{ id: string; value: string; isDir: boolean; path: string; isSelected: boolean; }`
{{< /table >}}

<!-- Event usage -->

{{< headname level="4" >}} Event usage {{< /headname >}}

Just like in the methods section, assign an ID to the `data-tree-view` in events. Click on the item, and observe the `console` output.

{{< code jsCode="true" addClass="justify-between flex-wrap" >}}

<div role="tree" id="tree-view-event" aria-orientation="vertical" data-tree-view>
  <div class="accordion-item active" role="treeitem" aria-expanded="true" id="cco-four-heading-one-alt"
    data-tree-view-item='{
    "value": "assets",
    "isDir": true
  }'
  >
    <div class="accordion-heading tree-view-selected:bg-base-300/40 flex w-full items-center gap-x-0.5 rounded-md py-0.5" >
      <button class="accordion-toggle btn btn-sm btn-circle btn-text" aria-expanded="true" aria-controls="cco-four-collapse-one" >
        <span class="icon-[tabler--plus] text-base-content/80 accordion-item-active:rotate-45 size-4 transition-all duration-300" ></span>
      </button>
      assets
    </div>
    <div id="cco-four-collapse-one" class="accordion-content overflow-hidden px-2 transition-[height] duration-300" role="group" aria-labelledby="cco-four-heading-one-alt" >
      <div class="tree-view-selected:bg-base-300/40 cursor-pointer rounded-md px-2" role="treeitem"
        data-tree-view-item='{
          "value": "image.jpg",
          "isDir": false
        }'
      >
        <div class="flex items-center gap-x-3">
          <span class="icon-[tabler--photo] text-base-content size-4 shrink-0"></span>
          <div class="grow">
            <span class="text-base-content">image.jpg</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Js -->
<script>
  window.addEventListener('load', function () {
    const el = HSTreeView.getInstance('#tree-view-event', true)

    el.element.on('click', data => {
      console.log('data', data)
    })
  })
</script>

{{< /code >}}

<p class="mt-12 mb-1.5 not-prose">When select changes event example.</p>

{{< code-highlight lang="js" >}}const el = HSTreeView.getInstance('#tree-view-event', true)

el.element.on('click', data => {
  console.log('data', data)
})
{{< /code-highlight >}}
