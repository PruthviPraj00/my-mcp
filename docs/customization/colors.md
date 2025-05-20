---
title: "Colors"
description: "Explore FlyonUI's color system with semantic classes and CSS variables."
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "customization"
    weight: 4

previous: Basic style
previousLink: customization/base/

next: Icons
nextLink: customization/icons/
---

<!-------------------- Overview -------------------->

{{< headsingle addClass="!mt-px" level="2" >}} Overview {{< /headsingle >}}

FlyonUI offers a robust and flexible color system that allows you to manage themes and colors seamlessly. Instead of relying on hard-coded utility color classes like:

- `bg-red-500`
- `bg-lime-500`
- `bg-fuchsia-500`

FlyonUI encourages the use of **semantic color utility classes** such as:

- `bg-primary`
- `bg-info`
- `bg-error`

These semantic classes simplify theme customization and management across multiple modes (e.g., dark or light themes). Each theme dynamically assigns colors to these classes via CSS variables, allowing your design to adapt effortlessly to theme changes.

<!-------------------- Why Use Semantic Color Naming? -------------------->

{{< headsingle level="2" >}} Why use semantic color naming? {{< /headsingle >}}

Using **semantic color names** provides a more organized, consistent approach to your design system. Instead of randomly picking colors for each component, you define a palette with specific roles (e.g., `primary`, `secondary`). This approach ensures:

- **Consistency:** Enforces a unified color palette across your UI.
- **Theming Flexibility:** Allows for seamless switching between themes, with colors automatically adapting through CSS variables.
- **Scalability:** Easily extend the system to support multiple themes (beyond just light and dark) by simply modifying a few CSS variables.

Benifts of the semantic color naming:

{{< table >}}
Traditional Color Approach | FlyonUI Semantic Colors
❌ `bg-[#1a73e8]` or `bg-blue-500` (Static values) | ✅  `bg-primary` (Dynamic, context-aware values)
🔧 Requires separate dark mode classes (`dark:bg-blue-700`) | 🎨 Automatic theme adaptation with a single class
⚠️ Theme changes require updating multiple color values | 🔄 Update one CSS variable to change the entire theme
📝 Verbose class names for different states | 🎯 Consistent, semantic naming across states
🔍 Hard to maintain color consistency | 🎪 Built-in design system compliance
⏱️ More development time managing colors | ⚡ Rapid development with semantic classes
🔒 Limited to explicit color definitions | 🌈 Flexible theming system with unlimited possibilities
{{< /table >}}

<!-------------------- Available Color Options in FlyonUI -------------------->

{{< headsingle level="2" >}} Available color options in FlyonUI {{< /headsingle >}}

FlyonUI provides a comprehensive list of color options, which can be used either within themes or as utility classes. Below is a table of available color options, along with examples of how to use them.


