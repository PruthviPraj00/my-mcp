---
title: "Introduction"
description: "The easiest, free and open-source Tailwind CSS component library with semantic classes. 🚀"
bg_image: "svg/landing-page/flyonui-landing-logo.svg"
menu:
  main:
    parent: "getting-started"
    weight: 1

next: Quick start
nextLink: getting-started/quick-start/
---

{{< headsingle level="2" >}} What is FlyonUI? {{< /headsingle >}}

FlyonUI is designed to combine the best of both worlds: the aesthetic appeal of **semantic classes** and the powerful functionality of **JS plugins**.

Under the hood, it uses the strengths of:

- <a href="https://tailwindcss.com/" target="_blank" class="link link-primary font-semibold not-prose">Tailwind CSS</a>: A utility-first CSS framework that helps you build beautiful websites with ease.
- <a href="https://daisyui.com/" target="_blank" class="link link-primary font-semibold not-prose">daisyUI</a> adds component semantic class names to Tailwind CSS so you can make beautiful websites faster, easier and Maintainable.
- <a href="https://preline.co/plugins.html" target="_blank" class="link link-primary font-semibold not-prose">Preline</a> JavaScript headless & fully unstyled Tailwind plugins for accessible, responsive UI. Enhance experiences with animations, transitions, and more.

{{< headsingle level="2" >}} Why should I use FlyonUI? {{< /headsingle >}}

Using Tailwind CSS alone may lead to cluttered HTML with numerous utility classes, which can be a nightmare to maintain.

Apart from that Tailwind CSS or daisyUI doesn't provide any interactive headless JavaScript components like accordion, overlay, dropdowns, etc...

**This is where FlyonUI shines.✨**

FlyonUI brings together the beauty of **semantic classes** and the interactive **headless JavaScript plugins**, offering you a powerful toolkit to build stunning, interactive user interfaces with ease.

- **Beautiful and Semantic Styling:** Utilize comprehensive CSS components with semantic class names for a clean and readable codebase.
- **Interactive and Dynamic Features:** Incorporate Headless JavaScript plugins for ex: {{< link link="components/accordion/" addClass="link link-primary" >}}Accordion{{< /link >}}, {{< link link="overlays/dropdown/" addClass="link link-primary" >}}Dropdown{{< /link >}}, {{< link link="overlays/modal/" addClass="link link-primary" >}}Overlay{{< /link >}} etc... to add interactivity and dynamic behavior to your UI components.
- **Efficiency and Productivity:** Enjoy a faster and more efficient development process by combining the strengths of semantic classes and JS plugins.
- **Maintainable and Scalable:** Keep your projects maintainable and scalable with a consistent coding approach and powerful JS plugins.

**Features of FlyonUI:**
- **800+ Free Components & Examples:** Hundreds of component examples for all your WebApp needs that meet accessibility criteria.
- **Universal Framework Compatibility:** Fully compatible wherever Tailwind CSS is in action, from React to Vue and beyond.
- **Unstyled & Accessible Plugins:** Seamlessly add unstyled, accessible plugins for functionality without sacrificing design.
- **Unlimited Themes:** Customize your app's look and feel with FlyonUI's theming capabilities. Refer to the {{< link link="customization/themes/" addClass="link link-primary" >}}theme{{< /link >}} section for more details.
- **Responsive & RTL support :** Built with responsiveness in mind, ensuring your app looks great on all devices with RTL language support.
- **Free Forever:** Completely free forever, open-source, and built for the community.

**FlyonUI might not be the right fit for you if you:**

- Would rather invest time and resources creating everything from the ground up instead of focusing on delivering your project.
- Prefer spending time rebuilding common UI elements such as buttons, cards, checkboxes, and more from scratch for every project.
- Enjoy navigating through a sea of countless class names with no clear path in sight.
- Like turning your codebase into a chaotic puzzle, spending hours deciphering which code controls which UI component.

{{< headsingle level="2" >}} How does FlyonUI function? {{< /headsingle >}}
FlyonUI is an NPM package that seamlessly integrates into your project as a dev dependency. 

By adding it to your Tailwind CSS configuration as a plugin, you instantly gain access to FlyonUI's class names, which work just like any other Tailwind CSS utility—ready to use.

{{< headsingle level="2" >}} Why do we need another component library on top of daisyUI? {{< /headsingle >}}
Here are some key points addressing the need for another component library on top of daisyUI, like **FlyonUI**:

- **Additional JavaScript Support:** daisyUI is the most popular component library for Tailwind CSS, offering a wide range of components with semantic class names. But many projects require interactive features that need JavaScript.
- **Headless Architecture:** FlyonUI’s headless architecture allows developers to focus on functionality, providing greater flexibility when integrating components into any UI framework or design system.
- **Broader Component Set:** FlyonUI extends the component offering, with both UI elements and functional components that handle interactive behaviors like accordion, overlay, dropdowns, and carousels, etc.
- **Third-Party Component Support:** FlyonUI provides built-in support for popular third-party libraries like ApexCharts, FullCalendar, Flatpickr, and Toast, etc. This allows developers to extend their UIs with advanced features.


{{< headsingle level="2" >}} Does FlyonUI stay true to Tailwind CSS' utility-first approach? {{< /headsingle >}}
Absolutely! FlyonUI is designed to work seamlessly with Tailwind CSS while balancing both flexibility and speed. Tailwind's utility-first approach offers unmatched customization, but can sometimes lead to slower development and more verbose code. 

FlyonUI bridges this gap by providing ready-made, customizable components that speed up development without sacrificing control over design. You can quickly implement components for faster UI creation, while still using Tailwind CSS utilities for fine-tuning and personalizing every detail when needed—delivering the perfect balance of efficiency and flexibility.

{{< headsingle level="2" >}} Is FlyonUI really free to use? {{< /headsingle >}}
Yes, FlyonUI is completely free and open-source, released under the MIT license. 

You’re welcome to use it in any project, whether it’s for personal, commercial, or open-source purposes, with no hidden fees or limitations.

{{< headsingle level="2" >}} How can you contribute and support the growth of FlyonUI? {{< /headsingle >}}
Supporting FlyonUI is simple and meaningful! You can contribute in several ways:

- **Contribute Code or Features:** If you're a developer, feel free to contribute by improving components, adding new features, or fixing bugs. Every pull request helps make FlyonUI even better.
- **Star and Fork on GitHub:** A little recognition goes a long way. By starring the project or forking it to experiment, you help increase its visibility and foster community growth.
- **Spread the Word:** Share FlyonUI with fellow developers, designers, or teams who could benefit from it. The more people who know about it, the more it can grow and evolve.

By supporting FlyonUI, you’re contributing to a tool that’s designed to make web development easier and faster for everyone—your involvement helps shape its future!

{{< headsingle level="2" >}} Can FlyonUI be integrated with other UI frameworks seamlessly? {{< /headsingle >}}
While FlyonUI is designed to work seamlessly with Tailwind CSS, its flexible, utility-based components can be adapted for use with other UI frameworks. Whether you're working with React, Vue, or Angular, you can leverage FlyonUI's components and plugins by simply incorporating Tailwind into your setup.
