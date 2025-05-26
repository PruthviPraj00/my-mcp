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
                            "description": "Detailed description of the UI to generate, including purpose, functionality, and any specific requirements",
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
                    "title": "Create UI Blocks and pages",
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
            # Extract the description from arguments
            description = arguments.get("description", "")
            requested_components = arguments.get("components", [])

            # Import the search_docs function from main
            from main import search_docs

            # Find relevant components based on user description or specific requests
            relevant_components = []
            if requested_components:
                for component_name in requested_components:
                    results = search_docs(component_name, limit=1)
                    relevant_components.extend(results)
            else:
                # Search for components that match the description
                relevant_components = search_docs(description, limit=5)

            # Generate UI implementation
            html_code = generate_ui_implementation(description, relevant_components)

            # Extract any JavaScript needed
            js_code = extract_javascript(relevant_components)

            # Prepare the response
            response = []

            # Add a title based on the description or component names
            if requested_components:
                title = "FlyonUI: " + ", ".join(requested_components)
            else:
                title = get_title_from_description(description)
            response.append(types.TextContent(type="text", text=f"# {title}\n\n"))

            # Add the component code blocks
            response.append(
                types.TextContent(
                    type="text",
                    text="## Component Code\n\n```html\n" + html_code + "\n```\n\n",
                )
            )

            # Add JavaScript if present
            if js_code:
                response.append(
                    types.TextContent(
                        type="text",
                        text="## JavaScript\n\n```javascript\n" + js_code + "\n```\n\n",
                    )
                )

            # Add information about components used
            if relevant_components:
                components_used = "## Components Used\n\n"
                for comp in relevant_components:
                    # Use component name instead of title if title is not available
                    component_name = comp.get("component", "Unknown Component")
                    # Extract a brief description from content if available
                    content_preview = ""
                    if "content" in comp:
                        # Take the first 100 characters of content as a preview
                        content_preview = comp["content"][:100] + "..."

                    components_used += f"- **{component_name}**: {content_preview}\n\n"
                response.append(types.TextContent(type="text", text=components_used))

            # Add implementation guidelines
            implementation_guidelines = """
## Implementation Guidelines


### 2. Styling & Visual Accuracy

- Apply FlyonUI semantic classes (bg-primary, text-primary-content, etc.)
- Use text colors appropriately:
  - Main text: `text-base-content`
  - Body text: `text-base-content/80`
  - Subtext: `text-base-content/50`
  - Colored text: `text-{primary, secondary, accent, info, success, warning, error}`
  - for border use `border-base-content/20` and can also be used with `border-{primary, secondary, accent, info, success, warning, error}`
  - for shadow use `shadow-base-300/20` and can also be used with `shadow-{primary, secondary, accent, info, success, warning, error}`
- Use Tailwind CSS utilities for additional styling needs
- Match colors, typography, spacing, and visual hierarchy exactly
- Implement all interactive states (hover, focus, active, disabled)
- Maintain consistent spacing using Tailwind's spacing scale

### 3. Responsive Design

- Desktop (1200px+): Full layout as shown in design
- Tablet (768px - 1199px): Optimized layout with appropriate adjustments
- Mobile (320px - 767px): Stacked, mobile-friendly layout
- Use Tailwind breakpoints (sm, md, lg, xl) consistently
- Ensure smooth transitions between breakpoints

### 4. Icons

- Use tabler icons from iconify (e.g., `icon-[tabler--user]`)
- Ensure icons are properly sized and positioned
"""

            response.append(
                types.TextContent(type="text", text=implementation_guidelines)
            )

            # Add usage notes
            response.append(
                types.TextContent(
                    type="text",
                    text="## Usage Notes\n\n- These components require FlyonUI to be installed in your project\n- Copy the component code into your existing HTML structure\n- If JavaScript is included, make sure to add it to your scripts\n",
                )
            )

            return response


def get_title_from_description(description: str) -> str:
    """Extract a title from the user description."""
    # Take the first 5-8 words as the title
    words = description.split()
    title_words = words[: min(8, len(words))]
    title = " ".join(title_words)

    # Capitalize the title
    title = title.capitalize()

    # Add "FlyonUI:" prefix
    return f"FlyonUI: {title}"


def generate_ui_implementation(
    description: str, components: List[Dict[str, Any]]
) -> str:
    """Generate component code blocks based on user description and components."""
    # Just return the component code blocks without full HTML structure
    html = ""

    # Add components based on what was found
    if not components:
        # No components found, provide a placeholder with FlyonUI styling
        html = '<div class="card p-6 bg-base-200 border border-base-300 rounded-lg shadow-sm">\n'
        html += '  <h3 class="text-lg font-semibold mb-2 text-base-content">No matching components found</h3>\n'
        html += '  <p class="text-base-content/80">Please try a different description or specify component names.</p>\n'
        html += '  <div class="mt-4">\n'
        html += '    <span class="icon-[tabler--search] size-5 text-base-content/50 mr-2"></span>\n'
        html += '    <span class="text-sm text-base-content/50">Try searching for specific component names like "button", "card", "form", etc.</span>\n'
        html += "  </div>\n"
        html += "</div>\n"
    else:
        # Add each component with a wrapper and title
        for i, comp in enumerate(components):
            # Use component name if title is not available
            component_title = comp.get("component", "Component")
            component_category = comp.get("category", "")

            # Add component wrapper with detailed comment
            html += f"<!-- {component_title} ({component_category}) -->\n"
            html += f"<!-- Follow FlyonUI guidelines for proper implementation -->\n"

            # Add the component code if available
            if "example" in comp:
                html += comp["example"]["code"] + "\n\n"
            else:
                # Create a well-styled placeholder with FlyonUI classes
                html += '<div class="card bg-base-100 border border-base-300 rounded-lg shadow-sm p-4 mb-4">\n'
                html += '  <div class="card-header pb-3 border-b border-base-200">\n'
                html += '    <h3 class="text-lg font-semibold text-base-content flex items-center">\n'
                html += (
                    '      <span class="icon-[tabler--components] size-5 mr-2 text-primary"></span>'
                    + component_title
                    + "\n"
                )
                html += "    </h3>\n"
                html += "  </div>\n"
                html += '  <div class="card-body py-3">\n'
                html += (
                    '    <p class="text-base-content/80">'
                    + comp.get("description", "")
                    + "...</p>\n"
                )
                html += "  </div>\n"
                html += '  <div class="card-footer pt-3 border-t border-base-200 text-sm text-base-content/60">\n'
                html += "    Category: " + component_category + "\n"
                html += "  </div>\n"
                html += "</div>\n\n"

    return html


def extract_javascript(components: List[Dict[str, Any]]) -> str:
    """Extract JavaScript code from component examples."""
    js_code = ""

    for comp in components:
        # Use component name if title is not available
        component_title = comp.get("component", "Component")
        if (
            "example" in comp
            and comp["example"].get("has_js")
            and comp["example"].get("js_code")
        ):
            js_code += (
                f"\n// {component_title} JavaScript\n{comp['example']['js_code']}\n"
            )

    if js_code:
        js_code = (
            "document.addEventListener('DOMContentLoaded', function() {\n"
            + js_code
            + "\n});\n"
        )

    return js_code
