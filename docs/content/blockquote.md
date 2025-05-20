---
title: "Blockquote"
description: "The blockquote component serves as a tool to incorporate quoted text from an external source, ideal for testimonials, reviews, and quotes within an article."
bg_image: "svg/content/blockquote.svg"
components: 3
menu:
  main:
    parent: "content"

previous: Theme Generator
previousLink: customization/theme-generator/

next: Divider
nextLink: content/divider/
---

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Default -->

{{< headname level="3" >}} Default {{< /headname >}}

Basic blockquote example.

{{< code >}}

<blockquote class="relative p-4">
  <span class="icon-[tabler--quote] text-base-300/20 absolute -start-3 -top-3 size-16 rotate-180 rtl:rotate-0"></span>

  <div class="relative z-1">
    <p class="text-base-content text-lg">
      <em>
        The blockquote element is ideal for showcasing well-known quotes within content. It's commonly used for
        testimonials, reviews, and notable quotes in articles.
      </em>
    </p>
  </div>
</blockquote>
{{< /code >}}

<!-------------------- Alignment -------------------->

{{< headname level="2" >}} Alignment {{< /headname >}}

<!-- Center align -->

{{< headname level="3" >}} Center align {{< /headname >}}

An example of a centered blockquote.

{{< code >}}

<blockquote class="relative mx-auto p-4 text-center">
  <span class="icon-[tabler--quote] text-base-300/20 absolute -top-3 start-2 size-16 rotate-180 rtl:rotate-0"></span>

  <div class="relative z-1">
    <p class="text-base-content text-lg">
      <em>
        The blockquote element is ideal for showcasing well-known quotes within content. It's commonly used for
        testimonials, reviews, and notable quotes in articles.
      </em>
    </p>
  </div>
</blockquote>
{{< /code >}}

<!-- Right align -->

{{< headname level="3" >}} Right align {{< /headname >}}

An example of a end blockquote.

{{< code >}}

<blockquote class="relative ms-auto p-4 text-end">
  <span class="icon-[tabler--quote] text-base-300/20 absolute -top-3 start-6 size-16 rotate-180 rtl:rotate-0"></span>

  <div class="relative z-1">
    <p class="text-base-content text-lg">
      <em>
        The blockquote element is ideal for showcasing well-known quotes within content. It's commonly used for
        testimonials, reviews, and notable quotes in articles.
      </em>
    </p>
  </div>
</blockquote>
{{< /code >}}

<!-------------------- Illustrations -------------------->

{{< headname level="2" >}} Illustrations {{< /headname >}}

<!-- Naming a source -->

{{< headname level="3" >}} Naming a source {{< /headname >}}

Labeling a source with a name.

{{< code >}}

<blockquote class="relative p-4">
  <span class="icon-[tabler--quote] text-base-300/20 absolute -start-3 -top-3 size-16 rotate-180 rtl:rotate-0"></span>

  <div class="relative z-1">
    <p class="text-base-content text-lg">
      <em>
        The blockquote element is ideal for showcasing well-known quotes within content. It's commonly used for
        testimonials, reviews, and notable quotes in articles.
      </em>
    </p>
  </div>
  <footer class="mt-4">
    <div class="text-base-content/50 text-base font-semibold">~ Shamus Tuttle</div>
  </footer>
</blockquote>
{{< /code >}}

<!-- With avatar -->

{{< headname level="3" >}} With avatar {{< /headname >}}

Labeling a source with an avatar.

{{< code >}}

<blockquote class="relative p-4">
  <span class="icon-[tabler--quote] text-base-300/20 absolute -start-3 -top-3 size-16 rotate-180 rtl:rotate-0"></span>

  <div class="relative z-1">
    <p class="text-base-content text-lg">
      <em>
        The blockquote element is ideal for showcasing well-known quotes within content. It's commonly used for
        testimonials, reviews, and notable quotes in articles.
      </em>
    </p>
  </div>
  <footer class="mt-4 flex items-center">
    <div class="avatar">
      <div class="size-10 rounded-full">
        <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
      </div>
    </div>
    <div class="ms-4">
      <div class="text-base-content text-base font-semibold">Shamus Tuttle</div>
      <div class="text-base-content/50 text-xs">Source title</div>
    </div>
  </footer>
</blockquote>
{{< /code >}}
