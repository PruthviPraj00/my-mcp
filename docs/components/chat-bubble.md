---
title: "Chat Bubble"
components: 4
description: "Chat bubbles are ideal for organizing conversations in messaging apps, chats, social media platforms, and similar spaces."
bg_image: "svg/components/chat-bubble.svg"
menu:
  main:
    parent: "components"

previous: Carousel
previousLink: components/carousel/

next: Collapse
nextLink: components/collapse/
---

<!-- Class Table -->

{{< class-table >}}
chat | component | The class for the chat container which contains the chat bubbles.
chat-bubble | part | For the content of chat.
chat-avatar | part | For display avatar of the sender or receiver.
chat-header | part | For the header of the chat bubble.
chat-footer | part | For the footer of the chat bubble.
chat-receiver | modifier | For the chat bubble of the receiver.
chat-sender | modifier | For the chat bubble of the sender.
{{< /class-table >}}

<!-------------------- Basic example -------------------->

{{< headname level="2" >}} Basic example {{< /headname >}}

<!-- Chat start and chat end -->

{{< headname level="3" >}} Chat receiver and chat sender {{< /headname >}}

Assign the `chat-receiver` class to the receiver’s chat bubble and the `chat-sender` class to the sender’s chat bubble.

{{< code addClass="!block bg-base-200/60" >}}

<div class="chat chat-receiver">
  <div class="chat-bubble">Just booked tickets for our vacation!</div>
</div>
<div class="chat chat-sender">
  <div class="chat-bubble">Awesome! I can't wait!</div>
</div>
{{< /code >}}

<!-------------------- Illustration -------------------->

{{< headname level="2" >}} Illustration {{< /headname >}}

<!-- Chat with avatar -->

{{< headname level="3" >}} Chat with avatar {{< /headname >}}

Apply the `chat-avatar` class to show the avatar of either the sender or the receiver.

{{< code addClass="!block bg-base-200/60" >}}

<div class="chat chat-receiver">
  <div class="chat-avatar avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
    </div>
  </div>
  <div class="chat-bubble">I finally finished the marathon!</div>
</div>
<div class="chat chat-sender">
  <div class="chat-avatar avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="avatar" />
    </div>
  </div>
  <div class="chat-bubble">Wow, that's incredible! I'm so proud of you!</div>
</div>
{{< /code >}}

<!-- Chat with header -->

{{< headname level="3" >}} Chat with header {{< /headname >}}

Apply the `chat-header` class to incorporate a header into the chat bubble.

{{< code addClass="!block bg-base-200/60">}}

<div class="chat chat-receiver">
  <div class="chat-header text-base-content">
    Obi-Wan Kenobi
    <time class="text-base-content/50">12:45</time>
  </div>
  <div class="chat-bubble">I aced my final exams!</div>
</div>
<div class="chat chat-sender">
  <div class="chat-header text-base-content">
    Anakin
    <time class="text-base-content/50">12:46</time>
  </div>
  <div class="chat-bubble">Fantastic news! You worked so hard for it!</div>
</div>
{{< /code >}}

<!-- Chat with footer -->

{{< headname level="3" >}} Chat with footer {{< /headname >}}

Apply the `chat-footer` class to incorporate a footer into the chat bubble.

{{< code addClass="!block bg-base-200/60">}}

<div class="chat chat-receiver">
  <div class="chat-bubble">Just finished my first painting!</div>
  <div class="chat-footer text-base-content/50">
    <div>Delivered</div>
  </div>
</div>
<div class="chat chat-sender">
  <div class="chat-bubble">That’s amazing! I’d love to see it!</div>
  <div class="chat-footer text-base-content/50">
    Seen
    <span class="icon-[tabler--checks] text-success align-bottom"></span>
  </div>
</div>
{{< /code >}}

<!-- Chat with avatar, header and footer -->

{{< headname level="3" >}} Chat with avatar, header and footer {{< /headname >}}

Here's an example of a chat bubble that includes an avatar, header, and footer.

{{< code addClass="!block bg-base-200/60 ">}}

<div class="chat chat-receiver">
  <div class="chat-avatar avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png" alt="avatar" />
    </div>
  </div>
  <div class="chat-header text-base-content">
    Obi-Wan Kenobi
    <time class="text-base-content/50">12:45</time>
  </div>
  <div class="chat-bubble">I started learning guitar today!</div>
  <div class="chat-footer text-base-content/50">
    <div>Delivered</div>
  </div>
