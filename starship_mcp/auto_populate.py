#!/usr/bin/env python3
"""
Auto-population of default flight configs for STARSHIP.

This module provides default flight configurations that are essential for the compound
intelligence system. These configs are auto-populated when STARSHIP is first used.
"""

import json
import logging
import os
from pathlib import Path
from typing import Dict, Any
import uuid
from datetime import datetime

logger = logging.getLogger(__name__)

# Default flight configs embedded as Python dictionaries
DEFAULT_FLIGHT_CONFIGS = {
    "create_flight_config_flight_config": {
        "category": "meta",
        "description": "Meta-flight config that guides users through creating custom domain-specific flight configs",
        "payload_discovery": {
            "domain": "starlog_meta",
            "version": "1.0.0",
            "description": "Meta-flight config that guides users through creating custom flight configs",
            "directories": {},
            "root_files": [
                {
                    "sequence_number": 1,
                    "filename": "01_understand_domain.md",
                    "title": "Understand Your Domain and Workflow",
                    "content": """# Domain Analysis

## Your Domain
What specific area are you creating a flight config for?
- Research methodology?
- Debugging workflow?
- Documentation generation?
- Code review process?
- Testing strategy?

## Workflow Analysis
Describe your ideal workflow:
1. What are the key steps in your process?
2. Which steps are amplificatory (repeatable/improvable)?
3. What tools and files do you typically work with?
4. What outputs do you want to generate?

## Amplificatory vs One-Time
✅ Good for flight configs (amplificatory):
- "Review and improve code quality"
- "Research and synthesize findings"
- "Analyze and optimize performance"

❌ Not ideal (one-time tasks):
- "Write the user manual"
- "Fix this specific bug"
- "Create the database schema"

**Action**: Document your domain and workflow requirements above.""",
                    "piece_type": "instruction",
                    "dependencies": []
                },
                {
                    "sequence_number": 2,
                    "filename": "02_design_payloaddiscovery.md",
                    "title": "Design Your PayloadDiscovery Structure",
                    "content": """# PayloadDiscovery Design

## Template Structure
```json
{
  "domain": "your_domain",
  "version": "1.0.0",
  "description": "Brief description of what this workflow accomplishes",
  "directories": {},
  "root_files": [
    {
      "sequence_number": 1,
      "filename": "01_setup.md",
      "title": "Setup and Context",
      "content": "Instructions for initial setup...",
      "piece_type": "instruction",
      "dependencies": []
    },
    {
      "sequence_number": 2,
      "filename": "02_main_work.md",
      "title": "Core Workflow Step",
      "content": "Main amplificatory process...",
      "piece_type": "instruction",
      "dependencies": [1]
    },
    {
      "sequence_number": 3,
      "filename": "03_iterate.md",
      "title": "Review and Iterate",
      "content": "How to improve and continue...",
      "piece_type": "instruction",
      "dependencies": [2]
    }
  ],
  "entry_point": "01_setup.md"
}
```

## Design Principles
1. **Sequential**: Each step builds on previous steps
2. **Clear Instructions**: Each piece should be actionable
3. **Amplificatory**: Focus on processes that improve with repetition
4. **Dependencies**: Use sequence numbers to show step relationships

**Action**: Create your PayloadDiscovery JSON file based on your domain analysis.""",
                    "piece_type": "instruction",
                    "dependencies": [1]
                },
                {
                    "sequence_number": 3,
                    "filename": "03_create_pd_file.md",
                    "title": "Create and Validate PayloadDiscovery File",
                    "content": """# Create PayloadDiscovery File

## Steps
1. Create your PayloadDiscovery JSON file
2. Save it with a descriptive name: `/path/to/your_domain_pd.json`
3. Validate the structure

## Validation Checklist
- [ ] `domain` field describes your area
- [ ] `description` explains the workflow purpose
- [ ] `root_files` contains numbered sequence
- [ ] Each piece has `sequence_number`, `filename`, `title`, `content`
- [ ] Dependencies reference earlier sequence numbers
- [ ] Content provides actionable instructions
- [ ] Workflow is amplificatory (repeatable/improvable)

## Test Your PayloadDiscovery
You can test the structure using:
```bash
python -c 'import payload_discovery; pd = payload_discovery.PayloadDiscovery.from_json("your_file.json"); print(pd.validate_sequence())'
```

**Action**: Create and validate your PayloadDiscovery JSON file.""",
                    "piece_type": "instruction",
                    "dependencies": [2]
                },
                {
                    "sequence_number": 4,
                    "filename": "04_register_flight_config.md",
                    "title": "Register Your Flight Config",
                    "content": """# Register Flight Config

## Registration Command
Use the STARLOG MCP tool to register your flight config:

```python
starlog.add_flight_config(
    path="/your/project/path",
    name="your_domain_flight_config",  # Must end with _flight_config
    config_data={
        "description": "Your workflow description",
        "work_loop_subchain": "/path/to/your_domain_pd.json"
    },
    category="your_category"  # e.g., research, debugging, docs
)
```

## Naming Requirements
- Name MUST end with `_flight_config`
- Use descriptive prefixes: `research_methodology_flight_config`
- Categories help organize: research, debugging, docs, testing, etc.

## Test Your Flight Config
After registration:
1. `starlog.fly(path)` - Should show your new config
2. Test with a simple project to verify it works
3. Iterate and improve based on usage

**Action**: Register your flight config and test it.""",
                    "piece_type": "instruction",
                    "dependencies": [3]
                },
                {
                    "sequence_number": 5,
                    "filename": "05_iterate_and_improve.md",
                    "title": "Iterate and Improve Your Flight Config",
                    "content": """# Continuous Improvement

## Usage Feedback Loop
1. **Use** your flight config on real projects
2. **Observe** where the workflow breaks down or could be clearer
3. **Update** the PayloadDiscovery JSON with improvements
4. **Re-register** using `update_flight_config()`
5. **Share** successful patterns with the community

## Common Improvements
- **Clearer Instructions**: Add more detail to ambiguous steps
- **Better Dependencies**: Ensure steps build logically
- **Tool Integration**: Reference specific tools and commands
- **Output Templates**: Provide examples of expected outputs
- **Error Handling**: Include troubleshooting guidance

## Update Command
```python
starlog.update_flight_config(
    path="/your/project/path",
    name="your_domain_flight_config",
    config_data={
        "description": "Updated description",
        "work_loop_subchain": "/path/to/improved_pd.json"
    }
)
```

## Success Metrics
- Does the workflow feel natural to follow?
- Do you get better results each time you use it?
- Can others understand and use your flight config?
- Does it save time compared to ad-hoc approaches?

**Action**: Plan your improvement cycle and create a feedback loop.""",
                    "piece_type": "instruction",
                    "dependencies": [4]
                }
            ],
            "entry_point": "01_understand_domain.md"
        }
    }
}