<div class="not-prose border-base-content/10 rounded-box w-full overflow-x-auto border">
  <table class="table">
    <thead>
      <tr>
        <th class="w-1/4">Color</th>
        <th>CSS Variable</th>
        <th>Description</th>
        <th>Example Usage</th>
      </tr>
    </thead>
    <tbody class="**:[:nth-child(3)]:text-wrap">
    <!-- Primary Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-primary border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span>Primary</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-primary)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Main color used to represent your brand or core actions.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-primary</span>
        </td>
      </tr>
      <!-- Primary Content Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-primary-content border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Primary Content</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-primary-content)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Foreground color used on top of the primary background color for contrast.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">text-primary-content</span>
        </td>
      </tr>
      <!-- Secondary Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-secondary border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span>Secondary</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-secondary)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">A complementary accent color, typically used to support the primary color.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-secondary</span>
        </td>
      </tr>
      <!-- Secondary Content Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-secondary-content border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Secondary Content</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-secondary-content)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Used for text and content on the secondary background color for good contrast.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">text-secondary-content</span>
        </td>
      </tr>
      <!-- Accent Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-accent border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span>Accent</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-accent)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Used for highlighting key UI elements or drawing attention to specific actions.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-accent</span>
        </td>
      </tr>
      <!-- Accent Content Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-accent-content border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Accent Content</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-accent-content)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Used for text and content that sits over the accent background color for contrast.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">text-accent-content</span>
        </td>
      </tr>
      <!-- Neutral Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-neutral border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span>Neutral</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-neutral)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">A neutral background color, used for less prominent elements or surfaces.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-neutral</span>
        </td>
      </tr>
      <!-- Neutral Content Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-neutral-content border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Neutral Content</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-neutral-content)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Used for text and content on neutral backgrounds to ensure legibility.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">text-neutral-content</span>
        </td>
      </tr>
      <!-- Base 100 Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-base-100 border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Base 100</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-base-100)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">The lightest surface color, ideal for general backgrounds and page content.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-base-100</span>
        </td>
      </tr>
      <!-- Base 200 Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-base-200 border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Base 200</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-base-200)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">A slightly darker shade, typically used for sections or elements with elevated backgrounds.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-base-200</span>
        </td>
      </tr>
      <!-- Base 300 Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-base-300 border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Base 300</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-base-300)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Used for darker elements or deeper shadow effects to create elevation.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">shadow-base-300</span>
        </td>
      </tr>
      <!-- Base Content Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-base-content border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Base Content</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-base-content)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Foreground color for elements sitting on base color backgrounds.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">text-base-content</span>
        </td>
      </tr>
      <!-- Info Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-info border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span>Info</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-info)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Used for informational messages or helpful tips within the UI.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-info</span>
        </td>
      </tr>
      <!-- Info Content Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-info-content border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Info Content</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-info-content)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Text color to use on top of the info background for good visibility.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">text-info-content</span>
        </td>
      </tr>
      <!-- Success Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-success border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span>Success</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-success)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Indicates success or a positive state, often used in success messages or actions.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-success</span>
        </td>
      </tr>
      <!-- Success Content Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-success-content border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Success Content</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-success-content)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Used for content and text over success backgrounds to maintain readability.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">text-success-content</span>
        </td>
      </tr>
      <!-- Warning Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-warning border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span>Warning</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-warning)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Used for alerting the user to potential issues or warnings.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-warning</span>
        </td>
      </tr>
      <!-- Warning Content Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-warning-content border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Warning Content</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-warning-content)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Content color for text or icons on top of warning backgrounds for visibility.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">text-warning-content</span>
        </td>
      </tr>
      <!-- Error Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-error border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span>Error</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-error)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Indicates error or danger messages, typically used for alerts or destructive actions.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">bg-error</span>
        </td>
      </tr>
      <!-- Error Content Color -->
      <tr>
        <td>
          <p class="font-medium flex gap-3"><span class="bg-error-content border-base-content/10 size-5 rounded-full border p-0 shrink-0"></span> Error Content</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">var(--color-error-content)</span>
        </td>
        <td>
          <p class="text-base-content/80 text-sm">Content color for text and elements placed over the error background.</p>
        </td>
        <td>
          <span class="badge badge-soft badge-sm rounded-full text-nowrap">text-error-content</span>
        </td>
      </tr>
    </tbody>
  </table>
</div>



<!-------------------- How to Apply FlyonUI Colors -------------------->

{{< headsingle level="2" >}} How to apply FlyonUI colors? {{< /headsingle >}}

FlyonUI components come with predefined color utility classes. To apply colors to your components, simply use one of these classes:

```html
<span class="badge badge-primary">Badge</span>
```

<p class="not-prose my-4">Or for input elements:</p>

```html
<input type="radio" class="radio radio-primary" />
```

<!-------------------- Available Utility Classes -------------------->

{{< headsingle level="2" >}} Available utility classes {{< /headsingle >}}

FlyonUI's color utilities follow a similar pattern to Tailwind's default color utilities. You can easily apply colors to various aspects of your UI using the following syntax:
<!-- //TODO - if we support cdn then update this and added cdn like like daisyui -->
{{< table >}}
CSS Class
bg-{COLOR_NAME}
text-{COLOR_NAME}
border-{COLOR_NAME}
from-{COLOR_NAME}
via-{COLOR_NAME}
to-{COLOR_NAME}
ring-{COLOR_NAME}
fill-{COLOR_NAME}
stroke-{COLOR_NAME}
shadow-{COLOR_NAME}
outline-{COLOR_NAME}
divide-{COLOR_NAME}
accent-{COLOR_NAME}
caret-{COLOR_NAME}
decoration-{COLOR_NAME}
placeholder-{COLOR_NAME}
ring-offset-{COLOR_NAME}
{{< /table >}}

<p class="not-prose my-4">For example:</p>

- **Background color**: `bg-primary`
- **Text color**: `text-secondary`
- **Border color**: `border-accent`
- **Shadow color**: `shadow-primary`

With this system, you can easily apply semantic colors throughout your UI, making theme switching and color management intuitive and scalable.