</div>
<div class="chat chat-sender">
  <div class="chat-avatar avatar">
    <div class="size-10 rounded-full">
      <img src="https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png" alt="avatar" />
    </div>
  </div>
  <div class="chat-header text-base-content">
    Anakin
    <time class="text-base-content/50">12:46</time>
  </div>
  <div class="chat-bubble">That's awesome! You're going to be great at it!</div>
  <div class="chat-footer text-base-content/50">
    Seen
    <span class="icon-[tabler--checks] text-success align-bottom"></span>
  </div>
</div>
{{< /code >}}

<!-- Chat with image -->

{{< headname level="3" >}} Chat with image {{< /headname >}}

This is an example of a chat bubble featuring an image.

{{< code addClass="!block bg-base-200/60">}}

<div class="chat chat-sender">
  <div class="chat-bubble">
    <div class="flex flex-col gap-4">
      Check out my new watch! 🤩
      <button class="border-base-content/30 w-52 overflow-hidden rounded-md border" aria-label="Image Button">
        <img class="w-full" src="https://cdn.flyonui.com/fy-assets/components/card/image-9.png" alt="Watch Image" />
      </button>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Chat with image gallery -->

{{< headname level="3" >}} Chat with image gallery {{< /headname >}}

The following example demonstrates a chat bubble containing multiple images sent or received.

{{< code addClass="!block bg-base-200/60">}}

<div class="chat chat-sender">
  <div class="chat-bubble">
    Places on my bucket list. 🤩
    <div class="mt-4 grid h-36 w-56 grid-cols-2 gap-2 max-sm:w-52">
      <button class="border-base-content/30 overflow-hidden rounded-md border" aria-label="River Image Button">
        <img class="h-full" src="https://cdn.flyonui.com/fy-assets/components/carousel/image-5.png" alt="River Image" />
      </button>
      <button class="border-base-content/30 overflow-hidden rounded-md border" aria-label="Desert Image Button">
        <img class="h-full" src="https://cdn.flyonui.com/fy-assets/components/carousel/image-1.png" alt="Desert Image" />
      </button>
      <button class="border-base-content/30 overflow-hidden rounded-md border" aria-label="Mountain Image Button">
        <img class="h-full" src="https://cdn.flyonui.com/fy-assets/components/carousel/image-20.png" alt="Mountain Image" />
      </button>
      <div class="border-base-content/30 relative overflow-hidden rounded-md border" aria-label="More Images Button">
        <button class="bg-base-content/60 absolute flex size-full items-center justify-center">
          <span class="text-base-100 text-sm font-semibold">+5</span>
        </button>
        <img src="https://cdn.flyonui.com/fy-assets/components/carousel/image-21.png" class="h-full" alt="Lake Image" />
      </div>
    </div>
  </div>
</div>
{{< /code >}}

<!-- Chat with file attachment -->

{{< headname level="3" >}} Chat with file attachment {{< /headname >}}

Here's an example of a chat bubble with a file attachment.

{{< code addClass="!block bg-base-200/60">}}

<div class="chat chat-sender">
  <div class="chat-bubble">
    <div class="flex flex-col gap-4">
      FlyonUI documentation file 📁
      <div class="bg-base-100 rounded-md">
        <button class="flex items-center gap-2 px-3 py-2 max-sm:w-11/12">
          <div class="flex flex-col gap-2 max-sm:w-5/6">
            <div class="flex items-center">
              <span class="icon-[tabler--file-type-pdf] text-error me-2 size-5"></span>
              <span class="text-base-content/80 truncate font-medium">documentation.pdf</span>
            </div>
            <div class="text-base-content flex items-center gap-1 text-xs max-sm:hidden">
              12 Pages
              <span class="icon-[tabler--circle-filled] mt-0.5 size-1.5"></span>
              18 MB
              <span class="icon-[tabler--circle-filled] mt-0.5 size-1.5"></span>
              PDF
            </div>
          </div>
          <span class="btn btn-text btn-circle">
            <span class="icon-[tabler--download] size-5"></span>
          </span>
        </button>
      </div>
    </div>
  </div>
</div>
{{< /code >}}
