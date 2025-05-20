---
title: "List"
description: "Create attractive lists using Tailwind CSS, a potent tool for styling lists, improving readability, and enhancing user experience."
bg_image: "svg/content/list.svg"
components: 1
menu:
  main:
    parent: "content"

previous: Link
previousLink: link/

next: Mask
nextLink: content/mask/
---

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- List style type -->

{{< headname level="3" >}} List style type {{< /headname >}}

Utilize the `list-disc` class for bulleted lists and the `list-decimal` class for numeric lists. For further information, consult the Tailwind documentation on <a href="https://tailwindcss.com/docs/list-style-type" target="_blank" class="link link-primary">List Style Type</a>.

{{< code addClass="flex-col" >}}

<h5 class="text-base-content text-lg">List decimal</h5>
<ol class="list-inside list-decimal">
  <li class="mb-2">Start by signing up for our newsletter.</li>
  <li class="mb-2">Explore our collection of articles and tutorials.</li>
  <li class="mb-2">Join our community forums to connect with like-minded individuals.</li>
</ol>

<h5 class="text-base-content text-lg">List disc</h5>
<ul class="list-inside list-disc">
  <li class="mb-2">Benefits of regular exercise:</li>
  <li class="mb-2">Healthy weight maintenance</li>
  <li class="mb-2">Improved mood and mental health</li>
</ul>

<h5 class="text-base-content text-lg">List none</h5>
<ul class="list-inside list-none">
  <li class="mb-2">Essential items for a hiking trip:</li>
  <li class="mb-2">Backpack with proper support</li>
  <li class="mb-2">Water bottle or hydration pack</li>
</ul>
{{< /code >}}

<!-------------------- List Style -------------------->

{{< headname level="2" >}} List Style {{< /headname >}}

<!-- Position -->

{{< headname level="3" >}} Position {{< /headname >}}

Utilize the `list-inside` and `list-outside` utility classes to manage the position of list markers and text indentation
within a list. Refer to the Tailwind documentation on <a href="https://tailwindcss.com/docs/list-style-position" target="_blank" class="link link-primary">List Style Position</a> for more details.

<!-- List inside -->

{{< headname level="4" >}} List inside {{< /headname >}}

This example uses `list-inside`.

{{< code addClass="flex-col" >}}

<h5 class="text-base-content text-lg">List inside</h5>
<ul class="list-inside list-disc">
  <li class="mb-2">"Harry Potter and the Sorcerer's Stone" by J.K. Rowling</li>
  <li class="mb-2">"To Kill a Mockingbird" by Harper Lee</li>
  <li class="mb-2">"The Great Gatsby" by F. Scott Fitzgerald</li>
</ul>
{{< /code >}}

<!-- List outside -->

{{< headname level="4" >}}List outside {{< /headname >}}

This example uses `list-outside`.

{{< code addClass="flex-col">}}

<h5 class="text-base-content text-lg ms-4">List outside</h5>
<ul class="list-outside list-disc ms-4">
  <li class="mb-2">Rio de Janeiro, Brazil</li>
  <li class="mb-2">Paris, France</li>
  <li class="mb-2">Kyoto, Japan</li>
</ul>
{{< /code >}}

<!-- List image -->

{{< headname level="3" >}} List image {{< /headname >}}

Utilize the `list-image-[url(svg-url)]` utilities to manage the marker image for list items. Refer to the Tailwind documentation on
<a href="https://tailwindcss.com/docs/list-style-image" target="_blank" class="link link-primary">List Style Image</a>
for more details.

{{< code addClass="flex-col" >}}

<ul class="text-base-content/80 list-inside list-image-[url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTIiIHZpZXdCb3g9IjAgMCAxNCAxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSIjMzhiZGY4Ij48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMy42ODUuMTUzYS43NTIuNzUyIDAgMCAxIC4xNDMgMS4wNTJsLTggMTAuNWEuNzUuNzUgMCAwIDEtMS4xMjcuMDc1bC00LjUtNC41YS43NS43NSAwIDAgMSAxLjA2LTEuMDZsMy44OTQgMy44OTMgNy40OC05LjgxN2EuNzUuNzUgMCAwIDEgMS4wNS0uMTQzWiIgLz48L3N2Zz4=)]" >
  <li class="mb-2">Mumbai, India</li>
  <li class="mb-2">Paris, France</li>
  <li class="mb-2">Kyoto, Japan</li>
  <li class="mb-2">Rio de Janeiro, Brazil</li>
