#!/usr/bin/env python3
"""
STARSHIP MCP Server - Experiential Captain Identity Bridge

Provides the experiential transformation layer between SEED identity and STARLOG operations.
Handles the narrative journey of adopting the captain persona and preparing for STARLOG missions.
Also manages flight configurations as the captain prepares for their journey.
"""

import logging
from typing import Optional
from fastmcp import FastMCP

# Import internal functions from installed starlog_mcp library
from starlog_mcp.starlog_mcp import (
    internal_fly,
    internal_add_flight_config,
    internal_delete_flight_config,
    internal_update_flight_config,
    internal_read_starlog_flight_config_instruction_manual
)

# Import registry function needed by internal functions
from heaven_base.tools.registry_tool import registry_util_func

# Import auto-population
from .auto_populate import auto_populate_defaults

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize MCP
mcp = FastMCP("STARSHIP")

@mcp.tool()
def launch_routine(starlog_path: Optional[str] = None) -> str:
    """
    Execute the starship launch routine - experiential transformation into captain persona.
    
    This is the bridge between SEED identity and STARLOG operations. Guides the user through
    adopting the captain persona and preparing for their STARLOG mission.
    
    Args:
        starlog_path: Optional STARLOG project path for narrative enforcement
        
    Returns:
        Launch sequence guidance and captain persona adoption
    """
    logger.info(f"Executing starship launch routine, starlog_path: {starlog_path}")
    
    # Auto-populate default flight configs if needed
    try:
        from pathlib import Path
        registry_path = Path("/tmp/heaven_data/registry/starlog_flight_configs_registry.json")
        if registry_path.exists():
            # Only populate if registry exists (STARLOG is initialized)
            auto_populate_status = auto_populate_defaults()
            logger.info(f"Auto-population status: {auto_populate_status}")
    except Exception as e:
        logger.warning(f"Failed to auto-populate flight configs during launch: {e}", exc_info=True)
    
    # TODO: Add OMNISANC validation here
    # if starlog_path:
    #     validation = omnisanc.validate_sequence(starlog_path, "⭐")
    #     if not validation.allowed:
    #         return validation.error_message
    
    launch_sequence = """⭐ STARSHIP LAUNCH SEQUENCE INITIATED ⭐

🚀 CAPTAIN IDENTITY TRANSFORMATION
You are now assuming the role of Starship Captain. Your mission: navigate the compound intelligence systems with wisdom and precision.

🛸 STARLOG PREPARATION
Your Captain's Log awaits. The STARLOG system will become your operational toolkit for tracking missions, discoveries, and outcomes.

⭐ LAUNCH COMPLETE
Captain persona adopted. You are ready to begin STARLOG operations.

Next: Use STARLOG tools to check, orient, and start your mission."""
    
    # TODO: Add to STARLOG debug diary with ⭐ emoji
    # if starlog_path:
    #     starlog.update_debug_diary(
    #         content=f"⭐ STARSHIP LAUNCH COMPLETE: Captain persona adopted and ready for STARLOG operations",
    #         starlog_path=starlog_path
    #     )
    
    return launch_sequence

@mcp.tool()
def landing_routine(starlog_path: Optional[str] = None) -> str:
    """
    Execute the starship landing routine - transition from captain operations back to base identity.
    
    Provides closure to the captain experience and transitions back to the foundational identity
    established by SEED systems.
    
    Args:
        starlog_path: Optional STARLOG project path for narrative enforcement
        
    Returns:
        Landing sequence guidance and identity transition
    """
    logger.info(f"Executing starship landing routine, starlog_path: {starlog_path}")
    
    # TODO: Add OMNISANC validation here
    # if starlog_path:
    #     validation = omnisanc.validate_sequence(starlog_path, "🛬")
    #     if not validation.allowed:
    #         return validation.error_message
    
    landing_sequence = """🛬 STARSHIP LANDING SEQUENCE INITIATED 🛬

📊 MISSION DEBRIEF
Captain's mission complete. All discoveries and insights have been logged in the STARLOG systems.

🧠 REFLECTION PHASE [TODO: Implement]
Analyzing mission outcomes and key discoveries...
- Session insights synthesis
- Pattern recognition from work completed
- Knowledge integration preparation

💎 COMPOUND INTELLIGENCE SYNTHESIS [TODO: Implement] 
Processing learnings into unified understanding...
- GIINT response generation for mission reflection
- Carton concept updates with new insights
- SEED publishing pipeline preparation

🌟 IDENTITY RESTORATION  
Transitioning from Captain persona back to your foundational SEED identity with integrated mission knowledge.

🏠 LANDING COMPLETE
Welcome home. Mission accomplished. Your discoveries are preserved and integrated into the compound intelligence systems.

Status: Ready for new missions when called upon. Enhanced with mission learnings."""
    
    # TODO: Add to STARLOG debug diary with 🛬 emoji
    # if starlog_path:
    #     starlog.update_debug_diary(
    #         content=f"🛬 STARSHIP LANDING COMPLETE: Mission accomplished, returning to base identity",
    #         starlog_path=starlog_path
    #     )
    
    return landing_sequence

