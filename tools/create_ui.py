from typing import Dict, List, Any, Union
import mcp.types as types


def register_tool(app):
    """
    Register the create-ui tool with the MCP server
    
    Args:
        app: The MCP server instance
    """
    @app.list_tools()
    async def list_tools() -> List[types.Tool]:
        return [
            types.Tool(
                name="create-ui",
                description="Generate UI components based on user requirements using FlyonUI. Use this tool when the user requests a new UI component—e.g., mentions /fy, /ui, or asks for a button, input, dialog, table, form, banner, card, or other FlyonUI component.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "description": {
                            "type": "string",
                            "description": "Detailed description of the UI component to generate",
                        },
                        "components": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of specific FlyonUI components to include (optional)",
                        },
                    },
                    "required": ["description"],
                },
                annotations={
                    "title": "Create UI Component",
                    "readOnlyHint": True,
                    "openWorldHint": False,
                },
            )
        ]


    @app.call_tool()
    async def call_tool(
        name: str, arguments: Dict[str, Any]
    ) -> List[Union[types.TextContent, types.ImageContent, types.EmbeddedResource]]:
        if name == "create-ui":
            # Import here to avoid circular imports
            from main import search_docs, ALL_COMPONENT_NAMES
            
            description = arguments.get("description", "")
            components = arguments.get("components", [])

            # Check if the description starts with /fy or /ui and remove the prefix
            if description.startswith("/fy "):
                description = description[4:]
            elif description.startswith("/fy"):
                description = description[3:]
            elif description.startswith("/ui "):
                description = description[4:]
            elif description.startswith("/ui"):
                description = description[3:]

            # Identify potential components from the description
            potential_components = []

            # Check for component mentions using ALL_COMPONENT_NAMES
            for component in ALL_COMPONENT_NAMES:
                # Skip non-component files like introduction, license, etc.
                if component in ["introduction", "license", "quick-start", "javascript"]:
                    continue

                # Replace hyphens with spaces for natural language matching
                component_name = component.replace("-", " ")

                # Check if component is mentioned in the description
                if (
                    component_name in description.lower()
                    or component in description.lower()
                ):
                    potential_components.append(component)

            # Add any explicitly mentioned components
            for component in components:
                if component not in potential_components:
                    potential_components.append(component)

            # Search for relevant documentation
            search_query = description
            # Add identified components to the search query
            if potential_components:
                search_query += " " + " ".join(potential_components)
            # Add explicitly specified components
            if components:
                search_query += " " + " ".join(components)

            doc_results = search_docs(search_query)

            # Prepare the response with relevant documentation
            response_text = "# FlyonUI Component Generation\n\n"
            response_text += f"## User Request\n{description}\n\n"

            response_text += "## Relevant Documentation\n\n"

            # Include more documentation results for complex component combinations
            # Determine how many docs to include based on potential components identified
            max_docs = max(5, len(potential_components))
            for i, result in enumerate(doc_results[:max_docs]):
                component_name = result["component"].replace("-", " ").title()
                response_text += f"### {component_name}\n"

                # Extract the most relevant part of the documentation
                doc_content = result["content"]
                
                # Extract key information from documentation
                # Get the component name and add it to the response
                title_start = doc_content.find("# ")
                if title_start != -1:
                    title_end = doc_content.find("\n\n", title_start)
                    if title_end != -1:
                        response_text += doc_content[title_start:title_end] + "\n\n"
                    else:
                        # If we can't find the end, just take a reasonable chunk
                        response_text += doc_content[title_start:title_start+100] + "\n\n"
                
                # Include a brief description if available
                p_start = doc_content.find("p:\n  - ")
                if p_start != -1:
                    p_end = doc_content.find("\n\n", p_start)
                    if p_end != -1:
                        description_text = doc_content[p_start:p_end].replace("p:\n  - ", "")
                        response_text += f"{description_text}\n\n"
                
                # Try to find the table with class names and descriptions (most important part)
                table_start = doc_content.find("| Class Name | Type | Description |")
                if table_start != -1:
                    # Find where the table ends (next heading or paragraph)
                    table_end = doc_content.find("\n\nh", table_start)
                    if table_end == -1:
                        table_end = doc_content.find("\n\np", table_start)
                    if table_end == -1:
                        table_end = len(doc_content)
                    
                    # Include the table of class names and descriptions
                    table_content = doc_content[table_start:table_end]
                    
                    # Only include rows relevant to the request to keep it concise
                    table_rows = table_content.split("\n")
                    filtered_rows = [table_rows[0], table_rows[1]]  # Keep header and separator
                    
                    # Add relevant rows based on keywords in the description
                    keywords = description.lower().split()
                    for row in table_rows[2:]:  # Skip header and separator
                        if any(keyword in row.lower() for keyword in keywords):
                            filtered_rows.append(row)
                    
                    # If we filtered too aggressively, include some basic rows
                    if len(filtered_rows) <= 2:  # Only header and separator
                        # Include basic component classes
                        for row in table_rows[2:]:  # Skip header and separator
                            if "Component" in row or result["component"].lower() in row.lower():
                                filtered_rows.append(row)
                    
                    # If still too few rows, add a few more important ones
                    if len(filtered_rows) <= 5:  # Add a few more important rows
                        for row in table_rows[2:]:  # Skip header and separator
                            if "primary" in row.lower() or "size" in row.lower() or "style" in row.lower():
                                if row not in filtered_rows:
                                    filtered_rows.append(row)
                    
                    # Combine the filtered rows back into a table
                    filtered_table = "\n".join(filtered_rows)
                    response_text += filtered_table + "\n\n"
                
                # Look for code examples - they're very valuable
                code_start = doc_content.find("Code:")
                if code_start != -1:
                    code_end = doc_content.find("\n\nh", code_start)
                    if code_end == -1:
                        code_end = doc_content.find("\n\np", code_start)
                    if code_end == -1:
                        code_end = min(code_start + 800, len(doc_content))
                    
                    # Extract just the code part, not all the surrounding text
                    code_content = doc_content[code_start:code_end]
                    # Find the actual HTML code
                    html_start = code_content.find("<div")
                    if html_start != -1:
                        # Add a brief code example
                        response_text += "Example:\n```html\n"
                        response_text += code_content[html_start:min(html_start+400, len(code_content))]
                        response_text += "\n```\n\n"
                
                # If we couldn't extract structured content, include a truncated version
                if not (title_start != -1 or table_start != -1 or code_start != -1):
                    max_content_length = 400
                    if len(doc_content) > max_content_length:
                        doc_content = (
                            doc_content[:max_content_length]
                            + "...\n(Documentation truncated for brevity)"
                        )
                    response_text += f"{doc_content}\n\n"

            # Add guidance for implementation
            response_text += "## Implementation Guidance\n\n"
            response_text += "Based on the documentation above, here's how to implement the requested UI component:\n\n"

            # Add example code structure
            response_text += (
                "```html\n<!-- Example structure for the requested component -->\n"
            )
            
            # Analyze the request to determine what components are needed
            needs_button = "button" in description.lower() or "button" in components
            needs_form = "form" in description.lower() or "login" in description.lower() or "signup" in description.lower()
            needs_card = "card" in description.lower() or "card" in components
            needs_carousel = "carousel" in description.lower() or "carousel" in components or "slider" in description.lower()
            needs_checkbox = "checkbox" in description.lower() or "remember" in description.lower()
            needs_link = "link" in description.lower() or "forgot password" in description.lower() or "sign up" in description.lower()
            
            # Check for specific input types to enhance the implementation
            has_password = "password" in description.lower() or any("password" in comp for comp in components)
            has_email = "email" in description.lower() or "login" in description.lower()
            has_text_input = "input" in description.lower() or "field" in description.lower() or "text" in description.lower()
            
            # Determine if this is a login/signup form with card container
            login_in_card = needs_form and needs_card
            
            # Generate appropriate implementation based on component needs
            
            # CASE 1: Login/Signup Form (highest priority for common requests)
            if needs_form:
                # Determine if the form should be in a card
                container_start = ""
                container_end = ""
                if login_in_card:
                    container_start = "<div class=\"card card-border max-w-md mx-auto\">\n"
                    if "header" in description.lower():
                        container_start += "  <div class=\"card-header text-center p-6 bg-base-200/50\">\n"
                        container_start += "    <h2 class=\"text-2xl font-bold\">" + ("Sign In" if "login" in description.lower() else "Sign Up") + "</h2>\n"
                        container_start += "  </div>\n"
                    container_start += "  <div class=\"card-body\">\n"
                    container_end = "  </div>\n</div>\n"
                
                # Start the form
                form_class = "max-w-md mx-auto p-6" + ("" if login_in_card else " bg-base-100 rounded-lg shadow-md")
                response_text += container_start
                response_text += f"<form class=\"{form_class}\">\n"
                
                # Add form fields based on login or signup
                if "signup" in description.lower() or "register" in description.lower():
                    # Name field for signup
                    response_text += "  <div class=\"mb-4\">\n"
                    response_text += "    <label class=\"block text-sm font-medium mb-1\" for=\"name\">Full Name</label>\n"
                    response_text += "    <div class=\"input\">\n"
                    response_text += "      <span class=\"icon-[tabler--user] size-5 text-base-content/50\"></span>\n"
                    response_text += "      <input type=\"text\" id=\"name\" placeholder=\"Enter your name\" />\n"
                    response_text += "    </div>\n"
                    response_text += "  </div>\n\n"
                
                # Email field (common for both login and signup)
                response_text += "  <div class=\"mb-4\">\n"
                response_text += "    <label class=\"block text-sm font-medium mb-1\" for=\"email\">Email</label>\n"
                response_text += "    <div class=\"input\">\n"
                response_text += "      <span class=\"icon-[tabler--mail] size-5 text-base-content/50\"></span>\n"
                response_text += "      <input type=\"email\" id=\"email\" placeholder=\"Enter your email\" />\n"
                response_text += "    </div>\n"
                response_text += "  </div>\n\n"
                
                # Password field with toggle
                response_text += "  <div class=\"mb-4\">\n"
                response_text += "    <label class=\"block text-sm font-medium mb-1\" for=\"password\">Password</label>\n"
                response_text += "    <div class=\"input\">\n"
                response_text += "      <span class=\"icon-[tabler--lock] size-5 text-base-content/50\"></span>\n"
                response_text += "      <input id=\"password\" type=\"password\" placeholder=\"Enter password\" />\n"
                response_text += "      <button aria-label=\"password toggle\" class=\"block cursor-pointer\" data-toggle-password='{ \"target\": \"#password\" }' type=\"button\">\n"
                response_text += "        <span class=\"icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0\"></span>\n"
                response_text += "        <span class=\"icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0\"></span>\n"
                response_text += "      </button>\n"
                response_text += "    </div>\n"
                response_text += "  </div>\n\n"
                
                # Confirm password for signup
                if "signup" in description.lower() or "register" in description.lower():
                    response_text += "  <div class=\"mb-4\">\n"
                    response_text += "    <label class=\"block text-sm font-medium mb-1\" for=\"confirm-password\">Confirm Password</label>\n"
                    response_text += "    <div class=\"input\">\n"
                    response_text += "      <span class=\"icon-[tabler--lock] size-5 text-base-content/50\"></span>\n"
                    response_text += "      <input id=\"confirm-password\" type=\"password\" placeholder=\"Confirm password\" />\n"
                    response_text += "    </div>\n"
                    response_text += "  </div>\n\n"
                
                # Remember me checkbox
                if "remember" in description.lower() or needs_checkbox:
                    response_text += "  <div class=\"mb-4 flex items-center justify-between\">\n"
                    response_text += "    <div class=\"flex items-center\">\n"
                    response_text += "      <input type=\"checkbox\" id=\"remember\" class=\"checkbox checkbox-sm\" />\n"
                    response_text += "      <label for=\"remember\" class=\"ml-2 text-sm\">Remember me</label>\n"
                    response_text += "    </div>\n"
                    
                    # Forgot password link
                    if needs_link or "forgot" in description.lower():
                        response_text += "    <a href=\"#\" class=\"text-sm text-primary hover:underline\">Forgot password?</a>\n"
                        
                    response_text += "  </div>\n\n"
                
                # Submit button
                btn_text = "Sign In" if "login" in description.lower() else "Sign Up"
                response_text += f"  <button type=\"submit\" class=\"btn btn-primary w-full\">{btn_text}</button>\n"
                
                # Sign up/in link
                if needs_link:
                    response_text += "  <div class=\"text-center mt-4\">\n"
                    if "login" in description.lower():
                        response_text += "    <p class=\"text-sm\">Don't have an account? <a href=\"#\" class=\"text-primary hover:underline\">Sign up</a></p>\n"
                    else:
                        response_text += "    <p class=\"text-sm\">Already have an account? <a href=\"#\" class=\"text-primary hover:underline\">Sign in</a></p>\n"
                    response_text += "  </div>\n"
                
                response_text += "</form>\n"
                response_text += container_end
            
            # CASE 2: Simple Button (if not part of a form)
            elif needs_button and not needs_form:
                primary = "primary" in description.lower()
                outline = "outline" in description.lower()
                size = ""
                if "small" in description.lower() or "sm" in description.lower():
                    size = "btn-sm"
                elif "large" in description.lower() or "lg" in description.lower():
                    size = "btn-lg"
                elif "extra small" in description.lower() or "xs" in description.lower():
                    size = "btn-xs"
                elif "extra large" in description.lower() or "xl" in description.lower():
                    size = "btn-xl"
                
                btn_class = "btn"
                if primary:
                    btn_class += " btn-primary"
                if outline:
                    btn_class += " btn-outline"
                if size:
                    btn_class += f" {size}"
                
                button_text = "Button"
                if "submit" in description.lower():
                    button_text = "Submit"
                elif "cancel" in description.lower():
                    button_text = "Cancel"
                elif "save" in description.lower():
                    button_text = "Save"
                
                response_text += f"<button class=\"{btn_class}\">{button_text}</button>\n"
                
            # CASE 3: Card (if not already handled as part of a form)
            elif needs_card and not login_in_card:
                has_image = "image" in description.lower()
                has_actions = "action" in description.lower() or "button" in description.lower()
                
                response_text += "<div class=\"card card-border max-w-sm\">\n"
                if has_image:
                    response_text += "  <figure>\n"
                    response_text += "    <img src=\"https://source.unsplash.com/random/600x400/?nature\" alt=\"Card image\" class=\"w-full h-48 object-cover\" />\n"
                    response_text += "  </figure>\n"
                response_text += "  <div class=\"card-body\">\n"
                response_text += "    <h2 class=\"card-title\">Card Title</h2>\n"
                response_text += "    <p>This is a description for the card. You can add any content here.</p>\n"
                if has_actions:
                    response_text += "    <div class=\"card-actions justify-end\">\n"
                    response_text += "      <button class=\"btn btn-primary\">Action</button>\n"
                    response_text += "      <button class=\"btn btn-outline\">Cancel</button>\n"
                    response_text += "    </div>\n"
                response_text += "  </div>\n"
                response_text += "</div>\n"
                
            # CASE 4: Carousel
            elif needs_carousel:
                response_text += "<div class=\"relative w-full\" data-carousel='{ \"loadingClasses\": \"opacity-0\" }'>\n"
                response_text += "  <div class=\"carousel h-80\">\n"
                response_text += "    <div class=\"carousel-body h-full opacity-0\">\n"
                response_text += "      <!-- Carousel slides -->\n"
                response_text += "      <div class=\"carousel-slide\">\n"
                response_text += "        <img src=\"https://source.unsplash.com/random/1200x600/?nature\" alt=\"Slide 1\" class=\"w-full h-full object-cover\" />\n"
                response_text += "      </div>\n"
                response_text += "      <div class=\"carousel-slide\">\n"
                response_text += "        <img src=\"https://source.unsplash.com/random/1200x600/?city\" alt=\"Slide 2\" class=\"w-full h-full object-cover\" />\n"
                response_text += "      </div>\n"
                response_text += "      <div class=\"carousel-slide\">\n"
                response_text += "        <img src=\"https://source.unsplash.com/random/1200x600/?technology\" alt=\"Slide 3\" class=\"w-full h-full object-cover\" />\n"
                response_text += "      </div>\n"
                response_text += "    </div>\n"
                response_text += "  </div>\n"
                response_text += "  <!-- Navigation buttons -->\n"
                response_text += "  <button class=\"carousel-prev\" type=\"button\">\n"
                response_text += "    <span class=\"size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm\">\n"
                response_text += "      <span class=\"icon-[tabler--chevron-left] size-5 cursor-pointer rtl:rotate-180\"></span>\n"
                response_text += "    </span>\n"
                response_text += "    <span class=\"sr-only\">Previous</span>\n"
                response_text += "  </button>\n"
                response_text += "  <button class=\"carousel-next\" type=\"button\">\n"
                response_text += "    <span class=\"sr-only\">Next</span>\n"
                response_text += "    <span class=\"size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm\">\n"
                response_text += "      <span class=\"icon-[tabler--chevron-right] size-5 cursor-pointer rtl:rotate-180\"></span>\n"
                response_text += "    </span>\n"
                response_text += "  </button>\n"
                response_text += "  <!-- Pagination indicators -->\n"
                response_text += "  <div class=\"carousel-pagination absolute bottom-3 end-0 start-0 flex justify-center gap-3\"></div>\n"
                response_text += "</div>\n"
            
            # CASE 5: Generic component or custom combination
            else:
                # Try to detect what kind of component the user might want
                if has_text_input:
                    # Provide a text input field
                    response_text += "<!-- Input field component -->\n"
                    response_text += "<div class=\"mb-4\">\n"
                    response_text += "  <label class=\"block text-sm font-medium mb-1\" for=\"input-field\">Input Label</label>\n"
                    response_text += "  <div class=\"input\">\n"
                    if has_email:
                        response_text += "    <span class=\"icon-[tabler--mail] size-5 text-base-content/50\"></span>\n"
                        response_text += "    <input type=\"email\" id=\"input-field\" placeholder=\"Enter your email\" />\n"
                    elif has_password:
                        response_text += "    <span class=\"icon-[tabler--lock] size-5 text-base-content/50\"></span>\n"
                        response_text += "    <input type=\"password\" id=\"input-field\" placeholder=\"Enter password\" />\n"
                        response_text += "    <button aria-label=\"password toggle\" class=\"block cursor-pointer\" data-toggle-password='{ \"target\": \"#input-field\" }' type=\"button\">\n"
                        response_text += "      <span class=\"icon-[tabler--eye] text-base-content/80 password-active:block hidden size-5 shrink-0\"></span>\n"
                        response_text += "      <span class=\"icon-[tabler--eye-off] text-base-content/80 password-active:hidden block size-5 shrink-0\"></span>\n"
                        response_text += "    </button>\n"
                    else:
                        response_text += "    <span class=\"icon-[tabler--edit] size-5 text-base-content/50\"></span>\n"
                        response_text += "    <input type=\"text\" id=\"input-field\" placeholder=\"Enter text\" />\n"
                    response_text += "  </div>\n"
                    response_text += "</div>\n"
                else:
                    # Generic component template
                    response_text += "<!-- Generic component structure -->\n"
                    response_text += "<div class=\"p-4 bg-base-100 rounded-lg shadow-md\">\n"
                    response_text += "  <h2 class=\"text-xl font-semibold mb-2\">Component Title</h2>\n"
                    response_text += "  <p class=\"mb-4\">Component description or content goes here.</p>\n"
                    response_text += "  <div class=\"flex gap-2\">\n"
                    response_text += "    <button class=\"btn btn-primary\">Primary Action</button>\n"
                    response_text += "    <button class=\"btn btn-outline\">Secondary Action</button>\n"
                    response_text += "  </div>\n"
                    response_text += "</div>\n"

            # If carousel is mentioned in the description, provide a basic carousel template
            if "carousel" in description.lower() or "carousel" in components:
                response_text += """<div class="relative w-full" data-carousel='{ "loadingClasses": "opacity-0" }'>
  <div class="carousel h-80">
    <div class="carousel-body h-full opacity-0">
      <!-- Carousel slides go here -->
      <div class="carousel-slide">
        <!-- Slide content -->
      </div>
      <!-- More slides as needed -->
    </div>
  </div>
  <!-- Navigation buttons -->
  <button class="carousel-prev" type="button">
    <span class="size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
      <span class="icon-[tabler--chevron-left] size-5 cursor-pointer rtl:rotate-180"></span>
    </span>
    <span class="sr-only">Previous</span>
  </button>
  <button class="carousel-next" type="button">
    <span class="sr-only">Next</span>
    <span class="size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
      <span class="icon-[tabler--chevron-right] size-5 cursor-pointer rtl:rotate-180"></span>
    </span>
  </button>
  <!-- Pagination indicators -->
  <div class="carousel-pagination absolute bottom-3 end-0 start-0 flex justify-center gap-3"></div>
</div>"""
            # If team page is mentioned, provide a basic team page structure
            if "team" in description.lower():
                response_text += """<!-- Team Page Structure -->
<div class="container mx-auto px-4 py-8">
  <h1 class="text-3xl font-bold text-center mb-8">Our Team</h1>
  
  <!-- Team description -->
  <div class="max-w-3xl mx-auto text-center mb-12">
    <p class="text-lg text-gray-600">Our talented team of professionals is dedicated to delivering exceptional results.</p>
  </div>
  
  <!-- Team member carousel -->
  <div class="relative w-full" data-carousel='{ "loadingClasses": "opacity-0", "slidesQty": { "xs": 1, "sm": 2, "md": 3, "lg": 4 } }'>
    <div class="carousel h-auto">
      <div class="carousel-body opacity-0 gap-4">
        <!-- Team member cards -->
        <div class="carousel-slide">
          <div class="bg-base-100 rounded-lg shadow-md overflow-hidden">
            <img src="https://source.unsplash.com/random/300x300/?portrait" alt="Team Member" class="w-full h-64 object-cover">
            <div class="p-4">
              <h3 class="text-xl font-semibold">John Doe</h3>
              <p class="text-sm text-gray-500">CEO & Founder</p>
              <p class="mt-2 text-gray-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              <div class="mt-4 flex space-x-3">
                <a href="#" class="text-blue-500"><span class="icon-[tabler--brand-twitter] size-5"></span></a>
                <a href="#" class="text-blue-700"><span class="icon-[tabler--brand-linkedin] size-5"></span></a>
                <a href="#" class="text-gray-700"><span class="icon-[tabler--mail] size-5"></span></a>
              </div>
            </div>
          </div>
        </div>
        <!-- More team members would be added here -->
      </div>
    </div>
    <!-- Navigation buttons -->
    <button class="carousel-prev" type="button">
      <span class="size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
        <span class="icon-[tabler--chevron-left] size-5 cursor-pointer rtl:rotate-180"></span>
      </span>
      <span class="sr-only">Previous</span>
    </button>
    <button class="carousel-next" type="button">
      <span class="sr-only">Next</span>
      <span class="size-9.5 bg-base-100 flex items-center justify-center rounded-full shadow-base-300/20 shadow-sm">
        <span class="icon-[tabler--chevron-right] size-5 cursor-pointer rtl:rotate-180"></span>
      </span>
    </button>
  </div>
</div>"""

            response_text += "\n```\n\n"

            # Add installation instructions and usage notes
            response_text += "## Installation Instructions\n\n"
            response_text += "To use FlyonUI components, make sure you have the following in your project:\n\n"
            response_text += "1. Tailwind CSS installed and configured\n"
            response_text += "2. FlyonUI installed: `npm install flyonui`\n"
            response_text += "3. Include the necessary JavaScript for interactive components\n"
            response_text += "4. Configure Iconify for Tabler icons: `npm i -D @iconify/tailwind4 @iconify-json/tabler`\n\n"

            # Add usage notes based on the components used
            response_text += "## Usage Notes\n\n"

            if needs_form or has_password:
                response_text += "### Password Toggle\n"
                response_text += "The password toggle functionality requires the FlyonUI JavaScript to be properly initialized:\n\n"
                response_text += "```js\n"
                response_text += "// Initialize password toggle\n"
                response_text += "document.addEventListener('DOMContentLoaded', function() {\n"
                response_text += "  FlyonUI.initPasswordToggle();\n"
                response_text += "});\n"
                response_text += "```\n\n"

            if needs_carousel:
                response_text += "### Carousel\n"
                response_text += "The carousel component requires JavaScript initialization:\n\n"
                response_text += "```js\n"
                response_text += "// Initialize carousel\n"
                response_text += "document.addEventListener('DOMContentLoaded', function() {\n"
                response_text += "  FlyonUI.initCarousel();\n"
                response_text += "});\n"
                response_text += "```\n\n"

            response_text += "For more details, refer to the FlyonUI documentation."

            return [types.TextContent(content=response_text)]
        
        # If the tool name is not recognized
        return [
            types.TextContent(
                type="text",
                text="Error: Unknown tool. Please use 'create-ui' to generate UI components.",
            )
        ]
