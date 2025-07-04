"""Utility functions for working with metadata in MCP types.

These utilities are primarily intended for client-side usage to properly display
human-readable names in user interfaces in a spec compliant way.
"""

from mcp.types import Implementation, Prompt, Resource, ResourceTemplate, Tool


def get_display_name(obj: Tool | Resource | Prompt | ResourceTemplate | Implementation) -> str:
    """
    Get the display name for an MCP object with proper precedence.

    This is a client-side utility function designed to help MCP clients display
    human-readable names in their user interfaces. When servers provide a 'title'
    field, it should be preferred over the programmatic 'name' field for display.

    For tools: title > annotations.title > name
    For other objects: title > name

    Example:
        # In a client displaying available tools
        tools = await session.list_tools()
        for tool in tools.tools:
            display_name = get_display_name(tool)
            print(f"Available tool: {display_name}")

    Args:
        obj: An MCP object with name and optional title fields

    Returns:
        The display name to use for UI presentation
    """
    if isinstance(obj, Tool):
        # Tools have special precedence: title > annotations.title > name
        if hasattr(obj, "title") and obj.title is not None:
            return obj.title
        if obj.annotations and hasattr(obj.annotations, "title") and obj.annotations.title is not None:
            return obj.annotations.title
        return obj.name
    else:
        # All other objects: title > name
        if hasattr(obj, "title") and obj.title is not None:
            return obj.title
        return obj.name