</ul>
{{< /code >}}

<!-------------------- Custom Marker -------------------->

{{< headname level="2" >}} Custom Marker {{< /headname >}}

<!-- Arrow style -->

{{< headname level="3" >}} Arrow style {{< /headname >}}

This showcases the process of incorporating a custom marker with various styles. Although it presently displays the primary color, the color
can be adjusted as needed.

<!-- Solid color -->

{{< headname level="4" >}}Solid color {{< /headname >}}

Illustration of a solid color example.

{{< code >}}

<ul class="space-y-3 text-sm">
  <li class="flex items-center space-x-3">
    <span class="bg-primary text-primary-content flex items-center justify-center rounded-full p-1">
      <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
    </span>
    <span class="text-base-content/80"> Product Overview </span>
  </li>
  <li class="flex items-center space-x-3">
    <span class="bg-primary text-primary-content flex items-center justify-center rounded-full p-1">
      <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
    </span>
    <span class="text-base-content/80"> Installation Guide </span>
  </li>
  <li class="flex items-center space-x-3">
    <span class="bg-primary text-primary-content flex items-center justify-center rounded-full p-1">
      <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
    </span>
    <span class="text-base-content/80"> Troubleshooting Tips </span>
  </li>
</ul>
{{< /code >}}

<!-- Soft color -->

{{< headname level="4" >}}Soft color {{< /headname >}}

Illustration of a soft color example.

{{< code >}}

<ul class="space-y-3 text-sm">
  <li class="flex items-center space-x-3">
    <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
      <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
    </span>
    <span class="text-base-content/80"> Product Overview </span>
  </li>
  <li class="flex items-center space-x-3">
    <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
      <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
    </span>
    <span class="text-base-content/80"> Installation Guide </span>
  </li>
  <li class="flex items-center space-x-3">
    <span class="bg-primary/20 text-primary flex items-center justify-center rounded-full p-1">
      <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
    </span>
    <span class="text-base-content/80"> Troubleshooting Tips </span>
  </li>
</ul>
{{< /code >}}

<!-- Outline style -->

{{< headname level="4" >}}Outline style {{< /headname >}}

An instance showcasing an outline example.

{{< code >}}

<ul class="space-y-3 text-sm">
  <li class="flex items-center space-x-3">
    <span class="border-primary text-primary flex items-center justify-center rounded-full border p-0.5">
      <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
    </span>
    <span class="text-base-content/80"> FAQ </span>
  </li>
  <li class="flex items-center space-x-3">
    <span class="border-primary text-primary flex items-center justify-center rounded-full border p-0.5">
      <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
    </span>
    <span class="text-base-content/80"> Installation Guide </span>
  </li>
  <li class="flex items-center space-x-3">
    <span class="border-primary text-primary flex items-center justify-center rounded-full border p-0.5">
      <span class="icon-[tabler--arrow-right] size-4 rtl:rotate-180"></span>
    </span>
    <span class="text-base-content/80"> Troubleshooting Tips </span>
  </li>
</ul>
{{< /code >}}

<!-------------------- Description list -------------------->

{{< headname level="2" >}} Description list {{< /headname >}}

<!-- Description list example  -->

{{< headname level="3" >}} Description list example {{< /headname >}}

Basic Description list example.

{{< code >}}

