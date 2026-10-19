"""A Model Context Protocol server exposing plant-telemetry tools."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("cement-tools")


@mcp.tool()
def get_kiln_temp() -> float:
    """Return the current kiln temperature in Celsius."""
    return 1450.0


@mcp.tool()
def get_clinker_rate() -> float:
    """Return the current clinker production rate in tonnes/hour."""
    return 210.5


if __name__ == "__main__":
    mcp.run()