def get_registry_path() -> Path:
    """Get the path to the STARLOG flight configs registry."""
    heaven_data_dir = os.getenv("HEAVEN_DATA_DIR")
    if not heaven_data_dir:
        raise ValueError("HEAVEN_DATA_DIR environment variable must be set")
    registry_path = Path(os.path.join(heaven_data_dir, "registry/starlog_flight_configs_registry.json"))
    return registry_path


def load_registry() -> Dict[str, Any]:
    """Load the existing flight configs registry if it exists."""
    registry_path = get_registry_path()
    
    if registry_path.exists():
        try:
            with open(registry_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load registry: {e}", exc_info=True)
            return {}
    
    # Create registry directory if it doesn't exist
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    return {}


def save_registry(registry: Dict[str, Any]) -> None:
    """Save the registry to disk."""
    registry_path = get_registry_path()
    
    try:
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        with open(registry_path, 'w') as f:
            json.dump(registry, f, indent=2)
        logger.info(f"Registry saved to {registry_path}")
    except Exception as e:
        logger.exception(f"Failed to save registry: {e}")


def create_payload_discovery_file(name: str, config: Dict[str, Any]) -> str:
    """Create a PayloadDiscovery JSON file and return its path."""
    heaven_data_dir = os.getenv("HEAVEN_DATA_DIR")
    if not heaven_data_dir:
        raise ValueError("HEAVEN_DATA_DIR environment variable must be set")
    pd_dir = Path(os.path.join(heaven_data_dir, "default_flight_configs"))
    pd_dir.mkdir(parents=True, exist_ok=True)
    
    pd_file = pd_dir / f"{name}_pd.json"
    
    try:
        with open(pd_file, 'w') as f:
            json.dump(config["payload_discovery"], f, indent=2)
        logger.info(f"Created PayloadDiscovery file: {pd_file}")
        return str(pd_file)
    except Exception as e:
        logger.exception(f"Failed to create PayloadDiscovery file: {e}")
        return None


def register_flight_config(name: str, config: Dict[str, Any], pd_path: str) -> Dict[str, Any]:
    """Create a flight config registry entry."""
    config_id = str(uuid.uuid4())
    
    entry = {
        "id": config_id,
        "name": name,
        "original_project_path": "SYSTEM_DEFAULT",
        "category": config["category"],
        "description": config["description"],
        "work_loop_subchain": pd_path,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    
    return entry


def auto_populate_defaults() -> str:
    """
    Auto-populate default flight configs for STARSHIP.
    
    Returns:
        Status message indicating success or failure
    """
    try:
        logger.info("Starting STARSHIP flight config auto-population...")
        
        # Load existing registry
        registry = load_registry()
        
        populated = []
        skipped = []
        
        for name, config in DEFAULT_FLIGHT_CONFIGS.items():
            # Check if already exists
            existing = any(entry.get("name") == name for entry in registry.values())
            if existing:
                skipped.append(name)
                logger.info(f"Flight config '{name}' already exists, skipping...")
                continue
            
            # Create PayloadDiscovery file
            pd_path = create_payload_discovery_file(name, config)
            if not pd_path:
                logger.error(f"Failed to create PayloadDiscovery file for {name}")
                continue
            
            # Register the flight config
            entry = register_flight_config(name, config, pd_path)
            registry[entry["id"]] = entry
            populated.append(name)
            logger.info(f"Registered flight config: {name}")
        
        # Save updated registry
        if populated:
            save_registry(registry)
        
        # Prepare status message
        status_parts = []
        if populated:
            status_parts.append(f"✅ Auto-populated {len(populated)} flight configs: {', '.join(populated)}")
        if skipped:
            status_parts.append(f"⏭️ Skipped {len(skipped)} existing configs: {', '.join(skipped)}")
        if not populated and not skipped:
            status_parts.append("❌ No flight configs to populate")
        
        status = "\n".join(status_parts)
        logger.info(f"Auto-population complete: {status}")
        return status
        
    except Exception as e:
        error_msg = f"Failed to auto-populate flight configs: {e}"
        logger.error(error_msg)
        return f"❌ {error_msg}"