<div>
  <div class="px-4 sm:px-0">
    <h3 class="text-2xl font-semibold text-base-content">Product Information</h3>
    <p class="mt-1 max-w-full text-base-content/80">Details of the latest product release.</p>
  </div>
  <div class="mt-6 border-t border-base-content/25">
    <dl class="divide-y divide-base-content/25">
      <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0 text-base">
        <dt class="font-medium text-base-content">Product Name</dt>
        <dd class="mt-1  text-base-content/80 sm:col-span-2 sm:mt-0">FlyonUI Django</dd>
      </div>
      <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0 text-base">
        <dt class="font-medium text-base-content">Category</dt>
        <dd class="mt-1  text-base-content/80 sm:col-span-2 sm:mt-0">Admin template</dd>
      </div>
      <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0 text-base">
        <dt class="font-medium text-base-content">Release Date</dt>
        <dd class="mt-1  text-base-content/80 sm:col-span-2 sm:mt-0">March 15, 2024</dd>
      </div>
      <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0 text-base">
        <dt class="font-medium text-base-content">Price</dt>
        <dd class="mt-1  text-base-content/80 sm:col-span-2 sm:mt-0">$499</dd>
      </div>
      <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0 text-base">
        <dt class="font-medium text-base-content">Description</dt>
        <dd class="mt-1  text-base-content/80 sm:col-span-2 sm:mt-0">
          The <span class="font-semibold text-base-content">FlyonUI – Bootstrap Django Admin Dashboard Template</span> – is the most developer friendly & highly customizable Admin Dashboard Template based on Bootstrap 5.
        </dd>
      </div>
      <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0 text-base">
        <dt class="font-medium text-base-content">Documents</dt>
        <dd class="mt-2 text-base-content sm:col-span-2 sm:mt-0">
          <ul role="list" class="divide-y divide-base-content/25 rounded-md border border-base-content/25">
            <li class="flex items-center justify-between py-4 ps-4 pe-5">
              <div class="flex w-0 flex-1 items-center">
                <span class="icon-[tabler--paperclip] size-5 shrink-0"></span>
                <div class="ms-4 flex min-w-0 flex-1 gap-2">
                  <span class="truncate font-medium">FlyonUI_Pro_User_Manual.pdf</span>
                  <span class="shrink-0 text-base-content/50">3.2mb</span>
                </div>
              </div>
              <div class="ms-4 shrink-0">
                <a href="#" class="link link-primary">Download</a>
              </div>
            </li>
            <li class="flex items-center justify-between py-4 ps-4 pe-5">
              <div class="flex w-0 flex-1 items-center">
                <span class="icon-[tabler--paperclip] size-5 shrink-0"></span>
                <div class="ms-4 flex min-w-0 flex-1 gap-2">
                  <span class="truncate font-medium">FlyonUI_Pro_Installation_Guide.pdf</span>
                  <span class="shrink-0 text-base-content/50">5.1mb</span>
                </div>
              </div>
              <div class="ms-4 shrink-0">
                <a href="#" class="link link-primary">Download</a>
              </div>
            </li>
          </ul>
        </dd>
      </div>
    </dl>
  </div>
</div>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Marker -->

{{< headname level="3" >}} Marker {{< /headname >}}

Tailwind offers the `marker:` modifier, allowing us to adjust the color of markers. Refer to the Tailwind documentation
on <a href="https://tailwindcss.com/docs/hover-focus-and-other-states#list-markers" target="_blank" class="link link-primary">Marker</a> for more details.

{{< code addClass="flex-col" >}}

<ul class="list-inside list-disc marker:text-purple-500">
  <li class="mb-2">"Harry Potter and the Sorcerer's Stone" by J.K. Rowling</li>
  <li class="mb-2">"To Kill a Mockingbird" by Harper Lee</li>
  <li class="mb-2">"The Great Gatsby" by F. Scott Fitzgerald</li>
</ul>
<ul class="list-inside list-decimal marker:text-purple-500">
  <li class="mb-2">"Harry Potter and the Sorcerer's Stone" by J.K. Rowling</li>
  <li class="mb-2">"To Kill a Mockingbird" by Harper Lee</li>
  <li class="mb-2">"The Great Gatsby" by F. Scott Fitzgerald</li>
</ul>
{{< /code >}}

<!-- Separator -->

{{< headname level="3" >}} Separator {{< /headname >}}

A basic form of the inline list with dotted separator.

{{< code >}}

<ul class="flex list-inside list-disc gap-3 marker:text-neutral-300">
  <li class="list-none text-nowrap">Product</li>
  <li class="text-nowrap">Pro Tips</li>
  <li class="text-nowrap">Install Guide</li>
</ul>
{{< /code >}}