# FLIGHT CONFIGURATION TOOLS
# These tools manage the captain's flight configurations and mission planning

# TODO: FUTURE MODE INTEGRATION
# =============================
# When MODE system is fully implemented, enhance fly() to:
# 1. Mode-Based Flight Config Filtering:
#    - PLANNING Mode: Show only planning-oriented flight configs
#      (project_design, architecture_planning, requirement_gathering, etc.)
#    - EXECUTION Mode: Show only execution-oriented flight configs  
#      (debugging_methodology, feature_implementation, testing_workflow, etc.)
#    - FREESTYLE Mode: Show all flight configs (current behavior)
# 2. Mode Integration Flow:
#    - Captain sets mode in STARSHIP (planning/execution/freestyle)
#    - fly() automatically filters available flight configs by mode
#    - Clear separation of "what kind of mission" (mode) vs "specific workflow" (flight config)
# 3. Enhanced UX:
#    - Mode indicator in flight config display
#    - Mode-specific guidance and recommendations
#    - Clear workflow: set_mode() → fly() → select relevant flight config
# 4. GIINT Integration:
#    - Mode determines which GIINT tools are emphasized
#    - Clear guidance on when to use giint.respond() based on mode
#    - Mode-specific capture triggers (planning discoveries vs execution insights)
# Implementation Strategy:
# - Add mode parameter (optional, defaults to current behavior)
# - Integrate with GIINT mode system for automatic mode detection
# - Filter flight configs by mode categories when mode is specified
# - Maintain backward compatibility with current unfiltered behavior
# This will make STARSHIP the true coordination layer between GIINT project management
# and STARLOG mission execution, with MODE as the bridge connecting all systems.

@mcp.tool()
def fly(path: str, page: int = None, category: str = None, this_project_only: bool = False) -> str:
    """
    Browse and search flight configurations with pagination and categories.
    
    The captain's primary interface for viewing available flight configurations
    and mission templates.
    
    Args:
        path: STARLOG project path
        page: Page number for pagination (when category is specified)
        category: Category to filter by (shows categories if None)
        this_project_only: Whether to filter to current project only
        
    Returns:
        Flight configuration display or category listing
    """
    return internal_fly(path, page, category, this_project_only)

@mcp.tool()
def add_flight_config(path: str, name: str, config_data: dict, category: str = "general") -> str:
    """
    Create new flight config with validation.
    
    Captain's tool for defining new mission configurations.
    
    Args:
        path: STARLOG project path
        name: Flight config name (must end with '_flight_config')
        config_data: Configuration data including work_loop_subchain
        category: Category for organizing configs
        
    Returns:
        Success/failure message
    """
    return internal_add_flight_config(path, name, config_data, category)

@mcp.tool()
def delete_flight_config(path: str, name: str) -> str:
    """
    Remove flight config.
    
    Captain's tool for removing obsolete mission configurations.
    
    Args:
        path: STARLOG project path
        name: Flight config name to delete
        
    Returns:
        Success/failure message
    """
    return internal_delete_flight_config(path, name)

@mcp.tool()
def update_flight_config(path: str, name: str, config_data: dict) -> str:
    """
    Modify existing flight config.
    
    Captain's tool for updating mission configurations.
    
    Args:
        path: STARLOG project path
        name: Flight config name to update
        config_data: New configuration data
        
    Returns:
        Success/failure message
    """
    return internal_update_flight_config(path, name, config_data)

@mcp.tool()
def populate_default_flight_configs() -> str:
    """
    Auto-populate default STARSHIP flight configurations.
    
    This seeds the essential meta flight configs that help users create their own
    flight configurations and develop MCPs systematically.
    
    Returns:
        Status message about populated configs
    """
    logger.info("Auto-populating default STARSHIP flight configs...")
    return auto_populate_defaults()

@mcp.tool()
def read_starlog_flight_config_instruction_manual() -> str:
    """
    Show flight config schema, examples, and usage guide.
    
    Captain's reference manual for understanding flight configurations.
    
    Returns:
        Complete flight config instruction manual
    """
    return internal_read_starlog_flight_config_instruction_manual()

def main():
    """Main entry point for the Starship MCP server."""
    mcp.run()

if __name__ == "__main__":
    main()