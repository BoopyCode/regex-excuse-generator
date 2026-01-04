#!/usr/bin/env python3
import random

# Regex Excuse Generator - Because sometimes the problem isn't you, it's the universe
# (or at least that's what we tell management)

def generate_excuse():
    """Generate a plausible-sounding excuse for regex failure.
    Returns: A string that sounds technical enough to fool non-technical people.
    """
    
    # The secret sauce: mix and match these components
    problems = [
        "unicode normalization issue",
        "edge case with whitespace characters",
        "timezone-aware datetime formatting",
        "legacy encoding mismatch",
        "browser-specific character rendering",
        "internationalization edge case",
        "mobile keyboard input variation",
        "copy-paste formatting artifacts",
        "CMS auto-formatting interference",
        "email client sanitization"
    ]
    
    causes = [
        "an undocumented API change",
        "a recent library update",
        "unexpected user behavior",
        "third-party service modifications",
        "caching layer interference",
        "CDN configuration differences",
        "browser update side effects",
        "operating system regional settings",
        "accessibility tool interactions",
        "security policy enforcement"
    ]
    
    solutions = [
        "adding additional validation layers",
        "implementing a more robust parsing strategy",
        "creating a custom normalization pipeline",
        "deploying a targeted hotfix",
        "updating our character encoding standards",
        "adding comprehensive logging for future incidents",
        "coordinating with external service providers",
        "scheduling a refactor in the next sprint",
        "documenting this as a known limitation",
        "implementing a graceful degradation fallback"
    ]
    
    templates = [
        "The regex failed due to {problem} caused by {cause}. We're addressing this by {solution}.",
        "We encountered {problem} because of {cause}. The fix involves {solution}.",
        "{problem} occurred due to {cause}. We'll resolve this through {solution}.",
        "The issue was {problem} triggered by {cause}. Our solution: {solution}."
    ]
    
    # Mix and match for maximum plausibility
    excuse = random.choice(templates).format(
        problem=random.choice(problems),
        cause=random.choice(causes),
        solution=random.choice(solutions)
    )
    
    return excuse

if __name__ == "__main__":
    # When your regex fails but your excuses shouldn't
    print("\n🔧 Regex Failure Excuse Generator 🔧\n")
    print("Here's your professionally crafted excuse:")
    print("-" * 50)
    print(generate_excuse())
    print("-" * 50)
    print("\n(Use responsibly. Or don't. We're not your manager.)\n")
