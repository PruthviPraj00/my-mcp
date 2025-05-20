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
                if component in [
                    "introduction",
                    "quick start",
                    "upgrade guide",
                    "usage",
                    "framework guides",
                    "javascript",
                    "license",
                    "customization",
                    "customize components",
                    "config",
                    "base style",
                    "colors",
                    "icons",
                    "themes",
                    "utilities and variables",
                    "rtl",
                    "theme generator",
                ]:
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

            # Create a simple analysis of what components might be needed based on the request
            component_keywords = {
                "grid": ["grid", "layout", "columns", "rows"],
                "card": ["card", "project", "item", "thumbnail"],
                "modal": ["modal", "popup", "dialog", "opens up"],
                "carousel": ["carousel", "slider", "slideshow", "gallery"],
                "image": ["image", "picture", "photo", "img"],
                "overlay": ["overlay", "hover", "cover"],
                "button": ["button", "btn", "click"],
            }
            
            # Identify components based on the description
            description_lower = description.lower()
            identified_components = []
            
            for component, keywords in component_keywords.items():
                if any(keyword in description_lower for keyword in keywords):
                    identified_components.append(component)
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

            # Add a section to help the LLM understand what components are needed
            response_text += "## Component Analysis\n\n"
            response_text += "Based on your request, the following FlyonUI components would be useful:\n\n"

            # Add identified components to the response
            for component in identified_components:
                response_text += f"- **{component.title()}**: Required for your request\n"
            
            response_text += "\n"

            # First, thoroughly analyze the documentation to understand the components
            component_analysis = {}
            for result in doc_results:
                component_name = result["component"]
                doc_content = result["content"]

                # Create an analysis structure for this component
                analysis = {
                    "name": component_name,
                    "title": "",
                    "description": "",
                    "usage": "",
                    "examples": [],
                    "classes": [],
                    "best_example": "",
                }

                # Extract the title
                title_start = doc_content.find("# ")
                if title_start != -1:
                    title_end = doc_content.find("\n\n", title_start)
                    if title_end != -1:
                        analysis["title"] = doc_content[title_start:title_end].strip()

                # Extract the description
                p_start = doc_content.find("p:\n  - ")
                if p_start != -1:
                    p_end = doc_content.find("\n\n", p_start)
                    if p_end != -1:
                        analysis["description"] = (
                            doc_content[p_start:p_end].replace("p:\n  - ", "").strip()
                        )

                # Extract the class information
                table_start = doc_content.find("| Class Name | Type | Description |")
                if table_start != -1:
                    table_end = doc_content.find("\n\nh", table_start)
                    if table_end == -1:
                        table_end = doc_content.find("\n\np", table_start)
                    if table_end == -1:
                        table_end = len(doc_content)

                    table_content = doc_content[table_start:table_end]
                    table_rows = table_content.split("\n")[
                        2:
                    ]  # Skip header and separator

                    for row in table_rows:
                        if "|" in row:
                            parts = row.split("|")[
                                1:-1
                            ]  # Remove empty first and last elements
                            if len(parts) >= 3:
                                class_name = parts[0].strip()
                                class_type = parts[1].strip()
                                class_desc = parts[2].strip()
                                analysis["classes"].append(
                                    {
                                        "name": class_name,
                                        "type": class_type,
                                        "description": class_desc,
                                    }
                                )

                # Extract examples with their headings to understand context
                heading_positions = []
                lines = doc_content.split("\n")

                # Find all h2 and h3 headings
                for i, line in enumerate(lines):
                    if line.startswith("h2:") or line.startswith("h3:"):
                        heading_text = ""
                        if line.startswith("h2:"):
                            heading_text = line.replace("h2:\n  - ", "").strip()
                            heading_level = 2
                        else:
                            heading_text = line.replace("h3:\n  - ", "").strip()
                            heading_level = 3

                        heading_positions.append(
                            {"line": i, "text": heading_text, "level": heading_level}
                        )

                # Extract code examples with their context
                code_positions = []
                for i, line in enumerate(lines):
                    if line.startswith("Code:"):
                        code_positions.append(i)

                # Match code examples with their headings
                examples = []
                for code_pos in code_positions:
                    # Find the closest heading before this code
                    closest_heading = None
                    closest_distance = float("inf")

                    for heading in heading_positions:
                        if (
                            heading["line"] < code_pos
                            and code_pos - heading["line"] < closest_distance
                        ):
                            closest_heading = heading
                            closest_distance = code_pos - heading["line"]

                    # Extract the code
                    for j in range(code_pos + 1, min(code_pos + 30, len(lines))):
                        if lines[j].startswith("<div"):
                            # Extract HTML content
                            html_content = ""
                            k = j
                            depth = 0
                            started = False

                            while k < len(lines) and (not started or depth > 0):
                                line = lines[k]
                                if "<div" in line:
                                    depth += 1
                                    started = True
                                if "</div>" in line:
                                    depth -= 1
                                html_content += line + "\n"
                                k += 1
                                if k - j > 50:  # Limit to 50 lines max
                                    break

                            if closest_heading:
                                examples.append(
                                    {
                                        "heading": closest_heading["text"],
                                        "level": closest_heading["level"],
                                        "code": html_content.strip(),
                                    }
                                )
                            else:
                                examples.append(
                                    {
                                        "heading": "Example",
                                        "level": 3,
                                        "code": html_content.strip(),
                                    }
                                )
                            break

                analysis["examples"] = examples

                # Determine the best example based on the request
                if examples:
                    best_example = None
                    best_score = -1

                    for example in examples:
                        score = 0
                        # Check if heading matches keywords in the description
                        for keyword in description.lower().split():
                            if keyword in example["heading"].lower():
                                score += 3

                        # Check if the example code contains relevant elements
                        for keyword in description.lower().split():
                            if keyword in example["code"].lower():
                                score += 1

                        # Prefer basic/default examples for beginners
                        if (
                            "basic" in example["heading"].lower()
                            or "default" in example["heading"].lower()
                        ):
                            score += 2

                        if score > best_score:
                            best_score = score
                            best_example = example

                    if best_example:
                        analysis["best_example"] = best_example

                component_analysis[component_name] = analysis

            # Generate a concise summary of each component
            response_text += "## Component Summaries\n\n"

            for component_name, analysis in component_analysis.items():
                formatted_name = component_name.replace("-", " ").title()
                response_text += f"### {formatted_name}\n\n"

                # Add title and description
                if analysis["title"]:
                    response_text += f"{analysis['title']}\n\n"
                if analysis["description"]:
                    response_text += f"{analysis['description']}\n\n"

                # Add key classes (limit to most relevant)
                if analysis["classes"]:
                    response_text += "**Key Classes:**\n\n"
                    response_text += "| Class Name | Type | Description |\n"
                    response_text += "|------------|------|-------------|\n"

                    # Filter classes to show only the most relevant ones
                    relevant_classes = []

                    # First include component classes
                    for cls in analysis["classes"]:
                        if cls["type"].lower() == "component":
                            relevant_classes.append(cls)

                    # Then include classes mentioned in the description
                    for cls in analysis["classes"]:
                        if cls not in relevant_classes:
                            for keyword in description.lower().split():
                                if (
                                    keyword in cls["name"].lower()
                                    or keyword in cls["description"].lower()
                                ):
                                    relevant_classes.append(cls)
                                    break

                    # If we still have few classes, add some common ones (color, size, etc.)
                    if len(relevant_classes) < 5:
                        for cls in analysis["classes"]:
                            if cls not in relevant_classes and (
                                "color" in cls["type"].lower()
                                or "size" in cls["type"].lower()
                                or "style" in cls["type"].lower()
                            ):
                                relevant_classes.append(cls)
                                if len(relevant_classes) >= 8:
                                    break

                    # Show the relevant classes
                    for cls in relevant_classes[:8]:  # Limit to 8 classes
                        response_text += f"| {cls['name']} | {cls['type']} | {cls['description']} |\n"

                    response_text += "\n"

                # Add the best example if available
                if analysis["best_example"]:
                    response_text += f"**{analysis['best_example']['heading']}:**\n\n"
                    response_text += "```html\n"
                    response_text += analysis["best_example"]["code"] + "\n"
                    response_text += "```\n\n"

            # Add implementation guidance
            response_text += "## Implementation Guidance\n\n"
            response_text += "Based on the documentation above, here's how to implement the requested UI component:\n\n"

            # Generate implementation code based on the request and component analysis
            response_text += (
                "```html\n<!-- Example implementation for the requested component -->\n"
            )

            # Determine what type of component to generate based on the request
            needs_form = (
                "form" in description.lower()
                or "login" in description.lower()
                or "signup" in description.lower()
                or "register" in description.lower()
            )
            needs_card = "card" in description.lower() or any(
                "card" in comp for comp in potential_components
            )
            needs_button = "button" in description.lower() or any(
                "button" in comp for comp in potential_components
            )
            needs_input = (
                "input" in description.lower()
                or "field" in description.lower()
                or any("input" in comp for comp in potential_components)
            )

            # Generate the appropriate implementation
            if needs_form:
                # Find the best form example from our component analysis
                form_example = None
                for comp_name, analysis in component_analysis.items():
                    if comp_name == "form" and analysis["best_example"]:
                        form_example = analysis["best_example"]["code"]
                        break

                # If we found a form example, use it as a base
                if form_example:
                    response_text += form_example + "\n"
                else:
                    # Create a basic form structure
                    response_text += '<form class="max-w-md mx-auto p-6">\n'

                    # Add form fields based on the description
                    if "email" in description.lower() or "login" in description.lower():
                        # Find an input example
                        input_example = None
                        for comp_name, analysis in component_analysis.items():
                            if comp_name == "input" and analysis["best_example"]:
                                input_example = analysis["best_example"]["code"]
                                break

                        if input_example:
                            # Modify the input example for email
                            email_input = input_example.replace(
                                'type="text"', 'type="email"'
                            )
                            email_input = email_input.replace(
                                'placeholder="Enter text"',
                                'placeholder="Enter your email"',
                            )
                            response_text += "  <!-- Email field -->\n"
                            response_text += '  <div class="mb-4">\n'
                            response_text += '    <label class="block text-sm mb-1" for="email">Email address</label>\n'
                            response_text += f"    {email_input}\n"
                            response_text += "  </div>\n\n"
                        else:
                            # Fallback to a basic email input
                            response_text += "  <!-- Email field -->\n"
                            response_text += '  <div class="mb-4">\n'
                            response_text += '    <label class="block text-sm mb-1" for="email">Email address</label>\n'
                            response_text += '    <input type="email" id="email" placeholder="Enter your email" class="input w-full" />\n'
                            response_text += "  </div>\n\n"

                    if (
                        "password" in description.lower()
                        or "login" in description.lower()
                        or "signup" in description.lower()
                    ):
                        # Find a password input example
                        password_example = None
                        for comp_name, analysis in component_analysis.items():
                            if (
                                comp_name == "toggle-password"
                                and analysis["best_example"]
                            ):
                                password_example = analysis["best_example"]["code"]
                                break

                        if password_example:
                            response_text += "  <!-- Password field -->\n"
                            response_text += '  <div class="mb-4">\n'
                            response_text += '    <label class="block text-sm mb-1" for="password">Password</label>\n'
                            response_text += f"    {password_example}\n"
                            response_text += "  </div>\n\n"
                        else:
                            # Fallback to a basic password input
                            response_text += "  <!-- Password field -->\n"
                            response_text += '  <div class="mb-4">\n'
                            response_text += '    <label class="block text-sm mb-1" for="password">Password</label>\n'
                            response_text += (
                                '    <div class="input w-full flex items-center">\n'
                            )
                            response_text += '      <input id="password" type="password" placeholder="••••••••" class="flex-1 bg-transparent border-none focus:outline-none p-0" />\n'
                            response_text += '      <button type="button" aria-label="password toggle" class="block cursor-pointer" data-toggle-password=\'{ "target": "#password" }\'>\n'
                            response_text += '        <span class="icon-[tabler--eye] text-base-content/60 password-active:block hidden size-5 shrink-0"></span>\n'
                            response_text += '        <span class="icon-[tabler--eye-off] text-base-content/60 password-active:hidden block size-5 shrink-0"></span>\n'
                            response_text += "      </button>\n"
                            response_text += "    </div>\n"
                            response_text += "  </div>\n\n"

                    # Add a submit button
                    button_example = None
                    for comp_name, analysis in component_analysis.items():
                        if comp_name == "button" and analysis["best_example"]:
                            button_example = analysis["best_example"]["code"]
                            break

                    if button_example:
                        # Modify the button example for submit
                        submit_button = button_example.replace(
                            'class="btn', 'class="btn btn-primary w-full'
                        )
                        submit_button = submit_button.replace(">Button<", ">Submit<")
                        response_text += "  <!-- Submit button -->\n"
                        response_text += f"  {submit_button}\n"
                    else:
                        # Fallback to a basic submit button
                        response_text += "  <!-- Submit button -->\n"
                        response_text += '  <button type="submit" class="btn btn-primary w-full">Submit</button>\n'

                    response_text += "</form>\n"

            elif needs_card:
                # Find the best card example
                card_example = None
                for comp_name, analysis in component_analysis.items():
                    if comp_name == "card" and analysis["best_example"]:
                        card_example = analysis["best_example"]["code"]
                        break

                if card_example:
                    response_text += card_example + "\n"
                else:
                    # Fallback to a basic card
                    response_text += '<div class="card">\n'
                    response_text += '  <div class="card-body">\n'
                    response_text += '    <h2 class="card-title">Card Title</h2>\n'
                    response_text += "    <p>Card content goes here.</p>\n"
                    response_text += "  </div>\n"
                    response_text += "</div>\n"

            elif needs_button:
                # Find the best button example
                button_example = None
                for comp_name, analysis in component_analysis.items():
                    if comp_name == "button" and analysis["best_example"]:
                        button_example = analysis["best_example"]["code"]
                        break

                if button_example:
                    response_text += button_example + "\n"
                else:
                    # Fallback to a basic button
                    response_text += '<button class="btn btn-primary">Button</button>\n'

            elif needs_input:
                # Find the best input example
                input_example = None
                for comp_name, analysis in component_analysis.items():
                    if comp_name == "input" and analysis["best_example"]:
                        input_example = analysis["best_example"]["code"]
                        break

                if input_example:
                    response_text += input_example + "\n"
                else:
                    # Fallback to a basic input
                    response_text += '<div class="mb-4">\n'
                    response_text += '  <label class="block text-sm mb-1" for="input">Input Label</label>\n'
                    response_text += '  <input type="text" id="input" placeholder="Enter text" class="input w-full" />\n'
                    response_text += "</div>\n"

            else:
                # If we can't determine a specific component, use the first best example we find
                example_used = False
                for comp_name, analysis in component_analysis.items():
                    if analysis["best_example"]:
                        response_text += analysis["best_example"]["code"] + "\n"
                        example_used = True
                        break

                if not example_used:
                    # Fallback to a generic message
                    response_text += "<!-- No specific component was identified. Please refer to the documentation above. -->\n"

            response_text += "```"

            return [types.TextContent(type="text", text=response_text)]

        # If the tool name is not recognized
        return [
            types.TextContent(
                type="text",
                text="Error: Unknown tool. Please use 'create-ui' to generate UI components.",
            )
        ]
